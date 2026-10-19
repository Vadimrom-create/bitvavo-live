#!/usr/bin/env python3
"""Normalize public Solaire machine decisions without inventing fills or profits.

Read-only, offline input: production_direct_decision_journal.json.
BUY_SENT is an alert state, not an exchange fill and not proof an email was read.
REJECTED is a machine gate verdict, not a ChatGPT rejection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


SCHEMA = "solaire_economic_machine_event_ledger_v1"


class EventLedgerError(ValueError):
    pass


def numeric(value):
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def build_machine_event_ledger(source, source_sha256):
    if not isinstance(source, dict) or source.get("schema") != "solaire_prospective_journal_v1":
        raise EventLedgerError("unsupported source journal")
    entries = source.get("entries")
    if not isinstance(entries, list):
        raise EventLedgerError("missing decision list")
    source_ts = numeric(source.get("updated_at_ts"))
    if source_ts is None or source_ts <= 0:
        raise EventLedgerError("missing source publication timestamp")
    source_asof = datetime.fromtimestamp(source_ts, tz=timezone.utc)
    if not isinstance(source_sha256, str) or len(source_sha256) != 64:
        raise EventLedgerError("source hash required")
    decisions = []
    seen = set()
    counts = {"BUY_SENT": 0, "REJECTED": 0}
    valid_plans = 0
    invalid_plans = 0
    for idx, e in enumerate(entries):
        if not isinstance(e, dict):
            raise EventLedgerError(f"entry {idx}: not an object")
        kind = e.get("decision_type")
        if kind not in counts:
            raise EventLedgerError(f"entry {idx}: unknown decision type")
        did = e.get("decision_id")
        eid = e.get("episode_id")
        sig = e.get("signal_id")
        market = e.get("market")
        if not all(isinstance(v, str) and v.strip() for v in (did, eid, sig)):
            raise EventLedgerError(f"entry {idx}: missing stable IDs")
        if did in seen:
            raise EventLedgerError(f"entry {idx}: duplicate decision ID")
        seen.add(did)
        if not isinstance(market, str) or not market.endswith("-EUR"):
            raise EventLedgerError(f"entry {idx}: invalid market")
        ts = numeric(e.get("decision_ts"))
        if ts is None or ts <= 0 or ts > source_ts + 0.001:
            raise EventLedgerError(f"entry {idx}: invalid or future decision time")
        counts[kind] += 1
        entry = numeric(e.get("entry_eur"))
        stop = numeric(e.get("stop_eur"))
        tp1 = numeric(e.get("tp1_eur"))
        tp2 = numeric(e.get("tp2_eur"))
        stake = numeric(e.get("stake_eur"))
        valid = all(x is not None and x > 0 for x in (entry, stop, tp1, tp2, stake))
        valid = valid and stop < entry < tp1 <= tp2
        if kind == "BUY_SENT":
            if valid:
                valid_plans += 1
            else:
                invalid_plans += 1
        context = e.get("context") if isinstance(e.get("context"), dict) else {}
        decisions.append({
            "record_type": "MACHINE_DECISION",
            "market": market,
            "decision_type": kind,
            "decision_id": did,
            "episode_id": eid,
            "signal_id": sig,
            "alert_id": e.get("alert_id") if kind == "BUY_SENT" else None,
            "observed_at_utc": datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
            "observation_ts": ts,
            "source_cycle_id": e.get("cycle_id"),
            "execution_observation_id": e.get("execution_observation_id"),
            "regime": context.get("regime"),
            "reason": e.get("reason"),
            "score": numeric(e.get("signal_score")),
            "signal_price_eur": numeric(e.get("signal_price_eur")),
            "machine_plan": {
                "entry_limit_eur": entry,
                "stop_eur": stop,
                "tp1_eur": tp1,
                "tp2_eur": tp2,
                "stake_eur": stake,
                "structural_plan_valid": bool(valid) if kind == "BUY_SENT" else None,
            },
            "source_policy_commit": None,
            "feature_asof_utc": None,
            "feature_freshness_verified": False,
            "execution_book_independently_loaded": False,
            "entry_fill_eur": None,
            "exit_fill_eur": None,
            "fee_eur": None,
            "execution_fill_status": "UNKNOWN_NOT_PROVEN",
            "gross_trade_pnl_eur": None,
            "net_trade_pnl_eur": None,
            "can_claim_executable_pnl": False,
            "source_type": "PUBLIC_MACHINE_JOURNAL_ONLY",
        })
    decisions.sort(key=lambda x: (x["observation_ts"], x["decision_id"]))
    return {
        "schema": SCHEMA,
        "research_only": True,
        "source": {
            "input_name": "production_direct_decision_journal.json",
            "sha256": source_sha256,
            "published_at_utc": source_asof.isoformat(),
            "coverage_start_utc": decisions[0]["observed_at_utc"] if decisions else None,
            "coverage_end_utc": decisions[-1]["observed_at_utc"] if decisions else None,
            "historical_history_complete": False,
        },
        "count": len(decisions),
        "counts_by_machine_action": counts,
        "buy_sent_structurally_valid_plan_count": valid_plans,
        "buy_sent_invalid_or_incomplete_plan_count": invalid_plans,
        "actual_exchange_fills_verified": 0,
        "actual_net_pnl_eur": None,
        "actual_portfolio_equity_eur": None,
        "actual_portfolio_drawdown_eur": None,
        "buy_sent_equals_filled_order": False,
        "policy_snapshot_sha_verified": False,
        "records": decisions,
        "limitations": [
            "Published journal is retention-limited and not exhaustive across Solaire history.",
            "BUY_SENT is a machine alert, NOT a trade or a receipt read by the user.",
            "REJECTED is the machine's gate verdict, NOT a ChatGPT veto.",
            "Machine proposed entry/stop/TP and stake have NO verified exchange fills.",
            "Historical order-book snapshots and outcome trajectories are not joined.",
            "Observed context has no trustworthy as-of for each derived feature here.",
            "No costs, cash allocations, fees, PnL or market outcome is fabricated.",
            "Never publish real wallet, ChatGPT transcripts or chat exports here.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", default="production_direct_decision_journal.json")
    p.add_argument("--output", help="Research output path; stdout if omitted")
    args = p.parse_args()
    try:
        raw = Path(args.source).read_bytes()
        source = json.loads(raw.decode("utf-8"))
        result = build_machine_event_ledger(source, hashlib.sha256(raw).hexdigest())
        output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (EventLedgerError, ValueError, OSError, json.JSONDecodeError) as exc:
        p.exit(2, f"machine event ledger refused evidence: {exc}\n")


if __name__ == "__main__":
    main()
