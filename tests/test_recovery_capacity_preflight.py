"""Capacity preflight: archive before guard, without ever discarding evidence."""
import copy
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.common import atomic_json, read_json
from research.recovery_registry import new_registry, summarize
from research.recovery_storage import reconstruct_and_verify, summarize_all
from scripts import update_recovery_registry_heartbeat as mod


class TestCapacityArchivePreflight(unittest.TestCase):
    def setUp(self):
        self.previous = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.previous)
        self.temp.cleanup()

    def sample(self):
        r = new_registry()
        for i in range(130):
            r["episodes"]["closed_" + str(i)] = {
                "market": "ABC-EUR", "closed": True, "state": "EXPIRED_24H",
                "source_episode_id": "episode_" + str(i),
                "source_decision_id": "decision_" + str(i),
                "first_execution_pass": None,
                "attempts": [{"at_ts": j, "price": 0.01 + j / 10000}
                             for j in range(10)],
            }
        r["episodes"]["open"] = {
            "market": "ABC-EUR", "closed": False, "state": "BLOCKED_BUT_ALIVE",
            "source_episode_id": "live_episode", "attempts": [],
        }
        return r

    def test_large_source_archives_and_roundtrips_before_guard(self):
        original = self.sample()
        expected = copy.deepcopy(original)
        atomic_json(mod.REGISTRY, original)
        size_before = Path(mod.REGISTRY).stat().st_size
        self.assertGreater(size_before, 4096)
        with patch.object(mod, "REGISTRY_CAPACITY_GUARD_BYTES", 4096), \
             patch.object(mod.subprocess, "check_output", return_value="historic-git-blob"):
            self.assertIs(mod.archive_capacity_preflight(1000.0), True)
            self.assertIs(mod.capacity_guard(1000.0), False)
        live = read_json(mod.REGISTRY)
        index = read_json("production_recovery_archive_index.json")
        self.assertEqual(reconstruct_and_verify(live, index), expected["episodes"])
        self.assertEqual(summarize_all(live, index), summarize(expected))
        self.assertEqual(index["archived_total"], 130)
        self.assertEqual(len(live["episodes"]), 1)
        self.assertEqual(len(index["archives"]), 3)
        self.assertLess(Path(mod.REGISTRY).stat().st_size, size_before)

    def test_invalid_policy_must_not_modify_original(self):
        r = self.sample()
        r["policy"] = {"invalid": True}
        atomic_json(mod.REGISTRY, r)
        original = Path(mod.REGISTRY).read_bytes()
        with patch.object(mod, "REGISTRY_CAPACITY_GUARD_BYTES", 4096):
            with self.assertRaisesRegex(mod.ArchivePreflightError, "FROZEN_POLICY"):
                mod.archive_capacity_preflight(1000.0)
        self.assertEqual(Path(mod.REGISTRY).read_bytes(), original)
        self.assertFalse(Path("production_recovery_archive_index.json").exists())
        self.assertFalse(Path("production_recovery_archives").exists())
