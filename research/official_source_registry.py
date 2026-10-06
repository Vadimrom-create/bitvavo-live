"""Official-source registry for every active Bitvavo EUR asset.

CoinGecko is used only as a directory to discover official project links.
News attribution always points to the project's own website/blog/forum/X source.
"""
from __future__ import annotations

import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

REGISTRY = Path("official_source_registry.json")
COINGECKO_LIST = "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
COINGECKO_COIN = "https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
USER_AGENT = "SolaireOfficialSources/1.0"
DETAIL_DELAY_SECONDS = 4.0

OFFICIAL_OVERRIDES = {
    "ETHFI": {
        "homepage": ["https://ether.fi/"],
        "announcement_urls": ["https://www.ether.fi/blog?tag=Announcement"],
        "official_forum_urls": ["https://governance.ether.fi/"],
        "medium": ["https://medium.com/@etherfi"],
        "x_handle": "ether_fi",
        "verification": "ETHERFI_OFFICIAL_COMMUNITY_RESOURCES",
    },
}


def _norm(value: Any) -> str:
    raw = unicodedata.normalize("NFKD", str(value or ""))
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", raw.lower())


def _get_json(url: str, timeout: int = 15) -> Any:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
    )
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code != 429 or attempt >= 3:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            try:
                delay = max(8.0, min(60.0, float(retry_after)))
            except (TypeError, ValueError):
                delay = 12.0 * (attempt + 1)
            time.sleep(delay)
    if last_error:
        raise last_error
    raise RuntimeError("COINGECKO_FETCH_FAILED")


def _clean_urls(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    result = []
    for value in values:
        value = str(value or "").strip()
        if value.startswith(("https://", "http://")) and value not in result:
            result.append(value)
    return result


def _asset_names(asset_rows: list[dict[str, Any]]) -> dict[str, str]:
    return {
        str(row.get("symbol") or "").upper(): str(row.get("name") or "").strip()
        for row in asset_rows
        if row.get("symbol") and row.get("name")
    }


def _resolve_id(symbol: str, name: str, coin_rows: list[dict[str, Any]]) -> tuple[str | None, str]:
    candidates = [
        row for row in coin_rows
        if str(row.get("symbol") or "").upper() == symbol.upper()
    ]
    if not candidates:
        return None, "NO_SYMBOL_MATCH"
    wanted = _norm(name)
    exact_name = [row for row in candidates if wanted and _norm(row.get("name")) == wanted]
    if len(exact_name) == 1:
        return str(exact_name[0].get("id")), "SYMBOL_AND_NAME"
    if len(candidates) == 1:
        return str(candidates[0].get("id")), "UNIQUE_SYMBOL"
    # Never guess on symbol collisions. Persist ambiguity for later explicit resolution.
    return None, "AMBIGUOUS_SYMBOL"


def ensure_universe_entries(
    registry: dict[str, Any],
    markets: list[dict[str, Any]],
    asset_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    registry = dict(registry or {})
    registry.setdefault("schema", "solaire_official_source_registry_v1")
    entries = registry.setdefault("markets", {})
    names = _asset_names(asset_rows)
    active = set()
    for meta in markets:
        market = str(meta.get("market") or "")
        base = str(meta.get("base") or market.split("-", 1)[0]).upper()
        if not market or not base:
            continue
        active.add(market)
        row = entries.setdefault(market, {})
        row.update(
            market=market,
            symbol=base,
            project_name=names.get(base) or row.get("project_name") or base,
            active_on_bitvavo=True,
        )
        row.setdefault("homepage", [])
        row.setdefault("announcement_urls", [])
        row.setdefault("official_forum_urls", [])
        row.setdefault("medium", [])
        row.setdefault("x_handle", None)
        row.setdefault("discovery_status", "PENDING")
        override = OFFICIAL_OVERRIDES.get(base)
        if override:
            for key in ("homepage", "announcement_urls", "official_forum_urls", "medium"):
                row[key] = list(dict.fromkeys((row.get(key) or []) + override.get(key, [])))
            row["x_handle"] = override.get("x_handle") or row.get("x_handle")
            row["verification"] = override.get("verification")
            row["discovery_status"] = "VERIFIED_OVERRIDE"
    for market, row in entries.items():
        if isinstance(row, dict):
            row["active_on_bitvavo"] = market in active
    registry["active_market_count"] = len(active)
    return registry


def discover_official_links(
    registry: dict[str, Any],
    *,
    max_details: int | None = None,
) -> dict[str, Any]:
    coin_rows = _get_json(COINGECKO_LIST)
    if not isinstance(coin_rows, list):
        raise RuntimeError("COINGECKO_LIST_INVALID")

    entries = registry.get("markets") or {}
    resolved = 0
    attempted = 0
    errors = []
    for market in sorted(entries):
        row = entries[market]
        if not row.get("active_on_bitvavo"):
            continue
        if row.get("discovery_status") in {"DISCOVERED", "VERIFIED_OVERRIDE"} and (
            row.get("homepage") or row.get("x_handle") or row.get("announcement_urls")
        ):
            continue
        if max_details is not None and max_details >= 0 and attempted >= max_details:
            break
        attempted += 1
        coin_id, method = _resolve_id(
            str(row.get("symbol") or ""),
            str(row.get("project_name") or ""),
            coin_rows,
        )
        row["coingecko_resolution"] = method
        row["coingecko_id"] = coin_id
        if not coin_id:
            row["discovery_status"] = method
            continue
        try:
            detail = _get_json(COINGECKO_COIN.format(coin_id=urllib.parse.quote(coin_id)))
            links = (detail or {}).get("links") or {}
            homepage = _clean_urls(links.get("homepage"))
            announcements = _clean_urls(links.get("announcement_url"))
            forums = _clean_urls(links.get("official_forum_url"))
            x_handle = str(links.get("twitter_screen_name") or "").strip() or None

            row["homepage"] = list(dict.fromkeys((row.get("homepage") or []) + homepage))
            row["announcement_urls"] = list(dict.fromkeys((row.get("announcement_urls") or []) + announcements))
            row["official_forum_urls"] = list(dict.fromkeys((row.get("official_forum_urls") or []) + forums))
            row["x_handle"] = row.get("x_handle") or x_handle
            row["discovery_status"] = "DISCOVERED"
            row.pop("discovery_error", None)
            row["link_discovery_source"] = "COINGECKO_DIRECTORY"
            row["links_are_project_sources"] = True
            resolved += 1
        except Exception as exc:
            row["discovery_status"] = "DISCOVERY_ERROR"
            row["discovery_error"] = f"{type(exc).__name__}: {exc}"
            errors.append({"market": market, "error": row["discovery_error"]})
        time.sleep(DETAIL_DELAY_SECONDS)

    active_rows = [row for row in entries.values() if isinstance(row, dict) and row.get("active_on_bitvavo")]
    with_any = sum(bool(row.get("homepage") or row.get("announcement_urls") or row.get("official_forum_urls") or row.get("x_handle")) for row in active_rows)
    with_x = sum(bool(row.get("x_handle")) for row in active_rows)
    with_page = sum(bool(row.get("announcement_urls") or row.get("official_forum_urls") or row.get("homepage")) for row in active_rows)
    registry["coverage"] = {
        "active_markets": len(active_rows),
        "with_any_official_source": with_any,
        "with_official_page": with_page,
        "with_official_x": with_x,
        "coverage_pct": round(100.0 * with_any / len(active_rows), 2) if active_rows else 0.0,
        "attempted_this_run": attempted,
        "resolved_this_run": resolved,
        "errors_this_run": len(errors),
    }
    registry["updated_at_ts"] = time.time()
    return registry


def load_registry() -> dict[str, Any]:
    try:
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception:
        return {"schema": "solaire_official_source_registry_v1", "markets": {}}


def save_registry(registry: dict[str, Any]) -> None:
    tmp = REGISTRY.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(REGISTRY)
