"""Independent acceleration detection and 24-72h candidate memory.

These diagnostics never mutate frozen V4 scores. Confirmed acceleration can be
considered by the separate production gate, which still requires data quality,
liquidity and a fresh final execution validation before an email is sent.
"""
from __future__ import annotations

from typing import Any

from research.common import finite, utc


MEMORY_FULL_SECONDS = 24 * 3600
MEMORY_MAX_SECONDS = 72 * 3600
ACCELERATION_WATCH_MIN = 4.75
ACCELERATION_CONFIRMED_MIN = 6.50
BASELINE_SIGNAL_STATES = {"WATCH", "ENTRY_WINDOW", "BUY_READY", "REENTRY_READY"}
ACCELERATION_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}


def _n(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return default
    return result


def _cap(value: float) -> float:
    return max(0.0, min(10.0, value))


def acceleration_signal(obs: dict[str, Any]) -> dict[str, Any]:
    """Detect short-term acceleration independently from V4 scoring.

    The detector uses only closed 5m/15m diagnostics already collected for the
    full EUR universe. Detection alone is never enough to send an email; a
    separate production gate and fresh execution validation remain mandatory.
    """
    f5 = (obs.get("features") or {}).get("5m") or {}
    f15 = (obs.get("features") or {}).get("15m") or {}
    # Capability-specific quality: book/enrichment failures can block an
    # executable entry without invalidating closed-candle acceleration data.
    # Conversely, invalid 5m/15m candles always fail this detector closed.
    if not f5.get("valid") or not f15.get("valid"):
        reasons = list(f5.get("reasons") or []) + list(f15.get("reasons") or [])
        return {
            "state": "DATA_UNAVAILABLE",
            "score": None,
            "detected": False,
            "components": {},
            "reasons": sorted(set(reasons)) or [
                "INVALID_5M_ACCELERATION_INPUT" if not f5.get("valid") else "INVALID_15M_ACCELERATION_INPUT"
            ],
            "buyability": "NOT_ASSESSED",
            "alert_eligible": False,
            "affects_baseline": False,
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
        "confirmation_15m": _cap((_n(f15.get("return_1bar_pct")) + _n(f15.get("return_4bar_pct")) / 2.0) * 2.0),
    }
    score = round(
        0.30 * components["momentum_5m"]
        + 0.25 * components["momentum_acceleration_5m"]
        + 0.20 * components["volume_expansion"]
        + 0.15 * components["breakout_pressure"]
        + 0.10 * components["confirmation_15m"],
        3,
    )
    evidence_count = sum(
        (
            components["momentum_5m"] >= 4.0,
            components["momentum_acceleration_5m"] >= 4.0,
            components["volume_expansion"] >= 4.0,
            components["breakout_pressure"] >= 4.0,
            components["confirmation_15m"] >= 3.0,
        )
    )
    if score >= ACCELERATION_CONFIRMED_MIN and evidence_count >= 3:
        state = "CONFIRMED_ACCELERATION"
    elif score >= ACCELERATION_WATCH_MIN and evidence_count >= 2:
        state = "BUILDING_ACCELERATION"
    else:
        state = "NO_ACCELERATION"

    change24 = _n(obs.get("change_24h_pct"))
    chase = _n((obs.get("chase_risk") or {}).get("score"))
    too_late = obs.get("category") == "TOO LATE" or change24 >= 20.0 or chase >= 8.0
    if state == "NO_ACCELERATION":
        buyability = "NOT_APPLICABLE"
    elif too_late:
        buyability = "DETECTED_BUT_TOO_LATE"
    else:
        buyability = "REQUIRES_FINAL_EXECUTION_VALIDATION"
    return {
        "state": state,
        "score": score,
        "detected": state in ACCELERATION_STATES,
        "components": components,
        "evidence_count": evidence_count,
        "buyability": buyability,
        "alert_eligible": False,
        "affects_baseline": False,
    }


def current_candidates(decisions: list[dict[str, Any]], observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Combine V4, decision-layer and acceleration evidence without conflation."""
    by_market = {row.get("market"): row for row in decisions}
    result = []
    for obs in observations:
        market = obs.get("market")
        decision = by_market.get(market) or {}
        baseline = obs.get("baseline") or {}
        acceleration = obs.get("acceleration") or {}
        sources = []
        if baseline.get("action_status") in BASELINE_SIGNAL_STATES:
            sources.append("V4")
        if decision.get("bucket"):
            sources.append("DECISION_LAYER")
        if acceleration.get("state") in ACCELERATION_STATES:
            sources.append("ACCELERATION")
        if not sources:
            continue
        score = max(_n(decision.get("rank_score")), _n(acceleration.get("score")))
        too_late = obs.get("category") == "TOO LATE" or acceleration.get("buyability") == "DETECTED_BUT_TOO_LATE"
        plan = obs.get("trade_plan") or {}
        buyable = bool(
            obs.get("decision") == "ACHÈTE"
            and baseline.get("buy_ready")
            and (obs.get("data_quality") or {}).get("ok")
            and plan.get("valid")
            and not too_late
        )
        result.append({
            "market": market,
            "price_eur": obs.get("price_eur"),
            "signal_score": round(score, 4),
            "sources": sources,
            "decision_bucket": decision.get("bucket"),
            "decision_action": decision.get("action"),
            "acceleration_state": acceleration.get("state"),
            "acceleration_score": acceleration.get("score"),
            "buyable_now": buyable,
            "buyability": "BUYABLE_NOW" if buyable else "DETECTED_BUT_TOO_LATE" if too_late else "WATCH_ONLY",
            "alert_eligible": buyable,
        })
    return result


def _decay(age_seconds: float) -> float:
    if age_seconds <= MEMORY_FULL_SECONDS:
        return 1.0
    if age_seconds >= MEMORY_MAX_SECONDS:
        return 0.0
    return (MEMORY_MAX_SECONDS - age_seconds) / (MEMORY_MAX_SECONDS - MEMORY_FULL_SECONDS)


def update_candidate_memory(previous: dict[str, Any], current: list[dict[str, Any]], now: float) -> dict[str, Any]:
    """Keep last-seen candidates for 72h, with decay beginning after 24h."""
    old = {row["market"]: row for row in previous.get("candidates", []) if row.get("market")}
    active = {row["market"]: row for row in current if row.get("market")}
    candidates = []
    for market in sorted(set(old) | set(active)):
        prior = old.get(market) or {}
        fresh = active.get(market)
        if fresh:
            period = int(now // 900)
            prior_period = prior.get("last_signal_period_15m")
            hits = int(prior.get("distinct_signal_periods", 0)) + int(prior_period != period)
            raw_score = _n(fresh.get("signal_score"))
            row = {
                **prior,
                **fresh,
                "first_seen_ts": prior.get("first_seen_ts", now),
                "first_seen_at_utc": prior.get("first_seen_at_utc", utc(now)),
                "last_seen_ts": now,
                "last_seen_at_utc": utc(now),
                "last_signal_period_15m": period,
                "distinct_signal_periods": hits,
                "all_sources": sorted(set(prior.get("all_sources", [])) | set(fresh.get("sources", []))),
                "max_signal_score": max(_n(prior.get("max_signal_score")), raw_score),
                "memory_score": round(raw_score, 4),
                "decay_factor": 1.0,
                "age_since_last_signal_hours": 0.0,
                "memory_state": "ACTIVE_NOW",
                "expires_at_utc": utc(now + MEMORY_MAX_SECONDS),
            }
        else:
            age = max(0.0, now - _n(prior.get("last_seen_ts"), now))
            factor = _decay(age)
            if factor <= 0:
                continue
            row = {
                **prior,
                "sources": [],
                "buyable_now": False,
                "buyability": "MEMORY_ONLY",
                "alert_eligible": False,
                "memory_score": round(_n(prior.get("signal_score")) * factor, 4),
                "decay_factor": round(factor, 4),
                "age_since_last_signal_hours": round(age / 3600, 3),
                "memory_state": "MEMORY_24H" if age <= MEMORY_FULL_SECONDS else "MEMORY_DECAY_24_72H",
                "expires_at_utc": utc(_n(prior.get("last_seen_ts")) + MEMORY_MAX_SECONDS),
            }
        candidates.append(row)
    candidates.sort(key=lambda row: (bool(row.get("buyable_now")), _n(row.get("memory_score"))), reverse=True)
    return {
        "schema_version": 1,
        "policy": "CANDIDATE_MEMORY_24_72H_SHADOW",
        "generated_at_utc": utc(now),
        "retention": {
            "full_score_hours": 24,
            "maximum_hours": 72,
            "decay": "LINEAR_FROM_24H_TO_ZERO_AT_72H",
        },
        "alert_policy": "MEMORY_AND_ACCELERATION_NEVER_TRIGGER_EMAIL_WITHOUT_CURRENT_BUY_ELIGIBILITY",
        "candidates": candidates,
    }
