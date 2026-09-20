#!/usr/bin/env python3
"""Send at most one production BUY alert after a fresh Bitvavo execution gate."""
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
from email_alert_v4 import select_events
from research.common import atomic_json, finite, freshness, read_json, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import plan as make_plan

INPUT = "production_alert_candidates.json"
STATE = "production_alert_state.json"
STATUS = "production_alert_status.json"
MAX_PRICE_DRIFT = 0.005
MAX_SPREAD = 0.005


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
    retrieved = client.metadata("/" + market + "/book", {"depth": 25}).get("retrieved_at_utc")
    raw = client.get("/" + market + "/candles", {"interval": "15m", "limit": 100}, cache=False)
    candles = closed_candles(raw, "15m", now)
    features = describe(candles, "15m")
    return {"bid": bid, "ask": ask, "retrieved_at_utc": retrieved}, features


def validate(row: dict, client: PublicClient, metadata: dict[str, dict], now: float):
    market = row.get("market")
    if not market or market not in metadata:
        return None, "MARKET_UNAVAILABLE"
    quote, features = market_inputs(client, market, now)
    bid, ask, signal_price = finite(quote.get("bid")), finite(quote.get("ask")), finite(row.get("last"))
    if bid is None or ask is None or signal_price is None or not 0 < bid <= ask:
        return None, "INVALID_BOOK"
    if ask / bid - 1 > MAX_SPREAD:
        return None, "SPREAD_TOO_WIDE"
    if abs(ask / signal_price - 1) > MAX_PRICE_DRIFT:
        return None, "PRICE_MOVED"
    if not features.get("valid") or not freshness(
        now=now,
        retrieved=quote.get("retrieved_at_utc"),
        candle_start_ms=features.get("last_closed_start_ms"),
        interval="15m",
        max_retrieval_age=90,
    )["ok"]:
        return None, "STALE_OR_INVALID_STRUCTURE"
    trade = make_plan({**row, "ask": ask}, features, metadata[market])
    if not trade.get("valid"):
        return None, trade.get("reason", "INVALID_PLAN")
    return {"row": row, "quote": quote, "trade": trade}, None


def body(validated: dict) -> str:
    row, trade = validated["row"], validated["trade"]
    accel = row.get("acceleration") or {}
    return "\n".join([
        "ACHÈTE — signal Bitvavo validé",
        "",
        f"Marché : {row['market']}",
        f"Source : {row.get('signal_source', 'DIRECT_SCAN')}",
        f"Score signal : {finite(row.get('signal_score'), 0):.2f}/10",
        f"Accélération : {accel.get('state', 'n/a')} — preuves {accel.get('evidence_count', 'n/a')}",
        f"Prix signal : {finite(row.get('last'), 0):.8g} €",
        f"Entrée revalidée : {trade['entry_eur']:.8g} €",
        f"Stop structurel : {trade['stop_eur']:.8g} €",
        f"TP1 théorique : {trade['tp1_eur']:.8g} €",
        f"Montant théorique : {trade['stake_eur']:.2f} €",
        f"Risque théorique : {trade['theoretical_loss_eur']:.2f} €",
        "",
        "Le carnet, le spread, le prix et la structure 15 min viennent d'être revalidés.",
        "Aucun ordre n'a été envoyé automatiquement.",
    ])


def main() -> int:
    now = time.time()
    status = {"checked_at_utc": utc(now), "status": "STARTING", "email": "NONE"}
    payload = read_json(INPUT, {})
    state = read_json(STATE, {"markets": {}})
    events, state = select_events(payload, state, now, limit=None)
    atomic_json(STATE, state)
    if not events:
        status.update(status="OK", reason="NO_NEW_ACTIONABLE_EPISODE")
        atomic_json(STATUS, status)
        print("PRODUCTION_ALERT " + json.dumps(status))
        return 0

    try:
        client = PublicClient(timeout=10, retries=2)
        client.get("/time", cache=False)
        if abs(client.server_offset) > 30:
            raise RuntimeError("EXCHANGE_CLOCK_SKEW")
        metadata = {
            m["market"]: m for m in client.get("/markets")
            if m.get("quote") == "EUR" and m.get("status") == "trading"
        }
        selected = None
        rejections = []
        for row in events:
            validated, reason = validate(row, client, metadata, time.time())
            if validated:
                selected = validated
                break
            rejections.append({"market": row.get("market"), "reason": reason})
        status["rejections"] = rejections
        if not selected:
            status.update(status="OK", reason="NO_CANDIDATE_PASSED_FINAL_EXECUTION_GATE")
            atomic_json(STATUS, status)
            print("PRODUCTION_ALERT " + json.dumps(status))
            return 0
    except (RuntimeError, ValueError, KeyError) as exc:
        status.update(status="DEGRADED", reason=str(exc))
        atomic_json(STATUS, status)
        print("PRODUCTION_ALERT " + json.dumps(status))
        return 0

    creds = credentials()
    if creds is None:
        status.update(status="DEGRADED", reason="SMTP_CONFIG_MISSING")
        atomic_json(STATUS, status)
        print("PRODUCTION_ALERT " + json.dumps(status))
        return 0

    row = selected["row"]
    subject = f"ACHÈTE — {row['market']} — Bitvavo"
    try:
        email_alert.send_email(creds[0], creds[1], creds[2], subject, body(selected))
    except smtplib.SMTPAuthenticationError:
        status.update(status="DEGRADED", reason="SMTP_AUTHENTICATION_ERROR", email="DELIVERY_PENDING")
        atomic_json(STATUS, status)
        print("PRODUCTION_ALERT " + json.dumps(status))
        return 0
    except (smtplib.SMTPException, OSError, TimeoutError) as exc:
        status.update(status="DEGRADED", reason=type(exc).__name__, email="DELIVERY_PENDING")
        atomic_json(STATUS, status)
        print("PRODUCTION_ALERT " + json.dumps(status))
        return 0

    sent_at = time.time()
    market = row["market"]
    previous = state["markets"].setdefault(market, {})
    previous.update(
        last_sent_ts=sent_at,
        sent_episode=previous.get("episode", 0),
        signal_score=row.get("signal_score"),
        signal_source=row.get("signal_source"),
        opportunity=row.get("opportunity_score"),
        entry=row.get("entry_score"),
        price=row.get("last"),
        status=row.get("action_status"),
    )
    state["last_global_sent_ts"] = sent_at
    state["updated_at_utc"] = utc(sent_at)
    atomic_json(STATE, state)
    status.update(status="OK", reason="DELIVERED", email="DELIVERY_COMPLETED", market=market)
    atomic_json(STATUS, status)
    print("PRODUCTION_ALERT " + json.dumps(status))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
