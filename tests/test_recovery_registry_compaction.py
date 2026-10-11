"""Regression checks for lossless recovery archival and batch semantics."""
import copy
import gzip
import hashlib
import json
from pathlib import Path

import pytest

from research.recovery_registry import new_registry, observe_episode, register_episode, summarize
from scripts.recovery_registry_storage import ACTIVE, ARCHIVE_DIR, LEGACY, MANIFEST, load_registry, persist_registry


def event(i):
    return {"event_id": f"MKT-EUR|{i}", "market": "MKT-EUR",
            "source_episode_id": f"source-{i}", "source_decision_id": f"decision-{i}",
            "rejected_ts": 1000.0 + i, "rejection_price_eur": 1.0,
            "first_rejection_reason": "SPREAD_TOO_WIDE",
            "signal_state": "CONFIRMED_ACCELERATION",
            "signal_score": 7.0, "evidence_count": 4}


def row(i):
    return {"market": "MKT-EUR", "episode": i, "last": 1.01,
            "signal_state": "CONFIRMED_ACCELERATION", "signal_score": 7.0,
            "acceleration": {"evidence_count": 4}}


def test_batch_matches_legacy_behavior_and_public_calls_stay_pure():
    original = new_registry()
    baseline, optimized = original, new_registry()
    for i in range(65):
        baseline = register_episode(baseline, event(i), row(i), 1100.0)
        optimized = register_episode(optimized, event(i), row(i), 1100.0, _normalized=True)
    assert baseline == optimized
    previous = copy.deepcopy(baseline)
    for i in range(65):
        baseline = observe_episode(
            baseline, event(i)["event_id"], None, 1200.0, execution_pass=None
        )
        optimized = observe_episode(
            optimized, event(i)["event_id"], None, 1200.0,
            execution_pass=None, _normalized=True
        )
    assert baseline == optimized
    assert summarize(baseline) == summarize(optimized)
    assert previous["episodes"]["MKT-EUR|1"]["attempts"] == []
    assert original["episodes"] == {}


def test_lossless_migration_preserves_archive_bytes_and_all_episodes(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    original = new_registry()
    for i in range(20):
        original = register_episode(original, event(i), row(i), 1100.0 + i, _normalized=True)
    before = json.dumps(original, separators=(",", ":"), ensure_ascii=False).encode()
    LEGACY.write_bytes(before)
    live = copy.deepcopy(original)
    live["updated_at_utc"] = "2026-10-11T00:00:00+00:00"
    persist_registry(live)
    assert not LEGACY.exists()
    assert load_registry() == live
    manifest = json.loads(MANIFEST.read_text())
    archive = Path(manifest["archive_path"])
    assert archive.is_file()
    assert gzip.decompress(archive.read_bytes()) == before
    assert manifest["source_raw_bytes"] == len(before)
    assert manifest["source_sha256"] == hashlib.sha256(before).hexdigest()
    assert manifest["episode_count"] == len(original["episodes"])
    assert manifest["lossless_bytes_verified"] is True
    snapshots = sorted(p.name for p in ARCHIVE_DIR.iterdir())
    live["episodes"]["MKT-EUR|0"]["attempts"].append({"at_ts": 1200})
    persist_registry(live)
    assert load_registry() == live
    assert sorted(p.name for p in ARCHIVE_DIR.iterdir()) == snapshots


def test_ambiguous_dual_store_rejected(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    LEGACY.write_text('{"episodes":{}}')
    ACTIVE.write_bytes(gzip.compress(b'{"episodes":{}}'))
    with pytest.raises(RuntimeError, match="AMBIGUOUS"):
        load_registry()
    with pytest.raises(RuntimeError, match="AMBIGUOUS"):
        persist_registry({"episodes": {}})


def test_missing_store_cannot_silently_reset_history(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError, match="REFUSE_EMPTY_RESET"):
        load_registry()


def test_bad_source_cannot_delete_history(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    LEGACY.write_text('{"episodes":[]}')
    with pytest.raises(ValueError, match="INVALID_SOURCE"):
        persist_registry({"episodes": {}})
    assert LEGACY.exists()
    assert not ACTIVE.exists()
