"""Pure helpers for the Solaire full-funnel prospective audit.

Measurement-only.  This module must never alter V2/V3/V3.1 decisions, scores,
thresholds, alerts, orders or portfolio policy.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

from research.common import finite

AUDIT_VERSION = "full-funnel-audit-v2-measurement-hardening-20260925"
FIXED_HORIZON_SECONDS = 4 * 3600
PATHS = ("V2_REAL", "RAW", "THESIS_REENTRY", "NEAR_MISS_DIAGNOSTIC")


def pct_change(start: float | None, end: float | None) -> float | None:
    start = finite(start)
    end = finite(end)
    if start is None or end is None or start <= 0:
        return None
    return (end / start - 1.0) * 100.0


def _plan_id(path: str, execution: dict[str, Any] | None) -> str | None:
    if not isinstance(execution, dict):
        return None
    plan = execution.get("plan") or {}
    payload = {
        "path": path,
        "available_ts": finite(execution.get("available_ts")),
        "entry_eur": finite(plan.get("entry_eur")),
        "stop_eur": finite(plan.get("stop_eur")),
        "tp1_eur": finite(plan.get("tp1_eur")),
        "tp2_eur": finite(plan.get("tp2_eur")),
        "stake_eur": finite(plan.get("stake_eur")),
    }
    if all(v is None for k, v in payload.items() if k != "path"):
        return None
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def execution_snapshot(path: str, execution: dict[str, Any] | None) -> dict[str, Any]:
    execution = execution if isinstance(execution, dict) else {}
    plan = execution.get("plan") or {}
    depth = execution.get("depth") or {}
    return {
        "execution_ready": bool(execution.get("ready")),
        "execution_reason": execution.get("reason"),
        "plan_id": _plan_id(path, execution),
        "plan_available_ts": finite(execution.get("available_ts")),
        "plan_available_at_utc": execution.get("available_at_utc"),
        "execution_entry_eur": finite(plan.get("entry_eur")),
        "stop_eur": finite(plan.get("stop_eur")),
        "tp1_eur": finite(plan.get("tp1_eur")),
        "tp2_eur": finite(plan.get("tp2_eur")),
        "stake_eur": finite(plan.get("stake_eur")),
        "stop_distance_pct": finite(plan.get("stop_distance_pct")),
        "net_rr_tp1": finite(plan.get("net_rr_tp1")),
        "spread_pct": finite(execution.get("spread_pct")),
        "depth_slippage_pct": finite(depth.get("depth_slippage_pct")),
        "execution_available": bool(execution),
    }


def _selected_for(path: str, v31: dict[str, Any]) -> bool:
    entry_path = str(v31.get("entry_path") or "")
    if path == "RAW":
        return entry_path == "RAW"
    if path == "THESIS_REENTRY":
        return entry_path.startswith("THESIS_REENTRY")
    return False


def _classify_execution_path(
    *,
    path: str,
    hypothesis: bool,
    credible: bool,
    execution: dict[str, Any] | None,
    v31: dict[str, Any],
) -> dict[str, Any]:
    ex = execution_snapshot(path, execution)
    selected = _selected_for(path, v31)
    selectable = bool(selected and v31.get("selectable"))
    selection_reason = v31.get("selection_reason") if selected else None
    selection_checked = bool(
        selected
        and selection_reason
        and selection_reason != "NOT_CHECKED"
    )

    if selectable:
        stage = f"{path}_SELECTABLE"
        family = None
        blocking = None
    elif ex["execution_ready"] and selection_checked:
        stage = f"{path}_EXECUTION_READY_REJECTED"
        family = "POST_EXECUTION_SELECTION"
        blocking = selection_reason or "V31_REJECTED"
    elif ex["execution_ready"]:
        stage = f"{path}_EXECUTION_READY_UNCHECKED"
        family = "EXECUTION_READY_NOT_ECONOMICALLY_CHECKED"
        blocking = "PATH_NOT_SELECTED_OR_NOT_CHECKED_BY_V31"
    elif hypothesis:
        stage = f"{path}_WAITING_EXECUTION"
        family = "EXECUTION"
        blocking = ex["execution_reason"] or "EXECUTION_NOT_READY_OR_NOT_CHECKED"
    elif credible:
        stage = f"{path}_CREDIBLE_PRE_ENTRY"
        family = "PRE_ENTRY"
        blocking = "NO_ENTRY_HYPOTHESIS_YET"
    else:
        stage = f"{path}_CONTROL"
        family = "CONTROL"
        blocking = None

    return {
        "path": path,
        "stage": stage,
        "loss_family": family,
        "credible": credible,
        "entry_hypothesis": hypothesis,
        "v2_state": v31.get("v2_state"),
        "v2_confirmed": False,
        "selectable": selectable,
        "selection_checked": selection_checked,
        "selection_reason": selection_reason,
        "economic_score": finite(v31.get("economic_score")),
        "v3_opportunity_score": finite(v31.get("v3_opportunity_score")),
        "v2_score": finite(v31.get("v2_score")),
        "entry_path": v31.get("entry_path"),
        "decision_id": v31.get("decision_id"),
        "blocking_reason": blocking,
        **ex,
    }


def classify_path_snapshots(
    candidate: dict[str, Any],
    v31: dict[str, Any] | None = None,
    *,
    near_miss_execution: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Return independent path snapshots instead of merging incompatible paths."""
    v31 = v31 or {}
    out: list[dict[str, Any]] = []
    early = candidate.get("early_quant") or {}
    v2_state = candidate.get("v2_state") or v31.get("v2_state")
    v2_score = finite(candidate.get("v2_score"), finite(v31.get("v2_score")))

    if (
        v2_state in {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}
        or early.get("ready")
    ):
        confirmed = v2_state == "CONFIRMED_ACCELERATION"
        out.append({
            "path": "V2_REAL",
            "stage": "V2_CONFIRMED" if confirmed else "V2_BUILDING",
            "loss_family": None if confirmed else "PRE_CONFIRMATION",
            "credible": True,
            "entry_hypothesis": confirmed,
            "v2_state": v2_state,
            "v2_confirmed": confirmed,
            "execution_ready": False,
            "selectable": False,
            "selection_checked": False,
            "blocking_reason": None if confirmed else "WAITING_V2_CONFIRMATION",
            "selection_reason": None,
            "execution_reason": None,
            "economic_score": None,
            "v3_opportunity_score": finite(candidate.get("opportunity_score")),
            "v2_score": v2_score,
            "early_quant_score": finite(early.get("score_0_10")),
            "early_quant_evidence_count": int(early.get("evidence_count") or 0),
            "entry_path": "V2_REAL",
            "decision_id": None,
            "plan_id": None,
            "plan_available_ts": None,
            "plan_available_at_utc": None,
            "execution_entry_eur": None,
            "stop_eur": None,
            "tp1_eur": None,
            "tp2_eur": None,
            "stake_eur": None,
            "stop_distance_pct": None,
            "net_rr_tp1": None,
            "spread_pct": None,
            "depth_slippage_pct": None,
            "execution_available": False,
        })

    raw_execution = v31.get("raw_execution")
    if not isinstance(raw_execution, dict):
        raw_execution = candidate.get("execution")
    raw_hypothesis = bool(candidate.get("entry_hypothesis"))
    raw_credible = bool(candidate.get("credible_opportunity") or raw_hypothesis)
    if raw_credible or isinstance(raw_execution, dict):
        raw = _classify_execution_path(
            path="RAW",
            hypothesis=raw_hypothesis,
            credible=raw_credible,
            execution=raw_execution,
            v31=v31,
        )
        raw["early_quant_score"] = finite(early.get("score_0_10"))
        raw["early_quant_evidence_count"] = int(early.get("evidence_count") or 0)
        out.append(raw)

    thesis_execution = v31.get("thesis_execution")
    if not isinstance(thesis_execution, dict):
        thesis_execution = candidate.get("thesis_execution")
    thesis_hypothesis = bool(
        candidate.get("thesis_reentry_hypothesis")
        or v31.get("thesis_reentry_hypothesis")
    )
    thesis_credible = bool(thesis_hypothesis or isinstance(thesis_execution, dict))
    if thesis_credible:
        thesis = _classify_execution_path(
            path="THESIS_REENTRY",
            hypothesis=thesis_hypothesis,
            credible=thesis_credible,
            execution=thesis_execution,
            v31=v31,
        )
        thesis["early_quant_score"] = finite(early.get("score_0_10"))
        thesis["early_quant_evidence_count"] = int(early.get("evidence_count") or 0)
        out.append(thesis)

    if candidate.get("near_miss_opportunity"):
        ex = execution_snapshot("NEAR_MISS_DIAGNOSTIC", near_miss_execution)
        ready = bool(ex["execution_ready"])
        out.append({
            "path": "NEAR_MISS_DIAGNOSTIC",
            "stage": (
                "NEAR_MISS_DIAGNOSTIC_READY"
                if ready
                else "NEAR_MISS_DIAGNOSTIC_WAITING"
            ),
            "loss_family": "DIAGNOSTIC_ONLY",
            "credible": True,
            "entry_hypothesis": False,
            "v2_state": v2_state,
            "v2_confirmed": False,
            "selectable": False,
            "selection_checked": False,
            "blocking_reason": None if ready else (ex["execution_reason"] or "DIAGNOSTIC_NOT_CHECKED"),
            "selection_reason": None,
            "economic_score": None,
            "v3_opportunity_score": finite(candidate.get("opportunity_score")),
            "v2_score": v2_score,
            "early_quant_score": finite(early.get("score_0_10")),
            "early_quant_evidence_count": int(early.get("evidence_count") or 0),
            "entry_path": "NEAR_MISS_DIAGNOSTIC",
            "decision_id": None,
            **ex,
        })

    return out


def should_track(
    candidate: dict[str, Any],
    v31: dict[str, Any] | None = None,
    *,
    near_miss_execution: dict[str, Any] | None = None,
) -> bool:
    return bool(
        classify_path_snapshots(
            candidate,
            v31,
            near_miss_execution=near_miss_execution,
        )
    )


def _record_first(
    state: dict[str, Any],
    key: str,
    active: bool,
    now: float,
    stage_price: float | None,
) -> None:
    if not active or state.get(f"first_{key}_ts") is not None:
        return
    state[f"first_{key}_ts"] = now
    state[f"first_{key}_price_eur"] = finite(stage_price)


def advance_funnel_memory(
    prior: dict[str, Any] | None,
    *,
    snapshot: dict[str, Any],
    now: float,
    price_eur: float | None,
) -> tuple[dict[str, Any], bool]:
    """Advance one path-specific fixed-horizon episode."""
    state = dict(prior or {})
    price = finite(price_eur)
    if not state:
        state = {
            "opened_ts": now,
            "horizon_end_ts": now + FIXED_HORIZON_SECONDS,
            "origin_price_eur": price,
            "origin_stage": snapshot.get("stage"),
            "origin_reason": snapshot.get("blocking_reason"),
            "path": snapshot.get("path"),
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
    state["age_seconds"] = max(0.0, now - float(state.get("opened_ts") or now))
    state["age_hours"] = state["age_seconds"] / 3600.0

    scan_stage_price = price
    plan_stage_price = finite(snapshot.get("execution_entry_eur"), price)
    _record_first(state, "credible", bool(snapshot.get("credible")), now, scan_stage_price)
    _record_first(state, "entry_hypothesis", bool(snapshot.get("entry_hypothesis")), now, scan_stage_price)
    _record_first(state, "confirmed", bool(snapshot.get("v2_confirmed")), now, scan_stage_price)
    _record_first(state, "execution_ready", bool(snapshot.get("execution_ready")), now, plan_stage_price)
    _record_first(state, "selectable", bool(snapshot.get("selectable")), now, plan_stage_price)

    if snapshot.get("execution_ready") and state.get("first_execution_plan_id") is None:
        state["first_execution_plan_id"] = snapshot.get("plan_id")
        state["first_execution_plan_available_ts"] = snapshot.get("plan_available_ts")
        state["first_execution_entry_eur"] = finite(snapshot.get("execution_entry_eur"))
        state["first_execution_stop_eur"] = finite(snapshot.get("stop_eur"))
        state["first_execution_tp1_eur"] = finite(snapshot.get("tp1_eur"))

    if snapshot.get("selectable") and state.get("first_selectable_plan_id") is None:
        state["first_selectable_plan_id"] = snapshot.get("plan_id")
        state["first_selectable_entry_eur"] = finite(snapshot.get("execution_entry_eur"))
        state["first_selectable_stop_eur"] = finite(snapshot.get("stop_eur"))
        state["first_selectable_decision_id"] = snapshot.get("decision_id")

    for key in ("credible", "entry_hypothesis", "confirmed", "execution_ready", "selectable"):
        stage_price = finite(state.get(f"first_{key}_price_eur"))
        state[f"movement_consumed_to_{key}_pct"] = pct_change(origin, stage_price)

    signature = "|".join([
        str(snapshot.get("stage") or ""),
        str(snapshot.get("blocking_reason") or ""),
        str(snapshot.get("plan_id") or ""),
        str(snapshot.get("decision_id") or ""),
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
            "path": snapshot.get("path"),
            "plan_id": snapshot.get("plan_id"),
            "execution_entry_eur": snapshot.get("execution_entry_eur"),
            "decision_id": snapshot.get("decision_id"),
        })
        state["reason_history"] = hist[-80:]
        state["last_signature"] = signature

    state["current_stage"] = snapshot.get("stage")
    state["current_loss_family"] = snapshot.get("loss_family")
    state["current_blocking_reason"] = snapshot.get("blocking_reason")
    state["current_economic_score"] = snapshot.get("economic_score")
    state["current_v3_opportunity_score"] = snapshot.get("v3_opportunity_score")
    state["current_v2_score"] = snapshot.get("v2_score")
    state["current_entry_path"] = snapshot.get("entry_path")
    state["current_plan_id"] = snapshot.get("plan_id")
    state["current_execution_entry_eur"] = finite(snapshot.get("execution_entry_eur"))
    return state, changed


def observe_price_only(
    prior: dict[str, Any],
    *,
    now: float,
    price_eur: float | None,
) -> dict[str, Any]:
    """Continue the outcome trajectory after the signal disappears."""
    state = dict(prior)
    price = finite(price_eur)
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
    state["age_seconds"] = max(0.0, now - float(state.get("opened_ts") or now))
    state["age_hours"] = state["age_seconds"] / 3600.0
    return state


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
