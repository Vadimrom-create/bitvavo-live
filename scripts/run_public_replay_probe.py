#!/usr/bin/env python3
"""One-off public-only 5m evidence probe for a predetermined dated BUY_SENT cohort.

Runs only inside an isolated research CI job. Calls *public* Bitvavo candles,
never private wallet/markets/order endpoints. NOT a production scheduler.
A censored path, unknown quote or any source gap prevents whole-cohort PnL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.capital_constrained_replay import replay_portfolio
from research.http import PublicClient
from scripts.prepare_economic_replay import prepare


def time_utc(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def select_time_window(book_join, asof, window_lookback_h=72, holding_h=24):
    """Window chosen from age ONLY, before fetching any outcome candles."""
    if holding_h != 24 or window_lookback_h != 72:
        raise ValueError("this probe is deliberately frozen to 24h / 72h window")
    first = asof - timedelta(hours=window_lookback_h)
    last = asof - timedelta(hours=holding_h, minutes=10)
    all_buys = [
        r for r in book_join.get("records", [])
        if r.get("decision_type") == "BUY_SENT"
        and first <= time_utc(r["observed_at_utc"]) <= last
    ]
    ids = {r["decision_id"] for r in all_buys}
    prepared = prepare(book_join, stake_eur=100)
    events = [e for e in prepared["events"] if e["event_id"] in ids]
    missing = [r["decision_id"] for r in all_buys if r["decision_id"] not in {e["event_id"] for e in events}]
    return {"first_utc": first.isoformat(), "last_utc": last.isoformat(),
            "buy_alert_count": len(all_buys), "model_event_count": len(events),
            "missing_book_evidence_ids": missing, "events": events,
            "unique_markets": sorted({e["market"] for e in events})}


def capture_closed_public_candles(markets, asof):
    if len(markets) > 80:
        raise ValueError("probe restricted to 80 markets, not an adaptive winner sample")
    client = PublicClient(timeout=10, retries=2, requests_per_second=7)
    by_market = {}
    errors = {}
    for market in markets:
        try:
            raw = client.get("/" + market + "/candles", {"interval": "5m", "limit": 1000}, cache=False)
            series = []
            for item in raw:
                if not isinstance(item, list) or len(item) < 5:
                    continue
                ts = float(item[0]) / 1000
                if not math.isfinite(ts):
                    continue
                when = datetime.fromtimestamp(ts, timezone.utc)
                if when + timedelta(minutes=5) > asof:
                    continue
                try:
                    o, h, l, c = map(float, item[1:5])
                except (TypeError, ValueError):
                    continue
                if not all(math.isfinite(v) and v > 0 for v in (o, h, l, c)):
                    continue
                series.append({"start_utc": when.isoformat(), "open": o,
                               "high": h, "low": l, "close": c})
            by_market[market] = sorted(series, key=lambda x: x["start_utc"])
        except Exception as exc:
            errors[market] = type(exc).__name__ + ":" + str(exc)[:160]
    digest = hashlib.sha256(json.dumps(
        by_market, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")).hexdigest()
    return {"schema": "solaire_closed_5m_candles_bundle_v1",
            "asof_utc": asof.isoformat(), "source_sha256": digest,
            "markets": by_market,
            "source_kind": "Bitvavo public REST /<market>/candles interval=5m, limit=1000",
            "capture_window_ms": 300000,
            "fetch_error_by_market": errors,
            "market_count_requested": len(markets),
            "market_count_received": len(by_market),
            "data_origin_authentication": "PUBLIC_API_NO_TRADE_CONFIRMATION",
            "source_freshness_note": "Closed bars only at frozen probe asof; no interpolation."}


def probe(book_join, asof, capture_fn=capture_closed_public_candles):
    window = select_time_window(book_join, asof)
    if not window["buy_alert_count"]:
        return {"status": "NOT_READY_EMPTY_24H_COHORT", "window": window,
                "modeled_portfolio_pnl_eur": None, "real_bitvavo_pnl_eur": None}, None
    if window["missing_book_evidence_ids"]:
        return {"status": "NOT_READY_BOOK_EVIDENCE_GAPS", "window": window,
                "modeled_portfolio_pnl_eur": None, "real_bitvavo_pnl_eur": None}, None
    bundle = capture_fn(window["unique_markets"], asof)
    model = replay_portfolio(
        window["events"], bundle["markets"], asof.isoformat(),
        horizon_hours=24, initial_capital_eur=2300,
        fee_each_side=0.0025, slippage_each_side=0.001,
        maximum_open_positions=10,
    )
    # Official Bitvavo candle semantics: intervals without trades have no
    # returned candles. A separately labeled FLAT last-trade *proxy* is useful
    # for path diagnostics but does NOT establish future exit liquidity.
    official_public_source = (
        bundle.get("source_kind")
        == "Bitvavo public REST /<market>/candles interval=5m, limit=1000"
        and not bundle.get("fetch_error_by_market")
    )
    proxy = None
    if official_public_source:
        proxy = replay_portfolio(
            window["events"], bundle["markets"], asof.isoformat(),
            horizon_hours=24, initial_capital_eur=2300,
            fee_each_side=0.0025, slippage_each_side=0.001,
            maximum_open_positions=10,
            gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY",
        )
    next_print = None
    if official_public_source:
        next_print = replay_portfolio(
            window["events"], bundle["markets"], asof.isoformat(),
            horizon_hours=24, initial_capital_eur=2300,
            fee_each_side=0.0025, slippage_each_side=0.001,
            maximum_open_positions=10,
            gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY",
            horizon_exit_mode="NEXT_REAL_BAR_OPEN_PROXY",
        )
    result = {
        "schema": "solaire_public_replay_probe_v1",
        "research_only": True,
        "window": {k: v for k, v in window.items() if k != "events"},
        "market_capture": {
            "markets_requested": bundle["market_count_requested"],
            "markets_received": bundle["market_count_received"],
            "fetch_error_by_market": bundle["fetch_error_by_market"],
            "closed_candles_sha256": bundle["source_sha256"],
        },
        "model_only": model,
        "proxy_zero_trade_model_only": proxy,
        "next_observed_trade_exit_proxy_model_only": next_print,
        "gap_semantics_reference": "https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/",
        "status": model["status"],
        "real_bitvavo_pnl_eur": None,
        "modeled_portfolio_pnl_eur": model.get("modeled_portfolio_pnl_eur"),
        "r2_v4_comparison_ready": False,
        "risk_note": "No real fills, no known future exit order book, and no synchronized drawdown. Flat no-trade gaps are a CONDI-TIONAL PRICE PATH PROXY ONLY; cannot claim actual executable portfolio PnL.",
    }
    return result, bundle


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--books", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--candle-bundle", required=True)
    args = p.parse_args()
    try:
        book = json.loads(Path(args.books).read_text(encoding="utf-8"))
        # Freeze observation cutoff BEFORE any Bitvavo fetches.
        asof = datetime.now(timezone.utc)
        report, bundle = probe(book, asof)
        Path(args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)+"\n", encoding="utf-8")
        if bundle is not None:
            Path(args.candle_bundle).write_text(json.dumps(bundle, ensure_ascii=False, sort_keys=True)+"\n", encoding="utf-8")
        print("RESEARCH ONLY", report["status"])
        print("Predeclared 24h time-window BUY_SENT:", report["window"]["buy_alert_count"])
        print("STRICT MODEL net PnL:", report.get("modeled_portfolio_pnl_eur"))
        proxy = report.get("proxy_zero_trade_model_only")
        if isinstance(proxy, dict):
            print("ZERO-TRADE FLAT PROXY state:", proxy["status"])
            print("ZERO-TRADE FLAT PROXY event counts:", proxy["candidate_states"])
            print("ZERO-TRADE FLAT PROXY conditional EUR PnL:", proxy["modeled_portfolio_pnl_eur"])
        next_print = report.get("next_observed_trade_exit_proxy_model_only")
        if isinstance(next_print, dict):
            print("NEXT REAL TRADE EXIT PROXY state:", next_print["status"])
            print("NEXT REAL TRADE EXIT PROXY event counts:", next_print["candidate_states"])
            print("NEXT REAL TRADE EXIT PROXY conditional EUR PnL:",
                  next_print.get("modeled_portfolio_pnl_eur"))
            print("NEXT REAL TRADE EXIT PROXY allocations rejected:",
                  next_print.get("allocation_reject_count"))
        print("REAL net PnL: NEVER VERIFIED IN THIS PROBE")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        p.exit(2, f"public 5m economic probe refused: {exc}\n")


if __name__ == "__main__":
    main()
