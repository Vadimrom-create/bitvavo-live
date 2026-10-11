"""Adversarial recovery-registry compaction and performance regression tests."""
import copy
import gzip
import json
import subprocess

import pytest

from research.recovery_registry import (
    new_registry, register_episode, register_episode_inplace,
    observe_episode, observe_episode_inplace, summarize, summarize_inplace,
)
from scripts.archive_recovery_registry import run


def event(i, episode="same-" + "one"):
    return {
        "event_id": f"ABC-EUR|{i}", "market": "ABC-EUR",
        "rejected_ts": float(i), "source_episode_id": f"{episode}-{i}",
        "source_decision_id": f"decision-{i}", "first_rejection_reason": "SPREAD_TOO_WIDE",
        "rejection_price_eur": 1.0, "signal_state": "CONFIRMED_ACCELERATION",
        "signal_score": 7.0, "evidence_count": 4,
    }


def row(i=1):
    return {
        "market": "ABC-EUR", "episode": i, "last": 1.02,
        "signal_state": "CONFIRMED_ACCELERATION", "signal_score": 7.0,
        "acceleration": {"evidence_count": 4},
    }


def registered(i):
    return register_episode(new_registry(), event(i), row(), float(i) + 1)


def test_hot_path_matches_copy_on_write_for_transitions():
    cases = [
        (None, None, None),
        (row(), False, None),
        (row(), True, False),
        (row(), True, True),
        (row(episode=99), True, True),
    ]
    for signal, execution_pass, prior_clear in cases:
        base = registered(1000)
        expected = observe_episode(
            base, "ABC-EUR|1000", signal, 1100,
            execution_pass=execution_pass, execution_reason="SPREAD_TOO_WIDE",
            plan={"entry_eur": 1.03}, prior_thesis_clear=prior_clear,
        )
        actual = observe_episode_inplace(
            copy.deepcopy(base), "ABC-EUR|1000", signal, 1100,
            execution_pass=execution_pass, execution_reason="SPREAD_TOO_WIDE",
            plan={"entry_eur": 1.03}, prior_thesis_clear=prior_clear,
        )
        assert actual == expected
        assert summarize_inplace(actual) == summarize(expected)
    assert registered(1000)["episodes"]["ABC-EUR|1000"]["attempts"] == []


def test_register_hot_path_matches_public_wrapper():
    base = registered(1000)
    new = event(2000)
    expected = register_episode(base, new, row(), 2001.0)
    actual = register_episode_inplace(copy.deepcopy(base), new, row(), 2001.0)
    assert expected == actual
    assert len(base["episodes"]) == 1


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def small_registry():
    registry = new_registry()
    for i in (1000, 2000, 3000):
        registry = register_episode_inplace(registry, event(i), row(), i + 1.0)
        if i == 1000:
            registry = observe_episode_inplace(
                registry, f"ABC-EUR|{i}", None, i + 86401,
                execution_pass=None, execution_reason="SIGNAL_ABSENT_NOT_EVALUATED",
            )
        elif i == 2000:
            registry = observe_episode_inplace(
                registry, f"ABC-EUR|{i}", row(), i + 60,
                execution_pass=True, prior_thesis_clear=True,
                plan={"entry_eur": 1.02, "stop_eur": 0.97},
            )
    return registry


def setup_git(tmp_path, registry):
    git(tmp_path, "init")
    git(tmp_path, "config", "user.email", "test@example.com")
    git(tmp_path, "config", "user.name", "Solaire Test")
    (tmp_path / "production_recovery_registry_shadow.json").write_text(
        json.dumps(registry, separators=(",", ":"))
    )
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-m", "Original registry")


def test_archive_preserves_every_closed_attempt_and_summary(tmp_path):
    original = small_registry()
    setup_git(tmp_path, original)
    original_summary = summarize_inplace(original)
    batch = run(force=True, root=tmp_path, name="test.json.gz")
    active = json.loads((tmp_path / "production_recovery_registry_shadow.json").read_text())
    archive = json.loads(gzip.decompress((tmp_path / batch["path"]).read_bytes()))
    assert batch["archived_episodes"] == 2
    assert set(archive["episodes"]) == {"ABC-EUR|1000", "ABC-EUR|2000"}
    assert archive["episodes"]["ABC-EUR|2000"] == original["episodes"]["ABC-EUR|2000"]
    assert set(active["episodes"]) == {"ABC-EUR|3000"}
    assert summarize_inplace(active) == original_summary
    assert active["archive_summary"]["episodes"] == 2
    assert active["archive_batches"][-1]["source_commit"] == git(tmp_path, "rev-parse", "HEAD")
    assert run(root=tmp_path) is None

    # The closed event cannot be rediscovered after compression.
    same = dict(event(1000), event_id="ABC-EUR|1001", source_decision_id="another-decision")
    before = summarize_inplace(active)
    assert register_episode_inplace(active, same, row(), 1002) == active
    assert summarize_inplace(active) == before
    assert len(active["episodes"]) == 1


def test_tampered_uncommitted_source_is_rejected(tmp_path):
    registry = small_registry()
    setup_git(tmp_path, registry)
    p = tmp_path / "production_recovery_registry_shadow.json"
    p.write_text(p.read_text() + "\n")
    with pytest.raises(ValueError, match="SOURCE_REGISTRY_DIFFERS"):
        run(force=True, root=tmp_path, name="bad.json.gz")
    assert not (tmp_path / "recovery_registry_archives" / "bad.json.gz").exists()


def test_dry_run_never_writes(tmp_path):
    registry = small_registry()
    setup_git(tmp_path, registry)
    before = (tmp_path / "production_recovery_registry_shadow.json").read_bytes()
    batch = run(force=True, dry_run=True, root=tmp_path, name="dry.json.gz")
    assert batch["archived_episodes"] == 2
    assert (tmp_path / "production_recovery_registry_shadow.json").read_bytes() == before
    assert not (tmp_path / "recovery_registry_archives").exists()


def test_schema_drift_aborts_before_writes(tmp_path):
    registry = small_registry()
    registry["policy"]["ttl_seconds"] += 1
    setup_git(tmp_path, registry)
    with pytest.raises(ValueError, match="REGISTRY_SCHEMA_OR_POLICY_DRIFT"):
        run(force=True, root=tmp_path, name="invalid.json.gz")
    assert not (tmp_path / "recovery_registry_archives").exists()
