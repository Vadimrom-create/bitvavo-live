#!/usr/bin/env python3
"""Explicit private SCAN session capture (not an automatic chat hook)."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from scan_accountability_ledger import InputError, outside_public_repo, parse_utc, validate_decisions

UTC = timezone.utc
SESSION_STATES = {"SCAN_WITH_BUY", "SCAN_WAIT", "SCAN_NO_ACTION", "SCAN_INSUFFICIENT_DATA"}
SOURCE_STATES = {"FRESH", "PARTIAL", "UNAVAILABLE"}


def validate_session(obj, now):
    if not isinstance(obj, dict) or obj.get("schema") != "chatgpt_scan_session_capture_v1":
        raise InputError("session schema mismatch")
    sid = obj.get("scan_id")
    if not isinstance(sid, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{12,128}", sid):
        raise InputError("scan_id must be stable (12-128 chars)")
    start = parse_utc(obj.get("session_started_at_utc"), "session_started_at_utc")
    end = parse_utc(obj.get("session_completed_at_utc"), "session_completed_at_utc")
    if start > end or end > now + timedelta(minutes=2):
        raise InputError("invalid session time window or lookahead")
    answer = obj.get("assistant_final_text")
    if not isinstance(answer, str) or len(answer.strip()) < 20:
        raise InputError("exact user-facing recommendation required")
    if obj.get("session_status") not in SESSION_STATES:
        raise InputError("invalid session_status")
    source_status = obj.get("machine_source_status")
    if source_status not in SOURCE_STATES:
        raise InputError("invalid machine_source_status")
    asof = obj.get("machine_data_asof_utc")
    if asof is not None and parse_utc(asof, "machine_data_asof_utc") > end:
        raise InputError("lookahead in machine source")
    if source_status == "FRESH" and (asof is None or not str(obj.get("machine_source_ref") or "").strip()):
        raise InputError("FRESH source requires date and immutable reference")
    signals = obj.get("reviewed_signal_ids")
    if not isinstance(signals, list) or any(not isinstance(x, str) or not x for x in signals) or len(set(signals)) != len(signals):
        raise InputError("reviewed_signal_ids must be a unique string array")
    if not isinstance(obj.get("decisions"), list):
        raise InputError("decisions array required")
    decisions = validate_decisions(obj["decisions"], now)
    for d in decisions:
        if not start <= d["_at"] <= end:
            raise InputError("decision time not inside SCAN session")
        if d.get("scan_id") not in (None, sid):
            raise InputError("decision scan_id mismatch")
    if obj["session_status"] == "SCAN_WITH_BUY" and not any(d["chatgpt_action"] == "BUY" for d in decisions):
        raise InputError("SCAN_WITH_BUY requires BUY")
    if obj["session_status"] == "SCAN_INSUFFICIENT_DATA" and any(d["chatgpt_action"] == "BUY" for d in decisions):
        raise InputError("cannot claim BUY without data")
    if not decisions and not str(obj.get("no_decision_reason") or "").strip():
        raise InputError("zero decisions require a documented reason")
    digest = hashlib.sha256(answer.encode("utf-8")).hexdigest()
    payload_digest = hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    head = {
        "record_type": "scan_session", "schema": obj["schema"], "scan_id": sid,
        "session_started_at_utc": start.isoformat(), "session_completed_at_utc": end.isoformat(),
        "session_status": obj["session_status"], "machine_source_status": source_status,
        "machine_data_asof_utc": asof, "machine_source_ref": obj.get("machine_source_ref"),
        "reviewed_signal_ids": signals, "decision_count": len(decisions),
        "answer_sha256": digest, "capture_payload_sha256": payload_digest, "assistant_final_text": answer,
        "captured_at_utc": now.isoformat(), "no_decision_reason": obj.get("no_decision_reason"),
        "capture_mode": "EXPLICIT_WRITE_NOT_NATIVE_AUTO_HOOK",
    }
    return [head] + [
        {**{k: v for k, v in d.items() if not k.startswith("_")}, "scan_id": sid}
        for d in decisions
    ]


def commit_jsonl(ledger, lines):
    if not ledger.exists():
        raise InputError("existing private ledger_header required; refusing implicit ledger creation")
    lockfile = ledger.with_name(ledger.name + ".lock")
    with lockfile.open("a+", encoding="utf-8") as lk:
        fcntl.flock(lk.fileno(), fcntl.LOCK_EX)
        contents = ledger.read_text(encoding="utf-8")
        try:
            old = [json.loads(l) for l in contents.splitlines() if l.strip()]
        except json.JSONDecodeError as ex:
            raise InputError("invalid existing ledger") from ex
        if not old or old[0].get("record_type") != "ledger_header":
            raise InputError("missing existing ledger_header")
        sid = lines[0]["scan_id"]
        for e in old:
            if e.get("record_type") == "scan_session" and e.get("scan_id") == sid:
                if e.get("capture_payload_sha256") == lines[0]["capture_payload_sha256"]:
                    return "ALREADY_RECORDED", 0
                raise InputError("scan_id re-used with different answer hash")
        known = {e.get("decision_id") for e in old if e.get("record_type") == "scan_decision"}
        for d in lines[1:]:
            if d["decision_id"] in known:
                raise InputError("duplicate decision_id across sessions")
        addition = "".join(json.dumps(d, sort_keys=True, ensure_ascii=False) + "\n" for d in lines)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=ledger.parent, prefix=".scan-", delete=False) as temp:
            temp_path = temp.name
            temp.write(contents + ("\n" if contents and not contents.endswith("\n") else "") + addition)
            temp.flush()
            os.fsync(temp.fileno())
        try:
            os.replace(temp_path, ledger)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
        return "RECORDED", len(lines) - 1


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    p.add_argument("--ledger", required=True)
    a = p.parse_args(argv)
    try:
        outside_public_repo(a.session)
        outside_public_repo(a.ledger)
        if Path(a.session).resolve() == Path(a.ledger).resolve():
            raise InputError("session and ledger path must differ")
        lines = validate_session(json.loads(Path(a.session).read_text(encoding="utf-8")), datetime.now(UTC))
        status, n = commit_jsonl(Path(a.ledger), lines)
        print(json.dumps({"status": status, "scan_id": lines[0]["scan_id"], "answer_sha256": lines[0]["answer_sha256"],
                          "decisions_added": n, "privacy": "PRIVATE_LEDGER_ONLY"}))
        return 0
    except (InputError, ValueError, OSError) as ex:
        print(f"SCAN_SESSION_CAPTURE_ERROR: {ex}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
