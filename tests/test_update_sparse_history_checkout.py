from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPDATE = ROOT / ".github/workflows/update.yml"
HISTORICAL = ROOT / ".github/workflows/historical_evaluation.yml"


def test_live_update_uses_sparse_partial_clone_and_bounded_journals():
    text = UPDATE.read_text(encoding="utf-8")
    assert "sparse-checkout:" in text
    assert "sparse-checkout-cone-mode: true" in text
    assert "filter: blob:none" not in text
    assert "git sparse-checkout add" in text
    assert 'live_paths+=("history/$day")' in text
    assert 'live_paths+=("decision_history/$day")' in text
    assert "'3 days ago' '2 days ago' '1 day ago' 'today' 'tomorrow'" in text
    assert "'yesterday' 'today' 'tomorrow'" in text


def test_full_history_evaluator_remains_full_checkout():
    text = HISTORICAL.read_text(encoding="utf-8")
    assert "python pipeline.py --evaluate-only" in text
    assert "sparse-checkout:" not in text
