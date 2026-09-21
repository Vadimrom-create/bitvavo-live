"""Pure Solaire acceleration detector over full-universe closed candles.

This module has no dependency on V3/V4, Decision Layer, chase heuristics,
portfolio state, Oracle/Railway or alert transport.
"""
from __future__ import annotations

from typing import Any

ACCELERATION_WATCH_MIN = 4.75
ACCELERATION_CONFIRMED_MIN = 6.50
ACCELERATION_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}


def _n(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _cap(value: float) -> float:
    return max(0.0, min(10.0, value))


def acceleration_signal(obs: dict[str, Any]) -> dict[str, Any]:
    f5 = (obs.get("features") or {}).get("5m") or {}
    f15 = (obs.get("features") or {}).get("15m") or {}
    if not f5.get("valid") or not f15.get("valid"):
        reasons = list(f5.get("reasons") or []) + list(f15.get("reasons") or [])
        return {
            "state": "DATA_UNAVAILABLE",
            "score": None,
            "detected": False,
            "components": {},
            "evidence_flags": {},
            "evidence_count": 0,
            "timeframe_confirmation_15m": False,
            "confirmation_scope": "NOT_AVAILABLE",
            "reasons": sorted(set(reasons)) or ["INVALID_ACCELERATION_INPUT"],
            "buyability": "NOT_ASSESSED",
            "alert_eligible": False,
        }

    volume_ratio = max(
        _n(f5.get("relative_volume")),
        _n(f5.get("volume_4_vs_prev4")),
        _n(f15.get("relative_volume")),
    )
    components = {
        "momentum_5m": _cap((_n(f5.get("return_4bar_pct")) - 0.25) * 2.5),
        "momentum_acceleration_5m": _cap((_n(f5.get("momentum_acceleration_pp")) - 0.10) * 3.0),
        "volume_expansion": _cap((volume_ratio - 1.0) * 4.0),
        "breakout_pressure": _cap((_n(f5.get("distance_to_breakout_pct")) + 1.25) * 3.0),
        "confirmation_15m": _cap(
            (_n(f15.get("return_1bar_pct")) + _n(f15.get("return_4bar_pct")) / 2.0) * 2.0
        ),
    }
    score = round(
        0.30 * components["momentum_5m"]
        + 0.25 * components["momentum_acceleration_5m"]
        + 0.20 * components["volume_expansion"]
        + 0.15 * components["breakout_pressure"]
        + 0.10 * components["confirmation_15m"],
        3,
    )
    evidence_flags = {
        "momentum_5m": components["momentum_5m"] >= 4.0,
        "momentum_acceleration_5m": components["momentum_acceleration_5m"] >= 4.0,
        "volume_expansion": components["volume_expansion"] >= 4.0,
        "breakout_pressure": components["breakout_pressure"] >= 4.0,
        "confirmation_15m": components["confirmation_15m"] >= 3.0,
    }
    evidence_count = sum(evidence_flags.values())
    timeframe_confirmation_15m = evidence_flags["confirmation_15m"]
    confirmation_scope = (
        "MULTI_TIMEFRAME"
        if timeframe_confirmation_15m
        else "FAST_COMPOSITE_ONLY"
    )
    if score >= ACCELERATION_CONFIRMED_MIN and evidence_count >= 3:
        state = "CONFIRMED_ACCELERATION"
    elif score >= ACCELERATION_WATCH_MIN and evidence_count >= 2:
        state = "BUILDING_ACCELERATION"
    else:
        state = "NO_ACCELERATION"

    return {
        "state": state,
        "score": score,
        "detected": state in ACCELERATION_STATES,
        "components": components,
        "evidence_flags": evidence_flags,
        "evidence_count": evidence_count,
        "timeframe_confirmation_15m": timeframe_confirmation_15m,
        "confirmation_scope": confirmation_scope,
        "buyability": (
            "REQUIRES_FINAL_EXECUTION_VALIDATION"
            if state in ACCELERATION_STATES
            else "NOT_APPLICABLE"
        ),
        "alert_eligible": False,
    }
