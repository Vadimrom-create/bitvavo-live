#!/usr/bin/env python3
"""Strict prospective evaluator for Solaire V3 and the frozen V2 reference.

The evaluator is intentionally independent from detection.  It fixes the main
measurement defects found by Astra: chronological sorting, cumulative cohorts,
strict start/end horizon coverage and no premature "complete" horizon.
"""
from __future__ import annotations

import json
import math
import statistics
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import INTERVAL_MS, atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.solaire_v3 import FROZEN_V2_COMMIT, HORIZONS_HOURS, V3_ARCHITECTURE_VERSION, evaluate_candles_strict

V3_JOURNAL = "solaire_v3_journal.json"
V2_BENCHMARK = "solaire_v2_frozen_benchmark_journal.json"
V2_DECISIONS = "production_decision_journal.json"
V2_OUTCOMES = "solaire_v2_reference_outcomes.json"
STATUS = "solaire_v3_evaluation_status.json"
COMPARISON = "solaire_v3_comparison.json"
MAX_NEW_EVALUATIONS_PER_RUN = 40


def _interval_for_horizon(hours: int) -> str:
    if hours <= 24:
        return "5m"
    if hours <= 96:
        return "15m"
    if hours <= 336:
        return "1h"
    return "4h"


def _canonical_bounded(raw: list[Any], interval: str, first_start: int, last_start: int) -> list[dict[str, Any]]:
    """Canonicalize a bounded Bitvavo response without the 100-bar feature trim."""
    duration = INTERVAL_MS[interval]
    observed: dict[int, dict[str, Any]] = {}
    for r in raw:
        if not isinstance(r, list) or len(r) < 6:
            continue
        vals = [finite(x) for x in r[:6]]
        if any(x is None for x in vals):
            continue
        t, o, h, l, c, v = vals
        t = int(t)
        if t % duration or min(o, h, l, c) <= 0 or v < 0:
            continue
        observed[t] = {"t": t, "o": o, "h": h, "l": l, "c": c, "v": v, "bar_status": "CLOSED_TRADE"}

    anchors = [t for t in observed if t <= first_start]
    if not anchors:
        return []
    anchor = max(anchors)
    previous_close = observed[anchor]["c"]
    out = []
    t = anchor
    while t <= last_start:
        row = observed.get(t)
        if row is not None:
            previous_close = row["c"]
        else:
            row = {
                "t": t, "o": previous_close, "h": previous_close,
                "l": previous_close, "c": previous_close, "v": 0.0,
                "bar_status": "NO_TRADE",
            }
        if t >= first_start:
            out.append(row)
        t += duration
    return out


def _fetch_evaluation(
    client: PublicClient,
    market: str,
    baseline: float,
    decision_ts: float,
    horizon: int,
    stop_eur: float | None,
) -> dict[str, Any] | None:
    interval = _interval_for_horizon(horizon)
    duration = INTERVAL_MS[interval]
    first_start = ((int(decision_ts * 1000) // duration) + 1) * duration
    horizon_end = int((decision_ts + horizon * 3600) * 1000)
    last_start = (horizon_end // duration) * duration
    if last_start + duration > horizon_end:
        last_start -= duration
    if last_start < first_start:
        return None
    params = {
        "interval": interval,
        "start": max(0, first_start - duration),
        "end": horizon_end,
        "limit": 1000,
    }
    raw = client.get("/" + market + "/candles", params, cache=False)
    candles = _canonical_bounded(raw, interval, first_start, last_start)
    result = evaluate_candles_strict(
        baseline,
        decision_ts,
        candles,
        horizon,
        interval_ms=duration,
        stop_eur=stop_eur,
    )
    if result is not None:
        result["interval"] = interval
        result["source_window_start_ms"] = params["start"]
        result["source_window_end_ms"] = params["end"]
    return result


def _baseline_for_event(event: dict[str, Any]) -> float | None:
    for key in ("entry_eur", "price_eur", "signal_price_eur"):
        value = finite(event.get(key))
        if value is not None and value > 0:
            return value
    return None


def _due(event: dict[str, Any], now: float) -> list[int]:
    ts = finite(event.get("decision_ts"))
    if ts is None:
        return []
    evaluations = event.setdefault("evaluations", {})
    return [
        h for h in HORIZONS_HOURS
        if str(h) not in evaluations and now >= ts + h * 3600
    ]


def _summary(
    events: list[dict[str, Any]],
    event_type: str,
    horizon: int,
    *,
    architecture_version: str | None = None,
) -> dict[str, Any]:
    rows = []
    for event in events:
        if event.get("event_type") != event_type or event.get("left_censored_at_v3_t0"):
            continue
        if architecture_version is not None and event.get("architecture_version") != architecture_version:
            continue
        ev = (event.get("evaluations") or {}).get(str(horizon))
        if ev and ev.get("complete_horizon"):
            rows.append(ev)
    def vals(key: str) -> list[float]:
        return [finite(x.get(key)) for x in rows if finite(x.get(key)) is not None]
    def med(xs: list[float]) -> float | None:
        return round(statistics.median(xs), 4) if xs else None
    def mean(xs: list[float]) -> float | None:
        return round(statistics.mean(xs), 4) if xs else None
    return {
        "n": len(rows),
        "mean_net_close_return_pct_est": mean(vals("net_close_return_pct_est")),
        "median_net_close_return_pct_est": med(vals("net_close_return_pct_est")),
        "median_mfe_pct": med(vals("mfe_pct")),
        "median_mae_pct": med(vals("mae_pct")),
        "mfe_ge_10pct": sum(bool(x.get("mfe_ge_10pct")) for x in rows),
        "mfe_ge_20pct": sum(bool(x.get("mfe_ge_20pct")) for x in rows),
        "mfe_ge_50pct": sum(bool(x.get("mfe_ge_50pct")) for x in rows),
        "mfe_ge_100pct": sum(bool(x.get("mfe_ge_100pct")) for x in rows),
        "stop_hits": sum(bool(x.get("stop_hit")) for x in rows),
    }


def _evaluate_event_collection(
    client: PublicClient,
    events: list[dict[str, Any]],
    now: float,
    budget: int,
    errors: list[dict[str, Any]],
) -> int:
    completed = 0
    # Oldest due decisions first so long-horizon cohorts cannot be starved.
    ordered = sorted(events, key=lambda x: finite(x.get("decision_ts"), now))
    for event in ordered:
        if completed >= budget:
            break
        baseline = _baseline_for_event(event)
        decision_ts = finite(event.get("decision_ts"))
        market = event.get("market")
        if baseline is None or decision_ts is None or not market:
            continue
        for horizon in _due(event, now):
            if completed >= budget:
                break
            try:
                result = _fetch_evaluation(
                    client, market, baseline, decision_ts, horizon, finite(event.get("stop_eur"))
                )
                if result is not None and result.get("complete_horizon"):
                    event.setdefault("evaluations", {})[str(horizon)] = result
                    completed += 1
            except Exception as exc:
                errors.append({
                    "market": market, "event_type": event.get("event_type"),
                    "horizon": horizon, "reason": type(exc).__name__ + ":" + str(exc),
                })
    return completed


def _v2_buy_reference(decisions: dict[str, Any], outcomes: dict[str, Any], v3_start: float) -> list[dict[str, Any]]:
    outcomes.setdefault("schema", "solaire_v2_reference_outcomes_v1")
    outcomes.setdefault("events", [])
    existing = {
        (x.get("cycle_id"), x.get("market"))
        for x in outcomes["events"]
    }
    for row in decisions.get("entries", []) or []:
        if row.get("decision_type") != "BUY_SENT":
            continue
        ts = finite(row.get("decision_ts"))
        if ts is None or ts < v3_start:
            continue
        key = (row.get("cycle_id"), row.get("market"))
        if key in existing:
            continue
        outcomes["events"].append({
            "event_type": "V2_BUY_SENT",
            "cycle_id": row.get("cycle_id"),
            "market": row.get("market"),
            "decision_ts": ts,
            "decision_at_utc": utc(ts),
            "entry_eur": finite(row.get("entry_eur")) or finite(row.get("signal_price_eur")),
            "stop_eur": finite(row.get("stop_eur")),
            "tp1_eur": finite(row.get("tp1_eur")),
            "stake_eur": finite(row.get("stake_eur")),
            "signal_score": finite(row.get("signal_score")),
            "evaluations": {},
        })
        existing.add(key)
    return outcomes["events"]


def _prewatch_leads(v3_events: list[dict[str, Any]], v2_events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    detections = [
        x for x in v2_events
        if x.get("event_type") == "V2_FIRST_DETECTION"
        and not x.get("left_censored_at_v3_t0")
    ]
    out = []
    for event in v3_events:
        if event.get("event_type") != "PREWATCH_CONTEXT" or event.get("left_censored_at_v3_t0"):
            continue
        t0 = finite(event.get("decision_ts"))
        if t0 is None:
            continue
        matches = [
            x for x in detections
            if x.get("market") == event.get("market")
            and finite(x.get("decision_ts")) is not None
            and t0 <= finite(x.get("decision_ts")) <= t0 + 24 * 3600
        ]
        if not matches:
            continue
        later = min(matches, key=lambda x: finite(x.get("decision_ts"), 1e30))
        dt = finite(later.get("decision_ts")) - t0
        p0 = finite(event.get("price_eur"))
        p1 = finite(later.get("price_eur"))
        price_delta = None if not p0 or p1 is None else (p1 / p0 - 1.0) * 100.0
        out.append({
            "market": event.get("market"),
            "v3_prewatch_at_utc": event.get("decision_at_utc"),
            "v2_first_detection_at_utc": later.get("decision_at_utc"),
            "lead_minutes": round(dt / 60.0, 2),
            "price_change_before_v2_detection_pct": None if price_delta is None else round(price_delta, 4),
        })
    return out


def main() -> int:
    now = time.time()
    v3 = read_json(V3_JOURNAL, {}) or {}
    benchmark = read_json(V2_BENCHMARK, {}) or {}
    decisions = read_json(V2_DECISIONS, {}) or {}
    outcomes = read_json(V2_OUTCOMES, {}) or {}
    errors: list[dict[str, Any]] = []

    v3_start = finite(v3.get("started_ts"), now)
    v2_buy_events = _v2_buy_reference(decisions, outcomes, v3_start)
    current_v3_events = [
        x for x in v3.get("events", [])
        if x.get("architecture_version") == V3_ARCHITECTURE_VERSION
    ]
    legacy_v3_events = [
        x for x in v3.get("events", [])
        if x.get("architecture_version") != V3_ARCHITECTURE_VERSION
    ]

    client = PublicClient(timeout=10, retries=2, requests_per_second=8)
    critical = None
    total_new = 0
    try:
        client.get("/time", cache=False)
        budget = MAX_NEW_EVALUATIONS_PER_RUN
        added = _evaluate_event_collection(client, current_v3_events, now, budget, errors)
        total_new += added
        budget -= added
        if budget > 0:
            added = _evaluate_event_collection(client, legacy_v3_events, now, budget, errors)
            total_new += added
            budget -= added
        if budget > 0:
            added = _evaluate_event_collection(client, benchmark.get("events", []), now, budget, errors)
            total_new += added
            budget -= added
        if budget > 0:
            added = _evaluate_event_collection(client, v2_buy_events, now, budget, errors)
            total_new += added
    except Exception as exc:
        critical = type(exc).__name__ + ":" + str(exc)

    v3["updated_at_utc"] = utc(now)
    benchmark["updated_at_utc"] = utc(now)
    outcomes["updated_at_utc"] = utc(now)
    outcomes["frozen_v2_commit"] = FROZEN_V2_COMMIT

    summary = {
        "v3_prewatch": {str(h): _summary(current_v3_events, "PREWATCH_CONTEXT", h) for h in HORIZONS_HOURS},
        "v3_entry_ready": {str(h): _summary(current_v3_events, "ENTRY_READY_SHADOW", h) for h in HORIZONS_HOURS},
        "v3_timing_persist_30m": {str(h): _summary(current_v3_events, "ENTRY_TIMING_PERSIST_30M", h) for h in HORIZONS_HOURS},
        "v3_timing_pullback_reclaim": {str(h): _summary(current_v3_events, "ENTRY_TIMING_PULLBACK_RECLAIM", h) for h in HORIZONS_HOURS},
        "v3_thesis_start": {str(h): _summary(current_v3_events, "OPPORTUNITY_THESIS_START", h) for h in HORIZONS_HOURS},
        "v3_thesis_reentry_ready": {str(h): _summary(current_v3_events, "OPPORTUNITY_THESIS_REENTRY_READY", h) for h in HORIZONS_HOURS},
        "v3_thesis_reentry_entry": {str(h): _summary(current_v3_events, "ENTRY_THESIS_REENTRY_SHADOW", h) for h in HORIZONS_HOURS},
        "v2_first_detection": {str(h): _summary(benchmark.get("events", []), "V2_FIRST_DETECTION", h) for h in HORIZONS_HOURS},
        "v2_buy_sent": {str(h): _summary(v2_buy_events, "V2_BUY_SENT", h) for h in HORIZONS_HOURS},
    }
    leads = _prewatch_leads(current_v3_events, benchmark.get("events", []))
    lead_values = [finite(x.get("lead_minutes")) for x in leads if finite(x.get("lead_minutes")) is not None]

    comparison = {
        "schema": "solaire_v3_vs_v2_comparison_v1",
        "checked_at_utc": utc(now),
        "prospective_started_at_utc": v3.get("started_at_utc"),
        "architecture_version": V3_ARCHITECTURE_VERSION,
        "architecture_scope": "CURRENT_VERSION_ONLY_FOR_V3_SUMMARIES",
        "legacy_v3_event_count_excluded_from_summary": len(legacy_v3_events),
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "method": "same-market prospective events; strict chronological complete horizons; 0.70% round-trip cost estimate",
        "horizons_hours": list(HORIZONS_HOURS),
        "summary": summary,
        "prewatch_vs_v2_detection": {
            "paired_n": len(leads),
            "median_lead_minutes": None if not lead_values else round(statistics.median(lead_values), 2),
            "pairs": leads[-200:],
        },
        "entry_timing_lab": {"raw": "ENTRY_READY_SHADOW", "persist_30m": "ENTRY_TIMING_PERSIST_30M", "pullback_reclaim": "ENTRY_TIMING_PULLBACK_RECLAIM"},
        "persistent_thesis_lab": {
            "opportunity_start": "OPPORTUNITY_THESIS_START",
            "reentry_state": "OPPORTUNITY_THESIS_REENTRY_READY",
            "reentry_executable": "ENTRY_THESIS_REENTRY_SHADOW",
            "affects_existing_rotation": False,
        },
        "warning": "This is a shadow comparison, not actual account PnL or proof of causal edge.",
    }
    status = {
        "schema": "solaire_v3_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical else ("OK_WITH_SOURCE_GAPS" if errors else "OK"),
        "prospective_started_at_utc": v3.get("started_at_utc"),
        "architecture_version": V3_ARCHITECTURE_VERSION,
        "current_architecture_events": len(current_v3_events),
        "legacy_v3_events": len(legacy_v3_events),
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "new_complete_evaluations": total_new,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "v3_events": len(v3.get("events", [])),
        "v2_benchmark_events": len(benchmark.get("events", [])),
        "v2_buy_reference_events": len(v2_buy_events),
        "critical_error": critical,
        "errors": errors[:40],
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
    }

    atomic_json(V3_JOURNAL, v3)
    atomic_json(V2_BENCHMARK, benchmark)
    atomic_json(V2_OUTCOMES, outcomes)
    atomic_json(COMPARISON, comparison)
    atomic_json(STATUS, status)
    print("SOLAIRE_V3_EVALUATION " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
