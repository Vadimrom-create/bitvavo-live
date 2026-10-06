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
import time
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.recovery_registry import POLICY, normalize_registry, observe_episode, register_episode, summarize
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


def _already_registered(registry, market, episode_id, decision_id):
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
        if _already_registered(registry, market, episode_id, decision_id):
            continue
        rejected_at = alert.get("checked_at_utc") or utc(now)
        rejected_ts = _parse_ts(rejected_at) or now
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
        registry = register_episode(registry, event, row, now)
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
            )
        except (RuntimeError, ValueError, KeyError) as exc:
            errors.append({
                "market": market,
                "reason": type(exc).__name__ + ":" + str(exc),
            })

    # Touch on every successful heartbeat observation, even when there are no
    # open episodes. This makes file freshness a direct health signal.
    registry["updated_at_utc"] = utc(now)
    summary = summarize(registry)
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
        "errors": errors,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
    }

    atomic_json(REGISTRY, registry)
    atomic_json(STATUS, status)
    print("SOLAIRE_RECOVERY_HEARTBEAT " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
