#!/usr/bin/env python3
"""Solaire V3.1 economic selection/allocation shadow.

Consumes the exact V3 candidate output and neutral Bitvavo universe snapshot.
It does not add discovery/network work, alter V3, send mail, or submit orders.
"""
from __future__ import annotations

import json
import math
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
    FROZEN_V3_COMMIT,
    V31_ARCHITECTURE_VERSION,
    V3_TIMING_LAB_COMMIT,
    MAX_SHADOW_POSITIONS,
    REFERENCE_CAPITAL_EUR,
    final_economic_score,
    preliminary_economic_score,
    execution_freshness,
    reprice_execution_for_stake,
    select_execution_path,
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
PORTFOLIO_RAW = "solaire_v31_portfolio_raw.json"
PORTFOLIO_REENTRY = "solaire_v31_portfolio_reentry.json"
STATUS = "solaire_v31_status.json"

WATCH_EXPIRY = 24 * 3600
ROTATION_SCORE_DELTA = 1.25
ENTRY_FEE_EST = 0.0035
EXIT_FEE_EST = 0.0035


def _event_key(event: dict[str, Any]) -> str:
    attempt_id = event.get("attempt_id")
    if attempt_id:
        return str(attempt_id)
    return "|".join([
        str(event.get("market") or ""),
        str(event.get("episode") or ""),
        str(event.get("event_type") or ""),
        str(event.get("entry_path") or ""),
    ])


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    event.setdefault("architecture_version", V31_ARCHITECTURE_VERSION)
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
        "stake_eur": stake,
        "decision_id": position.get("decision_id"),
    })


def _append_allocation_action_once(
    portfolio: dict[str, Any],
    row: dict[str, Any],
    now: float,
    reason: str,
) -> None:
    """Record allocation/capacity outcomes without changing portfolio policy."""
    decision_id = row.get("decision_id")
    key = "|".join([
        str(decision_id or ""),
        str(row.get("market") or ""),
        str(row.get("entry_path") or "RAW"),
        reason,
    ])
    for action in reversed(portfolio.get("actions", [])[-500:]):
        if action.get("allocation_audit_key") == key:
            return
    portfolio.setdefault("actions", []).append({
        "at_utc": utc(now),
        "action": "ALLOCATION_REJECTED",
        "reason": reason,
        "market": row.get("market"),
        "economic_score": finite(row.get("economic_score")),
        "entry_path": row.get("entry_path") or "RAW",
        "decision_id": decision_id,
        "allocation_audit_key": key,
        "measurement_only": True,
    })


def _trade_stop_observation(
    client: PublicClient,
    market: str,
    start_ts: float,
    end_ts: float,
    stop_eur: float,
) -> dict[str, Any] | None:
    if end_ts <= start_ts:
        return None
    raw = client.get(
        "/" + market + "/trades",
        {
            "start": max(0, int(start_ts * 1000)),
            "end": int(end_ts * 1000),
            "limit": 1000,
        },
        cache=False,
    )
    trades = []
    for row in raw or []:
        if not isinstance(row, dict):
            continue
        ts_ms = finite(row.get("timestamp"))
        price = finite(row.get("price"))
        if ts_ms is None or price is None:
            continue
        ts = ts_ms / 1000.0
        if start_ts <= ts <= end_ts:
            trades.append((ts, price))
    trades.sort(key=lambda x: x[0])
    for ts, price in trades:
        if price <= stop_eur:
            return {
                "observed_ts": ts,
                "observed_at_utc": utc(ts),
                "trade_price_eur": price,
                "exit_eur": min(stop_eur, price),
                "gap_through_stop": price < stop_eur,
                "coverage": "EXACT_PUBLIC_TRADES_PARTIAL_MINUTE",
            }
    return None


def _first_stop_observation(
    client: PublicClient | None,
    market: str,
    since_ts: float,
    now: float,
    stop_eur: float,
) -> dict[str, Any] | None:
    """Detect stop touches between checks, including partial opening/final minutes.

    Exact public trades cover the partial minutes containing the prior/current
    check.  Completed 1m bars cover the interval between them.  This avoids the
    old blind spot where a stop could be touched and recover before the next
    completed 5m candle.
    """
    if client is None or stop_eur <= 0 or now <= since_ts:
        return None
    try:
        interval = 60.0
        first_full_start = math.ceil(since_ts / interval) * interval
        final_minute_start = math.floor(now / interval) * interval
        observations: list[dict[str, Any]] = []

        # Opening partial minute: only trades after the position/check timestamp
        # are causal; the candle low could predate the position.
        opening_end = min(now, first_full_start)
        if opening_end > since_ts:
            hit = _trade_stop_observation(
                client, market, since_ts, opening_end, stop_eur
            )
            if hit is not None:
                observations.append(hit)

        # Completed one-minute bars between the partial endpoints.
        if first_full_start < final_minute_start:
            raw = client.get(
                "/" + market + "/candles",
                {
                    "interval": "1m",
                    "start": int(first_full_start * 1000),
                    "end": int(final_minute_start * 1000),
                    "limit": 1440,
                },
                cache=False,
            )
            bars = []
            for row in raw or []:
                if not isinstance(row, list) or len(row) < 4:
                    continue
                ts_ms = finite(row[0])
                open_eur = finite(row[1])
                low_eur = finite(row[3])
                if ts_ms is None or open_eur is None or low_eur is None:
                    continue
                start_ts = ts_ms / 1000.0
                if start_ts < first_full_start or start_ts + interval > now:
                    continue
                bars.append((start_ts, open_eur, low_eur))
            bars.sort(key=lambda x: x[0])
            for start_ts, open_eur, low_eur in bars:
                if low_eur <= stop_eur:
                    observations.append({
                        "observed_ts": start_ts,
                        "observed_at_utc": utc(start_ts),
                        "bar_start_ts": start_ts,
                        "bar_start_at_utc": utc(start_ts),
                        "open_eur": open_eur,
                        "low_eur": low_eur,
                        "exit_eur": min(stop_eur, open_eur),
                        "gap_through_stop": open_eur < stop_eur,
                        "coverage": "COMPLETED_1M_BARS_BETWEEN_CHECKS",
                    })
                    break

        # Final partial minute can also touch and recover before the next scan.
        partial_start = max(since_ts, final_minute_start)
        if now > partial_start:
            hit = _trade_stop_observation(
                client, market, partial_start, now, stop_eur
            )
            if hit is not None:
                observations.append(hit)

        if not observations:
            return None
        observations.sort(key=lambda x: finite(x.get("observed_ts"), now))
        return observations[0]
    except Exception:
        return None

def update_portfolio(
    portfolio: dict[str, Any],
    qualified: list[dict[str, Any]],
    universe_by_market: dict[str, dict[str, Any]],
    current_scores: dict[str, float],
    now: float,
    *,
    client: PublicClient | None = None,
    allow_score_rotation: bool = True,
) -> dict[str, Any]:
    portfolio.setdefault("schema", "solaire_v31_portfolio_v2")
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
        since = finite(position.get("last_stop_check_ts"))
        if since is None:
            since = max(finite(position.get("opened_ts"), now - 600), now - 600)
        stop_observation = (
            None if stop is None
            else _first_stop_observation(client, position["market"], since, now, stop)
        )
        position["stop_observation_since_last_check"] = stop_observation
        position["last_stop_check_ts"] = now
        position["last_stop_check_at_utc"] = utc(now)
        if stop_observation is not None:
            _close_position(
                portfolio,
                position,
                finite(stop_observation.get("exit_eur"), stop),
                now,
                "STOP_GAP_BETWEEN_V31_CYCLES"
                if stop_observation.get("gap_through_stop")
                else "STOP_TOUCHED_BETWEEN_V31_CYCLES",
            )
        elif stop is not None and current is not None and current <= stop:
            _close_position(portfolio, position, current, now, "STOP_GAP_OBSERVED_AT_V31_CYCLE")

    for row in sorted(qualified, key=lambda x: finite(x.get("economic_score"), 0), reverse=True):
        market = row["market"]
        episode_key = market + "|" + str(row.get("episode") or "") + "|" + str(row.get("entry_path") or "RAW")
        if episode_key in consumed:
            _append_allocation_action_once(portfolio, row, now, "EPISODE_ALREADY_CONSUMED")
            continue
        if any(p.get("market") == market for p in portfolio["positions"]):
            _append_allocation_action_once(portfolio, row, now, "MARKET_ALREADY_HELD")
            continue

        score = finite(row.get("economic_score"), 0)
        if len(portfolio["positions"]) >= MAX_SHADOW_POSITIONS:
            if not allow_score_rotation:
                _append_allocation_action_once(portfolio, row, now, "CAPACITY_FULL_ROTATION_DISABLED")
                continue
            weakest = min(portfolio["positions"], key=lambda p: finite(p.get("economic_score"), 0))
            weakest_score = finite(weakest.get("economic_score"), 0)
            if score < weakest_score + ROTATION_SCORE_DELTA:
                _append_allocation_action_once(portfolio, row, now, "CAPACITY_ROTATION_SCORE_DELTA_NOT_MET")
                continue
            current = finite((universe_by_market.get(weakest["market"]) or {}).get("price_eur"))
            if current is None:
                _append_allocation_action_once(portfolio, row, now, "CAPACITY_WEAKEST_MARK_MISSING")
                continue
            _close_position(portfolio, weakest, current, now, "ROTATE_TO_HIGHER_ECONOMIC_SCORE")

        sizing = row.get("sizing") or {}
        stake = finite(sizing.get("stake_eur"))
        entry = finite(row.get("entry_eur"))
        if stake is None or entry is None or stake <= 0 or entry <= 0:
            _append_allocation_action_once(portfolio, row, now, "INVALID_SIZING_OR_ENTRY")
            continue
        total_debit = stake * (1 + ENTRY_FEE_EST)
        if portfolio["cash_eur"] < total_debit:
            _append_allocation_action_once(portfolio, row, now, "INSUFFICIENT_SHADOW_CASH")
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
            "entry_path": row.get("entry_path") or "RAW",
            "decision_id": row.get("decision_id"),
            "last_stop_check_ts": now,
            "last_stop_check_at_utc": utc(now),
        })
        portfolio["actions"].append({
            "at_utc": utc(now),
            "action": "OPEN_V31_SHADOW",
            "market": market,
            "economic_score": score,
            "stake_eur": stake,
            "entry_path": row.get("entry_path") or "RAW",
            "decision_id": row.get("decision_id"),
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
    portfolio["stop_detection"] = "PARTIAL_MINUTE_PUBLIC_TRADES_PLUS_COMPLETED_1M_BARS"
    portfolio["score_rotation_enabled"] = allow_score_rotation
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
        "entry_path": "RAW_TIMING",
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
    portfolio_raw = read_json(PORTFOLIO_RAW, {}) or {}
    portfolio_reentry = read_json(PORTFOLIO_REENTRY, {}) or {}

    v3_candidates = v3_doc.get("candidates") or []
    news_mapping = v3_doc.get("news_mapping") or {}
    upstream_v3_architecture_version = v3_doc.get("architecture_version") or "legacy-unversioned-v3"
    upstream_v3_runtime_commit = v3_doc.get("runtime_commit")
    rows = universe.get("rows") or []
    universe_by_market = {x.get("market"): x for x in rows if x.get("market")}

    initial_cycle = not bool(state.get("initialized"))
    initial_timing_cycle = not bool(state.get("timing_lab_initialized"))
    state.setdefault("schema", "solaire_v31_state_v1")
    prior_architecture_version = state.get("architecture_version")
    architecture_rollover = prior_architecture_version != V31_ARCHITECTURE_VERSION
    prospective_censor = bool(initial_cycle or architecture_rollover)
    state["architecture_version"] = V31_ARCHITECTURE_VERSION
    if prior_architecture_version != V31_ARCHITECTURE_VERSION:
        state["architecture_migrated_at_utc"] = utc(now)
        state["architecture_migrated_from"] = prior_architecture_version or "legacy-unversioned"
    state.setdefault("started_ts", now)
    state.setdefault("started_at_utc", utc(now))
    state.setdefault("timing_lab_started_ts", now)
    state.setdefault("timing_lab_started_at_utc", utc(now))
    state.setdefault("markets", {})
    journal.setdefault("schema", "solaire_v31_prospective_journal_v1")
    journal.setdefault("started_ts", state["started_ts"])
    journal.setdefault("started_at_utc", state["started_at_utc"])
    journal.setdefault("events", [])
    for legacy_event in journal.get("events", []):
        legacy_event.setdefault("architecture_version", "legacy-pre-v3.1.1-unversioned")
        legacy_event.setdefault("upstream_v3_architecture_version", None)

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
        raw_execution = candidate.get("execution")
        thesis_execution = candidate.get("thesis_execution")
        thesis_reentry = bool(candidate.get("thesis_reentry_hypothesis"))
        selected_execution, entry_path = select_execution_path(candidate)
        selected_execution = execution_freshness(selected_execution, now)
        final = final_economic_score(preliminary, selected_execution)
        sizing = None
        if final.get("selectable"):
            sizing = shadow_sizing(
                finite(final.get("score"), 0),
                selected_execution or {},
                finite(row.get("quote_volume_24h_eur")),
            )
            if not sizing.get("valid"):
                final = {**final, "selectable": False, "reason": sizing.get("reason")}
            else:
                # V3 validates the same causal order-book snapshot. Reprice that
                # snapshot at the exact V3.1 notional before portfolio use.
                selected_execution = reprice_execution_for_stake(
                    selected_execution or {}, finite(sizing.get("stake_eur"), 0.0)
                )
                final = final_economic_score(preliminary, selected_execution)
                if not final.get("selectable"):
                    sizing = None
                else:
                    resized = shadow_sizing(
                        finite(final.get("score"), 0),
                        selected_execution or {},
                        finite(row.get("quote_volume_24h_eur")),
                    )
                    if not resized.get("valid"):
                        final = {**final, "selectable": False, "reason": resized.get("reason")}
                        sizing = None
                    else:
                        old_stake = finite(sizing.get("stake_eur"), 0.0)
                        new_stake = finite(resized.get("stake_eur"), 0.0)
                        if abs(new_stake - old_stake) > 0.01:
                            selected_execution = reprice_execution_for_stake(
                                selected_execution or {}, new_stake
                            )
                            final = final_economic_score(preliminary, selected_execution)
                        if final.get("selectable"):
                            sizing = resized
                            actual_risk = finite(
                                (selected_execution.get("plan") or {}).get("theoretical_loss_eur")
                            )
                            if actual_risk is not None:
                                sizing = {
                                    **sizing,
                                    "theoretical_risk_eur": round(actual_risk, 2),
                                    "final_stake_repriced": True,
                                }
                        else:
                            sizing = None
        ranked.append({
            "market": market,
            "price_eur": finite(row.get("price_eur")),
            "quote_volume_24h_eur": finite(row.get("quote_volume_24h_eur")),
            "preliminary": preliminary,
            "economic_score": finite(final.get("score"), 0),
            "selectable": bool(final.get("selectable")),
            "selection_reason": final.get("reason"),
            "execution_quality": final.get("execution_quality"),
            "execution": selected_execution,
            "entry_path": entry_path,
            "raw_execution": raw_execution,
            "thesis_execution": thesis_execution,
            "thesis_last_execution": candidate.get("thesis_last_execution"),
            "thesis_reentry_hypothesis": thesis_reentry,
            "persistent_thesis": candidate.get("persistent_thesis"),
            "near_miss_opportunity": candidate.get("near_miss_opportunity"),
            "credible_opportunity": candidate.get("credible_opportunity"),
            "opportunity_recovery": candidate.get("opportunity_recovery"),
            "news_positive_score": candidate.get("news_positive_score"),
            "news_negative_score": candidate.get("news_negative_score"),
            "external_score": candidate.get("external_score"),
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
            ms.pop("decision_recorded_paths", None)
            ms.pop("decision_state_by_path", None)
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
            "entry_path": row.get("entry_path"),
            "upstream_v3_architecture_version": upstream_v3_architecture_version,
            "legacy_v2_score_unused": row.get("v2_score"),
            "legacy_v3_opportunity_score_unused": row.get("v3_opportunity_score"),
            "left_censored_at_v31_t0": prospective_censor,
            "evaluations": {},
        }
        decision_key = row.get("entry_path") or "RAW"
        execution_reason = (execution or {}).get("reason") or "NOT_CHECKED"
        signature = "|".join([
            event_type,
            str(row.get("selection_reason") or ""),
            str(execution_reason),
        ])
        decision_states = ms.setdefault("decision_state_by_path", {})
        previous = decision_states.get(decision_key) or {}
        if previous.get("signature") != signature:
            ms["decision_sequence"] = int(ms.get("decision_sequence", 0)) + 1
            attempt_id = (
                f"{market}|{ms['episode']}|{decision_key}|"
                f"{ms['decision_sequence']}|{V31_ARCHITECTURE_VERSION}"
            )
            event["attempt_id"] = attempt_id
            event["decision_id"] = attempt_id
            event["transition_from"] = previous.get("event_type")
            event["transition_from_reason"] = previous.get("selection_reason")
            event["execution_reason"] = execution_reason
            event["execution"] = execution
            event["plan_available_ts"] = finite((execution or {}).get("available_ts"))
            event["plan_available_at_utc"] = (execution or {}).get("available_at_utc")
            event["execution_age_seconds"] = finite((execution or {}).get("execution_age_seconds"))
            if _append_event(journal, event):
                decision_states[decision_key] = {
                    "signature": signature,
                    "event_type": event_type,
                    "selection_reason": row.get("selection_reason"),
                    "execution_reason": execution_reason,
                    "attempt_id": attempt_id,
                }
                row["decision_id"] = attempt_id
        else:
            row["decision_id"] = previous.get("attempt_id")

        if row.get("selectable"):
            upstream_recovery = row.get("opportunity_recovery") or {}
            first_credible_ts = finite(upstream_recovery.get("first_credible_ts"))
            first_credible_price = finite(upstream_recovery.get("first_credible_price_eur"))
            selectable_key = None if first_credible_ts is None else round(first_credible_ts, 6)
            if selectable_key is not None and ms.get("first_selectable_credible_ts") != selectable_key:
                selectable_ts = now
                selectable_entry = finite(plan.get("entry_eur"))
                movement_to_selectable = None
                if (
                    selectable_entry is not None
                    and first_credible_price is not None
                    and first_credible_price > 0
                ):
                    movement_to_selectable = (
                        selectable_entry / first_credible_price - 1.0
                    ) * 100.0
                first_executable_ts = finite(upstream_recovery.get("first_executable_ts"))
                funnel = {
                    **upstream_recovery,
                    "first_selectable_ts": selectable_ts,
                    "first_selectable_at_utc": utc(selectable_ts),
                    "first_selectable_entry_eur": selectable_entry,
                    "first_selectable_score": row.get("economic_score"),
                    "first_selectable_path": row.get("entry_path") or "RAW",
                    "credible_to_selectable_delay_seconds": selectable_ts - first_credible_ts,
                    "movement_consumed_to_selectable_pct": movement_to_selectable,
                    "executable_to_selectable_delay_seconds": (
                        None if first_executable_ts is None
                        else selectable_ts - first_executable_ts
                    ),
                }
                recovery_event = {
                    "event_type": "OPPORTUNITY_RECOVERY_SELECTABLE",
                    "market": market,
                    "episode": ms["episode"],
                    "attempt_id": (
                        f"{market}|{ms['episode']}|FIRST_SELECTABLE|"
                        f"{selectable_key}|{V31_ARCHITECTURE_VERSION}"
                    ),
                    "decision_id": row.get("decision_id"),
                    "decision_ts": selectable_ts,
                    "decision_at_utc": utc(selectable_ts),
                    "price_eur": row.get("price_eur"),
                    "entry_eur": selectable_entry,
                    "stop_eur": finite(plan.get("stop_eur")),
                    "tp1_eur": finite(plan.get("tp1_eur")),
                    "stake_eur": finite((row.get("sizing") or {}).get("stake_eur")),
                    "economic_score": row.get("economic_score"),
                    "entry_path": row.get("entry_path") or "RAW",
                    "funnel": funnel,
                    "upstream_v3_architecture_version": upstream_v3_architecture_version,
                    "observation_only": True,
                    "left_censored_at_v31_t0": bool(
                        prospective_censor
                        or upstream_recovery.get("first_credible_left_censored")
                    ),
                    "evaluations": {},
                }
                if _append_event(journal, recovery_event):
                    ms["first_selectable_credible_ts"] = selectable_key
                    ms["first_selectable_at_utc"] = utc(selectable_ts)
                    ms["first_selectable_entry_eur"] = selectable_entry

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
    portfolio_client = None
    try:
        portfolio_client = PublicClient(timeout=8, retries=1, requests_per_second=10)
        portfolio_client.get("/time", cache=False)
    except Exception:
        portfolio_client = None

    portfolio = update_portfolio(
        portfolio, qualified_for_portfolio, universe_by_market, current_scores, now, client=portfolio_client
    )
    portfolio_persist = update_portfolio(
        portfolio_persist, qualified_persist, universe_by_market, current_scores, now, client=portfolio_client
    )
    portfolio_reclaim = update_portfolio(
        portfolio_reclaim, qualified_reclaim, universe_by_market, current_scores, now, client=portfolio_client
    )
    qualified_raw = [x for x in qualified_for_portfolio if (x.get("entry_path") or "RAW") == "RAW"]
    qualified_reentry = [x for x in qualified_for_portfolio if x.get("entry_path") == "THESIS_REENTRY"]
    portfolio_raw = update_portfolio(
        portfolio_raw, qualified_raw, universe_by_market, current_scores, now, client=portfolio_client
    )
    portfolio_reentry = update_portfolio(
        portfolio_reentry, qualified_reentry, universe_by_market, current_scores, now, client=portfolio_client
    )

    unchecked = [x for x in ranked if not (x.get("execution") or {}).get("ready") and (x.get("execution") is None)]
    candidate_doc = {
        "schema": "solaire_v31_candidates_v1",
        "generated_at_utc": utc(now),
        "architecture_version": V31_ARCHITECTURE_VERSION,
        "upstream_v3_architecture_version": upstream_v3_architecture_version,
        "upstream_v3_runtime_commit": upstream_v3_runtime_commit,
        "mode": "ECONOMIC_SELECTION_SHADOW",
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "frozen_v3_commit_role": "BENCHMARK_ONLY_NOT_LIVE_INPUT",
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
        "architecture_version": V31_ARCHITECTURE_VERSION,
        "upstream_v3_architecture_version": upstream_v3_architecture_version,
        "upstream_v3_runtime_commit": upstream_v3_runtime_commit,
        "frozen_v3_commit": FROZEN_V3_COMMIT,
        "frozen_v3_commit_role": "BENCHMARK_ONLY_NOT_LIVE_INPUT",
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
        "raw_portfolio_positions": len(portfolio_raw.get("positions", [])),
        "raw_portfolio_marked_value_eur": portfolio_raw.get("marked_value_eur"),
        "reentry_portfolio_positions": len(portfolio_reentry.get("positions", [])),
        "reentry_portfolio_marked_value_eur": portfolio_reentry.get("marked_value_eur"),
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
    journal["architecture_version"] = V31_ARCHITECTURE_VERSION
    journal["upstream_v3_architecture_version"] = upstream_v3_architecture_version
    journal["upstream_v3_runtime_commit"] = upstream_v3_runtime_commit
    journal["frozen_v3_commit"] = FROZEN_V3_COMMIT
    journal["frozen_v3_commit_role"] = "BENCHMARK_ONLY_NOT_LIVE_INPUT"
    journal["v3_timing_lab_commit"] = V3_TIMING_LAB_COMMIT
    journal["events"] = journal["events"][-10000:]

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(CANDIDATES, candidate_doc)
    atomic_json(PORTFOLIO, portfolio)
    atomic_json(PORTFOLIO_PERSIST, portfolio_persist)
    atomic_json(PORTFOLIO_RECLAIM, portfolio_reclaim)
    atomic_json(PORTFOLIO_RAW, portfolio_raw)
    atomic_json(PORTFOLIO_REENTRY, portfolio_reentry)
    atomic_json(STATUS, status)
    print("SOLAIRE_V31 " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
