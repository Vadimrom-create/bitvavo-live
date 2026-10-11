#!/usr/bin/env python3
"""Audit the retained public Solaire evaluation coverage. Strictly read-only.

No prices are downloaded and no hypothetical trade results are generated.
The legacy evaluator only attempts 4/12/24h with 400x5m candles per market.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PRODUCTION_HORIZONS = (4, 12, 24)
RESEARCH_HORIZONS = (24, 48, 72)
PRODUCTION_CANDLE_LIMIT = 400
PRODUCTION_CANDLE_MINUTES = 5
PRODUCTION_WINDOW_HOURS = PRODUCTION_CANDLE_LIMIT * PRODUCTION_CANDLE_MINUTES / 60


class AuditError(ValueError):
    pass


def ts(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        return None
    return float(value)


def parse_asof(value):
    if not isinstance(value, str):
        raise AuditError("asof must be timezone-aware UTC")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AuditError("invalid UTC asof") from exc
    if parsed.tzinfo is None or parsed.utcoffset().total_seconds() != 0:
        raise AuditError("asof must be UTC")
    return parsed.timestamp()


def valid_source(doc, label):
    if not isinstance(doc, dict) or doc.get("schema") != "solaire_prospective_journal_v1":
        raise AuditError(f"{label}: unexpected schema")
    if not isinstance(doc.get("entries"), list):
        raise AuditError(f"{label}: missing entries")
    return doc["entries"]


def uid(entry):
    d = entry.get("decision_id")
    if isinstance(d, str) and d.strip():
        return "decision:" + d
    # Legacy journal records without ID: sufficient for measuring row coverage,
    # NOT proof that two distinct episodes are the same economic trade.
    return "legacy:" + "|".join(str(entry.get(k) or "") for k in
                               ("cycle_id", "market", "decision_type", "reason"))


def audit(journal, direct, asof_ts):
    normal = valid_source(journal, "production journal")
    fast = valid_source(direct, "direct journal")
    by_key = {}
    duplicates = 0
    for source_name, rows in (("canonical", normal), ("direct", fast)):
        for index, item in enumerate(rows):
            if not isinstance(item, dict):
                raise AuditError(f"{source_name} entry {index} invalid")
            event_ts = ts(item.get("decision_ts"))
            if event_ts is None or event_ts <= 0 or event_ts > asof_ts:
                raise AuditError(f"{source_name} entry {index}: future/missing decision timestamp")
            key = uid(item)
            if key in by_key:
                duplicates += 1
                kept = by_key[key]
                # Prefer the first source for provenance, union only recorded
                # evaluations with explicit populated dict values.
                for horizon, outcome in (item.get("evaluations") or {}).items():
                    if isinstance(outcome, dict) and outcome and horizon not in kept["evaluations"]:
                        kept["evaluations"][horizon] = outcome
                continue
            by_key[key] = {
                "decision_type": item.get("decision_type"),
                "decision_ts": event_ts,
                "evaluations": {
                    str(k): v for k, v in (item.get("evaluations") or {}).items()
                    if isinstance(v, dict) and v
                },
                "origin": source_name,
            }

    summaries = {}
    for hours in sorted(set(PRODUCTION_HORIZONS) | set(RESEARCH_HORIZONS)):
        mature = 0
        recorded = 0
        outside_400 = 0
        not_mature = 0
        by_action = Counter()
        for row in by_key.values():
            if row["decision_type"] not in ("BUY_SENT", "REJECTED"):
                continue
            if asof_ts < row["decision_ts"] + hours * 3600:
                not_mature += 1
                continue
            mature += 1
            by_action[row["decision_type"]] += 1
            if str(hours) in row["evaluations"]:
                recorded += 1
            elif asof_ts - row["decision_ts"] > PRODUCTION_WINDOW_HOURS * 3600:
                outside_400 += 1

        summaries[str(hours)] = {
            "pipeline_supports_horizon": hours in PRODUCTION_HORIZONS,
            "matured": mature,
            "not_mature": not_mature,
            "recorded_evaluation_count": recorded,
            "mature_missing_evaluation_count": mature - recorded,
            "recorded_evaluation_coverage_pct": round(100 * recorded / mature, 2) if mature else None,
            "missing_and_now_older_than_400_candles": outside_400,
            "matured_by_machine_decision_type": dict(sorted(by_action.items())),
        }

    return {
        "schema": "solaire_public_evaluation_coverage_audit_v1",
        "asof_utc": datetime.fromtimestamp(asof_ts, timezone.utc).isoformat(),
        "source": ["production_decision_journal.json", "production_direct_decision_journal.json"],
        "mode": "RESEARCH_ONLY_READ_ONLY",
        "canonical_retained_rows": len(normal),
        "direct_retained_rows": len(fast),
        "overlap_rows": duplicates,
        "unique_retained_machine_decisions": len(by_key),
        "production_horizons_hours": list(PRODUCTION_HORIZONS),
        "research_requested_horizons_hours": list(RESEARCH_HORIZONS),
        "production_5m_candle_request_limit": PRODUCTION_CANDLE_LIMIT,
        "production_max_window_hours_approx": round(PRODUCTION_WINDOW_HOURS, 4),
        "horizons": summaries,
        "limitations": [
            "Snapshot of RETAINED journal records, not necessarily all historical episodes.",
            "A missing evaluation is UNKNOWN, never a losing or winning trade.",
            "The 400-candle time window is a structural limitation of the current evaluator, not proof a result cannot be recovered via archives.",
            "The production evaluator does not support 48h/72h, even if research shadows elsewhere do.",
            "This audit cannot infer live fills, return net of fees, or ChatGPT decision value.",
            "No market API requests, wallet access, secrets, trading changes, or persistence.",
        ],
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--canonical", required=True)
    p.add_argument("--direct", required=True)
    p.add_argument("--asof", required=True, help="explicit ISO UTC evidence cutoff")
    p.add_argument("--output", help="optional write path; research output only")
    a = p.parse_args(argv)
    try:
        canonical = json.loads(Path(a.canonical).read_text(encoding="utf-8"))
        direct = json.loads(Path(a.direct).read_text(encoding="utf-8"))
        res = audit(canonical, direct, parse_asof(a.asof))
        output = json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if a.output:
            Path(a.output).parent.mkdir(parents=True, exist_ok=True)
            Path(a.output).write_text(output, encoding="utf-8")
        print(output)
        return 0
    except (AuditError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"EVALUATION_COVERAGE_AUDIT_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
