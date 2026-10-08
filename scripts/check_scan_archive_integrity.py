#!/usr/bin/env python3
"""Validate private ChatGPT SCAN archive integrity, without inferring PnL.

Read-only: outputs aggregate counters, not private recommendation text.
"Time elapsed" is not "trade outcome matured"; executions and fills require
independently verified evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import timedelta, datetime, timezone
from pathlib import Path

from scan_accountability_ledger import InputError, jsonl, outside_public_repo, parse_utc, validate_decisions

UTC = timezone.utc
HORIZONS = (4, 24, 48, 72, 168)


def load_full(path):
    rows = []
    with Path(path).open(encoding="utf-8") as stream:
        for num, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise InputError(f"ledger line {num} invalid JSON") from exc
            if not isinstance(row, dict):
                raise InputError(f"ledger line {num} is not a JSON object")
            rows.append(row)
    if not rows or rows[0].get("record_type") != "ledger_header":
        raise InputError("ledger missing first ledger_header")
    return rows


def check(ledger, asof, manifest=None):
    rows = load_full(ledger)
    head = rows[0]
    sessions = [x for x in rows if x.get("record_type") == "scan_session"]
    decisions_raw = [x for x in rows if x.get("record_type") == "scan_decision"]
    other = [x.get("record_type") for x in rows[1:] if x.get("record_type") not in {"scan_session", "scan_decision"}]
    decisions = validate_decisions(decisions_raw, asof)
    flags = []
    if other:
        flags.append("UNRECOGNIZED_RECORD_TYPE")
    registered = head.get("decisions_recorded")
    if registered is not None and registered != len(decisions):
        flags.append("IMMUTABLE_HEADER_INITIAL_COUNT_NOT_LIVE")
    sid_counts = Counter(s.get("scan_id") for s in sessions)
    if any(n != 1 or sid is None for sid, n in sid_counts.items()):
        flags.append("DUPLICATE_OR_MISSING_SESSION_ID")
    group = defaultdict(list)
    for d in decisions:
        group[d.get("scan_id")].append(d)
    known = set(sid_counts)
    if any(sid not in known for sid in group):
        flags.append("DECISION_WITHOUT_SESSION")
    if any(sid not in group and s.get("decision_count") for sid, s in [(x.get("scan_id"), x) for x in sessions]):
        flags.append("SESSION_MISSING_DECISIONS")
    counts = Counter(d["chatgpt_action"] for d in decisions)
    timestamps = []
    provenance_limited = []
    partial = []
    archive_drift = []
    missing_docs = []
    for s in sessions:
        sid = s.get("scan_id")
        start = parse_utc(s.get("session_started_at_utc"), f"{sid}.start")
        end = parse_utc(s.get("session_completed_at_utc"), f"{sid}.end")
        if start > end or end > asof:
            flags.append("INVALID_SESSION_CHRONOLOGY")
        timestamps.append(end)
        if s.get("decision_count") != len(group.get(sid, [])):
            flags.append("SESSION_DECISION_COUNT_MISMATCH")
        content = s.get("assistant_final_text")
        if not isinstance(content, str) or hashlib.sha256(content.encode("utf-8")).hexdigest() != s.get("answer_sha256"):
            archive_drift.append(sid)
        if s.get("archived_text_scope") != "full_verbatim_user_facing_response":
            provenance_limited.append(sid)
        if s.get("machine_source_status") != "FRESH":
            partial.append(sid)
        if not s.get("machine_source_ref"):
            missing_docs.append(sid)
        for d in group.get(sid, []):
            if d["_at"] < start or d["_at"] > end or d["_source_at"] > d["_at"]:
                flags.append("DECISION_OUTSIDE_SESSION_OR_LOOKAHEAD")
    if archive_drift:
        flags.append("ARCHIVED_TEXT_HASH_MISMATCH")
    if provenance_limited:
        flags.append("ONLY_SUMMARY_NOT_FULL_CHAT_PROOF")
    if partial:
        flags.append("PARTIAL_OR_UNAVAILABLE_MACHINE_SOURCE")
    if missing_docs:
        flags.append("MISSING_MACHINE_SOURCE_REFERENCE")

    # Re-check times are obligations to inspect evidence, NOT autonomous trades.
    overdue = [d["decision_id"] for d in decisions if d["chatgpt_action"] == "WAIT_RECHECK"
               and d.get("recheck_due_utc") and parse_utc(d["recheck_due_utc"], "recheck_due_utc") < asof]
    # Chronological new decisions supersede prior waits *on same market*, but
    # never silently claim a recheck if no newer session decision exists.
    latest_by_market = {}
    for d in sorted(decisions, key=lambda z: (z["_at"], z["decision_id"])):
        latest_by_market[d["market"]] = d
    overdue_latest = [d["decision_id"] for d in latest_by_market.values()
                      if d["chatgpt_action"] == "WAIT_RECHECK"
                      and parse_utc(d["recheck_due_utc"], "recheck_due_utc") < asof]
    session_age_h = {str(h): sum((asof - t) >= timedelta(hours=h) for t in timestamps) for h in HORIZONS}
    if manifest:
        try:
            m = json.loads(Path(manifest).read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise InputError("manifest JSON invalid") from exc
        if not isinstance(m, dict):
            raise InputError("manifest must be JSON mapping")
        if sessions and "EMPTY" in str(m.get("status", "")).upper():
            flags.append("MANIFEST_EMPTY_DESPITE_SESSIONS")
        if isinstance(m.get("observed_session_count"), int) and m["observed_session_count"] != len(sessions):
            flags.append("MANIFEST_SESSION_COUNT_MISMATCH")
    return {
        "schema": "chatgpt_scan_archive_integrity_v1",
        "asof_utc": asof.isoformat(),
        "measurement_only": True,
        "sessions": len(sessions),
        "decisions": len(decisions),
        "decisions_by_action": dict(sorted(counts.items())),
        "session_text_scope_summary_not_full": len(provenance_limited),
        "sessions_with_partial_machine_source": len(partial),
        "session_text_hash_mismatch_count": len(archive_drift),
        "time_elapsed_horizon_session_count_NOT_TRADE_OUTCOMES": session_age_h,
        "verified_paired_execution_outcomes": 0,
        "chatgpt_financial_value_eur": None,
        "financial_verdict": "NON_MESURABLE",
        "latest_waits_overdue": len(overdue_latest),
        "any_historical_waits_expired": len(overdue),
        "flags": sorted(set(flags)),
        "notes": [
            "A 4h elapsed time is not proof of a filled profitable trade.",
            "The first SCAN archive contains a summary, not a full UI transcript.",
            "A stale immutable header must not be interpreted as an actual live decision count.",
            "New machine alerts outside a documented SCAN are not evidence of ChatGPT omission.",
            "Outcome comparison requires independently validated fills, fees, slippage and same time/position sizing.",
        ],
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger", required=True)
    p.add_argument("--manifest")
    p.add_argument("--asof", required=True, help="UTC timestamp")
    p.add_argument("--output")
    args = p.parse_args(argv)
    try:
        for private in (args.ledger, args.manifest, args.output):
            if private:
                outside_public_repo(private)
        out = check(args.ledger, parse_utc(args.asof, "--asof"), args.manifest)
        payload = json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(payload, encoding="utf-8")
        print(payload)
        return 0
    except (OSError, InputError, ValueError) as exc:
        print(f"SCAN_ARCHIVE_INTEGRITY_ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
