#!/usr/bin/env python3
"""Filtre strict anti-spam pour les alertes e-mail V3.

Le détecteur V3 peut conserver plusieurs BUY_READY pour l'audit et le classement.
Ce wrapper n'envoie un e-mail que pour un setup de très bonne qualité, au maximum
un candidat par message, avec un cooldown global de 30 minutes.
"""
from __future__ import annotations

import time
from typing import Any

import email_alert as base

GLOBAL_COOLDOWN_SECONDS = 30 * 60
MIN_FINAL_SCORE = 9.50
MIN_CONFIRMATIONS = 2
MIN_VOL24_EUR = 250_000
MAX_SPREAD_PCT = 0.12
MIN_BID_SHARE = 0.45
MIN_CHANGE24_PCT = -5.0
MAX_CHANGE24_PCT = 10.0
MIN_SINCE_FIRST_PCT = -2.0
MAX_SINCE_FIRST_PCT = 3.0
MAX_PRICE_15M_PCT = 2.5

FORBIDDEN_FLAGS = {
    "LOW_LIQUIDITY",
    "SPREAD",
    "SELLER_HEAVY_BOOK",
    "BTC_RISK",
    "HEI_REJECTION",
    "TOO_LATE_24H",
    "TOO_LATE_FROM_SIGNAL",
    "EXTENDED_24H",
}


def n(x: Any, default: float | None = None) -> float | None:
    try:
        return float(x)
    except Exception:
        return default


def strict_select(payload: dict, state: dict, now_ts: float) -> list[dict]:
    # Cooldown global : une nouvelle crypto ne doit pas créer un nouveau mail
    # cinq minutes après le précédent.
    sent_times = []
    for item in (state.get("markets") or {}).values():
        ts = n((item or {}).get("last_sent_ts"))
        if ts is not None:
            sent_times.append(ts)
    if sent_times and now_ts - max(sent_times) < GLOBAL_COOLDOWN_SECONDS:
        return []

    enriched = payload.get("enriched") or {}
    accepted: list[dict] = []

    for row in payload.get("watch") or []:
        if not isinstance(row, dict) or not row.get("buy_ready"):
            continue

        market = str(row.get("market") or "")
        if not market:
            continue

        score = n(row.get("final_score", row.get("early_score")), 0.0) or 0.0
        confirms = int(n(row.get("confirm_count"), 0) or 0)
        volume = n(row.get("quote_volume_24h_eur"), 0.0) or 0.0
        spread = n(row.get("spread_pct"), 99.0) or 99.0
        ch24 = n(row.get("change_24h_pct"), 0.0) or 0.0
        trajectory = row.get("trajectory") or {}
        since_first = n(trajectory.get("price_since_first_early_pct"), 0.0) or 0.0
        dprice15 = n(trajectory.get("dprice_15m_pct"), 0.0) or 0.0
        flags = set(row.get("risk_flags") or [])

        e = enriched.get(market, {}) or {}
        book = e.get("book") or {}
        bid_share = n(book.get("bid_share"))
        s15 = e.get("15m") or {}
        s1h = e.get("1h") or {}
        s4h = e.get("4h") or {}
        ch15_4 = n(s15.get("ch4"), -99.0) or -99.0
        ch1h_4 = n(s1h.get("ch4"), -99.0) or -99.0
        ch4h_4 = n(s4h.get("ch4"), -99.0) or -99.0

        if score < MIN_FINAL_SCORE:
            continue
        if confirms < MIN_CONFIRMATIONS:
            continue
        if volume < MIN_VOL24_EUR:
            continue
        if spread > MAX_SPREAD_PCT:
            continue
        if bid_share is None or bid_share < MIN_BID_SHARE:
            continue
        if not MIN_CHANGE24_PCT <= ch24 <= MAX_CHANGE24_PCT:
            continue
        if not MIN_SINCE_FIRST_PCT <= since_first <= MAX_SINCE_FIRST_PCT:
            continue
        if dprice15 > MAX_PRICE_15M_PCT:
            continue
        if flags & FORBIDDEN_FLAGS:
            continue
        if ch15_4 < 0.25 or ch1h_4 < 0.0 or ch4h_4 < -1.0:
            continue

        # Conserver le cooldown par marché existant du transport.
        previous = (state.get("markets") or {}).get(market, {}) or {}
        last_sent = n(previous.get("last_sent_ts"))
        if last_sent is not None and now_ts - last_sent < base.COOLDOWN_SECONDS:
            continue

        accepted.append(row)

    # Les scores V3 saturent encore parfois à 10. On départage alors par
    # qualité carnet/liquidité/spread plutôt que par score seul.
    def quality_key(row: dict):
        market = str(row.get("market") or "")
        e = enriched.get(market, {}) or {}
        bid = n((e.get("book") or {}).get("bid_share"), 0.0) or 0.0
        vol = n(row.get("quote_volume_24h_eur"), 0.0) or 0.0
        spr = n(row.get("spread_pct"), 99.0) or 99.0
        score = n(row.get("final_score", row.get("early_score")), 0.0) or 0.0
        return (score, bid, min(vol, 5_000_000), -spr)

    accepted.sort(key=quality_key, reverse=True)
    return accepted[:1]


base.select_buy_ready = strict_select

if __name__ == "__main__":
    raise SystemExit(base.main())
