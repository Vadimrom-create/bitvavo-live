#!/usr/bin/env python3
"""Read-only economic evidence gate for Solaire shadow measurements.

This is NOT a portfolio backtest. It validates already-published aggregate
shadow outcomes and prevents their promotion to real/executable PnL.
No Bitvavo calls, API credentials, private transactions, or order paths.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

EXIT_SCHEMA = "solaire_exit_policy_shadow_v3"
OOS_SCHEMA = "swing_selector_clean_oos_v1"
HORIZONS = ("4", "12", "24")
REFERENCE = "current_tp1_stop"
CANDIDATE = "full_1_4r"


class EvidenceError(ValueError):
    pass


def _object(value, label):
    if not isinstance(value, dict):
        raise EvidenceError(f"{label}: object required")
    return value


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise EvidenceError(f"{label}: finite number required")
    if not math.isfinite(value):
        raise EvidenceError(f"{label}: finite number required")
    return float(value)


def _count(value, label):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise EvidenceError(f"{label}: nonnegative integer required")
    return value


def _round(value):
    return round(value, 4)


def assess(exit_status, oos_status):
    x = _object(exit_status, "exit_status")
    s = _object(oos_status, "oos_status")
    if x.get("schema") != EXIT_SCHEMA or x.get("status") != "OK":
        raise EvidenceError("exit_status: expected OK v3 shadow schema")
    if s.get("schema") != OOS_SCHEMA:
        raise EvidenceError("oos_status: wrong schema")
    if not x.get("checked_at_utc") or not s.get("generated_at_utc"):
        raise EvidenceError("missing original evidence timestamps")
    summary = _object(x.get("summary"), "exit.summary")
    deltas = _object(x.get("comparisons_vs_current"), "exit.comparisons")
    rows = []
    for horizon in HORIZONS:
        cohorts = _object(summary.get(horizon), f"summary.{horizon}")
        ref = _object(cohorts.get(REFERENCE), f"summary.{horizon}.{REFERENCE}")
        new = _object(cohorts.get(CANDIDATE), f"summary.{horizon}.{CANDIDATE}")
        ref_n = _count(ref.get("n"), "reference.n")
        new_n = _count(new.get("n"), "candidate.n")
        if ref_n == 0 or ref_n != new_n:
            raise EvidenceError(f"horizon {horizon}: cohorts are not equally mature")
        baseline_pnl = _number(ref.get("sum_net_pnl_eur_est"), "reference.pnl")
        candidate_pnl = _number(new.get("sum_net_pnl_eur_est"), "candidate.pnl")
        ref_median = _number(ref.get("median_net_return_pct"), "reference.median")
        new_median = _number(new.get("median_net_return_pct"), "candidate.median")
        ref_positive = _count(ref.get("positive_net"), "reference.positive")
        new_positive = _count(new.get("positive_net"), "candidate.positive")
        ref_negative = _count(ref.get("negative_net"), "reference.negative")
        new_negative = _count(new.get("negative_net"), "candidate.negative")
        if ref_positive + ref_negative != ref_n or new_positive + new_negative != new_n:
            raise EvidenceError(f"horizon {horizon}: outcome count mismatch")
        published = _object(deltas.get(horizon), f"deltas.{horizon}")
        published = _object(published.get(CANDIDATE), "delta.1_4r")
        published_delta = _number(published.get("delta_sum_net_pnl_eur_est"), "delta.pnl")
        computed_delta = candidate_pnl - baseline_pnl
        if abs(computed_delta - published_delta) > 0.021:
            raise EvidenceError(f"horizon {horizon}: PnL sum/delta inconsistent")
        rows.append({
            "horizon_h": int(horizon),
            "same_mature_events_n": ref_n,
            "event_id_pairing_verified": False,
            "reference_sum_pnl_eur_est": _round(baseline_pnl),
            "candidate_1_4r_sum_pnl_eur_est": _round(candidate_pnl),
            "candidate_minus_reference_eur_est": _round(computed_delta),
            "reference_median_net_pct": _round(ref_median),
            "candidate_median_net_pct": _round(new_median),
            "candidate_positive_n": new_positive,
            "candidate_negative_n": new_negative,
            "candidate_positive_pct": _round(100 * new_positive / new_n),
            "provenance": "AGGREGATED_SHADOW_MODEL_ONLY",
            "portfolio_pnl_eur": None,
            "portfolio_drawdown_eur": None,
        })
    metrics = _object(s.get("metrics"), "oos.metrics")
    matured = {}
    for group in ("baseline", "swing_top10", "swing_human_review"):
        series = _object(metrics.get(group), f"oos.{group}")
        weekly = _object(series.get("168"), f"oos.{group}.168")
        matured[group] = _count(weekly.get("n"), f"oos.{group}.168.n")
    weekly_ready = min(matured.values()) > 0
    # Even >0 observations do not demonstrate statistical or economic validity.
    return {
        "schema": "solaire_economic_evidence_gate_v1",
        "measurement_only": True,
        "sources": {
            "exit_checked_at_utc": x["checked_at_utc"],
            "exit_study_id": x.get("study_id"),
            "oos_generated_at_utc": s["generated_at_utc"],
            "oos_version": s.get("version"),
        },
        "paired_exit_shadow_diagnostics": rows,
        "seven_day_mature_oos_n": matured,
        "seven_day_observations_exist": weekly_ready,
        "capital_test_eur": 2300,
        "net_executable_portfolio_pnl_eur": None,
        "actual_chatgpt_incremental_pnl_eur": None,
        "net_portfolio_drawdown_eur": None,
        "status": "NOT_IDENTIFIABLE_AS_EXECUTABLE_PORTFOLIO_PNL",
        "reasons": [
            "Aggregated exit shadow sums are not a capital-constrained equity ledger.",
            "Aggregated same-size cohorts do not independently prove event-ID pairing.",
            "No documented matched fills or portfolio cash, overlap and risk accounting.",
            "MFE/hit rates and positive cohort sums are not realized profit.",
            "ChatGPT decisions/fills are not yet privately paired to machine signals.",
            "No policy promotion, orders or production threshold changes are authorized.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--exit-status", default="production_exit_policy_shadow_status.json")
    p.add_argument("--oos-status", default="research/swing_selector_oos_latest.json")
    p.add_argument("--output", help="Optional research-only JSON output location")
    a = p.parse_args()
    try:
        exit_data = json.loads(Path(a.exit_status).read_text(encoding="utf-8"))
        oos_data = json.loads(Path(a.oos_status).read_text(encoding="utf-8"))
        result = assess(exit_data, oos_data)
        encoded = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if a.output:
            Path(a.output).write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
    except (EvidenceError, ValueError, OSError, json.JSONDecodeError) as exc:
        p.exit(2, f"economic evidence gate refused input: {exc}\n")


if __name__ == "__main__":
    main()
