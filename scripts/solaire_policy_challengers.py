#!/usr/bin/env python3
"""Prospective shadow challengers for Solaire entry gates and position rotation.

All challengers are research-only:
- STOP_NO_HARD_CAP: remove only V3's hard stop-distance veto, keep V3.1 unchanged.
- RR_NO_MECHANICAL_GATE: remove only V3's mechanical 2R/net-RR veto, keep V3.1 unchanged.
- HOLD_NO_SCORE_ROTATION: consume the same V3.1 qualified decisions but never rotate
  solely because another candidate has a higher entry score.

No email, order or production trading threshold is changed.
"""
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
from research.solaire_v31 import (
    V31_ARCHITECTURE_VERSION,
    final_economic_score,
    preliminary_economic_score,
    reprice_execution_for_stake,
    shadow_sizing,
)
from scripts.solaire_v31_shadow import update_portfolio

V3_CANDIDATES = "solaire_v3_candidates.json"
V31_CANDIDATES = "solaire_v31_candidates.json"
V31_PORTFOLIO = "solaire_v31_portfolio.json"
UNIVERSE = "production_universe_snapshot.json"
JOURNAL = "solaire_policy_challengers_journal.json"
PORTFOLIOS = "solaire_policy_challengers_portfolios.json"
STATUS = "solaire_policy_challengers_status.json"

CHALLENGER_VERSION = "solaire-policy-challengers-v1-20260924"
MAX_STOP_BASELINE_PCT = 10.0


def _event_key(event: dict[str, Any]) -> str:
    return "|".join([
        str(event.get("market") or ""),
        str(event.get("episode") or ""),
        str(event.get("entry_path") or ""),
        str(event.get("challenger") or ""),
        str(event.get("event_type") or ""),
        str(event.get("architecture_version") or ""),
    ])


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    keys = {_event_key(x) for x in journal.get("events", [])}
    if _event_key(event) in keys:
        return False
    journal.setdefault("events", []).append(event)
    return True


def _alternative_decision(
    candidate: dict[str, Any],
    universe_row: dict[str, Any],
    execution: dict[str, Any],
    challenger: str,
    entry_path: str,
    now: float,
) -> dict[str, Any]:
    alt_execution = {**execution, "ready": True, "reason": "ENTRY_READY_" + challenger}
    preliminary = preliminary_economic_score(candidate, universe_row)
    final = final_economic_score(preliminary, alt_execution)
    sizing = None
    if final.get("selectable"):
        sizing = shadow_sizing(
            finite(final.get("score"), 0),
            alt_execution,
            finite(universe_row.get("quote_volume_24h_eur")),
        )
        if not sizing.get("valid"):
            final = {**final, "selectable": False, "reason": sizing.get("reason")}
        else:
            alt_execution = reprice_execution_for_stake(
                alt_execution, finite(sizing.get("stake_eur"), 0.0)
            )
            final = final_economic_score(preliminary, alt_execution)
            if not final.get("selectable"):
                sizing = None
    plan = alt_execution.get("plan") or execution.get("plan") or {}
    episode = ((candidate.get("timing_state") or {}).get("episode")
               or ((candidate.get("persistent_thesis") or {}).get("thesis_id"))
               or 0)
    event_type = challenger + ("_QUALIFIED" if final.get("selectable") else "_REJECTED")
    decision_ts = finite(execution.get("available_ts"), now)
    return {
        "event_type": event_type,
        "challenger": challenger,
        "market": candidate.get("market"),
        "episode": episode,
        "entry_path": entry_path,
        "decision_ts": decision_ts,
        "decision_at_utc": utc(decision_ts),
        "price_eur": finite(candidate.get("price_eur")),
        "entry_eur": finite(plan.get("entry_eur")),
        "stop_eur": finite(plan.get("stop_eur")),
        "tp1_eur": finite(plan.get("tp1_eur")),
        "stake_eur": finite((sizing or {}).get("stake_eur")),
        "economic_score": finite(final.get("score")),
        "selectable": bool(final.get("selectable")),
        "selection_reason": final.get("reason"),
        "preliminary": preliminary,
        "execution_quality": final.get("execution_quality"),
        "sizing": sizing,
        "baseline_gate_reason": execution.get("reason"),
        "baseline_plan": execution.get("plan"),
        "alternative_execution": alt_execution,
        "v31_architecture_version": V31_ARCHITECTURE_VERSION,
        "architecture_version": CHALLENGER_VERSION,
        "research_only": True,
        "affects_v3": False,
        "affects_v31": False,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "evaluations": {},
    }


def main() -> int:
    now = time.time()
    v3_doc = read_json(V3_CANDIDATES, {}) or {}
    v31_doc = read_json(V31_CANDIDATES, {}) or {}
    universe = read_json(UNIVERSE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}
    portfolios = read_json(PORTFOLIOS, {}) or {}

    journal.setdefault("schema", "solaire_policy_challengers_journal_v1")
    journal.setdefault("started_ts", now)
    journal.setdefault("started_at_utc", utc(now))
    journal.setdefault("events", [])

    universe_by_market = {
        x.get("market"): x for x in (universe.get("rows") or []) if x.get("market")
    }
    v3_candidates = v3_doc.get("candidates") or []

    new_stop = 0
    new_rr = 0
    for candidate in v3_candidates:
        market = candidate.get("market")
        universe_row = universe_by_market.get(market)
        if not market or universe_row is None:
            continue
        paths = [("RAW", candidate.get("execution"))]
        if candidate.get("thesis_reentry_hypothesis"):
            paths.append(("THESIS_REENTRY", candidate.get("thesis_execution")))
        for entry_path, execution in paths:
            if not execution:
                continue
            plan = execution.get("plan") or {}
            if not plan.get("valid"):
                continue
            reason = execution.get("reason")
            if reason == "WAITING_STOP_GEOMETRY":
                event = _alternative_decision(
                    candidate, universe_row, execution,
                    "STOP_NO_HARD_CAP", entry_path, now,
                )
                if _append_event(journal, event):
                    new_stop += 1
            elif reason == "WAITING_INSUFFICIENT_NET_RISK_REWARD":
                stop_pct = finite(plan.get("stop_distance_pct"), 999.0)
                # Isolate only the R:R gate: cases that would also violate the
                # unchanged 10% stop cap are excluded from this challenger.
                if stop_pct <= MAX_STOP_BASELINE_PCT:
                    event = _alternative_decision(
                        candidate, universe_row, execution,
                        "RR_NO_MECHANICAL_GATE", entry_path, now,
                    )
                    if _append_event(journal, event):
                        new_rr += 1

    # Third challenger: same selectable V3.1 inputs, but no score-based rotation.
    hold = portfolios.get("hold_no_score_rotation") or {}
    ranked = v31_doc.get("candidates") or []
    qualified = []
    for row in ranked:
        if not row.get("selectable"):
            continue
        execution = row.get("execution") or {}
        if not execution.get("ready"):
            continue
        plan = execution.get("plan") or {}
        qualified.append({
            **row,
            "entry_eur": finite(plan.get("entry_eur")),
            "stop_eur": finite(plan.get("stop_eur")),
        })
    current_scores = {
        x.get("market"): finite(x.get("economic_score"), 0.0)
        for x in ranked if x.get("market")
    }
    client = None
    try:
        client = PublicClient(timeout=8, retries=1, requests_per_second=10)
        client.get("/time", cache=False)
    except Exception:
        client = None
    hold = update_portfolio(
        hold,
        qualified,
        universe_by_market,
        current_scores,
        now,
        client=client,
        allow_score_rotation=False,
    )
    hold["challenger"] = "HOLD_NO_SCORE_ROTATION"
    hold["architecture_version"] = CHALLENGER_VERSION

    portfolios["schema"] = "solaire_policy_challengers_portfolios_v1"
    portfolios["updated_at_utc"] = utc(now)
    portfolios["architecture_version"] = CHALLENGER_VERSION
    portfolios["hold_no_score_rotation"] = hold

    baseline_portfolio = read_json(V31_PORTFOLIO, {}) or {}
    status = {
        "schema": "solaire_policy_challengers_status_v1",
        "checked_at_utc": utc(now),
        "status": "OK",
        "architecture_version": CHALLENGER_VERSION,
        "v31_architecture_version": V31_ARCHITECTURE_VERSION,
        "new_stop_policy_events": new_stop,
        "new_rr_policy_events": new_rr,
        "stop_policy_events_total": sum(
            str(x.get("event_type") or "").startswith("STOP_NO_HARD_CAP")
            for x in journal.get("events", [])
        ),
        "rr_policy_events_total": sum(
            str(x.get("event_type") or "").startswith("RR_NO_MECHANICAL_GATE")
            for x in journal.get("events", [])
        ),
        "hold_positions": len(hold.get("positions", [])),
        "hold_marked_value_eur": hold.get("marked_value_eur"),
        "baseline_rotation_positions": len(baseline_portfolio.get("positions", [])),
        "baseline_rotation_marked_value_eur": baseline_portfolio.get("marked_value_eur"),
        "research_only": True,
        "affects_v3": False,
        "affects_v31": False,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    journal["updated_at_utc"] = utc(now)
    journal["architecture_version"] = CHALLENGER_VERSION
    journal["events"] = journal["events"][-10000:]
    atomic_json(JOURNAL, journal)
    atomic_json(PORTFOLIOS, portfolios)
    atomic_json(STATUS, status)
    print("SOLAIRE_POLICY_CHALLENGERS " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
