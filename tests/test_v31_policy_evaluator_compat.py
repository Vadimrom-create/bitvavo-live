from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path):
    return (ROOT / path).read_text(encoding="utf-8")


def test_v31_shared_evaluator_call_uses_new_context_and_unpacks_tuple():
    text = _text("scripts/update_solaire_v31_evaluation.py")
    assert "telemetry, retry_state = _evaluation_runtime_context()" in text
    assert "added, _ = _evaluate_event_collection(" in text
    assert "errors, telemetry, retry_state" in text


def test_policy_shared_evaluator_call_uses_new_context_and_unpacks_tuple():
    text = _text("scripts/update_solaire_policy_challengers_evaluation.py")
    assert "telemetry, retry_state = _evaluation_runtime_context()" in text
    assert "total_new, _ = _evaluate_event_collection(" in text
    assert "errors, telemetry, retry_state" in text


def test_v31_policy_compat_context_is_ephemeral_not_persisted():
    for path in (
        "scripts/update_solaire_v31_evaluation.py",
        "scripts/update_solaire_policy_challengers_evaluation.py",
    ):
        text = _text(path)
        assert 'return telemetry, {"entries": {}}' in text
        assert "solaire_v3_evaluation_retry_state.json" not in text
