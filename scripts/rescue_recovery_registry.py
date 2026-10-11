#!/usr/bin/env python3
"""One-time lossless recovery registry rescue, run in a dedicated GitHub job.

The production heartbeat capacity guard remains enabled. This job archives
the historical closed records, verifies complete reconstruction and cumulative
counts, then atomically writes a small live registry plus archive index.
The workflow MUST publish shards, index and live file in ONE Git commit.
Research only: no market requests, alerts, gate calls or orders.
"""
import json
import os
import subprocess
from pathlib import Path

from research.common import atomic_json, read_json
from research.recovery_registry import POLICY, normalize_registry
from research.recovery_storage import (
    INDEX, compact_closed, fresh_index, reconstruct_and_verify, summarize_all,
)

REGISTRY = Path("production_recovery_registry_shadow.json")
ARCHIVE_TRIGGER_BYTES = 32 * 1024 * 1024
SAFE_OUTPUT_BYTES = 80 * 1024 * 1024


def migrate(*, minimum_bytes=ARCHIVE_TRIGGER_BYTES, run_id=None,
            source_blob_sha=None):
    path = REGISTRY
    existing_size = path.stat().st_size
    if existing_size < minimum_bytes:
        return {"result": "BELOW_ARCHIVE_TRIGGER", "source_bytes": existing_size}
    old_registry = read_json(path)
    if not isinstance(old_registry, dict) or not isinstance(old_registry.get("episodes"), dict):
        raise RuntimeError("RECOVERY_SOURCE_INVALID")
    if old_registry.get("policy") != POLICY:
        raise RuntimeError("RECOVERY_FROZEN_POLICY_DRIFT")
    old_index = read_json(INDEX, {}) or fresh_index()
    baseline_summary = summarize_all(old_registry, old_index)
    source_ids = set(old_registry["episodes"])
    if source_blob_sha is None:
        source_blob_sha = subprocess.check_output(
            ["git", "hash-object", str(path)], text=True
        ).strip()
    label = run_id or (
        str(os.getenv("GITHUB_RUN_ID", "manual")) + "_" +
        str(os.getenv("GITHUB_RUN_ATTEMPT", "1")) + "_emergency"
    )
    live, index, work = compact_closed(
        normalize_registry(old_registry), old_index, run_id=label,
        source_bytes=existing_size, source_blob_sha=source_blob_sha, force=True,
    )
    if work["archived_now"] == 0:
        raise RuntimeError("RECOVERY_RESCUE_NO_CLOSED_EPISODES")
    reconstructed = reconstruct_and_verify(live, index)
    if any(reconstructed.get(key) != item for key, item in old_registry["episodes"].items()):
        raise RuntimeError("RECOVERY_RESCUE_LOST_OR_CHANGED_EPISODE")
    if set(reconstructed) != source_ids | set(old_index.get("archived_event_ids", [])):
        raise RuntimeError("RECOVERY_RESCUE_EVENT_ID_SET_MISMATCH")
    if summarize_all(live, index) != baseline_summary:
        raise RuntimeError("RECOVERY_RESCUE_COUNTER_DRIFT")
    encoded = json.dumps(live, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()
    if len(encoded) >= SAFE_OUTPUT_BYTES:
        raise RuntimeError("RECOVERY_RESCUE_COMPACTED_STILL_TOO_LARGE:" + str(len(encoded)))
    # No live state is changed until all archive shards and the complete
    # historical reconstruction are independently verified.
    atomic_json(INDEX, index)
    atomic_json(path, live)
    published_index = read_json(INDEX)
    published_live = read_json(path)
    if reconstruct_and_verify(published_live, published_index) != reconstructed:
        raise RuntimeError("RECOVERY_RESCUE_POST_WRITE_RECONSTRUCTION_FAILED")
    if summarize_all(published_live, published_index) != baseline_summary:
        raise RuntimeError("RECOVERY_RESCUE_POST_WRITE_COUNTER_MISMATCH")
    return {"result": "LOSSLESS_RESCUE_VERIFIED",
            "source_bytes": existing_size, "live_bytes": path.stat().st_size,
            "source_blob_sha": source_blob_sha,
            "archived_now": work["archived_now"],
            "archive_shard_count": len(work["shards"]),
            "total_episodes_preserved": baseline_summary["episodes"],
            "cumulative_status_identical": True}


if __name__ == "__main__":
    print("SOLAIRE_RECOVERY_EMERGENCY " + json.dumps(migrate(), sort_keys=True))
