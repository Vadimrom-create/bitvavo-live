from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WATCHDOG = ROOT / ".github/workflows/production_scan_watchdog.yml"
HEARTBEAT = ROOT / ".github/workflows/production_scan_fast.yml"


def _text(path):
    return path.read_text(encoding="utf-8")


def _job_block(text, job_name):
    marker = f"  {job_name}:\n"
    start = text.index(marker)
    tail = text[start + len(marker):]
    match = re.search(r"\n  [A-Za-z0-9_-]+:\n", tail)
    end = start + len(marker) + (match.start() if match else len(tail))
    return text[start:end]


def test_watchdog_has_no_workflow_level_publisher_concurrency():
    text = _text(WATCHDOG)
    jobs_pos = text.index("\njobs:\n")
    pre_jobs = text[:jobs_pos]
    assert "bitvavo-production-heartbeat-v1" not in pre_jobs


def test_freshness_observer_never_takes_heartbeat_lock():
    block = _job_block(_text(WATCHDOG), "production-freshness")
    assert "bitvavo-production-heartbeat-v1" not in block
    assert "outputs:" in block
    assert "stale:" in block


def test_freshness_observer_sparse_checkout_only_reads_status_files():
    block = _job_block(_text(WATCHDOG), "production-freshness")
    assert "sparse-checkout:" in block
    assert "production_scan_status.json" in block
    assert "production_recovery_registry_status.json" in block
    assert "sparse-checkout-cone-mode: false" in block
    assert "scripts/" not in block.split("Observe production scan freshness", 1)[0]
    assert "history/" not in block
    assert "decision_history/" not in block


def test_only_stale_rescue_enters_heartbeat_publisher_lock():
    block = _job_block(_text(WATCHDOG), "rescue-if-stale")
    assert "needs: production-freshness" in block
    assert "if: needs.production-freshness.outputs.stale == 'true'" in block
    assert "group: bitvavo-production-heartbeat-v1" in block
    assert "cancel-in-progress: false" in block


def test_rescue_rechecks_freshness_after_lock_before_scan_and_publish():
    block = _job_block(_text(WATCHDOG), "rescue-if-stale")
    recheck = block.index("Recheck freshness under publisher lock")
    scan = block.index("Run one rescue production scan")
    persist = block.index("Persist rescued production state")
    assert recheck < scan < persist
    assert "git reset --hard origin/main" in block
    assert block.count("if: steps.recheck.outputs.stale == 'true'") == 2


def test_heartbeat_keeps_same_single_publisher_lock():
    text = _text(HEARTBEAT)
    assert "group: bitvavo-production-heartbeat-v1" in text
    assert "cancel-in-progress: false" in text


def test_heartbeat_primary_cadence_self_chains_without_cron():
    text = _text(HEARTBEAT)
    assert "workflow_dispatch:" in text
    assert "actions: write" in text
    assert "Hand off to next heartbeat run" in text
    assert "/actions/workflows/production_scan_fast.yml/dispatches" in text
    assert "-f ref=main" in text
    assert "Another heartbeat is already queued/in progress" in text
    # Cron remains only as a coarse cold-start fallback, not the 5-minute driver.
    assert "cron: '4 * * * *'" in text
    assert "4,19,34,49" not in text


def test_watchdog_restarts_failed_heartbeat_outside_schedule_domain():
    text = _text(WATCHDOG)
    assert "workflow_run:" in text
    assert "'Solaire direct Bitvavo scan heartbeat'" in text
    block = _job_block(text, "restart-heartbeat-chain")
    assert "github.event_name == 'workflow_run'" in block
    assert "github.event.workflow_run.conclusion != 'success'" in block
    assert "actions: write" in block
    assert "/actions/workflows/production_scan_fast.yml/dispatches" in block
    assert "Heartbeat already queued/in progress" in block


def test_watchdog_stale_observation_can_restart_chain():
    block = _job_block(_text(WATCHDOG), "restart-heartbeat-chain")
    assert "needs: production-freshness" in block
    assert "needs.production-freshness.outputs.stale == 'true'" in block
    assert "needs.production-freshness.outputs.registry_stale == 'true'" in block
    assert "MAX_RECOVERY_REGISTRY_AGE_SECONDS: '900'" in _text(WATCHDOG)


def test_watchdog_keeps_prospective_anti_recursion_barrier():
    block = _job_block(_text(WATCHDOG), "prospective-wakeup")
    assert "github.event_name == 'schedule'" in block
    assert "github.event_name == 'workflow_dispatch'" in block
    assert "github.event_name == 'push'" in block
    assert "workflow_run" not in block


def test_prospective_wakeup_sparse_checkout_only_includes_runtime_dependencies():
    block = _job_block(_text(WATCHDOG), "prospective-wakeup")
    assert "sparse-checkout:" in block
    for path in (
        "scripts/prospective_wakeup.py",
        "research/common.py",
        "research/prospective_cadence.py",
        "prospective_collection_state.json",
        "prospective_collection_health.json",
    ):
        assert path in block
    assert "history/" not in block
    assert "decision_history/" not in block
