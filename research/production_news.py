"""Production NEWS signal for Solaire.

Fresh public crypto news is fetched on every production heartbeat. A material
headline can create an early NEWS_WATCH before price acceleration appears.
NEWS is intentionally unable to authorize a BUY on its own: market confirmation
and the normal execution gate remain mandatory.
"""
from __future__ import annotations

import hashlib
import html
import re
import time
import unicodedata
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.request import Request, urlopen

NEWS_LOOKBACK_SECONDS = 18 * 3600
NEWS_WATCH_MIN = 6.5
NEWS_WEIGHT = 0.35
MAX_ITEMS_PER_SOURCE = 80
FETCH_TIMEOUT_SECONDS = 8

SOURCES = (
    ("JOURNAL_DU_COIN", "https://journalducoin.com/feed/", 1.00),
    ("COINDESK", "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml", 1.00),
    ("DECRYPT", "https://decrypt.co/feed", 0.95),
    ("COINTELEGRAPH", "https://cointelegraph.com/rss", 0.90),
)

# Project/name aliases for symbols whose ticker alone is insufficient or ambiguous.
# The generic ticker itself is also matched case-sensitively in headlines/bodies.
ALIASES = {
    "ETHFI": ("ether.fi", "etherfi", "ether fi"),
    "AAVE": ("aave",),
    "ONDO": ("ondo finance", "ondo"),
    "SKY": ("sky ecosystem", "makerdao", "maker protocol"),
    "PUMP": ("pump.fun", "pumpfun", "pump fun"),
    "ENA": ("ethena",),
    "MORPHO": ("morpho",),
    "FLUID": ("fluid protocol", "instadapp"),
    "CVX": ("convex finance",),
    "PENDLE": ("pendle",),
    "SYRUP": ("maple finance", "syrup"),
    "COMP": ("compound finance",),
    "GMX": ("gmx",),
    "VTHO": ("vechainthor", "vtho"),
    "VET": ("vechain",),
    "SEI": ("sei network",),
    "KAS": ("kaspa",),
    "LINK": ("chainlink",),
    "VIRTUAL": ("virtuals protocol", "virtuals"),
    "SAND": ("the sandbox",),
    "XTZ": ("tezos",),
    "INJ": ("injective",),
    "ARB": ("arbitrum",),
    "OP": ("optimism",),
    "TIA": ("celestia",),
}

POSITIVE_GROUPS = (
    ("LAUNCH", (" launch", "launches", "launched", "lance", "lancement", "dévoile", "unveils")),
    ("PARTNERSHIP", ("partnership", "partners with", "partenariat", "collaboration")),
    ("INTEGRATION", ("integration", "integrates", "intègre", "powered by", "infrastructure")),
    ("LISTING", ("listing", "listed on", "liste ", "coté", "cotation")),
    ("TOKENOMICS", ("buyback", "rachat", "burn", "brûl", "tokenomics")),
    ("GROWTH", ("tvl", "deposits", "dépôts", "revenue", "revenus", "milestone", "record")),
    ("INSTITUTIONAL", ("treasury", "trésorerie", "institutional", "blackrock", "allocation")),
    ("PRODUCT", ("stablecoin", "mainnet", "collateral", "collatéral", "credit", "carte", "card")),
    ("REGULATORY_POSITIVE", ("approved", "approval", "approuvé", "licence", "license")),
)

NEGATIVE_GROUPS = (
    ("SECURITY", ("hack", "exploit", "breach", "attaque", "pirat")),
    ("DELIST", ("delist", "delisting", "retiré de la cote", "retrait de cotation")),
    ("SHUTDOWN", ("shutdown", "wind-down", "fermeture", "cessation")),
    ("REGULATORY_NEGATIVE", ("lawsuit", "procès", "ban", "interdiction", "sanction")),
    ("SOLVENCY", ("insolven", "bankrupt", "faillite", "default", "défaut")),
)


def _plain(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", value).strip().lower()


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _child_text(node: ET.Element, names: set[str]) -> str:
    for child in node.iter():
        if _local(child.tag) in names and (child.text or "").strip():
            return (child.text or "").strip()
    return ""


def _link(node: ET.Element) -> str:
    for child in node.iter():
        if _local(child.tag) != "link":
            continue
        href = (child.attrib or {}).get("href")
        if href:
            return href
        if (child.text or "").strip():
            return (child.text or "").strip()
    return ""


def _published_ts(value: str) -> float | None:
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except Exception:
        pass
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except Exception:
        return None


def parse_feed(payload: bytes, source: str) -> list[dict[str, Any]]:
    root = ET.fromstring(payload)
    nodes = [n for n in root.iter() if _local(n.tag) in {"item", "entry"}]
    rows = []
    for node in nodes[:MAX_ITEMS_PER_SOURCE]:
        title = _child_text(node, {"title"})
        description = _child_text(node, {"description", "summary", "content"})
        published = _child_text(node, {"pubdate", "published", "updated", "date"})
        link = _link(node)
        if not title:
            continue
        fingerprint = hashlib.sha256(
            (source + "\n" + title.strip().lower() + "\n" + link).encode("utf-8")
        ).hexdigest()[:20]
        rows.append(
            {
                "id": fingerprint,
                "source": source,
                "title": title.strip(),
                "description": description.strip(),
                "url": link,
                "published_at_utc": (
                    datetime.fromtimestamp(_published_ts(published), timezone.utc).isoformat()
                    if _published_ts(published) is not None
                    else None
                ),
                "published_ts": _published_ts(published),
            }
        )
    return rows


def _fetch_source(source: tuple[str, str, float]) -> tuple[str, float, list[dict], str | None]:
    name, url, weight = source
    try:
        req = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 SolaireNews/1.0",
                "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
            },
        )
        with urlopen(req, timeout=FETCH_TIMEOUT_SECONDS) as response:
            payload = response.read(2_000_000)
        return name, weight, parse_feed(payload, name), None
    except Exception as exc:
        return name, weight, [], f"{type(exc).__name__}: {exc}"


def _market_match(raw_text: str, normalized: str, base: str) -> bool:
    # Explicit ticker mention is strong and case-sensitive enough to avoid many
    # common-word collisions (e.g. LINK, SAND).
    if re.search(rf"(?<![A-Z0-9]){re.escape(base)}(?![A-Z0-9])", raw_text):
        return True
    for alias in ALIASES.get(base, ()):
        if _plain(alias) in normalized:
            return True
    return False


def _classify(text: str, age_seconds: float, source_weight: float) -> tuple[float, str, list[str]]:
    normalized = _plain(text)
    positive = [label for label, terms in POSITIVE_GROUPS if any(term in normalized for term in terms)]
    negative = [label for label, terms in NEGATIVE_GROUPS if any(term in normalized for term in terms)]

    if positive and not negative:
        direction = "POSITIVE"
        groups = positive
    elif negative and not positive:
        direction = "NEGATIVE"
        groups = negative
    elif positive or negative:
        direction = "MIXED"
        groups = positive + negative
    else:
        direction = "NEUTRAL"
        groups = []

    score = 4.5 + 1.15 * len(set(groups))
    if age_seconds <= 2 * 3600:
        score += 1.0
    elif age_seconds <= 6 * 3600:
        score += 0.5
    elif age_seconds > 12 * 3600:
        score -= 1.0
    score *= source_weight
    return round(max(0.0, min(10.0, score)), 3), direction, sorted(set(groups))


def collect_news_context(markets: list[dict], now_ts: float | None = None) -> dict[str, Any]:
    now_ts = time.time() if now_ts is None else now_ts
    fetched: list[tuple[str, float, list[dict], str | None]] = []
    with ThreadPoolExecutor(max_workers=len(SOURCES)) as pool:
        futures = [pool.submit(_fetch_source, source) for source in SOURCES]
        for future in as_completed(futures):
            fetched.append(future.result())

    source_status = []
    items = []
    weights = {}
    for name, weight, rows, error in fetched:
        weights[name] = weight
        source_status.append(
            {"source": name, "ok": error is None, "items": len(rows), "error": error}
        )
        items.extend(rows)

    active = []
    seen = set()
    for item in items:
        if item["id"] in seen:
            continue
        seen.add(item["id"])
        published_ts = item.get("published_ts")
        if published_ts is None:
            # Unknown publication time is useful context, but must not create an
            # early watch because temporal causality is unknown.
            continue
        age = now_ts - published_ts
        if age < -300 or age > NEWS_LOOKBACK_SECONDS:
            continue
        active.append((item, max(0.0, age)))

    by_market: dict[str, dict[str, Any]] = {}
    for meta in markets:
        market = str(meta.get("market") or "")
        base = str(meta.get("base") or market.split("-", 1)[0]).upper()
        if not market or not base:
            continue
        matches = []
        for item, age in active:
            raw_text = f"{item.get('title','')} {item.get('description','')}"
            normalized = _plain(raw_text)
            if not _market_match(raw_text, normalized, base):
                continue
            score, direction, groups = _classify(
                raw_text, age, weights.get(item["source"], 0.9)
            )
            matches.append(
                {
                    "news_id": item["id"],
                    "source": item["source"],
                    "title": item["title"],
                    "url": item.get("url"),
                    "published_at_utc": item.get("published_at_utc"),
                    "age_minutes": round(age / 60.0, 1),
                    "score": score,
                    "direction": direction,
                    "categories": groups,
                }
            )
        if not matches:
            continue
        matches.sort(key=lambda row: (row["score"], -row["age_minutes"]), reverse=True)
        top = matches[0]
        by_market[market] = {
            "score": top["score"],
            "direction": top["direction"],
            "watch_trigger": top["score"] >= NEWS_WATCH_MIN,
            "weight_in_composite": NEWS_WEIGHT,
            "top": top,
            "items": matches[:5],
        }

    return {
        "schema": "solaire_production_news_v1",
        "generated_at_utc": datetime.fromtimestamp(now_ts, timezone.utc).isoformat(),
        "lookback_hours": NEWS_LOOKBACK_SECONDS / 3600,
        "news_weight": NEWS_WEIGHT,
        "news_watch_min": NEWS_WATCH_MIN,
        "sources": sorted(source_status, key=lambda row: row["source"]),
        "items_with_known_recent_time": len(active),
        "markets": by_market,
    }


def composite_score(quant_score: Any, news: dict[str, Any] | None) -> float:
    try:
        quant = max(0.0, min(10.0, float(quant_score)))
    except (TypeError, ValueError):
        quant = 0.0
    news = news or {}
    try:
        news_score = max(0.0, min(10.0, float(news.get("score", 0.0))))
    except (TypeError, ValueError):
        news_score = 0.0
    direction = news.get("direction")
    if direction == "POSITIVE":
        # NEWS can contribute up to 35% of the final note but never penalises a
        # strong quant setup merely because no catalyst was found.
        result = quant + NEWS_WEIGHT * max(0.0, news_score - quant)
    elif direction == "NEGATIVE":
        # Material negative news can cut the long score by up to 35%.
        result = quant * (1.0 - NEWS_WEIGHT * news_score / 10.0)
    else:
        result = quant
    return round(max(0.0, min(10.0, result)), 3)
