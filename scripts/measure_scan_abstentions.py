#!/usr/bin/env python3
"""Private, read-only 24/48/72h SCAN decision and abstention accountability.

Extends scan_accountability_ledger without changing the live trading system.
Never infers executable profit from candle highs, midpoint prices or missing fills.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scan_accountability_ledger import (
    InputError, jsonl, outside_public_repo, parse_utc,
    validate_decisions, validate_pairs,
)

SCHEMA = "scan_abstention_accountability_v1"
HORIZONS = (24, 48, 72)
CATEGORIES = {
    "BUY": "ACHAT_TEST",
    "WAIT_RECHECK": "ATTENDRE_CONFIRMATION",
    "REJECT_STRUCTURAL": "ECARTER",
    "INSUFFICIENT_DATA": "NON_CLASSABLE",
}


def category_of(decision):
    """Backward-compatible taxonomy: an explicit category cannot contradict action."""
    expected = CATEGORIES[decision["chatgpt_action"]]
    explicit = decision.get("decision_category")
    if explicit is not None and explicit != expected:
        raise InputError(
            f"{decision['decision_id']}: decision_category {explicit!r} "
            f"contradicts chatgpt_action {decision['chatgpt_action']!r}"
        )
    return expected, "EXPLICIT" if explicit is not None else "LEGACY_INFERRED"


def verified_pairs(rows, decisions, asof):
    """Validate proofs and maturity before including any paired economic value."""
    ids = {d["decision_id"] for d in decisions}
    by_id = {d["decision_id"]: d for d in decisions}
    validated = validate_pairs(rows, ids)
    permitted = {}
    for horizon, solaire, chatgpt, decision_id in validated:
        if horizon not in HORIZONS:
            continue
        due = by_id[decision_id]["_at"] + timedelta(hours=horizon)
        # A claimed "horizon_matured" flag cannot bypass the actual clock.
        if asof < due:
            continue
        original = next(
            r for r in rows
            if r.get("decision_id") == decision_id
            and r.get("horizon_hours") == horizon
        )
        evidence_at = original.get("evidence_observed_at_utc")
        if evidence_at is not None:
            observed = parse_utc(evidence_at, "evidence_observed_at_utc")
            if observed < due or observed > asof:
                # The proof must have been observable after maturity, before cutoff.
                continue
        permitted[(decision_id, horizon)] = (solaire, chatgpt)
    return permitted


def report(decision_rows, paired_rows, asof):
    decisions = validate_decisions(decision_rows, asof)
    pairs = verified_pairs(paired_rows, decisions, asof)
    counts = Counter()
    category_origin = Counter()
    rows = []
    matured_counts = Counter()
    verified_counts = Counter()
    comparative = {}

    for d in decisions:
        category, origin = category_of(d)
        counts[category] += 1
        category_origin[origin] += 1
        market = d["market"]
        is_machine_buy = d["solaire_action"] == "ACHETE"
        horizons = {}
        for hours in HORIZONS:
            due = d["_at"] + timedelta(hours=hours)
            key = (d["decision_id"], hours)
            if asof < due:
                status = "NOT_MATURE"
            elif key in pairs:
                status = "VERIFIED_PAIRED_NET"
            else:
                status = "MATURE_NO_VERIFIED_PAIR"

            horizons[str(hours)] = {
                "due_at_utc": due.isoformat(),
                "status": status,
                "solaire_net_eur": pairs[key][0] if status == "VERIFIED_PAIRED_NET" else None,
                "chatgpt_net_eur": pairs[key][1] if status == "VERIFIED_PAIRED_NET" else None,
                "chatgpt_minus_solaire_eur": round(pairs[key][1] - pairs[key][0], 4)
                if status == "VERIFIED_PAIRED_NET" else None,
            }
            # Economic coverage is reported only for actual machine BUY signals.
            if is_machine_buy and asof >= due:
                matured_counts[(category, hours)] += 1
                if status == "VERIFIED_PAIRED_NET":
                    verified_counts[(category, hours)] += 1
                    comparative.setdefault((category, hours), []).append(pairs[key])

        rows.append({
            "decision_id": d["decision_id"],
            "market": market,
            "decision_at_utc": d["_at"].isoformat(),
            "source_at_utc": d["_source_at"].isoformat(),
            "source_age_seconds": round((d["_at"] - d["_source_at"]).total_seconds(), 1),
            "machine_action": d["solaire_action"],
            "assistant_action": d["chatgpt_action"],
            "category": category,
            "category_provenance": origin,
            "reason_codes": d["reason_codes"],
            "recheck_trigger": d.get("recheck_trigger"),
            "recheck_due_utc": d.get("recheck_due_utc"),
            "comparability_scope": "MACHINE_BUY" if is_machine_buy else "OUTSIDE_MACHINE_BUY",
            "horizons": horizons,
        })

    comparisons = {}
    for category in CATEGORIES.values():
        cat = {}
        for hours in HORIZONS:
            m = matured_counts[(category, hours)]
            n = verified_counts[(category, hours)]
            sample = comparative.get((category, hours), [])
            cat[str(hours)] = {
                "matured_machine_buy_decisions": m,
                "verified_paired_decisions": n,
                "verified_pair_coverage_pct": round(100.0 * n / m, 2) if m else None,
                "sum_solaire_net_eur": round(sum(a for a, _ in sample), 4) if sample else None,
                "sum_chatgpt_net_eur": round(sum(b for _, b in sample), 4) if sample else None,
                "chatgpt_minus_solaire_eur": round(sum(b - a for a, b in sample), 4)
                if sample else None,
                "verdict": "DESCRIPTIVE_ONLY" if sample else "NON_MESURABLE",
            }
        comparisons[category] = cat

    return {
        "schema": SCHEMA,
        "asof_utc": asof.isoformat(),
        "measurement_only": True,
        "changes_trading_policy": False,
        "decision_count": len(rows),
        "machine_buy_decision_count": sum(x["solaire_action"] == "ACHETE" for x in decisions),
        "categories": dict(sorted(counts.items())),
        "category_provenance": dict(sorted(category_origin.items())),
        "decisions": rows,
        "comparison_by_category_and_horizon": comparisons,
        "limitations": [
            "No native ChatGPT capture: SCAN decisions require explicit private recording.",
            "No private wallet data or order execution is read or written by this script.",
            "Comparative PnL requires independently verified, matched, executable pairs.",
            "Price increases following an abstention are not proof of a realizable profit.",
            "Overlapping episodes, missing pairs and selection bias prohibit causal claims.",
            "This report does not authorize trades, modify thresholds or send orders.",
        ],
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--decisions", required=True, help="private JSONL, outside public repo")
    p.add_argument("--pairs", help="optional independently verified paired outcomes JSONL")
    p.add_argument("--asof", help="UTC cutoff; default current time")
    p.add_argument("--output", help="optional private aggregate JSON output")
    a = p.parse_args(argv)
    try:
        for path in (a.decisions, a.pairs, a.output):
            outside_public_repo(path)
        asof = parse_utc(a.asof, "--asof") if a.asof else datetime.now(timezone.utc)
        result = report(jsonl(a.decisions), jsonl(a.pairs), asof)
        payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if a.output:
            Path(a.output).parent.mkdir(parents=True, exist_ok=True)
            Path(a.output).write_text(payload, encoding="utf-8")
        print(payload)
        return 0
    except (InputError, ValueError, OSError) as exc:
        print(f"SCAN_ABSTENTION_ACCOUNTABILITY_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
