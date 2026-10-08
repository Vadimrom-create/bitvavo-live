#!/usr/bin/env python3
"""
Autonomous execution-quality probe for Bitvavo public market data.

Purpose:
- eliminate the need for manual Bitvavo Pro screenshots to validate PUBLIC market execution;
- capture a fresh order book, best bid/ask, recent public trades and estimated slippage;
- focus on the persistent decision watchlist plus current V4 BUY_READY/ENTRY_WINDOW names.

This script uses only PUBLIC Bitvavo endpoints. It does not read the user's wallet,
private open orders or trade history and requires no API key.
"""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://api.bitvavo.com/v2"
WATCHLIST = Path("decision_watchlist.json")
MARKET_ANALYSIS_WATCHLIST = Path("market_analysis_watchlist.json")
V4 = Path("v4_watch.json")
OUTPUT = Path("execution_snapshot.json")

MAX_TARGETS = 30
BOOK_DEPTH = 100
TRADES_LIMIT = 100
STAKE_SIZES_EUR = (150.0, 300.0, 600.0)
HEADERS = {"Accept": "application/json", "User-Agent": "bitvavo-execution-probe/1.0"}


def get_json(path: str, params: dict | None = None, retries: int = 4):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            time.sleep(0.7 + attempt * 1.2)
    raise RuntimeError(f"Bitvavo API failure {url}: {last_error}")


def f(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def add_target(targets: list[str], sources: dict[str, list[str]], market: str, source: str):
    if not market or not isinstance(market, str) or not market.endswith("-EUR"):
        return
    if market not in sources:
        targets.append(market)
        sources[market] = []
    if source not in sources[market]:
        sources[market].append(source)


def select_targets():
    targets: list[str] = []
    sources: dict[str, list[str]] = {}

    # Public research targets take priority; they are NOT a wallet inventory.
    public_research = load_json(MARKET_ANALYSIS_WATCHLIST, {})
    for market in public_research.get("markets", []) or []:
        add_target(targets, sources, market, "public_market_analysis:requested")
    d = load_json(WATCHLIST, {})
    for key in ("priority", "active_position_monitoring", "near_term_candidates"):
        for row in d.get(key, []) or []:
            if isinstance(row, dict):
                add_target(targets, sources, row.get("market"), f"decision_watchlist:{key}")
    for market in d.get("continuation_wait_for_pullback", []) or []:
        add_target(targets, sources, market, "decision_watchlist:continuation")

    v4 = load_json(V4, {})
    rows = v4.get("watch", []) or []
    # Prefer actionable V4 states, then highest opportunity/entry combinations.
    ranked = sorted(
        [r for r in rows if isinstance(r, dict)],
        key=lambda r: (
            2 if r.get("action_status") == "BUY_READY" else 1 if r.get("action_status") == "ENTRY_WINDOW" else 0,
            f(r.get("opportunity_score")) + 0.35 * f(r.get("entry_score")),
        ),
        reverse=True,
    )
    for row in ranked:
        if row.get("action_status") in ("BUY_READY", "ENTRY_WINDOW"):
            add_target(targets, sources, row.get("market"), f"v4:{row.get('action_status')}")
        if len(targets) >= MAX_TARGETS:
            break

    return targets[:MAX_TARGETS], sources


def walk_book(levels, notional_eur: float, side: str):
    remaining = notional_eur
    spent = 0.0
    base = 0.0
    worst = None
    for level in levels:
        if not isinstance(level, (list, tuple)) or len(level) < 2:
            continue
        price, amount = f(level[0]), f(level[1])
        if price <= 0 or amount <= 0:
            continue
        level_notional = price * amount
        take = min(remaining, level_notional)
        if take <= 0:
            break
        spent += take
        base += take / price
        remaining -= take
        worst = price
        if remaining <= 1e-9:
            break
    avg = spent / base if base > 0 else None
    complete = remaining <= 0.01
    return {
        "side": side,
        "target_notional_eur": notional_eur,
        "complete_in_depth": complete,
        "filled_notional_eur": round(spent, 4),
        "avg_price": round(avg, 12) if avg is not None else None,
        "worst_price": worst,
    }


def near_depth(bids, asks, mid):
    out = {}
    for pct in (0.25, 0.5, 1.0):
        bid_floor = mid * (1.0 - pct / 100.0)
        ask_ceil = mid * (1.0 + pct / 100.0)
        bid_eur = sum(f(p) * f(q) for p, q in bids if f(p) >= bid_floor)
        ask_eur = sum(f(p) * f(q) for p, q in asks if f(p) <= ask_ceil)
        out[f"within_{pct:g}pct"] = {
            "bid_notional_eur": round(bid_eur, 2),
            "ask_notional_eur": round(ask_eur, 2),
        }
    return out


def trade_flow(trades):
    buy = 0.0
    sell = 0.0
    total_base = 0.0
    total_notional = 0.0
    latest_ts = None
    for t in trades if isinstance(trades, list) else []:
        price = f(t.get("price"))
        amount = f(t.get("amount"))
        n = price * amount
        total_notional += n
        total_base += amount
        side = t.get("side")
        if side == "buy":
            buy += n
        elif side == "sell":
            sell += n
        ts = t.get("timestamp")
        if isinstance(ts, (int, float)):
            latest_ts = max(latest_ts or ts, ts)
    denom = buy + sell
    return {
        "sample_trades": len(trades) if isinstance(trades, list) else 0,
        "buy_taker_notional_eur": round(buy, 2),
        "sell_taker_notional_eur": round(sell, 2),
        "buy_taker_share": round(buy / denom, 4) if denom else None,
        "vwap": round(total_notional / total_base, 12) if total_base else None,
        "latest_trade_timestamp_ms": latest_ts,
    }


def main():
    generated = datetime.now(timezone.utc)
    targets, sources = select_targets()

    price_raw = get_json("/ticker/price")
    book_ticker_raw = get_json("/ticker/book")
    prices = {r.get("market"): f(r.get("price")) for r in price_raw if isinstance(r, dict)}
    tickbooks = {r.get("market"): r for r in book_ticker_raw if isinstance(r, dict)}

    markets = []
    for market in targets:
        row = {"market": market, "sources": sources.get(market, [])}
        try:
            book = get_json(f"/{market}/book", {"depth": BOOK_DEPTH})
            trades = get_json(f"/{market}/trades", {"limit": TRADES_LIMIT})
            bids = book.get("bids", []) or []
            asks = book.get("asks", []) or []
            if not bids or not asks:
                raise ValueError("MISSING_BOOK_SIDE")
            bid_prices = [f(level[0]) for level in bids]
            ask_prices = [f(level[0]) for level in asks]
            if (any(p <= 0 for p in bid_prices + ask_prices)
                or bid_prices != sorted(set(bid_prices), reverse=True)
                or ask_prices != sorted(set(ask_prices))
                or f(bids[0][0]) > f(asks[0][0])):
                raise ValueError("INVALID_OR_CROSSED_BOOK")
            book_observed_at_utc = datetime.now(timezone.utc).isoformat()
            tb = tickbooks.get(market, {})
            last = prices.get(market) or 0.0
            # One order-book snapshot for price, spread and depth:
            # ticker/book quotes can be asynchronous to the depth levels.
            best_bid = f(bids[0][0])
            best_ask = f(asks[0][0])
            mid = (best_bid + best_ask) / 2.0 if best_bid and best_ask else last
            spread_pct = ((best_ask - best_bid) / mid * 100.0) if mid else None
            timed_trades = [t for t in trades if isinstance(t, dict)
                            and isinstance(t.get("timestamp"), (int, float))] if isinstance(trades, list) else []
            latest = max(timed_trades, key=lambda t: t["timestamp"], default=None)
            trade_observed_at_utc = datetime.now(timezone.utc).isoformat()
            latest_age_seconds = (
                datetime.now(timezone.utc).timestamp() - latest["timestamp"] / 1000
                if latest is not None else None
            )

            buy_slippage = []
            sell_slippage = []
            for stake in STAKE_SIZES_EUR:
                b = walk_book(asks, stake, "buy")
                s = walk_book(bids, stake, "sell")
                if b.get("avg_price") and best_ask:
                    b["slippage_vs_best_ask_pct"] = round((b["avg_price"] / best_ask - 1.0) * 100.0, 5)
                if s.get("avg_price") and best_bid:
                    s["slippage_vs_best_bid_pct"] = round((1.0 - s["avg_price"] / best_bid) * 100.0, 5)
                buy_slippage.append(b)
                sell_slippage.append(s)

            row.update({
                "last_trade_price": last,
                "best_bid": best_bid,
                "best_bid_size": f(bids[0][1]),
                "best_ask": best_ask,
                "best_ask_size": f(asks[0][1]),
                "ticker_book_bid": f(tb.get("bid")),
                "ticker_book_ask": f(tb.get("ask")),
                "book_observed_at_utc": book_observed_at_utc,
                "trades_observed_at_utc": trade_observed_at_utc,
                "latest_public_trade": (
                    {"price_eur": f(latest.get("price")), "quantity": f(latest.get("amount")),
                     "side": latest.get("side"), "timestamp_ms": latest["timestamp"]}
                    if latest is not None else None
                ),
                "latest_trade_age_seconds_at_write": (
                    round(latest_age_seconds, 3) if latest_age_seconds is not None else None
                ),
                "public_trade_sample_span_seconds": (
                    round((max(t["timestamp"] for t in timed_trades) -
                           min(t["timestamp"] for t in timed_trades)) / 1000, 3)
                    if timed_trades else None
                ),
                "mid": round(mid, 12) if mid else None,
                "spread_pct": round(spread_pct, 6) if spread_pct is not None else None,
                "book_depth_levels_requested": BOOK_DEPTH,
                "best_10_bids": bids[:10],
                "best_10_asks": asks[:10],
                "near_depth": near_depth(bids, asks, mid) if mid else {},
                "buy_slippage": buy_slippage,
                "sell_slippage": sell_slippage,
                "recent_public_trade_flow": trade_flow(trades),
                "status": "OK",
            })
        except Exception as exc:
            row.update({"status": "ERROR", "error": str(exc)})
        markets.append(row)

    out = {
        "generated_at_utc": generated.isoformat(),
        "source": "Bitvavo public REST API",
        "public_only": True,
        "api_key_used": False,
        "purpose": "Timestamped public order-book and trade evidence for pinned market research and prospective candidates; no user holdings inferred.",
        "limitations": "Does not expose the user's wallet, private open orders, personal fills or private trade history.",
        "target_count": len(markets),
        "markets": markets,
    }
    OUTPUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {OUTPUT} for {len(markets)} markets at {generated.isoformat()}")


if __name__ == "__main__":
    main()
