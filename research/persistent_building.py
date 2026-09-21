"""Shadow-only persistent BUILDING measurement for Solaire V2.

This module observes repeated BUILDING_ACCELERATION states across time. It never
changes detection, candidate ordering, execution validation, or email delivery.
"""
from __future__ import annotations

import copy
from datetime import datetime
from typing import Any

from research.common import finite

WINDOW_SECONDS = 6 * 60 * 60
MIN_SAMPLES = 4
MIN_SPAN_SECONDS = 30 * 60
MIN_NET_PROGRESS_PCT = 2.0
MIN_MAX_SCORE = 5.0
MIN_POSITIVE_STEP_RATIO = 0.60
MAX_EVENTS = 3000


def _ts(value: Any) -> float | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def _num(value: Any) -> float | None:
    return finite(value)


def _progress_pct(start: float | None, end: float | None) -> float | None:
    if start is None or end is None or start <= 0 or end <= 0:
        return None
    return (end / start - 1.0) * 100.0


def _metrics(samples: list[dict[str, Any]], now: float) -> dict[str, Any]:
    cutoff = now - WINDOW_SECONDS
    xs = [x for x in samples if finite(x.get("ts")) is not None and x["ts"] >= cutoff]
    xs.sort(key=lambda x: x["ts"])
    if not xs:
        return {
            "samples_6h": 0,
            "span_minutes": 0.0,
            "net_progress_pct": None,
            "max_score": None,
            "positive_step_ratio": None,
        }

    prices = [finite(x.get("price")) for x in xs]
    scores = [finite(x.get("score")) for x in xs]
    valid_prices = [p for p in prices if p is not None and p > 0]
    valid_scores = [s for s in scores if s is not None]

    positive = 0
    comparable = 0
    for left, right in zip(prices, prices[1:]):
        if left is None or right is None or left <= 0 or right <= 0:
            continue
        comparable += 1
        if right >= left:
            positive += 1

    first_price = valid_prices[0] if valid_prices else None
    last_price = valid_prices[-1] if valid_prices else None
    return {
        "samples_6h": len(xs),
        "first_seen_ts": xs[0]["ts"],
        "last_seen_ts": xs[-1]["ts"],
        "span_minutes": round((xs[-1]["ts"] - xs[0]["ts"]) / 60.0, 2),
        "first_price_eur": first_price,
        "last_price_eur": last_price,
        "net_progress_pct": (
            round(_progress_pct(first_price, last_price), 4)
            if first_price is not None and last_price is not None
            else None
        ),
        "max_score": round(max(valid_scores), 4) if valid_scores else None,
        "mean_score": (
            round(sum(valid_scores) / len(valid_scores), 4) if valid_scores else None
        ),
        "positive_step_ratio": (
            round(positive / comparable, 4) if comparable else None
        ),
    }


def qualifies(metrics: dict[str, Any]) -> bool:
    ratio = finite(metrics.get("positive_step_ratio"))
    progress = finite(metrics.get("net_progress_pct"))
    max_score = finite(metrics.get("max_score"))
    return bool(
        int(metrics.get("samples_6h") or 0) >= MIN_SAMPLES
        and finite(metrics.get("span_minutes"), 0.0) >= MIN_SPAN_SECONDS / 60.0
        and progress is not None
        and progress >= MIN_NET_PROGRESS_PCT
        and max_score is not None
        and max_score >= MIN_MAX_SCORE
        and ratio is not None
        and ratio >= MIN_POSITIVE_STEP_RATIO
    )


def update_shadow(
    payload: dict[str, Any],
    state: dict[str, Any] | None,
    journal: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    state = copy.deepcopy(state or {})
    journal = copy.deepcopy(journal or {})
    state.setdefault("schema", "solaire_persistent_building_state_v1")
    state.setdefault("markets", {})
    journal.setdefault("schema", "solaire_persistent_building_journal_v1")
    journal.setdefault("events", [])

    generated = _ts(payload.get("generated_at_utc"))
    if generated is None:
        return state, journal, {
            "status": "DEGRADED_NONBLOCKING",
            "reason": "INVALID_PAYLOAD_TIMESTAMP",
            "blocking": False,
        }

    tracked = {
        row.get("market"): row
        for row in payload.get("tracking", [])
        if isinstance(row, dict) and row.get("market")
    }

    confirmed_now = {
        market: row
        for market, row in tracked.items()
        if row.get("signal_state") == "CONFIRMED_ACCELERATION"
    }

    new_events = 0
    active_shadow = 0
    persistent_markets = []

    for market in sorted(set(state["markets"]) | set(tracked)):
        previous = state["markets"].setdefault(
            market,
            {"samples": [], "shadow_active": False},
        )
        samples = previous.setdefault("samples", [])
        cutoff = generated - WINDOW_SECONDS
        samples[:] = [x for x in samples if finite(x.get("ts")) is not None and x["ts"] >= cutoff]

        row = tracked.get(market)
        if row and row.get("signal_state") == "BUILDING_ACCELERATION":
            sample = {
                "ts": generated,
                "price": finite(row.get("last")),
                "score": finite(row.get("signal_score")),
            }
            # Idempotent across reruns of the same production snapshot.
            if not samples or finite(samples[-1].get("ts")) != generated:
                samples.append(sample)

        metrics = _metrics(samples, generated)
        is_persistent = qualifies(metrics)

        # Record a fresh shadow event only on the transition into qualification.
        if is_persistent and not previous.get("shadow_active", False):
            event = {
                "event_id": f"{market}|{int(generated)}",
                "market": market,
                "shadow_type": "PERSISTENT_BUILDING",
                "detected_at_utc": payload.get("generated_at_utc"),
                "detected_ts": generated,
                "baseline_price_eur": finite(
                    (row or {}).get("last"),
                    finite(metrics.get("last_price_eur")),
                ),
                "metrics_at_detection": copy.deepcopy(metrics),
                "confirmed_after_detection": False,
                "confirmation": None,
                "evaluations": {},
                "affects_detection": False,
                "affects_buy_gate": False,
                "affects_email": False,
            }
            journal["events"].append(event)
            new_events += 1

        previous["shadow_active"] = is_persistent
        previous["metrics"] = metrics
        previous["updated_at_ts"] = generated

        if is_persistent:
            active_shadow += 1
            persistent_markets.append(
                {
                    "market": market,
                    "metrics": copy.deepcopy(metrics),
                }
            )

    # If a market later confirms, attach that fact to all still-unconfirmed shadow
    # events created in the prior 24h. This is measurement only.
    for market, row in confirmed_now.items():
        for event in reversed(journal["events"]):
            if event.get("market") != market:
                continue
            if event.get("confirmed_after_detection"):
                continue
            detected_ts = finite(event.get("detected_ts"))
            if detected_ts is None or generated - detected_ts > 24 * 60 * 60:
                break
            event["confirmed_after_detection"] = True
            event["confirmation"] = {
                "ts": generated,
                "utc": payload.get("generated_at_utc"),
                "price_eur": finite(row.get("last")),
                "score": finite(row.get("signal_score")),
                "minutes_after_shadow": round((generated - detected_ts) / 60.0, 2),
            }

    journal["events"] = journal["events"][-MAX_EVENTS:]
    state["updated_at_ts"] = generated
    journal["updated_at_ts"] = generated

    persistent_markets.sort(
        key=lambda item: (
            finite(item["metrics"].get("net_progress_pct"), 0.0),
            finite(item["metrics"].get("max_score"), 0.0),
        ),
        reverse=True,
    )
    status = {
        "schema": "solaire_persistent_building_shadow_v1",
        "status": "OK",
        "blocking": False,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "window_hours": WINDOW_SECONDS / 3600,
        "criteria": {
            "min_samples": MIN_SAMPLES,
            "min_span_minutes": MIN_SPAN_SECONDS / 60,
            "min_net_progress_pct": MIN_NET_PROGRESS_PCT,
            "min_max_score": MIN_MAX_SCORE,
            "min_positive_step_ratio": MIN_POSITIVE_STEP_RATIO,
        },
        "active_shadow_markets": active_shadow,
        "new_shadow_events": new_events,
        "persistent_markets": persistent_markets[:25],
    }
    return state, journal, status
