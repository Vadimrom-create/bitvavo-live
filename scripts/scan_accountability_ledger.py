#!/usr/bin/env python3
"""Evaluate *private*, timestamped ChatGPT SCAN decisions; no trading I/O.

Reads local JSONL supplied by the operator. Never contacts exchanges, sends
alerts, stores portfolio data in the public repository or changes live policy.
Output is an aggregate with explicit NON_MESURABLE when evidence is missing.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "scan_accountability_v1"
HORIZONS = (4, 24, 48, 72, 168)
ACTIONS = {"BUY", "WAIT_RECHECK", "REJECT_STRUCTURAL", "INSUFFICIENT_DATA"}
MACHINE_ACTIONS = {"ACHETE", "WATCH", "NONE", "UNKNOWN"}
UTC = timezone.utc


class InputError(ValueError):
    pass


def parse_utc(value, label):
    if not isinstance(value, str):
        raise InputError(f"{label}: UTC timestamp is required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as ex:
        raise InputError(f"{label}: invalid ISO timestamp") from ex
    if dt.tzinfo is None or dt.utcoffset().total_seconds() != 0:
        raise InputError(f"{label}: timestamp must specify UTC")
    return dt.astimezone(UTC)


def jsonl(path):
    if path is None:
        return []
    rows = []
    with open(path, encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as ex:
                raise InputError(f"{path}:{lineno}: invalid JSON") from ex
            if not isinstance(row, dict):
                raise InputError(f"{path}:{lineno}: JSON object required")
            if row.get("record_type") in {"ledger_header", "scan_session"}:
                continue
            rows.append(row)
    return rows


def validate_decisions(rows, asof):
    accepted, ids = [], set()
    for i, row in enumerate(rows, 1):
        if row.get("record_type") != "scan_decision":
            raise InputError(f"decision line {i}: record_type must be scan_decision")
        key = row.get("decision_id")
        if not isinstance(key, str) or not key.strip() or key in ids:
            raise InputError(f"decision line {i}: missing or duplicate decision_id")
        ids.add(key)
        market = row.get("market")
        if not isinstance(market, str) or not re.fullmatch(r"[A-Z0-9]+-EUR", market):
            raise InputError(f"{key}: invalid market")
        if row.get("chatgpt_action") not in ACTIONS:
            raise InputError(f"{key}: invalid chatgpt_action")
        if row.get("solaire_action") not in MACHINE_ACTIONS:
            raise InputError(f"{key}: invalid solaire_action")
        at = parse_utc(row.get("decision_at_utc"), f"{key}.decision_at_utc")
        observed = parse_utc(row.get("source_at_utc"), f"{key}.source_at_utc")
        if observed > at:
            raise InputError(f"{key}: source cannot be newer than decision")
        if at > asof:
            raise InputError(f"{key}: future decision (check --asof)")
        reasons = row.get("reason_codes")
        if not isinstance(reasons, list) or not reasons or any(not isinstance(x, str) or not x for x in reasons):
            raise InputError(f"{key}: nonempty reason_codes required")
        if row["chatgpt_action"] == "WAIT_RECHECK":
            if not isinstance(row.get("recheck_trigger"), str) or not row["recheck_trigger"]:
                raise InputError(f"{key}: WAIT_RECHECK requires recheck_trigger")
            parse_utc(row.get("recheck_due_utc"), f"{key}.recheck_due_utc")
        elif row.get("recheck_due_utc"):
            parse_utc(row["recheck_due_utc"], f"{key}.recheck_due_utc")
        accepted.append({**row, "_at": at, "_source_at": observed})
    return accepted


def validate_alerts(rows, asof):
    accepted, seen = [], set()
    for i, row in enumerate(rows, 1):
        if row.get("record_type") != "machine_alert":
            raise InputError(f"alert line {i}: invalid record_type")
        key = row.get("signal_id")
        if not isinstance(key, str) or not key.strip() or key in seen:
            raise InputError(f"alert line {i}: missing or duplicate signal_id")
        seen.add(key)
        market = row.get("market")
        if not isinstance(market, str) or not re.fullmatch(r"[A-Z0-9]+-EUR", market):
            raise InputError(f"alert line {i}: invalid market")
        at = parse_utc(row.get("signal_at_utc"), f"{key}.signal_at_utc")
        if at > asof:
            raise InputError(f"{key}: future alert")
        if row.get("action") not in MACHINE_ACTIONS:
            raise InputError(f"{key}: invalid alert action")
        accepted.append({**row, "_at": at})
    return accepted


def validate_pairs(rows, decision_ids):
    """Pairs are *externally* verified comparable executions, not inferred highs."""
    accepted, seen = [], set()
    for i, row in enumerate(rows, 1):
        if row.get("record_type") != "paired_outcome":
            raise InputError(f"pair line {i}: invalid record_type")
        key = row.get("decision_id")
        horizon = row.get("horizon_hours")
        if key not in decision_ids:
            raise InputError(f"pair line {i}: unknown decision_id")
        if type(horizon) is not int or horizon not in HORIZONS:
            raise InputError(f"pair line {i}: invalid horizon")
        if (key, horizon) in seen:
            raise InputError(f"pair line {i}: duplicate decision/horizon")
        seen.add((key, horizon))
        # A falsy or missing proof excludes the pair; it cannot be backfilled
        # from a token's maximum favorable excursion or a candle high.
        if not all(row.get(flag) is True for flag in (
            "both_executions_validated", "matched_budget_policy_costs",
            "horizon_matured", "independent_episode"
        )):
            continue
        a = row.get("solaire_net_eur")
        b = row.get("chatgpt_net_eur")
        if any(type(x) not in (float, int) or not (-1e9 < x < 1e9) for x in (a, b)):
            continue
        accepted.append((horizon, float(a), float(b), key))
    return accepted


def aggregate(decisions, alerts, pairs, asof):
    by_market = defaultdict(list)
    for row in decisions:
        by_market[row["market"]].append(row)
    for arr in by_market.values():
        arr.sort(key=lambda row: (row["_at"], row["decision_id"]))

    latest = {market: arr[-1] for market, arr in by_market.items()}
    machine_buy_rejected = [d for d in decisions if d["solaire_action"] == "ACHETE" and d["chatgpt_action"] != "BUY"]
    stale_source = [d["decision_id"] for d in decisions if (d["_at"] - d["_source_at"]).total_seconds() > 600]
    missing_liquidity = [d["decision_id"] for d in decisions if
        any(d.get(k) is None for k in ("spread_pct", "book_asof_utc", "roundtrip_150eur_pct"))]
    overdue = [d["decision_id"] for d in latest.values() if
        d["chatgpt_action"] == "WAIT_RECHECK" and parse_utc(d["recheck_due_utc"], "recheck_due_utc") < asof]

    alerts_after_refusal = []
    for market, d in latest.items():
        if d["chatgpt_action"] == "BUY":
            continue
        new = [a for a in alerts if
               a["market"] == market and a["action"] == "ACHETE" and a["_at"] > d["_at"]]
        if new:
            alerts_after_refusal.append({"market": market, "last_decision_id": d["decision_id"],
                                         "new_signal_ids": [a["signal_id"] for a in new]})

    pairs_by_horizon = {}
    for h in HORIZONS:
        grp = [(a, b) for horizon, a, b, _ in pairs if horizon == h]
        pairs_by_horizon[str(h)] = {
            "n": len(grp),
            "solaire_net_eur": round(sum(a for a, _ in grp), 4) if grp else None,
            "chatgpt_net_eur": round(sum(b for _, b in grp), 4) if grp else None,
            "chatgpt_minus_solaire_eur": round(sum(b - a for a, b in grp), 4) if grp else None,
            "verdict": "DESCRIPTIVE_ONLY" if grp else "NON_MESURABLE",
        }
    durations = [x.get("human_minutes") for x in decisions]
    known_time = [x for x in durations if type(x) in (int, float) and 0 <= x <= 1440]
    return {
        "schema": SCHEMA, "asof_utc": asof.isoformat(), "measurement_only": True,
        "decision_count": len(decisions), "markets": len(by_market),
        "machine_buy_refused_count": len(machine_buy_rejected),
        "machine_buy_refused_ids": [d["decision_id"] for d in machine_buy_rejected],
        "stale_source_over_10min_ids": stale_source,
        "missing_execution_evidence_ids": missing_liquidity,
        "overdue_recheck_ids": overdue,
        "unreviewed_new_machine_alerts": alerts_after_refusal,
        "decisions_without_time_measurement": len(durations) - len(known_time),
        "human_minutes_measured": round(sum(known_time), 2) if known_time else None,
        "paired_net": pairs_by_horizon,
        "chatgpt_value_verdict": "NON_MESURABLE" if not pairs else "PROVISIONAL_DESCRIPTIVE_ONLY",
        "limitations": [
            "No automatic capture of ChatGPT messages: records must be written after each SCAN.",
            "Missing archival book or verified fills => no realized counterfactual PnL.",
            "Paired outcomes are supplied and verified externally, not inferred from token price highs.",
            "Small or overlapping cohorts do not establish statistical superiority.",
        ],
    }


def outside_public_repo(path):
    if path is None:
        return
    repo_root = Path(__file__).resolve().parents[1]
    if Path(path).resolve().is_relative_to(repo_root):
        raise InputError(f"PRIVATE_DATA_IN_PUBLIC_REPO: {path}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions", required=True, help="private local JSONL, outside the public repository")
    parser.add_argument("--machine-alerts", help="optional JSONL of time-stamped historical machine signals")
    parser.add_argument("--pairs", help="optional private, independently verified paired outcome JSONL")
    parser.add_argument("--asof", help="explicit UTC cutoff (default: current UTC)")
    parser.add_argument("--output", help="optional aggregate JSON output; also outside public repository")
    args = parser.parse_args(argv)
    try:
        for path in (args.decisions, args.pairs, args.output):
            outside_public_repo(path)
        asof = parse_utc(args.asof, "--asof") if args.asof else datetime.now(UTC)
        decisions = validate_decisions(jsonl(args.decisions), asof)
        alerts = validate_alerts(jsonl(args.machine_alerts), asof)
        paired = validate_pairs(jsonl(args.pairs), {d["decision_id"] for d in decisions})
        report = aggregate(decisions, alerts, paired, asof)
        out = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(out, encoding="utf-8")
        print(out)
        return 0
    except (InputError, OSError) as ex:
        print(f"ACCOUNTABILITY_INPUT_ERROR: {ex}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
