#!/usr/bin/env python3
"""Export verifiable Solaire BUY_SENT events for the private SCAN audit.

Reads only the *public* Solaire prospective direct decision journal. Exports
machine_alert JSONL consumable by scan_accountability_ledger.py. Never infers
a ChatGPT decision, a fill, or an opportunity from REJECTED events.
Does not change Solaire production, emails, signals, or any strategy.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from scan_accountability_ledger import InputError, outside_public_repo, parse_utc

UTC = timezone.utc
SCHEMA = "solaire_direct_journal_bridge_v1"


def normalized_timestamp(value: object, name: str) -> str:
    if type(value) not in (float, int) or not 1_500_000_000 <= value <= 4_000_000_000:
        raise InputError(f"{name}: missing or invalid Unix UTC seconds")
    return datetime.fromtimestamp(value, tz=UTC).isoformat().replace("+00:00", "Z")


def export_records(payload: dict) -> tuple[list[dict], dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("entries"), list):
        raise InputError("source journal missing entries list")
    entries = payload["entries"]
    if not entries:
        return [], dict(schema=SCHEMA, source_schema=payload.get("schema"),
                        source_event_count=0, source_first_at_utc=None,
                        source_last_at_utc=None, buy_sent_count=0,
                        rejected_count=0, skipped_event_count=0,
                        buy_markets=0, rejection_reasons={},
                        historical_coverage="NO_EVENTS")
    alerts = []
    reasons = Counter()
    seen_keys = set()
    skipped = 0
    all_ts = []
    for index, event in enumerate(entries, 1):
        if not isinstance(event, dict):
            raise InputError(f"journal entry #{index} is not a mapping")
        timestamp = normalized_timestamp(event.get("decision_ts"), f"entry #{index}")
        all_ts.append(timestamp)
        decision_type = event.get("decision_type")
        if decision_type == "REJECTED":
            reasons[str(event.get("reason") or "UNKNOWN")] += 1
            continue
        if decision_type != "BUY_SENT":
            skipped += 1
            continue
        market = event.get("market")
        if not isinstance(market, str) or not market.endswith("-EUR"):
            raise InputError(f"BUY_SENT entry #{index} invalid market")
        signal_id = event.get("signal_id")
        decision_id = event.get("decision_id")
        if not isinstance(signal_id, str) or not signal_id:
            raise InputError(f"BUY_SENT entry #{index} missing immutable signal_id")
        if not isinstance(decision_id, str) or not decision_id:
            raise InputError(f"BUY_SENT entry #{index} missing decision_id")
        # A repeated provider event is a duplicate record, not a fresh signal.
        key = (signal_id, decision_id)
        if key in seen_keys:
            continue
        seen_keys.add(key)
        alerts.append({
            "record_type": "machine_alert",
            "signal_id": f"solaire:{signal_id}:{decision_id}",
            "market": market,
            "signal_at_utc": timestamp,
            "action": "ACHETE",
            "machine_decision_id": decision_id,
            "machine_episode_id": event.get("episode_id"),
            "delivery_state": "BUY_SENT_JOURNAL",
            "source": "production_direct_decision_journal.json",
        })
    alerts.sort(key=lambda a: (a["signal_at_utc"], a["market"], a["signal_id"]))
    # Here 'BUY_SENT' means recorded sent by the Solaire pipeline, not a fill.
    summary = {
        "schema": SCHEMA,
        "source_schema": payload.get("schema"),
        "source_event_count": len(entries),
        "source_first_at_utc": min(all_ts),
        "source_last_at_utc": max(all_ts),
        "buy_sent_count": len(alerts),
        "rejected_count": sum(reasons.values()),
        "skipped_event_count": skipped,
        "buy_markets": len({a["market"] for a in alerts}),
        "rejection_reasons": dict(sorted(reasons.items())),
        "historical_coverage": "OBSERVED_WINDOW_ONLY",
        "limitations": [
            "The source journal has finite retention; absence before source_first_at_utc is UNKNOWN, not no alert.",
            "BUY_SENT does not establish user delivery, execution or profitable opportunity.",
            "Machine rejections are not ChatGPT decisions and are never counted as ChatGPT refusals.",
            "Without independently dated SCAN sessions, a machine alert absent from a private chat ledger is not proof of a ChatGPT omission.",
        ],
    }
    return alerts, summary


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--journal", required=True, help="public Solaire direct decision journal")
    p.add_argument("--output", required=True, help="private machine_alert JSONL path")
    p.add_argument("--summary", required=True, help="private aggregate summary JSON path")
    args = p.parse_args(argv)
    try:
        outside_public_repo(args.output)
        outside_public_repo(args.summary)
        if Path(args.output).resolve() == Path(args.summary).resolve():
            raise InputError("summary and JSONL must use distinct output paths")
        with open(args.journal, encoding="utf-8") as handle:
            payload = json.load(handle)
        records, summary = export_records(payload)
        out_file, summary_file = Path(args.output), Path(args.summary)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        # Empty JSONL is allowed as local file but remains NON_MEASURABLE,
        # since no machine alert was observed.
        out_file.write_text("".join(json.dumps(x, sort_keys=True) + "\n" for x in records),
                            encoding="utf-8")
        summary_file.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
        return 0
    except (InputError, OSError, ValueError, json.JSONDecodeError) as ex:
        print(f"BRIDGE_INPUT_ERROR: {ex}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
