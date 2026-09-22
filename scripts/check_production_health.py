#!/usr/bin/env python3
"""Make Solaire production degradation visible without coupling core components."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, read_json, utc

SCAN = "production_scan_status.json"
ALERT = "production_alert_status.json"
EVALUATION = "production_evaluation_status.json"
PERSISTENT_BUILDING = "production_persistent_building_status.json"
EARLY_BUILDING = "production_early_building_shadow_status.json"
V21_RANGE5 = "production_v21_range5_shadow_status.json"
REJECTION_SHADOW = "production_rejection_shadow_status.json"
ALL_ACTIONABLE = "production_all_actionable_shadow_status.json"
BREAKOUT_RISK = "production_breakout_risk_shadow_status.json"
EMERGING_LIQUIDITY = "production_emerging_liquidity_shadow_status.json"
EXIT_POLICY = "production_exit_policy_shadow_status.json"
HEALTH = "production_health.json"


def _shadow_warning(name: str, status: dict, env_name: str, warnings: list[str]) -> str:
    outcome = os.getenv(env_name, "success").lower()
    if outcome != "success" or status.get("status") not in (None, "OK"):
        warnings.append(name + "_DEGRADED_NONBLOCKING")
    return outcome


def main() -> int:
    scan = read_json(SCAN, {})
    alert = read_json(ALERT, {})
    evaluation = read_json(EVALUATION, {})
    persistent_building = read_json(PERSISTENT_BUILDING, {})
    early_building = read_json(EARLY_BUILDING, {})
    v21_range5 = read_json(V21_RANGE5, {})
    rejection_shadow = read_json(REJECTION_SHADOW, {})
    all_actionable = read_json(ALL_ACTIONABLE, {})
    breakout_risk = read_json(BREAKOUT_RISK, {})
    emerging_liquidity = read_json(EMERGING_LIQUIDITY, {})
    exit_policy = read_json(EXIT_POLICY, {})

    critical = []
    warnings = []

    if scan.get("status") != "OK":
        critical.append("SCAN_DEGRADED")
    active = int(scan.get("active_eur_markets") or 0)
    collected = int(scan.get("markets_collected") or 0)
    quality_pct = float(scan.get("quality_pct") or 0.0)
    if active and collected < active:
        critical.append("INCOMPLETE_MARKET_COVERAGE")
    if active and quality_pct < 95.0:
        critical.append("LOW_DATA_QUALITY")

    if alert.get("status") == "DEGRADED":
        critical.append("ALERT_PIPELINE_DEGRADED")

    context_status = scan.get("market_context_status")
    if context_status not in (None, "OK"):
        warnings.append("CONTEXT_DEGRADED_NONBLOCKING")

    if evaluation.get("status") not in (None, "OK"):
        warnings.append("EVALUATION_DEGRADED_NONBLOCKING")

    persistent_outcome = _shadow_warning(
        "PERSISTENT_BUILDING_SHADOW", persistent_building,
        "PERSISTENT_BUILDING_OUTCOME", warnings,
    )
    early_outcome = _shadow_warning(
        "EARLY_BUILDING_SHADOW", early_building,
        "EARLY_BUILDING_OUTCOME", warnings,
    )
    v21_outcome = _shadow_warning(
        "V21_RANGE5_SHADOW", v21_range5,
        "V21_RANGE5_OUTCOME", warnings,
    )
    rejection_outcome = _shadow_warning(
        "REJECTION_SHADOW", rejection_shadow,
        "REJECTION_SHADOW_OUTCOME", warnings,
    )
    all_actionable_outcome = _shadow_warning(
        "ALL_ACTIONABLE_SHADOW", all_actionable,
        "ALL_ACTIONABLE_OUTCOME", warnings,
    )
    breakout_risk_outcome = _shadow_warning(
        "BREAKOUT_RISK_SHADOW", breakout_risk,
        "BREAKOUT_RISK_OUTCOME", warnings,
    )
    emerging_liquidity_outcome = _shadow_warning(
        "EMERGING_LIQUIDITY_SHADOW", emerging_liquidity,
        "EMERGING_LIQUIDITY_OUTCOME", warnings,
    )
    exit_policy_outcome = _shadow_warning(
        "EXIT_POLICY_SHADOW", exit_policy,
        "EXIT_POLICY_OUTCOME", warnings,
    )

    publish_outcome = os.getenv("SCAN_PUBLISH_OUTCOME", "success").lower()
    if publish_outcome != "success":
        warnings.append("SCAN_STATE_PUBLISH_FAILED_NONBLOCKING")

    overall = "DEGRADED" if critical else ("OK_WITH_WARNINGS" if warnings else "OK")
    report = {
        "checked_at_utc": utc(time.time()),
        "schema": "solaire_production_health_v2",
        "overall_status": overall,
        "critical_failures": critical,
        "warnings": warnings,
        "components": {
            "scan": scan.get("status"),
            "market_context": context_status or "NOT_REPORTED",
            "alert": alert.get("status"),
            "evaluation": evaluation.get("status") or "NOT_REPORTED",
            "persistent_building_shadow": persistent_building.get("status") or "NOT_REPORTED",
            "early_building_shadow": early_building.get("status") or "NOT_REPORTED",
            "v21_range5_shadow": v21_range5.get("status") or "NOT_REPORTED",
            "rejection_shadow": rejection_shadow.get("status") or "NOT_REPORTED",
            "all_actionable_shadow": all_actionable.get("status") or "NOT_REPORTED",
            "breakout_risk_shadow": breakout_risk.get("status") or "NOT_REPORTED",
            "emerging_liquidity_shadow": emerging_liquidity.get("status") or "NOT_REPORTED",
            "exit_policy_shadow": exit_policy.get("status") or "NOT_REPORTED",
        },
        "coverage": {
            "active_eur_markets": active,
            "markets_collected": collected,
            "quality_pct": quality_pct,
        },
        "operational_dependencies": {
            "oracle_required": False,
            "railway_required": False,
            "v4_required": False,
            "decision_layer_required": False,
            "context_external_dependency": False,
            "evaluation_blocks_alerts": False,
            "all_shadows_block_anything": False,
            "persistent_building_step_outcome": persistent_outcome,
            "early_building_step_outcome": early_outcome,
            "v21_range5_step_outcome": v21_outcome,
            "rejection_shadow_step_outcome": rejection_outcome,
            "all_actionable_step_outcome": all_actionable_outcome,
            "breakout_risk_step_outcome": breakout_risk_outcome,
            "emerging_liquidity_step_outcome": emerging_liquidity_outcome,
            "exit_policy_step_outcome": exit_policy_outcome,
            "scan_state_publish_outcome": publish_outcome,
        },
    }
    atomic_json(HEALTH, report)
    print("SOLAIRE_HEALTH " + json.dumps(report, ensure_ascii=False))
    return 1 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
