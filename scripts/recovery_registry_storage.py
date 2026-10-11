#!/usr/bin/env python3
"""Lossless recovery registry migration: preserve original Git blob and gzip bytes."""
from __future__ import annotations

import gzip
import hashlib
import json
import os
import tempfile
from pathlib import Path

from research.common import atomic_json, read_json, utc

LEGACY = Path("production_recovery_registry_shadow.json")
ACTIVE = Path("production_recovery_registry_shadow.json.gz")
ARCHIVE_DIR = Path("recovery_registry_archives")
MANIFEST = ARCHIVE_DIR / "precompact_manifest.json"


def load_registry() -> dict:
    if LEGACY.exists() and ACTIVE.exists():
        raise RuntimeError("RECOVERY_REGISTRY_AMBIGUOUS_DUAL_WRITER")
    path = ACTIVE if ACTIVE.exists() else LEGACY
    if not path.exists():
        raise FileNotFoundError("RECOVERY_REGISTRY_MISSING_REFUSE_EMPTY_RESET")
    result = read_json(path)
    if not isinstance(result, dict) or not isinstance(result.get("episodes"), dict):
        raise ValueError("RECOVERY_REGISTRY_INVALID_SCHEMA")
    return result


def _atomic_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def _archive_legacy() -> None:
    source = LEGACY.read_bytes()
    prior = json.loads(source)
    if not isinstance(prior, dict) or not isinstance(prior.get("episodes"), dict):
        raise ValueError("RECOVERY_ARCHIVE_INVALID_SOURCE")
    if MANIFEST.exists():
        raise RuntimeError("RECOVERY_ARCHIVE_MANIFEST_EXISTS_WITHOUT_ACTIVE")
    git_blob_sha = hashlib.sha1(
        b"blob " + str(len(source)).encode() + b"\0" + source
    ).hexdigest()
    compressed = gzip.compress(source, mtime=0)
    archive_path = ARCHIVE_DIR / ("precompact_" + git_blob_sha + ".json.gz")
    if archive_path.exists():
        if archive_path.read_bytes() != compressed:
            raise ValueError("RECOVERY_ARCHIVE_EXISTING_CONTENT_MISMATCH")
    else:
        _atomic_bytes(archive_path, compressed)
    if gzip.decompress(archive_path.read_bytes()) != source:
        raise ValueError("RECOVERY_ARCHIVE_LOSSLESS_VERIFICATION_FAILED")
    atomic_json(MANIFEST, {
        "schema": "solaire_recovery_precompact_manifest_v1",
        "created_at_utc": utc(),
        "source_path": str(LEGACY),
        "source_git_blob_sha": git_blob_sha,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "source_raw_bytes": len(source),
        "archive_path": str(archive_path),
        "archive_sha256": hashlib.sha256(compressed).hexdigest(),
        "episode_count": len(prior["episodes"]),
        "episode_ids_sha256": hashlib.sha256(
            "\n".join(sorted(prior["episodes"])).encode()
        ).hexdigest(),
        "lossless_bytes_verified": True,
        "trade_rules_modified": False,
    })


def persist_registry(registry: dict) -> None:
    """Archive first, round-trip verify live store, then unlink legacy file."""
    if not isinstance(registry, dict) or not isinstance(registry.get("episodes"), dict):
        raise ValueError("RECOVERY_REGISTRY_INVALID_OUTPUT")
    if LEGACY.exists() and ACTIVE.exists():
        raise RuntimeError("RECOVERY_REGISTRY_AMBIGUOUS_DUAL_WRITER")
    migrating = LEGACY.exists()
    if migrating:
        _archive_legacy()
    atomic_json(ACTIVE, registry)
    if read_json(ACTIVE) != registry:
        raise ValueError("RECOVERY_REGISTRY_COMPRESSED_ROUNDTRIP_FAILED")
    if migrating:
        LEGACY.unlink()
        print("RECOVERY_REGISTRY_MIGRATED_LOSSLESSLY", MANIFEST)
