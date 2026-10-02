"""Measurement-only registry for post-veto Solaire recovery experiments.

This module has no sender, mail or order integration. It keeps rejected episodes
alive for a fixed prospective TTL and records whether execution quality and
current signal quality recover. Current scan absence is an observation, never an
implicit invalidation.
"""
from __future__ import annotations

import copy
from typing import Any

from research.common import finite, utc

SCHEMA = "solaire_recovery_registry_shadow_v1"
TTL_SECONDS = 24 * 60 * 60
MAX_ATTEMPTS_PER_EPISODE = 400

TERMINAL_STATES = {
    "SHADOW_RECOVERY_CANDIDATE",
    "EXPIRED_24H",
    "INVALIDATED_NEW_EPISODE",
}

POLICY = {
    "ttl_seconds": TTL_SECONDS,
    "absence_invalidates": False,
    "one_chronological_proposal_per_episode": True,
    "confirmed_min_score": 6.5,
    "confirmed_min_evidence": 3,
    "building_min_score": 6.0,
    "building_min_evidence": 4,
    "candidate_requires_execution_pass": True,
    "candidate_requires_current_signal_quality_pass": True,
    "candidate_requires_prior_thesis_clear": True,
    "affects_detection": False,
    "affects_buy_gate": False,
    "affects_email": False,
    "affects_orders": False,
}


def new_registry() -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "policy": copy.deepcopy(POLICY),
        "episodes": {},
        "updated_at_utc": None,
    }


def normalize_registry(registry: dict[str, Any] | None) -> dict[str, Any]:
    result = copy.deepcopy(registry or {})
    result["schema"] = SCHEMA
    result["policy"] = copy.deepcopy(POLICY)
    result.setdefault("episodes", {})
    return result


def _signal_quality(row: dict[str, Any] | None) -> tuple[bool, str]:
    if not row:
        return False, "ABSENT_CURRENT_SCAN"
    state = row.get("signal_state")
    score = finite(row.get("signal_score"))
    evidence = int((row.get("acceleration") or {}).get("evidence_count") or 0)
    if (
        state == "CONFIRMED_ACCELERATION"
        and score is not None
        and score >= POLICY["confirmed_min_score"]
        and evidence >= POLICY["confirmed_min_evidence"]
    ):
        return True, "CONFIRMED_QUALITY_PASS"
    if (
        state == "BUILDING_ACCELERATION"
        and score is not None
        and score >= POLICY["building_min_score"]
        and evidence >= POLICY["building_min_evidence"]
    ):
        return True, "BUILDING_HQ_QUALITY_PASS"
    return False, "CURRENT_SIGNAL_NOT_QUALIFIED"


def _episode_number(row: dict[str, Any] | None):
    value = finite((row or {}).get("episode"))
    return int(value) if value is not None else None


def _attempt(
    record: dict[str, Any],
    row: dict[str, Any] | None,
    now: float,
    *,
    execution_pass: bool | None,
    execution_reason: str | None,
    plan: dict[str, Any] | None,
    prior_thesis_clear: bool | None,
    prior_thesis_status: str | None,
) -> dict[str, Any]:
    quality_pass, quality_reason = _signal_quality(row)
    return {
        "at_utc": utc(now),
        "at_ts": now,
        "market": record["market"],
        "current_signal_present": row is not None,
        "signal_state": (row or {}).get("signal_state"),
        "signal_score": finite((row or {}).get("signal_score")),
        "evidence_count": int(((row or {}).get("acceleration") or {}).get("evidence_count") or 0),
        "signal_quality_pass": quality_pass,
        "signal_quality_reason": quality_reason,
        "current_episode": _episode_number(row),
        "signal_price_eur": finite((row or {}).get("last")),
        "execution_pass": execution_pass,
        "execution_reason": execution_reason,
        "plan": copy.deepcopy(plan) if plan else None,
        "prior_thesis_clear": prior_thesis_clear,
        "prior_thesis_status": prior_thesis_status,
    }


def register_episode(
    registry: dict[str, Any] | None,
    event: dict[str, Any],
    source_row: dict[str, Any] | None,
    now: float,
) -> dict[str, Any]:
    registry = normalize_registry(registry)
    event_id = str(event.get("event_id") or "")
    market = str(event.get("market") or "")
    if not event_id or not market:
        return registry
    if event_id in registry["episodes"]:
        return registry

    rejected_ts = finite(event.get("rejected_ts"), now)
    record = {
        "event_id": event_id,
        "market": market,
        "state": "BLOCKED_BUT_ALIVE",
        "registered_at_utc": utc(now),
        "registered_at_ts": now,
        "first_veto_at_utc": event.get("rejected_at_utc") or utc(rejected_ts),
        "first_veto_ts": rejected_ts,
        "first_veto_reason": event.get("first_rejection_reason"),
        "veto_price_eur": finite(event.get("rejection_price_eur")),
        "source_episode": _episode_number(source_row),
        "source_signal": {
            "signal_state": (source_row or {}).get("signal_state", event.get("signal_state")),
            "signal_score": finite((source_row or {}).get("signal_score"), finite(event.get("signal_score"))),
            "evidence_count": int(
                ((source_row or {}).get("acceleration") or {}).get(
                    "evidence_count", event.get("evidence_count") or 0
                )
            ),
            "signal_price_eur": finite((source_row or {}).get("last"), finite(event.get("rejection_price_eur"))),
        },
        "expires_at_ts": rejected_ts + TTL_SECONDS,
        "expires_at_utc": utc(rejected_ts + TTL_SECONDS),
        "attempts": [],
        "first_execution_pass": None,
        "first_shadow_candidate": None,
        "proposal_count": 0,
        "closed": False,
        "close_reason": None,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }
    registry["episodes"][event_id] = record
    registry["updated_at_utc"] = utc(now)
    return registry


def observe_episode(
    registry: dict[str, Any] | None,
    event_id: str,
    row: dict[str, Any] | None,
    now: float,
    *,
    execution_pass: bool | None,
    execution_reason: str | None = None,
    plan: dict[str, Any] | None = None,
    prior_thesis_clear: bool | None = None,
    prior_thesis_status: str | None = None,
) -> dict[str, Any]:
    registry = normalize_registry(registry)
    record = registry["episodes"].get(event_id)
    if not record or record.get("closed"):
        registry["updated_at_utc"] = utc(now)
        return registry

    if now >= finite(record.get("expires_at_ts"), now + 1):
        record["state"] = "EXPIRED_24H"
        record["closed"] = True
        record["close_reason"] = "TTL_EXPIRED"
        record["closed_at_utc"] = utc(now)
        registry["updated_at_utc"] = utc(now)
        return registry

    source_episode = record.get("source_episode")
    current_episode = _episode_number(row)
    if (
        source_episode is not None
        and current_episode is not None
        and current_episode > source_episode
    ):
        record["state"] = "INVALIDATED_NEW_EPISODE"
        record["closed"] = True
        record["close_reason"] = "NEW_ACCELERATION_EPISODE"
        record["closed_at_utc"] = utc(now)
        record["invalidating_episode"] = current_episode
        registry["updated_at_utc"] = utc(now)
        return registry

    attempt = _attempt(
        record,
        row,
        now,
        execution_pass=execution_pass,
        execution_reason=execution_reason,
        plan=plan,
        prior_thesis_clear=prior_thesis_clear,
        prior_thesis_status=prior_thesis_status,
    )
    record.setdefault("attempts", []).append(attempt)
    record["attempts"] = record["attempts"][-MAX_ATTEMPTS_PER_EPISODE:]
    record["last_observed_at_utc"] = attempt["at_utc"]

    if row is None:
        record["state"] = "BLOCKED_BUT_ALIVE"
        record["last_status_reason"] = "SIGNAL_ABSENT_NOT_INVALIDATED"
        registry["updated_at_utc"] = utc(now)
        return registry

    if execution_pass is not True:
        record["state"] = "BLOCKED_BUT_ALIVE"
        record["last_status_reason"] = execution_reason or "EXECUTION_NOT_PASS"
        registry["updated_at_utc"] = utc(now)
        return registry

    if record.get("first_execution_pass") is None:
        plan_entry = finite((plan or {}).get("entry_eur"), finite(row.get("last")))
        veto_price = finite(record.get("veto_price_eur"))
        record["first_execution_pass"] = {
            "at_utc": attempt["at_utc"],
            "at_ts": now,
            "entry_eur": plan_entry,
            "delay_seconds": round(now - finite(record.get("first_veto_ts"), now), 3),
            "price_extension_from_veto_pct": (
                round((plan_entry / veto_price - 1) * 100, 6)
                if plan_entry is not None and veto_price is not None and veto_price > 0
                else None
            ),
            "signal_quality_pass": attempt["signal_quality_pass"],
            "signal_quality_reason": attempt["signal_quality_reason"],
        }

    if not attempt["signal_quality_pass"]:
        record["state"] = "TECHNICAL_PASS_SIGNAL_NOT_QUALIFIED"
        record["last_status_reason"] = attempt["signal_quality_reason"]
        registry["updated_at_utc"] = utc(now)
        return registry

    if prior_thesis_clear is not True:
        record["state"] = "TECHNICAL_PASS_PRIOR_THESIS_BLOCKED"
        record["last_status_reason"] = prior_thesis_status or "PRIOR_THESIS_STATUS_UNKNOWN"
        registry["updated_at_utc"] = utc(now)
        return registry

    # First chronological proposal only. This is a shadow candidate, not a BUY.
    if record.get("first_shadow_candidate") is None:
        record["first_shadow_candidate"] = {
            "at_utc": attempt["at_utc"],
            "at_ts": now,
            "market": record["market"],
            "signal_state": attempt["signal_state"],
            "signal_score": attempt["signal_score"],
            "evidence_count": attempt["evidence_count"],
            "signal_price_eur": attempt["signal_price_eur"],
            "plan": copy.deepcopy(plan) if plan else None,
        }
        record["proposal_count"] = 1

    record["state"] = "SHADOW_RECOVERY_CANDIDATE"
    record["closed"] = True
    record["close_reason"] = "FIRST_CHRONOLOGICAL_SHADOW_CANDIDATE"
    record["closed_at_utc"] = utc(now)
    registry["updated_at_utc"] = utc(now)
    return registry


def summarize(registry: dict[str, Any] | None) -> dict[str, Any]:
    registry = normalize_registry(registry)
    episodes = list(registry["episodes"].values())
    by_state: dict[str, int] = {}
    for record in episodes:
        state = str(record.get("state") or "UNKNOWN")
        by_state[state] = by_state.get(state, 0) + 1
    return {
        "schema": SCHEMA,
        "episodes": len(episodes),
        "open": sum(not bool(record.get("closed")) for record in episodes),
        "shadow_candidates": sum(
            record.get("state") == "SHADOW_RECOVERY_CANDIDATE" for record in episodes
        ),
        "technical_passes": sum(
            record.get("first_execution_pass") is not None for record in episodes
        ),
        "by_state": by_state,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }
