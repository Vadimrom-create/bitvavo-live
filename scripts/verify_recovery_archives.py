#!/usr/bin/env python3
"""Read-only audit / dry-run of the Solaire recovery archival migration."""
import argparse
import copy
import json
import os
import subprocess
import tempfile
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research.common import read_json
from research.recovery_registry import normalize_registry, observe_episode, summarize
from research.recovery_storage import (
    INDEX, compact_closed, fresh_index, reconstruct_and_verify, summarize_all,
)

REGISTRY = "production_recovery_registry_shadow.json"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--exercise-migration", action="store_true")
    p.add_argument("--verify-published", action="store_true")
    args = p.parse_args()
    if args.exercise_migration == args.verify_published:
        p.error("choose exactly one mode")

    original_path = Path(REGISTRY).resolve()
    original = read_json(original_path)
    if not isinstance(original, dict) or not isinstance(original.get("episodes"), dict):
        raise SystemExit("REGISTRY_INPUT_INVALID")
    before = summarize(original)
    source_bytes = original_path.stat().st_size
    sha = subprocess.check_output(["git", "hash-object", str(original_path)],
                                  text=True).strip()

    if args.exercise_migration:
        with tempfile.TemporaryDirectory(prefix="recovery-migration-check-") as td:
            previous_dir = Path.cwd()
            try:
                os.chdir(td)
                started = time.monotonic()
                live, index, d = compact_closed(
                    normalize_registry(original), fresh_index(),
                    run_id="ci_dry_run", source_bytes=source_bytes,
                    source_blob_sha=sha, force=True,
                )
                reconstructed = reconstruct_and_verify(live, index)
                if reconstructed != original["episodes"]:
                    raise RuntimeError("RECOVERY_EPISODE_CONTENT_DIFFERS")
                if summarize_all(live, index) != before:
                    raise RuntimeError("RECOVERY_SUMMARY_DIFFERS")
                # Representative workload after migration; no market calls.
                start_benchmark = time.monotonic()
                for i, event_id in enumerate(list(live["episodes"])[:25]):
                    live = observe_episode(
                        live, event_id, None, time.time(),
                        execution_pass=None, inplace=True,
                    )
                bench = time.monotonic() - start_benchmark
                print(json.dumps({
                    "result": "PASS_VERIFIED_LOSSLESS_DRY_RUN",
                    "source_git_blob_sha": sha,
                    "source_bytes": source_bytes,
                    "before_episodes": before["episodes"],
                    "archived_episodes": index["archived_total"],
                    "still_active": len(live["episodes"]),
                    "shard_count": len(index["archives"]),
                    "reconstruction_matched": True,
                    "status_counters_matched": True,
                    "archive_duration_seconds": round(time.monotonic() - started, 3),
                    "batch_observation_25_seconds": round(bench, 3),
                }))
            finally:
                os.chdir(previous_dir)
    else:
        index = read_json(INDEX, {}) or {}
        reconstructed = reconstruct_and_verify(original, index)
        result = summarize_all(original, index)
        if result["episodes"] != len(reconstructed):
            raise RuntimeError("RECOVERY_RECONSTRUCTED_COUNT_MISMATCH")
        print(json.dumps({
            "result": "PASS_VERIFIED_PUBLISHED_ARCHIVES",
            "live_bytes": source_bytes,
            "live_count": len(original["episodes"]),
            "archived_count": index["archived_total"],
            "reconstructed_count": len(reconstructed),
            "archive_count": len(index["archives"]),
            "summary": result,
        }))


if __name__ == "__main__":
    main()
