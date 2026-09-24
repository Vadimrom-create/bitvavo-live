#!/usr/bin/env python3
"""Prospective evaluator for MEMORY_ENTRY_CHALLENGER."""
from __future__ import annotations

import json
import statistics
import time
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.solaire_v3 import HORIZONS_HOURS
from scripts.update_solaire_v3_evaluation import _evaluate_event_collection

JOURNAL = "solaire_memory_entry_challenger_journal.json"
PORTFOLIO = "solaire_memory_entry_challenger_portfolio.json"
BASELINE_PORTFOLIO = "solaire_v31_portfolio.json"
COMPARISON = "solaire_memory_entry_challenger_comparison.json"
STATUS = "solaire_memory_entry_challenger_evaluation_status.json"

CHALLENGER_VERSION = "memory-entry-challenger-v1-20260924"
MAX_NEW_EVALUATIONS_PER_RUN = 24


def _summary(events: list[dict[str, Any]], event_type: str, horizon: int) -> dict[str, Any]:
    rows = []
    for event in events:
        if event.get("event_type") != event_type:
            continue
        if event.get("architecture_version") != CHALLENGER_VERSION:
            continue
        if event.get("origin_left_censored") or event.get("left_censored"):
            continue
        ev = (event.get("evaluations") or {}).get(str(horizon))
        if ev and ev.get("complete_horizon"):
            rows.append(ev)

    def vals(key: str) -> list[float]:
        return [finite(x.get(key)) for x in rows if finite(x.get(key)) is not None]

    def med(xs: list[float]) -> float | None:
        return None if not xs else round(statistics.median(xs), 4)

    def mean(xs: list[float]) -> float | None:
        return None if not xs else round(statistics.mean(xs), 4)

    return {
        "n": len(rows),
        "mean_net_stop_or_horizon_return_pct_est": mean(vals("net_stop_or_horizon_return_pct_est")),
        "median_net_stop_or_horizon_return_pct_est": med(vals("net_stop_or_horizon_return_pct_est")),
        "mean_net_close_return_pct_est": mean(vals("net_close_return_pct_est")),
        "median_net_close_return_pct_est": med(vals("net_close_return_pct_est")),
        "median_mfe_pct": med(vals("mfe_pct")),
        "median_mae_pct": med(vals("mae_pct")),
        "mfe_ge_10pct": sum(bool(x.get("mfe_ge_10pct")) for x in rows),
        "mfe_ge_20pct": sum(bool(x.get("mfe_ge_20pct")) for x in rows),
        "stop_hits": sum(bool(x.get("stop_hit")) for x in rows),
    }


def _portfolio_summary(portfolio: dict[str, Any]) -> dict[str, Any]:
    marked = finite(portfolio.get("marked_value_eur"))
    inception = finite(portfolio.get("challenger_inception_marked_value_eur"))
    return {
        "positions": len(portfolio.get("positions") or []),
        "closed": len(portfolio.get("closed") or []),
        "cash_eur": finite(portfolio.get("cash_eur")),
        "marked_value_eur": marked,
        "inception_marked_value_eur": inception,
        "return_since_inception_pct": (
            None
            if marked is None or inception is None or inception <= 0
            else round((marked / inception - 1.0) * 100.0, 4)
        ),
        "rotation_closes": sum(
            str(x.get("close_reason") or "").startswith("ROTATE_")
            for x in (portfolio.get("closed") or [])
        ),
        "stop_closes": sum(
            "STOP" in str(x.get("close_reason") or "")
            for x in (portfolio.get("closed") or [])
        ),
    }


def main() -> int:
    now = time.time()
    journal = read_json(JOURNAL, {}) or {}
    portfolio = read_json(PORTFOLIO, {}) or {}
    baseline = read_json(BASELINE_PORTFOLIO, {}) or {}
    events = [
        x for x in (journal.get("events") or [])
        if x.get("architecture_version") == CHALLENGER_VERSION
    ]

    errors: list[dict[str, Any]] = []
    critical_error = None
    completed = 0
    try:
        client = PublicClient(timeout=10, retries=2, requests_per_second=8)
        client.get("/time", cache=False)
        completed = _evaluate_event_collection(
            client,
            events,
            now,
            MAX_NEW_EVALUATIONS_PER_RUN,
            errors,
        )
    except Exception as exc:
        critical_error = type(exc).__name__ + ":" + str(exc)

    qualified = [
        x for x in events
        if x.get("event_type") == "MEMORY_ENTRY_CHALLENGER_QUALIFIED"
        and not x.get("origin_left_censored")
    ]
    rejected = [
        x for x in events
        if x.get("event_type") == "MEMORY_ENTRY_CHALLENGER_REJECTED"
        and not x.get("origin_left_censored")
    ]

    baseline_marked = finite(baseline.get("marked_value_eur"))
    challenger_marked = finite(portfolio.get("marked_value_eur"))
    inception = finite(portfolio.get("challenger_inception_marked_value_eur"))

    comparison = {
        "schema": "solaire_memory_entry_challenger_comparison_v1",
        "checked_at_utc": utc(now),
        "architecture_version": CHALLENGER_VERSION,
        "experiment": {
            "control": "V3.5 MEMORY_ONLY baseline + V3.1.4 unchanged selection",
            "treatment": (
                "Same baseline plus near-miss-only candidates may seed an isolated "
                "persistent thesis; eventual entries still require unchanged V3 "
                "execution and unchanged V3.1 selection/sizing."
            ),
            "single_factor_intent": "NEAR_MISS_CAN_SEED_PERSISTENT_THESIS",
        },
        "event_summary": {
            "qualified": {
                str(h): _summary(events, "MEMORY_ENTRY_CHALLENGER_QUALIFIED", h)
                for h in HORIZONS_HOURS
            },
            "rejected": {
                str(h): _summary(events, "MEMORY_ENTRY_CHALLENGER_REJECTED", h)
                for h in HORIZONS_HOURS
            },
        },
        "portfolio": {
            "baseline": {
                "positions": len(baseline.get("positions") or []),
                "closed": len(baseline.get("closed") or []),
                "marked_value_eur": baseline_marked,
            },
            "challenger": _portfolio_summary(portfolio),
            "paired_inception": {
                "challenger_inception_at_utc": portfolio.get("challenger_inception_at_utc"),
                "inception_marked_value_eur": inception,
                "current_marked_delta_eur": (
                    None
                    if baseline_marked is None or challenger_marked is None
                    else round(challenger_marked - baseline_marked, 2)
                ),
            },
        },
        "warnings": [
            "This tests a selection-path change, not merely measurement.",
            "Do not infer benefit from a few favorable MFE observations.",
            "Promotion requires independent future periods and portfolio-level net evidence.",
        ],
    }

    status = {
        "schema": "solaire_memory_entry_challenger_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": (
            "DEGRADED_NONBLOCKING"
            if critical_error
            else "OK_WITH_SOURCE_GAPS"
            if errors
            else "OK"
        ),
        "architecture_version": CHALLENGER_VERSION,
        "qualified_events": len(qualified),
        "rejected_events": len(rejected),
        "new_complete_evaluations": completed,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "critical_error": critical_error,
        "errors": errors[:40],
        "research_only": True,
        "affects_v3": False,
        "affects_v31": False,
        "affects_v2": False,
        "affects_email": False,
    }

    journal["updated_at_utc"] = utc(now)
    atomic_json(JOURNAL, journal)
    atomic_json(COMPARISON, comparison)
    atomic_json(STATUS, status)
    print("SOLAIRE_MEMORY_ENTRY_CHALLENGER_EVALUATION " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
