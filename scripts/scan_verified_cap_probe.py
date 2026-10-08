#!/usr/bin/env python3
"""Observation-only OGN/RLC/ZRC turnover, with verified CoinGecko asset IDs.

Fetch CoinGecko first, then the public Bitvavo 24h ticker, to prevent
combining later cap information with an earlier Bitvavo snapshot.
No API key, orders, alerts, position, BUY gate or trading policy is involved.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from scan_volume_turnover_shadow import BadEvidence, summarize, utc

UTC = timezone.utc
ASSETS = {
    "OGN-EUR": ("origin-protocol", "ogn"),
    "RLC-EUR": ("iexec-rlc", "rlc"),
    "ZRC-EUR": ("zircuit", "zrc"),
}
COINGECKO = "https://api.coingecko.com/api/v3/coins/markets"
BITVAVO = "https://api.bitvavo.com/v2/ticker/24h"
SCHEMA = "verified_bitvavo_coingecko_turnover_v1"


def fetch_json(url):
    request = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "SolaireResearchMeasurement/1.0",
    })
    with urllib.request.urlopen(request, timeout=18) as response:
        return json.load(response)


def pos(value):
    try:
        x = float(value)
        return x if math.isfinite(x) and x > 0 else None
    except (ValueError, TypeError):
        return None


def build_observation(cg_response, bv_response):
    if not isinstance(cg_response, list) or not isinstance(bv_response, list):
        raise BadEvidence("providers must each return arrays")
    expected_id = {cg_id: (market, symbol) for market, (cg_id, symbol) in ASSETS.items()}
    cg = {}
    for row in cg_response:
        if not isinstance(row, dict):
            raise BadEvidence("invalid CoinGecko row")
        asset_id = row.get("id")
        if asset_id in expected_id:
            if asset_id in cg:
                raise BadEvidence("duplicate CoinGecko asset ID")
            cg[asset_id] = row
    bv = {}
    for row in bv_response:
        if not isinstance(row, dict):
            raise BadEvidence("invalid Bitvavo row")
        market = row.get("market")
        if market in ASSETS:
            if market in bv:
                raise BadEvidence("duplicate Bitvavo market")
            bv[market] = row
    live_rows, cap_rows = [], []
    missing = []
    market_timestamps = []
    for market, (asset_id, expected_symbol) in ASSETS.items():
        ticker = bv.get(market)
        if ticker is None:
            missing.append({"market": market, "reason": "BITVAVO_TICKER_MISSING"})
            continue
        vol = pos(ticker.get("volumeQuote"))
        price = pos(ticker.get("last"))
        if vol is None or price is None:
            missing.append({"market": market, "reason": "BITVAVO_PRICE_OR_VOLUME_INVALID"})
            continue
        ticker_ms = ticker.get("timestamp")
        if type(ticker_ms) not in (int, float) or not math.isfinite(ticker_ms):
            raise BadEvidence(f"{market}: missing Bitvavo server ticker timestamp")
        tick_dt = datetime.fromtimestamp(ticker_ms / 1000, UTC)
        market_timestamps.append(tick_dt)
        bid, ask = pos(ticker.get("bid")), pos(ticker.get("ask"))
        spread = (ask - bid) / ((ask + bid) / 2) * 100 if bid is not None and ask is not None and ask >= bid else None
        live_rows.append({
            "market": market,
            "last": price,
            "quote_volume_24h_eur": vol,
            "spread_pct": spread,
            "ticker_at_utc": tick_dt.isoformat(),
            # No m15: these are fresh 24h tickers, not contemporaneous 15m candles.
        })
        info = cg.get(asset_id)
        if info is None:
            missing.append({"market": market, "reason": "COINGECKO_ASSET_MISSING"})
            continue
        cg_price = pos(info.get("current_price"))
        mc = pos(info.get("market_cap"))
        global_vol = pos(info.get("total_volume"))
        updated = info.get("last_updated")
        try:
            updated_dt = utc(updated, f"{asset_id}.last_updated")
        except BadEvidence:
            missing.append({"market": market, "reason": "COINGECKO_TIMESTAMP_INVALID"})
            continue
        if mc is None or global_vol is None or cg_price is None:
            missing.append({"market": market, "reason": "COINGECKO_PRICE_CAP_VOLUME_INVALID"})
            continue
        match_symbol = info.get("symbol", "").lower() == expected_symbol
        divergence_pct = abs(price / cg_price - 1) * 100
        verified = bool(match_symbol and divergence_pct <= 20)
        cap_rows.append({
            "market": market, "asset_id": asset_id, "identity_verified": verified,
            "market_cap_eur": mc, "global_volume_24h_eur": global_vol,
            "source": "CoinGecko coins/markets vs_currency=eur",
            "asof_utc": updated_dt.isoformat(),
            "price_divergence_pct": round(divergence_pct, 4),
            "match_symbol": match_symbol,
        })
        if not verified:
            missing.append({"market": market, "reason": "IDENTITY_OR_PRICE_SANITY_FAILED"})
    if not market_timestamps:
        raise BadEvidence("no eligible Bitvavo tickers")
    # Conservative: use the oldest exchange timestamp. Any later cap is rejected
    # by summarize as CAP_FUTURE_LOOKAHEAD.
    snapshot_dt = min(market_timestamps)
    live = {"generated_at_utc": snapshot_dt.isoformat(), "markets": live_rows}
    report = summarize(live, {"rows": cap_rows}, max_cap_age_hours=2)
    report.update({
        "observer_schema": SCHEMA,
        "provider_order": "COINGECKO_FETCHED_THEN_BITVAVO",
        "coverage_scope": "THREE_CURATED_ASSETS_ONLY",
        "cap_asset_ids": {market: asset_id for market, (asset_id, _) in ASSETS.items()},
        "provider_gaps": missing,
        "not_a_trade_signal": True,
        "caveat": "CoinGecko aggregate volume and Bitvavo spot turnover are different; neither is a realized trading PnL.",
    })
    return report


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)
    try:
        query = urllib.parse.urlencode({
            "vs_currency": "eur", "ids": ",".join(v[0] for v in ASSETS.values()),
            "per_page": len(ASSETS), "page": 1, "sparkline": "false",
        })
        # This hard-coded vendor host is trusted research-only, no dynamic URLs.
        cg = fetch_json(COINGECKO + "?" + query)
        bv = fetch_json(BITVAVO)
        report = build_observation(cg, bv)
        pth = Path(args.output)
        pth.parent.mkdir(parents=True, exist_ok=True)
        pth.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        print(json.dumps({"status": "OK", "scope": report["coverage_scope"],
                          "market_count": report["market_count"],
                          "cap_coverage_pct": report["cap_coverage_pct"],
                          "provider_gaps": report["provider_gaps"],
                          "output": str(pth)}))
        return 0
    except (BadEvidence, OSError, ValueError, urllib.error.URLError) as err:
        print("VERIFIED_CAP_PROBE_UNAVAILABLE: " + str(err), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
