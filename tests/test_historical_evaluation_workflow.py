from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/historical_evaluation.yml"
UPDATE = ROOT / ".github/workflows/update.yml"


def test_full_history_evaluation_is_research_only_and_separate_from_live_update():
    workflow = WORKFLOW.read_text(encoding="utf-8")
    update = UPDATE.read_text(encoding="utf-8")

    assert "python pipeline.py --evaluate-only" in workflow
    assert "git add evaluation.json" in workflow
    assert "send_production_buy_alert.py" not in workflow
    assert "send_useful_alert.py" not in workflow
    assert "production_scan.py" not in workflow
    assert "pipeline.py --evaluate-only" not in update


def test_full_history_evaluation_runs_at_most_hourly_by_schedule():
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "cron: '28 * * * *'" in workflow
