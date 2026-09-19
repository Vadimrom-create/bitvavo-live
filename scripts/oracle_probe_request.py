#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
import time
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUEST = ROOT / "oracle_probe_request.json"
OUTPUT = ROOT / "oracle_requested_probe.json"
BASE = "http://144.24.206.128:8787"
BITVAVO_BASE = "https://api.bitvavo.com/v2"
MARKET_RE = re.compile(r"^[A-Z0-9]{2,20}-EUR$")
MAX_ATTEMPTS = 3
REQUEST_TIMEOUT_SECONDS = 8


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def get_json(path: str, params: dict[str, object] | None = None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "bitvavo-live-oracle-request/1.0"})
    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            if attempt < MAX_ATTEMPTS:
                time.sleep(attempt)
    raise last_error



def D(value):
    return Decimal(str(value))


def direct_get(path: str, params: dict[str, object] | None = None):
    url = BITVAVO_BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "bitvavo-live-oracle-fallback/1.0"})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def depth_eur(levels):
    return sum((D(price) * D(amount) for price, amount in levels), Decimal("0"))


def slippage(asks, stake_eur):
    remaining = D(stake_eur)
    spent = Decimal("0")
    base = Decimal("0")
    for price, amount in asks:
        price, amount = D(price), D(amount)
        available = price * amount
        take = min(remaining, available)
        if take > 0:
            spent += take
            base += take / price
            remaining -= take
        if remaining <= 0:
            break
    if base <= 0 or not asks:
        return {"stake_eur": float(stake_eur), "fillable": False, "avg_price": None,
                "slippage_pct": None}
    average = spent / base
    best = D(asks[0][0])
    return {
        "stake_eur": float(stake_eur),
        "fillable": remaining <= Decimal("0.000001"),
        "avg_price": float(average),
        "slippage_pct": float((average / best - 1) * 100),
        "unfilled_eur": float(max(remaining, Decimal("0"))),
    }


def flow(trades):
    buy = sell = Decimal("0")
    for trade in trades:
        notional = D(trade["price"]) * D(trade["amount"])
        if trade.get("side") == "buy":
            buy += notional
        elif trade.get("side") == "sell":
            sell += notional
    total = buy + sell
    return {
        "trade_count": len(trades),
        "buy_eur": float(buy),
        "sell_eur": float(sell),
        "buy_share_eur": float(buy / total) if total else None,
        "latest_trade_timestamp_ms": trades[0].get("timestamp") if trades else None,
        "oldest_trade_timestamp_ms": trades[-1].get("timestamp") if trades else None,
    }


def direct_bitvavo_quote(market: str, stake_eur: float):
    price = direct_get("/ticker/price", {"market": market})
    ticker = direct_get("/ticker/book", {"market": market})
    book = direct_get(f"/{market}/book", {"depth": 10})
    trades = direct_get(f"/{market}/trades", {"limit": 50})
    bids, asks = book.get("bids", [])[:10], book.get("asks", [])[:10]
    bid, ask = D(ticker["bid"]), D(ticker["ask"])
    midpoint = (bid + ask) / 2
    bid_depth, ask_depth = depth_eur(bids), depth_eur(asks)
    total_depth = bid_depth + ask_depth
    return {
        "ok": True,
        "timestamp_utc": now_iso(),
        "source": "bitvavo_public_direct_fallback",
        "oracle_fallback": True,
        "market": market,
        "last_trade_price": price.get("price"),
        "best_bid": ticker.get("bid"),
        "best_ask": ticker.get("ask"),
        "spread_pct": float((ask - bid) / midpoint * 100) if midpoint else None,
        "best_10_bids": bids,
        "best_10_asks": asks,
        "near_depth": {
            "bid_eur_top10": float(bid_depth),
            "ask_eur_top10": float(ask_depth),
            "imbalance": float((bid_depth - ask_depth) / total_depth) if total_depth else None,
        },
        "buy_slippage": slippage(asks, stake_eur),
        "recent_public_trade_flow": flow(trades),
        "exchange_book_timestamp": book.get("timestamp"),
    }


def main():
    req = json.loads(REQUEST.read_text(encoding="utf-8"))
    market = str(req.get("market", "")).upper()
    stake_eur = float(req.get("stake_eur", 75))
    if not MARKET_RE.fullmatch(market):
        raise SystemExit("invalid market")
    transport_ok = True
    error_type = None
    try:
        payload = get_json("/quote", {"market": market, "stake_eur": stake_eur})
    except Exception as exc:
        transport_ok = False
        error_type = type(exc).__name__
        try:
            payload = direct_bitvavo_quote(market, stake_eur)
        except Exception as fallback_exc:
            payload = {
                "ok": False,
                "error": "ORACLE_AND_BITVAVO_FALLBACK_UNAVAILABLE",
                "oracle_error_type": error_type,
                "fallback_error_type": type(fallback_exc).__name__,
            }
    out = {
        "schema": "oracle_requested_probe_v1",
        "requested_at_utc": now_iso(),
        "market": market,
        "stake_eur": stake_eur,
        "transport_ok": transport_ok,
        "attempts": MAX_ATTEMPTS,
        "probe": payload,
    }
    OUTPUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    if transport_ok:
        print(f"requested Oracle probe: {market} ok={payload.get('ok')}")
    elif payload.get("ok"):
        print(f"requested Oracle probe: {market} Oracle unavailable ({error_type}); direct Bitvavo fallback ok")
    else:
        print(f"requested Oracle probe: {market} Oracle unavailable ({error_type}); fallback unavailable")


if __name__ == "__main__":
    main()
