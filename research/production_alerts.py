"""Solaire alert episode policy.

One delivery per continuous market episode. There is deliberately no global
cooldown and no fixed multi-hour per-market cooldown: an independent market or
a genuinely new episode must never be censored by an older alert.
"""
from __future__ import annotations

import copy
from datetime import datetime
from typing import Any

MAX_SNAPSHOT_AGE = 15 * 60
ACTIONABLE_STATUSES = {"ACCELERATION_READY"}


def _ts(value: Any) -> float | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def _n(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def select_events(payload: dict[str, Any], state: dict[str, Any], now: float, limit: int | None = None):
    state = copy.deepcopy(state or {})
    state.setdefault("markets", {})
    generated = _ts(payload.get("generated_at_utc"))
    if generated is None or not -30 <= now - generated <= MAX_SNAPSHOT_AGE:
        return [], state

    eligible = {
        row["market"]: row
        for row in payload.get("watch", [])
        if isinstance(row, dict)
        and row.get("market")
        and row.get("action_status") in ACTIONABLE_STATUSES
        and (row.get("data_quality") or {}).get("ok", False)
    }

    events = []
    for market in sorted(set(state["markets"]) | set(eligible)):
        previous = state["markets"].setdefault(market, {})
        row = eligible.get(market)
        if row is None:
            previous["active"] = False
            continue

        was_active = bool(previous.get("active", False))
        if not was_active:
            previous["episode"] = int(previous.get("episode", 0)) + 1
        previous["active"] = True

        episode = int(previous.get("episode", 0))
        sent_episode = int(previous.get("sent_episode", 0))
        if episode != sent_episode:
            events.append(row)

    events.sort(
        key=lambda row: (
            _n(row.get("signal_score")),
            _n(row.get("quote_volume_24h_eur")),
        ),
        reverse=True,
    )
    return (events if limit is None else events[:limit]), state


def mark_sent(state: dict[str, Any], row: dict[str, Any], sent_at: float) -> dict[str, Any]:
    state = copy.deepcopy(state)
    market = row["market"]
    previous = state.setdefault("markets", {}).setdefault(market, {})
    previous.update(
        sent_episode=int(previous.get("episode", 0)),
        last_sent_ts=sent_at,
        signal_score=row.get("signal_score"),
        price=row.get("last"),
        status=row.get("action_status"),
        signal_source=row.get("signal_source"),
    )
    state["updated_at_ts"] = sent_at
    return state
