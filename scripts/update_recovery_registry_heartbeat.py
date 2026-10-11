#!/usr/bin/env python3
"""Lightweight heartbeat owner for the Solaire recovery registry.

Runs on the production heartbeat cadence and only:
- registers fresh final-gate veto episodes;
- observes still-open BLOCKED_BUT_ALIVE episodes against the current scan;
- expires / invalidates / promotes registry states through the frozen registry rules;
- persists registry freshness and a compact health status.

It deliberately does NOT run historical 1h/4h/12h/24h outcome measurements.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.recovery_registry import POLICY, normalize_registry, observe_episode, register_episode
from research.recovery_storage import (ARCHIVE_DIR, INDEX, compact_closed, fresh_index,
                                       reconstruct_and_verify, summarize_all)
from scripts.send_production_buy_alert import prior_buy_thesis_active, validate

CANDIDATES = "production_alert_candidates.json"
ALERT_STATUS = "production_alert_status.json"
PRODUCTION_STATE = "production_alert_state.json"
REGISTRY = "production_recovery_registry_shadow.json"
STATUS = "production_recovery_registry_status.json"
TRACKED = {
    "STRUCTURAL_RANGE_TOO_NARROW",
    "SPREAD_TOO_WIDE",
    "INSUFFICIENT_EXECUTION_LIQUIDITY",
    "STRUCTURAL_STOP_TOO_WIDE",
}
FRESHNESS_LIMIT_SECONDS = 15 * 60
# Fail safely before hitting GitHub's 100 MiB single-blob limit.  This shadow
# registry never participates in detection, the BUY gate, email or order flow.
# Preservation takes precedence over another append when the archive is full.
REGISTRY_CAPACITY_GUARD_BYTES = 85 * 1024 * 1024


def capacity_guard(now):
    """Preserve the original registry byte-for-byte if it is near GitHub's cap."""
    path = Path(REGISTRY)
    if not path.exists() or path.stat().st_size < REGISTRY_CAPACITY_GUARD_BYTES:
        return False
    size = path.stat().st_size
    previous = read_json(STATUS, {}) or {}
    status = {
        **previous,
        "schema": "solaire_recovery_registry_heartbeat_v1",
        "checked_at_utc": utc(now),
        "status": "DEGRADED_CAPACITY_GUARD",
        "writer": "production_scan_fast_heartbeat",
        "registry_update_paused": True,
        "registry_size_bytes": size,
        "registry_capacity_guard_bytes": REGISTRY_CAPACITY_GUARD_BYTES,
        "last_successful_registry_at_utc": previous.get("last_successful_registry_at_utc")
            or (previous.get("checked_at_utc") if previous.get("status") == "OK" else None),
        "new_episodes": 0,
        "revalidations": 0,
        "absence_observations": 0,
        "errors": [{"reason": "REGISTRY_CAPACITY_GUARD",
                    "detail": "Historical registry preserved; archive required before writes resume",
                    "size_bytes": size}],
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }
    atomic_json(STATUS, status)
    print("SOLAIRE_RECOVERY_HEARTBEAT " + json.dumps(status, ensure_ascii=False))
    return True



class ArchivePreflightError(RuntimeError):
    """A shadow storage validation failure; preserve the original registry."""


def archive_capacity_preflight(now):
    """One-shot lossless compaction BEFORE the normal capacity guard.

    The guard must remain fail-closed for unsafe archives, but cannot prevent
    its own remediation. No live scans, BUY gates or sender are called here.
    """
    source_path = Path(REGISTRY)
    if not source_path.exists() or source_path.stat().st_size < REGISTRY_CAPACITY_GUARD_BYTES:
        return False

    source_bytes = source_path.stat().st_size
    source = read_json(REGISTRY, {})
    if (not isinstance(source, dict)
            or source.get("schema") != "solaire_recovery_registry_shadow_v1"
            or source.get("policy") != POLICY
            or not isinstance(source.get("episodes"), dict)):
        raise ArchivePreflightError("REGISTRY_SOURCE_OR_FROZEN_POLICY_INVALID")

    old_index = read_json(INDEX, {}) or fresh_index()
    before = summarize_all(source, old_index)
    # This source blob SHA can be checked against the archived Git commit.
    source_blob_sha = subprocess.check_output(
        ["git", "hash-object", REGISTRY], text=True).strip()
    preexisting = set(ARCHIVE_DIR.glob("closed_*.json.gz"))
    try:
        working = normalize_registry(source)
        working, new_index, result = compact_closed(
            working, old_index,
            run_id=os.getenv("GITHUB_RUN_ID", "local") + "_capacity",
            source_bytes=source_bytes,
            source_blob_sha=source_blob_sha,
            force=True,
        )
        if not result.get("shards"):
            raise ArchivePreflightError("CAPACITY_LIMIT_WITHOUT_CLOSED_ARCHIVABLE_EPISODES")

        reconstructed = reconstruct_and_verify(working, new_index)
        # Every episode in the preflight source, including all attempts, MUST
        # still exist byte-for-byte at the JSON-value level after compaction.
        for event_id, record in source["episodes"].items():
            if reconstructed.get(event_id) != record:
                raise ArchivePreflightError("CAPACITY_ARCHIVE_EPISODE_MISMATCH:" + event_id)
        if summarize_all(working, new_index) != before:
            raise ArchivePreflightError("CAPACITY_ARCHIVE_COUNTER_MISMATCH")
        compact_size = len(json.dumps(
            working, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False).encode("utf-8"))
        if compact_size >= REGISTRY_CAPACITY_GUARD_BYTES:
            raise ArchivePreflightError("COMPACTED_REGISTRY_STILL_EXCEEDS_CAPACITY_GUARD")
    except Exception as exc:
        # Only new, uncommitted temporary shards are removed. Existing archives
        # and the original Git-tracked registry remain strictly unchanged.
        for path in set(ARCHIVE_DIR.glob("closed_*.json.gz")) - preexisting:
            path.unlink(missing_ok=True)
        if isinstance(exc, ArchivePreflightError):
            raise
        raise ArchivePreflightError(
            "CAPACITY_ARCHIVE_VERIFICATION_FAILED:" + type(exc).__name__) from exc

    # All read-only validations succeeded. The workflow stages these two files
    # and every verified gzip shard in ONE Git commit; no partial history can
    # be committed if a write raises an exception.
    atomic_json(INDEX, new_index)
    atomic_json(REGISTRY, working)
    print("SOLAIRE_RECOVERY_CAPACITY_ARCHIVED " + json.dumps({
        "source_size_bytes": source_bytes,
        "compact_size_bytes": compact_size,
        "source_git_blob_sha": source_blob_sha,
        "archived_episodes": result["archived_now"],
        "archive_shards": len(result["shards"]),
        "full_round_trip_verified": True,
        "cumulative_counters_unchanged": True,
        "research_only": True,
    }))
    return True


def _parse_ts(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def _source_row_maps(payload):
    tracking = {
        row.get("market"): row
        for row in payload.get("tracking", [])
        if isinstance(row, dict) and row.get("market")
    }
    watch = {
        row.get("market"): row
        for row in payload.get("watch", [])
        if isinstance(row, dict) and row.get("market")
    }
    return tracking, watch


def _already_registered(registry, market, episode_id, decision_id,
                        archived_episode_ids, archived_decision_ids, archived_event_ids,
                        rejection_ts):
    # Archived closed episodes must retain the same deduplication contract.
    identity = lambda value: str(market) + chr(31) + str(value)
    if episode_id and identity(episode_id) in archived_episode_ids:
        return True
    if decision_id and identity(decision_id) in archived_decision_ids:
        return True
    if rejection_ts is not None and f"{market}|{int(rejection_ts)}" in archived_event_ids:
        return True
    for record in (registry.get("episodes") or {}).values():
        if record.get("market") != market:
            continue
        if episode_id and record.get("source_episode_id") == episode_id:
            return True
        if decision_id and record.get("source_decision_id") == decision_id:
            return True
    return False


def main():
    now = time.time()
    try:
        archive_capacity_preflight(now)
    except (ArchivePreflightError, ValueError, OSError, TypeError, subprocess.CalledProcessError) as exc:
        print("SOLAIRE_RECOVERY_CAPACITY_ARCHIVE_FAILED " + type(exc).__name__ + ':' + str(exc)[:180])
        # Fail closed only for optional recovery research. Production scanner
        # and BUY email operations execute independently before this step.
        capacity_guard(now)
        return 0
    if capacity_guard(now):
        return 0
    payload = read_json(CANDIDATES, {})
    alert = read_json(ALERT_STATUS, {})
    production_state = read_json(PRODUCTION_STATE, {})
    raw_registry = read_json(REGISTRY, {})
    previous_updated = _parse_ts((raw_registry or {}).get("updated_at_utc"))
    previous_age = round(max(0.0, now - previous_updated), 3) if previous_updated is not None else None
    previous_stale = previous_age is None or previous_age > FRESHNESS_LIMIT_SECONDS

    policy_before = (raw_registry or {}).get("policy")
    policy_drift_detected = bool(policy_before is not None and policy_before != POLICY)
    registry = normalize_registry(raw_registry)
    archive_index = read_json(INDEX, {}) or fresh_index()
    registry_path = Path(REGISTRY)
    source_bytes = registry_path.stat().st_size if registry_path.exists() else 0
    source_blob_sha = None
    if source_bytes >= 32 * 1024 * 1024:
        source_blob_sha = subprocess.check_output(
            ["git", "hash-object", REGISTRY], text=True).strip()
    registry, archive_index, initial_archival = compact_closed(
        registry, archive_index, run_id=os.getenv("GITHUB_RUN_ID", "local") + "_pre",
        source_bytes=source_bytes, source_blob_sha=source_blob_sha,
    )
    archived_episode_ids = set(archive_index.get("archived_source_episode_identities", []))
    archived_decision_ids = set(archive_index.get("archived_source_decision_identities", []))
    archived_event_ids = set(archive_index.get("archived_event_ids", []))
    tracking_rows, watch_rows = _source_row_maps(payload)

    new_episodes = 0
    for rejection in alert.get("rejections") or []:
        market = rejection.get("market")
        reason = rejection.get("reason")
        if not market or reason not in TRACKED:
            continue
        row = tracking_rows.get(market) or watch_rows.get(market)
        if row is None:
            continue
        episode_id = rejection.get("episode_id")
        decision_id = rejection.get("decision_id")
        rejected_at = alert.get("checked_at_utc") or utc(now)
        rejected_ts = _parse_ts(rejected_at) or now
        if _already_registered(registry, market, episode_id, decision_id,
                               archived_episode_ids, archived_decision_ids,
                               archived_event_ids, rejected_ts):
            continue
        event = {
            "event_id": f"{market}|{int(rejected_ts)}",
            "market": market,
            "source_decision_id": decision_id,
            "source_episode_id": episode_id,
            "source_execution_observation_id": rejection.get("execution_observation_id"),
            "first_rejection_reason": reason,
            "rejected_at_utc": rejected_at,
            "rejected_ts": rejected_ts,
            "rejection_price_eur": finite(row.get("last")),
            "signal_state": row.get("signal_state"),
            "signal_score": finite(row.get("signal_score")),
            "evidence_count": int((row.get("acceleration") or {}).get("evidence_count") or 0),
        }
        before = len(registry.get("episodes") or {})
        registry = register_episode(registry, event, row, now, inplace=True)
        if len(registry.get("episodes") or {}) > before:
            new_episodes += 1

    client = None
    metadata = None
    errors = []
    revalidations = 0
    absence_observations = 0

    for event_id, record in list((registry.get("episodes") or {}).items()):
        if record.get("closed"):
            continue
        market = record.get("market")
        row = tracking_rows.get(market) or watch_rows.get(market)
        if row is None:
            registry = observe_episode(
                registry,
                event_id,
                None,
                now,
                execution_pass=None,
                execution_reason="SIGNAL_ABSENT_NOT_EVALUATED",
                plan=None,
                inplace=True,
            )
            absence_observations += 1
            continue

        try:
            if client is None:
                client = PublicClient(timeout=10, retries=2, requests_per_second=8)
                client.get("/time", cache=False)
                market_rows = client.get("/markets")
                metadata = {
                    m["market"]: m
                    for m in market_rows
                    if m.get("quote") == "EUR" and m.get("status") == "trading"
                }
            checked = time.time()
            validated, reason = validate(row, client, metadata, checked)
            revalidations += 1
            prior_thesis_clear = None
            prior_thesis_status = None
            if validated:
                thesis_active, prior_thesis_status = prior_buy_thesis_active(
                    production_state, validated, checked
                )
                prior_thesis_clear = not thesis_active
            registry = observe_episode(
                registry,
                event_id,
                row,
                checked,
                execution_pass=bool(validated),
                execution_reason=reason,
                plan=(validated or {}).get("trade") if validated else None,
                prior_thesis_clear=prior_thesis_clear,
                prior_thesis_status=prior_thesis_status,
                inplace=True,
            )
        except (RuntimeError, ValueError, KeyError) as exc:
            errors.append({
                "market": market,
                "reason": type(exc).__name__ + ":" + str(exc),
            })

    # Touch on every successful heartbeat observation, even when there are no
    # open episodes. This makes file freshness a direct health signal.
    registry["updated_at_utc"] = utc(now)
    registry, archive_index, subsequent_archival = compact_closed(
        registry, archive_index, run_id=os.getenv("GITHUB_RUN_ID", "local") + "_post",
    )
    summary = summarize_all(registry, archive_index)
    policy_frozen = registry.get("policy") == POLICY
    invariant_flags_ok = all(
        summary.get(key) is False
        for key in ("affects_detection", "affects_buy_gate", "affects_email", "affects_orders")
    )

    status = {
        "schema": "solaire_recovery_registry_heartbeat_v1",
        "checked_at_utc": utc(now),
        "status": "OK" if not errors and policy_frozen and invariant_flags_ok else "DEGRADED_NONBLOCKING",
        "writer": "production_scan_fast_heartbeat",
        "freshness_limit_seconds": FRESHNESS_LIMIT_SECONDS,
        "previous_registry_age_seconds": previous_age,
        "previous_registry_was_stale": previous_stale,
        "policy_drift_detected_before_normalization": policy_drift_detected,
        "policy_frozen": policy_frozen,
        "invariant_flags_ok": invariant_flags_ok,
        "new_episodes": new_episodes,
        "revalidations": revalidations,
        "absence_observations": absence_observations,
        "registry": summary,
        "archive": {"archived_total": archive_index.get("archived_total", 0),
                    "archive_shard_count": len(archive_index.get("archives", [])),
                    "archived_now": initial_archival["archived_now"] + subsequent_archival["archived_now"],
                    "new_shards_verified": len(initial_archival["shards"]) + len(subsequent_archival["shards"]),
                    "source_git_blob_sha": source_blob_sha,
                    "status": "VERIFIED_ARCHIVE" if initial_archival["shards"] or subsequent_archival["shards"]
                    else "INDEX_REUSED"},
        "errors": errors,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }

    # Workflow stages the archive shards, index, live registry and status in
    # ONE Git commit. Never publish a compact registry without its archives.
    atomic_json(INDEX, archive_index)
    atomic_json(REGISTRY, registry)
    atomic_json(STATUS, status)
    print("SOLAIRE_RECOVERY_HEARTBEAT " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
