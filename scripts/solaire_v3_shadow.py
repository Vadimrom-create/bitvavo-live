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
import html as html_lib
import json
import math
import os
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
    V3_ARCHITECTURE_VERSION,
    MAX_SHADOW_POSITIONS,
    REFERENCE_CAPITAL_EUR,
    REFERENCE_STAKE_EUR,
    advance_persistent_thesis,
    base_symbol,
    build_asset_aliases,
    build_dynamic_rotation_context,
    build_narrative_rotations,
    classify_horizon,
    classify_news_event,
    early_quant_evidence,
    match_news_assets,
    narratives_for_market,
    score_opportunity,
    select_fair_batch,
    select_priority_fair_batch,
    structured_news_symbols,
    walk_asks,
)

UNIVERSE = "production_universe_snapshot.json"
V2_PAYLOAD = "production_alert_candidates.json"
STATE = "solaire_v3_state.json"
JOURNAL = "solaire_v3_journal.json"
STATUS = "solaire_v3_status.json"
CANDIDATES = "solaire_v3_candidates.json"
THESES = "solaire_v3_theses.json"
ROTATION = "solaire_v3_rotation_state.json"
V2_BENCHMARK = "solaire_v2_frozen_benchmark_journal.json"

MAX_CONTEXT_AGE = 36 * 3600
WATCH_EXPIRY = 24 * 3600
MAX_EXTERNAL_MARKETS = 18
MAX_EXECUTION_MARKETS = 18
MAX_THESIS_PROFILE_MARKETS = 24
MAX_THESIS_EXECUTION_MARKETS = 20
MAX_DERIVATIVE_MARKETS = 12
MIN_QUOTE_VOLUME_EUR = 75_000.0
MAX_SPREAD_PCT = 0.50
MAX_DEPTH_SLIPPAGE_PCT = 0.50
MAX_STOP_DISTANCE_PCT = 10.0
MIN_NET_RR = 1.5
HTTP_TIMEOUT = 5
RUNTIME_COMMIT = os.environ.get("GITHUB_SHA") or "LOCAL_OR_UNKNOWN"

TIMING_PERSIST_MIN_SECONDS = 30 * 60
TIMING_PERSIST_MIN_DRIFT_PCT = -2.0
TIMING_PERSIST_MAX_DRIFT_PCT = 3.0
TIMING_PULLBACK_MIN_PCT = -2.0
TIMING_RECLAIM_MIN_PCT = 1.0
TIMING_RECLAIM_MAX_DRIFT_PCT = 3.0

OFFICIAL_ANNOUNCEMENT_PAGES = (
    ("binance_official_page", "https://www.binance.com/en/support/announcement/", "https://www.binance.com"),
    ("coinbase_official_page", "https://www.coinbase.com/blog", "https://www.coinbase.com"),
    ("bybit_official", "https://announcements.bybit.com/en/", "https://announcements.bybit.com"),
    ("okx_official", "https://www.okx.com/help/category/announcements", "https://www.okx.com"),
)

NEWS_FEEDS = (
    ("coindesk", "https://www.coindesk.com/arc/outboundfeeds/rss/", "media"),
    ("cointelegraph", "https://cointelegraph.com/rss", "media"),
    ("decrypt", "https://decrypt.co/feed", "media"),
    ("crypto.news", "https://crypto.news/feed/", "media"),
    ("cryptoast", "https://cryptoast.fr/feed/", "media"),
    ("coinbase_official", "https://www.coinbase.com/blog/rss.xml", "official_exchange"),
    ("kraken_official", "https://blog.kraken.com/feed", "official_exchange"),
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


def build_full_universe_news_aliases(
    universe_rows: list[dict[str, Any]],
) -> tuple[dict[str, tuple[str, ...]], dict[str, Any], list[dict[str, str]]]:
    """Build ticker + canonical-name aliases for every Bitvavo EUR market."""
    errors: list[dict[str, str]] = []
    asset_rows: list[dict[str, Any]] = []
    try:
        raw = _json_url("https://api.bitvavo.com/v2/assets")
        if isinstance(raw, list):
            asset_rows = [x for x in raw if isinstance(x, dict)]
        else:
            errors.append({"source": "bitvavo_assets", "reason": "UNEXPECTED_RESPONSE"})
    except Exception as exc:
        errors.append({"source": "bitvavo_assets", "reason": type(exc).__name__})

    aliases = build_asset_aliases(universe_rows, asset_rows)
    asset_names = {
        str(x.get("symbol") or "").upper(): str(x.get("name") or "").strip()
        for x in asset_rows
        if x.get("symbol") and x.get("name")
    }
    named = sum(bool(asset_names.get(symbol)) for symbol in aliases)
    diagnostics = {
        "mode": "FULL_BITVAVO_DYNAMIC_ASSET_MAP",
        "asset_source": "Bitvavo /assets",
        "universe_symbols": len(aliases),
        "ticker_coverage_symbols": len(aliases),
        "named_alias_symbols": named,
        "named_alias_coverage_pct": round(named / len(aliases) * 100.0, 2) if aliases else 0.0,
        "fallback_ticker_only_symbols": sorted(symbol for symbol in aliases if not asset_names.get(symbol))[:50],
    }
    return aliases, diagnostics, errors


def _news_asset_symbols(text: str, asset_aliases: dict[str, tuple[str, ...]]) -> list[str]:
    return match_news_assets(text, asset_aliases, GENERIC_SYMBOLS)


def _decorate_news_item(
    *,
    source: str,
    source_kind: str,
    published: float,
    title: str,
    url: str | None,
    symbols: list[str],
) -> dict[str, Any]:
    event = classify_news_event(title, source_kind=source_kind)
    return {
        "source": source,
        "source_kind": source_kind,
        "published_ts": published,
        "published_at_utc": utc(published),
        "title": title[:300],
        "url": url,
        "symbols": symbols,
        "event": event,
    }


def _fetch_binance_official_news(
    now: float,
    asset_aliases: dict[str, tuple[str, ...]],
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    items: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    try:
        url = (
            "https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?"
            + urllib.parse.urlencode({"catalogId": 48, "pageNo": 1, "pageSize": 30, "type": 1})
        )
        data = _json_url(url)
        catalogs = ((data or {}).get("data") or {}).get("catalogs") or []
        articles = []
        for catalog in catalogs:
            articles.extend(catalog.get("articles") or [])
        for row in articles:
            title = str(row.get("title") or "").strip()
            published = _parse_ts(row.get("releaseDate") or row.get("publishDate"))
            if published is not None and published > 10_000_000_000:
                published /= 1000.0
            if published is None or now - published > MAX_CONTEXT_AGE or published - now > 300:
                continue
            symbols = _news_asset_symbols(title, asset_aliases)
            if not symbols:
                continue
            code = str(row.get("code") or "").strip()
            link = f"https://www.binance.com/en/support/announcement/detail/{code}" if code else None
            items.append(_decorate_news_item(
                source="binance_official", source_kind="official_exchange",
                published=published, title=title, url=link, symbols=symbols,
            ))
    except Exception as exc:
        errors.append({"source": "binance_official", "reason": type(exc).__name__})
    return items, errors


def fetch_official_page_deltas(
    now: float,
    asset_aliases: dict[str, tuple[str, ...]],
    seen: dict[str, float] | None,
    *,
    initialized: bool,
) -> tuple[list[dict[str, Any]], dict[str, float], list[dict[str, str]]]:
    """Poll official announcement pages without pretending old page items are fresh.

    The first successful observation seeds the registry and emits nothing.  On
    later cycles, only newly observed announcement titles enter the news stream.
    """
    seen = dict(seen or {})
    items: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for source, url, base_url in OFFICIAL_ANNOUNCEMENT_PAGES:
        try:
            page = _text_url(url)
            for href, raw_title in re.findall(r"<a[^>]+href=['\\\"]([^'\\\"]+)['\\\"][^>]*>(.*?)</a>", page, flags=re.I | re.S):
                title = html_lib.unescape(re.sub(r"<[^>]+>", " ", raw_title))
                title = re.sub(r"\s+", " ", title).strip()
                if not (12 <= len(title) <= 260):
                    continue
                symbols = _news_asset_symbols(title, asset_aliases)
                if not symbols:
                    continue
                fingerprint = source + "|" + title.lower()
                first_seen = seen.get(fingerprint)
                if first_seen is None:
                    seen[fingerprint] = now
                    if initialized:
                        first_seen = now
                    else:
                        continue
                if now - first_seen > MAX_CONTEXT_AGE:
                    continue
                link = href if href.startswith("http") else base_url.rstrip("/") + "/" + href.lstrip("/")
                items.append(_decorate_news_item(
                    source=source, source_kind="official_exchange", published=first_seen,
                    title=title, url=link, symbols=symbols,
                ))
        except Exception as exc:
            errors.append({"source": source, "reason": type(exc).__name__})
    # Bound persistent state while keeping the full context window plus margin.
    keep_after = now - MAX_CONTEXT_AGE * 2
    seen = {k: v for k, v in seen.items() if finite(v, 0) >= keep_after}
    return items, seen, errors


def fetch_news(
    now: float,
    asset_aliases: dict[str, tuple[str, ...]],
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    items: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    official, official_errors = _fetch_binance_official_news(now, asset_aliases)
    items.extend(official)
    errors.extend(official_errors)

    try:
        data = _json_url("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
        for row in (data or {}).get("Data", []) or []:
            published = _parse_ts(row.get("published_on"))
            if published is None or now - published > MAX_CONTEXT_AGE or published - now > 300:
                continue
            title = str(row.get("title") or "")
            # Provider categories are structured evidence.  Free-form article
            # bodies are deliberately excluded from entity resolution because
            # they generated ordinary-word collisions (Across, Momentum, Form...).
            symbols = set(_news_asset_symbols(title, asset_aliases))
            symbols.update(structured_news_symbols(row.get("categories"), set(asset_aliases)))
            symbols = sorted(symbols)
            if symbols:
                items.append(_decorate_news_item(
                    source=str(row.get("source") or "cryptocompare"),
                    source_kind="aggregator", published=published, title=title,
                    url=row.get("url"), symbols=symbols,
                ))
    except Exception as exc:
        errors.append({"source": "cryptocompare", "reason": type(exc).__name__})

    for source, url, source_kind in NEWS_FEEDS:
        try:
            root = ET.fromstring(_text_url(url))
            for node in root.findall(".//item"):
                title = (node.findtext("title") or "").strip()
                link = (node.findtext("link") or "").strip()
                published = _parse_ts(node.findtext("pubDate"))
                if published is None or now - published > MAX_CONTEXT_AGE or published - now > 300:
                    continue
                # Title-only entity resolution is intentional: descriptions
                # are prose-heavy and created false asset mentions.
                symbols = _news_asset_symbols(title, asset_aliases)
                if symbols:
                    items.append(_decorate_news_item(
                        source=source, source_kind=source_kind,
                        published=published, title=title, url=link, symbols=symbols,
                    ))
        except Exception as exc:
            errors.append({"source": source, "reason": type(exc).__name__})

    dedup = {}
    for item in items:
        key = (item.get("source"), item.get("title"), item.get("published_at_utc"))
        dedup[key] = item
    return sorted(dedup.values(), key=lambda x: x["published_ts"], reverse=True), errors


def news_for_symbol(
    symbol: str,
    news: list[dict[str, Any]],
    now: float,
) -> tuple[list[dict[str, Any]], float, float, float]:
    hits = [x for x in news if symbol in (x.get("symbols") or [])]
    if not hits:
        return [], 0.0, 0.0, 0.0
    sources = {x.get("source") for x in hits}
    freshest_hours = min(max(0.0, (now - x["published_ts"]) / 3600) for x in hits)
    recency = max(0.0, 4.0 - freshest_hours / 6.0)

    def weight(item: dict[str, Any]) -> float:
        event = item.get("event") or {}
        materiality = float(event.get("materiality") or 1.0)
        reliability = 1.25 if item.get("source_kind") == "official_exchange" else 1.0
        return materiality * reliability

    total_weight = sum(weight(x) for x in hits)
    positive_weight = sum(weight(x) for x in hits if (x.get("event") or {}).get("direction") == "POSITIVE")
    negative_weight = sum(weight(x) for x in hits if (x.get("event") or {}).get("direction") == "NEGATIVE")
    score = min(10.0, recency + min(3.5, total_weight * 0.55) + min(2.5, len(sources) * 0.65))
    positive_score = min(10.0, recency * 0.5 + positive_weight * 1.25) if positive_weight else 0.0
    negative_score = min(10.0, recency * 0.5 + negative_weight * 1.25) if negative_weight else 0.0
    return hits[:10], round(score, 3), round(positive_score, 3), round(negative_score, 3)


def fetch_external_price_snapshot(
    allowed_symbols: set[str],
) -> tuple[dict[str, dict[str, float]], list[dict[str, str]]]:
    """One batch request per venue gives full-universe external discovery."""
    prices: dict[str, dict[str, float]] = {symbol: {} for symbol in allowed_symbols}
    errors: list[dict[str, str]] = []

    try:
        rows = _json_url("https://api.binance.com/api/v3/ticker/price") or []
        for row in rows if isinstance(rows, list) else []:
            pair = str(row.get("symbol") or "")
            if not pair.endswith("USDT"):
                continue
            symbol = pair[:-4]
            px = finite(row.get("price"))
            if symbol in prices and px is not None and px > 0:
                prices[symbol]["binance"] = px
    except Exception as exc:
        errors.append({"source": "external_batch_binance", "reason": type(exc).__name__})

    try:
        data = _json_url("https://api.bybit.com/v5/market/tickers?category=spot")
        rows = ((data or {}).get("result") or {}).get("list") or []
        for row in rows:
            pair = str(row.get("symbol") or "")
            if not pair.endswith("USDT"):
                continue
            symbol = pair[:-4]
            px = finite(row.get("lastPrice"))
            if symbol in prices and px is not None and px > 0:
                prices[symbol]["bybit"] = px
    except Exception as exc:
        errors.append({"source": "external_batch_bybit", "reason": type(exc).__name__})

    try:
        data = _json_url("https://www.okx.com/api/v5/market/tickers?instType=SPOT")
        rows = (data or {}).get("data") or []
        for row in rows:
            pair = str(row.get("instId") or "")
            if not pair.endswith("-USDT"):
                continue
            symbol = pair[:-5]
            px = finite(row.get("last"))
            if symbol in prices and px is not None and px > 0:
                prices[symbol]["okx"] = px
    except Exception as exc:
        errors.append({"source": "external_batch_okx", "reason": type(exc).__name__})

    try:
        pairs_data = _json_url("https://api.kraken.com/0/public/AssetPairs")
        pair_rows = (pairs_data or {}).get("result") or {}
        aliases: dict[str, str] = {}
        request_pairs: list[str] = []
        symbol_aliases = {"XBT": "BTC", "XDG": "DOGE"}
        for pair_key, row in pair_rows.items():
            wsname = str(row.get("wsname") or "")
            altname = str(row.get("altname") or pair_key)
            if "/" not in wsname:
                continue
            base, quote = wsname.split("/", 1)
            if quote not in {"USD", "USDT"}:
                continue
            symbol = symbol_aliases.get(base, base)
            if symbol not in prices:
                continue
            request_pairs.append(altname)
            aliases[pair_key] = symbol
            aliases[altname] = symbol
        for offset in range(0, len(request_pairs), 40):
            chunk = request_pairs[offset: offset + 40]
            if not chunk:
                continue
            data = _json_url(
                "https://api.kraken.com/0/public/Ticker?"
                + urllib.parse.urlencode({"pair": ",".join(chunk)})
            )
            for result_key, row in ((data or {}).get("result") or {}).items():
                symbol = aliases.get(result_key)
                if symbol is None:
                    compact = result_key.replace("X", "", 1) if result_key.startswith("X") else result_key
                    symbol = aliases.get(compact)
                close = row.get("c") or []
                px = finite(close[0]) if close else None
                if symbol in prices and px is not None and px > 0:
                    prices[symbol]["kraken"] = px
    except Exception as exc:
        errors.append({"source": "external_batch_kraken", "reason": type(exc).__name__})

    return {k: v for k, v in prices.items() if v}, errors


def build_external_sparks(
    universe_rows: list[dict[str, Any]],
    current: dict[str, dict[str, float]],
    previous: dict[str, dict[str, float]] | None,
    *,
    elapsed_seconds: float | None = None,
) -> dict[str, dict[str, Any]]:
    """Detect short external acceleration for every Bitvavo asset between cycles."""
    previous = previous or {}
    result: dict[str, dict[str, Any]] = {}
    for row in universe_rows:
        market = str(row.get("market") or "")
        symbol = base_symbol(market)
        deltas = []
        venue_deltas = {}
        for venue, px in (current.get(symbol) or {}).items():
            prior = finite((previous.get(symbol) or {}).get(venue))
            if prior is None or prior <= 0 or px <= 0:
                continue
            delta = (px / prior - 1.0) * 100.0
            venue_deltas[venue] = round(delta, 4)
            deltas.append(delta)
        med = _median(deltas)
        breadth = None if not deltas else 100.0 * sum(x > 0 for x in deltas) / len(deltas)
        max_up = max(deltas) if deltas else None
        score = 0.0
        if med is not None:
            score += min(6.0, max(0.0, med) * 8.0)
        if breadth is not None:
            score += min(2.0, max(0.0, breadth - 50.0) / 25.0)
        if max_up is not None:
            score += min(2.0, max(0.0, max_up - (med or 0.0)) * 2.0)
        cadence_valid = elapsed_seconds is not None and 60 <= elapsed_seconds <= 45 * 60
        ready = bool(
            cadence_valid
            and len(deltas) >= 2
            and (
                ((med or 0.0) >= 0.30 and (breadth or 0.0) >= 66.0)
                or ((max_up or 0.0) >= 0.75 and sum(x > 0 for x in deltas) >= 2)
            )
        )
        result[market] = {
            "mode": "FULL_UNIVERSE_BATCH_EXTERNAL_SPARK",
            "venues_observed": len(deltas),
            "elapsed_since_previous_snapshot_minutes": None if elapsed_seconds is None else round(elapsed_seconds / 60.0, 2),
            "cadence_valid_for_spark": cadence_valid,
            "venue_deltas_pct": venue_deltas,
            "median_change_since_previous_cycle_pct": None if med is None else round(med, 4),
            "breadth_positive_pct": None if breadth is None else round(breadth, 2),
            "max_change_since_previous_cycle_pct": None if max_up is None else round(max_up, 4),
            "score_0_10": round(min(10.0, score), 3),
            "ready": ready,
        }
    return result


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
    """Validate an executable plan and retain causal timing + rejected-plan detail."""
    started_ts = time.time()
    market = row["market"]

    def finish(payload: dict[str, Any], *, book_ts: float | None = None, structure_ts: float | None = None,
               book_snapshot: dict[str, Any] | None = None) -> dict[str, Any]:
        available_ts = time.time()
        return {
            **payload,
            "check_started_ts": started_ts,
            "check_started_at_utc": utc(started_ts),
            "book_observed_ts": book_ts,
            "book_observed_at_utc": None if book_ts is None else utc(book_ts),
            "structure_observed_ts": structure_ts,
            "structure_observed_at_utc": None if structure_ts is None else utc(structure_ts),
            "available_ts": available_ts,
            "available_at_utc": utc(available_ts),
            "latency_ms": round((available_ts - started_ts) * 1000.0, 2),
            "book_snapshot": book_snapshot,
        }

    if market not in metadata:
        return finish({"ready": False, "reason": "MARKET_UNAVAILABLE"})
    if finite(row.get("quote_volume_24h_eur"), 0.0) < MIN_QUOTE_VOLUME_EUR:
        return finish({"ready": False, "reason": "WAITING_EXECUTION_LIQUIDITY"})

    try:
        book = client.get("/" + market + "/book", {"depth": 25}, cache=False)
        book_ts = time.time()
        bid = finite(book["bids"][0][0]) if book.get("bids") else None
        ask = finite(book["asks"][0][0]) if book.get("asks") else None
        snapshot = {
            "best_bid_eur": bid,
            "best_ask_eur": ask,
            "asks": (book.get("asks") or [])[:25],
            "depth_levels": min(25, len(book.get("asks") or [])),
        }
        if bid is None or ask is None or not 0 < bid <= ask:
            return finish({"ready": False, "reason": "WAITING_VALID_BOOK"}, book_ts=book_ts, book_snapshot=snapshot)
        spread_pct = (ask / bid - 1.0) * 100.0
        benchmark_depth = walk_asks(book, REFERENCE_STAKE_EUR)
        if spread_pct > MAX_SPREAD_PCT:
            return finish({
                "ready": False, "reason": "WAITING_SPREAD",
                "spread_pct": round(spread_pct, 4), "depth": benchmark_depth,
            }, book_ts=book_ts, book_snapshot=snapshot)
        if not benchmark_depth.get("valid"):
            return finish({
                "ready": False, "reason": "WAITING_VISIBLE_DEPTH",
                "spread_pct": round(spread_pct, 4), "depth": benchmark_depth,
            }, book_ts=book_ts, book_snapshot=snapshot)
        if finite(benchmark_depth.get("depth_slippage_pct"), 999) > MAX_DEPTH_SLIPPAGE_PCT:
            return finish({
                "ready": False, "reason": "WAITING_DEPTH_SLIPPAGE",
                "spread_pct": round(spread_pct, 4), "depth": benchmark_depth,
            }, book_ts=book_ts, book_snapshot=snapshot)

        raw = client.get("/" + market + "/candles", {"interval": "15m", "limit": 100}, cache=False)
        structure_ts = time.time()
        features = describe(closed_candles(raw, "15m", structure_ts), "15m")
        if not features.get("valid"):
            return finish({
                "ready": False, "reason": "WAITING_VALID_STRUCTURE",
                "spread_pct": round(spread_pct, 4), "depth": benchmark_depth,
            }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)

        # Build the structural plan without hiding the R:R diagnostics. The
        # unchanged 1.5 net-R:R gate is applied explicitly below so rejected
        # plans remain inspectable by the shadow challenger.
        plan = structural_plan(
            {**row, "ask": benchmark_depth.get("vwap_eur") or ask},
            features,
            metadata[market],
            max_position_eur=REFERENCE_STAKE_EUR,
            max_trade_risk_eur=6.0,
            min_net_rr=0.0,
        )
        if not plan.get("valid"):
            return finish({
                "ready": False,
                "reason": "WAITING_" + str(plan.get("reason") or "STRUCTURAL_PLAN"),
                "spread_pct": round(spread_pct, 4),
                "depth": benchmark_depth,
                "plan": plan,
            }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)

        # Reprice the plan on the same causal book at the nominal that the risk
        # model actually proposes. This removes the previous 100 EUR-vs-smaller
        # plan inconsistency while keeping the 100 EUR depth check as a separate
        # conservative benchmark.
        proposed_stake = finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR)
        plan_depth = walk_asks(book, min(REFERENCE_STAKE_EUR, proposed_stake))
        if not plan_depth.get("valid"):
            return finish({
                "ready": False, "reason": "WAITING_VISIBLE_DEPTH",
                "spread_pct": round(spread_pct, 4), "depth": plan_depth,
                "depth_benchmark_100_eur": benchmark_depth, "plan": plan,
            }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)
        repriced = structural_plan(
            {**row, "ask": plan_depth.get("vwap_eur") or ask},
            features,
            metadata[market],
            max_position_eur=min(REFERENCE_STAKE_EUR, proposed_stake),
            max_trade_risk_eur=6.0,
            min_net_rr=0.0,
        )
        if repriced.get("valid"):
            plan = repriced

        base = {
            "spread_pct": round(spread_pct, 4),
            "depth": plan_depth,
            "depth_benchmark_100_eur": benchmark_depth,
            "plan": plan,
            "structural_range_15m_pct": finite(features.get("consolidation_range_pct")),
            "structural_features": {
                "atr14_eur": finite(features.get("atr14_eur")),
                "support_eur": finite(features.get("support_eur")),
                "consolidation_range_pct": finite(features.get("consolidation_range_pct")),
            },
        }
        if finite(plan.get("net_rr_tp1"), 0.0) < MIN_NET_RR:
            return finish({
                **base, "ready": False, "reason": "WAITING_INSUFFICIENT_NET_RISK_REWARD",
            }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)
        if finite(plan.get("stop_distance_pct"), 999) > MAX_STOP_DISTANCE_PCT:
            return finish({
                **base, "ready": False, "reason": "WAITING_STOP_GEOMETRY",
            }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)
        return finish({
            **base, "ready": True, "reason": "ENTRY_READY_SHADOW",
        }, book_ts=book_ts, structure_ts=structure_ts, book_snapshot=snapshot)
    except Exception as exc:
        return finish({"ready": False, "reason": "EXECUTION_SOURCE_ERROR", "error": type(exc).__name__})

def _event_key(event: dict[str, Any]) -> str:
    if event.get("attempt_id"):
        return str(event.get("attempt_id"))
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
    event.setdefault("architecture_version", V3_ARCHITECTURE_VERSION)
    event.setdefault("runtime_commit", RUNTIME_COMMIT)
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
    """Legacy V3 rotation shadow with plan-consistent nominal accounting."""
    rotation.setdefault("schema", "solaire_v3_rotation_shadow_v2")
    rotation.setdefault("reference_capital_eur", REFERENCE_CAPITAL_EUR)
    rotation.setdefault("reference_stake_eur", REFERENCE_STAKE_EUR)
    rotation.setdefault("cash_eur", REFERENCE_CAPITAL_EUR)
    rotation.setdefault("positions", [])
    rotation.setdefault("closed", [])
    rotation.setdefault("actions", [])
    rotation.setdefault("consumed_episodes", [])
    consumed = set(rotation["consumed_episodes"])

    def close_position(position: dict[str, Any], current: float, reason: str) -> None:
        stake = finite(position.get("stake_eur"), REFERENCE_STAKE_EUR)
        position["closed_ts"] = now
        position["closed_at_utc"] = utc(now)
        position["exit_eur"] = current
        position["close_reason"] = reason
        rotation["cash_eur"] += stake * (current / position["entry_eur"]) * (1 - 0.0035)
        rotation["closed"].append(position)
        rotation["positions"].remove(position)
        rotation["actions"].append({
            "at_utc": utc(now), "action": "CLOSE", "market": position["market"],
            "reason": reason, "stake_eur": stake, "exit_eur": current,
        })

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
            close_position(position, current, "STOP_OBSERVED_AT_V3_CYCLE")

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
            close_position(weakest, current, "ROTATE_TO_HIGHER_FORWARD_SCORE")
            rotation["actions"][-1]["to_market"] = market
            rotation["actions"][-1]["score_delta"] = round(score - finite(weakest.get("opportunity_score"), 0), 3)

        entry = finite(event.get("entry_eur"))
        stake = finite(event.get("stake_eur"), REFERENCE_STAKE_EUR)
        if entry is None or entry <= 0 or stake <= 0:
            continue
        total_debit = stake * 1.0035
        if rotation["cash_eur"] < total_debit:
            continue
        rotation["cash_eur"] -= total_debit
        rotation["positions"].append({
            "market": market,
            "episode": event.get("episode"),
            "opened_ts": now,
            "opened_at_utc": utc(now),
            "entry_eur": entry,
            "stop_eur": finite(event.get("stop_eur")),
            "stake_eur": stake,
            "theoretical_risk_eur": finite((event.get("execution") or {}).get("plan", {}).get("theoretical_loss_eur")),
            "opportunity_score": score,
            "horizon_class": event.get("horizon_class"),
        })
        rotation["actions"].append({
            "at_utc": utc(now), "action": "OPEN_SHADOW", "market": market,
            "score": score, "stake_eur": stake,
        })
        consumed.add(episode_key)

    rotation["consumed_episodes"] = sorted(consumed)[-5000:]
    marked = rotation["cash_eur"]
    for p in rotation["positions"]:
        mark = finite(p.get("mark_eur"), p.get("entry_eur"))
        entry = finite(p.get("entry_eur"))
        stake = finite(p.get("stake_eur"), REFERENCE_STAKE_EUR)
        if mark and entry:
            marked += stake * (mark / entry)
    rotation["marked_value_eur"] = round(marked, 2)
    rotation["updated_at_utc"] = utc(now)
    rotation["research_only"] = True
    rotation["nominal_accounting"] = "PLAN_STAKE_EUR"
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
    prior_architecture_version = state.get("architecture_version")
    state["architecture_version"] = V3_ARCHITECTURE_VERSION
    if prior_architecture_version != V3_ARCHITECTURE_VERSION:
        state["architecture_migrated_at_utc"] = utc(now)
        state["architecture_migrated_from"] = prior_architecture_version or "legacy-unversioned"
    state.setdefault("started_ts", now)
    state.setdefault("started_at_utc", utc(now))
    state.setdefault("markets", {})
    state.setdefault("previous_derivatives", {})
    state.setdefault("previous_external_prices", {})
    state.setdefault("execution_cursor", 0)
    state.setdefault("thesis_execution_cursor", 0)
    state.setdefault("thesis_profile_cursor", 0)
    state.setdefault("derivatives_cursor", 0)
    state.setdefault("theses", {})
    runtime_commit = RUNTIME_COMMIT
    journal.setdefault("schema", "solaire_v3_prospective_journal_v1")
    journal.setdefault("started_ts", state["started_ts"])
    journal.setdefault("started_at_utc", state["started_at_utc"])
    journal.setdefault("events", [])
    for legacy_event in journal.get("events", []):
        legacy_event.setdefault("architecture_version", "legacy-pre-v3.2-unversioned")
        legacy_event.setdefault("runtime_commit", None)

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
    dynamic_rotations = build_dynamic_rotation_context(rows)
    asset_aliases, news_mapping, alias_errors = build_full_universe_news_aliases(rows)
    source_errors.extend(alias_errors)
    news, news_errors = fetch_news(now, asset_aliases)
    source_errors.extend(news_errors)
    page_news, official_page_seen, official_page_errors = fetch_official_page_deltas(
        now,
        asset_aliases,
        state.get("official_page_seen") or {},
        initialized=bool(state.get("official_page_seen_initialized")),
    )
    state["official_page_seen"] = official_page_seen
    state["official_page_seen_initialized"] = True
    source_errors.extend(official_page_errors)
    if page_news:
        keyed = {(x.get("source"), x.get("title"), x.get("published_at_utc")): x for x in news}
        for item in page_news:
            keyed[(item.get("source"), item.get("title"), item.get("published_at_utc"))] = item
        news = sorted(keyed.values(), key=lambda x: x["published_ts"], reverse=True)

    allowed_symbols = {base_symbol(x.get("market")) for x in rows if x.get("market")}
    external_snapshot, external_batch_errors = fetch_external_price_snapshot(allowed_symbols)
    source_errors.extend(external_batch_errors)
    previous_external_ts = finite(state.get("previous_external_prices_ts"))
    elapsed_external = None if previous_external_ts is None else max(0.0, now - previous_external_ts)
    external_sparks = build_external_sparks(
        rows,
        external_snapshot,
        state.get("previous_external_prices") or {},
        elapsed_seconds=elapsed_external,
    )
    state["previous_external_prices"] = external_snapshot
    state["previous_external_prices_ts"] = now

    v2_tracking = {
        r["market"]: r
        for r in v2.get("tracking", []) or []
        if isinstance(r, dict) and r.get("market")
    }

    base_candidates = []
    for row in rows:
        market = row.get("market")
        if not market:
            continue
        quality_ok = bool((row.get("data_quality") or {}).get("ok", False))
        symbol = base_symbol(market)
        early = early_quant_evidence(row) if quality_ok else {
            "ready": False,
            "score_0_10": 0.0,
            "evidence_count": 0,
            "flags": {},
            "reason": "MARKET_DATA_NOT_STRATEGY_GRADE",
        }
        hits, news_score, news_positive_score, news_negative_score = news_for_symbol(symbol, news, now)
        sector_names = narratives_for_market(market)
        active_rotations = [
            (name, rotations.get(name) or {})
            for name in sector_names
            if (rotations.get(name) or {}).get("active_watch")
        ]
        dynamic_rotation = dynamic_rotations.get(market) or {}
        active_narratives = [x[0] for x in active_rotations]
        if dynamic_rotation.get("active_watch"):
            active_narratives.append("DYNAMIC_MOMENTUM_COHORT")
        static_rotation = max([finite(x[1].get("rotation_score_0_3"), 0) for x in active_rotations] or [0])
        raw_rotation = max(static_rotation, finite(dynamic_rotation.get("rotation_score_0_3"), 0))
        narrative_score = min(10.0, raw_rotation / 3.0 * 10.0)
        external_spark = external_sparks.get(market) or {}
        v2row = v2_tracking.get(market) or {}
        local_priority = (
            finite(early.get("score_0_10"), 0)
            + news_positive_score
            + narrative_score
            + finite(external_spark.get("score_0_10"), 0)
            + (3.0 if v2row.get("signal_state") == "CONFIRMED_ACCELERATION" else 1.5 if v2row else 0.0)
        )
        if (
            news_score > 0
            or bool(external_spark.get("ready"))
            or (quality_ok and (active_narratives or early.get("ready") or v2row))
        ):
            base_candidates.append({
                **row,
                "market_data_quality_ok": quality_ok,
                "symbol": symbol,
                "early_quant": early,
                "news_items": hits,
                "news_score": news_score,
                "news_positive_score": news_positive_score,
                "news_negative_score": news_negative_score,
                "narratives": sector_names,
                "active_narratives": active_narratives,
                "narrative_score": round(narrative_score, 3),
                "dynamic_rotation": dynamic_rotation,
                "external_spark": external_spark,
                "local_priority": round(local_priority, 3),
                "v2_state": v2row.get("signal_state"),
                "v2_score": finite(v2row.get("signal_score")),
            })

    base_candidates.sort(
        key=lambda x: (
            -int(bool((x.get("external_spark") or {}).get("ready"))),
            -finite((x.get("external_spark") or {}).get("score_0_10"), 0),
            -finite(x.get("local_priority"), 0),
        )
    )
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
            "market": row["market"], "venues_available": 0, "external_score_0_10": 0.0,
            "errors": [{"reason": "DETAILED_EXTERNAL_NOT_SELECTED_THIS_CYCLE"}],
        }
        external_score = max(
            finite(ext.get("external_score_0_10"), 0.0),
            finite((row.get("external_spark") or {}).get("score_0_10"), 0.0),
        )
        opp = score_opportunity(
            finite((row.get("early_quant") or {}).get("score_0_10"), 0),
            finite(row.get("news_positive_score"), 0),
            finite(row.get("narrative_score"), 0),
            external_score,
        )
        external_confirmed = int(ext.get("venues_available") or 0) >= 2 and finite(ext.get("external_score_0_10"), 0) >= 1.0
        external_spark_ready = bool((row.get("external_spark") or {}).get("ready"))
        context_watch = (
            finite(row.get("news_score"), 0) > 0
            or bool(row.get("active_narratives"))
            or external_confirmed
            or external_spark_ready
        )
        positive_context = (
            finite(row.get("news_positive_score"), 0) > 0
            or bool(row.get("active_narratives"))
            or external_confirmed
            or external_spark_ready
        )
        strong_negative_news = (
            finite(row.get("news_negative_score"), 0) >= 6.0
            and finite(row.get("news_negative_score"), 0) > finite(row.get("news_positive_score"), 0) + 2.0
        )
        v2_confirmed = row.get("v2_state") == "CONFIRMED_ACCELERATION"
        fresh_opportunity_trigger = (
            bool((row.get("early_quant") or {}).get("ready"))
            and positive_context
            and not strong_negative_news
        ) or v2_confirmed
        thesis_seed = bool(
            not strong_negative_news
            and (
                finite(row.get("news_positive_score"), 0) >= 4.0
                or external_spark_ready
            )
        )
        merged = {
            **row,
            "external": ext,
            "external_score": external_score,
            "opportunity_score": opp,
            "context_watch": context_watch,
            "positive_context": positive_context,
            "strong_negative_news": strong_negative_news,
            "fresh_opportunity_trigger": fresh_opportunity_trigger,
            "entry_hypothesis": fresh_opportunity_trigger,
            "thesis_seed": thesis_seed,
        }
        merged["horizon_class"] = classify_horizon(merged)
        candidates.append(merged)

    candidates.sort(key=lambda x: x["opportunity_score"], reverse=True)

    # Sixth V3 research axis: persistent opportunity theses.  This runs on
    # a separate observation set so the frozen V3 candidate stream consumed by
    # V3.1 is not widened or re-ranked.
    candidate_by_market = {x["market"]: x for x in candidates}
    universe_by_market_thesis = {x.get("market"): x for x in rows if x.get("market")}
    active_thesis_markets = {
        market for market, thesis in (state.get("theses") or {}).items()
        if thesis.get("active")
    }
    seeded_thesis_markets = {
        x["market"] for x in candidates if x.get("thesis_seed")
    }
    thesis_markets = sorted(active_thesis_markets | seeded_thesis_markets)

    thesis_observations: list[dict[str, Any]] = []
    for market in thesis_markets:
        current = candidate_by_market.get(market)
        if current is not None:
            obs = dict(current)
        else:
            raw = universe_by_market_thesis.get(market)
            if not raw or not (raw.get("data_quality") or {}).get("ok", False):
                continue
            symbol = base_symbol(market)
            early = early_quant_evidence(raw)
            hits, news_score, news_positive_score, news_negative_score = news_for_symbol(symbol, news, now)
            sector_names = narratives_for_market(market)
            active_rotations = [
                (name, rotations.get(name) or {})
                for name in sector_names
                if (rotations.get(name) or {}).get("active_watch")
            ]
            dynamic_rotation = dynamic_rotations.get(market) or {}
            active_narratives = [x[0] for x in active_rotations]
            if dynamic_rotation.get("active_watch"):
                active_narratives.append("DYNAMIC_MOMENTUM_COHORT")
            static_rotation = max([finite(x[1].get("rotation_score_0_3"), 0) for x in active_rotations] or [0])
            raw_rotation = max(static_rotation, finite(dynamic_rotation.get("rotation_score_0_3"), 0))
            narrative_score = min(10.0, raw_rotation / 3.0 * 10.0)
            v2row = v2_tracking.get(market) or {}
            prior = (state.get("theses") or {}).get(market) or {}
            external_spark = external_sparks.get(market) or {}
            obs = {
                **raw,
                "symbol": symbol,
                "early_quant": early,
                "news_items": hits,
                "news_score": news_score,
                "news_positive_score": news_positive_score,
                "news_negative_score": news_negative_score,
                "narratives": sector_names,
                "active_narratives": active_narratives,
                "narrative_score": round(narrative_score, 3),
                "dynamic_rotation": dynamic_rotation,
                "external_spark": external_spark,
                "external": {"venues_available": 0, "external_score_0_10": 0.0, "reason": "THESIS_ONLY_NO_DETAILED_EXTERNAL_QUERY"},
                "external_score": finite(external_spark.get("score_0_10"), 0),
                "opportunity_score": finite(prior.get("best_opportunity_score"), 0.0),
                "context_watch": bool(news_score > 0 or active_narratives or external_spark.get("ready")),
                "fresh_opportunity_trigger": False,
                "entry_hypothesis": False,
                "thesis_seed": False,
                "v2_state": v2row.get("signal_state"),
                "v2_score": finite(v2row.get("signal_score")),
            }
            obs["horizon_class"] = classify_horizon(obs)
        thesis_observations.append(obs)

    thesis_observations.sort(
        key=lambda x: (
            0 if x.get("fresh_opportunity_trigger") else 1,
            -finite(x.get("opportunity_score"), 0),
        )
    )
    long_trend_profiles: dict[str, dict[str, Any]] = {}
    profile_rows, state["thesis_profile_cursor"], thesis_profile_fairness = select_fair_batch(
        thesis_observations,
        MAX_THESIS_PROFILE_MARKETS,
        state.get("thesis_profile_cursor", 0),
        key=lambda x: x.get("market") or "",
    )
    if profile_rows:
        try:
            trend_client = PublicClient(timeout=8, retries=2, requests_per_second=8)
            long_trend_profiles, trend_errors = fetch_long_trend_profiles(
                trend_client,
                [x["market"] for x in profile_rows],
                now,
            )
            source_errors.extend(trend_errors)
        except Exception as exc:
            source_errors.append({"source": "long_trend", "reason": type(exc).__name__})

    for obs in thesis_observations:
        market = obs["market"]
        prior = (state.get("theses") or {}).get(market) or {}
        long_trend = long_trend_profiles.get(market) or prior.get("last_long_trend") or {}
        obs["long_trend"] = long_trend
        prior_state = prior.get("state")
        prior_active = bool(prior.get("active"))
        thesis = advance_persistent_thesis(prior, obs, now)
        if thesis:
            state["theses"][market] = thesis
        obs["persistent_thesis"] = thesis or {}
        obs["thesis_reentry_hypothesis"] = bool(
            thesis.get("active") and thesis.get("state") == "REENTRY_READY_THESIS"
        )
        if market in candidate_by_market:
            candidate_by_market[market]["long_trend"] = long_trend
            candidate_by_market[market]["persistent_thesis"] = thesis or {}
            candidate_by_market[market]["thesis_reentry_hypothesis"] = obs["thesis_reentry_hypothesis"]
            candidate_by_market[market]["thesis_execution"] = None
            candidate_by_market[market]["thesis_last_execution"] = (thesis or {}).get("last_execution")
        elif obs["thesis_reentry_hypothesis"]:
            # A persistent thesis re-entry must rejoin the main candidate stream
            # even when the original short-lived trigger/news has disappeared.
            promoted = {
                **obs,
                "persistent_thesis": thesis or {},
                "thesis_reentry_hypothesis": True,
                "thesis_execution": None,
                "thesis_last_execution": (thesis or {}).get("last_execution"),
                "entry_hypothesis": False,
                "candidate_source": "PERSISTENT_THESIS_REENTRY",
            }
            candidates.append(promoted)
            candidate_by_market[market] = promoted

        opened = bool(thesis.get("active")) and not prior_active
        if opened:
            _append_event(journal, {
                "event_type": "OPPORTUNITY_THESIS_START",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(obs.get("price_eur")),
                "opportunity_score": obs.get("opportunity_score"),
                "horizon_class": obs.get("horizon_class"),
                "long_trend": long_trend,
                "early_quant": obs.get("early_quant"),
                "context": {
                    "news_score": obs.get("news_score"),
                    "active_narratives": obs.get("active_narratives"),
                    "narrative_score": obs.get("narrative_score"),
                    "external": obs.get("external"),
                },
                "v2_state_at_event": obs.get("v2_state"),
                "left_censored_at_v3_t0": initial_v3_cycle,
                "evaluations": {},
            })

        if (
            thesis.get("active")
            and thesis.get("state") == "REENTRY_READY_THESIS"
            and prior_state != "REENTRY_READY_THESIS"
        ):
            _append_event(journal, {
                "event_type": "OPPORTUNITY_THESIS_REENTRY_READY",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(obs.get("price_eur")),
                "opportunity_score": obs.get("opportunity_score"),
                "horizon_class": obs.get("horizon_class"),
                "long_trend": long_trend,
                "thesis": thesis,
                "v2_state_at_event": obs.get("v2_state"),
                "left_censored_at_v3_t0": False,
                "evaluations": {},
            })

    candidates.sort(key=lambda x: finite(x.get("opportunity_score"), 0), reverse=True)

    # Expensive diagnostics use a fair queue: bounded work is acceptable,
    # permanent starvation is not.
    derivative_rows, state["derivatives_cursor"], derivatives_fairness = select_fair_batch(
        candidates,
        MAX_DERIVATIVE_MARKETS,
        state.get("derivatives_cursor", 0),
        key=lambda x: x.get("market") or "",
    )
    for row in derivative_rows:
        prev = finite((state.get("previous_derivatives") or {}).get(row["market"]))
        derivative = bybit_derivatives(row["symbol"], prev)
        row["derivatives"] = derivative
        oi = finite(derivative.get("open_interest"))
        if oi is not None:
            state["previous_derivatives"][row["market"]] = oi

    execution_eligible = [x for x in candidates if x.get("entry_hypothesis")]
    execution_rows, state["execution_cursor"], execution_fairness = select_priority_fair_batch(
        execution_eligible,
        MAX_EXECUTION_MARKETS,
        state.get("execution_cursor", 0),
        priority_count=min(8, MAX_EXECUTION_MARKETS),
        priority_key=lambda x: (
            int(x.get("v2_state") == "CONFIRMED_ACCELERATION"),
            finite(x.get("opportunity_score"), 0),
        ),
        key=lambda x: x.get("market") or "",
    )

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

    # Re-entry theses are now a first-class upstream path for V3.1.  The
    # bounded execution workload rotates fairly so an ONDO-like candidate can
    # never remain 40th forever behind a fixed top-N slice.
    thesis_execution_eligible = [
        x for x in thesis_observations if x.get("thesis_reentry_hypothesis")
    ]
    thesis_execution_rows, state["thesis_execution_cursor"], thesis_execution_fairness = select_priority_fair_batch(
        thesis_execution_eligible,
        MAX_THESIS_EXECUTION_MARKETS,
        state.get("thesis_execution_cursor", 0),
        priority_count=min(8, MAX_THESIS_EXECUTION_MARKETS),
        priority_key=lambda x: (
            int(((x.get("persistent_thesis") or {}).get("last_execution_state")) == "ENTRY_READY_SHADOW"),
            finite(x.get("opportunity_score"), 0),
            finite(((x.get("persistent_thesis") or {}).get("return_from_open_pct")), 0),
        ),
        key=lambda x: x.get("market") or "",
    )
    thesis_checks: dict[str, dict[str, Any]] = {}
    if metadata:
        for obs in thesis_execution_rows:
            thesis_checks[obs["market"]] = execution_check(client, metadata, obs, time.time())

    new_thesis_entry_events = []
    for obs in thesis_execution_rows:
        market = obs["market"]
        check = thesis_checks.get(market)
        thesis = (state.get("theses") or {}).get(market) or {}
        if check is None:
            continue
        thesis["last_execution_state"] = check.get("reason")
        thesis["last_execution_checked_at_utc"] = utc(now)
        thesis["last_execution"] = check
        if market in candidate_by_market:
            candidate_by_market[market]["thesis_execution"] = check
            candidate_by_market[market]["thesis_reentry_hypothesis"] = True
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
                "price_eur": finite(obs.get("price_eur")),
                "entry_eur": finite(plan.get("entry_eur")),
                "stop_eur": finite(plan.get("stop_eur")),
                "tp1_eur": finite(plan.get("tp1_eur")),
                "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
                "opportunity_score": obs.get("opportunity_score"),
                "horizon_class": obs.get("horizon_class"),
                "entry_source": "V3_PERSISTENT_THESIS_REENTRY",
                "execution": check,
                "long_trend": obs.get("long_trend"),
                "thesis": thesis,
                "v2_state_at_event": obs.get("v2_state"),
                "left_censored_at_v3_t0": False,
                "evaluations": {},
            }
            if _append_event(journal, event):
                thesis["entry_recorded_thesis_id"] = thesis_id
                new_thesis_entry_events.append(event)

    current_markets = set()
    new_entry_events = []
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
            ms["opportunity_recovery"] = {"episode": ms["episode"]}
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

        if row.get("entry_hypothesis"):
            recovery = ms.setdefault("opportunity_recovery", {"episode": ms["episode"]})
            if recovery.get("episode") != ms["episode"]:
                recovery.clear()
                recovery["episode"] = ms["episode"]
            if recovery.get("first_opportunity_ts") is None:
                recovery["first_opportunity_ts"] = now
                recovery["first_opportunity_at_utc"] = utc(now)
                recovery["first_opportunity_price_eur"] = finite(row.get("price_eur"))
                recovery["first_opportunity_definition"] = "FIRST_V3_ENTRY_HYPOTHESIS"
                first_event = {
                    "event_type": "FIRST_OPPORTUNITY_OBSERVED",
                    "market": market,
                    "episode": ms["episode"],
                    "attempt_id": f"{market}|{ms['episode']}|FIRST_OPPORTUNITY",
                    "decision_ts": now,
                    "decision_at_utc": utc(now),
                    "price_eur": finite(row.get("price_eur")),
                    "opportunity_score": row.get("opportunity_score"),
                    "horizon_class": row.get("horizon_class"),
                    "evaluation_excluded": True,
                    "left_censored_at_v3_t0": initial_v3_cycle,
                }
                _append_event(journal, first_event)

        check = checks.get(market)
        if row.get("entry_hypothesis") and check is not None:
            ms["execution_state"] = check.get("reason")
            ms["execution_checked_at_utc"] = check.get("available_at_utc") or utc(now)

            recovery = ms.setdefault("opportunity_recovery", {"episode": ms["episode"]})
            if recovery.get("episode") != ms["episode"]:
                recovery.clear()
                recovery["episode"] = ms["episode"]
            if recovery.get("first_opportunity_ts") is None:
                recovery["first_opportunity_ts"] = now
                recovery["first_opportunity_at_utc"] = utc(now)
                recovery["first_opportunity_price_eur"] = finite(row.get("price_eur"))
                recovery["first_opportunity_definition"] = "FIRST_V3_ENTRY_HYPOTHESIS"

            gate_signature = "|".join([
                "READY" if check.get("ready") else "REJECTED",
                str(check.get("reason") or ""),
            ])
            if ms.get("last_execution_gate_signature") != gate_signature:
                ms["execution_gate_sequence"] = int(ms.get("execution_gate_sequence", 0)) + 1
                gate_ts = finite(check.get("available_ts"), now)
                gate_event = {
                    "event_type": "EXECUTION_GATE_OBSERVATION",
                    "market": market,
                    "episode": ms["episode"],
                    "attempt_id": f"{market}|{ms['episode']}|GATE|{ms['execution_gate_sequence']}",
                    "decision_ts": gate_ts,
                    "decision_at_utc": utc(gate_ts),
                    "price_eur": finite(row.get("price_eur")),
                    "ready": bool(check.get("ready")),
                    "gate_reason": check.get("reason"),
                    "execution": check,
                    "plan": check.get("plan"),
                    "gate_vector": {
                        "spread_pct": check.get("spread_pct"),
                        "depth": check.get("depth"),
                        "stop_distance_pct": finite((check.get("plan") or {}).get("stop_distance_pct")),
                        "net_rr_tp1": finite((check.get("plan") or {}).get("net_rr_tp1")),
                    },
                    "evaluation_excluded": True,
                    "left_censored_at_v3_t0": initial_v3_cycle,
                }
                _append_event(journal, gate_event)
                ms["last_execution_gate_signature"] = gate_signature

            if check.get("ready") and recovery.get("first_executable_ts") is None:
                plan = check.get("plan") or {}
                executable_ts = finite(check.get("available_ts"), now)
                executable_entry = finite(plan.get("entry_eur"))
                first_price = finite(recovery.get("first_opportunity_price_eur"))
                movement = None
                if executable_entry is not None and first_price is not None and first_price > 0:
                    movement = (executable_entry / first_price - 1.0) * 100.0
                residual_to_tp1 = None
                tp1 = finite(plan.get("tp1_eur"))
                if executable_entry is not None and executable_entry > 0 and tp1 is not None:
                    residual_to_tp1 = (tp1 / executable_entry - 1.0) * 100.0
                recovery.update({
                    "first_executable_ts": executable_ts,
                    "first_executable_at_utc": utc(executable_ts),
                    "first_executable_entry_eur": executable_entry,
                    "delay_seconds": executable_ts - finite(recovery.get("first_opportunity_ts"), executable_ts),
                    "movement_consumed_pct": movement,
                    "structural_residual_to_tp1_pct": residual_to_tp1,
                })
                recovery_event = {
                    "event_type": "OPPORTUNITY_RECOVERY_EXECUTABLE",
                    "market": market,
                    "episode": ms["episode"],
                    "decision_ts": executable_ts,
                    "decision_at_utc": utc(executable_ts),
                    "price_eur": finite(row.get("price_eur")),
                    "entry_eur": executable_entry,
                    "stop_eur": finite(plan.get("stop_eur")),
                    "tp1_eur": tp1,
                    "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
                    "recovery": dict(recovery),
                    "execution": check,
                    "left_censored_at_v3_t0": initial_v3_cycle,
                    "evaluations": {},
                }
                _append_event(journal, recovery_event)

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
                            "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
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
                            "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
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
                    "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
                    "execution": check,
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
                    "stake_eur": finite(plan.get("stake_eur"), REFERENCE_STAKE_EUR),
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
    journal["architecture_version"] = V3_ARCHITECTURE_VERSION
    journal["runtime_commit"] = runtime_commit
    journal["events"] = journal["events"][-10000:]

    compact_candidates = []
    for row in candidates:
        compact_candidates.append({
            "market": row["market"],
            "price_eur": row.get("price_eur"),
            "change_24h_pct": row.get("change_24h_pct"),
            "quote_volume_24h_eur": row.get("quote_volume_24h_eur"),
            "opportunity_score": row.get("opportunity_score"),
            "horizon_class": row.get("horizon_class"),
            "context_watch": row.get("context_watch"),
            "entry_hypothesis": row.get("entry_hypothesis"),
            "early_quant": row.get("early_quant"),
            "market_data_quality_ok": row.get("market_data_quality_ok"),
            "news_score": row.get("news_score"),
            "news_positive_score": row.get("news_positive_score"),
            "news_negative_score": row.get("news_negative_score"),
            "news_items": row.get("news_items"),
            "active_narratives": row.get("active_narratives"),
            "narrative_score": row.get("narrative_score"),
            "dynamic_rotation": row.get("dynamic_rotation"),
            "external_spark": row.get("external_spark"),
            "external": row.get("external"),
            "external_score": finite((row.get("external") or {}).get("external_score_0_10")),
            "strong_negative_news": row.get("strong_negative_news"),
            "thesis_seed": row.get("thesis_seed"),
            "persistent_thesis": row.get("persistent_thesis"),
            "thesis_reentry_hypothesis": row.get("thesis_reentry_hypothesis"),
            "thesis_execution": row.get("thesis_execution"),
            "thesis_last_execution": row.get("thesis_last_execution"),
            "derivatives": row.get("derivatives"),
            "v2_state": row.get("v2_state"),
            "v2_score": row.get("v2_score"),
            "execution": checks.get(row["market"]),
            "timing_state": (state.get("markets", {}).get(row["market"], {}) or {}).get("timing"),
        })

    candidate_doc = {
        "schema": "solaire_v3_candidates_v1",
        "generated_at_utc": utc(now),
        "architecture_version": V3_ARCHITECTURE_VERSION,
        "runtime_commit": runtime_commit,
        "research_only": True,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "narrative_rotations": rotations,
        "dynamic_rotation_mode": "DYNAMIC_FULL_UNIVERSE_MOMENTUM_COHORT",
        "news_items_considered": len(news),
        "news_mapping": news_mapping,
        "candidates": compact_candidates,
    }

    thesis_doc = {
        "schema": "solaire_v3_persistent_theses_v1",
        "generated_at_utc": utc(now),
        "architecture_version": V3_ARCHITECTURE_VERSION,
        "runtime_commit": runtime_commit,
        "research_only": True,
        "affects_v2": False,
        "affects_v3_candidate_selection": True,
        "affects_v31": True,
        "affects_email": False,
        "orders_submitted": False,
        "max_profile_markets": MAX_THESIS_PROFILE_MARKETS,
        "observations": [
            {
                "market": obs.get("market"),
                "price_eur": obs.get("price_eur"),
                "opportunity_score": obs.get("opportunity_score"),
                "horizon_class": obs.get("horizon_class"),
                "fresh_opportunity_trigger": obs.get("fresh_opportunity_trigger"),
                "long_trend": obs.get("long_trend"),
                "persistent_thesis": obs.get("persistent_thesis"),
                "thesis_reentry_hypothesis": obs.get("thesis_reentry_hypothesis"),
                "execution": thesis_checks.get(obs.get("market")),
            }
            for obs in thesis_observations
        ],
    }
    status = {
        "schema": "solaire_v3_status_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_NONBLOCKING" if critical_error else ("OK_WITH_SOURCE_GAPS" if source_errors else "OK"),
        "mode": "PROSPECTIVE_SHADOW",
        "architecture_version": V3_ARCHITECTURE_VERSION,
        "runtime_commit": runtime_commit,
        "research_only": True,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
        "frozen_v2_commit": FROZEN_V2_COMMIT,
        "universe_rows": len(rows),
        "context_news_items": len(news),
        "news_mapping_mode": news_mapping.get("mode"),
        "news_universe_symbols": news_mapping.get("universe_symbols"),
        "news_ticker_coverage_symbols": news_mapping.get("ticker_coverage_symbols"),
        "news_named_alias_symbols": news_mapping.get("named_alias_symbols"),
        "news_named_alias_coverage_pct": news_mapping.get("named_alias_coverage_pct"),
        "candidate_count": len(candidates),
        "external_batch_universe_symbols": len(external_snapshot),
        "external_spark_count": sum(bool((x.get("external_spark") or {}).get("ready")) for x in candidates),
        "dynamic_rotation_active_count": sum(bool((x.get("dynamic_rotation") or {}).get("active_watch")) for x in candidates),
        "context_watch_count": sum(bool(x.get("context_watch")) for x in candidates),
        "entry_hypothesis_count": sum(bool(x.get("entry_hypothesis")) for x in candidates),
        "thesis_reentry_hypothesis_count": sum(bool(x.get("thesis_reentry_hypothesis")) for x in thesis_observations),
        "execution_checks": len(checks),
        "execution_fairness": execution_fairness,
        "thesis_execution_fairness": thesis_execution_fairness,
        "thesis_profile_fairness": thesis_profile_fairness,
        "derivatives_fairness": derivatives_fairness,
        "entry_ready_shadow_count": sum(
            bool(checks.get(x["market"], {}).get("ready"))
            for x in candidates if x.get("entry_hypothesis")
        ),
        "thesis_reentry_execution_ready_count": sum(bool(x.get("ready")) for x in thesis_checks.values()),
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
    atomic_json(THESES, thesis_doc)
    atomic_json(ROTATION, rotation)
    atomic_json(V2_BENCHMARK, benchmark)
    atomic_json(STATUS, status)
    print("SOLAIRE_V3 " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
