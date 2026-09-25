"""Solaire alert episode policy with trajectory memory.

BUILDING and CONFIRMED states belong to the same acceleration episode.
This prevents score oscillations from creating fake new opportunities and
lets the alert layer measure how far price has already travelled before the
first actionable confirmation.

No global cooldown and no fixed multi-hour per-market cooldown are used.
"""
from __future__ import annotations

import copy
from datetime import datetime
from typing import Any

MAX_SNAPSHOT_AGE = 15 * 60
ACTIONABLE_STATUSES = {"ACCELERATION_READY"}
TRACKED_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}


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


def _extension_pct(start_price: Any, current_price: Any) -> float:
    start = _n(start_price)
    current = _n(current_price)
    if start <= 0 or current <= 0:
        return 0.0
    return (current / start - 1.0) * 100.0


def _event_row(row: dict[str, Any], previous: dict[str, Any], generated: float) -> dict[str, Any]:
    result = copy.deepcopy(row)
    started = _n(previous.get("episode_started_ts"), generated)
    first_confirmed = _n(previous.get("first_confirmed_ts"), generated)
    extension = _extension_pct(previous.get("episode_start_price"), row.get("last"))
    result.update(
        episode=int(previous.get("episode", 0)),
        episode_started_ts=started,
        episode_start_price=previous.get("episode_start_price"),
        episode_start_score=previous.get("episode_start_score"),
        first_confirmed_ts=first_confirmed,
        first_confirmed_price=previous.get("first_confirmed_price"),
        episode_age_seconds=max(0.0, generated - started),
        confirmation_age_seconds=max(0.0, generated - first_confirmed),
        episode_extension_pct=round(extension, 4),
        signal_phase=(
            "FIRST_CONFIRMATION"
            if abs(generated - first_confirmed) < 1.0
            else "PERSISTENT_CONFIRMATION"
        ),
    )
    return result


def select_events(payload: dict[str, Any], state: dict[str, Any], now: float, limit: int | None = None):
    state = copy.deepcopy(state or {})
    state.setdefault("markets", {})
    generated = _ts(payload.get("generated_at_utc"))
    if generated is None or not -30 <= now - generated <= MAX_SNAPSHOT_AGE:
        return [], state

    tracking_rows = payload.get("tracking")
    if not isinstance(tracking_rows, list):
        # Backward compatibility for payloads created before trajectory memory.
        tracking_rows = payload.get("watch", [])

    tracked = {
        row["market"]: row
        for row in tracking_rows
        if isinstance(row, dict)
        and row.get("market")
        and (
            row.get("signal_state") in TRACKED_STATES
            or (row.get("acceleration") or {}).get("state") in TRACKED_STATES
            or row.get("action_status") in ACTIONABLE_STATUSES
        )
        and (row.get("data_quality") or {}).get("ok", False)
    }
    eligible = {
        row["market"]: row
        for row in payload.get("watch", [])
        if isinstance(row, dict)
        and row.get("market")
        and row.get("action_status") in ACTIONABLE_STATUSES
        and (row.get("data_quality") or {}).get("ok", False)
    }

    events = []
    for market in sorted(set(state["markets"]) | set(tracked)):
        previous = state["markets"].setdefault(market, {})
        tracked_row = tracked.get(market)
        if tracked_row is None:
            if previous.get("active"):
                previous["active"] = False
                previous["episode_ended_ts"] = generated
            continue

        was_active = bool(previous.get("active", False))
        if not was_active:
            previous["episode"] = int(previous.get("episode", 0)) + 1
            previous["episode_started_ts"] = generated
            previous["episode_start_price"] = tracked_row.get("last")
            previous["episode_start_score"] = tracked_row.get("signal_score")
            previous["episode_start_state"] = (
                tracked_row.get("signal_state")
                or (tracked_row.get("acceleration") or {}).get("state")
            )
            previous["max_signal_score"] = _n(tracked_row.get("signal_score"))
            previous.pop("first_confirmed_ts", None)
            previous.pop("first_confirmed_price", None)

        previous["active"] = True
        previous["current_state"] = (
            tracked_row.get("signal_state")
            or (tracked_row.get("acceleration") or {}).get("state")
        )
        previous["current_price"] = tracked_row.get("last")
        previous["current_score"] = tracked_row.get("signal_score")
        if was_active:
            previous["max_signal_score"] = max(
                _n(previous.get("max_signal_score")),
                _n(tracked_row.get("signal_score")),
            )

        row = eligible.get(market)
        if row is None:
            continue

        if previous.get("first_confirmed_ts") is None:
            previous["first_confirmed_ts"] = generated
            previous["first_confirmed_price"] = row.get("last")

        episode = int(previous.get("episode", 0))
        handled_episode = int(
            previous.get("handled_episode", previous.get("sent_episode", 0))
        )
        if episode != handled_episode:
            events.append(_event_row(row, previous, generated))

    # Signal quality leads the cross-sectional ordering. Extension remains a
    # risk/timing tiebreaker instead of outranking acceleration strength.
    # This avoids systematically demoting continuation moves simply because
    # they have already advanced while still preferring the cleaner entry when
    # signal quality is comparable.
    events.sort(
        key=lambda row: (
            -_n(row.get("signal_score")),
            -_n((row.get("acceleration") or {}).get("evidence_count")),
            max(0.0, _n(row.get("episode_extension_pct"))),
            _n(row.get("episode_age_seconds")),
            -_n(row.get("quote_volume_24h_eur")),
        )
    )
    return (events if limit is None else events[:limit]), state


def mark_suppressed(
    state: dict[str, Any],
    row: dict[str, Any],
    handled_at: float,
    reason: str,
) -> dict[str, Any]:
    """Mark one episode handled without claiming an email was sent."""
    state = copy.deepcopy(state)
    market = row["market"]
    previous = state.setdefault("markets", {}).setdefault(market, {})
    previous.update(
        handled_episode=int(previous.get("episode", 0)),
        last_suppressed_ts=handled_at,
        last_suppressed_reason=reason,
        last_suppressed_price=row.get("last"),
    )
    state["updated_at_ts"] = handled_at
    return state


def mark_sent(
    state: dict[str, Any],
    row: dict[str, Any],
    sent_at: float,
    trade: dict[str, Any] | None = None,
) -> dict[str, Any]:
    state = copy.deepcopy(state)
    market = row["market"]
    previous = state.setdefault("markets", {}).setdefault(market, {})
    episode = int(previous.get("episode", 0))
    previous.update(
        handled_episode=episode,
        sent_episode=episode,
        last_sent_ts=sent_at,
        signal_score=row.get("signal_score"),
        price=row.get("last"),
        status=row.get("action_status"),
        signal_source=row.get("signal_source"),
        last_sent_episode_extension_pct=row.get("episode_extension_pct"),
        last_sent_episode_age_seconds=row.get("episode_age_seconds"),
    )
    if trade:
        previous.update(
            last_sent_entry_eur=trade.get("entry_eur"),
            last_sent_stop_eur=trade.get("stop_eur"),
            last_sent_tp1_eur=trade.get("tp1_eur"),
            last_sent_stop_distance_pct=trade.get("stop_distance_pct"),
        )
    state["updated_at_ts"] = sent_at
    return state
