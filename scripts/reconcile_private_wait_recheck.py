#!/usr/bin/env python3
"""Read-only causal reconciliation of private WAIT_RECHECK and public Solaire events.

No GitHub/ChatGPT client, orders, email, BUY gate or automated reclassification.
Keep private decisions and this report outside the public repository.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    from scripts.scan_accountability_ledger import (
        InputError, jsonl, outside_public_repo, parse_utc, validate_decisions
    )
except ImportError:  # python scripts/reconcile_private_wait_recheck.py
    from scan_accountability_ledger import (
        InputError, jsonl, outside_public_repo, parse_utc, validate_decisions
    )

SCHEMA = "wait_recheck_causal_reconciliation_v1"
TARGET_TYPES = {"BUY_SENT", "REJECTED"}
UTC = timezone.utc


def read_machine_journal(payload: object, asof: datetime) -> list[dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("entries"), list):
        raise InputError("machine journal must contain an entries list")
    events = []
    for i, row in enumerate(payload["entries"]):
        if not isinstance(row, dict):
            raise InputError(f"machine journal entry {i} is not an object")
        if row.get("decision_type") not in TARGET_TYPES:
            continue
        ts = row.get("decision_ts")
        if type(ts) not in (int, float) or not 1_500_000_000 <= ts <= 4_000_000_000:
            raise InputError(f"machine journal entry {i}: invalid UTC timestamp")
        at = datetime.fromtimestamp(ts, tz=UTC)
        if at > asof:
            continue  # never use future observations
        market = row.get("market")
        if not isinstance(market, str) or not market.endswith("-EUR"):
            raise InputError(f"machine journal entry {i}: invalid market")
        if row["decision_type"] == "BUY_SENT":
            if not isinstance(row.get("signal_id"), str) or not row["signal_id"]:
                raise InputError(f"machine journal entry {i}: missing signal_id")
        events.append({**row, "_at": at})
    return sorted(events, key=lambda x: (x["_at"], x.get("signal_id", "")))


def reconcile(decisions: list[dict], machine_payload: dict,
              asof: datetime) -> dict:
    validated = validate_decisions(decisions, asof)
    events = read_machine_journal(machine_payload, asof)
    latest = {}
    for row in sorted(validated, key=lambda d: (d["_at"], d["decision_id"])):
        latest[row["market"]] = row

    pending = []
    for market, row in sorted(latest.items()):
        if row["chatgpt_action"] != "WAIT_RECHECK":
            continue  # a subsequent explicit decision supersedes the WAIT
        newer = [e for e in events if e["market"] == market and e["_at"] > row["_at"]]
        buys = {}
        for e in newer:
            if e["decision_type"] == "BUY_SENT":
                key = e["signal_id"]
                buys.setdefault(key, e)
        rejections = [e for e in newer if e["decision_type"] == "REJECTED"]
        due = parse_utc(row["recheck_due_utc"], f"{row['decision_id']}.recheck_due_utc")
        overdue = due < asof
        if buys:
            state = "REVIEW_NEW_MACHINE_BUY"
        elif overdue:
            state = "REVIEW_OVERDUE"
        else:
            state = "AWAITING_TRIGGER_OR_DEADLINE"
        # Missing events never prove the market was not detected:
        # the public direct journal has bounded retention.
        pending.append({
            "market": market,
            "decision_id": row["decision_id"],
            "decision_at_utc": row["_at"].isoformat(),
            "due_at_utc": due.isoformat(),
            "state": state,
            "overdue": overdue,
            "new_buy_sent_count": len(buys),
            "new_rejections_count": len(rejections),
            "new_buy_signals": [{
                "signal_id": e["signal_id"],
                "at_utc": e["_at"].isoformat(),
                "signal_price_eur": e.get("signal_price_eur"),
                "machine_decision_id": e.get("decision_id"),
                "machine_episode_id": e.get("episode_id"),
                "delivery_meaning": "RECORDED_SENT_NOT_TRADE_FILL"
            } for e in buys.values()],
            "latest_machine_event": None if not newer else {
                "at_utc": newer[-1]["_at"].isoformat(),
                "decision_type": newer[-1]["decision_type"],
                "reason": newer[-1].get("reason")
            },
            "recheck_trigger_text": row["recheck_trigger"],
            "recheck_completed": False,
            "auto_buy_authorized": False,
            "absence_of_new_buy_proven": False,
        })
    new_buy = sum(p["state"] == "REVIEW_NEW_MACHINE_BUY" for p in pending)
    overdue = sum(p["overdue"] for p in pending)
    return {
        "schema": SCHEMA,
        "asof_utc": asof.isoformat(),
        "source": "production_direct_decision_journal.json",
        "journal_retention": "PARTIAL_HISTORY_NOT_PROOF_OF_ABSENCE",
        "machine_first_event_at_utc": events[0]["_at"].isoformat() if events else None,
        "machine_last_event_at_utc": events[-1]["_at"].isoformat() if events else None,
        "private_decisions_count": len(validated),
        "pending_wait_count": len(pending),
        "pending_overdue_count": overdue,
        "pending_new_machine_buy_count": new_buy,
        "pending": pending,
        "research_only": True,
        "no_production_changes": True,
        "orders_submitted": False,
        "threshold_changes": False,
        "limitations": [
            "New BUY_SENT mandates human re-evaluation, never a buy recommendation.",
            "Journal retention is bounded: absence of an event is not proof of non-detection.",
            "This tool does not capture ChatGPT messages or write follow-up decisions.",
            "Private output must never be committed to the public repository.",
        ],
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--decisions", required=True,
                   help="Private JSONL from ChatGPT Library, outside the repo")
    p.add_argument("--journal", required=True,
                   help="Public production_direct_decision_journal.json")
    p.add_argument("--output", required=True,
                   help="PRIVATE JSON output, outside the repo")
    p.add_argument("--asof", help="UTC snapshot cutoff, default now")
    args = p.parse_args(argv)
    try:
        outside_public_repo(args.decisions)
        outside_public_repo(args.output)
        if Path(args.decisions).resolve() == Path(args.output).resolve():
            raise InputError("input and output paths must differ")
        asof = parse_utc(args.asof, "--asof") if args.asof else datetime.now(UTC)
        rows = jsonl(args.decisions)
        machine = json.loads(Path(args.journal).read_text(encoding="utf-8"))
        result = reconcile(rows, machine, asof)
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        # Private by default; no provider calls and no stdout of private decisions.
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        out.chmod(0o600)
        print(json.dumps({k: result[k] for k in (
            "asof_utc", "private_decisions_count", "pending_wait_count",
            "pending_overdue_count", "pending_new_machine_buy_count")}))
        return 0
    except (InputError, OSError, ValueError, json.JSONDecodeError) as exc:
        print("WAIT_RECHECK_RECONCILIATION_ERROR: " + str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
