#!/usr/bin/env python3
"""Fetch a fresh public Bitvavo execution quote snapshot.

This module deliberately uses the dedicated /ticker/price and /ticker/book
endpoints instead of treating the 24h ticker or a web page as a live quote.
No API key is required and no account or order endpoint is used.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.http import PublicClient

OUTPUT = Path("live_quotes.json")
MAX_CLOCK_SKEW_SECONDS = 30.0
MAX_SNAPSHOT_AGE_SECONDS = 30.0


def _utc(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).isoformat()


def _rows_by_market(payload):
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        raise ValueError("unexpected_ticker_payload")
    return {row.get("market"): row for row in payload if isinstance(row, dict) and row.get("market")}


def _positive(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return value if value > 0 else None


def build_snapshot(client: PublicClient | None = None, now_fn=time.time):
    client = client or PublicClient()

    # Exchange time is fetched immediately before the quotes. PublicClient
    # computes server_offset from request midpoint to detect local/future clock bugs.
    exchange = client.get("/time", cache=False)
    exchange_time_ms = int(exchange["time"])
    if abs(client.server_offset) > MAX_CLOCK_SKEW_SECONDS:
        raise RuntimeError("EXCHANGE_CLOCK_SKEW")

    requested_at = now_fn()
    price_payload = client.get("/ticker/price", cache=False)
    book_payload = client.get("/ticker/book", cache=False)
    received_at = now_fn()

    price_meta = client.metadata("/ticker/price")
    book_meta = client.metadata("/ticker/book")
    price_retrieved = price_meta.get("retrieved_at_utc")
    book_retrieved = book_meta.get("retrieved_at_utc")
    if not price_retrieved or not book_retrieved:
        raise RuntimeError("MISSING_RETRIEVAL_TIMESTAMP")

    prices = _rows_by_market(price_payload)
    books = _rows_by_market(book_payload)
    markets = {}
    for market in sorted(set(prices) & set(books)):
        last = _positive(prices[market].get("price"))
        bid = _positive(books[market].get("bid"))
        ask = _positive(books[market].get("ask"))
        valid = bool(last and bid and ask and bid <= ask)
        spread_pct = ((ask - bid) / ((ask + bid) / 2) * 100.0) if valid else None
        markets[market] = {
            "last": last,
            "best_bid": bid,
            "best_ask": ask,
            "spread_pct": round(spread_pct, 6) if spread_pct is not None else None,
            "valid": valid,
        }

    snapshot_age = max(0.0, now_fn() - received_at)
    future_timestamp = received_at > now_fn() + 2.0
    valid = (
        not future_timestamp
        and snapshot_age <= MAX_SNAPSHOT_AGE_SECONDS
        and abs(client.server_offset) <= MAX_CLOCK_SKEW_SECONDS
        and bool(markets)
    )
    reasons = []
    if future_timestamp:
        reasons.append("INVALID_FUTURE_TIMESTAMP")
    if snapshot_age > MAX_SNAPSHOT_AGE_SECONDS:
        reasons.append("STALE_LIVE_SNAPSHOT")
    if abs(client.server_offset) > MAX_CLOCK_SKEW_SECONDS:
        reasons.append("EXCHANGE_CLOCK_SKEW")
    if not markets:
        reasons.append("NO_MARKETS")

    return {
        "schema": "bitvavo_live_quotes_v1",
        "source": "Bitvavo public REST API /ticker/price + /ticker/book",
        "requested_at_utc": _utc(requested_at),
        "received_at_utc": _utc(received_at),
        "exchange_time_ms": exchange_time_ms,
        "exchange_clock_offset_seconds": round(client.server_offset, 6),
        "price_retrieved_at_utc": price_retrieved,
        "book_retrieved_at_utc": book_retrieved,
        "snapshot_age_seconds_at_write": round(snapshot_age, 6),
        "max_snapshot_age_seconds": MAX_SNAPSHOT_AGE_SECONDS,
        "valid": valid,
        "reasons": reasons,
        "market_count": len(markets),
        "markets": markets,
    }


def write_snapshot(path: Path = OUTPUT, client: PublicClient | None = None):
    snapshot = build_snapshot(client=client)
    path.write_text(json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return snapshot


def main():
    snapshot = write_snapshot()
    ethfi = snapshot["markets"].get("ETHFI-EUR")
    if ethfi:
        print(
            "ETHFI-EUR "
            f"last={ethfi['last']} bid={ethfi['best_bid']} ask={ethfi['best_ask']} "
            f"received={snapshot['received_at_utc']} valid={snapshot['valid']}"
        )
    else:
        print(f"ETHFI-EUR unavailable; snapshot valid={snapshot['valid']}")
    if not snapshot["valid"]:
        raise SystemExit("live quote snapshot rejected: " + ",".join(snapshot["reasons"]))


if __name__ == "__main__":
    main()
