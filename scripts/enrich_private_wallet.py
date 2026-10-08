#!/usr/bin/env python3
"""Read-only, private-artifact-only execution evidence for every held EUR asset.

Runs AFTER the account's wallet summary has been produced. Never consults
public candidate/watchlists, never accesses private API credentials, and never
writes public execution_snapshot.json. Missing/stale evidence is explicit.
"""
from __future__ import annotations

import copy
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from execution_probe import near_depth, trade_flow, walk_book
from research.common import atomic_json, finite, timestamp, utc
from research.http import PublicClient

SUMMARY_PATH = ROOT / "wallet_private_summary.json"
BOOK_DEPTH = 100
TRADES_LIMIT = 100
MAX_POSITIONS_PER_CYCLE = 30
MAX_COLLECTION_SECONDS = 90
MAX_SNAPSHOT_AGE_SECONDS = 90
MAX_LAST_TRADE_AGE_SECONDS = 900
STAKES_EUR = (50.0, 100.0, 150.0)
MARKET_PATTERN = re.compile(r"[A-Z0-9]+-EUR\Z")


def _levels(book, side):
    result = []
    if not isinstance(book, dict) or not isinstance(book.get(side), list):
        raise ValueError("MISSING_BOOK_SIDE")
    for level in book[side][:BOOK_DEPTH]:
        if not isinstance(level, (tuple, list)) or len(level) < 2:
            raise ValueError("INVALID_BOOK_LEVEL")
        p, q = finite(level[0]), finite(level[1])
        if p is None or q is None or p <= 0 or q <= 0:
            raise ValueError("INVALID_BOOK_LEVEL")
        result.append((p, q))
    prices = [p for p, _ in result]
    if not result or prices != sorted(set(prices), reverse=(side == "bids")):
        raise ValueError("UNSORTED_OR_EMPTY_BOOK")
    return result


def _age(meta, now):
    retrieved = (meta or {}).get("retrieved_at_utc")
    if not retrieved:
        return None
    try:
        return round(now - timestamp(retrieved), 3)
    except (ValueError, TypeError):
        return None


def _liquidate_quantity(bids, quantity, best_bid):
    """Sell actual base units, unlike a hypothetical EUR notional purchase."""
    remaining = quantity
    proceeds = 0.0
    filled = 0.0
    last_price = None
    for price, available in bids:
        take = min(remaining, available)
        if take <= 0:
            break
        proceeds += price * take
        filled += take
        remaining -= take
        last_price = price
        if remaining <= 1e-12:
            break
    complete = remaining <= max(1e-12, quantity * 1e-9)
    average = proceeds / filled if filled else None
    return {
        "status": "ESTIMATE" if complete else "INSUFFICIENT_OBSERVED_DEPTH",
        "quantity_requested": quantity,
        "quantity_covered": round(filled, 12),
        "complete_in_depth": complete,
        "estimated_proceeds_eur": round(proceeds, 6) if complete else None,
        "average_sell_price_eur": round(average, 12) if complete else None,
        "worst_sell_price_eur": last_price,
        "impact_below_best_bid_pct": round((1 - average / best_bid) * 100, 5)
        if complete and best_bid else None,
        "scope": "ONE_PUBLIC_BOOK_SNAPSHOT_NOT_AN_EXECUTED_ORDER",
    }


def collect_market(client, market, quantity, now_fn=time.time, *, ticker=None, ticker_meta=None):
    row = {
        "market": market,
        "source": "Bitvavo public REST /book + /trades",
        "public_market_data_only": True,
        "read_only": True,
        "orders_submitted": False,
        "affects_buy_gate": False,
        "affects_position_actions": False,
        "book_depth_levels_requested": BOOK_DEPTH,
        "trades_limit_requested": TRADES_LIMIT,
        "status": "UNAVAILABLE",
        "reasons": [],
    }
    if not isinstance(market, str) or not MARKET_PATTERN.fullmatch(market):
        return {**row, "reasons": ["INVALID_MARKET"]}
    if finite(quantity) is None or quantity <= 0:
        return {**row, "reasons": ["INVALID_QUANTITY"]}

    ticker_ok = False
    if isinstance(ticker, dict):
        last = finite(ticker.get("last"))
        opened = finite(ticker.get("open"))
        quote_volume = finite(ticker.get("volumeQuote"))
        ticker_age = _age(ticker_meta, now_fn())
        ticker_ok = (
            last is not None and last > 0 and quote_volume is not None
            and ticker_age is not None and -2 <= ticker_age <= MAX_SNAPSHOT_AGE_SECONDS
        )
        row.update(
            ticker_last_price_eur=last,
            change_24h_pct=round((last / opened - 1) * 100, 5) if opened and opened > 0 and last else None,
            quote_volume_24h_eur=quote_volume,
            ticker_retrieved_at_utc=(ticker_meta or {}).get("retrieved_at_utc"),
            ticker_age_seconds_at_write=ticker_age,
        )
    if not ticker_ok:
        row["reasons"].append("TICKER_24H_UNAVAILABLE_OR_STALE")
    book_ok = False
    trades_ok = False
    book_path = "/" + market + "/book"
    book_params = {"depth": BOOK_DEPTH}
    try:
        book = client.get(book_path, book_params, cache=False)
        bids, asks = _levels(book, "bids"), _levels(book, "asks")
        bid, ask = bids[0][0], asks[0][0]
        if bid > ask:
            raise ValueError("CROSSED_BOOK")
        mid = (bid + ask) / 2
        captured = now_fn()
        meta = client.metadata(book_path, book_params)
        age = _age(meta, captured)
        row.update(
            book_retrieved_at_utc=meta.get("retrieved_at_utc"),
            book_age_seconds_at_write=age,
            best_bid=bid,
            best_ask=ask,
            mid=round(mid, 12),
            spread_pct=round((ask - bid) / mid * 100, 6),
            best_bid_size=bids[0][1],
            best_ask_size=asks[0][1],
            full_observed_bids=[[p, q] for p, q in bids],
            full_observed_asks=[[p, q] for p, q in asks],
            near_depth=near_depth(bids, asks, mid),
            market_buy_slippage=[],
            market_sell_slippage=[],
            held_quantity_sell_estimate=_liquidate_quantity(bids, quantity, bid),
        )
        for notional in STAKES_EUR:
            buy = walk_book(asks, notional, "buy")
            sell = walk_book(bids, notional, "sell")
            buy["slippage_vs_best_ask_pct"] = (
                round((buy["avg_price"] / ask - 1) * 100, 5)
                if buy["complete_in_depth"] and buy["avg_price"] else None
            )
            sell["slippage_vs_best_bid_pct"] = (
                round((1 - sell["avg_price"] / bid) * 100, 5)
                if sell["complete_in_depth"] and sell["avg_price"] else None
            )
            row["market_buy_slippage"].append(buy)
            row["market_sell_slippage"].append(sell)
        book_ok = age is not None and -2 <= age <= MAX_SNAPSHOT_AGE_SECONDS
        if not book_ok:
            row["reasons"].append("STALE_OR_UNTIMED_BOOK")
    except (RuntimeError, ValueError, TypeError, KeyError, IndexError):
        row["reasons"].append("BOOK_UNAVAILABLE_OR_INVALID")

    trade_path = "/" + market + "/trades"
    trade_params = {"limit": TRADES_LIMIT}
    try:
        trades = client.get(trade_path, trade_params, cache=False)
        if not isinstance(trades, list):
            raise ValueError("INVALID_TRADES_RESPONSE")
        meta = client.metadata(trade_path, trade_params)
        age = _age(meta, now_fn())
        flow = trade_flow(trades)
        timed = [
            t for t in trades
            if isinstance(t, dict) and isinstance(t.get("timestamp"), (int, float))
        ]
        latest = max(timed, key=lambda t: t["timestamp"]) if timed else None
        earliest = min(timed, key=lambda t: t["timestamp"]) if timed else None
        last_age = (now_fn() * 1000 - latest["timestamp"]) / 1000 if latest else None
        row.update(
            trades_retrieved_at_utc=meta.get("retrieved_at_utc"),
            trades_age_seconds_at_write=age,
            recent_public_trade_flow=flow,
            public_trade_sample_window_seconds=(
                round((latest["timestamp"] - earliest["timestamp"]) / 1000, 3)
                if latest and earliest else None
            ),
            latest_public_trade=(
                {
                    "price_eur": finite(latest.get("price")),
                    "quantity": finite(latest.get("amount")),
                    "side": latest.get("side"),
                    "timestamp_ms": latest["timestamp"],
                    "age_seconds_at_write": round(last_age, 3),
                }
                if latest else None
            ),
        )
        trades_ok = (
            age is not None and -2 <= age <= MAX_SNAPSHOT_AGE_SECONDS
            and last_age is not None and -2 <= last_age <= MAX_LAST_TRADE_AGE_SECONDS
            and bool(trades)
        )
        if not trades_ok:
            row["reasons"].append("STALE_OR_EMPTY_TRADES")
    except (RuntimeError, ValueError, TypeError, KeyError, IndexError):
        row["reasons"].append("TRADES_UNAVAILABLE_OR_INVALID")

    row["status"] = "OK" if book_ok and trades_ok and ticker_ok else "PARTIAL" if book_ok or trades_ok else "UNAVAILABLE"
    return row


def enrich(summary, client, now_fn=time.time, monotonic_fn=time.monotonic):
    if not isinstance(summary, dict) or not isinstance(summary.get("positions"), list):
        raise ValueError("MISSING_PRIVATE_WALLET_POSITIONS")
    out = copy.deepcopy(summary)
    positions = out["positions"]
    started = monotonic_fn()
    ticker_meta = {}
    ticker_by_market = {}
    try:
        ticker_rows = client.get("/ticker/24h", cache=False)
        if isinstance(ticker_rows, list):
            ticker_by_market = {
                item["market"]: item for item in ticker_rows
                if isinstance(item, dict) and isinstance(item.get("market"), str)
            }
            ticker_meta = client.metadata("/ticker/24h")
    except (RuntimeError, ValueError, TypeError):
        pass  # Best effort; per-market state will record missing volumes.
    attempted = 0
    seen = set()
    for position in positions:
        market = position.get("market") if isinstance(position, dict) else None
        if not isinstance(position, dict):
            raise ValueError("INVALID_PRIVATE_POSITION")
        if market in seen:
            position["execution_evidence"] = {"market": market, "status": "UNAVAILABLE",
                                              "reasons": ["DUPLICATE_POSITION"]}
            continue
        seen.add(market)
        if attempted >= MAX_POSITIONS_PER_CYCLE or monotonic_fn() - started >= MAX_COLLECTION_SECONDS:
            position["execution_evidence"] = {"market": market, "status": "NOT_OBSERVED",
                                              "reasons": ["COLLECTION_BUDGET_EXCEEDED"]}
            continue
        attempted += 1
        position["execution_evidence"] = collect_market(
            client, market, finite(position.get("quantity")), now_fn=now_fn,
            ticker=ticker_by_market.get(market), ticker_meta=ticker_meta,
        )
    counts = {s: 0 for s in ("OK", "PARTIAL", "UNAVAILABLE", "NOT_OBSERVED")}
    for pos in positions:
        status = pos["execution_evidence"]["status"]
        counts[status] = counts.get(status, 0) + 1
    out["execution_coverage"] = {
        "schema": "private_held_execution_v1",
        "generated_at_utc": utc(now_fn()),
        "scope": "ALL_PRIVATE_HELD_EUR_MARKETS_IN_WALLET",
        "market_count": len(positions),
        "attempted_count": attempted,
        "status_counts": counts,
        "max_age_seconds_at_write": MAX_SNAPSHOT_AGE_SECONDS,
        "source": "PUBLIC_BITVAVO_BOOK_AND_TRADES_PRIVATE_ARTIFACT_ONLY",
        "open_orders_visibility": "UNAVAILABLE_VIEW_ONLY",
        "requires_freshness_recheck_on_read": True,
        "research_only": True,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "orders_submitted": False,
    }
    return out


def main():
    if not SUMMARY_PATH.is_file():
        raise SystemExit("PRIVATE_WALLET_SUMMARY_MISSING")
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    client = PublicClient(timeout=6, retries=1, requests_per_second=8)
    result = enrich(summary, client)
    atomic_json(SUMMARY_PATH, result)
    # Log counts only: do not print symbols, wallet values or transaction details.
    print("PRIVATE_EXECUTION_COVERAGE " + json.dumps(result["execution_coverage"]["status_counts"], sort_keys=True))


if __name__ == "__main__":
    main()
