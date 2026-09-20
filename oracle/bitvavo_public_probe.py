#!/usr/bin/env python3
"""Bounded, read-only Bitvavo public probe for a generic hosted service."""
from __future__ import annotations

import json
import os
import re
import threading
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import Decimal
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE = "https://api.bitvavo.com/v2"
PORT = int(os.environ.get("PORT", "8787"))
MARKET_RE = re.compile(r"^[A-Z0-9]{2,20}-EUR$")
MAX_CONCURRENT_QUOTES = max(1, min(8, int(os.environ.get("MAX_CONCURRENT_QUOTES", "4"))))
UPSTREAM_TIMEOUT_SECONDS = max(1, min(10, int(os.environ.get("UPSTREAM_TIMEOUT_SECONDS", "4"))))
WATCHDOG_INTERVAL_SECONDS = max(5, int(os.environ.get("WATCHDOG_INTERVAL_SECONDS", "10")))
WATCHDOG_FAILURES_BEFORE_EXIT = max(2, int(os.environ.get("WATCHDOG_FAILURES_BEFORE_EXIT", "3")))
QUOTE_SLOTS = threading.BoundedSemaphore(MAX_CONCURRENT_QUOTES)
COUNTER_LOCK = threading.Lock()
ACTIVE_QUOTES = 0
STARTED = time.time()


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def D(value):
    return Decimal(str(value))


def get(path, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "bitvavo-public-probe/2.0"})
    started = time.monotonic()
    with urllib.request.urlopen(req, timeout=UPSTREAM_TIMEOUT_SECONDS) as response:
        data = json.loads(response.read().decode())
    return data, round((time.monotonic() - started) * 1000, 1)


def depth_eur(levels):
    return sum((D(price) * D(amount) for price, amount in levels), Decimal("0"))


def slippage(asks, stake):
    remaining = D(stake)
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
    if base <= 0:
        return {
            "stake_eur": float(stake),
            "fillable": False,
            "avg_price": None,
            "slippage_pct": None,
        }
    average = spent / base
    best = D(asks[0][0])
    return {
        "stake_eur": float(stake),
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


def quote(market, stake):
    wall_started = time.monotonic()
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="bitvavo-upstream") as pool:
        price_future = pool.submit(get, "/ticker/price", {"market": market})
        ticker_future = pool.submit(get, "/ticker/book", {"market": market})
        book_future = pool.submit(get, f"/{market}/book", {"depth": 10})
        trades_future = pool.submit(get, f"/{market}/trades", {"limit": 50})

        price, t_price = price_future.result()
        ticker, t_ticker = ticker_future.result()
        book, t_book = book_future.result()
        trades, t_trades = trades_future.result()

    bids = book.get("bids", [])[:10]
    asks = book.get("asks", [])[:10]
    bid = D(ticker["bid"])
    ask = D(ticker["ask"])
    midpoint = (bid + ask) / 2
    spread = ((ask - bid) / midpoint * 100) if midpoint else None
    bid_depth = depth_eur(bids)
    ask_depth = depth_eur(asks)
    total_depth = bid_depth + ask_depth
    wall_ms = round((time.monotonic() - wall_started) * 1000, 1)

    return {
        "ok": True,
        "timestamp_utc": now_iso(),
        "source": "bitvavo_public",
        "market": market,
        "last_trade_price": price.get("price"),
        "best_bid": ticker.get("bid"),
        "best_ask": ticker.get("ask"),
        "spread_pct": float(spread) if spread is not None else None,
        "best_10_bids": bids,
        "best_10_asks": asks,
        "near_depth": {
            "bid_eur_top10": float(bid_depth),
            "ask_eur_top10": float(ask_depth),
            "imbalance": float((bid_depth - ask_depth) / total_depth) if total_depth else None,
        },
        "buy_slippage": slippage(asks, stake),
        "recent_public_trade_flow": flow(trades),
        "exchange_book_timestamp": book.get("timestamp"),
        "latency_ms": {
            "price": t_price,
            "ticker_book": t_ticker,
            "order_book": t_book,
            "trades": t_trades,
            "wall": wall_ms,
        },
    }


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, payload):
        raw = json.dumps(payload, separators=(",", ":")).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(raw)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        global ACTIVE_QUOTES

        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/health":
            with COUNTER_LOCK:
                active = ACTIVE_QUOTES
            load1 = None
            try:
                load1 = round(os.getloadavg()[0], 3)
            except Exception:
                pass
            return self.send_json(
                200,
                {
                    "ok": True,
                    "service": "bitvavo-public-probe",
                    "version": 2,
                    "timestamp_utc": now_iso(),
                    "uptime_seconds": round(time.time() - STARTED, 1),
                    "active_quotes": active,
                    "max_concurrent_quotes": MAX_CONCURRENT_QUOTES,
                    "loadavg_1m": load1,
                },
            )

        if parsed.path != "/quote":
            return self.send_json(404, {"ok": False, "error": "not_found"})

        query = urllib.parse.parse_qs(parsed.query)
        market = query.get("market", [""])[0].upper()
        if not MARKET_RE.fullmatch(market):
            return self.send_json(400, {"ok": False, "error": "invalid_market"})

        if not QUOTE_SLOTS.acquire(timeout=0.25):
            return self.send_json(
                503,
                {
                    "ok": False,
                    "timestamp_utc": now_iso(),
                    "error": "busy",
                    "retry_after_seconds": 1,
                },
            )

        with COUNTER_LOCK:
            ACTIVE_QUOTES += 1
        try:
            stake = D(query.get("stake_eur", ["75"])[0])
            if stake < 1 or stake > 10000:
                raise ValueError("stake_eur_out_of_range")
            return self.send_json(200, quote(market, stake))
        except Exception as exc:
            return self.send_json(
                502,
                {
                    "ok": False,
                    "timestamp_utc": now_iso(),
                    "error": type(exc).__name__,
                    "detail": str(exc)[:300],
                },
            )
        finally:
            with COUNTER_LOCK:
                ACTIVE_QUOTES -= 1
            QUOTE_SLOTS.release()

    def log_message(self, fmt, *args):
        pass


class ProbeServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False
    request_queue_size = 64


def self_watchdog(port: int) -> None:
    """Exit non-zero if the local HTTP server repeatedly stops answering.

    A managed host can then restart the process automatically. This catches
    the failure mode where the process still exists but its HTTP service is wedged.
    """
    failures = 0
    url = f"http://127.0.0.1:{port}/health"
    while True:
        time.sleep(WATCHDOG_INTERVAL_SECONDS)
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                payload = json.loads(response.read().decode())
            if response.status != 200 or payload.get("ok") is not True:
                raise RuntimeError("local healthcheck unhealthy")
            failures = 0
        except Exception:
            failures += 1
            if failures >= WATCHDOG_FAILURES_BEFORE_EXIT:
                os._exit(70)


if __name__ == "__main__":
    server = ProbeServer(("0.0.0.0", PORT), Handler)
    threading.Thread(
        target=self_watchdog,
        args=(server.server_address[1],),
        name="live-probe-watchdog",
        daemon=True,
    ).start()
    server.serve_forever()
