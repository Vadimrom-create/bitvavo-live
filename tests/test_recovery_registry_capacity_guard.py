"""Capacity-guard regression tests: never mutate the historical shadow corpus."""
import json

from scripts import update_recovery_registry_heartbeat as mod


def test_capacity_guard_preserves_large_registry_without_parsing(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    with registry.open("wb") as handle:
        handle.write(b"PRESERVED_REGISTRY")
        handle.truncate(mod.REGISTRY_CAPACITY_GUARD_BYTES + 1)
    status = tmp_path / "status.json"
    status.write_text(json.dumps({
        "status": "OK",
        "checked_at_utc": "2026-10-11T11:00:00+00:00",
        "registry": {"episodes": 1308},
    }))
    monkeypatch.setattr(mod, "REGISTRY", str(registry))
    monkeypatch.setattr(mod, "STATUS", str(status))

    # This path must short-circuit before read_json(REGISTRY) and before API.
    assert mod.main() == 0
    updated = json.loads(status.read_text())
    assert updated["status"] == "DEGRADED_CAPACITY_GUARD"
    assert updated["registry_update_paused"] is True
    assert updated["registry_size_bytes"] == mod.REGISTRY_CAPACITY_GUARD_BYTES + 1
    assert updated["last_successful_registry_at_utc"] == "2026-10-11T11:00:00+00:00"
    assert updated["registry"]["episodes"] == 1308
    assert not any(updated["affects_" + key] for key in ("detection", "buy_gate", "email", "orders"))
    assert registry.stat().st_size == mod.REGISTRY_CAPACITY_GUARD_BYTES + 1
    with registry.open("rb") as handle:
        assert handle.read(len(b"PRESERVED_REGISTRY")) == b"PRESERVED_REGISTRY"


def test_capacity_guard_does_not_touch_under_limit(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    registry.write_bytes(b'{"schema":"test","episodes":{}}')
    status = tmp_path / "status.json"
    monkeypatch.setattr(mod, "REGISTRY", str(registry))
    monkeypatch.setattr(mod, "STATUS", str(status))
    assert mod.capacity_guard(1234.0) is False
    assert not status.exists()


def test_capacity_guard_preserves_original_success_timestamp_on_repeat(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    with registry.open("wb") as handle:
        handle.truncate(mod.REGISTRY_CAPACITY_GUARD_BYTES + 100)
    status = tmp_path / "status.json"
    status.write_text(json.dumps({
        "status": "DEGRADED_CAPACITY_GUARD",
        "checked_at_utc": "2026-10-11T12:00:00+00:00",
        "last_successful_registry_at_utc": "2026-10-11T11:00:00+00:00",
    }))
    monkeypatch.setattr(mod, "REGISTRY", str(registry))
    monkeypatch.setattr(mod, "STATUS", str(status))
    assert mod.capacity_guard(1791723600.0) is True
    updated = json.loads(status.read_text())
    assert updated["last_successful_registry_at_utc"] == "2026-10-11T11:00:00+00:00"
