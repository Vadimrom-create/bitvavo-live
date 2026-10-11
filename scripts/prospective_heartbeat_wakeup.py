#!/usr/bin/env python3
"""Bounded, nonblocking prospective dispatch from an already-running heartbeat.

No Bitvavo API, private wallet, BUY sender, final gate or order operations.
The existing prospective workflow remains the sole collector and owns the lock.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from research.common import read_json
from research.prospective_cadence import begin, health

TARGET = "solaire_prospective_shadows.yml"
ACTIVE_STATUSES = {"queued", "in_progress", "pending", "waiting", "requested"}


def dispatch_decision(state, now, active):
    # begin is pure with respect to the passed state (copies it internally).
    _, attempt, _ = begin(state, now, "probe_non_reserving")
    if not attempt["run"]:
        return attempt["reason"]
    if active:
        return "ACTIVE_WORKFLOW_ALREADY_EXISTS"
    return "DUE"


def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    state = read_json("prospective_collection_state.json", {}) or {}
    status = health(state, time.time())
    # Never add this check to the timing-critical scanner or sender.
    try:
        response = subprocess.run(
            ["gh", "api", f"/repos/{repo}/actions/workflows/{TARGET}/runs?per_page=50"],
            capture_output=True, text=True, check=True, timeout=8,
        )
        runs = json.loads(response.stdout).get("workflow_runs", [])
        active = any(r.get("status") in ACTIVE_STATUSES for r in runs)
        reason = dispatch_decision(state, time.time(), active)
        if reason == "DUE":
            subprocess.run(
                ["gh", "workflow", "run", TARGET, "--ref", "main",
                 "-f", "wakeup_source_run=" + run_id,
                 "-f", "wakeup_source_event=heartbeat_tick"],
                capture_output=True, text=True, check=True, timeout=8,
            )
    except (subprocess.SubprocessError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "WAKEUP_DEGRADED_NONBLOCKING",
                          "error": type(exc).__name__, "research_only": True}))
        return 0
    print(json.dumps({
        "status": "OK", "decision": reason, "active_workflow_found": active,
        "capture_health_at_check": status["status"],
        "research_only": True, "sender_called": False,
        "orders_submitted": False,
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
