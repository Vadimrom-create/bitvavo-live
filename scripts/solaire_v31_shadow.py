#!/usr/bin/env python3
"""Solaire V3.1 economic selection/allocation shadow.

Consumes the exact V3 candidate output and neutral Bitvavo universe snapshot.
It does not add discovery/network work, alter V3, send mail, or submit orders.
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
from research.solaire_v31 import (
    FROZEN_V3_COMMIT,
    V3_TIMING_LAB_COMMIT,
    MAX_SHADOW_POSITIONS,
    REFERENCE_CAPITAL_EUR,
    final_economic_score,
    preliminary_economic_score,
    shadow_sizing,
    timing_variants,
)

V3_CANDIDATES = "solaire_v3_candidates.json"
UNIVERSE = "production_universe_snapshot.json"
STATE = "solaire_v31_state.json"
JOURNAL = "solaire_v31_journal.json"
CANDIDATES = "solaire_v31_candidates.json"
PORTFOLIO = "solaire_v31_portfolio.json"
PORTFOLIO_PERSIST = "solaire_v31_portfolio_persist30.json"
PORTFOLIO_RECLAIM = "solaire_v31_portfolio_pullback_reclaim.json"
STATUS = "solaire_v31_status.json"

WATCH_EXPIRY = 24 * 3600
ROTATION_SCORE_DELTA = 1.25
ENTRY_FEE_EST = 0.0035
EXIT_FEE_EST = 0.0035


def _event_key(event: dict[str, Any]) -> str:
    return "|".join([
        str(event.get("market") or ""),
        str(event.get("episode") or ""),
        str(event.get("event_type") or ""),
    ])


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    keys = {_event_key(x) for x in journal.get("events", [])}
    if _event_key(event) in keys:
        return False
    journal.setdefault("events", []).append(event)
    return True


def _close_position(portfolio: dict[str, Any], position: dict[str, Any], current: float, now: float, reason: str) -> None:
    position["closed_ts"] = now
    position["closed_at_utc"] = utc(now)
    position["exit_eur"] = current
    position["close_reason"] = reason
    stake = finite(position.get("stake_eur"), 0.0)
    entry = finite(position.get("entry_eur"))
    if entry and entry > 0:
        portfolio["cash_eur"] += stake * (current / entry) * (1 - EXIT_FEE_EST)
    portfolio["closed"].append(position)
    portfolio["positions"].remove(position)
    portfolio["actions"].append({
        "at_utc": utc(now),
        "action": "CLOSE_SHADOW",
        "market": position.get("market"),
        "reason": reason,
        "exit_eur": current,
    })


def update_portfolio(
    portfolio: dict[str, Any],
    qualified: list[dict[str, Any]],
    universe_by_market: dict[str, dict[str, Any]],
    current_scores: dict[str, float],
    now: float,
) -> dict[str, Any]:
    portfolio.setdefault("schema", "solaire_v31_portfolio_v1")
    portfolio.setdefault("reference_capital_eur", REFERENCE_CAPITAL_EUR)
    portfolio.setdefault("cash_eur", REFERENCE_CAPITAL_EUR)
    portfolio.setdefault("positions", [])
    portfolio.setdefault("closed", [])
    portfolio.setdefault("actions", [])
    portfolio.setdefault("consumed_episodes", [])
    consumed = set(portfolio["consumed_episodes"])

    for position in list(portfolio["positions"]):
        current = finite((universe_by_market.get(position["market"]) or {}).get("price_eur"))
        if current is not None:
            position["mark_eur"] = current
            position["updated_at_utc"] = utc(now)
        if position["market"] in current_scores:
            position["economic_score"] = current_scores[position["market"]]
        stop = finite(position.get("stop_eur"))
        if current is not None and stop is not None and current <= stop:
            _close_position(portfolio, position, current, now, "STOP_OBSERVED_AT_V31_CYCLE")

    for row in sorted(qualified, key=lambda x: finite(x.get("economic_score"), 0), reverse=True):
        market = row["market"]
        episode_key = market + "|" + str(row.get("episode") or "")
        if episode_key in consumed:
            continue
        if any(p.get("market") == market for p in portfolio["positions"]):
            continue

        score = finite(row.get("economic_score"), 0)
        if len(portfolio["positions"]) >= MAX_SHADOW_POSITIONS:
            weakest = min(portfolio["positions"], key=lambda p: finite(p.get("economic_score"), 0))
            weakest_score = finite(weakest.get("economic_score"), 0)
            if score < weakest_score + ROTATION_SCORE_DELTA:
                continue
            current = finite((universe_by_market.get(weakest["market"]) or {}).get("price_eur"))
            if current is None:
                continue
            _close_position(portfolio, weakest, current, now, "ROTATE_TO_HIGHER_ECONOMIC_SCORE")

        sizing = row.get("sizing") or {}
        stake = finite(sizing.get("stake_eur"))
        entry = finite(row.get("entry_eur"))
        if stake is None or entry is None or stake <= 0 or entry <= 0:
            continue
        total_debit = stake * (1 + ENTRY_FEE_EST)
        if portfolio["cash_eur"] < total_debit:
            continue

        portfolio["cash_eur"] -= total_debit
        portfolio["positions"].append({
            "market": market,
            "episode": row.get("episode"),
            "opened_ts": now,
            "opened_at_utc": utc(now),
            "entry_eur": entry,
            "stop_eur": finite(row.get("stop_eur")),
            "stake_eur": stake,
            "theoretical_risk_eur": finite(sizing.get("theoretical_risk_eur")),
            "economic_score": score,
        })
        portfolio["actions"].append({
            "at_utc": utc(now),
            "action": "OPEN_V31_SHADOW",
            "market": market,
            "economic_score": score,
            "stake_eur": stake,
        })
        consumed.add(episode_key)

    portfolio["consumed_episodes"] = sorted(consumed)[-5000:]
    marked = portfolio["cash_eur"]
    for position in portfolio["positions"]:
        mark = finite(position.get("mark_eur"), position.get("entry_eur"))
        entry = finite(position.get("entry_eur"))
        stake = finite(position.get("stake_eur"), 0)
        if mark is not None and entry and entry > 0:
            marked += stake * (mark / entry)
    portfolio["marked_value_eur"] = round(marked, 2)
    portfolio["updated_at_utc"] = utc(now)
    portfolio["research_only"] = True
    return portfolio



def _timing_event(
    row: dict[str, Any],
    market_state: dict[str, Any],
    plan: dict[str, Any],
    now: float,
    path: str,
    initial_timing_cycle: bool,
) -> dict[str, Any]:
    qualified = bool(row.get("selectable"))
    return {
        "event_type": f"V31_{path}_" + ("QUALIFIED_ENTRY" if qualified else "REJECTED_READY"),
        "market": row["market"],
        "episode": market_state["episode"],
        "decision_ts": now,
        "decision_at_utc": utc(now),
        "price_eur": row.get("price_eur"),
        "entry_eur": finite(plan.get("entry_eur")),
        "stop_eur": finite(plan.get("stop_eur")),
        "tp1_eur": finite(plan.get("tp1_eur")),
        "stake_eur": finite((row.get("sizing") or {}).get("stake_eur")),
        "economic_score": row["economic_score"],
        "selection_reason": row["selection_reason"],
        "preliminary": row["preliminary"],
        "execution_quality": row["execution_quality"],
        "sizing": row.get("sizing"),
        "timing_path": path,
        "timing_state": row.get("timing_state"),
        "upstream_v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "legacy_v2_score_unused": row.get("v2_score"),
        "legacy_v3_opportunity_score_unused": row.get("v3_opportunity_score"),
        "left_censored_at_v31_timing_t0": initial_timing_cycle,
        "evaluations": {},
    }



def main() -> int:
    now = time.time()
    v3_doc = read_json(V3_CANDIDATES, {}) or {}
    universe = read_json(UNIVERSE, {}) or {}
    state = read_json(STATE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}
    portfolio = read_json(PORTFOLIO, {}) or {}
    portfolio_persist = read_json(PORTFOLIO_PERSIST, {}) or {}
    portfolio_reclaim = read_json(PORTFOLIO_RECLAIM, {}) or {}

    v3_candidates = v3_doc.get("candidates") or []
    news_mapping = v3_doc.get("news_mapping") or {}
    rows = universe.get("rows") or []
    universe_by_market = {x.get("market"): x for x in rows if x.get("market")}

    initial_cycle = not bool(state.get("initialized"))
    initial_timing_cycle = not bool(state.get("timing_lab_initialized"))
    state.setdefault("schema", "solaire_v31_state_v1")
    state.setdefault("started_ts", now)
    state.setdefault("started_at_utc", utc(now))
    state.setdefault("timing_lab_started_ts", now)
    state.setdefault("timing_lab_started_at_utc", utc(now))
    state.setdefault("markets", {})
    journal.setdefault("schema", "solaire_v31_prospective_journal_v1")
    journal.setdefault("started_ts", state["started_ts"])
    journal.setdefault("started_at_utc", state["started_at_utc"])
    journal.setdefault("events", [])

    if not v3_candidates or not rows:
        status = {
            "schema": "solaire_v31_status_v1",
            "checked_at_utc": utc(now),
            "status": "DEGRADED_NONBLOCKING",
            "reason": "MISSING_V3_CANDIDATES_OR_UNIVERSE",
            "mode": "ECONOMIC_SELECTION_SHADOW",
            "frozen_v3_commit": FROZEN_V3_COMMIT,
            "affects_v3": False,
            "affects_v2": False,
            "affects_email": False,
            "orders_submitted": False,
        }
        atomic_json(STATUS, status)
        print("SOLAIRE_V31 " + json.dumps(status))
        return 0

    ranked = []
    for candidate in v3_candidates:
        market = candidate.get("market")
        row = universe_by_market.get(market)
        if not market or row is None:
            continue
        preliminary = preliminary_economic_score(candidate, row)
        final = final_economic_score(preliminary, candidate.get("execution"))
        sizing = None
        if final.get("selectable"):
            sizing = shadow_sizing(
                finite(final.get("score"), 0),
                candidate.get("execution") or {},
                finite(row.get("quote_volume_24h_eur")),
            )
            if not sizing.get("valid"):
                final = {**final, "selectable": False, "reason": sizing.get("reason")}
        ranked.append({
            "market": market,
            "price_eur": finite(row.get("price_eur")),
            "quote_volume_24h_eur": finite(row.get("quote_volume_24h_eur")),
            "preliminary": preliminary,
            "economic_score": finite(final.get("score"), 0),
            "selectable": bool(final.get("selectable")),
            "selection_reason": final.get("reason"),
            "execution_quality": final.get("execution_quality"),
            "execution": candidate.get("execution"),
            "sizing": sizing,
            "v2_state": candidate.get("v2_state"),
            "v2_score": candidate.get("v2_score"),
            "v3_opportunity_score": candidate.get("opportunity_score"),
            "timing_state": candidate.get("timing_state"),
            "timing_paths": timing_variants(candidate),
        })

    ranked.sort(key=lambda x: x["economic_score"], reverse=True)
    current_markets = set()
    qualified_for_portfolio = []
    ready_rejected = []
    qualified_persist = []
    qualified_reclaim = []

    for row in ranked:
        market = row["market"]
        current_markets.add(market)
        ms = state["markets"].setdefault(market, {"episode": 0, "active": False})
        if not ms.get("active") or now - finite(ms.get("last_seen_ts"), 0) > WATCH_EXPIRY:
            ms["episode"] = int(ms.get("episode", 0)) + 1
            ms["active"] = True
            ms["started_ts"] = now
            ms["started_at_utc"] = utc(now)
            ms.pop("decision_recorded_episode", None)
            ms.pop("timing_decisions", None)

        ms["last_seen_ts"] = now
        ms["last_seen_at_utc"] = utc(now)
        ms["economic_score"] = row["economic_score"]
        ms["selection_reason"] = row["selection_reason"]
        row["episode"] = ms["episode"]

        execution = row.get("execution") or {}
        if not execution.get("ready"):
            continue

        plan = execution.get("plan") or {}
        event_type = "V31_QUALIFIED_ENTRY" if row.get("selectable") else "V31_REJECTED_READY"
        event = {
            "event_type": event_type,
            "market": market,
            "episode": ms["episode"],
            "decision_ts": now,
            "decision_at_utc": utc(now),
            "price_eur": row.get("price_eur"),
            "entry_eur": finite(plan.get("entry_eur")),
            "stop_eur": finite(plan.get("stop_eur")),
            "tp1_eur": finite(plan.get("tp1_eur")),
            "stake_eur": finite((row.get("sizing") or {}).get("stake_eur")),
            "economic_score": row["economic_score"],
            "selection_reason": row["selection_reason"],
            "preliminary": row["preliminary"],
            "execution_quality": row["execution_quality"],
            "sizing": row.get("sizing"),
            "legacy_v2_score_unused": row.get("v2_score"),
            "legacy_v3_opportunity_score_unused": row.get("v3_opportunity_score"),
            "left_censored_at_v31_t0": initial_cycle,
            "evaluations": {},
        }
        if ms.get("decision_recorded_episode") != ms["episode"] and _append_event(journal, event):
            ms["decision_recorded_episode"] = ms["episode"]

        if row.get("selectable"):
            qualified_for_portfolio.append({
                **row,
                "entry_eur": finite(plan.get("entry_eur")),
                "stop_eur": finite(plan.get("stop_eur")),
            })
        else:
            ready_rejected.append(row)

        # Factorial timing lab: RAW above remains untouched. These two paths
        # reuse V3's already-recorded timing decisions and apply only the
        # unchanged V3.1 economic score/gate at that exact observation cycle.
        timing_decisions = ms.setdefault("timing_decisions", {})
        for path, active in (row.get("timing_paths") or {}).items():
            if not active or timing_decisions.get(path) == ms["episode"]:
                continue
            timing_event = _timing_event(row, ms, plan, now, path, initial_timing_cycle)
            _append_event(journal, timing_event)
            timing_decisions[path] = ms["episode"]
            if initial_timing_cycle or not row.get("selectable"):
                continue
            timed_row = {
                **row,
                "entry_eur": finite(plan.get("entry_eur")),
                "stop_eur": finite(plan.get("stop_eur")),
            }
            if path == "PERSIST_30M":
                qualified_persist.append(timed_row)
            elif path == "PULLBACK_RECLAIM":
                qualified_reclaim.append(timed_row)

    for market, ms in state["markets"].items():
        if market not in current_markets and ms.get("active") and now - finite(ms.get("last_seen_ts"), 0) > WATCH_EXPIRY:
            ms["active"] = False
            ms["ended_ts"] = now
            ms["ended_at_utc"] = utc(now)

    current_scores = {x["market"]: x["economic_score"] for x in ranked}
    portfolio = update_portfolio(portfolio, qualified_for_portfolio, universe_by_market, current_scores, now)
    portfolio_persist = update_portfolio(portfolio_persist, qualified_persist, universe_by_market, current_scores, now)
    portfolio_reclaim = update_portfolio(portfolio_reclaim, qualified_reclaim, universe_by_market, current_scores, now)

    unchecked = [x for x in ranked if not (x.get("execution") or {}).get("ready") and (x.get("execution") is None)]
    candidate_doc = {
        "schema": "solaire_v31_candidates_v1",
        "generated_at_utc": utc(now),
        "mode": "ECONOMIC_SELECTION_SHADOW",
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "research_only": True,
        "affects_v3": False,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "method_note": "RAW ranking is unchanged; timing variants consume only V3-recorded timing events. News discovery is inherited from V3's full Bitvavo dynamic asset map; V3.1 adds no separate whitelist.",
        "news_mapping": news_mapping,
        "candidates": ranked,
    }
    status = {
        "schema": "solaire_v31_status_v1",
        "checked_at_utc": utc(now),
        "status": "OK",
        "mode": "ECONOMIC_SELECTION_SHADOW",
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "v3_timing_lab_commit": V3_TIMING_LAB_COMMIT,
        "candidate_count": len(ranked),
        "news_mapping_mode": news_mapping.get("mode"),
        "news_universe_symbols": news_mapping.get("universe_symbols"),
        "news_ticker_coverage_symbols": news_mapping.get("ticker_coverage_symbols"),
        "news_named_alias_symbols": news_mapping.get("named_alias_symbols"),
        "news_mapping_inherited_from_v3": True,
        "execution_ready_count": sum(bool((x.get("execution") or {}).get("ready")) for x in ranked),
        "qualified_count": len(qualified_for_portfolio),
        "ready_rejected_count": len(ready_rejected),
        "timing_persist_qualified_this_cycle": len(qualified_persist),
        "timing_reclaim_qualified_this_cycle": len(qualified_reclaim),
        "unchecked_candidate_count": len(unchecked),
        "portfolio_positions": len(portfolio.get("positions", [])),
        "portfolio_marked_value_eur": portfolio.get("marked_value_eur"),
        "persist30_portfolio_positions": len(portfolio_persist.get("positions", [])),
        "persist30_portfolio_marked_value_eur": portfolio_persist.get("marked_value_eur"),
        "pullback_reclaim_portfolio_positions": len(portfolio_reclaim.get("positions", [])),
        "pullback_reclaim_portfolio_marked_value_eur": portfolio_reclaim.get("marked_value_eur"),
        "affects_v3": False,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    state["initialized"] = True
    state["timing_lab_initialized"] = True
    state["updated_at_utc"] = utc(now)
    journal["updated_at_utc"] = utc(now)
    journal["research_only"] = True
    journal["frozen_v3_commit"] = FROZEN_V3_COMMIT
    journal["v3_timing_lab_commit"] = V3_TIMING_LAB_COMMIT
    journal["events"] = journal["events"][-10000:]

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(CANDIDATES, candidate_doc)
    atomic_json(PORTFOLIO, portfolio)
    atomic_json(PORTFOLIO_PERSIST, portfolio_persist)
    atomic_json(PORTFOLIO_RECLAIM, portfolio_reclaim)
    atomic_json(STATUS, status)
    print("SOLAIRE_V31 " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
