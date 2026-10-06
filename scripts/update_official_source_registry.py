#!/usr/bin/env python3
"""Build/refresh official source links for the active Bitvavo EUR universe."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.http import PublicClient
from research.official_source_registry import (
    discover_official_links,
    ensure_universe_entries,
    load_registry,
    save_registry,
)


def main() -> int:
    client=PublicClient(timeout=15,retries=3,requests_per_second=6)
    client.get("/time",cache=False)
    markets=[
        row for row in client.get("/markets")
        if row.get("quote")=="EUR" and row.get("status")=="trading"
    ]
    assets=client.get("/assets")
    if not isinstance(assets,list):
        raise RuntimeError("BITVAVO_ASSETS_INVALID")
    registry=ensure_universe_entries(load_registry(),markets,assets)
    raw=os.getenv("OFFICIAL_SOURCE_MAX_DETAILS","").strip()
    max_details=None if not raw else int(raw)
    registry=discover_official_links(registry,max_details=max_details)
    save_registry(registry)
    coverage=registry.get("coverage") or {}
    print(
        "OFFICIAL_SOURCE_REGISTRY "
        f"active={coverage.get('active_markets')} "
        f"covered={coverage.get('with_any_official_source')} "
        f"x={coverage.get('with_official_x')} "
        f"pages={coverage.get('with_official_page')} "
        f"pct={coverage.get('coverage_pct')}"
    )
    return 0


if __name__=="__main__":
    raise SystemExit(main())
