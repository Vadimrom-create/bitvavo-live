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
from research.solaire_v3 import HORIZONS_HOURS
from research.solaire_v31 import FROZEN_V3_COMMIT, V3_TIMING_LAB_COMMIT
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
    errors: list[dict[str, Any]] = []
    critical = None
    total_new = 0

    try:
        client = PublicClient(timeout=10, retries=2, requests_per_second=8)
        client.get("/time", cache=False)
        total_new = _evaluate_event_collection(
            client,
            events,
            now,
            MAX_NEW_EVALUATIONS_PER_RUN,
            errors,
        )
    except Exception as exc:
        critical = type(exc).__name__ + ":" + str(exc)

    qualified = _eligible(events, "V31_QUALIFIED_ENTRY")
    rejected = _eligible(events, "V31_REJECTED_READY")
    persist_qualified = _eligible(events, "V31_PERSIST_30M_QUALIFIED_ENTRY")
    persist_rejected = _eligible(events, "V31_PERSIST_30M_REJECTED_READY")
    reclaim_qualified = _eligible(events, "V31_PULLBACK_RECLAIM_QUALIFIED_ENTRY")
    reclaim_rejected = _eligible(events, "V31_PULLBACK_RECLAIM_REJECTED_READY")

    def v3_window(event_type: str) -> list[dict[str, Any]]:
        out = []
        for event in v3.get("events", []) or []:
            if event.get("event_type") != event_type or event.get("left_censored_at_v3_t0"):
                continue
            ts = finite(event.get("decision_ts"))
            if start_ts is not None and ts is not None and ts >= start_ts:
                out.append(event)
        return out

    v3_raw = v3_window("ENTRY_READY_SHADOW")
    v3_persist = v3_window("ENTRY_TIMING_PERSIST_30M")
    v3_reclaim = v3_window("ENTRY_TIMING_PULLBACK_RECLAIM")

    summary = {
        "v31_raw_qualified": {str(h): _summary(qualified, "V31_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_raw_rejected": {str(h): _summary(rejected, "V31_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_persist30_qualified": {str(h): _summary(persist_qualified, "V31_PERSIST_30M_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_persist30_rejected": {str(h): _summary(persist_rejected, "V31_PERSIST_30M_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v31_pullback_reclaim_qualified": {str(h): _summary(reclaim_qualified, "V31_PULLBACK_RECLAIM_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_pullback_reclaim_rejected": {str(h): _summary(reclaim_rejected, "V31_PULLBACK_RECLAIM_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v3_raw_same_window": {str(h): _summary(v3_raw, "ENTRY_READY_SHADOW", h) for h in HORIZONS_HOURS},
        "v3_persist30_same_window": {str(h): _summary(v3_persist, "ENTRY_TIMING_PERSIST_30M", h) for h in HORIZONS_HOURS},
        "v3_pullback_reclaim_same_window": {str(h): _summary(v3_reclaim, "ENTRY_TIMING_PULLBACK_RECLAIM", h) for h in HORIZONS_HOURS},
    }

    comparison = {
        "schema": "solaire_v31_vs_frozen_v3_comparison_v1",
        "checked_at_utc": utc(now),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "method": "factorial shadow: V3 raw/persist/reclaim crossed with unchanged V3.1 economic gate; strict complete horizons",
        "horizons_hours": list(HORIZONS_HOURS),
        "summary": summary,
        "score_calibration": {
            "raw": {str(h): _score_bins(qualified, h) for h in (4, 24, 48, 96)},
            "persist30": {str(h): _score_bins(persist_qualified, h) for h in (4, 24, 48, 96)},
            "pullback_reclaim": {str(h): _score_bins(reclaim_qualified, h) for h in (4, 24, 48, 96)},
        },
        "factorial_axes": {
            "ranking": ["V3", "V3.1_ECONOMIC_GATE"],
            "timing": ["RAW", "PERSIST_30M", "PULLBACK_RECLAIM"],
        },
        "warning": "Pre-V3.1 NIL/APE/FORM outcomes motivated the hypotheses but are excluded from prospective V3.1 performance.",
    }
    status = {
        "schema": "solaire_v31_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical else ("OK_WITH_SOURCE_GAPS" if errors else "OK"),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "new_complete_evaluations": total_new,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "qualified_events": len(qualified),
        "rejected_ready_events": len(rejected),
        "persist30_qualified_events": len(persist_qualified),
        "persist30_rejected_events": len(persist_rejected),
        "pullback_reclaim_qualified_events": len(reclaim_qualified),
        "pullback_reclaim_rejected_events": len(reclaim_rejected),
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
