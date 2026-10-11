"""Adversarial regression checks for recovery-history preservation and batch math."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from research.common import read_json, utc, atomic_json
from research.recovery_storage import (
    RecoveryMigrationError, ensure_compressed_registry, MANIFEST_SCHEMA,
)
from research.recovery_registry import (
    new_registry, register_episode, observe_episode, summarize,
)


class TestLosslessRegistryMigration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.old = self.root / "production_recovery_registry_shadow.json"
        self.new = self.root / "production_recovery_registry_shadow.json.gz"
        self.manifest = self.root / "migration_manifest.json"
        self.document = new_registry()
        self.document["episodes"] = {
            "ABC-EUR|100": {"event_id": "ABC-EUR|100", "market": "ABC-EUR",
                            "state": "EXPIRED_24H", "closed": True,
                            "attempts": [{"at_ts": 100.0, "execution_pass": False},
                                         {"at_ts": 200.0, "execution_pass": True}]},
            "XYZ-EUR|300": {"event_id": "XYZ-EUR|300", "market": "XYZ-EUR",
                            "state": "BLOCKED_BUT_ALIVE", "closed": False,
                            "attempts": [{"at_ts": 300.0, "execution_pass": False}]},
        }
        atomic_json(self.old, self.document)

    def test_lossless_migration_preserves_all_attempts_and_digests(self):
        original = self.old.read_bytes()
        result = ensure_compressed_registry(self.old, self.new, self.manifest)
        self.assertEqual(result, "MIGRATED")
        self.assertFalse(self.old.exists())
        self.assertEqual(read_json(self.new), self.document)
        proof = read_json(self.manifest)
        self.assertEqual(proof["schema"], MANIFEST_SCHEMA)
        self.assertEqual(proof["source_sha256"], hashlib.sha256(original).hexdigest())
        self.assertEqual(proof["archive_sha256"], hashlib.sha256(self.new.read_bytes()).hexdigest())
        self.assertEqual(proof["episode_count"], 2)
        self.assertEqual(proof["attempt_count"], 3)
        self.assertTrue(proof["complete_round_trip_verified"])
        self.assertEqual(ensure_compressed_registry(self.old, self.new, self.manifest), "EXISTING")

    def test_interrupted_migration_reconciles_identical_both_files(self):
        atomic_json(self.new, self.document)
        self.assertFalse(self.manifest.exists())
        self.assertEqual(ensure_compressed_registry(self.old, self.new, self.manifest), "MIGRATED")
        self.assertFalse(self.old.exists())
        self.assertEqual(read_json(self.new), self.document)
        self.assertEqual(read_json(self.manifest)["episode_count"], 2)

    def test_divergent_compressed_copy_preserves_original(self):
        bad = copy.deepcopy(self.document)
        bad["episodes"].pop("ABC-EUR|100")
        atomic_json(self.new, bad)
        with self.assertRaises(RecoveryMigrationError):
            ensure_compressed_registry(self.old, self.new, self.manifest)
        self.assertTrue(self.old.exists())
        self.assertEqual(read_json(self.old), self.document)
        self.assertFalse(self.new.exists())

    def test_missing_source_refuses_to_invent_empty_history(self):
        self.old.unlink()
        with self.assertRaises(RecoveryMigrationError):
            ensure_compressed_registry(self.old, self.new, self.manifest)


class TestBatchCompatibility(unittest.TestCase):
    def _event(self):
        return {
            "event_id": "ABC-EUR|1000", "market": "ABC-EUR",
            "rejected_ts": 1000.0, "rejected_at_utc": utc(1000),
            "first_rejection_reason": "SPREAD_TOO_WIDE",
            "rejection_price_eur": 0.1,
            "source_episode_id": "episode_1",
            "source_decision_id": "decision_1",
        }

    def _row(self):
        return {
            "market": "ABC-EUR", "signal_state": "BUILDING_ACCELERATION",
            "signal_score": 6.7, "last": 0.1, "episode": 1,
            "acceleration": {"evidence_count": 4},
        }

    def test_batch_matches_copy_safe_calls_byte_equivalently(self):
        original = new_registry()
        event = self._event()
        row = self._row()
        copy_safe = register_episode(original, event, row, 1001.0)
        mutable = copy.deepcopy(original)
        updated = register_episode(mutable, event, row, 1001.0, _inplace=True)
        self.assertIs(updated, mutable)
        self.assertEqual(copy_safe, mutable)
        self.assertEqual(original["episodes"], {})

        for i, current in enumerate((None, row, None, row)):
            now = 1100.0 + i * 60
            kw = {
                "execution_pass": False, "execution_reason": "SPREAD_TOO_WIDE",
                "plan": None,
            }
            copy_safe = observe_episode(copy_safe, event["event_id"], current, now, **kw)
            updated = observe_episode(mutable, event["event_id"], current, now, _inplace=True, **kw)
            self.assertIs(updated, mutable)
            self.assertEqual(copy_safe, mutable)
        self.assertEqual(summarize(copy_safe), summarize(mutable, _inplace=True))

    def test_terminal_states_match_after_expiry(self):
        event = self._event()
        row = self._row()
        a = register_episode(new_registry(), event, row, 1001.0)
        b = copy.deepcopy(a)
        future = 1000.0 + 24 * 3600 + 1
        a = observe_episode(a, event["event_id"], None, future, execution_pass=None)
        observe_episode(b, event["event_id"], None, future, execution_pass=None, _inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(summarize(a), summarize(b, _inplace=True))
