#!/usr/bin/env python3
"""OFFLINE replay evidence -> public market tape near frozen modeled exits.

Reads a frozen research artifact; fetches ONLY public market-wide trades,
never Bitvavo account/order data. This is an execution-activity diagnostic,
NOT historical depth and NOT proof of a 100 EUR executable sell.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from datetime import timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.capital_constrained_replay import utc
from research.http import PublicClient

EXPECTED_MARKET_SHA = "6df783e699ae28ae63d791223000c4c5f11e1a660025521093154fba98b557d6"
WINDOW_MINUTES = 5
MAX_TARGETS = 80
MAX_PUBLIC_TRADES = 1000


def plan_targets(frozen):
    if frozen.get("schema") != "solaire_frozen_exit_executability_audit_v1":
        raise ValueError("wrong frozen audit evidence schema")
    if frozen.get("source_candles_sha256") != EXPECTED_MARKET_SHA:
        raise ValueError("wrong market evidence checksum")
    if frozen.get("alerts") != 75 or frozen.get("markets") != 44:
        raise ValueError("wrong original fixed cohort")
    modes = frozen.get("modes")
    if not isinstance(modes, dict):
        raise ValueError("missing model modes")
    targets = []
    seen = set()
    for mode in ("flat_last_price", "next_real_print"):
        model = modes.get(mode)
        if model is None or model.get("status") != "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF":
            raise ValueError("model result missing or not completed")
        for trade in model.get("trades", []):
            eid, market = trade["event_id"], trade["market"]
            if not isinstance(eid, str) or not isinstance(market, str) or not market.endswith("-EUR"):
                raise ValueError("malformed model trade")
            closed = utc(trade["modeled_closed_utc"], "modeled_closed_utc")
            if closed.second or closed.microsecond or closed.minute % 5:
                raise ValueError("non-aligned modeled exit")
            candle_start = closed - timedelta(minutes=WINDOW_MINUTES)
            key = (market, candle_start.isoformat())
            if key in seen:
                continue
            seen.add(key)
            targets.append({
                "market": market,
                "bar_start_utc": candle_start.isoformat(),
                "bar_end_utc": closed.isoformat(),
                "source_model": mode,
                "event_id": eid,
                "exit_reason": trade["exit_reason"],
                "trade_model_proceeds_eur": trade["modeled_sell_proceeds_eur"],
                "observed_trade_not_an_order_fill": True,
            })
    if not targets or len(targets) > MAX_TARGETS:
        raise ValueError("invalid 29-trade frozen exit target count")
    targets.sort(key=lambda r: (r["market"], r["bar_start_utc"]))
    return targets


def analyze_target(target, trades, asof_time):
    """Count public trading flow; cannot infer quotes/queue/executable fill."""
    start = utc(target["bar_start_utc"], "start")
    end = utc(target["bar_end_utc"], "end")
    if asof_time < end + timedelta(minutes=WINDOW_MINUTES):
        raise ValueError("end time after capture cutoff")
    before = []
    after = []
    seen = set()
    for raw in trades:
        if not isinstance(raw, dict):
            raise ValueError("unexpected public tape row")
        ident = raw.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("missing or duplicate trade ID")
        seen.add(ident)
        ms = raw.get("timestamp")
        if isinstance(ms, bool) or not isinstance(ms, (int, float)) or not math.isfinite(ms):
            raise ValueError("invalid trade timestamp")
        price = float(raw.get("price"))
        amount = float(raw.get("amount"))
        if not all(math.isfinite(n) and n > 0 for n in (price, amount)):
            raise ValueError("non-finite or non-positive market print")
        side = raw.get("side")
        if side not in ("sell", "buy"):
            raise ValueError("unsupported public trade side")
        at = __import__("datetime").datetime.fromtimestamp(ms / 1000, __import__("datetime").timezone.utc)
        if at < start or at > end + timedelta(minutes=WINDOW_MINUTES):
            raise ValueError("public API returned out-of-window trade")
        row = (at, price * amount, side, price)
        if at < end:
            before.append(row)
        else:
            after.append(row)

    def summarise(rows):
        return {
            "trade_count": len(rows),
            "total_printed_notional_eur": round(sum(r[1] for r in rows), 6),
            "taker_sell_printed_notional_eur": round(sum(r[1] for r in rows if r[2] == "sell"), 6),
            "printed_notional_under_100_eur": sum(r[1] for r in rows) < 100,
            "first_public_trade_at_utc": min((r[0].isoformat() for r in rows), default=None),
            "last_public_trade_at_utc": max((r[0].isoformat() for r in rows), default=None),
        }
    # Exactly LIMIT results can indicate truncation; don't treat their sums as complete.
    return {
        **target,
        "market_prints_5m_ending_at_model_exit": summarise(before),
        "market_prints_5m_after_model_exit": summarise(after),
        "public_trade_rows_returned": len(trades),
        "public_trade_page_truncated_or_uncertain": len(trades) >= MAX_PUBLIC_TRADES,
        "historical_bid_ask_or_depth_available": False,
        "model_exit_fill_verified": False,
        "user_trade_proven": False,
        "liquidity_evidence_class": "PUBLIC_EXECUTED_TRADES_NOT_EXIT_ORDER_BOOK",
    }


def collect(frozen, *, client, asof_time):
    targets = plan_targets(frozen)
    records = []
    for item in targets:
        first = utc(item["bar_start_utc"], "start")
        end = utc(item["bar_end_utc"], "end")
        params = {
            "start": int(first.timestamp() * 1000),
            "end": int((end + timedelta(minutes=WINDOW_MINUTES)).timestamp() * 1000),
            "limit": MAX_PUBLIC_TRADES,
        }
        try:
            tape = client.get("/" + item["market"] + "/trades", params, cache=False)
            if not isinstance(tape, list):
                raise ValueError("public response must be a list")
            observation = analyze_target(item, tape, asof_time)
            observation["data_status"] = ("PAGE_LIMIT_TRUNCATED" if len(tape) >= MAX_PUBLIC_TRADES
                                          else "PUBLIC_PRINTS_CAPTURED")
        except Exception as exc:
            observation = {
                **item,
                "data_status": "UNKNOWN_PUBLIC_TAPE_UNAVAILABLE",
                "error_type": type(exc).__name__,
                "market_prints_5m_ending_at_model_exit": None,
                "market_prints_5m_after_model_exit": None,
                "model_exit_fill_verified": False,
                "historical_bid_ask_or_depth_available": False,
            }
        records.append(observation)
    good = [r for r in records if r["data_status"] == "PUBLIC_PRINTS_CAPTURED"]
    summary = {
        "target_count": len(records),
        "public_prints_captured_count": len(good),
        "page_limit_truncated_count": sum(r["data_status"] == "PAGE_LIMIT_TRUNCATED" for r in records),
        "unknown_data_count": sum(r["data_status"] == "UNKNOWN_PUBLIC_TAPE_UNAVAILABLE" for r in records),
        "target_bar_no_public_prints_count": sum(r["market_prints_5m_ending_at_model_exit"]["trade_count"] == 0 for r in good),
        "target_bar_printed_notional_under_100_eur_count": sum(r["market_prints_5m_ending_at_model_exit"]["printed_notional_under_100_eur"] for r in good),
        "next_5m_no_public_prints_count": sum(r["market_prints_5m_after_model_exit"]["trade_count"] == 0 for r in good),
        "next_5m_printed_notional_under_100_eur_count": sum(r["market_prints_5m_after_model_exit"]["printed_notional_under_100_eur"] for r in good),
        "historical_book_depth_matches": 0,
        "real_exit_fills_verified": 0,
    }
    return {
        "schema": "solaire_public_exit_trades_activity_v1",
        "research_only": True,
        "frozen_candle_sha256": EXPECTED_MARKET_SHA,
        "asof_utc": asof_time.isoformat(),
        "public_query_windows_minutes": 10,
        "base_cohort_buy_sent_alerts": 75,
        "base_cohort_markets": 44,
        "summary": summary,
        "records": records,
        "actual_wallet_pnl_eur": None,
        "real_exit_execution_proven": False,
        "interpretation": (
            "Public trades measure other participants' past activity, NOT resting "
            "bid book depth, ability to sell an extra 100 EUR, or personal fills. "
            "Even zero existing prints does not rule out resting bids. The first "
            "public printed price is not an executable quote."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frozen-report", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    frozen_raw = Path(args.frozen_report).read_bytes()
    frozen = json.loads(frozen_raw.decode("utf-8"))
    asof = __import__("datetime").datetime.now(__import__("datetime").timezone.utc)
    result = collect(frozen, client=PublicClient(timeout=12, retries=2, requests_per_second=2),
                     asof_time=asof)
    result["source_frozen_report_sha256"] = hashlib.sha256(frozen_raw).hexdigest()
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                                 encoding="utf-8")
    print("PUBLIC_EXIT_ACTIVITY_REPORT", json.dumps(result["summary"], sort_keys=True))
    print("IMPORTANT: No historical exit depth or verified Bitvavo fills.")
if __name__ == "__main__":
    main()
