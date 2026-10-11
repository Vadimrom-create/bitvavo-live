"""Lossless, verified migration of the recovery research registry.

The old JSON remains recoverable in the Git parent commit.  This migration
never deletes it until the compressed copy, full round-trip and manifest have
been verified.  No order, mail, production detector or trading-policy path.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from research.common import atomic_json, read_json, utc

SCHEMA = "solaire_recovery_registry_shadow_v1"
MANIFEST_SCHEMA = "solaire_recovery_registry_lossless_gzip_v1"


class RecoveryMigrationError(RuntimeError):
    pass


def _blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _check_registry(value):
    if not isinstance(value, dict) or value.get("schema") != SCHEMA:
        raise RecoveryMigrationError("Unexpected recovery registry schema")
    if not isinstance(value.get("episodes"), dict):
        raise RecoveryMigrationError("Recovery registry episodes must be a dictionary")
    if not isinstance(value.get("policy"), dict):
        raise RecoveryMigrationError("Recovery registry policy missing")
    return value


def _build_manifest(source: Path, compressed: Path, document: dict, raw: bytes):
    episodes = document["episodes"]
    return {
        "schema": MANIFEST_SCHEMA,
        "migrated_at_utc": utc(),
        "source_path": str(source),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "source_git_blob_sha1": _blob_sha1(raw),
        "source_size_bytes": len(raw),
        "archive_path": str(compressed),
        "archive_sha256": _sha256_file(compressed),
        "archive_size_bytes": compressed.stat().st_size,
        "episode_count": len(episodes),
        "attempt_count": sum(len(e.get("attempts") or []) for e in episodes.values()),
        "complete_round_trip_verified": True,
        "historical_source_retained_in_git_parent": True,
        "research_only": True,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }


def ensure_compressed_registry(legacy_path, compressed_path, manifest_path):
    """Idempotent migration; returns MIGRATED, EXISTING, or NEW_REGISTRY.

    Failure never removes the legacy source; a partially written compressed
    file is safe to inspect/retry but MUST NOT be treated as authoritative.
    """
    legacy = Path(legacy_path)
    compressed = Path(compressed_path)
    manifest = Path(manifest_path)

    if compressed.exists() and not legacy.exists():
        if not manifest.exists():
            raise RecoveryMigrationError("Compressed registry lacks verified migration manifest")
        details = read_json(manifest, {}) or {}
        if details.get("schema") != MANIFEST_SCHEMA or not details.get("complete_round_trip_verified"):
            raise RecoveryMigrationError("Compressed registry manifest invalid")
        _check_registry(read_json(compressed))
        return "EXISTING"

    if not legacy.exists() and not compressed.exists():
        # Allow new installations to create a new registry at the compressed path.
        return "NEW_REGISTRY"

    # Includes interrupted migration where both files exist: reconcile exactly.
    raw = legacy.read_bytes()
    try:
        source_doc = _check_registry(json.loads(raw))
    except (ValueError, TypeError) as exc:
        raise RecoveryMigrationError("Legacy registry unreadable; original preserved") from exc

    if not compressed.exists():
        atomic_json(compressed, source_doc)
    try:
        restored = _check_registry(read_json(compressed))
        if restored != source_doc:
            raise RecoveryMigrationError("Lossless round-trip mismatch; original preserved")
    except Exception:
        # Never leave an unverified compressed file on an ordinary retry.
        compressed.unlink(missing_ok=True)
        raise

    details = _build_manifest(legacy, compressed, source_doc, raw)
    # Check existing manifest, if present, before accepting a recovered migration.
    if manifest.exists():
        old = read_json(manifest, {}) or {}
        for field in ("source_sha256", "archive_sha256", "episode_count", "attempt_count"):
            if old.get(field) != details[field]:
                raise RecoveryMigrationError("Existing migration manifest conflicts with source")

    atomic_json(manifest, details)
    # Extra read verifies durable metadata before removing the working-tree copy.
    if read_json(manifest) != details:
        raise RecoveryMigrationError("Migration manifest verification failed")

    # The entire legacy blob remains reachable from Git history until rewritten
    # by any explicit history-rewrite operation, which this workflow never does.
    legacy.unlink()
    return "MIGRATED"
