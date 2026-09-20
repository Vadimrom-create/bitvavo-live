#!/usr/bin/env python3
"""Fast production-only Bitvavo scanner.

This path intentionally excludes V3/V4, replay, Oracle/Railway, Pages and
research publication. It scans every active EUR market directly from Bitvavo,
uses canonical closed 5m/15m bars, detects confirmed acceleration and writes
only normalized production alert candidates plus a compact health status.
"""
from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, freshness, utc
from research.features import category, chase_risk, closed_candles, describe, wick_setup
from research.feedback_loop import acceleration_signal
from research.http import PublicClient
from research.production_gate import build_alert_payload

CANDIDATES = "production_alert_candidates.json"
STATUS = "production_scan_status.json"
INTERVALS = ("5m", "15m")


def _spread_pct(ticker: dict) -> float | None:
    bid, ask = finite(ticker.get("bid")), finite(ticker.get("ask"))
    if bid is None or ask is None or not 0 < bid <= ask:
        return None
    return (ask - bid) / ((ask + bid) / 2) * 100.0


def collect_market(client: PublicClient, meta: dict, ticker: dict, signal_ts: float):
    market = meta["market"]
    timeframes = {}
    errors = []
    for interval in INTERVALS:
        params = {"interval": interval, "limit": 100}
        try:
            raw = client.get("/" + market + "/candles", params)
            candles = closed_candles(raw, interval, signal_ts)
            timeframes[interval] = {
                "candles": candles,
                "features": describe(candles, interval),
                "retrieved_at_utc": client.metadata("/" + market + "/candles", params).get("retrieved_at_utc"),
            }
        except (RuntimeError, ValueError, KeyError) as exc:
            errors.append({"interval": interval, "reason": str(exc)})
            timeframes[interval] = {"candles": [], "features": {"valid": False, "reasons": ["FETCH_FAILED"]}}
    return market, {"meta": meta, "ticker": ticker, "timeframes": timeframes, "errors": errors}


def collect_universe(client: PublicClient, markets: list[dict], tickers: dict[str, dict], signal_ts: float):
    result = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [
            pool.submit(collect_market, client, meta, tickers.get(meta["market"], {}), signal_ts)
            for meta in markets
        ]
        for future in as_completed(futures):
            market, data = future.result()
            result[market] = data
    return result


def observation(data: dict, signal_ts: float, ticker_retrieved_at: str) -> dict:
    meta, ticker = data["meta"], data["ticker"]
    market = meta["market"]
    last, open24 = finite(ticker.get("last")), finite(ticker.get("open"))
    change24 = (last / open24 - 1) * 100 if last and open24 else None
    volume = finite(ticker.get("volumeQuote"), 0.0)
    row = {
        "market": market,
        "last": last,
        "ask": finite(ticker.get("ask")),
        "quote_volume_24h_eur": volume,
        "spread_pct": _spread_pct(ticker),
        "change_24h_pct": change24,
    }
    f5 = data["timeframes"]["5m"]["features"]
    f15 = data["timeframes"]["15m"]["features"]
    quality = freshness(now=time.time(), retrieved=ticker_retrieved_at)
    for interval, features in (("5m", f5), ("15m", f15)):
        if not features.get("valid"):
            quality["reasons"].append("INVALID_" + interval.upper())
        candles = data["timeframes"][interval]["candles"]
        if candles:
            q = freshness(
                now=signal_ts,
                retrieved=ticker_retrieved_at,
                candle_start_ms=candles[-1]["t"],
                interval=interval,
            )
            quality["reasons"].extend(q["reasons"])
        else:
            quality["reasons"].append("MISSING_" + interval.upper())
    quality["reasons"] = sorted(set(quality["reasons"]))
    quality["ok"] = not quality["reasons"]

    cls = category(row)
    obs = {
        "market": market,
        "price_eur": last,
        "change_24h_pct": change24,
        "quote_volume_24h_eur": volume,
        "baseline": None,
        "category": cls,
        "features": {"5m": f5, "15m": f15},
        "data_quality": quality,
        "exclusions": list(quality["reasons"]),
        "chase_risk": chase_risk(f15, change24),
        "wick_setup": wick_setup(f15, row),
        "recurrence": {"distinct_15m_periods": 0},
        "trade_plan": None,
        "decision": "SURVEILLE" if quality["ok"] else "DATA UNAVAILABLE",
        "timestamps": {"scan_at_utc": utc(signal_ts), "ticker_retrieved_at_utc": ticker_retrieved_at},
    }
    obs["acceleration"] = acceleration_signal(obs)
    return obs


def run() -> dict:
    started = time.time()
    client = PublicClient(timeout=12, retries=3, requests_per_second=12)
    client.get("/time", cache=False)
    if abs(client.server_offset) > 30:
        raise RuntimeError("EXCHANGE_CLOCK_SKEW")
    signal_ts = time.time()

    markets_raw = client.get("/markets")
    markets = sorted(
        [m for m in markets_raw if m.get("quote") == "EUR" and m.get("status") == "trading"],
        key=lambda m: m["market"],
    )
    ticker_rows = client.get("/ticker/24h")
    tickers = {r["market"]: r for r in ticker_rows if r.get("market")}
    ticker_retrieved_at = client.metadata("/ticker/24h").get("retrieved_at_utc")
    if not ticker_retrieved_at:
        raise RuntimeError("MISSING_TICKER_TIMESTAMP")

    universe = collect_universe(client, markets, tickers, signal_ts)
    observations = [observation(universe[m["market"]], signal_ts, ticker_retrieved_at) for m in markets]
    payload = build_alert_payload(observations, [], utc(signal_ts))
    atomic_json(CANDIDATES, payload)

    confirmed = [
        o for o in observations
        if (o.get("acceleration") or {}).get("state") == "CONFIRMED_ACCELERATION"
    ]
    status = {
        "schema": "production_direct_scan_v1",
        "checked_at_utc": utc(),
        "signal_at_utc": utc(signal_ts),
        "status": "OK",
        "source": "Bitvavo public REST direct",
        "oracle_required": False,
        "hosted_probe_required": False,
        "v4_required": False,
        "active_eur_markets": len(markets),
        "markets_collected": len(universe),
        "quality_ok": sum((o.get("data_quality") or {}).get("ok", False) for o in observations),
        "confirmed_accelerations": len(confirmed),
        "alert_candidates": len(payload["watch"]),
        "candidate_markets": [r["market"] for r in payload["watch"][:20]],
        "duration_seconds": round(time.time() - started, 3),
        "api_error_count": len(client.errors),
        "api_errors": client.errors[-20:],
    }
    atomic_json(STATUS, status)
    print("PRODUCTION_SCAN " + json.dumps(status, ensure_ascii=False))
    return status


def main() -> int:
    try:
        run()
        return 0
    except (RuntimeError, ValueError) as exc:
        status = {
            "schema": "production_direct_scan_v1",
            "checked_at_utc": utc(),
            "status": "DEGRADED",
            "reason": str(exc),
            "alert_candidates": 0,
            "oracle_required": False,
            "hosted_probe_required": False,
            "v4_required": False,
        }
        atomic_json(CANDIDATES, {
            "schema": "production_alert_candidates_v2",
            "generated_at_utc": utc(),
            "policy": "FULL_UNIVERSE_DIRECT_SCAN_WITH_FINAL_EXECUTION_GATE",
            "oracle_required": False,
            "hosted_probe_required": False,
            "watch": [],
        })
        atomic_json(STATUS, status)
        print("PRODUCTION_SCAN " + json.dumps(status, ensure_ascii=False))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
