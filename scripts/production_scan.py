#!/usr/bin/env python3
"""Fast production-only Solaire scanner.

Direct Bitvavo public REST -> full EUR universe -> closed 5m/15m features ->
pure Solaire acceleration -> normalized candidates.

No V3/V4, Decision Layer, Oracle/Railway, chase heuristic, portfolio state,
research replay or alert cooldown participates in detection.
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, freshness, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_acceleration import acceleration_signal
from research.production_context import build_market_context, candidate_context
from research.production_gate import build_alert_payload
from research.production_news import collect_news_context

CANDIDATES = "production_alert_candidates.json"
STATUS = "production_scan_status.json"
UNIVERSE_SNAPSHOT = "production_universe_snapshot.json"
NEWS_CONTEXT = "production_news_context.json"
INTERVALS = ("5m", "15m")


def collect_market(client: PublicClient, meta: dict, signal_ts: float):
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
                "retrieved_at_utc": client.metadata(
                    "/" + market + "/candles", params
                ).get("retrieved_at_utc"),
            }
        except (RuntimeError, ValueError, KeyError) as exc:
            errors.append({"interval": interval, "reason": str(exc)})
            timeframes[interval] = {
                "candles": [],
                "features": {"valid": False, "reasons": ["FETCH_FAILED"]},
            }
    return market, {"meta": meta, "timeframes": timeframes, "errors": errors}


def collect_universe(client: PublicClient, markets: list[dict], signal_ts: float):
    result = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(collect_market, client, meta, signal_ts) for meta in markets]
        for future in as_completed(futures):
            market, data = future.result()
            result[market] = data
    return result


def observation(
    data: dict,
    ticker: dict,
    signal_ts: float,
    ticker_retrieved_at: str,
    news: dict | None = None,
) -> dict:
    market = data["meta"]["market"]
    last, open24 = finite(ticker.get("last")), finite(ticker.get("open"))
    change24 = (last / open24 - 1) * 100 if last and open24 else None
    volume = finite(ticker.get("volumeQuote"), 0.0)
    f5 = data["timeframes"]["5m"]["features"]
    f15 = data["timeframes"]["15m"]["features"]

    quality = freshness(now=time.time(), retrieved=ticker_retrieved_at)
    for interval, features in (("5m", f5), ("15m", f15)):
        if not features.get("valid"):
            quality["reasons"].append("INVALID_" + interval.upper())

        # Retrieval freshness and signal-time candle admissibility are distinct.
        # The request naturally completes after signal_ts; that must not be
        # misclassified as FUTURE_RETRIEVAL_TIMESTAMP. closed_candles() already
        # excludes every bar that was not closed at signal_ts.
        retrieved_at = data["timeframes"][interval].get("retrieved_at_utc")
        retrieval_q = freshness(now=time.time(), retrieved=retrieved_at)
        quality["reasons"].extend(retrieval_q["reasons"])

        candles = data["timeframes"][interval]["candles"]
        if candles:
            candle_q = freshness(
                now=signal_ts,
                retrieved=utc(signal_ts),
                candle_start_ms=candles[-1]["t"],
                interval=interval,
            )
            quality["reasons"].extend(candle_q["reasons"])
        else:
            quality["reasons"].append("MISSING_" + interval.upper())
    quality["reasons"] = sorted(set(quality["reasons"]))
    quality["ok"] = not quality["reasons"]

    obs = {
        "market": market,
        "price_eur": last,
        "change_24h_pct": change24,
        "quote_volume_24h_eur": volume,
        "features": {"5m": f5, "15m": f15},
        "news": news or {},
        "data_quality": quality,
        "timestamps": {
            "scan_at_utc": utc(signal_ts),
            "ticker_retrieved_at_utc": ticker_retrieved_at,
            "5m_retrieved_at_utc": data["timeframes"]["5m"].get("retrieved_at_utc"),
            "15m_retrieved_at_utc": data["timeframes"]["15m"].get("retrieved_at_utc"),
        },
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
        [
            m
            for m in markets_raw
            if m.get("quote") == "EUR" and m.get("status") == "trading"
        ],
        key=lambda m: m["market"],
    )
    news_context = collect_news_context(markets, signal_ts)
    atomic_json(NEWS_CONTEXT, news_context)

    ticker_rows = client.get("/ticker/24h")
    tickers = {r["market"]: r for r in ticker_rows if r.get("market")}
    ticker_retrieved_at = client.metadata("/ticker/24h").get("retrieved_at_utc")
    if not ticker_retrieved_at:
        raise RuntimeError("MISSING_TICKER_TIMESTAMP")

    universe = collect_universe(client, markets, signal_ts)
    observations = [
        observation(
            universe[m["market"]],
            tickers.get(m["market"], {}),
            signal_ts,
            ticker_retrieved_at,
            (news_context.get("markets") or {}).get(m["market"], {}),
        )
        for m in markets
    ]
    market_context = build_market_context(observations)
    # Neutral full-universe export for the V3 prospective shadow.  It reuses the
    # exact same Bitvavo observations as V2 and therefore adds no market-data
    # requests and cannot alter the frozen V2 decision path.
    universe_snapshot = {
        "schema": "solaire_production_universe_snapshot_v2_news",
        "generated_at_utc": utc(signal_ts),
        "source": "same_direct_bitvavo_scan+public_news",
        "affects_v2": True,
        "affects_detection": True,
        "affects_buy_gate": True,
        "news_policy": {"production": True, "watch_before_quant": True, "news_alone_can_buy": False, "weight_in_composite": 0.35},
        "market_context": market_context,
        "rows": [
            {
                "market": obs.get("market"),
                "price_eur": obs.get("price_eur"),
                "change_24h_pct": obs.get("change_24h_pct"),
                "quote_volume_24h_eur": obs.get("quote_volume_24h_eur"),
                "features": obs.get("features") or {},
                "acceleration": obs.get("acceleration") or {},
                "news": obs.get("news") or {},
                "data_quality": obs.get("data_quality") or {},
                "timestamps": obs.get("timestamps") or {},
                "context": (
                    candidate_context(obs, market_context)
                    if (obs.get("data_quality") or {}).get("ok", False)
                    else {}
                ),
            }
            for obs in observations
        ],
    }
    atomic_json(UNIVERSE_SNAPSHOT, universe_snapshot)
    payload = build_alert_payload(observations, utc(signal_ts), market_context)
    atomic_json(CANDIDATES, payload)

    confirmed = [
        o
        for o in observations
        if (o.get("acceleration") or {}).get("state") == "CONFIRMED_ACCELERATION"
    ]
    building = [
        o
        for o in observations
        if (o.get("acceleration") or {}).get("state") == "BUILDING_ACCELERATION"
    ]
    quality_failures = Counter(
        reason
        for o in observations
        for reason in (o.get("data_quality") or {}).get("reasons", [])
    )
    quality_ok_count = sum(
        (o.get("data_quality") or {}).get("ok", False) for o in observations
    )
    status = {
        "schema": "solaire_direct_scan_v2",
        "checked_at_utc": utc(),
        "signal_at_utc": utc(signal_ts),
        "status": "OK",
        "source": "Bitvavo public REST direct",
        "oracle_required": False,
        "hosted_probe_required": False,
        "v4_required": False,
        "decision_layer_required": False,
        "active_eur_markets": len(markets),
        "markets_collected": len(universe),
        "quality_ok": quality_ok_count,
        "quality_pct": round(100.0 * quality_ok_count / len(markets), 2) if markets else 0.0,
        "quality_failure_counts": dict(quality_failures.most_common()),
        "building_accelerations": len(building),
        "confirmed_accelerations": len(confirmed),
        "news_watch_count": len(payload.get("news_watch") or []),
        "news_watch_markets": [r["market"] for r in (payload.get("news_watch") or [])[:20]],
        "news_sources_ok": sum(1 for row in (news_context.get("sources") or []) if row.get("ok")),
        "news_sources_total": len(news_context.get("sources") or []),
        "alert_candidates": len(payload["watch"]),
        "candidate_markets": [r["market"] for r in payload["watch"][:20]],
        "universe_snapshot_rows": len(universe_snapshot["rows"]),
        "market_context_status": market_context.get("status"),
        "market_regime": market_context.get("regime"),
        "market_breadth_1h_pct": market_context.get("breadth_positive_1h_pct"),
        "market_breadth_4h_pct": market_context.get("breadth_positive_4h_pct"),
        "duration_seconds": round(time.time() - started, 3),
        "api_error_count": len(client.errors),
        "api_errors": client.errors[-20:],
    }
    atomic_json(STATUS, status)
    print("SOLAIRE_SCAN " + json.dumps(status, ensure_ascii=False))
    return status


def main() -> int:
    try:
        run()
        return 0
    except (RuntimeError, ValueError) as exc:
        status = {
            "schema": "solaire_direct_scan_v2",
            "checked_at_utc": utc(),
            "status": "DEGRADED",
            "reason": str(exc),
            "alert_candidates": 0,
            "oracle_required": False,
            "hosted_probe_required": False,
            "v4_required": False,
            "decision_layer_required": False,
        }
        atomic_json(
            UNIVERSE_SNAPSHOT,
            {
                "schema": "solaire_production_universe_snapshot_v2_news",
                "generated_at_utc": utc(),
                "source": "same_direct_bitvavo_scan+public_news",
                "affects_v2": True,
                "affects_detection": True,
                "affects_buy_gate": True,
                "market_context": {},
                "rows": [],
            },
        )
        atomic_json(
            NEWS_CONTEXT,
            {
                "schema": "solaire_production_news_v1",
                "generated_at_utc": utc(),
                "lookback_hours": 18,
                "news_weight": 0.35,
                "news_watch_min": 6.5,
                "sources": [],
                "items_with_known_recent_time": 0,
                "markets": {},
                "status": "UNAVAILABLE",
            },
        )
        atomic_json(
            CANDIDATES,
            {
                "schema": "production_alert_candidates_v5_news",
                "generated_at_utc": utc(),
                "policy": "SOLAIRE_NEWS_PLUS_DIRECT_ACCELERATION",
                "news_policy": {"production": True, "watch_before_quant": True, "news_alone_can_buy": False, "weight_in_composite": 0.35},
                "oracle_required": False,
                "hosted_probe_required": False,
                "v4_required": False,
                "decision_layer_required": False,
                "market_context": {
                    "schema": "solaire_market_context_v1",
                    "status": "UNAVAILABLE",
                    "affects_detection": False,
                    "affects_buy_gate": False,
                },
                "news_watch": [],
                "tracking": [],
                "watch": [],
            },
        )
        atomic_json(STATUS, status)
        print("SOLAIRE_SCAN " + json.dumps(status, ensure_ascii=False))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
