"""Production NEWS signal for Solaire.

Priority:
1. official project sources (website/blog/forum/X);
2. official partner/project sources mentioning the asset;
3. crypto media feeds as a fallback.

A material NEWS item can open NEWS_WATCH before price acceleration. NEWS is a
material part of scoring but cannot authorize a BUY by itself.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import time
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

NEWS_LOOKBACK_SECONDS = 18 * 3600
CATALYST_LOOKBACK_SECONDS = 7 * 24 * 3600
NEWS_WATCH_MIN = 6.5
CATALYST_PREWATCH_MIN = 6.5
NEWS_WEIGHT = 0.35
CATALYST_WEIGHT = 0.20
MAX_ITEMS_PER_SOURCE = 80
FETCH_TIMEOUT_SECONDS = 5
OFFICIAL_POLL_LIMIT = 160
OFFICIAL_WORKERS = 32
X_HANDLES_PER_CYCLE = 500
X_HANDLES_PER_QUERY = 20

REGISTRY_PATH = Path("official_source_registry.json")
OFFICIAL_STATE_PATH = Path("production_official_news_state.json")

SOURCES = (
    ("JOURNAL_DU_COIN", "https://journalducoin.com/feed/", 1.00, "media"),
    ("COINDESK", "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml", 1.00, "media"),
    ("DECRYPT", "https://decrypt.co/feed", 0.95, "media"),
    ("COINTELEGRAPH", "https://cointelegraph.com/rss", 0.90, "media"),
)

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
    ("LAUNCH", (" launch", "launches", "launched", "lance", "lancement", "devoile", "unveils", "introducing")),
    ("PARTNERSHIP", ("partnership", "partners with", "partenariat", "collaboration")),
    ("INTEGRATION", ("integration", "integrates", "integre", "powered by", "infrastructure")),
    ("LISTING", ("listing", "listed on", "liste ", "cote", "cotation")),
    ("TOKENOMICS", ("buyback", "rachat", "burn", "brul", "tokenomics")),
    ("GROWTH", ("tvl", "deposits", "depots", "revenue", "revenus", "milestone", "record")),
    ("INSTITUTIONAL", ("treasury", "tresorerie", "institutional", "blackrock", "allocation")),
    ("PRODUCT", ("stablecoin", "mainnet", "collateral", "collateral", "credit", "carte", "card")),
    ("REGULATORY_POSITIVE", ("approved", "approval", "approuve", "licence", "license")),
)

NEGATIVE_GROUPS = (
    ("SECURITY", ("hack", "exploit", "breach", "attaque", "pirat")),
    ("DELIST", ("delist", "delisting", "retire de la cote", "retrait de cotation")),
    ("SHUTDOWN", ("shutdown", "wind-down", "fermeture", "cessation")),
    ("REGULATORY_NEGATIVE", ("lawsuit", "proces", "ban", "interdiction", "sanction")),
    ("SOLVENCY", ("insolven", "bankrupt", "faillite", "default", "defaut")),
)

CATALYST_LEVEL_3 = (
    "tomorrow", "demain", "later today", "ce soir", "cet apres-midi",
    "in a few hours", "dans quelques heures", "in 1 hour", "in 2 hours",
    "in 3 hours", "in 4 hours", "countdown", "goes live today",
    "launching today", "launching tomorrow", "announcement tomorrow",
    "annonce demain", "lancement demain",
)
CATALYST_LEVEL_2 = (
    "coming soon", "bientot", "this week", "cette semaine", "next week",
    "la semaine prochaine", "stay tuned", "restez connectes", "upcoming",
    "will announce", "will launch", "we are launching", "prepare for",
    "save the date", "vote ends", "voting ends", "proposal ends",
    "mainnet soon", "testnet soon", "launch soon", "announcement soon",
)
CATALYST_LEVEL_1 = (
    "roadmap", "planned", "we plan to", "will support", "future support",
    "next phase", "coming months", "prochains mois", "a venir",
    "native stablecoin support", "future integration",
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
        published_ts = _published_ts(published)
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
                    datetime.fromtimestamp(published_ts, timezone.utc).isoformat()
                    if published_ts is not None else None
                ),
                "published_ts": published_ts,
            }
        )
    return rows


def _fetch_bytes(url: str, *, headers: dict[str, str] | None = None) -> bytes:
    default_headers = {
        "User-Agent": "Mozilla/5.0 SolaireNews/2.0",
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, text/html, */*",
    }
    default_headers.update(headers or {})
    req = Request(url, headers=default_headers)
    with urlopen(req, timeout=FETCH_TIMEOUT_SECONDS) as response:
        return response.read(2_000_000)


def _fetch_source(source: tuple[str, str, float, str]) -> tuple[str, float, str, list[dict], str | None]:
    name, url, weight, source_kind = source
    try:
        payload = _fetch_bytes(url)
        return name, weight, source_kind, parse_feed(payload, name), None
    except Exception as exc:
        return name, weight, source_kind, [], f"{type(exc).__name__}: {exc}"


def _load_registry() -> dict[str, Any]:
    try:
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _load_official_state() -> dict[str, Any]:
    try:
        data = json.loads(OFFICIAL_STATE_PATH.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data.setdefault("sources", {})
            data.setdefault("x_last_checked", {})
            data.setdefault("x_seen", {})
            data.setdefault("recent_items", {})
            return data
    except Exception:
        pass
    return {"schema": "solaire_official_news_state_v2", "sources": {}, "x_last_checked": {}, "x_seen": {}, "recent_items": {}}


def _save_official_state(state: dict[str, Any]) -> None:
    state["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
    tmp = OFFICIAL_STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OFFICIAL_STATE_PATH)


def _asset_names(asset_rows: list[dict[str, Any]] | None) -> dict[str, str]:
    return {
        str(row.get("symbol") or "").upper(): str(row.get("name") or "").strip()
        for row in (asset_rows or [])
        if row.get("symbol") and row.get("name")
    }


def _market_match(raw_text: str, normalized: str, base: str, project_name: str | None = None) -> bool:
    # Very short tickers (C, S, OP, etc.) collide constantly with ordinary
    # language. They may match only through a project name/alias or an explicit
    # official direct-market attribution.
    if len(base) >= 3 and re.search(rf"(?<![A-Z0-9]){re.escape(base)}(?![A-Z0-9])", raw_text):
        return True
    aliases = list(ALIASES.get(base, ()))
    if project_name:
        aliases.append(project_name)
    for alias in aliases:
        alias_plain = _plain(alias)
        if len(alias_plain) < 4 or alias_plain == base.lower():
            continue
        if re.search(rf"(?<![a-z0-9]){re.escape(alias_plain)}(?![a-z0-9])", normalized):
            return True
    return False


def _classify(text: str, age_seconds: float, source_weight: float) -> tuple[float, str, list[str]]:
    normalized = " " + _plain(text) + " "
    positive = [label for label, terms in POSITIVE_GROUPS if any(_plain(term) in normalized for term in terms)]
    negative = [label for label, terms in NEGATIVE_GROUPS if any(_plain(term) in normalized for term in terms)]

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


def _catalyst_signal(
    text: str,
    age_seconds: float,
    source_weight: float,
    *,
    official_direct: bool,
) -> dict[str, Any] | None:
    normalized = " " + _plain(text) + " "
    level = 0
    label = None
    cues: list[str] = []

    def matched(terms: tuple[str, ...]) -> list[str]:
        return [term for term in terms if _plain(term) in normalized]

    l3 = matched(CATALYST_LEVEL_3)
    l2 = matched(CATALYST_LEVEL_2)
    l1 = matched(CATALYST_LEVEL_1)
    # Explicit clock/date language raises an already future-looking item to
    # imminent. It cannot create a catalyst by itself.
    explicit_time = bool(
        re.search(r"\\b(?:[01]?\\d|2[0-3])[:h][0-5]\\d\\b", normalized)
        or re.search(r"\\b(?:utc|cet|cest)\\b", normalized)
        or re.search(r"\\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\\b", normalized)
    )

    if l3:
        level, label, cues = 3, "IMMINENT", l3
    elif l2:
        level, label, cues = 2, "UPCOMING", l2
    elif l1:
        level, label, cues = 1, "ROADMAP", l1
    else:
        return None
    if explicit_time and level >= 2:
        level, label = 3, "IMMINENT"
        cues.append("explicit_time")

    _, direction, categories = _classify(text, age_seconds, 1.0)
    event_words = (
        "announcement", "annonce", "launch", "lancement", "release",
        "mainnet", "testnet", "listing", "cotation", "upgrade", "mise a jour",
        "stablecoin", "product", "produit", "partnership", "partenariat",
        "integration", "tokenomics", "buyback", "rachat", "burn", "airdrop",
        "vote", "proposal", "proposition",
    )
    has_event_word = any(_plain(term) in normalized for term in event_words)
    # Generic calendar/social chatter ("community call tomorrow") is not a
    # tradable catalyst. Levels 2/3 require either a material category or an
    # explicit event/announcement word. Roadmap requires a material category.
    if level == 1 and not categories:
        return None
    if level >= 2 and not categories and not has_event_word:
        return None

    base_score = {1: 4.8, 2: 6.8, 3: 8.4}[level]
    score = base_score
    score += 0.45 if official_direct else 0.20
    score += min(0.6, 0.2 * len(categories))
    if age_seconds > 72 * 3600:
        score -= 0.8
    elif age_seconds > 24 * 3600:
        score -= 0.35
    score *= min(1.30, max(0.8, source_weight))

    return {
        "level": level,
        "label": label,
        "score": round(max(0.0, min(10.0, score)), 3),
        "direction": direction if direction != "NEUTRAL" else "UNKNOWN",
        "timing_cues": sorted(set(cues)),
        "categories": categories,
        "prewatch_trigger": level >= 2 and score >= CATALYST_PREWATCH_MIN,
    }


def _official_sources(registry: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for market, entry in (registry.get("markets") or {}).items():
        if not isinstance(entry, dict) or not entry.get("active_on_bitvavo", True):
            continue
        urls = []
        # Always keep one canonical project homepage in the rotation. Some
        # directory "forum" links are merely social profiles and should not
        # displace the project's own site.
        for url in (entry.get("homepage") or [])[:1]:
            urls.append((url, "OFFICIAL_HOMEPAGE"))
        for key, kind in (
            ("announcement_urls", "OFFICIAL_ANNOUNCEMENTS"),
            ("official_forum_urls", "OFFICIAL_GOVERNANCE"),
            ("medium", "OFFICIAL_MEDIUM"),
        ):
            for url in entry.get(key) or []:
                urls.append((url, kind))
        for url, kind in urls:
            if str(url).startswith(("https://", "http://")):
                rows.append({"market": market, "url": str(url), "kind": kind})
    return rows


def _material_anchor_titles(payload: bytes) -> list[tuple[str, str]]:
    text = payload.decode("utf-8", errors="replace")
    result = []
    for href, inner in re.findall(r"<a[^>]+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", text, flags=re.I | re.S):
        title = html.unescape(re.sub(r"<[^>]+>", " ", inner))
        title = re.sub(r"\s+", " ", title).strip()
        if not (14 <= len(title) <= 260):
            continue
        score, direction, _ = _classify(title, 0, 1.25)
        if direction == "NEUTRAL" or score < NEWS_WATCH_MIN:
            continue
        result.append((href, title))
    dedup = {}
    for href, title in result:
        dedup[title.lower()] = (href, title)
    return list(dedup.values())[:80]


def _poll_official_page(source: dict[str, Any], prior: dict[str, Any], now_ts: float) -> tuple[list[dict], dict[str, Any], dict[str, Any]]:
    url = source["url"]
    market = source["market"]
    kind = source["kind"]
    try:
        payload = _fetch_bytes(url)
        stripped = payload.lstrip().lower()
        items = []
        if stripped.startswith(b"<?xml") or b"<rss" in stripped[:1000] or b"<feed" in stripped[:1000]:
            for row in parse_feed(payload, "OFFICIAL:" + url):
                published_ts = row.get("published_ts")
                if published_ts is None:
                    continue
                age = now_ts - published_ts
                if -300 <= age <= CATALYST_LOOKBACK_SECONDS:
                    row["direct_markets"] = [market]
                    row["source_kind"] = "official_project"
                    row["source_weight"] = 1.25
                    items.append(row)
            new_prior = {"last_checked_ts": now_ts, "initialized": True, "seen": prior.get("seen", {})}
            return items, new_prior, {"source": url, "kind": kind, "ok": True, "items": len(items)}

        anchors = _material_anchor_titles(payload)
        old_seen = dict(prior.get("seen") or {})
        initialized = bool(prior.get("initialized"))
        emitted = []
        for href, title in anchors:
            fingerprint = hashlib.sha256((url + "\n" + title.lower()).encode("utf-8")).hexdigest()[:20]
            if fingerprint not in old_seen:
                old_seen[fingerprint] = now_ts
                if initialized:
                    absolute = urllib.parse.urljoin(url, href)
                    emitted.append({
                        "id": fingerprint,
                        "source": "OFFICIAL:" + kind,
                        "source_kind": "official_project",
                        "source_weight": 1.25,
                        "title": title,
                        "description": "",
                        "url": absolute,
                        "published_at_utc": datetime.fromtimestamp(now_ts, timezone.utc).isoformat(),
                        "published_ts": now_ts,
                        "direct_markets": [market],
                        "timestamp_semantics": "FIRST_SEEN_ON_OFFICIAL_PAGE",
                    })
        # bound page fingerprints
        old_seen = dict(sorted(old_seen.items(), key=lambda kv: kv[1], reverse=True)[:200])
        new_prior = {"last_checked_ts": now_ts, "initialized": True, "seen": old_seen}
        return emitted, new_prior, {"source": url, "kind": kind, "ok": True, "items": len(emitted)}
    except Exception as exc:
        new_prior = dict(prior)
        new_prior["last_checked_ts"] = now_ts
        return [], new_prior, {"source": url, "kind": kind, "ok": False, "items": 0, "error": f"{type(exc).__name__}: {exc}"}


def _collect_x_items(registry: dict[str, Any], state: dict[str, Any], now_ts: float) -> tuple[list[dict], list[dict]]:
    token = os.getenv("X_BEARER_TOKEN", "").strip()
    handles = []
    handle_markets: dict[str, list[str]] = {}
    for market, entry in (registry.get("markets") or {}).items():
        if not isinstance(entry, dict) or not entry.get("active_on_bitvavo", True):
            continue
        handle = str(entry.get("x_handle") or "").strip().lstrip("@")
        if not handle:
            continue
        key = handle.lower()
        handle_markets.setdefault(key, []).append(market)
    handles = sorted(handle_markets, key=lambda h: float((state.get("x_last_checked") or {}).get(h, 0)))
    selected = handles[:X_HANDLES_PER_CYCLE]
    if not token:
        return [], [{
            "source": "X_OFFICIAL",
            "ok": False,
            "configured": False,
            "registered_handles": len(handles),
            "polled_handles": 0,
            "error": "X_BEARER_TOKEN_NOT_CONFIGURED",
        }]

    items = []
    statuses = []
    x_seen = dict(state.get("x_seen") or {})
    for offset in range(0, len(selected), X_HANDLES_PER_QUERY):
        batch = selected[offset:offset + X_HANDLES_PER_QUERY]
        query = "(" + " OR ".join("from:" + h for h in batch) + ") -is:retweet"
        previous_checks = [
            float((state.get("x_last_checked") or {}).get(handle, 0) or 0)
            for handle in batch
        ]
        known_checks = [ts for ts in previous_checks if ts > 0]
        # First subscription pass looks back across the normal NEWS window.
        # Later passes only revisit a two-minute overlap from the oldest
        # handle checkpoint in the batch, preventing high-volume accounts from
        # crowding material posts out of max_results=100.
        start_ts = (
            max(now_ts - NEWS_LOOKBACK_SECONDS, min(known_checks) - 120)
            if len(known_checks) == len(batch)
            else now_ts - NEWS_LOOKBACK_SECONDS
        )
        params = urllib.parse.urlencode({
            "query": query,
            "max_results": 100,
            "tweet.fields": "created_at,author_id",
            "expansions": "author_id",
            "user.fields": "username",
            "start_time": datetime.fromtimestamp(start_ts, timezone.utc).isoformat().replace("+00:00", "Z"),
        })
        url = "https://api.x.com/2/tweets/search/recent?" + params
        try:
            payload = json.loads(_fetch_bytes(url, headers={"Authorization": "Bearer " + token, "Accept": "application/json"}))
            users = {
                str(row.get("id")): str(row.get("username") or "").lower()
                for row in ((payload.get("includes") or {}).get("users") or [])
            }
            for tweet in payload.get("data") or []:
                tweet_id = str(tweet.get("id") or "")
                if not tweet_id or tweet_id in x_seen:
                    continue
                handle = users.get(str(tweet.get("author_id") or ""), "")
                direct = handle_markets.get(handle, [])
                if not direct:
                    continue
                published_ts = _published_ts(str(tweet.get("created_at") or ""))
                if published_ts is None:
                    continue
                x_seen[tweet_id] = published_ts
                items.append({
                    "id": "x-" + tweet_id,
                    "source": "OFFICIAL_X:@" + handle,
                    "source_kind": "official_project",
                    "source_weight": 1.30,
                    "title": str(tweet.get("text") or "").strip(),
                    "description": "",
                    "url": "https://x.com/" + handle + "/status/" + tweet_id,
                    "published_at_utc": datetime.fromtimestamp(published_ts, timezone.utc).isoformat(),
                    "published_ts": published_ts,
                    "direct_markets": direct,
                    "timestamp_semantics": "X_CREATED_AT",
                })
            statuses.append({"source": "X_OFFICIAL", "ok": True, "configured": True, "polled_handles": len(batch)})
        except Exception as exc:
            statuses.append({"source": "X_OFFICIAL", "ok": False, "configured": True, "polled_handles": len(batch), "error": f"{type(exc).__name__}: {exc}"})
        for handle in batch:
            state.setdefault("x_last_checked", {})[handle] = now_ts
    state["x_seen"] = dict(sorted(x_seen.items(), key=lambda kv: kv[1], reverse=True)[:3000])
    return items, statuses


def _collect_official_items(registry: dict[str, Any], now_ts: float) -> tuple[list[dict], list[dict], dict[str, Any]]:
    state = _load_official_state()
    sources = _official_sources(registry)
    sources.sort(key=lambda s: float((state.get("sources", {}).get(s["url"], {}) or {}).get("last_checked_ts", 0)))
    selected = sources[:OFFICIAL_POLL_LIMIT]

    items = []
    statuses = []
    updates: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=min(OFFICIAL_WORKERS, max(1, len(selected)))) as pool:
        future_map = {}
        for source in selected:
            prior = (state.get("sources") or {}).get(source["url"], {})
            future = pool.submit(_poll_official_page, source, prior, now_ts)
            future_map[future] = source["url"]
        for future in as_completed(future_map):
            page_items, new_prior, status = future.result()
            items.extend(page_items)
            statuses.append(status)
            updates[future_map[future]] = new_prior
    state.setdefault("sources", {}).update(updates)

    x_items, x_status = _collect_x_items(registry, state, now_ts)
    items.extend(x_items)
    statuses.extend(x_status)

    # Official sources are event-driven. Persist recently observed official
    # items so a teaser/news item remains visible across later 5-minute cycles
    # instead of disappearing immediately after its first observation.
    stored = dict(state.get("recent_items") or {})
    for item in items:
        item_id = str(item.get("id") or "")
        published_ts = item.get("published_ts")
        if item_id and published_ts is not None:
            stored[item_id] = item
    stored = {
        item_id: item
        for item_id, item in stored.items()
        if item.get("published_ts") is not None
        and -300 <= now_ts - float(item.get("published_ts")) <= CATALYST_LOOKBACK_SECONDS
    }
    state["recent_items"] = stored
    _save_official_state(state)
    items = list(stored.values())
    diagnostics = {
        "registered_official_pages": len(sources),
        "polled_official_pages": len(selected),
        "registered_x_handles": sum(bool((row or {}).get("x_handle")) for row in (registry.get("markets") or {}).values() if isinstance(row, dict)),
        "registry_coverage": registry.get("coverage") or {},
    }
    return items, statuses, diagnostics


def collect_news_context(
    markets: list[dict],
    now_ts: float | None = None,
    asset_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    now_ts = time.time() if now_ts is None else now_ts
    registry = _load_registry()
    official_items, official_status, official_diag = _collect_official_items(registry, now_ts)

    fetched: list[tuple[str, float, str, list[dict], str | None]] = []
    with ThreadPoolExecutor(max_workers=len(SOURCES)) as pool:
        futures = [pool.submit(_fetch_source, source) for source in SOURCES]
        for future in as_completed(futures):
            fetched.append(future.result())

    source_status = list(official_status)
    items = list(official_items)
    weights = {}
    source_kinds = {}
    for name, weight, source_kind, rows, error in fetched:
        weights[name] = weight
        source_kinds[name] = source_kind
        source_status.append(
            {"source": name, "kind": source_kind, "ok": error is None, "items": len(rows), "error": error}
        )
        for row in rows:
            row["source_kind"] = source_kind
            row["source_weight"] = weight
        items.extend(rows)

    active = []
    seen = set()
    for item in items:
        if item["id"] in seen:
            continue
        seen.add(item["id"])
        published_ts = item.get("published_ts")
        if published_ts is None:
            continue
        age = now_ts - published_ts
        max_age = (
            CATALYST_LOOKBACK_SECONDS
            if item.get("source_kind") == "official_project"
            else NEWS_LOOKBACK_SECONDS
        )
        if age < -300 or age > max_age:
            continue
        active.append((item, max(0.0, age)))

    asset_names = _asset_names(asset_rows)
    registry_names = {
        str((row or {}).get("symbol") or market.split("-", 1)[0]).upper(): str((row or {}).get("project_name") or "")
        for market, row in (registry.get("markets") or {}).items()
        if isinstance(row, dict)
    }

    by_market: dict[str, dict[str, Any]] = {}
    for meta in markets:
        market = str(meta.get("market") or "")
        base = str(meta.get("base") or market.split("-", 1)[0]).upper()
        if not market or not base:
            continue
        project_name = asset_names.get(base) or registry_names.get(base)
        matches = []
        catalyst_matches = []
        for item, age in active:
            raw_text = f"{item.get('title','')} {item.get('description','')}"
            normalized = _plain(raw_text)
            direct = market in (item.get("direct_markets") or [])
            if not direct and not _market_match(raw_text, normalized, base, project_name):
                continue
            source_kind = item.get("source_kind") or source_kinds.get(item.get("source"), "media")
            source_weight = float(item.get("source_weight") or weights.get(item.get("source"), 0.9))
            catalyst = None
            if source_kind == "official_project" and age <= CATALYST_LOOKBACK_SECONDS:
                catalyst = _catalyst_signal(
                    raw_text,
                    age,
                    source_weight,
                    official_direct=direct,
                )
                if catalyst:
                    catalyst_matches.append(
                        {
                            "catalyst_id": item["id"],
                            "source": item["source"],
                            "source_kind": source_kind,
                            "source_role": "PROJECT" if direct else "PARTNER",
                            "title": item["title"],
                            "url": item.get("url"),
                            "published_at_utc": item.get("published_at_utc"),
                            "timestamp_semantics": item.get("timestamp_semantics", "PUBLISHED_AT"),
                            "age_minutes": round(age / 60.0, 1),
                            "official_direct_match": direct,
                            **catalyst,
                        }
                    )
            # A future-looking official announcement is PREWATCH, not realised
            # NEWS. Once the project publishes the actual launch/update without
            # future timing language it naturally moves into NEWS_WATCH.
            is_future_prewatch = bool(catalyst and catalyst.get("prewatch_trigger"))
            if age <= NEWS_LOOKBACK_SECONDS and not is_future_prewatch:
                score, direction, groups = _classify(raw_text, age, source_weight)
                matches.append(
                    {
                        "news_id": item["id"],
                        "source": item["source"],
                        "source_kind": source_kind,
                        "title": item["title"],
                        "url": item.get("url"),
                        "published_at_utc": item.get("published_at_utc"),
                        "timestamp_semantics": item.get("timestamp_semantics", "PUBLISHED_AT"),
                        "age_minutes": round(age / 60.0, 1),
                        "score": score,
                        "direction": direction,
                        "categories": groups,
                        "official_direct_match": direct,
                    }
                )
        if not matches and not catalyst_matches:
            continue
        matches.sort(
            key=lambda row: (
                row.get("direction") != "NEUTRAL",
                row.get("source_kind") == "official_project",
                row["score"],
                -row["age_minutes"],
            ),
            reverse=True,
        )
        top = matches[0] if matches else None
        catalyst_matches.sort(
            key=lambda row: (
                row.get("level", 0),
                row.get("score", 0),
                row.get("official_direct_match", False),
                -row.get("age_minutes", 0),
            ),
            reverse=True,
        )
        top_catalyst = catalyst_matches[0] if catalyst_matches else None
        by_market[market] = {
            "score": top["score"] if top else 0.0,
            "direction": top["direction"] if top else "NEUTRAL",
            "watch_trigger": bool(top) and top["direction"] != "NEUTRAL" and top["score"] >= NEWS_WATCH_MIN,
            "weight_in_composite": NEWS_WEIGHT,
            "top": top,
            "items": matches[:8],
            "official_items": sum(row.get("source_kind") == "official_project" for row in matches),
            "catalyst": (
                {
                    "level": top_catalyst["level"],
                    "label": top_catalyst["label"],
                    "score": top_catalyst["score"],
                    "direction": top_catalyst["direction"],
                    "prewatch_trigger": top_catalyst["prewatch_trigger"],
                    "weight_in_composite": CATALYST_WEIGHT,
                    "top": top_catalyst,
                    "items": catalyst_matches[:8],
                }
                if top_catalyst
                else {}
            ),
        }

    return {
        "schema": "solaire_production_news_v3_catalyst_prewatch",
        "generated_at_utc": datetime.fromtimestamp(now_ts, timezone.utc).isoformat(),
        "lookback_hours": NEWS_LOOKBACK_SECONDS / 3600,
        "news_weight": NEWS_WEIGHT,
        "news_watch_min": NEWS_WATCH_MIN,
        "catalyst_lookback_hours": CATALYST_LOOKBACK_SECONDS / 3600,
        "catalyst_prewatch_min": CATALYST_PREWATCH_MIN,
        "catalyst_weight": CATALYST_WEIGHT,
        "source_priority": ["OFFICIAL_PROJECT", "OFFICIAL_PARTNER", "MEDIA_FALLBACK"],
        "official_sources": official_diag,
        "sources": sorted(source_status, key=lambda row: str(row.get("source"))),
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
    catalyst = news.get("catalyst") or {}
    try:
        catalyst_score = max(0.0, min(10.0, float(catalyst.get("score", 0.0))))
    except (TypeError, ValueError):
        catalyst_score = 0.0
    catalyst_direction = catalyst.get("direction")

    # A realised/material NEWS item has priority. A PREWATCH catalyst contributes
    # less (20%) and only while no material directional NEWS is already doing so,
    # preventing the same official post from being double-counted.
    if direction == "POSITIVE":
        result = quant + NEWS_WEIGHT * max(0.0, news_score - quant)
    elif direction == "NEGATIVE":
        result = quant * (1.0 - NEWS_WEIGHT * news_score / 10.0)
    elif catalyst_direction == "POSITIVE":
        result = quant + CATALYST_WEIGHT * max(0.0, catalyst_score - quant)
    elif catalyst_direction == "NEGATIVE":
        result = quant * (1.0 - CATALYST_WEIGHT * catalyst_score / 10.0)
    else:
        result = quant
    return round(max(0.0, min(10.0, result)), 3)
