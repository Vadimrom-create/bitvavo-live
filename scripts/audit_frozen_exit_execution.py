#!/usr/bin/env python3
"""Frozen research replay over the ORIGINAL 11 Oct public artifacts.

No network/Bitvavo access. Strict, last-price, and next-real-print modes are
run on identical dated alerts and the exact same captured public candles.
Never mistake the first exchange print for actual order fill liquidity.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.capital_constrained_replay import replay_portfolio
from scripts.run_public_replay_probe import select_time_window


def digest_markets(markets):
    return hashlib.sha256(json.dumps(
        markets, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")).hexdigest()


def replay_frozen(book_join, bundle, baseline_report, stake_eur=100):
    if bundle.get("schema") != "solaire_closed_5m_candles_bundle_v1":
        raise ValueError("historical candle bundle schema invalid")
    asof_str = bundle.get("asof_utc")
    if not isinstance(asof_str, str):
        raise ValueError("missing historical asof")
    asof = datetime.fromisoformat(asof_str.replace("Z", "+00:00"))
    if asof.tzinfo is None or asof.utcoffset().total_seconds() != 0:
        raise ValueError("UTC asof required")
    markets = bundle.get("markets")
    if not isinstance(markets, dict) or digest_markets(markets) != bundle.get("source_sha256"):
        raise ValueError("frozen candle data hash mismatch")
    if baseline_report.get("schema") != "solaire_public_replay_probe_v1":
        raise ValueError("expected frozen research report")
    if baseline_report.get("market_capture", {}).get("closed_candles_sha256") != bundle.get("source_sha256"):
        raise ValueError("frozen baseline capture hash mismatch")
    window = select_time_window(book_join, asof)
    if window["buy_alert_count"] != baseline_report.get("window", {}).get("buy_alert_count"):
        raise ValueError("cohort count drift versus frozen checkpoint")
    frozen_ids = sorted(x["event_id"] for x in window["events"])
    old_observed = baseline_report.get("window", {}).get("unique_markets")
    if sorted(window["unique_markets"]) != sorted(old_observed or []):
        raise ValueError("market universe drift versus frozen checkpoint")
    if len(frozen_ids) != 75 or window["missing_book_evidence_ids"]:
        raise ValueError("frozen 75-alert evidence not complete")
    modes = (
        ("strict", "STRICT", "LAST_BAR_CLOSE_PROXY"),
        ("flat_last_price", "BITVAVO_ZERO_TRADE_FLAT_PROXY", "LAST_BAR_CLOSE_PROXY"),
        ("next_real_print", "BITVAVO_ZERO_TRADE_FLAT_PROXY", "NEXT_REAL_BAR_OPEN_PROXY"),
    )
    result = {}
    for label, gap, exit_mode in modes:
        result[label] = replay_portfolio(
            window["events"], markets, asof_str,
            horizon_hours=24, initial_capital_eur=2300,
            fee_each_side=0.0025, slippage_each_side=0.001,
            maximum_open_positions=10,
            gap_mode=gap, horizon_exit_mode=exit_mode,
        )
        assert result[label]["real_bitvavo_pnl_eur"] is None
    old_proxy = baseline_report.get("proxy_zero_trade_model_only")
    if stake_eur == 100 and old_proxy and old_proxy.get("status") == "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF":
        expected = old_proxy.get("modeled_portfolio_pnl_eur")
        got = result["flat_last_price"].get("modeled_portfolio_pnl_eur")
        if got is None or abs(got - expected) > 0.000001:
            raise ValueError(f"frozen model v1 replay drift {got} vs {expected}")
    return {
        "schema": "solaire_frozen_exit_executability_audit_v1",
        "research_only": True,
        "capital_eur": 2300,
        "entry_stake_eur": stake_eur,
        "alerts": len(window["events"]),
        "markets": len(window["unique_markets"]),
        "first_utc": window["first_utc"],
        "last_utc": window["last_utc"],
        "frozen_observation_asof_utc": asof_str,
        "source_candles_sha256": bundle["source_sha256"],
        "source_machine_sha256": book_join.get("source", {}).get("sha256"),
        "modes": result,
        "real_execution_status": "NOT_PROVEN_NO_HISTORICAL_EXIT_BOOK_OR_FILLS",
        "v4_vs_r2_comparable": False,
        "caveat": "Next real candle open is a PRINT proxy, not evidence a 100 EUR sell order was executable. It can delay cash release and still understates liquidity risk.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--books", required=True)
    p.add_argument("--candles", required=True)
    p.add_argument("--baseline", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    try:
        book = json.loads(Path(a.books).read_text(encoding="utf-8"))
        candles = json.loads(Path(a.candles).read_text(encoding="utf-8"))
        baseline = json.loads(Path(a.baseline).read_text(encoding="utf-8"))
        r = replay_frozen(book, candles, baseline)
        Path(a.output).write_text(json.dumps(r, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print("FROZEN PUB DATA:",r["alerts"],"alerts,",r["markets"],"markets")
        for label, result in r["modes"].items():
            print(label, "status=",result["status"],
                  "modeled_eur=",result["modeled_portfolio_pnl_eur"],
                  "candidate=",result["candidate_states"],
                  "allocations_rejected=",result.get("allocation_reject_count"))
        print("Real exchange pnl always NULL. No V4 vs R2 attribution.")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        p.exit(2, f"frozen replay refused: {exc}\n")


if __name__ == "__main__":
    main()
