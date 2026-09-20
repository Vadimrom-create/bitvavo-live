"""Pure Solaire candidate gate over the complete Bitvavo EUR scan.

This module has no dependency on V3/V4, Decision Layer, Oracle/Railway,
portfolio state or transport cooldowns. It only turns confirmed direct
acceleration into candidates for a separate execution-quality gate.
"""
from __future__ import annotations

import copy
from typing import Any

from research.common import finite

ACCELERATION_ACTION = "ACCELERATION_READY"
ACTIONABLE_STATUSES = {ACCELERATION_ACTION}
MIN_ACCELERATION_SCORE = 6.50
MIN_ACCELERATION_EVIDENCE = 3


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def _candidate(obs: dict[str, Any]) -> dict[str, Any] | None:
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

    market = obs.get("market")
    price = _n(obs.get("price_eur"), -1.0)
    if not market or price <= 0:
        return None

    score = _n(acceleration.get("score"))
    return {
        "market": market,
        "last": price,
        "change_24h_pct": obs.get("change_24h_pct"),
        "quote_volume_24h_eur": _n(obs.get("quote_volume_24h_eur")),
        "action_status": ACCELERATION_ACTION,
        "signal_score": score,
        "data_quality": copy.deepcopy(quality),
        "acceleration": copy.deepcopy(acceleration),
        "signal_source": "DIRECT_ACCELERATION",
    }


def build_alert_payload(observations: list[dict[str, Any]], generated_at_utc: str) -> dict[str, Any]:
    watch = [row for obs in observations if (row := _candidate(obs)) is not None]
    watch.sort(
        key=lambda row: (
            _n(row.get("signal_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )
    return {
        "schema": "production_alert_candidates_v3",
        "generated_at_utc": generated_at_utc,
        "policy": "SOLAIRE_FULL_UNIVERSE_DIRECT_ACCELERATION",
        "oracle_required": False,
        "hosted_probe_required": False,
        "v4_required": False,
        "decision_layer_required": False,
        "actionable_statuses": sorted(ACTIONABLE_STATUSES),
        "watch": watch,
    }
