#!/usr/bin/env python3
"""Prospective outcome evaluator for the V3.1 economic challenger."""
from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.solaire_v3 import HORIZONS_HOURS, V3_ARCHITECTURE_VERSION
from research.solaire_v31 import FROZEN_V3_COMMIT, V31_ARCHITECTURE_VERSION, V3_TIMING_LAB_COMMIT
from scripts.update_solaire_v3_evaluation import _evaluate_event_collection, _summary

V31_JOURNAL = "solaire_v31_journal.json"
V3_JOURNAL = "solaire_v3_journal.json"
STATUS = "solaire_v31_evaluation_status.json"
COMPARISON = "solaire_v31_comparison.json"
MAX_NEW_EVALUATIONS_PER_RUN = 24


def _eligible(events: list[dict[str, Any]], event_type: str, start_ts: float | None = None) -> list[dict[str, Any]]:
    out = []
    for event in events:
        if event.get("event_type") != event_type:
            continue
        if event.get("left_censored_at_v31_t0") or event.get("left_censored_at_v31_timing_t0"):
            continue
        ts = finite(event.get("decision_ts"))
        if start_ts is not None and (ts is None or ts < start_ts):
            continue
        out.append(event)
    return out


def _eligible_path(
    events: list[dict[str, Any]],
    event_type: str,
    entry_path: str,
    start_ts: float | None = None,
) -> list[dict[str, Any]]:
    return [
        x for x in _eligible(events, event_type, start_ts)
        if (x.get("entry_path") or "RAW") == entry_path
    ]


def _selectable_recovery_summary(events: list[dict[str, Any]]) -> dict[str, Any]:
    rows = _eligible(events, "OPPORTUNITY_RECOVERY_SELECTABLE")
    def med(values: list[float]) -> float | None:
        return None if not values else round(statistics.median(values), 4)
    credible_to_selectable = []
    executable_to_selectable = []
    consumed = []
    scores = []
    records = []
    for event in rows:
        funnel = event.get("funnel") or {}
        delay = finite(funnel.get("credible_to_selectable_delay_seconds"))
        exec_delay = finite(funnel.get("executable_to_selectable_delay_seconds"))
        move = finite(funnel.get("movement_consumed_to_selectable_pct"))
        score = finite(event.get("economic_score"))
        if delay is not None:
            credible_to_selectable.append(delay / 60.0)
        if exec_delay is not None:
            executable_to_selectable.append(exec_delay / 60.0)
        if move is not None:
            consumed.append(move)
        if score is not None:
            scores.append(score)
        records.append({
            "market": event.get("market"),
            "entry_path": event.get("entry_path"),
            "first_credible_at_utc": funnel.get("first_credible_at_utc"),
            "first_entry_hypothesis_at_utc": funnel.get("first_entry_hypothesis_at_utc"),
            "first_executable_at_utc": funnel.get("first_executable_at_utc"),
            "first_selectable_at_utc": funnel.get("first_selectable_at_utc"),
            "first_credible_price_eur": funnel.get("first_credible_price_eur"),
            "first_executable_entry_eur": funnel.get("first_executable_entry_eur"),
            "first_selectable_entry_eur": funnel.get("first_selectable_entry_eur"),
            "credible_to_selectable_minutes": None if delay is None else round(delay / 60.0, 3),
            "executable_to_selectable_minutes": None if exec_delay is None else round(exec_delay / 60.0, 3),
            "movement_consumed_to_selectable_pct": move,
            "economic_score": score,
        })
    return {
        "n": len(rows),
        "median_credible_to_selectable_minutes": med(credible_to_selectable),
        "median_executable_to_selectable_minutes": med(executable_to_selectable),
        "median_movement_consumed_to_selectable_pct": med(consumed),
        "median_first_selectable_score": med(scores),
        "records": records[-300:],
    }


def _score_bins(events: list[dict[str, Any]], horizon: int) -> list[dict[str, Any]]:
    bins = [(6.0, 7.0), (7.0, 8.0), (8.0, 9.0), (9.0, 10.01)]
    out = []
    for low, high in bins:
        rows = []
        for event in events:
            score = finite(event.get("economic_score"))
            ev = (event.get("evaluations") or {}).get(str(horizon))
            if score is None or not (low <= score < high) or not ev or not ev.get("complete_horizon"):
                continue
            rows.append(ev)
        returns = [finite(x.get("net_close_return_pct_est")) for x in rows if finite(x.get("net_close_return_pct_est")) is not None]
        out.append({
            "score_low": low,
            "score_high": high,
            "n": len(rows),
            "mean_net_close_return_pct_est": None if not returns else round(statistics.mean(returns), 4),
            "mfe_ge_10pct": sum(bool(x.get("mfe_ge_10pct")) for x in rows),
            "stop_hits": sum(bool(x.get("stop_hit")) for x in rows),
        })
    return out


def main() -> int:
    now = time.time()
    v31 = read_json(V31_JOURNAL, {}) or {}
    v3 = read_json(V3_JOURNAL, {}) or {}
    start_ts = finite(v31.get("started_ts"))
    events = v31.get("events", []) or []
    current_events = [x for x in events if x.get("architecture_version") == V31_ARCHITECTURE_VERSION]
    legacy_events = [x for x in events if x.get("architecture_version") != V31_ARCHITECTURE_VERSION]
    errors: list[dict[str, Any]] = []
    critical = None
    total_new = 0

    try:
        client = PublicClient(timeout=10, retries=2, requests_per_second=8)
        client.get("/time", cache=False)
        budget = MAX_NEW_EVALUATIONS_PER_RUN
        added = _evaluate_event_collection(client, current_events, now, budget, errors)
        total_new += added
        budget -= added
        if budget > 0:
            added = _evaluate_event_collection(client, legacy_events, now, budget, errors)
            total_new += added
    except Exception as exc:
        critical = type(exc).__name__ + ":" + str(exc)

    qualified = _eligible(current_events, "V31_QUALIFIED_ENTRY")
    rejected = _eligible(current_events, "V31_REJECTED_READY")
    raw_qualified = _eligible_path(current_events, "V31_QUALIFIED_ENTRY", "RAW")
    raw_rejected = _eligible_path(current_events, "V31_REJECTED_READY", "RAW")
    reentry_qualified = _eligible_path(current_events, "V31_QUALIFIED_ENTRY", "THESIS_REENTRY")
    reentry_rejected = _eligible_path(current_events, "V31_REJECTED_READY", "THESIS_REENTRY")
    persist_qualified = _eligible(current_events, "V31_PERSIST_30M_QUALIFIED_ENTRY")
    persist_rejected = _eligible(current_events, "V31_PERSIST_30M_REJECTED_READY")
    reclaim_qualified = _eligible(current_events, "V31_PULLBACK_RECLAIM_QUALIFIED_ENTRY")
    reclaim_rejected = _eligible(current_events, "V31_PULLBACK_RECLAIM_REJECTED_READY")
    recovery_selectable = _eligible(current_events, "OPPORTUNITY_RECOVERY_SELECTABLE")

    def v3_window(event_type: str) -> list[dict[str, Any]]:
        out = []
        for event in v3.get("events", []) or []:
            if event.get("event_type") != event_type or event.get("left_censored_at_v3_t0"):
                continue
            if event.get("architecture_version") != V3_ARCHITECTURE_VERSION:
                continue
            ts = finite(event.get("decision_ts"))
            if start_ts is not None and ts is not None and ts >= start_ts:
                out.append(event)
        return out

    v3_raw = v3_window("ENTRY_READY_SHADOW")
    v3_persist = v3_window("ENTRY_TIMING_PERSIST_30M")
    v3_reclaim = v3_window("ENTRY_TIMING_PULLBACK_RECLAIM")

    summary = {
        "v31_raw_qualified": {str(h): _summary(raw_qualified, "V31_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_raw_rejected": {str(h): _summary(raw_rejected, "V31_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_reentry_qualified": {str(h): _summary(reentry_qualified, "V31_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_reentry_rejected": {str(h): _summary(reentry_rejected, "V31_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_persist30_qualified": {str(h): _summary(persist_qualified, "V31_PERSIST_30M_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_persist30_rejected": {str(h): _summary(persist_rejected, "V31_PERSIST_30M_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_pullback_reclaim_qualified": {str(h): _summary(reclaim_qualified, "V31_PULLBACK_RECLAIM_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_pullback_reclaim_rejected": {str(h): _summary(reclaim_rejected, "V31_PULLBACK_RECLAIM_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_opportunity_recovery_selectable": {str(h): _summary(recovery_selectable, "OPPORTUNITY_RECOVERY_SELECTABLE", h) for h in HORIZONS_HOURS},
        "v3_raw_same_window": {str(h): _summary(v3_raw, "ENTRY_READY_SHADOW", h) for h in HORIZONS_HOURS},
        "v3_persist30_same_window": {str(h): _summary(v3_persist, "ENTRY_TIMING_PERSIST_30M", h) for h in HORIZONS_HOURS},
        "v3_pullback_reclaim_same_window": {str(h): _summary(v3_reclaim, "ENTRY_TIMING_PULLBACK_RECLAIM", h) for h in HORIZONS_HOURS},
    }

    comparison = {
        "schema": "solaire_v31_vs_frozen_v3_comparison_v1",
        "checked_at_utc": utc(now),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "architecture_version": V31_ARCHITECTURE_VERSION,
        "upstream_v3_architecture_version": V3_ARCHITECTURE_VERSION,
        "architecture_scope": "CURRENT_VERSION_ONLY",
        "legacy_v31_event_count_excluded_from_summary": len(legacy_events),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "frozen_v3_commit_role": "BENCHMARK_ONLY_NOT_LIVE_INPUT",
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "method": "factorial shadow: V3 raw/persist/reclaim crossed with unchanged V3.1 economic gate; strict complete horizons",
        "horizons_hours": list(HORIZONS_HOURS),
        "summary": summary,
        "near_miss_funnel": _selectable_recovery_summary(current_events),
        "score_calibration": {
            "raw": {str(h): _score_bins(raw_qualified, h) for h in (4, 24, 48, 96)},
            "reentry": {str(h): _score_bins(reentry_qualified, h) for h in (4, 24, 48, 96)},
            "persist30": {str(h): _score_bins(persist_qualified, h) for h in (4, 24, 48, 96)},
            "pullback_reclaim": {str(h): _score_bins(reclaim_qualified, h) for h in (4, 24, 48, 96)},
        },
        "factorial_axes": {
            "ranking": ["V3", "V3.1_ECONOMIC_GATE"],
            "timing": ["RAW", "THESIS_REENTRY", "PERSIST_30M", "PULLBACK_RECLAIM"],
        },
        "warning": "Pre-V3.1 NIL/APE/FORM outcomes motivated the hypotheses but are excluded from prospective V3.1 performance.",
    }
    status = {
        "schema": "solaire_v31_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical else ("OK_WITH_SOURCE_GAPS" if errors else "OK"),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "architecture_version": V31_ARCHITECTURE_VERSION,
        "upstream_v3_architecture_version": V3_ARCHITECTURE_VERSION,
        "current_architecture_events": len(current_events),
        "legacy_v31_events": len(legacy_events),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "frozen_v3_commit_role": "BENCHMARK_ONLY_NOT_LIVE_INPUT",
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "new_complete_evaluations": total_new,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "qualified_events": len(qualified),
        "rejected_ready_events": len(rejected),
        "raw_qualified_events": len(raw_qualified),
        "raw_rejected_events": len(raw_rejected),
        "reentry_qualified_events": len(reentry_qualified),
        "reentry_rejected_events": len(reentry_rejected),
        "persist30_qualified_events": len(persist_qualified),
        "persist30_rejected_events": len(persist_rejected),
        "pullback_reclaim_qualified_events": len(reclaim_qualified),
        "pullback_reclaim_rejected_events": len(reclaim_rejected),
        "opportunity_recovery_selectable_events": len(recovery_selectable),
        "v3_raw_same_window_events": len(v3_raw),
        "v3_persist30_same_window_events": len(v3_persist),
        "v3_pullback_reclaim_same_window_events": len(v3_reclaim),
        "critical_error": critical,
        "errors": errors[:40],
        "affects_v3": False,
        "affects_v2": False,
        "affects_email": False,
    }

    v31["updated_at_utc"] = utc(now)
    atomic_json(V31_JOURNAL, v31)
    atomic_json(COMPARISON, comparison)
    atomic_json(STATUS, status)
    print("SOLAIRE_V31_EVALUATION " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
