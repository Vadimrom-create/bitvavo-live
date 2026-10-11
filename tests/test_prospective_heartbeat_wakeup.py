from pathlib import Path

from research.prospective_cadence import begin, finish, slot_at
from scripts.prospective_heartbeat_wakeup import dispatch_decision


def test_bounded_heartbeat_wakeup_respects_active_collection():
    t = slot_at(20000) + 20
    assert dispatch_decision({}, t, active=False) == "DUE"
    assert dispatch_decision({}, t, active=True) == "ACTIVE_WORKFLOW_ALREADY_EXISTS"


def test_heartbeat_wakeup_does_not_duplicate_completed_slot():
    t = slot_at(20000) + 20
    state, attempt, _ = begin({}, t, "first")
    state, _, _ = finish(
        state, attempt, t + 20,
        {"v3": {"checked_at_utc": "1970-01-01T05:00:00+00:00", "status": "OK"}})
    # The deliberately ancient output is invalid, so the first try is FAILED.
    assert dispatch_decision(state, t + 30, active=False) == "RETRY_COOLDOWN"


def test_heartbeat_wakeup_does_not_touch_trading_gates():
    workflow = Path(".github/workflows/production_scan_fast.yml").read_text()
    script = Path("scripts/prospective_heartbeat_wakeup.py").read_text()
    assert "python scripts/prospective_heartbeat_wakeup.py" in workflow
    assert workflow.index("python scripts/send_production_buy_alert.py") < workflow.index(
        "python scripts/prospective_heartbeat_wakeup.py")
    assert workflow.index("python scripts/update_recovery_registry_heartbeat.py") < workflow.index(
        "python scripts/prospective_heartbeat_wakeup.py")
    assert "send_production_buy_alert" not in script
    assert "production_scan.py" not in script
    assert "orders_submitted" in script
