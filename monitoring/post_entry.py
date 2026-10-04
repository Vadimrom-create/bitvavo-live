"""Post-entry position assessment, separate from BUY detection.

This module evaluates whether an already-open position thesis remains healthy.
It deliberately does not reuse the direct-acceleration BUY score as an exit
signal. Horizon scores are deterministic management outlooks, not return
forecasts and not calibrated probabilities.
"""
from __future__ import annotations

from typing import Any

from research.common import finite

METHOD = "HEURISTIC_POSITION_MANAGEMENT_NOT_RETURN_FORECAST_V1"


def _clamp(value: float, low: float = 0.0, high: float = 10.0) -> float:
    return max(low, min(high, value))


def _tf_health(features: dict[str, Any] | None) -> float | None:
    """Return a compact -1..+1 health signal from one closed-candle timeframe."""
    if not isinstance(features, dict) or not features.get("valid"):
        return None
    ret = finite(features.get("return_4bar_pct"))
    accel = finite(features.get("momentum_acceleration_pp"))
    extension = finite(features.get("extension_ma20_pct"))
    if ret is None or accel is None or extension is None:
        return None

    score = 0.0
    score += 1.0 if ret > 0 else (-1.0 if ret < 0 else 0.0)
    score += 0.5 if accel > 0 else (-0.5 if accel < 0 else 0.0)
    score += 0.5 if extension > 0 else (-0.5 if extension < 0 else 0.0)
    return max(-1.0, min(1.0, score / 2.0))


def _label(score: float | None) -> str:
    if score is None:
        return "UNAVAILABLE"
    if score >= 7.0:
        return "FAVORABLE"
    if score >= 5.25:
        return "NEUTRAL_POSITIVE"
    if score >= 4.0:
        return "FRAGILE"
    return "UNFAVORABLE"


def assess_post_entry(
    *,
    market: str,
    bid: float | None,
    cost_basis_eur: float | None,
    stop_eur: float | None,
    timeframes: dict[str, dict[str, Any]] | None,
    source_alert: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assess an existing position independently from fresh-entry eligibility."""
    bid = finite(bid)
    cost = finite(cost_basis_eur)
    stop = finite(stop_eur)
    source_alert = source_alert or {}
    timeframes = timeframes or {}

    result: dict[str, Any] = {
        "schema": "solaire_post_entry_assessment_v1",
        "market": market,
        "method": METHOD,
        "is_return_forecast": False,
        "is_entry_signal": False,
        "acceleration_decay_is_invalidation": False,
        "source_entry_signal": {
            "signal_score": finite(source_alert.get("signal_score")),
            "entry_eur": finite(source_alert.get("last_sent_entry_eur")),
            "stop_eur": finite(source_alert.get("last_sent_stop_eur")),
            "lifecycle_state": source_alert.get("alert_lifecycle_state"),
            "lifecycle_reason": source_alert.get("alert_lifecycle_reason"),
        },
    }

    if bid is None or bid <= 0 or stop is None or stop <= 0:
        result.update(
            thesis_status="DATA_INCOMPLETE",
            management_outlook_24h=None,
            management_outlook_48h=None,
            management_outlook_72h=None,
            outlook_labels={"24h": "UNAVAILABLE", "48h": "UNAVAILABLE", "72h": "UNAVAILABLE"},
        )
        return result

    pnl_pct = ((bid / cost) - 1.0) * 100.0 if cost not in (None, 0) else None
    stop_cushion_pct = ((bid / stop) - 1.0) * 100.0

    result["pnl_pct"] = round(pnl_pct, 3) if pnl_pct is not None else None
    result["stop_cushion_pct"] = round(stop_cushion_pct, 3)

    if bid <= stop:
        result.update(
            thesis_status="INVALIDATED_STOP_BREACH",
            management_outlook_24h=0.0,
            management_outlook_48h=0.0,
            management_outlook_72h=0.0,
            outlook_labels={"24h": "UNFAVORABLE", "48h": "UNFAVORABLE", "72h": "UNFAVORABLE"},
        )
        return result

    tf = {name: _tf_health(timeframes.get(name)) for name in ("15m", "1h", "4h")}
    result["timeframe_health"] = tf

    # Structural base: a live thesis starts neutral-positive while its verified
    # invalidation level remains intact. PnL only nudges the score; it never
    # overrides a broken stop or dominates the trend evidence.
    base = 5.4
    base += min(0.6, max(0.0, stop_cushion_pct) / 10.0)
    if pnl_pct is not None:
        base += max(-0.4, min(0.4, pnl_pct / 20.0))

    def horizon(weights: dict[str, float]) -> float | None:
        available = [(tf[name], weight) for name, weight in weights.items() if tf[name] is not None]
        if not available:
            return None
        adjustment = sum(value * weight for value, weight in available)
        # Normalize when one timeframe is unavailable so missing data does not
        # mechanically depress the score.
        total_weight = sum(abs(weight) for _, weight in available)
        target_weight = sum(abs(weight) for weight in weights.values())
        if total_weight > 0:
            adjustment *= target_weight / total_weight
        return round(_clamp(base + adjustment), 3)

    score24 = horizon({"15m": 1.30, "1h": 1.20, "4h": 0.50})
    score48 = horizon({"15m": 0.50, "1h": 1.20, "4h": 1.30})
    score72 = horizon({"15m": 0.20, "1h": 0.90, "4h": 1.60})
    scores = [s for s in (score24, score48, score72) if s is not None]

    if not scores:
        status = "VALID_DATA_INCOMPLETE"
    else:
        avg = sum(scores) / len(scores)
        if avg >= 7.0:
            status = "VALID_STRONG"
        elif avg >= 5.25:
            status = "VALID"
        else:
            status = "VALID_WEAKENING"

    result.update(
        thesis_status=status,
        management_outlook_24h=score24,
        management_outlook_48h=score48,
        management_outlook_72h=score72,
        outlook_labels={"24h": _label(score24), "48h": _label(score48), "72h": _label(score72)},
    )
    return result
