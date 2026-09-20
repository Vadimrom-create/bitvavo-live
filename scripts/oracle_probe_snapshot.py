#!/usr/bin/env python3
"""Shadow fetch of enriched public execution probes from the configured live-probe host.

This does not alter V3/V4 scoring and does not use private Bitvavo credentials.
It collects enriched microstructure only for currently relevant EUR markets.
"""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "oracle_live_probe.json"
BASE = os.environ.get("LIVE_PROBE_BASE_URL", "").rstrip("/")
MARKET_RE = re.compile(r"^[A-Z0-9]{2,20}-EUR$")
SOURCE_FILES = [
    "decision_layer.json",
    "v4_watch.json",
    "early_watch.json",
    "candidate_memory.json",
    "decision_watchlist.json",
]
MAX_MARKETS = 24
STAKE_EUR = 75


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def collect_markets(value, out: list[str], seen: set[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "market" and isinstance(item, str):
                market = item.upper()
                if MARKET_RE.fullmatch(market) and market not in seen:
                    seen.add(market)
                    out.append(market)
            collect_markets(item, out, seen)
    elif isinstance(value, list):
        for item in value:
            collect_markets(item, out, seen)
    elif isinstance(value, str):
        market = value.upper()
        if MARKET_RE.fullmatch(market) and market not in seen:
            seen.add(market)
            out.append(market)


def relevant_markets() -> list[str]:
    markets: list[str] = []
    seen: set[str] = set()
    for filename in SOURCE_FILES:
        path = ROOT / filename
        if not path.exists():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        collect_markets(payload, markets, seen)
    for market in ("BTC-EUR", "FET-EUR", "POL-EUR"):
        if market not in seen:
            seen.add(market)
            markets.append(market)
    return markets[:MAX_MARKETS]


def get_json(path: str, params: dict[str, object] | None = None, timeout: float = 4.0):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "bitvavo-live-oracle-shadow/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    started = now_iso()
    markets = relevant_markets()
    probes: dict[str, object] = {}
    errors: dict[str, str] = {}

    try:
        health = get_json("/health", timeout=3.0)
    except Exception as exc:
        health = {"ok": False, "error": f"{type(exc).__name__}:{exc}"}

    # A dead Oracle endpoint must not trigger 24 sequential timeouts. One failed
    # healthcheck is sufficient evidence that the transport is unavailable for
    # this shadow cycle; publish that state immediately and let the next cycle retry.
    if health.get("ok") is True:
        def fetch_one(market: str):
            try:
                return market, get_json("/quote", {"market": market, "stake_eur": STAKE_EUR}, timeout=4.0), None
            except Exception as exc:
                return market, None, f"{type(exc).__name__}:{exc}"

        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = [pool.submit(fetch_one, market) for market in markets]
            for future in as_completed(futures):
                market, payload, error = future.result()
                if payload is not None:
                    probes[market] = payload
                else:
                    errors[market] = error
    else:
        errors["_transport"] = health.get("error", "ORACLE_HEALTH_UNAVAILABLE")

    valid_count = sum(1 for p in probes.values() if isinstance(p, dict) and p.get("ok") is True)
    output = {
        "schema": "oracle_live_probe_shadow_v1",
        "shadow_only": True,
        "does_not_change_v4_scoring": True,
        "source": BASE or None,
        "requested_at_utc": started,
        "completed_at_utc": now_iso(),
        "stake_eur": STAKE_EUR,
        "health": health,
        "requested_markets": markets,
        "requested_market_count": len(markets),
        "valid_probe_count": valid_count,
        "valid": bool(markets) and valid_count == len(markets) and health.get("ok") is True,
        "errors": errors,
        "probes": probes,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(
        f"oracle probe shadow: health={health.get('ok')} "
        f"valid={valid_count}/{len(markets)} output={OUTPUT.name}"
    )


if __name__ == "__main__":
    main()
