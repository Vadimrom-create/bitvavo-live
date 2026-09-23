"""Solaire V3.1 economic-ranking shadow.

This module is intentionally a pure challenger layer on top of the frozen
Solaire V3 detector. It does not discover markets, send mail or submit orders.

The design is pre-registered prospectively:
- V2/V3 legacy signal scores are diagnostic only and never enter the V3.1 score;
- persistence and relative strength receive more weight than headlines/narratives;
- contradictory multi-horizon evidence is explicitly penalised;
- execution quality is part of economic ranking, not merely a pass/fail gate;
- sizing is risk-based and score-aware, with hard notional caps.
"""
from __future__ import annotations

import math
from typing import Any

from research.common import finite

FROZEN_V3_COMMIT = "2b0a5b25173e8ac5dd67625f80755f26acbedabf"
V3_TIMING_LAB_COMMIT = "0c05e0fbf55b0ff99dae3f10bcfc3411bbee0cc6"
REFERENCE_CAPITAL_EUR = 2400.0
MAX_SHADOW_POSITIONS = 3
MIN_SELECTED_SCORE = 6.0
MIN_STAKE_EUR = 50.0
MAX_STAKE_EUR = 250.0
BASE_RISK_EUR = 8.0
MAX_RISK_EUR = 12.0
ROUND_TRIP_COST_PCT = 0.70


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def _clip(value: float, low: float = 0.0, high: float = 10.0) -> float:
    return min(high, max(low, value))


def _linear(value: float, low: float, high: float) -> float:
    if high <= low:
        return 0.0
    return _clip((value - low) / (high - low) * 10.0)


def _peak(value: float, ideal: float, width: float) -> float:
    if width <= 0:
        return 0.0
    return _clip(10.0 - abs(value - ideal) / width * 10.0)


def preliminary_economic_score(candidate: dict[str, Any], universe_row: dict[str, Any]) -> dict[str, Any]:
    """Rank forward economic quality before execution diagnostics.

    No legacy V2/V3 score is used in the arithmetic. Those fields can still be
    logged for later calibration.
    """
    features = universe_row.get("features") or {}
    f5 = features.get("5m") or {}
    f15 = features.get("15m") or {}
    context = universe_row.get("context") or {}
    early = candidate.get("early_quant") or {}
    external = candidate.get("external") or {}

    early_score = _n(early.get("score_0_10"))
    r20 = _n(f5.get("return_4bar_pct"))
    r1h = _n(f15.get("return_4bar_pct"))
    r4h = _n(f15.get("return_16bar_pct"))
    rs1 = _n(context.get("relative_strength_1h_pp"))
    rs4 = _n(context.get("relative_strength_4h_pp"))
    vol = max(_n(f5.get("relative_volume")), _n(f5.get("volume_4_vs_prev4")))
    accel = _n(f5.get("momentum_acceleration_pp"))
    change24 = _n(universe_row.get("change_24h_pct"))
    extension = _n(f15.get("extension_ma20_pct"))
    breakout = _n(f15.get("distance_to_breakout_pct"))
    upper_wick = _n(f15.get("upper_wick_max"))
    ext20 = _n(external.get("median_return_20m_pct"))
    ext60 = _n(external.get("median_return_60m_pct"))
    ext_breadth = _n(external.get("breadth_positive_20m_pct"), 50.0)

    persistence = (
        0.24 * early_score
        + 0.18 * _linear(r20, 0.0, 2.5)
        + 0.24 * _linear(r1h, 0.0, 5.0)
        + 0.24 * _linear(r4h, 0.0, 10.0)
        + 0.10 * _linear(accel, 0.0, 1.5)
    )

    relative_strength = (
        0.45 * _linear(rs1, -0.5, 5.0)
        + 0.55 * _linear(rs4, -1.0, 10.0)
    )

    participation = (
        0.45 * _linear(vol, 1.0, 4.0)
        + 0.30 * _linear(ext20, -0.2, 3.0)
        + 0.15 * _linear(ext60, -0.5, 6.0)
        + 0.10 * _linear(ext_breadth, 45.0, 100.0)
    )

    # Prefer entries close to an emerging breakout, but penalise vertical/chased
    # geometry. High 24h return is not bad by itself; it becomes expensive when
    # accompanied by large local extension.
    breakout_quality = _peak(breakout, 0.5, 4.0)
    extension_quality = _peak(extension, 2.0, 8.0)
    change24_quality = _peak(change24, 8.0, 22.0)
    wick_quality = _clip(10.0 - upper_wick * 8.0)
    entry_geometry = (
        0.35 * breakout_quality
        + 0.30 * extension_quality
        + 0.20 * change24_quality
        + 0.15 * wick_quality
    )

    context_score = (
        0.50 * _n(candidate.get("external_score"))
        + 0.30 * _n(candidate.get("narrative_score"))
        + 0.20 * _n(candidate.get("news_score"))
    )

    penalties: dict[str, float] = {}
    if r4h < 0:
        penalties["negative_4h_trend"] = min(1.8, abs(r4h) / 3.0)
    if rs4 < -1.0:
        penalties["negative_4h_relative_strength"] = min(1.5, abs(rs4 + 1.0) / 3.0 + 0.4)
    if r20 < -0.5:
        penalties["short_term_reversal"] = min(1.2, abs(r20 + 0.5) / 2.0 + 0.3)
    if change24 > 20.0 and extension > 6.0:
        penalties["late_extension"] = min(1.4, (change24 - 20.0) / 20.0 + (extension - 6.0) / 10.0)
    if early_score >= 5.0 and r4h <= -2.0:
        penalties["horizon_disagreement"] = 0.8

    contradiction_penalty = sum(penalties.values())
    raw = (
        0.34 * persistence
        + 0.27 * relative_strength
        + 0.17 * participation
        + 0.14 * entry_geometry
        + 0.08 * context_score
        - contradiction_penalty
    )
    score = _clip(raw)

    return {
        "preliminary_score": round(score, 3),
        "components": {
            "persistence": round(persistence, 3),
            "relative_strength": round(relative_strength, 3),
            "participation": round(participation, 3),
            "entry_geometry": round(entry_geometry, 3),
            "context": round(context_score, 3),
        },
        "contradiction_penalty": round(contradiction_penalty, 3),
        "penalties": {k: round(v, 3) for k, v in penalties.items()},
        "diagnostics": {
            "return_20m_pct": round(r20, 4),
            "return_1h_pct": round(r1h, 4),
            "return_4h_pct": round(r4h, 4),
            "relative_strength_1h_pp": round(rs1, 4),
            "relative_strength_4h_pp": round(rs4, 4),
            "change_24h_pct": round(change24, 4),
            "extension_ma20_pct": round(extension, 4),
            "legacy_v2_score_unused": finite(candidate.get("v2_score")),
            "legacy_v3_opportunity_score_unused": finite(candidate.get("opportunity_score")),
        },
    }


def execution_quality_score(execution: dict[str, Any] | None) -> dict[str, Any]:
    if not execution:
        return {"available": False, "ready": False, "score": None, "reason": "NOT_CHECKED"}
    if not execution.get("ready"):
        return {
            "available": True,
            "ready": False,
            "score": 0.0,
            "reason": execution.get("reason") or "NOT_READY",
        }

    spread = _n(execution.get("spread_pct"), 99.0)
    depth = execution.get("depth") or {}
    slippage = _n(depth.get("depth_slippage_pct"), 99.0)
    plan = execution.get("plan") or {}
    stop_distance = _n(plan.get("stop_distance_pct"), 99.0)
    rr = _n(plan.get("net_rr_tp1"), 0.0)

    spread_score = _clip(10.0 - max(0.0, spread - 0.08) / 0.42 * 10.0)
    slippage_score = _clip(10.0 - max(0.0, slippage - 0.05) / 0.45 * 10.0)
    stop_score = _peak(stop_distance, 6.0, 5.0)
    rr_score = _linear(rr, 1.5, 3.0)
    score = 0.30 * spread_score + 0.20 * slippage_score + 0.30 * stop_score + 0.20 * rr_score

    return {
        "available": True,
        "ready": True,
        "score": round(_clip(score), 3),
        "reason": "EXECUTION_READY",
        "components": {
            "spread": round(spread_score, 3),
            "depth_slippage": round(slippage_score, 3),
            "stop_geometry": round(stop_score, 3),
            "net_rr": round(rr_score, 3),
        },
    }


def final_economic_score(preliminary: dict[str, Any], execution: dict[str, Any] | None) -> dict[str, Any]:
    eq = execution_quality_score(execution)
    pre = _n(preliminary.get("preliminary_score"))
    if not eq.get("ready"):
        return {
            "score": round(pre, 3),
            "selectable": False,
            "reason": eq.get("reason"),
            "execution_quality": eq,
        }

    final = 0.72 * pre + 0.28 * _n(eq.get("score"))
    persistence = _n((preliminary.get("components") or {}).get("persistence"))
    relative_strength = _n((preliminary.get("components") or {}).get("relative_strength"))
    selectable = (
        final >= MIN_SELECTED_SCORE
        and persistence >= 4.5
        and relative_strength >= 4.0
    )
    if selectable:
        reason = "SELECTABLE"
    elif final < MIN_SELECTED_SCORE:
        reason = "ECONOMIC_SCORE_BELOW_THRESHOLD"
    elif persistence < 4.5:
        reason = "INSUFFICIENT_PERSISTENCE"
    else:
        reason = "INSUFFICIENT_RELATIVE_STRENGTH"

    return {
        "score": round(_clip(final), 3),
        "selectable": selectable,
        "reason": reason,
        "execution_quality": eq,
    }



def timing_variants(candidate: dict[str, Any]) -> dict[str, bool]:
    """Read V3's timing-lab decisions without reimplementing its thresholds.

    V3 remains the authority for whether PERSIST_30M or PULLBACK_RECLAIM fired.
    V3.1 only applies its unchanged economic score/gate to those same timed
    opportunities. This preserves a clean factorial comparison.
    """
    timing = candidate.get("timing_state") or {}
    episode = timing.get("episode")
    if episode is None:
        return {"PERSIST_30M": False, "PULLBACK_RECLAIM": False}
    return {
        "PERSIST_30M": timing.get("persist30_recorded_episode") == episode,
        "PULLBACK_RECLAIM": timing.get("reclaim_recorded_episode") == episode,
    }



def shadow_sizing(score: float, execution: dict[str, Any], quote_volume_24h_eur: float | None) -> dict[str, Any]:
    """Risk-aware theoretical notional for comparison only."""
    plan = execution.get("plan") or {}
    entry = finite(plan.get("entry_eur"))
    stop = finite(plan.get("stop_eur"))
    if not execution.get("ready") or entry is None or stop is None or not 0 < stop < entry:
        return {"valid": False, "reason": "INVALID_EXECUTION_PLAN"}

    stop_pct = (entry / stop - 1.0) * 100.0
    # The stop-loss loss fraction is based on entry-to-stop distance plus the
    # same 0.70% round-trip cost convention used by the evaluator.
    effective_risk_pct = (entry - stop) / entry * 100.0 + ROUND_TRIP_COST_PCT
    score_fraction = _clip((score - MIN_SELECTED_SCORE) / (10.0 - MIN_SELECTED_SCORE), 0.0, 1.0)
    target_risk = BASE_RISK_EUR + (MAX_RISK_EUR - BASE_RISK_EUR) * score_fraction
    stake = target_risk / (effective_risk_pct / 100.0)

    volume = _n(quote_volume_24h_eur)
    liquidity_cap = MAX_STAKE_EUR
    if volume < 150_000:
        liquidity_cap = 100.0
    elif volume < 400_000:
        liquidity_cap = 160.0

    stake = min(MAX_STAKE_EUR, liquidity_cap, stake)
    if stake < MIN_STAKE_EUR:
        return {
            "valid": False,
            "reason": "STAKE_BELOW_MINIMUM",
            "target_risk_eur": round(target_risk, 2),
            "effective_risk_pct": round(effective_risk_pct, 4),
        }

    theoretical_risk = stake * effective_risk_pct / 100.0
    return {
        "valid": True,
        "stake_eur": round(stake, 2),
        "target_risk_eur": round(target_risk, 2),
        "theoretical_risk_eur": round(theoretical_risk, 2),
        "effective_risk_pct": round(effective_risk_pct, 4),
        "raw_stop_distance_pct": round((entry - stop) / entry * 100.0, 4),
        "liquidity_cap_eur": liquidity_cap,
        "method": "score_aware_risk_budget_with_notional_and_liquidity_caps",
    }
