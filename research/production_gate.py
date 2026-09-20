"""Production candidate gate over the complete Bitvavo EUR scan.

The gate is deliberately independent from Oracle/hosted probe availability.
Frozen V4 remains a benchmark/source of evidence, but a market can become
alert-eligible from confirmed full-universe acceleration even when V4 did not
preselect it. Every candidate is revalidated against fresh Bitvavo execution
data immediately before email delivery.
"""
from __future__ import annotations

import copy
from typing import Any

from research.common import finite
from research.decision_layer import decide

ACCELERATION_ACTION = "ACCELERATION_READY"
ACTIONABLE_STATUSES = {"BUY_READY", "REENTRY_READY", ACCELERATION_ACTION}
MIN_ACCELERATION_SCORE = 6.50
MIN_ACCELERATION_EVIDENCE = 3
MIN_QUOTE_VOLUME_EUR = 75_000.0


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def _v4_candidate(obs: dict[str, Any]) -> dict[str, Any] | None:
    baseline = obs.get("baseline") or {}
    if not baseline.get("buy_ready"):
        return None
    if baseline.get("action_status") not in {"BUY_READY", "REENTRY_READY"}:
        return None
    if not (obs.get("data_quality") or {}).get("ok"):
        return None
    plan = obs.get("trade_plan") or {}
    if not plan.get("valid"):
        return None
    row = copy.deepcopy(baseline)
    row.update(
        {
            "market": obs.get("market"),
            "last": obs.get("price_eur", baseline.get("last")),
            "data_quality": copy.deepcopy(obs.get("data_quality") or {}),
            "trade_plan": copy.deepcopy(plan),
            "acceleration": copy.deepcopy(obs.get("acceleration") or {}),
            "signal_score": max(
                _n(baseline.get("opportunity_score")),
                _n(baseline.get("entry_score")),
            ),
            "signal_source": "V4",
            "signal_sources": ["V4"],
        }
    )
    return row


def _acceleration_candidate(
    obs: dict[str, Any], decision_by_market: dict[str, dict[str, Any]]
) -> dict[str, Any] | None:
    quality = obs.get("data_quality") or {}
    acceleration = obs.get("acceleration") or {}
    if not quality.get("ok"):
        return None
    if acceleration.get("state") != "CONFIRMED_ACCELERATION":
        return None
    if _n(acceleration.get("score"), -1.0) < MIN_ACCELERATION_SCORE:
        return None
    if int(_n(acceleration.get("evidence_count"))) < MIN_ACCELERATION_EVIDENCE:
        return None
    if acceleration.get("buyability") == "DETECTED_BUT_TOO_LATE":
        return None

    baseline = obs.get("baseline") or {}
    quote_volume = _n(
        obs.get("quote_volume_24h_eur"),
        _n(baseline.get("quote_volume_24h_eur")),
    )
    if quote_volume < MIN_QUOTE_VOLUME_EUR:
        return None
    market = obs.get("market")
    price = _n(obs.get("price_eur"), -1.0)
    if not market or price <= 0:
        return None

    decision = decision_by_market.get(market) or {}
    accel_score = _n(acceleration.get("score"))
    row = {
        "market": market,
        "last": price,
        "quote_volume_24h_eur": quote_volume,
        "buy_ready": True,
        "action_status": ACCELERATION_ACTION,
        "signal_score": accel_score,
        "opportunity_score": _n(baseline.get("opportunity_score"), accel_score),
        "entry_score": _n(baseline.get("entry_score"), accel_score),
        "trend_score": _n(baseline.get("trend_score")),
        "risk_flags": list(baseline.get("risk_flags") or []),
        "data_quality": copy.deepcopy(quality),
        "trade_plan": copy.deepcopy(obs.get("trade_plan") or {}),
        "acceleration": copy.deepcopy(acceleration),
        "decision_bucket": decision.get("bucket"),
        "decision_action": decision.get("action"),
        "signal_source": "DIRECT_ACCELERATION",
        "signal_sources": ["DIRECT_ACCELERATION"],
    }
    return row


def build_alert_payload(
    observations: list[dict[str, Any]],
    v4_buys: list[dict[str, Any]],
    generated_at_utc: str,
) -> dict[str, Any]:
    """Return one normalized production alert payload.

    V4 candidates and direct acceleration candidates share the same final
    execution gate. Direct acceleration cannot auto-trade and cannot bypass
    fresh order-book, price-drift, candle-structure or risk checks.
    """
    decisions = decide(observations)
    decision_by_market = {
        row.get("market"): row for row in decisions.get("ranked", []) if row.get("market")
    }

    by_market: dict[str, dict[str, Any]] = {}
    for obs in v4_buys:
        row = _v4_candidate(obs)
        if row:
            by_market[row["market"]] = row

    for obs in observations:
        row = _acceleration_candidate(obs, decision_by_market)
        if not row:
            continue
        market = row["market"]
        current = by_market.get(market)
        if current is None:
            by_market[market] = row
            continue
        sources = sorted(set(current.get("signal_sources", [])) | {"DIRECT_ACCELERATION"})
        current["signal_sources"] = sources
        current["signal_source"] = "+".join(sources)
        current["signal_score"] = max(
            _n(current.get("signal_score")), _n(row.get("signal_score"))
        )
        current["acceleration"] = row["acceleration"]
        current["decision_bucket"] = row.get("decision_bucket")
        current["decision_action"] = row.get("decision_action")

    watch = sorted(
        by_market.values(),
        key=lambda row: (
            _n(row.get("signal_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )
    return {
        "schema": "production_alert_candidates_v2",
        "generated_at_utc": generated_at_utc,
        "policy": "FULL_UNIVERSE_DIRECT_SCAN_WITH_FINAL_EXECUTION_GATE",
        "oracle_required": False,
        "hosted_probe_required": False,
        "actionable_statuses": sorted(ACTIONABLE_STATUSES),
        "watch": watch,
    }
