#!/usr/bin/env python3
"""Research-only finite-capital replay from explicit public 5m candle evidence.

No market calls, keys or real orders. Refuses reported portfolio profit when
any model signal lacks price-path or book evidence. Comparing V4/R2 requires
separate matched-policy cohorts, not the production BUY_SENT subset alone.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from research.capital_constrained_replay import HORIZONS, replay_portfolio
from scripts.prepare_economic_replay import prepare


def evaluate_preflight(preflight, candle_bundle, asof_utc, horizon_hours=24):
    if preflight.get("schema") != "solaire_replay_preflight_v1":
        raise ValueError("preflight schema mismatch")
    if candle_bundle is None:
        return {
            "schema": "solaire_capital_replay_readiness_v1",
            "status": "NOT_READY_NO_PUBLIC_PRICE_PATHS_SUPPLIED",
            "candidate_count": preflight["prepared_signal_count"],
            "book_evidence_gaps": preflight["missing_book_proof_count"],
            "real_bitvavo_pnl_eur": None,
            "modeled_portfolio_pnl_eur": None,
            "capital_test_eur": 2300,
            "comparisons_ready": False,
            "note": "No continuous, as-of proven 5m trajectory was submitted. Don't infer profit from shadow aggregate totals.",
        }
    if not isinstance(candle_bundle, dict) or candle_bundle.get("schema") != "solaire_closed_5m_candles_bundle_v1":
        raise ValueError("candle bundle schema required")
    if candle_bundle.get("asof_utc") != asof_utc:
        raise ValueError("candle bundle asof must exactly match evaluation asof")
    if not candle_bundle.get("source_sha256"):
        raise ValueError("candle source checksum/provenance required")
    bars = candle_bundle.get("markets")
    if not isinstance(bars, dict):
        raise ValueError("candle bundle markets object required")
    if preflight["missing_book_proof_count"]:
        return {
            "schema": "solaire_capital_replay_readiness_v1",
            "status": "NOT_IDENTIFIABLE_INCOMPLETE_BOOK_COHORT",
            "book_evidence_gaps": preflight["missing_book_proof_count"],
            "real_bitvavo_pnl_eur": None,
            "modeled_portfolio_pnl_eur": None,
            "capital_test_eur": 2300,
            "comparisons_ready": False,
        }
    score = replay_portfolio(
        preflight["events"],
        bars,
        asof_utc,
        horizon_hours=horizon_hours,
        initial_capital_eur=2300,
        fee_each_side=0.0025,
        slippage_each_side=0.001,
        maximum_open_positions=10,
    )
    return {
        **score,
        "source_candles_sha256": candle_bundle["source_sha256"],
        "source_machine_sha256": preflight.get("source_sha256"),
        "comparisons_ready": False,
        "comparator_warning": "Production BUY_SENT model is not V4/R2; no comparable same-time R2 and V4 book evidence attached.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--books", default="/tmp/solaire-machine-book-join.json")
    p.add_argument("--candles", help="Explicit closed 5m market bundle; not fetched automatically")
    p.add_argument("--asof", help="Required with --candles; exact bundle asof UTC")
    p.add_argument("--horizon-hours", type=int, choices=HORIZONS, default=24)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    try:
        if args.candles and not args.asof:
            raise ValueError("--asof required whenever --candles is supplied")
        if args.asof and not args.candles:
            raise ValueError("--candles required whenever --asof is supplied")
        book = json.loads(Path(args.books).read_text(encoding="utf-8"))
        preflight = prepare(book, stake_eur=100)
        candles = json.loads(Path(args.candles).read_text(encoding="utf-8")) if args.candles else None
        report = evaluate_preflight(preflight, candles, args.asof, args.horizon_hours)
        Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)+"\n", encoding="utf-8")
        print(report["status"])
        print(f"Modeled portfolio PnL: {report.get('modeled_portfolio_pnl_eur')!r}; actual EUR PnL: {report['real_bitvavo_pnl_eur']!r}")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        p.exit(2, f"portfolio replay refused: {exc}\n")


if __name__ == "__main__":
    main()
