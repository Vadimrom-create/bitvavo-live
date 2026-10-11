#!/usr/bin/env python3
"""Link PRIVATE ChatGPT SCAN decisions to public Solaire alerts, exact IDs only.

Offline/read-only. No user data or linkage file may be written in the public repo.
This is provenance of a machine event, NOT evidence of a trade fill or PnL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from scan_accountability_ledger import (
    InputError, jsonl, outside_public_repo, parse_utc, validate_decisions,
)

SCHEMA = "scan_private_machine_join_v1"
MAX_FRESH_SECONDS = 600


def _time(value):
    if type(value) not in (float, int) or not math.isfinite(value) or value <= 0:
        return None
    return float(value)


def machine_index(source, asof):
    if (not isinstance(source, dict)
            or source.get("schema") != "solaire_prospective_journal_v1"
            or not isinstance(source.get("entries"), list)):
        raise InputError("machine source must be the raw Solaire prospective journal")
    published = _time(source.get("updated_at_ts"))
    if published is None:
        raise InputError("machine journal publication timestamp missing")
    index = {}
    counts = Counter()
    for entry in source["entries"]:
        if not isinstance(entry, dict):
            raise InputError("non-object machine event")
        kind = entry.get("decision_type")
        if kind not in ("BUY_SENT", "REJECTED"):
            raise InputError("unknown machine event type")
        signal = entry.get("signal_id")
        decision = entry.get("decision_id")
        episode = entry.get("episode_id")
        market = entry.get("market")
        ts = _time(entry.get("decision_ts"))
        if not all(isinstance(x, str) and x for x in (signal, decision, episode, market)):
            raise InputError("machine event missing stable identifiers")
        if ts is None or ts > published + 1 or ts > asof.timestamp() + 1:
            raise InputError("machine event has invalid/future timestamp")
        counts[kind] += 1
        index.setdefault(signal, []).append({
            "market": market, "machine_action": kind,
            "signal_id": signal, "machine_decision_id": decision,
            "episode_id": episode, "event_at_utc": datetime.fromtimestamp(ts, timezone.utc).isoformat(),
            "event_ts": ts,
        })
    return index, dict(counts)


def _link_one(decision, indexed, asof):
    signal = decision.get("machine_signal_id")
    result = {
        "private_decision_id": decision["decision_id"],
        "market": decision["market"],
        "assistant_action": decision["chatgpt_action"],
        "assistant_decision_at_utc": decision["_at"].isoformat(),
        "machine_signal_id_declared": signal if isinstance(signal, str) else None,
        "link_status": None,
        "machine_decision_id": None, "machine_episode_id": None,
        "machine_event_at_utc": None, "machine_event_age_seconds": None,
        "source_causal": False,
        "eligible_for_economic_pairing": False,
        "fills_proven": False, "net_pnl_eur": None,
    }
    if not isinstance(signal, str) or not signal.strip():
        result["link_status"] = "MISSING_EXPLICIT_SIGNAL_ID"
        return result
    hits = indexed.get(signal, [])
    if not hits:
        result["link_status"] = "SIGNAL_NOT_IN_RETAINED_JOURNAL"
        return result
    if len(hits) != 1:
        result["link_status"] = "AMBIGUOUS_SIGNAL_ID"
        return result
    event = hits[0]
    if event["market"] != decision["market"]:
        result["link_status"] = "MARKET_IDENTITY_MISMATCH"
        return result
    if event["machine_action"] != "BUY_SENT" or decision["solaire_action"] != "ACHETE":
        result["link_status"] = "NOT_A_MATCHED_MACHINE_BUY"
        return result

    observed = decision["_source_at"].timestamp()
    at = decision["_at"].timestamp()
    event_ts = event["event_ts"]
    if event_ts > observed or event_ts > at or event_ts > asof.timestamp():
        result["link_status"] = "MACHINE_EVENT_AFTER_RECORDED_SOURCE"
        return result
    age = at - event_ts
    result.update({
        "machine_decision_id": event["machine_decision_id"],
        "machine_episode_id": event["episode_id"],
        "machine_event_at_utc": event["event_at_utc"],
        "machine_event_age_seconds": round(age, 3),
        "source_causal": True,
    })
    if age > MAX_FRESH_SECONDS:
        result["link_status"] = "STALE_MACHINE_BUY"
        return result

    # Chronology + identity is a necessary condition, NEVER sufficient proof
    # of a trade or of comparative profitability.
    result["link_status"] = "EXACT_CAUSAL_MACHINE_BUY"
    result["eligible_for_economic_pairing"] = True
    return result


def link(decision_rows, machine, asof, *, raw_sha256=None):
    decisions = validate_decisions(decision_rows, asof)
    indexed, counts = machine_index(machine, asof)
    rows = [_link_one(d, indexed, asof) for d in decisions]
    stats = Counter(row["link_status"] for row in rows)
    return {
        "schema": SCHEMA, "asof_utc": asof.isoformat(),
        "private_decisions_checked": len(rows),
        "machine_retained_counts": counts,
        "machine_source_sha256": raw_sha256,
        "link_status_counts": dict(sorted(stats.items())),
        "causally_matched": stats.get("EXACT_CAUSAL_MACHINE_BUY", 0),
        "proven_executed_trades": 0, "real_or_comparable_net_pnl_eur": None,
        "links": rows,
        "privacy": "PRIVATE_OUTPUT_ONLY",
        "limitations": [
            "Only explicit machine_signal_id links: no market/time-guessing.",
            "Only BUY_SENT, not REJECTED or WATCH, permits exact machine BUY join.",
            "Retained public journal can omit old signals; absent is UNKNOWN.",
            "Source chronology and <=10m freshness enforced; email read or trade never inferred.",
            "An exact causal link does not prove that either counterfactual entry was filled.",
            "No automatic capture of ChatGPT responses; private input must be explicitly recorded.",
        ],
    }


def public_audit(machine, asof, *, sha256=None):
    idx, counts = machine_index(machine, asof)
    duplicates = sum(len(events) > 1 for events in idx.values())
    return {
        "schema": "solaire_public_machine_join_readiness_v1",
        "asof_utc": asof.isoformat(),
        "machine_source_sha256": sha256,
        "machine_retained_counts": counts,
        "unique_signal_ids": len(idx),
        "duplicate_signal_ids": duplicates,
        "private_decisions_loaded": False,
        "chatgpt_attribution": "UNKNOWN_NO_PRIVATE_INPUT",
        "trade_fills": "NOT_PROVEN",
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--machine", required=True, help="retained public machine journal")
    p.add_argument("--decisions", help="PRIVATE JSONL captured SCAN decisions")
    p.add_argument("--asof", help="explicit UTC ISO cutoff; default now")
    p.add_argument("--output", help="PRIVATE JSON output (required for private decisions)")
    p.add_argument("--public-audit-only", action="store_true")
    args = p.parse_args(argv)
    try:
        if args.asof:
            asof = parse_utc(args.asof, "--asof")
            if asof > datetime.now(timezone.utc):
                raise InputError("--asof cannot be future")
        else:
            asof = datetime.now(timezone.utc)
        if args.public_audit_only and args.decisions:
            raise InputError("public audit cannot read private decisions")
        if not args.public_audit_only and (not args.decisions or not args.output):
            raise InputError("private mode needs --decisions and --output")
        if args.decisions:
            outside_public_repo(args.decisions)
        if args.output:
            outside_public_repo(args.output)
        raw = Path(args.machine).read_bytes()
        machine = json.loads(raw)
        sha = hashlib.sha256(raw).hexdigest()
        if args.public_audit_only:
            result = public_audit(machine, asof, sha256=sha)
        else:
            result = link(jsonl(args.decisions), machine, asof, raw_sha256=sha)
        payload = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.output:
            destination = Path(args.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if args.decisions:
                # Private output permissions; caller controls secure location.
                import os
                fd = os.open(destination, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    handle.write(payload)
            else:
                destination.write_text(payload, encoding="utf-8")
        else:
            print(payload, end="")
        return 0
    except (InputError, OSError, ValueError, json.JSONDecodeError) as exc:
        print("SCAN_MACHINE_LINK_ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
