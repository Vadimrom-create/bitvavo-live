#!/usr/bin/env python3
"""Prepare *hypothetical* 100/150 EUR signals from public matched BUY_SENT books.

Produces research readiness. NO price path data or fill is invented.
Only matched post-decision books within 60 seconds become modeled candidates.
Missing book evidence remains a blocker, not a disqualified trading asset.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research.capital_constrained_replay import replay_portfolio

BOOK_SCHEMA = "solaire_economic_machine_book_join_v1"


def prepare(book_join, stake_eur=100.0, max_book_delay_seconds=60):
    if not isinstance(book_join, dict) or book_join.get("schema") != BOOK_SCHEMA:
        raise ValueError("book join evidence schema required")
    if stake_eur not in (100, 150):
        raise ValueError("fixed stake must be 100 or 150 EUR")
    records = book_join.get("records")
    if not isinstance(records, list):
        raise ValueError("book join records unavailable")
    alerts = [x for x in records if x.get("decision_type") == "BUY_SENT"]
    missing = []
    result = []
    for r in alerts:
        b = r.get("historical_book_evidence")
        p = r.get("machine_plan")
        decision = r.get("decision_id")
        if not isinstance(b, dict) or not isinstance(p, dict):
            missing.append({"decision_id": decision, "reason": "BOOK_OR_PLAN_NOT_PROVEN"})
            continue
        if b.get("book_observation_status") != "MATCHED_PUBLIC_BOOK_ESTIMATE":
            missing.append({"decision_id": decision, "reason": "BOOK_UNAVAILABLE_OR_BAD"})
            continue
        lag = b.get("book_vs_decision_seconds")
        if isinstance(lag, bool) or not isinstance(lag, (float, int)) or not 0 <= lag <= max_book_delay_seconds:
            missing.append({"decision_id": decision, "reason": "BOOK_NOT_FRESH_POST_DECISION"})
            continue
        quote = b.get("stake_estimates", {}).get(str(int(stake_eur)))
        if not isinstance(quote, dict) or quote.get("entry_book_covered") is not True or quote.get("same_snapshot_exit_book_covered") is not True:
            missing.append({"decision_id": decision, "reason": "BOOK_DEPTH_NOT_VERIFIED"})
            continue
        if p.get("structural_plan_valid") is not True:
            missing.append({"decision_id": decision, "reason": "MACHINE_PLAN_UNVERIFIED"})
            continue
        result.append({
            "event_type": "MODEL_SIGNAL",
            "event_id": decision,
            "market": r["market"],
            "decision_at_utc": r["observed_at_utc"],
            "book_available_at_utc": b["book_available_at_utc"],
            "entry_limit_eur": p["entry_limit_eur"],
            "stop_eur": p["stop_eur"],
            "target_eur": p["tp1_eur"],
            "stake_eur": stake_eur,
            "book_entry_covered": True,
            "book_exit_covered": True,
            "policy_id": "SOLAIRE_PRODUCTION_BUY_SENT_NOT_V4_NOT_R2",
            "execution_model": "ONE_5M_BAR_PASSIVE_LIMIT_TOUCH_HYPOTHESIS_WITH_ADVERSE_FILL",
            "source_execution_observation_id": r.get("execution_observation_id"),
            "original_book_available_after_decision_seconds": lag,
            "real_order_claimed": False,
        })
    return {
        "schema": "solaire_replay_preflight_v1",
        "research_only": True,
        "cohort_policy": "SOLAIRE_PRODUCTION_BUY_SENT_NOT_V4_NOT_R2",
        "source_book_join_schema": BOOK_SCHEMA,
        "source_sha256": (book_join.get("source") or {}).get("sha256"),
        "fixed_stake_eur": stake_eur,
        "alert_count": len(alerts),
        "prepared_signal_count": len(result),
        "missing_book_proof_count": len(missing),
        "unresolved_book_proof": missing,
        "events": result,
        "current_market_price_paths_attached": False,
        "model_replay_ready": False,
        "real_bitvavo_pnl_eur": None,
        "model_portfolio_pnl_eur": None,
        "comparison_vs_r2_ready": False,
        "comparison_vs_v4_ready": False,
        "limitation": "Snapshots are historical public books, but full closed 5m future paths and matched R2/V4 fills are absent.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--books", default="/tmp/solaire-machine-book-join.json")
    p.add_argument("--stake", type=int, choices=(100, 150), default=100)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    try:
        book = json.loads(Path(args.books).read_text(encoding="utf-8"))
        result = prepare(book, stake_eur=args.stake)
        Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                                     encoding="utf-8")
        print(f"Book-proof preflight {args.stake} EUR: {result['prepared_signal_count']} model candidates / {result['alert_count']} alerts, {result['missing_book_proof_count']} evidence gaps.")
        print("Capital replay: NOT READY without closed price trajectories; no profitability claim.")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        p.exit(2, f"replay preflight refused: {exc}\n")


if __name__ == "__main__":
    main()
