import copy
import hashlib
from pathlib import Path

import pytest

from research.recovery_registry import (
    POLICY, new_registry, normalize_registry, observe_episode,
    register_episode, summarize,
)
from research.recovery_storage import (
    SCHEMA, compact_closed, fresh_index, reconstruct_and_verify, summarize_all,
)


def _closed(i):
    return {
        "market": "ABC-EUR",
        "closed": True,
        "state": "EXPIRED_24H" if i % 2 else "SHADOW_RECOVERY_CANDIDATE",
        "source_episode_id": "episode_" + str(i),
        "source_decision_id": "decision_" + str(i),
        "first_execution_pass": {"at_ts": 100.0} if i % 2 else None,
        "attempts": [{"at_ts": 100 + j, "price": 0.9 + j / 10000}
                     for j in range(20)],
    }


def _open(i):
    return {
        "market": "ABC-EUR", "closed": False, "state": "BLOCKED_BUT_ALIVE",
        "attempts": [{"at_ts": i}], "source_episode_id": "open_" + str(i),
    }


def test_lossless_shards_and_identical_summary(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    r = new_registry()
    r["episodes"] = {("event_%04d" % i): _closed(i) for i in range(137)}
    r["episodes"]["open_1"] = _open(1)
    r["episodes"]["open_2"] = _open(2)
    original = copy.deepcopy(r)
    old_status = summarize(original)
    live, index, diagnostic = compact_closed(
        r, fresh_index(), run_id="test001", source_bytes=95_000_000,
        source_blob_sha="git_sha_reference", force=True,
    )
    assert diagnostic["status"] == "ARCHIVED_VERIFIED"
    assert diagnostic["archived_now"] == 137
    assert len(diagnostic["shards"]) == 3
    assert len(live["episodes"]) == 2
    assert index["archived_total"] == 137
    assert index["archives"][0]["source_blob_sha"] == "git_sha_reference"
    assert "ABC-EUR\x1fepisode_1" in index["archived_source_episode_identities"]
    assert "ABC-EUR\x1fdecision_1" in index["archived_source_decision_identities"]
    assert reconstruct_and_verify(live, index) == original["episodes"]
    assert summarize_all(live, index) == old_status
    assert all(Path(p).stat().st_size > 0 for p in diagnostic["shards"])


def test_archive_detects_mutated_shard(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    r = new_registry()
    r["episodes"] = {"one": _closed(1)}
    live, index, d = compact_closed(r, fresh_index(), run_id="tamper", force=True)
    path = Path(d["shards"][0])
    content = bytearray(path.read_bytes())
    content[-1] ^= 1
    path.write_bytes(content)
    with pytest.raises(RuntimeError, match="SHA256_MISMATCH"):
        reconstruct_and_verify(live, index)


def test_compaction_skips_when_not_due(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    r = new_registry()
    r["episodes"]["one"] = _closed(1)
    live, index, d = compact_closed(r, fresh_index(), run_id="skip")
    assert d["status"] == "NOT_DUE"
    assert "one" in live["episodes"]
    assert index["archived_total"] == 0


def test_inplace_and_legacy_public_apis_produce_equivalent_results():
    event = {
        "event_id": "ABC-EUR|1000", "market": "ABC-EUR",
        "rejected_ts": 1000.0, "source_episode_id": "ep",
        "source_decision_id": "dec", "first_rejection_reason": "SPREAD_TOO_WIDE",
        "rejection_price_eur": 1.0,
    }
    row = {
        "market": "ABC-EUR", "episode": 1, "last": 1.01,
        "signal_state": "CONFIRMED_ACCELERATION", "signal_score": 7.0,
        "acceleration": {"evidence_count": 4},
    }
    original = new_registry()
    legacy = register_episode(original, event, row, 1001.0)
    fast = register_episode(normalize_registry(original), event, row, 1001.0, inplace=True)
    assert legacy == fast
    assert original["episodes"] == {}
    for at, source, passed, prior in [
        (1200.0, None, None, None),
        (1300.0, row, True, False),
        (1400.0, row, True, True),
    ]:
        options = {"execution_pass": passed, "prior_thesis_clear": prior,
                   "plan": {"entry_eur": 1.02, "stop_eur": 0.98} if source else None}
        legacy = observe_episode(legacy, event["event_id"], source, at, **options)
        fast = observe_episode(fast, event["event_id"], source, at,
                               inplace=True, **options)
        assert legacy == fast
    assert fast["episodes"][event["event_id"]]["closed"] is True
    assert fast["episodes"][event["event_id"]]["proposal_count"] == 1


def test_inplace_requires_normalized_registry():
    with pytest.raises(ValueError, match="NORMALIZED"):
        observe_episode({"episodes": {}}, "x", None, 1,
                        execution_pass=None, inplace=True)
