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
from research.solaire_v31 import FROZEN_V3_COMMIT
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
        if event.get("left_censored_at_v31_t0"):
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
    v3_same_window = []
    for event in v3.get("events", []) or []:
        if event.get("event_type") != "ENTRY_READY_SHADOW" or event.get("left_censored_at_v3_t0"):
            continue
        ts = finite(event.get("decision_ts"))
        if start_ts is not None and ts is not None and ts >= start_ts:
            v3_same_window.append(event)

    summary = {
        "v31_qualified": {str(h): _summary(qualified, "V31_QUALIFIED_ENTRY", h) for h in HORIZONS_HOURS},
        "v31_rejected_ready": {str(h): _summary(rejected, "V31_REJECTED_READY", h) for h in HORIZONS_HOURS},
        "v3_entry_ready_same_window": {str(h): _summary(v3_same_window, "ENTRY_READY_SHADOW", h) for h in HORIZONS_HOURS},
    }

    comparison = {
        "schema": "solaire_v31_vs_frozen_v3_comparison_v1",
        "checked_at_utc": utc(now),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "method": "same V3 candidate feed; V3.1 changes only ranking, economic gate, sizing and allocation; strict complete horizons",
        "horizons_hours": list(HORIZONS_HOURS),
        "summary": summary,
        "score_calibration": {
            str(h): _score_bins(qualified, h)
            for h in (4, 24, 48, 96)
        },
        "warning": "Pre-V3.1 NIL/APE/FORM outcomes motivated the hypotheses but are excluded from prospective V3.1 performance.",
    }
    status = {
        "schema": "solaire_v31_evaluation_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical else ("OK_WITH_SOURCE_GAPS" if errors else "OK"),
        "prospective_started_at_utc": v31.get("started_at_utc"),
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "new_complete_evaluations": total_new,
        "evaluation_budget_per_run": MAX_NEW_EVALUATIONS_PER_RUN,
        "qualified_events": len(qualified),
        "rejected_ready_events": len(rejected),
        "v3_same_window_events": len(v3_same_window),
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
