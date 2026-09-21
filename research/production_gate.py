"""Pure Solaire candidate gate over the complete Bitvavo EUR scan.

Detection and execution remain separate. BUILDING and CONFIRMED accelerations
are exported for episode memory; only confirmed accelerations are actionable.
"""
from __future__ import annotations

import copy
from typing import Any

from research.common import finite
from research.production_context import candidate_context

ACCELERATION_ACTION = "ACCELERATION_READY"
ACTIONABLE_STATUSES = {ACCELERATION_ACTION}
TRACKED_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}
MIN_ACCELERATION_SCORE = 6.50
MIN_ACCELERATION_EVIDENCE = 3


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def _tracking_row(
    obs: dict[str, Any],
    market_context: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    quality = obs.get("data_quality") or {}
    acceleration = obs.get("acceleration") or {}
    state = acceleration.get("state")
    if not quality.get("ok") or state not in TRACKED_STATES:
        return None

    market = obs.get("market")
    price = _n(obs.get("price_eur"), -1.0)
    if not market or price <= 0:
        return None

    result = {
        "market": market,
        "last": price,
        "change_24h_pct": obs.get("change_24h_pct"),
        "quote_volume_24h_eur": _n(obs.get("quote_volume_24h_eur")),
        "signal_score": _n(acceleration.get("score")),
        "signal_state": state,
        "data_quality": copy.deepcopy(quality),
        "acceleration": copy.deepcopy(acceleration),
        "signal_source": "DIRECT_ACCELERATION",
    }
    if market_context:
        result["context"] = candidate_context(obs, market_context)
    return result


def _candidate(
    obs: dict[str, Any],
    market_context: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    row = _tracking_row(obs, market_context)
    if row is None:
        return None
    acceleration = row["acceleration"]
    if acceleration.get("state") != "CONFIRMED_ACCELERATION":
        return None
    if _n(acceleration.get("score"), -1.0) < MIN_ACCELERATION_SCORE:
        return None
    if int(_n(acceleration.get("evidence_count"))) < MIN_ACCELERATION_EVIDENCE:
        return None

    row["action_status"] = ACCELERATION_ACTION
    return row


def build_alert_payload(
    observations: list[dict[str, Any]],
    generated_at_utc: str,
    market_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    tracking = [
        row
        for obs in observations
        if (row := _tracking_row(obs, market_context)) is not None
    ]
    tracking.sort(
        key=lambda row: (
            _n(row.get("signal_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )

    watch = [
        row
        for obs in observations
        if (row := _candidate(obs, market_context)) is not None
    ]
    watch.sort(
        key=lambda row: (
            _n(row.get("signal_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )
    return {
        "schema": "production_alert_candidates_v4",
        "generated_at_utc": generated_at_utc,
        "policy": "SOLAIRE_FULL_UNIVERSE_DIRECT_ACCELERATION",
        "oracle_required": False,
        "hosted_probe_required": False,
        "v4_required": False,
        "decision_layer_required": False,
        "actionable_statuses": sorted(ACTIONABLE_STATUSES),
        "market_context": copy.deepcopy(market_context or {}),
        "tracking": tracking,
        "watch": watch,
    }
