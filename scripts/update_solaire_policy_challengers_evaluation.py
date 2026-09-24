#!/usr/bin/env python3
"""Prospective evaluator for Solaire policy challengers."""
from __future__ import annotations

import json
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
from scripts.update_solaire_v3_evaluation import _evaluate_event_collection, _summary

JOURNAL = "solaire_policy_challengers_journal.json"
PORTFOLIOS = "solaire_policy_challengers_portfolios.json"
BASELINE_PORTFOLIO = "solaire_v31_portfolio.json"
COMPARISON = "solaire_policy_challengers_comparison.json"
STATUS = "solaire_policy_challengers_evaluation_status.json"

CHALLENGER_VERSION = "solaire-policy-challengers-v2-baseline-aligned-20260924"
MAX_NEW_EVALUATIONS_PER_RUN = 24


def _events(events: list[dict[str, Any]], prefix: str, suffix: str) -> list[dict[str, Any]]:
    wanted = prefix + suffix
    return [
        x for x in events
        if x.get("event_type") == wanted
        and x.get("architecture_version") == CHALLENGER_VERSION
    ]


def _portfolio_summary(portfolio: dict[str, Any]) -> dict[str, Any]:
    closed = portfolio.get("closed") or []
    positions = portfolio.get("positions") or []
    reference = finite(portfolio.get("reference_capital_eur"))
    marked = finite(portfolio.get("marked_value_eur"))
    return {
        "positions": len(positions),
        "closed": len(closed),
        "cash_eur": finite(portfolio.get("cash_eur")),
        "marked_value_eur": marked,
        "return_from_reference_pct": (
            None if reference is None or marked is None or reference <= 0
            else round((marked / reference - 1.0) * 100.0, 4)
        ),
        "rotation_close_count": sum(
            str(x.get("close_reason") or "").startswith("ROTATE_") for x in closed
        ),
        "stop_close_count": sum(
            "STOP" in str(x.get("close_reason") or "") for x in closed
        ),
    }


def main() -> int:
    now = time.time()
    journal = read_json(JOURNAL, {}) or {}
    portfolios = read_json(PORTFOLIOS, {}) or {}
    baseline = read_json(BASELINE_PORTFOLIO, {}) or {}
    events = journal.get("events") or []
    current = [
        x for x in events
        if x.get("architecture_version") == CHALLENGER_VERSION
    ]

    errors: list[dict[str, Any]] = []
    critical = None
    total_new = 0
    try:
        client = PublicClient(timeout=10, retries=2, requests_per_second=8)
        client.get("/time", cache=False)
        total_new = _evaluate_event_collection(
            client, current, now, MAX_NEW_EVALUATIONS_PER_RUN, errors
        )
    except Exception as exc:
        critical = type(exc).__name__ + ":" + str(exc)

    stop_q = _events(current, "STOP_NO_HARD_CAP", "_QUALIFIED")
    stop_r = _events(current, "STOP_NO_HARD_CAP", "_REJECTED")
    rr_q = _events(current, "RR_NO_MECHANICAL_GATE", "_QUALIFIED")
    rr_r = _events(current, "RR_NO_MECHANICAL_GATE", "_REJECTED")

    summary = {
        "stop_no_hard_cap_qualified": {
            str(h): _summary(stop_q, "STOP_NO_HARD_CAP_QUALIFIED", h)
            for h in HORIZONS_HOURS
        },
        "stop_no_hard_cap_rejected": {
            str(h): _summary(stop_r, "STOP_NO_HARD_CAP_REJECTED", h)
            for h in HORIZONS_HOURS
        },
        "rr_no_mechanical_gate_qualified": {
            str(h): _summary(rr_q, "RR_NO_MECHANICAL_GATE_QUALIFIED", h)
            for h in HORIZONS_HOURS
        },
        "rr_no_mechanical_gate_rejected": {
            str(h): _summary(rr_r, "RR_NO_MECHANICAL_GATE_REJECTED", h)
            for h in HORIZONS_HOURS
        },
    }

    hold = portfolios.get("hold_no_score_rotation") or {}
    comparison = {
        "schema": "solaire_policy_challengers_comparison_v1",
        "checked_at_utc": utc(now),
        "architecture_version": CHALLENGER_VERSION,
        "method": (
            "Prospective shadow only. Stop/RR challengers alter exactly one V3 "
            "execution veto before applying unchanged V3.1 economic selection. "
            "Hold challenger uses the same qualified V3.1 inputs and disables only "
            "score-based rotation."
        ),
        "horizons_hours": list(HORIZONS_HOURS),
        "summary": summary,
        "portfolios": {
            "baseline_v31_rotation": _portfolio_summary(baseline),
            "hold_no_score_rotation": _portfolio_summary(hold),
            "hold_vs_baseline": {
                "same_inception": bool(
                    hold.get("challenger_inception_at_utc")
                    and hold.get("challenger_inception_marked_value_eur") is not None
                ),
                "challenger_inception_at_utc": hold.get("challenger_inception_at_utc"),
                "challenger_inception_marked_value_eur": finite(
                    hold.get("challenger_inception_marked_value_eur")
                ),
                "marked_value_delta_eur": (
                    None
                    if finite(hold.get("marked_value_eur")) is None
                    or finite(baseline.get("marked_value_eur")) is None
                    else round(
                        finite(hold.get("marked_value_eur"))
                        - finite(baseline.get("marked_value_eur")),
                        2,
                    )
                ),
                "closed_count_delta": (
                    len(hold.get("closed") or []) - len(baseline.get("closed") or [])
                ),
            },
        },
        "warnings": [
            "No challenger sends email or submits orders.",
            "Qualified/rejected cohorts can share markets and are not independent trades.",
            "Promotion requires complete prospective horizons and portfolio-level evidence.",
        ],
    }
    status = {
        "schema": "solaire_policy_challengers_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical else ("OK_WITH_SOURCE_GAPS" if errors else "OK"),
        "architecture_version": CHALLENGER_VERSION,
        "events_current_version": len(current),
        "stop_qualified_events": len(stop_q),
        "stop_rejected_events": len(stop_r),
        "rr_qualified_events": len(rr_q),
        "rr_rejected_events": len(rr_r),
        "new_complete_evaluations": total_new,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "critical_error": critical,
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
    print("SOLAIRE_POLICY_CHALLENGERS_EVALUATION " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
