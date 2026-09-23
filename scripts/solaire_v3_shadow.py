#!/usr/bin/env python3
"""Solaire V3 prospective shadow.

This process runs beside Solaire V2.  It never sends mail and never submits an
order.  It tests independent hypotheses prospectively:
- context/news/narratives can focus attention before V2 confirmation,
- opportunities may remain valuable beyond 24h,
- capital should be compared with cash and alternative opportunities,
- global venues may discover a move before Bitvavo,
- entry timing should be measured separately from detection,
- an opportunity thesis can persist after short acceleration disappears.

All external feeds are non-blocking.  Missing feeds remain missing evidence;
they are never silently imputed.
"""
from __future__ import annotations

import concurrent.futures
import email.utils
import json
import math
import re
import statistics
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan
from research.solaire_v3 import (
    FROZEN_V2_COMMIT,
    MAX_SHADOW_POSITIONS,
    REFERENCE_CAPITAL_EUR,
    REFERENCE_STAKE_EUR,
    TOKEN_ALIASES,
    advance_persistent_thesis,
    base_symbol,
    build_narrative_rotations,
    classify_horizon,
    early_quant_evidence,
    narratives_for_market,
    score_opportunity,
    walk_asks,
)

UNIVERSE = "production_universe_snapshot.json"
V2_PAYLOAD = "production_alert_candidates.json"
STATE = "solaire_v3_state.json"
JOURNAL = "solaire_v3_journal.json"
STATUS = "solaire_v3_status.json"
CANDIDATES = "solaire_v3_candidates.json"
ROTATION = "solaire_v3_rotation_state.json"
V2_BENCHMARK = "solaire_v2_frozen_benchmark_journal.json"

MAX_CONTEXT_AGE = 36 * 3600
WATCH_EXPIRY = 24 * 3600
MAX_EXTERNAL_MARKETS = 16
MAX_EXECUTION_MARKETS = 14
MAX_THESIS_PROFILE_MARKETS = 20
MIN_QUOTE_VOLUME_EUR = 75_000.0
MAX_SPREAD_PCT = 0.50
MAX_DEPTH_SLIPPAGE_PCT = 0.50
MAX_STOP_DISTANCE_PCT = 10.0
HTTP_TIMEOUT = 5

TIMING_PERSIST_MIN_SECONDS = 30 * 60
TIMING_PERSIST_MIN_DRIFT_PCT = -2.0
TIMING_PERSIST_MAX_DRIFT_PCT = 3.0
TIMING_PULLBACK_MIN_PCT = -2.0
TIMING_RECLAIM_MIN_PCT = 1.0
TIMING_RECLAIM_MAX_DRIFT_PCT = 3.0

NEWS_FEEDS = (
    ("coindesk", "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("cointelegraph", "https://cointelegraph.com/rss"),
    ("decrypt", "https://decrypt.co/feed"),
)

GENERIC_SYMBOLS = {
    "G", "S", "ONE", "NEAR", "FLUX", "GRASS", "KERNEL", "ICON", "MET", "DATA",
    "MOVE", "SAFE", "MASK", "MAGIC", "SAGA",
}


def _json_url(url: str, timeout: int = HTTP_TIMEOUT) -> Any:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "solaire-v3-shadow/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read())


def _text_url(url: str, timeout: int = HTTP_TIMEOUT) -> str:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/rss+xml,text/xml,*/*", "User-Agent": "solaire-v3-shadow/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def _parse_ts(value: Any) -> float | None:
    if value is None:
        return None
    try:
        if isinstance(value, (int, float)):
            result = float(value)
            return result if result > 0 else None
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        try:
            return email.utils.parsedate_to_datetime(str(value)).timestamp()
        except Exception:
            return None


def _median(xs: list[float]) -> float | None:
    vals = [x for x in xs if x is not None and math.isfinite(x)]
    return statistics.median(vals) if vals else None



def _closed_return(candles: list[dict[str, Any]], bars: int) -> float | None:
    if len(candles) <= bars:
        return None
    start = finite(candles[-bars - 1].get("c"))
    end = finite(candles[-1].get("c"))
    if start is None or end is None or start <= 0:
        return None
    return (end / start - 1.0) * 100.0


def _trend_returns(client: PublicClient, market: str, now: float) -> dict[str, float | None]:
    raw = client.get("/" + market + "/candles", {"interval": "4h", "limit": 50}, cache=False)
    candles = closed_candles(raw, "4h", now)
    return {
        "return_24h_pct": _closed_return(candles, 6),
        "return_72h_pct": _closed_return(candles, 18),
        "return_7d_pct": _closed_return(candles, 42),
    }


def fetch_long_trend_profiles(
    client: PublicClient,
    markets: list[str],
    now: float,
) -> tuple[dict[str, dict[str, Any]], list[dict[str, str]]]:
    """Medium/long-horizon trend evidence used only by the thesis lab."""
    profiles: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, str]] = []
    try:
        btc = _trend_returns(client, "BTC-EUR", now)
    except Exception as exc:
        btc = {}
        errors.append({"source": "long_trend", "market": "BTC-EUR", "reason": type(exc).__name__})

    for market in markets[:MAX_THESIS_PROFILE_MARKETS]:
        try:
            own = _trend_returns(client, market, now)
            rel72 = None
            rel7d = None
            if finite(own.get("return_72h_pct")) is not None and finite(btc.get("return_72h_pct")) is not None:
                rel72 = finite(own.get("return_72h_pct")) - finite(btc.get("return_72h_pct"))
            if finite(own.get("return_7d_pct")) is not None and finite(btc.get("return_7d_pct")) is not None:
                rel7d = finite(own.get("return_7d_pct")) - finite(btc.get("return_7d_pct"))
            flags = {
                "positive_72h": finite(own.get("return_72h_pct"), -999.0) > 0,
                "positive_7d": finite(own.get("return_7d_pct"), -999.0) > 0,
                "relative_72h_vs_btc": rel72 is not None and rel72 > 0,
                "relative_7d_vs_btc": rel7d is not None and rel7d > 0,
            }
            evidence_count = sum(flags.values())
            profiles[market] = {
                **own,
                "relative_72h_vs_btc_pp": None if rel72 is None else round(rel72, 4),
                "relative_7d_vs_btc_pp": None if rel7d is None else round(rel7d, 4),
                "flags": flags,
                "evidence_count": evidence_count,
                "support": evidence_count >= 2,
                "method": "closed_4h_candles_point_in_time",
            }
        except Exception as exc:
            errors.append({"source": "long_trend", "market": market, "reason": type(exc).__name__})
    return profiles, errors


def _news_asset_symbols(text: str) -> list[str]:
    low = " " + re.sub(r"\s+", " ", text.lower()) + " "
    hits = []
    for symbol, aliases in TOKEN_ALIASES.items():
        matched = False
        for alias in aliases:
            a = alias.lower().strip()
            if len(a) >= 4 and re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", low):
                matched = True
                break
        if not matched and symbol not in GENERIC_SYMBOLS:
            if ("$" + symbol.lower()) in low:
                matched = True
            elif len(symbol) >= 4 and re.search(r"(?<![a-z0-9])" + re.escape(symbol.lower()) + r"(?![a-z0-9])", low):
                matched = True
        if matched:
            hits.append(symbol)
    return sorted(set(hits))


def fetch_news(now: float) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    items: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    try:
        data = _json_url("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
        for row in (data or {}).get("Data", []) or []:
            published = _parse_ts(row.get("published_on"))
            if published is None or now - published > MAX_CONTEXT_AGE or published - now > 300:
                continue
            title = str(row.get("title") or "")
            body = str(row.get("body") or "")
            symbols = _news_asset_symbols(title + " " + body)
            if symbols:
                items.append({
                    "source": str(row.get("source") or "cryptocompare"),
                    "published_ts": published,
                    "published_at_utc": utc(published),
                    "title": title[:300],
                    "url": row.get("url"),
                    "symbols": symbols,
                })
    except Exception as exc:
        errors.append({"source": "cryptocompare", "reason": type(exc).__name__})

    for source, url in NEWS_FEEDS:
        try:
            root = ET.fromstring(_text_url(url))
            for node in root.findall(".//item"):
                title = (node.findtext("title") or "").strip()
                desc = (node.findtext("description") or "").strip()
                link = (node.findtext("link") or "").strip()
                published = _parse_ts(node.findtext("pubDate"))
                if published is None or now - published > MAX_CONTEXT_AGE or published - now > 300:
                    continue
                symbols = _news_asset_symbols(title + " " + re.sub("<[^>]+>", " ", desc))
                if symbols:
                    items.append({
                        "source": source,
                        "published_ts": published,
                        "published_at_utc": utc(published),
                        "title": title[:300],
                        "url": link,
                        "symbols": symbols,
                    })
        except Exception as exc:
            errors.append({"source": source, "reason": type(exc).__name__})

    dedup = {}
    for item in items:
        key = (item.get("source"), item.get("title"), item.get("published_at_utc"))
        dedup[key] = item
    return sorted(dedup.values(), key=lambda x: x["published_ts"], reverse=True), errors


def news_for_symbol(symbol: str, news: list[dict[str, Any]], now: float) -> tuple[list[dict[str, Any]], float]:
    hits = [x for x in news if symbol in (x.get("symbols") or [])]
    if not hits:
        return [], 0.0
    sources = {x.get("source") for x in hits}
    freshest_hours = min(max(0.0, (now - x["published_ts"]) / 3600) for x in hits)
    recency = max(0.0, 4.0 - freshest_hours / 6.0)
    score = min(10.0, recency + min(3.0, len(hits) * 0.8) + min(3.0, len(sources) * 0.8))
    return hits[:8], round(score, 3)


def _return_from_points(points: list[tuple[float, float]], minutes: int) -> float | None:
    pts = sorted((t, p) for t, p in points if t and p and p > 0)
    if len(pts) < 2:
        return None
    last_t, last_p = pts[-1]
    target = last_t - minutes * 60
    prior = min(pts[:-1], key=lambda x: abs(x[0] - target), default=None)
    if prior is None or abs(prior[0] - target) > 10 * 60:
        return None
    return (last_p / prior[1] - 1.0) * 100.0


def _binance(symbol: str) -> dict[str, Any]:
    url = "https://api.binance.com/api/v3/klines?" + urllib.parse.urlencode(
        {"symbol": symbol + "USDT", "interval": "5m", "limit": 14}
    )
    data = _json_url(url)
    pts = [(float(x[0]) / 1000.0, float(x[4])) for x in data]
    return {"venue": "binance", "r20": _return_from_points(pts, 20), "r60": _return_from_points(pts, 60)}


def _bybit_spot(symbol: str) -> dict[str, Any]:
    url = "https://api.bybit.com/v5/market/kline?" + urllib.parse.urlencode(
        {"category": "spot", "symbol": symbol + "USDT", "interval": "5", "limit": 14}
    )
    data = _json_url(url)
    rows = ((data or {}).get("result") or {}).get("list") or []
    pts = [(float(x[0]) / 1000.0, float(x[4])) for x in rows]
    return {"venue": "bybit", "r20": _return_from_points(pts, 20), "r60": _return_from_points(pts, 60)}


def _okx(symbol: str) -> dict[str, Any]:
    url = "https://www.okx.com/api/v5/market/candles?" + urllib.parse.urlencode(
        {"instId": symbol + "-USDT", "bar": "5m", "limit": 14}
    )
    data = _json_url(url)
    rows = (data or {}).get("data") or []
    pts = [(float(x[0]) / 1000.0, float(x[4])) for x in rows]
    return {"venue": "okx", "r20": _return_from_points(pts, 20), "r60": _return_from_points(pts, 60)}


def _coinbase(symbol: str) -> dict[str, Any]:
    url = f"https://api.exchange.coinbase.com/products/{symbol}-USD/candles?granularity=300"
    data = _json_url(url)
    pts = [(float(x[0]), float(x[4])) for x in (data or [])[:20]]
    return {"venue": "coinbase", "r20": _return_from_points(pts, 20), "r60": _return_from_points(pts, 60)}


def _kraken(symbol: str) -> dict[str, Any]:
    pair = symbol + "USD"
    url = "https://api.kraken.com/0/public/OHLC?" + urllib.parse.urlencode({"pair": pair, "interval": 5})
    data = _json_url(url)
    result = (data or {}).get("result") or {}
    rows = next((v for k, v in result.items() if k != "last" and isinstance(v, list)), [])
    pts = [(float(x[0]), float(x[4])) for x in rows[-20:]]
    return {"venue": "kraken", "r20": _return_from_points(pts, 20), "r60": _return_from_points(pts, 60)}


VENUE_FUNCS = (_binance, _bybit_spot, _okx, _coinbase, _kraken)


def fetch_global_market(market: str, bitvavo_20m: float | None) -> dict[str, Any]:
    symbol = base_symbol(market)
    rows = []
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        future_map = {pool.submit(fn, symbol): fn.__name__ for fn in VENUE_FUNCS}
        for future in concurrent.futures.as_completed(future_map):
            try:
                row = future.result()
                if row.get("r20") is not None or row.get("r60") is not None:
                    rows.append(row)
            except Exception as exc:
                errors.append({"venue": future_map[future], "reason": type(exc).__name__})
    r20s = [finite(x.get("r20")) for x in rows if finite(x.get("r20")) is not None]
    r60s = [finite(x.get("r60")) for x in rows if finite(x.get("r60")) is not None]
    med20 = _median(r20s)
    med60 = _median(r60s)
    breadth20 = None if not r20s else 100.0 * sum(x > 0 for x in r20s) / len(r20s)
    lead = None if med20 is None or bitvavo_20m is None else med20 - bitvavo_20m
    score = 0.0
    if med20 is not None:
        score += min(4.0, max(0.0, med20) * 1.5)
    if med60 is not None:
        score += min(2.5, max(0.0, med60) * 0.5)
    if breadth20 is not None:
        score += min(2.0, max(0.0, breadth20 - 50.0) / 25.0)
    if lead is not None and lead > 0:
        score += min(1.5, lead * 0.75)
    return {
        "market": market,
        "venues_available": len(rows),
        "venues": sorted(rows, key=lambda x: x["venue"]),
        "median_return_20m_pct": None if med20 is None else round(med20, 4),
        "median_return_60m_pct": None if med60 is None else round(med60, 4),
        "breadth_positive_20m_pct": None if breadth20 is None else round(breadth20, 2),
        "lead_vs_bitvavo_20m_pp": None if lead is None else round(lead, 4),
        "external_score_0_10": round(min(10.0, score), 3),
        "errors": errors,
    }


def bybit_derivatives(symbol: str, previous_oi: float | None) -> dict[str, Any]:
    try:
        url = "https://api.bybit.com/v5/market/tickers?" + urllib.parse.urlencode(
            {"category": "linear", "symbol": symbol + "USDT"}
        )
        data = _json_url(url)
        rows = ((data or {}).get("result") or {}).get("list") or []
        if not rows:
            return {"available": False}
        row = rows[0]
        oi = finite(row.get("openInterest"))
        funding = finite(row.get("fundingRate"))
        turnover = finite(row.get("turnover24h"))
        oi_delta = None
        if oi is not None and previous_oi is not None and previous_oi > 0:
            oi_delta = (oi / previous_oi - 1.0) * 100.0
        return {
            "available": True,
            "open_interest": oi,
            "open_interest_change_since_last_v3_pct": None if oi_delta is None else round(oi_delta, 4),
            "funding_rate": funding,
            "turnover_24h": turnover,
        }
    except Exception as exc:
        return {"available": False, "error": type(exc).__name__}


def execution_check(
    client: PublicClient,
    metadata: dict[str, dict[str, Any]],
    row: dict[str, Any],
    now: float,
) -> dict[str, Any]:
    market = row["market"]
    if market not in metadata:
        return {"ready": False, "reason": "MARKET_UNAVAILABLE"}
    if finite(row.get("quote_volume_24h_eur"), 0.0) < MIN_QUOTE_VOLUME_EUR:
        return {"ready": False, "reason": "WAITING_EXECUTION_LIQUIDITY"}

    try:
        book = client.get("/" + market + "/book", {"depth": 25}, cache=False)
        bid = finite(book["bids"][0][0]) if book.get("bids") else None
        ask = finite(book["asks"][0][0]) if book.get("asks") else None
        if bid is None or ask is None or not 0 < bid <= ask:
            return {"ready": False, "reason": "WAITING_VALID_BOOK"}
        spread_pct = (ask / bid - 1.0) * 100.0
        depth = walk_asks(book, REFERENCE_STAKE_EUR)
        if spread_pct > MAX_SPREAD_PCT:
            return {
                "ready": False, "reason": "WAITING_SPREAD",
                "spread_pct": round(spread_pct, 4), "depth": depth,
            }
        if not depth.get("valid"):
            return {"ready": False, "reason": "WAITING_VISIBLE_DEPTH", "spread_pct": round(spread_pct, 4), "depth": depth}
        if finite(depth.get("depth_slippage_pct"), 999) > MAX_DEPTH_SLIPPAGE_PCT:
            return {"ready": False, "reason": "WAITING_DEPTH_SLIPPAGE", "spread_pct": round(spread_pct, 4), "depth": depth}

        raw = client.get("/" + market + "/candles", {"interval": "15m", "limit": 100}, cache=False)
        features = describe(closed_candles(raw, "15m", now), "15m")
        if not features.get("valid"):
            return {"ready": False, "reason": "WAITING_VALID_STRUCTURE", "spread_pct": round(spread_pct, 4), "depth": depth}

        # V3 intentionally does not require V2's >=6% consolidation-range gate.
        # It still requires a causal structural invalidation and acceptable risk.
        plan = structural_plan(
            {**row, "ask": depth.get("vwap_eur") or ask},
            features,
            metadata[market],
            max_position_eur=REFERENCE_STAKE_EUR,
            max_trade_risk_eur=6.0,
        )
        if not plan.get("valid"):
            return {
                "ready": False,
                "reason": "WAITING_" + str(plan.get("reason") or "STRUCTURAL_PLAN"),
                "spread_pct": round(spread_pct, 4),
                "depth": depth,
            }
        if finite(plan.get("stop_distance_pct"), 999) > MAX_STOP_DISTANCE_PCT:
            return {
                "ready": False, "reason": "WAITING_STOP_GEOMETRY",
                "spread_pct": round(spread_pct, 4), "depth": depth, "plan": plan,
            }
        return {
            "ready": True,
            "reason": "ENTRY_READY_SHADOW",
            "spread_pct": round(spread_pct, 4),
            "depth": depth,
            "plan": plan,
            "structural_range_15m_pct": finite(features.get("consolidation_range_pct")),
        }
    except Exception as exc:
        return {"ready": False, "reason": "EXECUTION_SOURCE_ERROR", "error": type(exc).__name__}


def _event_key(event: dict[str, Any]) -> str:
    event_type = str(event.get("event_type") or "")
    if "THESIS" in event_type:
        scope = "thesis:" + str(event.get("thesis_id") or "")
    else:
        scope = "episode:" + str(event.get("episode") or "")
    return "|".join([
        str(event.get("market") or ""),
        scope,
        event_type,
    ])


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    keys = {_event_key(x) for x in journal.get("events", [])}
    if _event_key(event) in keys:
        return False
    journal.setdefault("events", []).append(event)
    return True


def update_v2_benchmark(payload: dict[str, Any], benchmark: dict[str, Any], now: float) -> dict[str, Any]:
    initializing = not bool(benchmark.get("initialized"))
    benchmark.setdefault("schema", "solaire_v2_frozen_benchmark_journal_v1")
    benchmark.setdefault("frozen_commit", FROZEN_V2_COMMIT)
    benchmark.setdefault("markets", {})
    benchmark.setdefault("events", [])
    tracked = {
        r["market"]: r
        for r in payload.get("tracking", []) or []
        if isinstance(r, dict) and r.get("market")
    }
    generated = _parse_ts(payload.get("generated_at_utc")) or now

    for market in sorted(set(benchmark["markets"]) | set(tracked)):
        state = benchmark["markets"].setdefault(market, {"episode": 0, "active": False})
        row = tracked.get(market)
        if row is None:
            if state.get("active"):
                state["active"] = False
                state["ended_ts"] = generated
            continue
        if not state.get("active"):
            state["episode"] = int(state.get("episode", 0)) + 1
            state["active"] = True
            state["first_seen_ts"] = generated
            benchmark["events"].append({
                "event_type": "V2_FIRST_DETECTION",
                "market": market,
                "episode": state["episode"],
                "decision_ts": generated,
                "decision_at_utc": utc(generated),
                "price_eur": finite(row.get("last")),
                "signal_state": row.get("signal_state"),
                "signal_score": finite(row.get("signal_score")),
                "frozen_commit": FROZEN_V2_COMMIT,
                "left_censored_at_v3_t0": initializing,
                "evaluations": {},
            })
        if row.get("signal_state") == "CONFIRMED_ACCELERATION" and state.get("confirmed_episode") != state["episode"]:
            state["confirmed_episode"] = state["episode"]
            benchmark["events"].append({
                "event_type": "V2_FIRST_CONFIRMED",
                "market": market,
                "episode": state["episode"],
                "decision_ts": generated,
                "decision_at_utc": utc(generated),
                "price_eur": finite(row.get("last")),
                "signal_state": row.get("signal_state"),
                "signal_score": finite(row.get("signal_score")),
                "frozen_commit": FROZEN_V2_COMMIT,
                "left_censored_at_v3_t0": initializing,
                "evaluations": {},
            })
    benchmark["initialized"] = True
    benchmark["updated_at_utc"] = utc(now)
    return benchmark


def update_rotation(
    rotation: dict[str, Any],
    entry_events: list[dict[str, Any]],
    universe_by_market: dict[str, dict[str, Any]],
    candidates_by_market: dict[str, dict[str, Any]],
    now: float,
) -> dict[str, Any]:
    rotation.setdefault("schema", "solaire_v3_rotation_shadow_v1")
    rotation.setdefault("reference_capital_eur", REFERENCE_CAPITAL_EUR)
    rotation.setdefault("reference_stake_eur", REFERENCE_STAKE_EUR)
    rotation.setdefault("cash_eur", REFERENCE_CAPITAL_EUR)
    rotation.setdefault("positions", [])
    rotation.setdefault("closed", [])
    rotation.setdefault("actions", [])
    rotation.setdefault("consumed_episodes", [])
    consumed = set(rotation["consumed_episodes"])

    for position in list(rotation["positions"]):
        current = finite((universe_by_market.get(position["market"]) or {}).get("price_eur"))
        if current is not None:
            position["mark_eur"] = current
            position["updated_at_utc"] = utc(now)
        score = finite((candidates_by_market.get(position["market"]) or {}).get("opportunity_score"))
        if score is not None:
            position["opportunity_score"] = score
        stop = finite(position.get("stop_eur"))
        if current is not None and stop is not None and current <= stop:
            position["closed_ts"] = now
            position["closed_at_utc"] = utc(now)
            position["exit_eur"] = current
            position["close_reason"] = "STOP_OBSERVED_AT_V3_CYCLE"
            rotation["cash_eur"] += REFERENCE_STAKE_EUR * (current / position["entry_eur"]) * (1 - 0.0035)
            rotation["closed"].append(position)
            rotation["positions"].remove(position)
            rotation["actions"].append({"at_utc": utc(now), "action": "CLOSE", "market": position["market"], "reason": position["close_reason"]})

    for event in sorted(entry_events, key=lambda x: finite(x.get("opportunity_score"), 0), reverse=True):
        market = event["market"]
        episode_key = market + "|" + str(event.get("episode") or "")
        if episode_key in consumed:
            continue
        if any(p["market"] == market for p in rotation["positions"]):
            continue
        score = finite(event.get("opportunity_score"), 0)
        if len(rotation["positions"]) >= MAX_SHADOW_POSITIONS:
            weakest = min(rotation["positions"], key=lambda p: finite(p.get("opportunity_score"), 0))
            if score < finite(weakest.get("opportunity_score"), 0) + 2.0:
                continue
            current = finite((universe_by_market.get(weakest["market"]) or {}).get("price_eur"))
            if current is None:
                continue
            weakest["closed_ts"] = now
            weakest["closed_at_utc"] = utc(now)
            weakest["exit_eur"] = current
            weakest["close_reason"] = "ROTATE_TO_HIGHER_FORWARD_SCORE"
            rotation["cash_eur"] += REFERENCE_STAKE_EUR * (current / weakest["entry_eur"]) * (1 - 0.0035)
            rotation["closed"].append(weakest)
            rotation["positions"].remove(weakest)
            rotation["actions"].append({
                "at_utc": utc(now), "action": "ROTATE_OUT", "market": weakest["market"],
                "to_market": market, "score_delta": round(score - finite(weakest.get("opportunity_score"), 0), 3),
            })
        if rotation["cash_eur"] < REFERENCE_STAKE_EUR * 1.0035:
            continue
        entry = finite(event.get("entry_eur"))
        if entry is None or entry <= 0:
            continue
        rotation["cash_eur"] -= REFERENCE_STAKE_EUR * 1.0035
        rotation["positions"].append({
            "market": market,
            "episode": event.get("episode"),
            "opened_ts": now,
            "opened_at_utc": utc(now),
            "entry_eur": entry,
            "stop_eur": finite(event.get("stop_eur")),
            "stake_eur": REFERENCE_STAKE_EUR,
            "opportunity_score": score,
            "horizon_class": event.get("horizon_class"),
        })
        rotation["actions"].append({"at_utc": utc(now), "action": "OPEN_SHADOW", "market": market, "score": score})
        consumed.add(episode_key)

    rotation["consumed_episodes"] = sorted(consumed)[-5000:]
    marked = rotation["cash_eur"]
    for p in rotation["positions"]:
        mark = finite(p.get("mark_eur"), p.get("entry_eur"))
        if mark and p.get("entry_eur"):
            marked += REFERENCE_STAKE_EUR * (mark / p["entry_eur"])
    rotation["marked_value_eur"] = round(marked, 2)
    rotation["updated_at_utc"] = utc(now)
    rotation["research_only"] = True
    return rotation


def main() -> int:
    now = time.time()
    universe = read_json(UNIVERSE, {}) or {}
    rows = universe.get("rows") or []
    v2 = read_json(V2_PAYLOAD, {}) or {}
    state = read_json(STATE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}
    rotation = read_json(ROTATION, {}) or {}
    benchmark = read_json(V2_BENCHMARK, {}) or {}

    initial_v3_cycle = not bool(state.get("initialized"))
    state.setdefault("schema", "solaire_v3_state_v1")
    state.setdefault("started_ts", now)
    state.setdefault("started_at_utc", utc(now))
    state.setdefault("markets", {})
    state.setdefault("previous_derivatives", {})
    state.setdefault("theses", {})
    journal.setdefault("schema", "solaire_v3_prospective_journal_v1")
    journal.setdefault("started_ts", state["started_ts"])
    journal.setdefault("started_at_utc", state["started_at_utc"])
    journal.setdefault("events", [])

    source_errors: list[dict[str, Any]] = []
    if not rows:
        status = {
            "schema": "solaire_v3_status_v1",
            "checked_at_utc": utc(now),
            "status": "DEGRADED_NONBLOCKING",
            "reason": "MISSING_NEUTRAL_UNIVERSE_SNAPSHOT",
            "frozen_v2_commit": FROZEN_V2_COMMIT,
            "research_only": True,
            "affects_v2": False,
            "affects_email": False,
            "orders_submitted": False,
        }
        atomic_json(STATUS, status)
        print("SOLAIRE_V3 " + json.dumps(status))
        return 0

    rotations = build_narrative_rotations(rows)
    news, news_errors = fetch_news(now)
    source_errors.extend(news_errors)

    v2_tracking = {
        r["market"]: r
        for r in v2.get("tracking", []) or []
        if isinstance(r, dict) and r.get("market")
    }

    base_candidates = []
    for row in rows:
        if not (row.get("data_quality") or {}).get("ok", False):
            continue
        market = row.get("market")
        if not market:
            continue
        symbol = base_symbol(market)
        early = early_quant_evidence(row)
        hits, news_score = news_for_symbol(symbol, news, now)
        sector_names = narratives_for_market(market)
        active_rotations = [
            (name, rotations.get(name) or {})
            for name in sector_names
            if (rotations.get(name) or {}).get("active_watch")
        ]
        raw_rotation = max([finite(x[1].get("rotation_score_0_3"), 0) for x in active_rotations] or [0])
        narrative_score = min(10.0, raw_rotation / 3.0 * 10.0)
        v2row = v2_tracking.get(market) or {}
        local_priority = (
            finite(early.get("score_0_10"), 0)
            + news_score
            + narrative_score
            + (3.0 if v2row.get("signal_state") == "CONFIRMED_ACCELERATION" else 1.5 if v2row else 0.0)
        )
        if news_score > 0 or active_rotations or early.get("ready") or v2row:
            base_candidates.append({
                **row,
                "symbol": symbol,
                "early_quant": early,
                "news_items": hits,
                "news_score": news_score,
                "narratives": sector_names,
                "active_narratives": [x[0] for x in active_rotations],
                "narrative_score": round(narrative_score, 3),
                "local_priority": round(local_priority, 3),
                "v2_state": v2row.get("signal_state"),
                "v2_score": finite(v2row.get("signal_score")),
            })

    base_candidates.sort(key=lambda x: x["local_priority"], reverse=True)
    external_targets = base_candidates[:MAX_EXTERNAL_MARKETS]
    external_map: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {}
        for row in external_targets:
            bitvavo20 = finite(((row.get("features") or {}).get("5m") or {}).get("return_4bar_pct"))
            futures[pool.submit(fetch_global_market, row["market"], bitvavo20)] = row["market"]
        for future in concurrent.futures.as_completed(futures):
            market = futures[future]
            try:
                external_map[market] = future.result()
            except Exception as exc:
                source_errors.append({"source": "global_price_discovery", "market": market, "reason": type(exc).__name__})

    candidates = []
    for row in base_candidates:
        ext = external_map.get(row["market"]) or {
            "market": row["market"], "venues_available": 0, "external_score_0_10": 0.0, "errors": [{"reason": "NOT_QUERIED_OR_UNAVAILABLE"}]
        }
        external_score = finite(ext.get("external_score_0_10"), 0.0)
        opp = score_opportunity(
            finite((row.get("early_quant") or {}).get("score_0_10"), 0),
            finite(row.get("news_score"), 0),
            finite(row.get("narrative_score"), 0),
            external_score,
        )
        external_confirmed = int(ext.get("venues_available") or 0) >= 2 and external_score >= 1.0
        context_watch = (
            finite(row.get("news_score"), 0) > 0
            or bool(row.get("active_narratives"))
            or external_confirmed
        )
        independent_context = context_watch
        v2_confirmed = row.get("v2_state") == "CONFIRMED_ACCELERATION"
        fresh_opportunity_trigger = (
            bool((row.get("early_quant") or {}).get("ready")) and independent_context
        ) or v2_confirmed
        entry_hypothesis = fresh_opportunity_trigger
        merged = {
            **row,
            "external": ext,
            "external_score": external_score,
            "opportunity_score": opp,
            "context_watch": context_watch,
            "fresh_opportunity_trigger": fresh_opportunity_trigger,
            "entry_hypothesis": entry_hypothesis,
        }
        merged["horizon_class"] = classify_horizon(merged)
        candidates.append(merged)

    candidates.sort(key=lambda x: x["opportunity_score"], reverse=True)

    # Sixth V3 research axis: persistent opportunity theses.  A thesis is
    # independent from the short acceleration episode and remains research-only.
    thesis_targets = [
        x for x in candidates
        if x.get("fresh_opportunity_trigger")
        or bool(((state.get("theses") or {}).get(x["market"]) or {}).get("active"))
    ]
    thesis_targets.sort(
        key=lambda x: (
            0 if x.get("fresh_opportunity_trigger") else 1,
            -finite(x.get("opportunity_score"), 0),
        )
    )
    long_trend_profiles: dict[str, dict[str, Any]] = {}
    if thesis_targets:
        try:
            trend_client = PublicClient(timeout=8, retries=2, requests_per_second=8)
            long_trend_profiles, trend_errors = fetch_long_trend_profiles(
                trend_client,
                [x["market"] for x in thesis_targets],
                now,
            )
            source_errors.extend(trend_errors)
        except Exception as exc:
            source_errors.append({"source": "long_trend", "reason": type(exc).__name__})

    for row in candidates:
        market = row["market"]
        prior = (state.get("theses") or {}).get(market) or {}
        long_trend = long_trend_profiles.get(market) or prior.get("last_long_trend") or {}
        row["long_trend"] = long_trend
        prior_state = prior.get("state")
        prior_active = bool(prior.get("active"))
        thesis = advance_persistent_thesis(prior, row, now)
        if thesis:
            state["theses"][market] = thesis
        row["persistent_thesis"] = thesis or {}
        row["thesis_reentry_hypothesis"] = bool(
            thesis.get("active") and thesis.get("state") == "REENTRY_READY_THESIS"
        )

        opened = bool(thesis.get("active")) and not prior_active
        if opened:
            event = {
                "event_type": "OPPORTUNITY_THESIS_START",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(row.get("price_eur")),
                "opportunity_score": row.get("opportunity_score"),
                "horizon_class": row.get("horizon_class"),
                "long_trend": long_trend,
                "early_quant": row.get("early_quant"),
                "context": {
                    "news_score": row.get("news_score"),
                    "active_narratives": row.get("active_narratives"),
                    "narrative_score": row.get("narrative_score"),
                    "external": row.get("external"),
                },
                "v2_state_at_event": row.get("v2_state"),
                "left_censored_at_v3_t0": initial_v3_cycle,
                "evaluations": {},
            }
            _append_event(journal, event)

        if (
            thesis.get("active")
            and thesis.get("state") == "REENTRY_READY_THESIS"
            and prior_state != "REENTRY_READY_THESIS"
        ):
            event = {
                "event_type": "OPPORTUNITY_THESIS_REENTRY_READY",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(row.get("price_eur")),
                "opportunity_score": row.get("opportunity_score"),
                "horizon_class": row.get("horizon_class"),
                "long_trend": long_trend,
                "thesis": thesis,
                "v2_state_at_event": row.get("v2_state"),
                "left_censored_at_v3_t0": False,
                "evaluations": {},
            }
            _append_event(journal, event)

    # Derivatives are diagnostic only and sampled on the strongest candidates.
    for row in candidates[:8]:
        prev = finite((state.get("previous_derivatives") or {}).get(row["market"]))
        derivative = bybit_derivatives(row["symbol"], prev)
        row["derivatives"] = derivative
        oi = finite(derivative.get("open_interest"))
        if oi is not None:
            state["previous_derivatives"][row["market"]] = oi

    # Preserve V2 confirmed candidates in the execution check even if their V3
    # opportunity score is not in the top-N.
    execution_rows = [x for x in candidates if x.get("entry_hypothesis")]
    execution_rows.sort(
        key=lambda x: (
            0 if x.get("v2_state") == "CONFIRMED_ACCELERATION" else 1,
            -finite(x.get("opportunity_score"), 0),
        )
    )
    execution_rows = execution_rows[:MAX_EXECUTION_MARKETS]

    client = PublicClient(timeout=8, retries=2, requests_per_second=10)
    metadata: dict[str, dict[str, Any]] = {}
    critical_error = None
    try:
        client.get("/time", cache=False)
        metadata = {
            m["market"]: m for m in client.get("/markets")
            if m.get("quote") == "EUR" and m.get("status") == "trading"
        }
    except Exception as exc:
        critical_error = type(exc).__name__ + ":" + str(exc)

    checks = {}
    if metadata:
        for row in execution_rows:
            checks[row["market"]] = execution_check(client, metadata, row, time.time())

    current_markets = set()
    new_entry_events = []
    new_thesis_entry_events = []
    rotation_ready_events = []
    for row in candidates:
        market = row["market"]
        current_markets.add(market)
        ms = state["markets"].setdefault(market, {"episode": 0, "active": False})
        if not ms.get("active") or now - finite(ms.get("last_seen_ts"), 0) > WATCH_EXPIRY:
            ms["episode"] = int(ms.get("episode", 0)) + 1
            ms["active"] = True
            ms["started_ts"] = now
            ms["started_at_utc"] = utc(now)
            ms.pop("prewatch_recorded_episode", None)
            ms.pop("entry_recorded_episode", None)
            ms["timing"] = {"episode": ms["episode"]}
        ms["last_seen_ts"] = now
        ms["last_seen_at_utc"] = utc(now)
        ms["last_opportunity_score"] = row["opportunity_score"]
        ms["last_horizon_class"] = row["horizon_class"]

        if row.get("context_watch") and ms.get("prewatch_recorded_episode") != ms["episode"]:
            event = {
                "event_type": "PREWATCH_CONTEXT",
                "market": market,
                "episode": ms["episode"],
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(row.get("price_eur")),
                "opportunity_score": row["opportunity_score"],
                "horizon_class": row["horizon_class"],
                "context": {
                    "news_score": row.get("news_score"),
                    "news_items": row.get("news_items"),
                    "active_narratives": row.get("active_narratives"),
                    "narrative_score": row.get("narrative_score"),
                    "external": row.get("external"),
                },
                "early_quant": row.get("early_quant"),
                "v2_state_at_event": row.get("v2_state"),
                "left_censored_at_v3_t0": initial_v3_cycle,
                "evaluations": {},
            }
            if _append_event(journal, event):
                ms["prewatch_recorded_episode"] = ms["episode"]

        check = checks.get(market)
        if row.get("entry_hypothesis") and check is not None:
            ms["execution_state"] = check.get("reason")
            ms["execution_checked_at_utc"] = utc(now)

            # Fifth V3 research axis: entry timing.  These timing variants are
            # measured prospectively in parallel and never affect V2, email,
            # orders, or the existing raw V3 entry-ready event.
            timing = ms.setdefault("timing", {"episode": ms["episode"]})
            if timing.get("episode") != ms["episode"]:
                timing.clear()
                timing["episode"] = ms["episode"]

            observed_price = finite(row.get("price_eur"))
            if timing.get("raw_ready_ts") is not None and observed_price is not None:
                low = finite(timing.get("low_since_raw_ready_eur"), observed_price)
                timing["low_since_raw_ready_eur"] = min(low, observed_price)

            if check.get("ready"):
                plan = check.get("plan") or {}
                current_entry = finite(plan.get("entry_eur"))
                if current_entry is not None and current_entry > 0:
                    if timing.get("raw_ready_ts") is None:
                        timing["raw_ready_ts"] = now
                        timing["raw_ready_at_utc"] = utc(now)
                        timing["raw_entry_eur"] = current_entry
                        timing["low_since_raw_ready_eur"] = current_entry
                    low = finite(timing.get("low_since_raw_ready_eur"), current_entry)
                    timing["low_since_raw_ready_eur"] = min(low, current_entry)

                    raw_entry = finite(timing.get("raw_entry_eur"))
                    raw_ts = finite(timing.get("raw_ready_ts"))
                    low = finite(timing.get("low_since_raw_ready_eur"))
                    drift_pct = None if not raw_entry else (current_entry / raw_entry - 1.0) * 100.0
                    pullback_pct = None if not raw_entry or low is None else (low / raw_entry - 1.0) * 100.0
                    reclaim_pct = None if low is None or low <= 0 else (current_entry / low - 1.0) * 100.0
                    timing["current_drift_pct"] = None if drift_pct is None else round(drift_pct, 4)
                    timing["max_pullback_pct"] = None if pullback_pct is None else round(pullback_pct, 4)
                    timing["reclaim_from_low_pct"] = None if reclaim_pct is None else round(reclaim_pct, 4)

                    if (
                        raw_ts is not None
                        and now - raw_ts >= TIMING_PERSIST_MIN_SECONDS
                        and drift_pct is not None
                        and TIMING_PERSIST_MIN_DRIFT_PCT <= drift_pct <= TIMING_PERSIST_MAX_DRIFT_PCT
                        and timing.get("persist30_recorded_episode") != ms["episode"]
                    ):
                        event = {
                            "event_type": "ENTRY_TIMING_PERSIST_30M",
                            "market": market,
                            "episode": ms["episode"],
                            "decision_ts": now,
                            "decision_at_utc": utc(now),
                            "price_eur": finite(row.get("price_eur")),
                            "entry_eur": current_entry,
                            "stop_eur": finite(plan.get("stop_eur")),
                            "tp1_eur": finite(plan.get("tp1_eur")),
                            "stake_eur": REFERENCE_STAKE_EUR,
                            "opportunity_score": row["opportunity_score"],
                            "horizon_class": row["horizon_class"],
                            "entry_source": "V3_TIMING_PERSIST_30M",
                            "timing": {
                                "raw_ready_ts": raw_ts,
                                "raw_entry_eur": raw_entry,
                                "delay_minutes": round((now - raw_ts) / 60.0, 2),
                                "drift_from_raw_pct": round(drift_pct, 4),
                                "max_pullback_pct": None if pullback_pct is None else round(pullback_pct, 4),
                            },
                            "execution": check,
                            "v2_state_at_event": row.get("v2_state"),
                            "left_censored_at_v3_t0": initial_v3_cycle,
                            "evaluations": {},
                        }
                        if _append_event(journal, event):
                            timing["persist30_recorded_episode"] = ms["episode"]

                    if (
                        pullback_pct is not None
                        and pullback_pct <= TIMING_PULLBACK_MIN_PCT
                        and reclaim_pct is not None
                        and reclaim_pct >= TIMING_RECLAIM_MIN_PCT
                        and drift_pct is not None
                        and drift_pct <= TIMING_RECLAIM_MAX_DRIFT_PCT
                        and timing.get("reclaim_recorded_episode") != ms["episode"]
                    ):
                        event = {
                            "event_type": "ENTRY_TIMING_PULLBACK_RECLAIM",
                            "market": market,
                            "episode": ms["episode"],
                            "decision_ts": now,
                            "decision_at_utc": utc(now),
                            "price_eur": finite(row.get("price_eur")),
                            "entry_eur": current_entry,
                            "stop_eur": finite(plan.get("stop_eur")),
                            "tp1_eur": finite(plan.get("tp1_eur")),
                            "stake_eur": REFERENCE_STAKE_EUR,
                            "opportunity_score": row["opportunity_score"],
                            "horizon_class": row["horizon_class"],
                            "entry_source": "V3_TIMING_PULLBACK_RECLAIM",
                            "timing": {
                                "raw_ready_ts": raw_ts,
                                "raw_entry_eur": raw_entry,
                                "delay_minutes": None if raw_ts is None else round((now - raw_ts) / 60.0, 2),
                                "drift_from_raw_pct": round(drift_pct, 4),
                                "max_pullback_pct": round(pullback_pct, 4),
                                "reclaim_from_low_pct": round(reclaim_pct, 4),
                            },
                            "execution": check,
                            "v2_state_at_event": row.get("v2_state"),
                            "left_censored_at_v3_t0": initial_v3_cycle,
                            "evaluations": {},
                        }
                        if _append_event(journal, event):
                            timing["reclaim_recorded_episode"] = ms["episode"]

                rotation_ready_events.append({
                    "market": market,
                    "episode": ms["episode"],
                    "entry_eur": finite(plan.get("entry_eur")),
                    "stop_eur": finite(plan.get("stop_eur")),
                    "opportunity_score": row["opportunity_score"],
                    "horizon_class": row["horizon_class"],
                })
            if check.get("ready") and ms.get("entry_recorded_episode") != ms["episode"]:
                plan = check.get("plan") or {}
                source = (
                    "V2_CONFIRMED_REFERENCE_PATH"
                    if row.get("v2_state") == "CONFIRMED_ACCELERATION"
                    else "V3_CONTEXT_PLUS_EARLY_QUANT"
                )
                event = {
                    "event_type": "ENTRY_READY_SHADOW",
                    "market": market,
                    "episode": ms["episode"],
                    "decision_ts": now,
                    "decision_at_utc": utc(now),
                    "price_eur": finite(row.get("price_eur")),
                    "entry_eur": finite(plan.get("entry_eur")),
                    "stop_eur": finite(plan.get("stop_eur")),
                    "tp1_eur": finite(plan.get("tp1_eur")),
                    "stake_eur": REFERENCE_STAKE_EUR,
                    "opportunity_score": row["opportunity_score"],
                    "horizon_class": row["horizon_class"],
                    "entry_source": source,
                    "execution": check,
                    "context": {
                        "news_score": row.get("news_score"),
                        "news_items": row.get("news_items"),
                        "active_narratives": row.get("active_narratives"),
                        "narrative_score": row.get("narrative_score"),
                        "external": row.get("external"),
                        "derivatives": row.get("derivatives"),
                    },
                    "early_quant": row.get("early_quant"),
                    "v2_state_at_event": row.get("v2_state"),
                    "left_censored_at_v3_t0": initial_v3_cycle,
                    "evaluations": {},
                }
                if _append_event(journal, event):
                    ms["entry_recorded_episode"] = ms["episode"]
                    new_entry_events.append(event)

        if row.get("thesis_reentry_hypothesis") and check is not None:
            thesis = (state.get("theses") or {}).get(market) or {}
            thesis["last_execution_state"] = check.get("reason")
            thesis["last_execution_checked_at_utc"] = utc(now)
            thesis_id = thesis.get("thesis_id")
            if (
                check.get("ready")
                and thesis_id is not None
                and thesis.get("entry_recorded_thesis_id") != thesis_id
            ):
                plan = check.get("plan") or {}
                event = {
                    "event_type": "ENTRY_THESIS_REENTRY_SHADOW",
                    "market": market,
                    "thesis_id": thesis_id,
                    "decision_ts": now,
                    "decision_at_utc": utc(now),
                    "price_eur": finite(row.get("price_eur")),
                    "entry_eur": finite(plan.get("entry_eur")),
                    "stop_eur": finite(plan.get("stop_eur")),
                    "tp1_eur": finite(plan.get("tp1_eur")),
                    "stake_eur": REFERENCE_STAKE_EUR,
                    "opportunity_score": row.get("opportunity_score"),
                    "horizon_class": row.get("horizon_class"),
                    "entry_source": "V3_PERSISTENT_THESIS_REENTRY",
                    "execution": check,
                    "long_trend": row.get("long_trend"),
                    "thesis": thesis,
                    "v2_state_at_event": row.get("v2_state"),
                    "left_censored_at_v3_t0": False,
                    "evaluations": {},
                }
                if _append_event(journal, event):
                    thesis["entry_recorded_thesis_id"] = thesis_id
                    new_thesis_entry_events.append(event)

    for market, ms in state["markets"].items():
        if market not in current_markets and ms.get("active") and now - finite(ms.get("last_seen_ts"), 0) > WATCH_EXPIRY:
            ms["active"] = False
            ms["ended_ts"] = now
            ms["ended_at_utc"] = utc(now)

    benchmark = update_v2_benchmark(v2, benchmark, now)
    universe_by_market = {x.get("market"): x for x in rows if x.get("market")}
    candidates_by_market = {x["market"]: x for x in candidates}
    rotation = update_rotation(rotation, rotation_ready_events, universe_by_market, candidates_by_market, now)

    state["initialized"] = True
    state["updated_at_utc"] = utc(now)
    journal["updated_at_utc"] = utc(now)
    journal["research_only"] = True
    journal["frozen_v2_commit"] = FROZEN_V2_COMMIT
    journal["events"] = journal["events"][-10000:]

    compact_candidates = []
    for row in candidates[:40]:
        compact_candidates.append({
            "market": row["market"],
            "price_eur": row.get("price_eur"),
            "change_24h_pct": row.get("change_24h_pct"),
            "quote_volume_24h_eur": row.get("quote_volume_24h_eur"),
            "opportunity_score": row.get("opportunity_score"),
            "horizon_class": row.get("horizon_class"),
            "context_watch": row.get("context_watch"),
            "fresh_opportunity_trigger": row.get("fresh_opportunity_trigger"),
            "entry_hypothesis": row.get("entry_hypothesis"),
            "thesis_reentry_hypothesis": row.get("thesis_reentry_hypothesis"),
            "early_quant": row.get("early_quant"),
            "news_score": row.get("news_score"),
            "news_items": row.get("news_items"),
            "active_narratives": row.get("active_narratives"),
            "narrative_score": row.get("narrative_score"),
            "external": row.get("external"),
            "long_trend": row.get("long_trend"),
            "persistent_thesis": row.get("persistent_thesis"),
            "derivatives": row.get("derivatives"),
            "v2_state": row.get("v2_state"),
            "v2_score": row.get("v2_score"),
            "execution": checks.get(row["market"]),
            "timing_state": (state.get("markets", {}).get(row["market"], {}) or {}).get("timing"),
        })

    candidate_doc = {
        "schema": "solaire_v3_candidates_v1",
        "generated_at_utc": utc(now),
        "research_only": True,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "narrative_rotations": rotations,
        "news_items_considered": len(news),
        "candidates": compact_candidates,
    }
    status = {
        "schema": "solaire_v3_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical_error else ("OK_WITH_SOURCE_GAPS" if source_errors else "OK"),
        "mode": "PROSPECTIVE_SHADOW",
        "research_only": True,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "universe_rows": len(rows),
        "context_news_items": len(news),
        "candidate_count": len(candidates),
        "context_watch_count": sum(bool(x.get("context_watch")) for x in candidates),
        "entry_hypothesis_count": sum(bool(x.get("entry_hypothesis")) for x in candidates),
        "thesis_reentry_hypothesis_count": sum(bool(x.get("thesis_reentry_hypothesis")) for x in candidates),
        "execution_checks": len(checks),
        "entry_ready_shadow_count": sum(
            bool(checks.get(x["market"], {}).get("ready"))
            for x in candidates if x.get("entry_hypothesis")
        ),
        "thesis_reentry_execution_ready_count": sum(
            bool(checks.get(x["market"], {}).get("ready"))
            for x in candidates if x.get("thesis_reentry_hypothesis")
        ),
        "new_entry_events": len(new_entry_events),
        "new_thesis_entry_events": len(new_thesis_entry_events),
        "active_theses": sum(bool(x.get("active")) for x in (state.get("theses") or {}).values()),
        "thesis_reentry_ready_states": sum(
            x.get("state") == "REENTRY_READY_THESIS"
            for x in (state.get("theses") or {}).values()
        ),
        "thesis_start_events": sum(x.get("event_type") == "OPPORTUNITY_THESIS_START" for x in journal.get("events", [])),
        "thesis_reentry_events": sum(x.get("event_type") == "OPPORTUNITY_THESIS_REENTRY_READY" for x in journal.get("events", [])),
        "thesis_entry_events": sum(x.get("event_type") == "ENTRY_THESIS_REENTRY_SHADOW" for x in journal.get("events", [])),
        "timing_persist_30m_events": sum(x.get("event_type") == "ENTRY_TIMING_PERSIST_30M" for x in journal.get("events", [])),
        "timing_pullback_reclaim_events": sum(x.get("event_type") == "ENTRY_TIMING_PULLBACK_RECLAIM" for x in journal.get("events", [])),
        "rotation_positions": len(rotation.get("positions", [])),
        "rotation_marked_value_eur": rotation.get("marked_value_eur"),
        "critical_error": critical_error,
        "source_errors": source_errors[:40],
    }

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(CANDIDATES, candidate_doc)
    atomic_json(ROTATION, rotation)
    atomic_json(V2_BENCHMARK, benchmark)
    atomic_json(STATUS, status)
    print("SOLAIRE_V3 " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
