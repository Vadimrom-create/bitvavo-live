#!/usr/bin/env python3
"""Read-only as-of evidence join: machine decisions vs archived Decision Layer.

Joins the last previously generated DL shadow to a production decision.
This is NOT a paired executable backtest. No trading or account side effects.
"""
from __future__ import annotations
import argparse
import bisect
import gzip
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

SCHEMA = "solaire_dl_asof_comparator_v1"
ALLOWED_ACTIONS = {
    "ACHETE_MAINTENANT", "PLACE_LIMITE_PASSIVE", "ATTENDS_REPRISE_OU_REENTREE",
    "LATENT_ACCELERATOR", "WATCH", "VETO_STRUCTUREL",
}

class EvidenceError(ValueError):
    pass

def utc_ts(value):
    if not isinstance(value, str) or not value:
        raise EvidenceError("missing UTC timestamp")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceError("invalid timestamp") from exc
    if dt.tzinfo is None or dt.utcoffset().total_seconds() != 0:
        raise EvidenceError("timestamp must explicitly be UTC")
    return dt.timestamp()

def read_events(source):
    if not isinstance(source, dict) or source.get("schema") != "solaire_prospective_journal_v1":
        raise EvidenceError("invalid production journal schema")
    if not isinstance(source.get("entries"), list):
        raise EvidenceError("missing event list")
    updated = source.get("updated_at_ts")
    if isinstance(updated, bool) or not isinstance(updated, (int, float)) or not math.isfinite(updated):
        raise EvidenceError("publication time missing")
    events, seen = [], set()
    for row in source["entries"]:
        if not isinstance(row, dict):
            raise EvidenceError("non-object decision")
        action = row.get("decision_type")
        if action not in ("BUY_SENT", "REJECTED"):
            raise EvidenceError("unsupported machine decision type")
        did, market, signal = row.get("decision_id"), row.get("market"), row.get("signal_id")
        if not all(isinstance(v, str) and v for v in (did, market, signal)):
            raise EvidenceError("missing event identity")
        if did in seen:
            raise EvidenceError("duplicate machine decision ID")
        seen.add(did)
        ts = row.get("decision_ts")
        if isinstance(ts, bool) or not isinstance(ts, (int, float)) or not math.isfinite(ts) or ts <= 0 or ts > updated + 1:
            raise EvidenceError("invalid/future event time")
        events.append({
            "decision_id": did, "signal_id": signal, "episode_id": row.get("episode_id"),
            "market": market, "decision_type": action, "decision_ts": float(ts),
        })
    return sorted(events, key=lambda x: (x["decision_ts"], x["decision_id"]))

def load_shadow_snapshots(directory, markets):
    items, failures = [], Counter()
    for path in sorted(Path(directory).glob("*/*.json.gz")):
        try:
            with gzip.open(path, "rt", encoding="utf-8") as stream:
                obj = json.load(stream)
            if obj.get("policy") != "DECISION_LAYER_V1_SHADOW":
                raise EvidenceError("unexpected shadow policy")
            available = utc_ts(obj.get("generated_at_utc"))
            scanned = utc_ts(obj.get("scan_at_utc"))
            if scanned > available:
                raise EvidenceError("snapshot generated before scan")
            rows = obj.get("ranked")
            if not isinstance(rows, list):
                raise EvidenceError("ranked decisions unavailable")
            per_market = {}
            for row in rows:
                if not isinstance(row, dict):
                    raise EvidenceError("non-object DL row")
                market = row.get("market")
                if market in markets:
                    if market in per_market:
                        raise EvidenceError("duplicate market in DL snapshot")
                    action = row.get("action")
                    if action not in ALLOWED_ACTIONS:
                        raise EvidenceError("unknown DL action")
                    per_market[market] = action
            items.append({
                "available_ts": available, "scan_ts": scanned,
                "source": str(path), "actions": per_market,
            })
        except (OSError, EOFError, ValueError, TypeError, KeyError) as exc:
            failures[type(exc).__name__] += 1
    # Corrupt/missing snapshots are counted, never silently made into DL rejections.
    return sorted(items, key=lambda o: (o["available_ts"], o["source"])), dict(failures)

def compare(events, shadows, max_age_seconds=3600):
    if not isinstance(max_age_seconds, int) or max_age_seconds <= 0:
        raise EvidenceError("max age must be positive")
    timestamps = [r["available_ts"] for r in shadows]
    if timestamps != sorted(timestamps):
        raise EvidenceError("snapshots must be ordered by availability")
    rows = []
    for event in events:
        # decision_ts = early sender timestamp, NOT email delivery timestamp.
        t = event["decision_ts"]
        i = bisect.bisect_right(timestamps, t) - 1
        state, action, age, source = "NO_PRIOR_SHADOW", None, None, None
        if i >= 0:
            shadow = shadows[i]
            age = round(t - shadow["available_ts"], 3)
            source = shadow["source"]
            if age > max_age_seconds:
                state = "STALE_SHADOW"
            elif event["market"] not in shadow["actions"]:
                state = "MARKET_MISSING_IN_SHADOW"
            else:
                state, action = "ASOF_MATCH", shadow["actions"][event["market"]]
        rows.append({
            "decision_id": event["decision_id"], "signal_id": event["signal_id"],
            "episode_id": event["episode_id"], "market": event["market"],
            "machine_action": event["decision_type"], "machine_ts": t,
            "join_status": state, "shadow_action": action,
            "shadow_age_seconds": age, "shadow_source": source,
            "shadow_publication_time_verified": False,
            "filled_order_proven": False, "executable_pnl_eur": None,
        })
    status = Counter(x["join_status"] for x in rows)
    matrix = Counter((x["machine_action"], x["shadow_action"]) for x in rows if x["join_status"] == "ASOF_MATCH")
    bought = [x for x in rows if x["machine_action"] == "BUY_SENT"]
    return {
        "schema": SCHEMA, "research_only": True,
        "max_shadow_age_seconds": max_age_seconds,
        "n_machine_decisions": len(rows), "n_machine_buy_sent": len(bought),
        "n_shadows": len(shadows),
        "join_status_counts": dict(sorted(status.items())),
        "buy_sent_join_status_counts": dict(sorted(Counter(x["join_status"] for x in bought).items())),
        "asof_action_matrix": [
            {"machine_action": m, "shadow_action": a, "n": count}
            for (m, a), count in sorted(matrix.items())
        ],
        "dl_causal_filter_effect_verified": False,
        "shadow_availability_at_signal_verified": False,
        "actual_fills_verified": 0, "paired_net_pnl_eur": None,
        "interpretation": "Generated-before-signal descriptive alignment only; Git publication time is unverified, no same-signal causal policy or executable PnL.",
        "rows": rows,
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--machine", default="production_direct_decision_journal.json")
    parser.add_argument("--decision-history", default="decision_history")
    parser.add_argument("--max-age-seconds", type=int, default=3600)
    parser.add_argument("--output", help="research JSON output; stdout summary otherwise")
    args = parser.parse_args(argv)
    try:
        source = json.loads(Path(args.machine).read_text(encoding="utf-8"))
        events = read_events(source)
        snaps, invalid = load_shadow_snapshots(args.decision_history, {e["market"] for e in events})
        report = compare(events, snaps, max_age_seconds=args.max_age_seconds)
        report["invalid_shadow_snapshot_counts"] = invalid
        report["historical_coverage_complete"] = False
        report["missing_archive_policy"] = "UNKNOWN_NOT_A_REJECTION"
        report["production_event_time_note"] = "decision_ts denotes sender start; email may arrive later."
        if args.output:
            Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False, indent=2))
        return 0
    except (EvidenceError, OSError, ValueError) as exc:
        parser.exit(2, "EVIDENCE_REJECTED: " + str(exc) + "\n")

if __name__ == "__main__":
    raise SystemExit(main())
