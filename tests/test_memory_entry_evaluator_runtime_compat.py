"""Regression: MEMORY_ENTRY evaluator must follow the shared V3 helper contract."""
from unittest.mock import patch

from scripts import update_solaire_memory_entry_challenger_evaluation as mod


def test_compatibility_context_is_ephemeral_and_well_formed():
    telemetry, retry_state = mod._evaluation_runtime_context()
    assert retry_state == {"entries": {}}
    assert telemetry["logical_attempts"] == 0
    assert telemetry["incomplete_market_counts"] == {}
    telemetry["logical_attempts"] = 99
    retry_state["entries"]["AAA"] = {"retry": True}
    new_telemetry, new_state = mod._evaluation_runtime_context()
    assert new_telemetry["logical_attempts"] == 0
    assert new_state["entries"] == {}


def test_main_passes_context_unpacks_tuple_and_does_not_persist_retry_state():
    event = {
        "event_type": "MEMORY_ENTRY_CHALLENGER_QUALIFIED",
        "architecture_version": mod.CHALLENGER_VERSION,
        "evaluations": {},
    }
    written = {}
    calls = []

    class FakeClient:
        def __init__(self, **kwargs):
            pass

        def get(self, path, **kwargs):
            assert path == "/time"
            return {"time": 123}

    def fake_read(path, fallback):
        return {"events": [event]} if path == mod.JOURNAL else {}

    def fake_evaluator(client, events, now, budget, errors, telemetry, retry_state):
        calls.append((events, budget, telemetry, retry_state))
        assert isinstance(client, FakeClient)
        assert telemetry["complete_results"] == 0
        assert retry_state == {"entries": {}}
        return 1, False

    with (
        patch.object(mod, "PublicClient", FakeClient),
        patch.object(mod, "read_json", side_effect=fake_read),
        patch.object(mod, "_evaluate_event_collection", side_effect=fake_evaluator),
        patch.object(mod, "atomic_json", side_effect=lambda path, obj: written.setdefault(path, obj)),
    ):
        assert mod.main() == 0

    assert len(calls) == 1
    assert calls[0][1] == mod.MAX_NEW_EVALUATIONS_PER_RUN
    assert written[mod.STATUS]["status"] == "OK"
    assert written[mod.STATUS]["new_complete_evaluations"] == 1
    assert written[mod.STATUS]["critical_error"] is None
    assert set(written) == {mod.JOURNAL, mod.COMPARISON, mod.STATUS}
