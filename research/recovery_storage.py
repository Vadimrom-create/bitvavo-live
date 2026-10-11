"""Lossless, Git-auditable storage for closed Solaire recovery episodes.

The live registry retains open episodes. Immutable gzip shards retain every
closed episode, including its full attempts. An index preserves deduplication
and cumulative counters without opening the archives on each heartbeat.

No market calls, sender, orders or trading policy appear in this module.
"""
from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path

from research.common import atomic_json, read_json, utc
from research.recovery_registry import summarize

ARCHIVE_DIR = Path("production_recovery_archives")
INDEX = "production_recovery_archive_index.json"
SCHEMA = "solaire_recovery_archive_v1"
MAX_EPISODES_PER_SHARD = 60
COMPACT_CLOSED_THRESHOLD = 50
COMPACT_FILE_BYTES = 32 * 1024 * 1024


def _identity(market, value):
    return str(market) + "\x1f" + str(value)


def fresh_index():
    return {
        "schema": SCHEMA,
        "archives": [],
        "archived_event_ids": [],
        "archived_source_episode_identities": [],
        "archived_source_decision_identities": [],
        "archived_by_state": {},
        "archived_technical_passes": 0,
        "archived_total": 0,
    }


def _digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def compact_closed(registry, original_index, *, run_id, source_bytes=0,
                   source_blob_sha=None, force=False):
    """Move closed episodes to verified, immutable shards, never truncating data.

    In-memory mutations are safe only after each archive has been written and
    round-trip verified. The caller MUST publish the registry, index and all
    new shards in one atomic Git commit. A crash before push cannot lose data.
    """
    index = dict(original_index or fresh_index())
    if index.get("schema") != SCHEMA:
        raise ValueError("RECOVERY_ARCHIVE_INDEX_SCHEMA_MISMATCH")
    closed = [(key, record) for key, record in registry["episodes"].items()
              if bool(record.get("closed"))]
    if not force and source_bytes < COMPACT_FILE_BYTES and len(closed) < COMPACT_CLOSED_THRESHOLD:
        return registry, index, {"archived_now": 0, "shards": [], "status": "NOT_DUE"}
    if not closed:
        return registry, index, {"archived_now": 0, "shards": [], "status": "NO_CLOSED_EPISODES"}

    safe_run = re.sub(r"[^A-Za-z0-9_-]", "_", str(run_id))
    if not safe_run:
        raise ValueError("MISSING_ARCHIVE_RUN_ID")
    event_ids = set(index.get("archived_event_ids", []))
    source_episode_ids = set(index.get("archived_source_episode_identities", []))
    source_decision_ids = set(index.get("archived_source_decision_identities", []))
    by_state = dict(index.get("archived_by_state", {}))
    technical = int(index.get("archived_technical_passes", 0))
    archives = list(index.get("archives", []))
    created = []

    for part, offset in enumerate(range(0, len(closed), MAX_EPISODES_PER_SHARD), 1):
        group = dict(closed[offset:offset + MAX_EPISODES_PER_SHARD])
        path = ARCHIVE_DIR / ("closed_" + safe_run + "_%04d.json.gz" % part)
        if path.exists():
            raise RuntimeError("RECOVERY_ARCHIVE_PATH_ALREADY_EXISTS:" + str(path))
        payload = {"schema": SCHEMA, "episodes": group}
        atomic_json(path, payload)
        if read_json(path) != payload:
            raise RuntimeError("RECOVERY_ARCHIVE_ROUNDTRIP_FAILED:" + str(path))
        sha = _digest(path)
        if not sha:
            raise RuntimeError("RECOVERY_ARCHIVE_MISSING_HASH")
        group_states = {}
        for key, record in group.items():
            if key in event_ids:
                raise RuntimeError("RECOVERY_ARCHIVE_DUPLICATE_EVENT:" + key)
            event_ids.add(key)
            state = str(record.get("state") or "UNKNOWN")
            group_states[state] = group_states.get(state, 0) + 1
            by_state[state] = by_state.get(state, 0) + 1
            if record.get("first_execution_pass") is not None:
                technical += 1
            market = record.get("market")
            if record.get("source_episode_id") and market:
                source_episode_ids.add(_identity(market, record["source_episode_id"]))
            if record.get("source_decision_id") and market:
                source_decision_ids.add(_identity(market, record["source_decision_id"]))
        entry = {"path": str(path), "sha256": sha, "count": len(group),
                 "by_state": group_states, "source_blob_sha": source_blob_sha,
                 "written_at_utc": utc()}
        archives.append(entry)
        created.append(str(path))

    index.update({
        "archives": archives,
        "archived_event_ids": sorted(event_ids),
        "archived_source_episode_identities": sorted(source_episode_ids),
        "archived_source_decision_identities": sorted(source_decision_ids),
        "archived_by_state": by_state,
        "archived_technical_passes": technical,
        "archived_total": len(event_ids),
        "last_archived_at_utc": utc(),
    })
    registry["episodes"] = {key: record for key, record in registry["episodes"].items()
                            if not record.get("closed")}
    if int(index["archived_total"]) != sum(int(a["count"]) for a in archives):
        raise RuntimeError("RECOVERY_ARCHIVE_INDEX_COUNT_MISMATCH")
    if len(set(registry["episodes"]) & event_ids):
        raise RuntimeError("RECOVERY_ARCHIVE_ACTIVE_EVENT_COLLISION")
    return registry, index, {"archived_now": len(closed), "shards": created,
                             "status": "ARCHIVED_VERIFIED"}


def summarize_all(registry, index):
    summary = summarize(registry)
    archived = int(index.get("archived_total", 0))
    summary["episodes"] += archived
    summary["shadow_candidates"] += int(index.get("archived_by_state", {}).get(
        "SHADOW_RECOVERY_CANDIDATE", 0))
    summary["technical_passes"] += int(index.get("archived_technical_passes", 0))
    for state, count in index.get("archived_by_state", {}).items():
        summary["by_state"][state] = summary["by_state"].get(state, 0) + int(count)
    if summary["episodes"] != sum(summary["by_state"].values()):
        raise RuntimeError("RECOVERY_CUMULATIVE_COUNTER_MISMATCH")
    if summary["open"] != sum(1 for r in registry["episodes"].values() if not r.get("closed")):
        raise RuntimeError("RECOVERY_ACTIVE_COUNTER_MISMATCH")
    return summary


def reconstruct_and_verify(registry, index):
    """Expensive audit command, NEVER called on the 5-minute critical path."""
    episodes = dict(registry["episodes"])
    archived_ids = set()
    observed_technical = 0
    observed_states = {}
    for entry in index.get("archives", []):
        path = Path(entry["path"])
        if _digest(path) != entry["sha256"]:
            raise RuntimeError("RECOVERY_ARCHIVE_SHA256_MISMATCH:" + str(path))
        payload = read_json(path)
        if payload.get("schema") != SCHEMA:
            raise RuntimeError("RECOVERY_ARCHIVE_SCHEMA_MISMATCH")
        group = payload.get("episodes")
        if not isinstance(group, dict) or len(group) != entry["count"]:
            raise RuntimeError("RECOVERY_ARCHIVE_SHARD_COUNT_MISMATCH")
        for key, record in group.items():
            if key in episodes or key in archived_ids or not record.get("closed"):
                raise RuntimeError("RECOVERY_ARCHIVE_DUPLICATE_OR_OPEN_EPISODE:" + key)
            episodes[key] = record
            archived_ids.add(key)
            state = str(record.get("state") or "UNKNOWN")
            observed_states[state] = observed_states.get(state, 0) + 1
            if record.get("first_execution_pass") is not None:
                observed_technical += 1
    if archived_ids != set(index.get("archived_event_ids", [])):
        raise RuntimeError("RECOVERY_ARCHIVE_IDS_MISMATCH")
    if observed_states != index.get("archived_by_state", {}):
        raise RuntimeError("RECOVERY_ARCHIVE_STATES_MISMATCH")
    if observed_technical != index.get("archived_technical_passes", 0):
        raise RuntimeError("RECOVERY_ARCHIVE_TECHNICAL_MISMATCH")
    if len(archived_ids) != index.get("archived_total", 0):
        raise RuntimeError("RECOVERY_ARCHIVE_TOTAL_MISMATCH")
    return episodes
