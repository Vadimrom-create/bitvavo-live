#!/usr/bin/env python3
"""Prospective measurement-only audit of the complete Solaire decision funnel.

V2 real alerts, RAW V3/V3.1, thesis re-entry and near-miss diagnostics are kept
as separate paths.  Once an episode starts, its price trajectory is followed for
four hours even if the signal disappears.

This script changes no score, threshold, alert, order or portfolio decision.
"""
from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.solaire_funnel_audit import (
    AUDIT_VERSION,
    FIXED_HORIZON_SECONDS,
    advance_funnel_memory,
    classify_path_snapshots,
    loss_family_counts,
    observe_price_only,
    stage_counts,
)

V3_CANDIDATES = "solaire_v3_candidates.json"
V31_CANDIDATES = "solaire_v31_candidates.json"
UNIVERSE = "production_universe_snapshot.json"
V3_JOURNAL = "solaire_v3_journal.json"
V31_PORTFOLIO = "solaire_v31_portfolio.json"
PRODUCTION_JOURNAL = "production_decision_journal.json"
PRODUCTION_ALERT_STATUS = "production_alert_status.json"

STATE = "solaire_funnel_audit_state.json"
JOURNAL = "solaire_funnel_audit_journal.json"
REPORT = "solaire_funnel_audit_report.json"
STATUS = "solaire_funnel_audit_status.json"

MAX_SOURCE_AGE_SECONDS = 30 * 60
MAX_JOURNAL_EVENTS = 50000
MAX_EPISODES_RETAINED = 5000


def _ts(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return finite(value)


def _source_health(name: str, doc: dict[str, Any], now: float, *, rows_key: str | None = None) -> dict[str, Any]:
    if not isinstance(doc, dict) or not doc:
        return {"source": name, "ok": False, "reason": "MISSING_DOCUMENT"}
    if rows_key is not None:
        rows = doc.get(rows_key)
        if not isinstance(rows, list) or not rows:
            return {"source": name, "ok": False, "reason": "MISSING_ROWS"}
    stamp = (
        _ts(doc.get("generated_at_utc"))
        or _ts(doc.get("checked_at_utc"))
        or _ts(doc.get("updated_at_utc"))
    )
    if stamp is None:
        return {"source": name, "ok": False, "reason": "MISSING_TIMESTAMP"}
    age = now - stamp
    if age < -300:
        return {"source": name, "ok": False, "reason": "FUTURE_TIMESTAMP", "age_seconds": age}
    if age > MAX_SOURCE_AGE_SECONDS:
        return {"source": name, "ok": False, "reason": "STALE_SOURCE", "age_seconds": age}
    return {"source": name, "ok": True, "age_seconds": age}


def _candidate_price(v3: dict[str, Any], v31: dict[str, Any], universe: dict[str, Any]) -> float | None:
    return finite(
        universe.get("price_eur"),
        finite(v3.get("price_eur"), finite(v31.get("price_eur"))),
    )


def _latest_near_miss_checks(v3_journal: dict[str, Any]) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for event in v3_journal.get("events", []) or []:
        if event.get("event_type") != "NEAR_MISS_EXECUTION_OBSERVATION":
            continue
        market = event.get("market")
        if not market:
            continue
        ts = finite(event.get("decision_ts"), 0.0)
        previous = latest.get(market)
        if previous is None or ts >= finite(previous.get("decision_ts"), 0.0):
            latest[market] = event
    return latest


def _portfolio_actions(
    portfolio: dict[str, Any],
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    opened: dict[str, dict[str, Any]] = {}
    rejected: dict[str, dict[str, Any]] = {}
    open_positions: dict[str, dict[str, Any]] = {}
    closed_positions: dict[str, dict[str, Any]] = {}
    for action in portfolio.get("actions", []) or []:
        decision_id = action.get("decision_id")
        if not decision_id:
            continue
        kind = str(action.get("action") or "")
        if kind == "OPEN_V31_SHADOW":
            opened[str(decision_id)] = action
        elif kind.startswith("ALLOCATION_"):
            rejected[str(decision_id)] = action
    for position in portfolio.get("positions", []) or []:
        decision_id = position.get("decision_id")
        if decision_id:
            open_positions[str(decision_id)] = position
    for position in portfolio.get("closed", []) or []:
        decision_id = position.get("decision_id")
        if decision_id:
            closed_positions[str(decision_id)] = position
    return opened, rejected, open_positions, closed_positions


def _alert_records(prod_journal: dict[str, Any], alert_status: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    rows: dict[str, list[dict[str, Any]]] = {}
    for entry in prod_journal.get("entries", []) or []:
        if entry.get("decision_type") != "BUY_SENT" or not entry.get("market"):
            continue
        item = dict(entry)
        item["alert_ts"] = finite(entry.get("decision_ts"))
        rows.setdefault(entry["market"], []).append(item)

    if alert_status.get("email") == "DELIVERY_COMPLETED":
        stamp = _ts(alert_status.get("checked_at_utc"))
        deliveries = alert_status.get("deliveries")
        if not isinstance(deliveries, list) or not deliveries:
            deliveries = [alert_status] if alert_status.get("market") else []
        for delivery in deliveries:
            market = delivery.get("market")
            if not market:
                continue
            rows.setdefault(market, []).append({
                "market": market,
                "decision_type": "BUY_SENT",
                "alert_ts": stamp,
                "entry_eur": finite(delivery.get("entry_eur")),
                "stop_eur": finite(delivery.get("stop_eur")),
                "tp1_eur": finite(delivery.get("tp1_eur")),
                "tp2_eur": finite(delivery.get("tp2_eur")),
                "stake_eur": finite(delivery.get("stake_eur")),
                "source": "CURRENT_PRODUCTION_ALERT_STATUS",
            })

    for market in rows:
        rows[market].sort(key=lambda x: finite(x.get("alert_ts"), 0.0))
    return rows


def _record_allocation(
    memory: dict[str, Any],
    snapshot: dict[str, Any],
    opened: dict[str, dict[str, Any]],
    rejected: dict[str, dict[str, Any]],
    open_positions: dict[str, dict[str, Any]],
    closed_positions: dict[str, dict[str, Any]],
) -> None:
    decision_id = snapshot.get("decision_id")
    if not decision_id:
        if snapshot.get("selectable"):
            memory["current_allocation_status"] = "SELECTABLE_DECISION_ID_MISSING"
        return
    action = opened.get(str(decision_id))
    if action is not None:
        if memory.get("first_allocated_ts") is None:
            memory["first_allocated_ts"] = _ts(action.get("at_utc"))
            memory["first_allocated_at_utc"] = action.get("at_utc")
            memory["first_allocated_decision_id"] = decision_id
            memory["first_allocated_entry_eur"] = finite(snapshot.get("execution_entry_eur"))
            memory["first_allocated_plan_id"] = snapshot.get("plan_id")
        memory["current_allocation_status"] = "ALLOCATED_SHADOW"
        memory["current_allocation_reason"] = None
        closed = closed_positions.get(str(decision_id))
        opened_position = open_positions.get(str(decision_id))
        if closed is not None:
            entry = finite(closed.get("entry_eur"))
            exit_eur = finite(closed.get("exit_eur"))
            gross = None
            if entry is not None and entry > 0 and exit_eur is not None:
                gross = (exit_eur / entry - 1.0) * 100.0
            memory["shadow_simulation_result"] = {
                "status": "CLOSED",
                "closed_ts": finite(closed.get("closed_ts")),
                "closed_at_utc": closed.get("closed_at_utc"),
                "entry_eur": entry,
                "exit_eur": exit_eur,
                "gross_return_pct": gross,
                "close_reason": closed.get("close_reason"),
                "stop_eur": finite(closed.get("stop_eur")),
                "fees_are_accounted_at_portfolio_cash_level": True,
            }
        elif opened_position is not None:
            memory["shadow_simulation_result"] = {
                "status": "OPEN",
                "opened_ts": finite(opened_position.get("opened_ts")),
                "opened_at_utc": opened_position.get("opened_at_utc"),
                "entry_eur": finite(opened_position.get("entry_eur")),
                "stop_eur": finite(opened_position.get("stop_eur")),
                "mark_eur": finite(opened_position.get("mark_eur")),
            }
        return
    skip = rejected.get(str(decision_id))
    if skip is not None:
        memory["current_allocation_status"] = "NOT_ALLOCATED"
        memory["current_allocation_reason"] = skip.get("reason") or skip.get("action")
        return
    if snapshot.get("selectable"):
        memory["current_allocation_status"] = "SELECTABLE_ALLOCATION_NOT_OBSERVED"
        memory["current_allocation_reason"] = "NO_MATCHING_PORTFOLIO_ACTION"


def _record_alert(memory: dict[str, Any], alerts: list[dict[str, Any]]) -> None:
    opened = finite(memory.get("opened_ts"), 0.0)
    horizon_end = finite(memory.get("horizon_end_ts"), opened + FIXED_HORIZON_SECONDS)
    valid = [
        x for x in alerts
        if finite(x.get("alert_ts")) is not None
        and opened <= finite(x.get("alert_ts")) <= horizon_end
    ]
    if not valid:
        return
    first = valid[0]
    if memory.get("first_alerted_ts") is None:
        memory["first_alerted_ts"] = finite(first.get("alert_ts"))
        memory["first_alerted_at_utc"] = utc(memory["first_alerted_ts"])
        memory["first_alert_entry_eur"] = finite(first.get("entry_eur"))
        memory["first_alert_stop_eur"] = finite(first.get("stop_eur"))
        memory["first_alert_tp1_eur"] = finite(first.get("tp1_eur"))
        memory["first_alert_stake_eur"] = finite(first.get("stake_eur"))
    memory["current_alert_status"] = "BUY_SENT"
    evaluations = first.get("evaluations") or {}
    if evaluations:
        memory["production_alert_evaluations"] = evaluations
        four_hour = evaluations.get("4")
        if isinstance(four_hour, dict):
            memory["production_alert_4h_result"] = four_hour


def _snapshot_event(
    *,
    episode: dict[str, Any],
    snapshot: dict[str, Any] | None,
    now: float,
    price: float | None,
    cycle_id: str,
    path_present: bool,
) -> dict[str, Any]:
    snapshot = snapshot or {}
    return {
        "event_type": "FUNNEL_CYCLE_SNAPSHOT",
        "attempt_id": f"{episode['episode_id']}|CYCLE|{cycle_id}",
        "episode_id": episode["episode_id"],
        "market": episode["market"],
        "path": episode["path"],
        "decision_ts": now,
        "decision_at_utc": utc(now),
        "cycle_id": cycle_id,
        "path_present": path_present,
        "scan_price_eur": price,
        "stage": snapshot.get("stage") if path_present else "SIGNAL_ABSENT_CONTINUING_FIXED_HORIZON",
        "loss_family": snapshot.get("loss_family") if path_present else "OUTCOME_FOLLOWUP",
        "blocking_reason": snapshot.get("blocking_reason") if path_present else None,
        "economic_score": snapshot.get("economic_score") if path_present else None,
        "v3_opportunity_score": snapshot.get("v3_opportunity_score") if path_present else None,
        "v2_score": snapshot.get("v2_score") if path_present else None,
        "early_quant_score": snapshot.get("early_quant_score") if path_present else None,
        "execution_ready": snapshot.get("execution_ready") if path_present else None,
        "selectable": snapshot.get("selectable") if path_present else None,
        "selection_checked": snapshot.get("selection_checked") if path_present else None,
        "plan_id": snapshot.get("plan_id") if path_present else None,
        "plan_available_ts": snapshot.get("plan_available_ts") if path_present else None,
        "execution_entry_eur": snapshot.get("execution_entry_eur") if path_present else None,
        "stop_eur": snapshot.get("stop_eur") if path_present else None,
        "tp1_eur": snapshot.get("tp1_eur") if path_present else None,
        "spread_pct": snapshot.get("spread_pct") if path_present else None,
        "depth_slippage_pct": snapshot.get("depth_slippage_pct") if path_present else None,
        "decision_id": snapshot.get("decision_id") if path_present else None,
        "current_allocation_status": episode.get("current_allocation_status"),
        "current_alert_status": episode.get("current_alert_status"),
        "current_return_from_origin_pct": episode.get("current_return_from_origin_pct"),
        "mfe_since_origin_pct_scan_sampled": episode.get("mfe_since_origin_pct"),
        "mae_since_origin_pct_scan_sampled": episode.get("mae_since_origin_pct"),
        "measurement_note": "price extrema are scan-sampled; fixed-horizon continuity no longer depends on signal persistence",
        "observation_only": True,
    }


def main() -> int:
    now = time.time()
    cycle_id = f"{now:.6f}"

    v3_doc = read_json(V3_CANDIDATES, {}) or {}
    v31_doc = read_json(V31_CANDIDATES, {}) or {}
    universe_doc = read_json(UNIVERSE, {}) or {}
    v3_journal = read_json(V3_JOURNAL, {}) or {}
    v31_portfolio = read_json(V31_PORTFOLIO, {}) or {}
    prod_journal = read_json(PRODUCTION_JOURNAL, {}) or {}
    alert_status = read_json(PRODUCTION_ALERT_STATUS, {}) or {}
    state = read_json(STATE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}

    v3_rows = v3_doc.get("candidates") or []
    v31_rows = v31_doc.get("candidates") or []
    universe_rows = universe_doc.get("rows") or []
    v3_by_market = {x.get("market"): x for x in v3_rows if x.get("market")}
    v31_by_market = {x.get("market"): x for x in v31_rows if x.get("market")}
    universe_by_market = {x.get("market"): x for x in universe_rows if x.get("market")}

    health = [
        _source_health("V3_CANDIDATES", v3_doc, now, rows_key="candidates"),
        _source_health("V31_CANDIDATES", v31_doc, now, rows_key="candidates"),
        _source_health("UNIVERSE", universe_doc, now, rows_key="rows"),
    ]
    inputs_ok = all(x.get("ok") for x in health)

    prior_version = state.get("architecture_version")
    rollover = prior_version != AUDIT_VERSION
    if rollover:
        state = {
            "schema": "solaire_funnel_audit_state_v2",
            "architecture_version": AUDIT_VERSION,
            "prospective_start_ts": now,
            "prospective_start_at_utc": utc(now),
            "architecture_migrated_from": prior_version,
            "episodes": {},
            "active_by_key": {},
        }
    state.setdefault("episodes", {})
    state.setdefault("active_by_key", {})
    state["architecture_version"] = AUDIT_VERSION

    journal.setdefault("schema", "solaire_funnel_audit_journal_v2")
    journal.setdefault("events", [])
    journal.setdefault("started_ts", now)
    journal.setdefault("started_at_utc", utc(now))
    event_keys = {
        str(x.get("attempt_id"))
        for x in journal.get("events", [])
        if x.get("attempt_id")
    }

    def append_event(event: dict[str, Any]) -> None:
        event.setdefault("architecture_version", AUDIT_VERSION)
        key = str(event.get("attempt_id") or "")
        if key and key in event_keys:
            return
        journal["events"].append(event)
        if key:
            event_keys.add(key)

    near_checks = _latest_near_miss_checks(v3_journal)
    opened_actions, rejected_actions, open_positions, closed_positions = _portfolio_actions(v31_portfolio)
    alerts_by_market = _alert_records(prod_journal, alert_status)

    # First, continue every already-open episode with the full-universe price,
    # independent of whether its signal remains present.
    completed_this_cycle = 0
    for key, episode_id in list(state["active_by_key"].items()):
        episode = state["episodes"].get(episode_id)
        if not episode:
            state["active_by_key"].pop(key, None)
            continue
        market = episode.get("market")
        price = finite((universe_by_market.get(market) or {}).get("price_eur"))
        episode = observe_price_only(episode, now=now, price_eur=price)
        state["episodes"][episode_id] = episode
        if now >= finite(episode.get("horizon_end_ts"), now + 1):
            episode["active"] = False
            episode["completed_ts"] = now
            episode["completed_at_utc"] = utc(now)
            episode["fixed_horizon_complete"] = True
            episode["fixed_horizon_final_price_eur"] = price
            episode["fixed_horizon_return_pct_scan_sampled"] = episode.get("current_return_from_origin_pct")
            state["active_by_key"].pop(key, None)
            completed_this_cycle += 1

    current_episode_ids: set[str] = set()
    if inputs_ok:
        markets = sorted(set(v3_by_market) | set(v31_by_market))
        for market in markets:
            v3 = v3_by_market.get(market) or {}
            v31 = v31_by_market.get(market) or {}
            universe = universe_by_market.get(market) or {}
            near_event = near_checks.get(market) or {}
            near_execution = near_event.get("execution") if isinstance(near_event, dict) else None
            snapshots = classify_path_snapshots(
                v3,
                v31,
                near_miss_execution=near_execution,
            )
            if not snapshots:
                continue
            price = _candidate_price(v3, v31, universe)

            for snapshot in snapshots:
                path = snapshot["path"]
                key = market + "|" + path
                episode_id = state["active_by_key"].get(key)
                episode = state["episodes"].get(episode_id) if episode_id else None

                if episode is None:
                    episode_id = f"{market}|{path}|{int(now * 1000)}"
                    episode, changed = advance_funnel_memory(
                        None,
                        snapshot=snapshot,
                        now=now,
                        price_eur=price,
                    )
                    episode.update({
                        "episode_id": episode_id,
                        "market": market,
                        "path": path,
                        "active": True,
                        "opened_at_utc": utc(now),
                        "fixed_horizon_seconds": FIXED_HORIZON_SECONDS,
                        "left_censored": rollover,
                    })
                    state["episodes"][episode_id] = episode
                    state["active_by_key"][key] = episode_id
                else:
                    episode, changed = advance_funnel_memory(
                        episode,
                        snapshot=snapshot,
                        now=now,
                        price_eur=price,
                    )
                    episode["active"] = True
                    state["episodes"][episode_id] = episode

                _record_allocation(
                    episode,
                    snapshot,
                    opened_actions,
                    rejected_actions,
                    open_positions,
                    closed_positions,
                )
                if path == "V2_REAL":
                    _record_alert(episode, alerts_by_market.get(market, []))

                episode["last_path_present_ts"] = now
                episode["last_path_present_at_utc"] = utc(now)
                episode["current_stage"] = snapshot.get("stage")
                episode["current_loss_family"] = snapshot.get("loss_family")
                episode["current_blocking_reason"] = snapshot.get("blocking_reason")
                episode["source_v3_architecture_version"] = v3_doc.get("architecture_version")
                episode["source_v31_architecture_version"] = v31_doc.get("architecture_version")
                state["episodes"][episode_id] = episode
                current_episode_ids.add(episode_id)

                append_event(_snapshot_event(
                    episode=episode,
                    snapshot=snapshot,
                    now=now,
                    price=price,
                    cycle_id=cycle_id,
                    path_present=True,
                ))

                if changed:
                    append_event({
                        "event_type": "FUNNEL_STAGE_TRANSITION",
                        "attempt_id": f"{episode_id}|TRANSITION|{episode.get('transition_count')}",
                        "episode_id": episode_id,
                        "market": market,
                        "path": path,
                        "decision_ts": now,
                        "decision_at_utc": utc(now),
                        "scan_price_eur": price,
                        "stage": snapshot.get("stage"),
                        "loss_family": snapshot.get("loss_family"),
                        "blocking_reason": snapshot.get("blocking_reason"),
                        "economic_score": snapshot.get("economic_score"),
                        "v3_opportunity_score": snapshot.get("v3_opportunity_score"),
                        "v2_score": snapshot.get("v2_score"),
                        "execution_ready": snapshot.get("execution_ready"),
                        "selectable": snapshot.get("selectable"),
                        "selection_checked": snapshot.get("selection_checked"),
                        "plan_id": snapshot.get("plan_id"),
                        "plan_available_ts": snapshot.get("plan_available_ts"),
                        "execution_entry_eur": snapshot.get("execution_entry_eur"),
                        "stop_eur": snapshot.get("stop_eur"),
                        "tp1_eur": snapshot.get("tp1_eur"),
                        "decision_id": snapshot.get("decision_id"),
                        "current_allocation_status": episode.get("current_allocation_status"),
                        "current_alert_status": episode.get("current_alert_status"),
                        "observation_only": True,
                    })

    # Episodes whose signal disappeared remain sampled until their fixed horizon.
    for key, episode_id in list(state["active_by_key"].items()):
        if episode_id in current_episode_ids:
            continue
        episode = state["episodes"].get(episode_id)
        if not episode:
            continue
        market = episode.get("market")
        price = finite((universe_by_market.get(market) or {}).get("price_eur"))
        append_event(_snapshot_event(
            episode=episode,
            snapshot=None,
            now=now,
            price=price,
            cycle_id=cycle_id,
            path_present=False,
        ))

    episodes = list(state["episodes"].values())
    episodes.sort(key=lambda x: finite(x.get("opened_ts"), 0.0), reverse=True)
    if len(episodes) > MAX_EPISODES_RETAINED:
        keep_ids = {x["episode_id"] for x in episodes[:MAX_EPISODES_RETAINED]}
        state["episodes"] = {
            k: v for k, v in state["episodes"].items() if k in keep_ids
        }
        state["active_by_key"] = {
            k: v for k, v in state["active_by_key"].items() if v in keep_ids
        }
        episodes = episodes[:MAX_EPISODES_RETAINED]

    active = [x for x in episodes if x.get("active")]
    completed = [x for x in episodes if x.get("fixed_horizon_complete")]
    actionable_paths = [x for x in active if x.get("path") in {"V2_REAL", "RAW", "THESIS_REENTRY"}]
    unresolved = [
        x for x in actionable_paths
        if (
            (x.get("path") == "V2_REAL" and x.get("first_alerted_ts") is None)
            or (
                x.get("path") in {"RAW", "THESIS_REENTRY"}
                and x.get("first_allocated_ts") is None
            )
        )
    ]
    high_mfe_unresolved = [
        x for x in unresolved
        if finite(x.get("mfe_since_origin_pct"), -999.0) >= 10.0
    ]
    high_mfe_unresolved.sort(
        key=lambda x: finite(x.get("mfe_since_origin_pct"), -999.0),
        reverse=True,
    )

    path_counts: dict[str, int] = {}
    for row in active:
        path = str(row.get("path") or "UNKNOWN")
        path_counts[path] = path_counts.get(path, 0) + 1

    allocation_counts: dict[str, int] = {}
    for row in active:
        status = str(row.get("current_allocation_status") or "NONE")
        allocation_counts[status] = allocation_counts.get(status, 0) + 1

    report = {
        "schema": "solaire_funnel_audit_report_v2",
        "generated_at_utc": utc(now),
        "architecture_version": AUDIT_VERSION,
        "mode": "MEASUREMENT_ONLY",
        "method_note": (
            "Independent paths; exact execution-plan prices; every active episode "
            "continues for a fixed four-hour horizon even after signal disappearance. "
            "MFE/MAE in this report are scan-sampled diagnostics, not candle-exact outcomes."
        ),
        "input_health": health,
        "inputs_ok": inputs_ok,
        "source_v3_architecture_version": v3_doc.get("architecture_version"),
        "source_v31_architecture_version": v31_doc.get("architecture_version"),
        "stage_counts": stage_counts(active),
        "loss_family_counts": loss_family_counts(active),
        "path_counts": path_counts,
        "allocation_status_counts": allocation_counts,
        "active_episode_count": len(active),
        "completed_fixed_4h_count": len(completed),
        "completed_this_cycle": completed_this_cycle,
        "unresolved_actionable_count": len(unresolved),
        "high_mfe_unresolved_count": len(high_mfe_unresolved),
        "high_mfe_unresolved": high_mfe_unresolved[:100],
        "active_episodes": active[:1000],
        "recent_completed_episodes": completed[:500],
        "research_only": True,
        "affects_v2": False,
        "affects_v3": False,
        "affects_v31": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    status = {
        "schema": "solaire_funnel_audit_status_v2",
        "checked_at_utc": utc(now),
        "status": "OK" if inputs_ok else "DEGRADED_INPUT_GAP",
        "architecture_version": AUDIT_VERSION,
        "mode": "MEASUREMENT_ONLY",
        "input_health": health,
        "active_episode_count": len(active),
        "completed_fixed_4h_count": len(completed),
        "unresolved_actionable_count": len(unresolved),
        "high_mfe_unresolved_count": len(high_mfe_unresolved),
        "path_counts": path_counts,
        "stage_counts": report["stage_counts"],
        "loss_family_counts": report["loss_family_counts"],
        "research_only": True,
        "affects_v2": False,
        "affects_v3": False,
        "affects_v31": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    state["updated_at_utc"] = utc(now)
    journal["updated_at_utc"] = utc(now)
    journal["architecture_version"] = AUDIT_VERSION
    journal["events"] = journal["events"][-MAX_JOURNAL_EVENTS:]

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(REPORT, report)
    atomic_json(STATUS, status)

    print("SOLAIRE_FUNNEL_AUDIT " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
