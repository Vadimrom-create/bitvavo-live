import os
import tempfile
from contextlib import contextmanager
from pathlib import Path

from research.common import atomic_json, read_json
from research.recovery_registry import new_registry
from research.recovery_storage import INDEX, fresh_index, reconstruct_and_verify, summarize_all
from scripts.rescue_recovery_registry import migrate, REGISTRY


@contextmanager
def _working_directory(p):
    previous = Path.cwd()
    os.chdir(p)
    try:
        yield
    finally:
        os.chdir(previous)


def test_emergency_rescue_preserves_all_closed_records_and_counters():
    with tempfile.TemporaryDirectory() as tmp, _working_directory(tmp):
        original = new_registry()
        for i in range(12):
            original["episodes"][f"event_{i}"] = {
                "market": "ABC-EUR", "state": "EXPIRED_24H", "closed": True,
                "source_episode_id": f"ep_{i}", "first_execution_pass": None,
                "attempts": [{"at_ts": i*100+j, "price": 1.0+j/1000}
                             for j in range(35)],
            }
        original["episodes"]["active"] = {
            "market": "ABC-EUR", "state": "BLOCKED_BUT_ALIVE",
            "closed": False, "attempts": [{"at_ts": 999}],
        }
        before = summarize_all(original, fresh_index())
        atomic_json(REGISTRY, original)
        result = migrate(minimum_bytes=0, run_id="test_emergency", source_blob_sha="fixture")
        assert result["result"] == "LOSSLESS_RESCUE_VERIFIED"
        assert result["archived_now"] == 12
        after = read_json(REGISTRY)
        index = read_json(INDEX)
        assert set(after["episodes"]) == {"active"}
        assert reconstruct_and_verify(after, index) == original["episodes"]
        assert summarize_all(after, index) == before
        assert migrate(minimum_bytes=1000000)["result"] == "BELOW_ARCHIVE_TRIGGER"


def test_emergency_never_changes_policy_or_bad_source():
    with tempfile.TemporaryDirectory() as tmp, _working_directory(tmp):
        data = new_registry()
        data["policy"]["ttl_seconds"] = 1
        atomic_json(REGISTRY, data)
        try:
            migrate(minimum_bytes=0, run_id="bad", source_blob_sha="fixture")
            assert False, "Policy drift must stop migration"
        except RuntimeError as exc:
            assert "POLICY_DRIFT" in str(exc)
        assert read_json(REGISTRY) == data
        assert not Path("production_recovery_archives").exists()
