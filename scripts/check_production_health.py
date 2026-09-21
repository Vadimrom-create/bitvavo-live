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
HEALTH = "production_health.json"


def main() -> int:
    scan = read_json(SCAN, {})
    alert = read_json(ALERT, {})
    evaluation = read_json(EVALUATION, {})

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

    publish_outcome = os.getenv("SCAN_PUBLISH_OUTCOME", "success").lower()
    if publish_outcome != "success":
        warnings.append("SCAN_STATE_PUBLISH_FAILED_NONBLOCKING")

    overall = "DEGRADED" if critical else ("OK_WITH_WARNINGS" if warnings else "OK")
    report = {
        "checked_at_utc": utc(time.time()),
        "schema": "solaire_production_health_v1",
        "overall_status": overall,
        "critical_failures": critical,
        "warnings": warnings,
        "components": {
            "scan": scan.get("status"),
            "market_context": context_status or "NOT_REPORTED",
            "alert": alert.get("status"),
            "evaluation": evaluation.get("status") or "NOT_REPORTED",
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
            "scan_state_publish_outcome": publish_outcome,
        },
    }
    atomic_json(HEALTH, report)
    print("SOLAIRE_HEALTH " + json.dumps(report, ensure_ascii=False))
    return 1 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
