"""Prevent an oversized research-only registry from blocking production scans."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import update_recovery_registry_heartbeat as mod


class TestRecoveryRegistryCapacityGuard(unittest.TestCase):
    def test_capacity_guard_preserves_large_registry_without_parsing(self):
        with tempfile.TemporaryDirectory() as td:
            registry = Path(td) / "registry.json"
            with registry.open("wb") as handle:
                handle.write(b"PRESERVED_REGISTRY")
                handle.truncate(mod.REGISTRY_CAPACITY_GUARD_BYTES + 1)
            status = Path(td) / "status.json"
            status.write_text(json.dumps({
                "status": "OK",
                "checked_at_utc": "2026-10-11T11:00:00+00:00",
                "registry": {"episodes": 1308},
            }))
            with patch.object(mod, "REGISTRY", str(registry)), patch.object(mod, "STATUS", str(status)):
                self.assertEqual(mod.main(), 0)
            updated = json.loads(status.read_text())
            self.assertEqual(updated["status"], "DEGRADED_CAPACITY_GUARD")
            self.assertIs(updated["registry_update_paused"], True)
            self.assertEqual(updated["registry_size_bytes"], mod.REGISTRY_CAPACITY_GUARD_BYTES + 1)
            self.assertEqual(updated["last_successful_registry_at_utc"], "2026-10-11T11:00:00+00:00")
            self.assertEqual(updated["registry"]["episodes"], 1308)
            for key in ("detection", "buy_gate", "email", "orders"):
                self.assertIs(updated["affects_" + key], False)
            self.assertEqual(registry.stat().st_size, mod.REGISTRY_CAPACITY_GUARD_BYTES + 1)
            with registry.open("rb") as handle:
                self.assertEqual(handle.read(len(b"PRESERVED_REGISTRY")), b"PRESERVED_REGISTRY")

    def test_capacity_guard_does_not_touch_under_limit(self):
        with tempfile.TemporaryDirectory() as td:
            registry = Path(td) / "registry.json"
            registry.write_bytes(b'{"schema":"test","episodes":{}}')
            status = Path(td) / "status.json"
            with patch.object(mod, "REGISTRY", str(registry)), patch.object(mod, "STATUS", str(status)):
                self.assertIs(mod.capacity_guard(1234.0), False)
            self.assertFalse(status.exists())

    def test_capacity_guard_preserves_original_success_timestamp_on_repeat(self):
        with tempfile.TemporaryDirectory() as td:
            registry = Path(td) / "registry.json"
            with registry.open("wb") as handle:
                handle.truncate(mod.REGISTRY_CAPACITY_GUARD_BYTES + 100)
            status = Path(td) / "status.json"
            status.write_text(json.dumps({
                "status": "DEGRADED_CAPACITY_GUARD",
                "checked_at_utc": "2026-10-11T12:00:00+00:00",
                "last_successful_registry_at_utc": "2026-10-11T11:00:00+00:00",
            }))
            with patch.object(mod, "REGISTRY", str(registry)), patch.object(mod, "STATUS", str(status)):
                self.assertIs(mod.capacity_guard(1791723600.0), True)
            updated = json.loads(status.read_text())
            self.assertEqual(updated["last_successful_registry_at_utc"], "2026-10-11T11:00:00+00:00")
