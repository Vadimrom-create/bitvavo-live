#!/usr/bin/env python3
"""Solaire final execution gate and BUY email transport.

Detection is already complete before this script runs. This layer may reject an
entry only for current execution-quality reasons: inactive market, insufficient
liquidity, invalid book, excessive spread, stale/invalid 15m structure or an
invalid structural risk/reward plan. Signal-price drift is measured, never used
as a fixed veto.
"""
from __future__ import annotations

import json
import os
import smtplib
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import email_alert
from research.common import atomic_json, finite, freshness, read_json, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_alerts import mark_sent, mark_suppressed, select_events
from research.risk import structural_plan

INPUT = "production_alert_candidates.json"
STATE = "production_alert_state.json"
STATUS = "production_alert_status.json"
MIN_QUOTE_VOLUME_EUR = 75_000.0
MAX_SPREAD = 0.005
MAX_STOP_DISTANCE_PCT = 10.0
MIN_15M_CONSOLIDATION_RANGE_PCT = 6.0
THESIS_MAX_AGE_SECONDS = 24 * 60 * 60


def structural_range_ready(features: dict) -> bool:
    value = finite(features.get("consolidation_range_pct"))
    return value is not None and value >= MIN_15M_CONSOLIDATION_RANGE_PCT


def closed_5m_lows(raw: list, now: float) -> list[dict]:
    """Keep the full raw closed 5m history needed to audit a 24h thesis."""
    result = []
    for row in raw:
        if not isinstance(row, list) or len(row) < 4:
            continue
        timestamp = finite(row[0])
        low = finite(row[3])
        if timestamp is None or low is None or low <= 0:
            continue
        if timestamp != int(timestamp) or int(timestamp) % 300_000:
            continue
        if timestamp + 300_000 <= now * 1000:
            result.append({"t": int(timestamp), "l": low})
    return sorted(result, key=lambda candle: candle["t"])


def credentials():
    user = os.getenv("ALERT_GMAIL_USER", "").strip()
    recipient = os.getenv("ALERT_EMAIL_TO", "").strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "").strip().replace(" ", "")
    if recipient.lower() != "bellonirom@gmail.com" or not user or not password:
        return None
    return user, password, recipient


def market_inputs(client: PublicClient, market: str, now: float):
    book = client.get("/" + market + "/book", {"depth": 25}, cache=False)
    bid = finite(book["bids"][0][0]) if book.get("bids") else None
    ask = finite(book["asks"][0][0]) if book.get("asks") else None
    retrieved = client.metadata("/" + market + "/book", {"depth": 25}).get(
        "retrieved_at_utc"
    )
    raw = client.get(
        "/" + market + "/candles",
        {"interval": "15m", "limit": 100},
        cache=False,
    )
    candles = closed_candles(raw, "15m", now)
    features = describe(candles, "15m")
    raw_5m = client.get(
        "/" + market + "/candles",
        {"interval": "5m", "limit": 300},
        cache=False,
    )
    candles_5m = closed_5m_lows(raw_5m, now)
    return (
        {"bid": bid, "ask": ask, "retrieved_at_utc": retrieved},
        features,
        candles_5m,
    )


def validate(row: dict, client: PublicClient, metadata: dict[str, dict], now: float):
    market = row.get("market")
    if not market or market not in metadata:
        return None, "MARKET_UNAVAILABLE"

    volume = finite(row.get("quote_volume_24h_eur"), 0.0)
    if volume < MIN_QUOTE_VOLUME_EUR:
        return None, "INSUFFICIENT_EXECUTION_LIQUIDITY"

    quote, features, candles_5m = market_inputs(client, market, now)
    bid = finite(quote.get("bid"))
    ask = finite(quote.get("ask"))
    signal_price = finite(row.get("last"))
    if bid is None or ask is None or signal_price is None or not 0 < bid <= ask:
        return None, "INVALID_BOOK"

    spread = ask / bid - 1
    if spread > MAX_SPREAD:
        return None, "SPREAD_TOO_WIDE"

    fresh = freshness(
        now=now,
        retrieved=quote.get("retrieved_at_utc"),
        candle_start_ms=features.get("last_closed_start_ms"),
        interval="15m",
        max_retrieval_age=90,
    )
    if not features.get("valid") or not fresh["ok"]:
        return None, "STALE_OR_INVALID_STRUCTURE"

    structural_range_pct = finite(features.get("consolidation_range_pct"))
    if not structural_range_ready(features):
        return None, "STRUCTURAL_RANGE_TOO_NARROW"

    trade = structural_plan({**row, "ask": ask}, features, metadata[market])
    if not trade.get("valid"):
        return None, trade.get("reason", "INVALID_PLAN")
    if finite(trade.get("stop_distance_pct"), 999.0) > MAX_STOP_DISTANCE_PCT:
        return None, "STRUCTURAL_STOP_TOO_WIDE"

    drift_pct = (ask / signal_price - 1) * 100
    return {
        "row": row,
        "quote": quote,
        "trade": trade,
        "spread_pct": spread * 100,
        "price_drift_pct": drift_pct,
        "structural_range_15m_pct": structural_range_pct,
        "candles_5m": candles_5m,
    }, None


def prior_buy_thesis_active(
    state: dict,
    validated: dict,
    now: float,
) -> tuple[bool, str]:
    """Suppress repeat BUYs while the previous alerted trade thesis still holds."""
    market = validated["row"]["market"]
    previous = (state.get("markets") or {}).get(market) or {}

    # A fresh acceleration episode is new information, not a duplicate of an
    # older emailed thesis. Do not let an unfilled/unconfirmed prior user trade
    # suppress a later re-acceleration merely because the old stop was never
    # breached.
    current_episode = finite((validated.get("row") or {}).get("episode"))
    sent_episode = finite(previous.get("sent_episode"))
    if (
        current_episode is not None
        and sent_episode is not None
        and int(current_episode) > int(sent_episode)
    ):
        return False, "NEW_ACCELERATION_EPISODE"

    sent_at = finite(previous.get("last_sent_ts"))
    stop = finite(previous.get("last_sent_stop_eur"))
    if sent_at is None or stop is None or stop <= 0:
        return False, "NO_TRACKED_PRIOR_BUY_THESIS"
    age = now - sent_at
    if age < -30:
        return True, "PRIOR_BUY_THESIS_TIMESTAMP_INVALID"
    if age > THESIS_MAX_AGE_SECONDS:
        return False, "PRIOR_BUY_THESIS_EXPIRED"

    ask = finite((validated.get("quote") or {}).get("ask"))
    if ask is not None and ask <= stop:
        return False, "PRIOR_BUY_THESIS_INVALIDATED"

    # Only use bars that started after the bar containing the original alert.
    # This avoids falsely attributing a pre-alert wick to the post-alert thesis.
    first_full_bar_ms = ((int(sent_at * 1000) // 300_000) + 1) * 300_000
    lows = [
        finite(candle.get("l"))
        for candle in validated.get("candles_5m") or []
        if candle.get("t", 0) >= first_full_bar_ms
    ]
    if any(low is not None and low <= stop for low in lows):
        return False, "PRIOR_BUY_THESIS_INVALIDATED"
    return True, "PRIOR_BUY_THESIS_STILL_ACTIVE"


def body(validated: dict) -> str:
    row = validated["row"]
    trade = validated["trade"]
    accel = row.get("acceleration") or {}
    return "\n".join(
        [
            "ACHÈTE — signal Solaire validé",
            "",
            f"Marché : {row['market']}",
            f"Score signal : {finite(row.get('signal_score'), 0):.2f}/10",
            f"Accélération : {accel.get('state', 'n/a')} — preuves {accel.get('evidence_count', 'n/a')}",
            f"Portée confirmation : {accel.get('confirmation_scope', 'n/a')} — 15 min {'OUI' if accel.get('timeframe_confirmation_15m') else 'NON'} ({finite((accel.get('components') or {}).get('confirmation_15m'), 0):.2f}/10)",
            f"Prix signal : {finite(row.get('last'), 0):.8g} €",
            f"Début épisode : {finite(row.get('episode_start_price'), finite(row.get('last'), 0)):.8g} €",
            f"Extension depuis début épisode : {finite(row.get('episode_extension_pct'), 0):+.2f} %",
            f"Âge de l'épisode : {finite(row.get('episode_age_seconds'), 0) / 60:.1f} min",
            f"Phase : {row.get('signal_phase', 'n/a')}",
            f"Entrée revalidée : {trade['entry_eur']:.8g} €",
            f"Dérive depuis signal : {validated['price_drift_pct']:+.2f} %",
            f"Spread actuel : {validated['spread_pct']:.3f} %",
            f"Amplitude structurelle 15 min (2 h) : {validated['structural_range_15m_pct']:.2f} %",
            f"Stop structurel : {trade['stop_eur']:.8g} €",
            f"Distance stop : {trade['stop_distance_pct']:.2f} %",
            f"TP1 théorique : {trade['tp1_eur']:.8g} €",
            f"Montant guide : {trade['stake_eur']:.2f} €",
            f"Risque théorique : {trade['theoretical_loss_eur']:.2f} €",
            "",
            f"Contexte marché (shadow) : {(row.get('context') or {}).get('regime', 'n/a')}",
            f"Phase court terme (shadow) : {(row.get('context') or {}).get('regime_phase', (row.get('context') or {}).get('short_term_phase', 'n/a'))}",
            f"Breadth + 1 h : {finite((row.get('context') or {}).get('breadth_positive_1h_pct'), 0):.1f} %",
            f"Breadth + 4 h : {finite((row.get('context') or {}).get('breadth_positive_4h_pct'), 0):.1f} %",
            f"Force relative 1 h : {finite((row.get('context') or {}).get('relative_strength_1h_pp'), 0):+.2f} pp",
            f"Force relative 4 h : {finite((row.get('context') or {}).get('relative_strength_4h_pp'), 0):+.2f} pp",
            "Le contexte est observé et journalisé mais ne peut pas bloquer un BUY.",
            "",
            "Le signal n'a pas été filtré par V4, Decision Layer, chase risk ou un cooldown global.",
            "Le carnet, le spread, la structure 15 min et le ratio risque/rendement viennent d'être revalidés.",
            "Aucun ordre n'a été envoyé automatiquement.",
        ]
    )


def subject_for(selected: list[dict]) -> str:
    if len(selected) == 1:
        row = selected[0]["row"]
        phase = row.get("signal_phase", "CONFIRMED")
        return f"ACHÈTE — {row['market']} — Solaire {phase}"
    markets = ", ".join(item["row"]["market"] for item in selected[:4])
    suffix = "" if len(selected) <= 4 else f" +{len(selected)-4}"
    return f"ACHÈTE — {len(selected)} candidats Solaire — {markets}{suffix}"


def body_for(selected: list[dict]) -> str:
    if len(selected) == 1:
        return body(selected[0])
    sections = [
        f"ACHÈTE — {len(selected)} signaux Solaire validés dans le même scan",
        "Tous les candidats ci-dessous ont passé le gate d'exécution et le contrôle de thèse antérieure.",
        "Ils sont classés selon l'ordre Solaire; aucun ordre n'a été envoyé automatiquement.",
    ]
    for idx, validated in enumerate(selected, 1):
        sections.extend([
            "",
            "=" * 48,
            f"CANDIDAT {idx}/{len(selected)}",
            "=" * 48,
            body(validated),
        ])
    return "\n".join(sections)


def delivery_record(validated: dict) -> dict:
    row = validated["row"]
    trade = validated["trade"]
    return {
        "market": row["market"],
        "price_drift_pct": validated.get("price_drift_pct"),
        "spread_pct": validated.get("spread_pct"),
        "structural_range_15m_pct": validated.get("structural_range_15m_pct"),
        "signal_phase": row.get("signal_phase"),
        "episode_extension_pct": row.get("episode_extension_pct"),
        "episode_age_seconds": row.get("episode_age_seconds"),
        "stop_distance_pct": trade.get("stop_distance_pct"),
        "prior_thesis_status": validated.get("prior_thesis_status"),
        "entry_eur": trade.get("entry_eur"),
        "stop_eur": trade.get("stop_eur"),
        "tp1_eur": trade.get("tp1_eur"),
        "tp2_eur": trade.get("tp2_eur"),
        "stake_eur": trade.get("stake_eur"),
        "market_context": row.get("context") or {},
    }


def main() -> int:
    now = time.time()
    status = {
        "checked_at_utc": utc(now),
        "status": "STARTING",
        "email": "NONE",
        "policy": "SOLAIRE_V2_EXECUTION_GATE",
    }
    payload = read_json(INPUT, {})
    state = read_json(STATE, {"markets": {}})
    events, state = select_events(payload, state, now, limit=None)
    atomic_json(STATE, state)

    if not events:
        status.update(status="OK", reason="NO_NEW_ACTIONABLE_EPISODE")
        atomic_json(STATUS, status)
        print("SOLAIRE_ALERT " + json.dumps(status))
        return 0

    try:
        client = PublicClient(timeout=10, retries=2)
        client.get("/time", cache=False)
        if abs(client.server_offset) > 30:
            raise RuntimeError("EXCHANGE_CLOCK_SKEW")
        metadata = {
            m["market"]: m
            for m in client.get("/markets")
            if m.get("quote") == "EUR" and m.get("status") == "trading"
        }

        selected = []
        rejections = []
        for row in events:
            checked_at = time.time()
            validated, reason = validate(row, client, metadata, checked_at)
            if validated:
                thesis_active, thesis_status = prior_buy_thesis_active(
                    state, validated, checked_at
                )
                if thesis_active:
                    rejections.append(
                        {
                            "market": row.get("market"),
                            "reason": thesis_status,
                        }
                    )
                    state = mark_suppressed(
                        state,
                        row,
                        checked_at,
                        thesis_status,
                    )
                    continue
                validated["prior_thesis_status"] = thesis_status
                selected.append(validated)
                continue
            rejections.append({"market": row.get("market"), "reason": reason})
        status["rejections"] = rejections
        atomic_json(STATE, state)

        if not selected:
            status.update(
                status="OK",
                reason="NO_CANDIDATE_PASSED_FINAL_EXECUTION_GATE",
                evaluated_event_count=len(events),
            )
            atomic_json(STATUS, status)
            print("SOLAIRE_ALERT " + json.dumps(status))
            return 0
    except (RuntimeError, ValueError, KeyError) as exc:
        status.update(status="DEGRADED", reason=str(exc))
        atomic_json(STATUS, status)
        print("SOLAIRE_ALERT " + json.dumps(status))
        return 0

    creds = credentials()
    if creds is None:
        status.update(status="DEGRADED", reason="SMTP_CONFIG_MISSING")
        atomic_json(STATUS, status)
        print("SOLAIRE_ALERT " + json.dumps(status))
        return 0

    primary = selected[0]
    primary_row = primary["row"]
    try:
        email_alert.send_email(
            creds[0], creds[1], creds[2],
            subject_for(selected),
            body_for(selected),
        )
    except smtplib.SMTPAuthenticationError:
        status.update(
            status="DEGRADED",
            reason="SMTP_AUTHENTICATION_ERROR",
            email="DELIVERY_PENDING_RETRY",
            market=primary_row["market"],
            markets=[item["row"]["market"] for item in selected],
            selected_count=len(selected),
        )
        atomic_json(STATUS, status)
        print("SOLAIRE_ALERT " + json.dumps(status))
        return 0
    except (smtplib.SMTPException, OSError, TimeoutError) as exc:
        status.update(
            status="DEGRADED",
            reason=type(exc).__name__,
            email="DELIVERY_PENDING_RETRY",
            market=primary_row["market"],
            markets=[item["row"]["market"] for item in selected],
            selected_count=len(selected),
        )
        atomic_json(STATUS, status)
        print("SOLAIRE_ALERT " + json.dumps(status))
        return 0

    sent_at = time.time()
    deliveries = []
    for validated in selected:
        row = validated["row"]
        state = mark_sent(state, row, sent_at, validated["trade"])
        deliveries.append(delivery_record(validated))
    atomic_json(STATE, state)

    primary_delivery = deliveries[0]
    status.update(
        status="OK",
        reason="DELIVERED",
        email="DELIVERY_COMPLETED",
        market=primary_delivery["market"],
        markets=[item["market"] for item in deliveries],
        selected_count=len(deliveries),
        deliveries=deliveries,
        evaluated_event_count=len(events),
        price_drift_pct=primary_delivery["price_drift_pct"],
        spread_pct=primary_delivery["spread_pct"],
        structural_range_15m_pct=primary_delivery.get("structural_range_15m_pct"),
        signal_phase=primary_delivery.get("signal_phase"),
        episode_extension_pct=primary_delivery.get("episode_extension_pct"),
        episode_age_seconds=primary_delivery.get("episode_age_seconds"),
        stop_distance_pct=primary_delivery.get("stop_distance_pct"),
        prior_thesis_status=primary_delivery.get("prior_thesis_status"),
        entry_eur=primary_delivery.get("entry_eur"),
        stop_eur=primary_delivery.get("stop_eur"),
        tp1_eur=primary_delivery.get("tp1_eur"),
        tp2_eur=primary_delivery.get("tp2_eur"),
        stake_eur=primary_delivery.get("stake_eur"),
        market_context=primary_delivery.get("market_context") or {},
    )
    atomic_json(STATUS, status)
    print("SOLAIRE_ALERT " + json.dumps(status))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
