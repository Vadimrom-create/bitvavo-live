"""Pure helpers for the Solaire full-funnel prospective audit.

This module is measurement-only.  It does not alter V2/V3/V3.1 decisions,
emails, orders, scores, thresholds or portfolios.
"""
from __future__ import annotations

from typing import Any

from research.common import finite

AUDIT_VERSION = "full-funnel-audit-v1-20260924"


def _n(value: Any, default: float = 0.0) -> float:
    out = finite(value)
    return default if out is None else out


def _execution(candidate: dict[str, Any], v31: dict[str, Any]) -> dict[str, Any] | None:
    """Pick the most decision-relevant execution object already computed upstream."""
    options = (
        v31.get("execution"),
        candidate.get("execution"),
        candidate.get("thesis_execution"),
        candidate.get("near_miss_execution"),
    )
    for item in options:
        if isinstance(item, dict):
            return item
    return None


def should_track(candidate: dict[str, Any], v31: dict[str, Any] | None = None) -> bool:
    """Track any evidence-bearing signal so losers remain available as controls."""
    v31 = v31 or {}
    early = candidate.get("early_quant") or {}
    v2_state = candidate.get("v2_state")
    execution = _execution(candidate, v31)
    return bool(
        candidate.get("credible_opportunity")
        or candidate.get("near_miss_opportunity")
        or candidate.get("entry_hypothesis")
        or candidate.get("thesis_reentry_hypothesis")
        or early.get("ready")
        or v2_state in {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}
        or execution is not None
        or v31.get("selectable")
        or (
            v31.get("selection_reason")
            and v31.get("selection_reason") != "NOT_CHECKED"
        )
    )


def classify_snapshot(
    candidate: dict[str, Any],
    v31: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Classify where an opportunity currently sits in the decision funnel."""
    v31 = v31 or {}
    execution = _execution(candidate, v31) or {}
    execution_ready = bool(execution.get("ready"))
    v2_state = candidate.get("v2_state")
    v2_confirmed = v2_state == "CONFIRMED_ACCELERATION"
    entry_hypothesis = bool(candidate.get("entry_hypothesis"))
    credible = bool(
        candidate.get("credible_opportunity")
        or candidate.get("near_miss_opportunity")
        or entry_hypothesis
        or v2_confirmed
    )
    selectable = bool(v31.get("selectable"))

    if selectable:
        stage = "SELECTABLE"
        loss_family = None
    elif execution_ready:
        stage = "EXECUTION_READY_REJECTED"
        loss_family = "POST_EXECUTION_SELECTION"
    elif v2_confirmed:
        stage = "CONFIRMED_WAITING_EXECUTION"
        loss_family = "POST_CONFIRMATION_EXECUTION"
    elif entry_hypothesis:
        stage = "ENTRY_HYPOTHESIS_WAITING_EXECUTION"
        loss_family = "PRE_CONFIRMATION_EXECUTION"
    elif credible:
        stage = "CREDIBLE_PRE_ENTRY"
        loss_family = "PRE_CONFIRMATION"
    else:
        stage = "EARLY_CONTROL"
        loss_family = "CONTROL_NOT_YET_CREDIBLE"

    selection_reason = v31.get("selection_reason")
    execution_reason = execution.get("reason") if execution else None
    if selectable:
        blocking_reason = None
    elif execution_ready:
        blocking_reason = selection_reason or "V31_NOT_SELECTABLE"
    elif execution_reason:
        blocking_reason = execution_reason
    elif not entry_hypothesis and not v2_confirmed:
        blocking_reason = "NO_ENTRY_HYPOTHESIS_YET"
    else:
        blocking_reason = selection_reason or "EXECUTION_NOT_READY_OR_NOT_CHECKED"

    return {
        "stage": stage,
        "loss_family": loss_family,
        "credible": credible,
        "entry_hypothesis": entry_hypothesis,
        "v2_state": v2_state,
        "v2_confirmed": v2_confirmed,
        "execution_ready": execution_ready,
        "selectable": selectable,
        "blocking_reason": blocking_reason,
        "selection_reason": selection_reason,
        "execution_reason": execution_reason,
        "economic_score": finite(v31.get("economic_score")),
        "v3_opportunity_score": finite(candidate.get("opportunity_score")),
        "v2_score": finite(candidate.get("v2_score")),
        "early_quant_score": finite((candidate.get("early_quant") or {}).get("score_0_10")),
        "early_quant_evidence_count": int((candidate.get("early_quant") or {}).get("evidence_count") or 0),
        "entry_path": v31.get("entry_path"),
    }


def pct_change(start: float | None, end: float | None) -> float | None:
    start = finite(start)
    end = finite(end)
    if start is None or end is None or start <= 0:
        return None
    return (end / start - 1.0) * 100.0


def _record_first(
    state: dict[str, Any],
    key: str,
    active: bool,
    now: float,
    price: float | None,
) -> None:
    if not active or state.get(f"first_{key}_ts") is not None:
        return
    state[f"first_{key}_ts"] = now
    state[f"first_{key}_price_eur"] = finite(price)


def advance_funnel_memory(
    prior: dict[str, Any] | None,
    *,
    snapshot: dict[str, Any],
    now: float,
    price_eur: float | None,
) -> tuple[dict[str, Any], bool]:
    """Advance one market's measurement-only funnel memory.

    Returns (new_state, transition_changed).
    """
    state = dict(prior or {})
    price = finite(price_eur)
    if not state:
        state = {
            "opened_ts": now,
            "origin_price_eur": price,
            "origin_stage": snapshot.get("stage"),
            "origin_reason": snapshot.get("blocking_reason"),
            "peak_eur": price,
            "low_eur": price,
            "transition_count": 0,
            "reason_history": [],
        }

    state["last_seen_ts"] = now
    state["last_price_eur"] = price
    if price is not None:
        peak = finite(state.get("peak_eur"), price)
        low = finite(state.get("low_eur"), price)
        state["peak_eur"] = max(peak, price)
        state["low_eur"] = min(low, price)

    origin = finite(state.get("origin_price_eur"))
    state["current_return_from_origin_pct"] = pct_change(origin, price)
    state["mfe_since_origin_pct"] = pct_change(origin, finite(state.get("peak_eur")))
    state["mae_since_origin_pct"] = pct_change(origin, finite(state.get("low_eur")))
    state["age_hours"] = max(0.0, now - _n(state.get("opened_ts"), now)) / 3600.0

    _record_first(state, "credible", bool(snapshot.get("credible")), now, price)
    _record_first(state, "entry_hypothesis", bool(snapshot.get("entry_hypothesis")), now, price)
    _record_first(state, "confirmed", bool(snapshot.get("v2_confirmed")), now, price)
    _record_first(state, "execution_ready", bool(snapshot.get("execution_ready")), now, price)
    _record_first(state, "selectable", bool(snapshot.get("selectable")), now, price)

    for key in ("credible", "entry_hypothesis", "confirmed", "execution_ready", "selectable"):
        stage_price = finite(state.get(f"first_{key}_price_eur"))
        state[f"movement_consumed_to_{key}_pct"] = pct_change(origin, stage_price)

    signature = "|".join([
        str(snapshot.get("stage") or ""),
        str(snapshot.get("blocking_reason") or ""),
        str(snapshot.get("entry_path") or ""),
    ])
    changed = signature != state.get("last_signature")
    if changed:
        state["transition_count"] = int(state.get("transition_count") or 0) + 1
        hist = list(state.get("reason_history") or [])
        hist.append({
            "ts": now,
            "price_eur": price,
            "stage": snapshot.get("stage"),
            "loss_family": snapshot.get("loss_family"),
            "blocking_reason": snapshot.get("blocking_reason"),
            "economic_score": snapshot.get("economic_score"),
            "v3_opportunity_score": snapshot.get("v3_opportunity_score"),
            "v2_score": snapshot.get("v2_score"),
            "entry_path": snapshot.get("entry_path"),
        })
        state["reason_history"] = hist[-40:]
        state["last_signature"] = signature

    state["current_stage"] = snapshot.get("stage")
    state["current_loss_family"] = snapshot.get("loss_family")
    state["current_blocking_reason"] = snapshot.get("blocking_reason")
    state["current_economic_score"] = snapshot.get("economic_score")
    state["current_v3_opportunity_score"] = snapshot.get("v3_opportunity_score")
    state["current_v2_score"] = snapshot.get("v2_score")
    state["current_entry_path"] = snapshot.get("entry_path")
    state["resolved_selectable"] = bool(
        state.get("first_selectable_ts") is not None
    )
    return state, changed


def stage_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        key = str(row.get("current_stage") or "UNKNOWN")
        out[key] = out.get(key, 0) + 1
    return out


def loss_family_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        key = str(row.get("current_loss_family") or "NONE")
        out[key] = out.get(key, 0) + 1
    return out
