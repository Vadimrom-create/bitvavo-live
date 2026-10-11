#!/usr/bin/env python3
"""Lossless, verified cold archive for the measurement-only recovery registry.

Closed episodes are copied byte-for-byte at the JSON data level into a gzip
archive, verified by decompression, and only then removed from the working
registry. One Git commit publishes BOTH the compressed archive and compact
working registry. Old Git commits remain an additional recovery path.

No historical prices are reconstituted. Does not change BUY, email or orders.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from research.common import atomic_json
from research.recovery_registry import POLICY, SCHEMA, TERMINAL_STATES, identity_key, summarize_inplace

SOURCE = Path("production_recovery_registry_shadow.json")
ARCHIVES = Path("recovery_registry_archives")
SIZE_TRIGGER_BYTES = 75 * 1024 * 1024
MAX_ARCHIVE_BYTES = 90 * 1024 * 1024


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def compact(registry: dict, *, source_commit: str, original_bytes: bytes, archive_path: str):
    if registry.get("schema") != SCHEMA or registry.get("policy") != POLICY:
        raise ValueError("REGISTRY_SCHEMA_OR_POLICY_DRIFT_REFUSE_ARCHIVE")
    episodes = registry.get("episodes")
    if not isinstance(episodes, dict):
        raise ValueError("REGISTRY_EPISODES_NOT_DICT")

    before = summarize_inplace(registry)
    to_archive = {k: v for k, v in episodes.items() if v.get("closed") is True}
    remaining = {k: v for k, v in episodes.items() if v.get("closed") is not True}
    if not to_archive:
        raise ValueError("NO_CLOSED_EPISODES_TO_COMPACT")
    if any(v.get("state") not in TERMINAL_STATES for v in to_archive.values()):
        raise ValueError("CLOSED_EPISODE_WITH_NONTERMINAL_STATE")
    if any(v.get("closed") for v in remaining.values()):
        raise ValueError("ACTIVE_EPISODE_MISMATCH")

    archive = {
        "schema": "solaire_recovery_closed_archive_v1",
        "source_commit": source_commit,
        "source_registry_git_blob": git_blob_sha(original_bytes),
        "source_registry_sha256": hashlib.sha256(original_bytes).hexdigest(),
        "episodes": to_archive,
    }
    archive_raw = json.dumps(archive, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()
    compressed = gzip.compress(archive_raw, compresslevel=6, mtime=0)
    if len(compressed) >= MAX_ARCHIVE_BYTES:
        raise ValueError("ARCHIVE_TOO_LARGE_REFUSE_WRITE")
    decoded = json.loads(gzip.decompress(compressed))
    if decoded != archive or len(decoded["episodes"]) != len(to_archive):
        raise ValueError("ARCHIVE_ROUND_TRIP_MISMATCH")

    compacted = dict(registry)
    compacted["episodes"] = remaining
    event_index = dict(compacted.get("archive_event_ids") or {})
    episode_index = dict(compacted.get("archive_source_episodes") or {})
    decision_index = dict(compacted.get("archive_source_decisions") or {})
    archived_counts = dict(compacted.get("archive_summary") or {})
    by_state = dict(archived_counts.get("by_state") or {})
    for event_id, row in to_archive.items():
        if event_id in event_index:
            raise ValueError("ARCHIVED_EVENT_ID_ALREADY_EXISTS")
        event_index[event_id] = 1
        market = row.get("market")
        if row.get("source_episode_id"):
            episode_index[identity_key(market, row["source_episode_id"])] = 1
        if row.get("source_decision_id"):
            decision_index[identity_key(market, row["source_decision_id"])] = 1
        state = row["state"]
        by_state[state] = by_state.get(state, 0) + 1

    archived_counts["episodes"] = archived_counts.get("episodes", 0) + len(to_archive)
    archived_counts["open"] = archived_counts.get("open", 0)
    archived_counts["shadow_candidates"] = archived_counts.get("shadow_candidates", 0) + sum(
        v.get("state") == "SHADOW_RECOVERY_CANDIDATE" for v in to_archive.values()
    )
    archived_counts["technical_passes"] = archived_counts.get("technical_passes", 0) + sum(
        v.get("first_execution_pass") is not None for v in to_archive.values()
    )
    archived_counts["by_state"] = by_state

    compacted["archive_event_ids"] = event_index
    compacted["archive_source_episodes"] = episode_index
    compacted["archive_source_decisions"] = decision_index
    compacted["archive_summary"] = archived_counts
    batch = {
        "path": archive_path,
        "source_commit": source_commit,
        "source_registry_git_blob": archive["source_registry_git_blob"],
        "source_registry_sha256": archive["source_registry_sha256"],
        "archive_sha256": hashlib.sha256(compressed).hexdigest(),
        "archive_uncompressed_sha256": hashlib.sha256(archive_raw).hexdigest(),
        "archived_episodes": len(to_archive),
        "live_episodes_remaining": len(remaining),
        "archive_bytes": len(compressed),
    }
    compacted["archive_batches"] = list(compacted.get("archive_batches") or []) + [batch]
    after = summarize_inplace(compacted)
    if before != after:
        raise ValueError("REGISTRY_COUNTERS_DIFFER_AFTER_COMPACTION")
    if len(event_index) != archived_counts["episodes"]:
        raise ValueError("ARCHIVE_IDENTITY_INDEX_COUNT_MISMATCH")
    if set(compacted["episodes"]).intersection(event_index):
        raise ValueError("LIVE_AND_ARCHIVED_ID_OVERLAP")
    return compacted, compressed, batch, before


def run(*, dry_run=False, force=False, root=Path("."), name=None):
    path = root / SOURCE
    if not path.is_file():
        raise ValueError("SOURCE_REGISTRY_MISSING")
    size = path.stat().st_size
    if size < SIZE_TRIGGER_BYTES and not force:
        print(json.dumps({"status": "NOT_DUE", "size_bytes": size}))
        return None
    raw = path.read_bytes()
    try:
        registry = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        raise ValueError("SOURCE_REGISTRY_UNREADABLE_REFUSE_ARCHIVE") from exc

    source_commit = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()
    if not dry_run:
        # Verify this is the exact tracked blob being archived; no dirty source.
        actual_blob = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD:" + str(SOURCE)], text=True
        ).strip()
        if actual_blob != git_blob_sha(raw):
            raise ValueError("SOURCE_REGISTRY_DIFFERS_FROM_COMMITTED_BLOB")

    time_key = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    filename = name or f"{time_key}-{run_id}-{attempt}.json.gz"
    dest = ARCHIVES / filename
    if (root / dest).exists():
        raise ValueError("ARCHIVE_ALREADY_EXISTS_REFUSE_OVERWRITE")

    compacted, compressed, batch, summary = compact(
        registry, source_commit=source_commit, original_bytes=raw, archive_path=str(dest)
    )
    print(json.dumps({"status": "DRY_RUN_OK" if dry_run else "ARCHIVE_PREPARED",
                      "source_bytes": len(raw), "archive_bytes": len(compressed),
                      "active_episodes": len(compacted["episodes"]),
                      "summary": summary, "batch": batch}))
    if dry_run:
        return batch

    target = root / dest
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(".pending")
    with temp.open("xb") as stream:
        stream.write(compressed)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, target)
    if hashlib.sha256(target.read_bytes()).hexdigest() != batch["archive_sha256"]:
        raise ValueError("ARCHIVE_WRITE_CHECKSUM_MISMATCH")
    atomic_json(root / SOURCE, compacted)
    if summarize_inplace(json.loads((root / SOURCE).read_bytes())) != summary:
        raise ValueError("COMPACTED_REGISTRY_RELOAD_MISMATCH")
    return batch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Only for tests")
    options = parser.parse_args()
    run(dry_run=options.dry_run, force=options.force)


if __name__ == "__main__":
    main()
