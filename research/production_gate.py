"""Solaire production candidate gate over the complete Bitvavo EUR scan.

Fresh NEWS is now a first-class production signal:
- material news can open an early NEWS_WATCH before price acceleration;
- news contributes materially to the candidate score;
- NEWS alone never authorizes a BUY. Confirmed market acceleration and the
  normal execution gate remain mandatory.
"""
from __future__ import annotations

import copy
from typing import Any

from research.common import finite
from research.production_context import candidate_context
from research.production_news import NEWS_WATCH_MIN, composite_score

ACCELERATION_ACTION = "ACCELERATION_READY"
ACTIONABLE_STATUSES = {ACCELERATION_ACTION}
TRACKED_ACCELERATION_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}
NEWS_TRACKED_STATES = {"NEWS_WATCH_POSITIVE", "NEWS_WATCH_NEGATIVE", "NEWS_WATCH_MIXED", "NEWS_WATCH_NEUTRAL"}
MIN_ACCELERATION_SCORE = 6.50
MIN_ACCELERATION_EVIDENCE = 3
MIN_COMPOSITE_SCORE = 6.50


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def _news_state(news: dict[str, Any]) -> str:
    direction = str(news.get("direction") or "NEUTRAL").upper()
    if direction not in {"POSITIVE", "NEGATIVE", "MIXED", "NEUTRAL"}:
        direction = "NEUTRAL"
    return "NEWS_WATCH_" + direction


def _tracking_row(
    obs: dict[str, Any],
    market_context: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    quality = obs.get("data_quality") or {}
    acceleration = obs.get("acceleration") or {}
    news = obs.get("news") or {}
    acceleration_state = acceleration.get("state")
    news_watch = bool(news.get("watch_trigger")) and _n(news.get("score")) >= NEWS_WATCH_MIN

    if not quality.get("ok"):
        return None
    if acceleration_state not in TRACKED_ACCELERATION_STATES and not news_watch:
        return None

    market = obs.get("market")
    price = _n(obs.get("price_eur"), -1.0)
    if not market or price <= 0:
        return None

    quant_score = _n(acceleration.get("score"))
    final_score = composite_score(quant_score, news)
    signal_state = (
        acceleration_state
        if acceleration_state in TRACKED_ACCELERATION_STATES
        else _news_state(news)
    )
    if news_watch and acceleration_state in TRACKED_ACCELERATION_STATES:
        source = "NEWS_PLUS_DIRECT_ACCELERATION"
    elif news_watch:
        source = "NEWS"
    else:
        source = "DIRECT_ACCELERATION"

    result = {
        "market": market,
        "last": price,
        "change_24h_pct": obs.get("change_24h_pct"),
        "quote_volume_24h_eur": _n(obs.get("quote_volume_24h_eur")),
        "signal_score": final_score,
        "quant_score": quant_score,
        "news_score": _n(news.get("score")),
        "signal_state": signal_state,
        "data_quality": copy.deepcopy(quality),
        "acceleration": copy.deepcopy(acceleration),
        "news": copy.deepcopy(news),
        "signal_source": source,
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

    # NEWS may discover and prioritise the setup, but cannot create a BUY alone.
    acceleration = row["acceleration"]
    if acceleration.get("state") != "CONFIRMED_ACCELERATION":
        return None
    if _n(acceleration.get("score"), -1.0) < MIN_ACCELERATION_SCORE:
        return None
    if int(_n(acceleration.get("evidence_count"))) < MIN_ACCELERATION_EVIDENCE:
        return None
    # Negative material news is allowed to lower the final long score.
    if _n(row.get("signal_score"), -1.0) < MIN_COMPOSITE_SCORE:
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
            _n(row.get("news_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )

    news_watch = [
        row for row in tracking if (row.get("news") or {}).get("watch_trigger")
    ]
    news_watch.sort(
        key=lambda row: (
            _n(row.get("news_score")),
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
            _n(row.get("news_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )
    return {
        "schema": "production_alert_candidates_v5_news",
        "generated_at_utc": generated_at_utc,
        "policy": "SOLAIRE_NEWS_PLUS_DIRECT_ACCELERATION",
        "news_policy": {
            "production": True,
            "watch_before_quant": True,
            "news_alone_can_buy": False,
            "weight_in_composite": 0.35,
            "news_watch_min": NEWS_WATCH_MIN,
        },
        "oracle_required": False,
        "hosted_probe_required": False,
        "v4_required": False,
        "decision_layer_required": False,
        "actionable_statuses": sorted(ACTIONABLE_STATUSES),
        "market_context": copy.deepcopy(market_context or {}),
        "news_watch": news_watch,
        "tracking": tracking,
        "watch": watch,
    }
