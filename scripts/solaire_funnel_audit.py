#!/usr/bin/env python3
"""Prospective measurement-only audit of the Solaire decision funnel.

The audit watches every evidence-bearing V3/V3.1 candidate, including losers,
and records the first time it reaches each stage:
credible -> entry hypothesis -> V2 confirmed -> execution ready -> selectable.

It changes no score, threshold, portfolio, alert or order path.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.solaire_funnel_audit import (
    AUDIT_VERSION,
    advance_funnel_memory,
    classify_snapshot,
    loss_family_counts,
    should_track,
    stage_counts,
)

V3_CANDIDATES = "solaire_v3_candidates.json"
V31_CANDIDATES = "solaire_v31_candidates.json"

STATE = "solaire_funnel_audit_state.json"
JOURNAL = "solaire_funnel_audit_journal.json"
REPORT = "solaire_funnel_audit_report.json"
STATUS = "solaire_funnel_audit_status.json"

INACTIVE_AFTER_SECONDS = 2 * 3600
MAX_JOURNAL_EVENTS = 20000


def _event_key(event: dict[str, Any]) -> str:
    return str(event.get("attempt_id") or "|".join([
        str(event.get("market") or ""),
        str(event.get("event_type") or ""),
        str(event.get("transition_sequence") or ""),
        str(event.get("architecture_version") or ""),
    ]))


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    event.setdefault("architecture_version", AUDIT_VERSION)
    keys = {_event_key(x) for x in journal.get("events", [])}
    key = _event_key(event)
    if key in keys:
        return False
    journal.setdefault("events", []).append(event)
    return True


def _candidate_price(v3: dict[str, Any], v31: dict[str, Any]) -> float | None:
    return finite(v3.get("price_eur"), finite(v31.get("price_eur")))


def main() -> int:
    now = time.time()
    v3_doc = read_json(V3_CANDIDATES, {}) or {}
    v31_doc = read_json(V31_CANDIDATES, {}) or {}
    state = read_json(STATE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}

    v3_rows = v3_doc.get("candidates") or []
    v31_rows = v31_doc.get("candidates") or []
    v3_by_market = {x.get("market"): x for x in v3_rows if x.get("market")}
    v31_by_market = {x.get("market"): x for x in v31_rows if x.get("market")}

    state.setdefault("schema", "solaire_funnel_audit_state_v1")
    prior_version = state.get("architecture_version")
    rollover = prior_version != AUDIT_VERSION
    state["architecture_version"] = AUDIT_VERSION
    if rollover:
        # New audit definitions start a clean prospective cohort.  Historical
        # runtime files stay untouched; only this audit's own state resets.
        state["markets"] = {}
        state["prospective_start_ts"] = now
        state["prospective_start_at_utc"] = utc(now)
        state["architecture_migrated_from"] = prior_version
    state.setdefault("markets", {})

    journal.setdefault("schema", "solaire_funnel_audit_journal_v1")
    journal.setdefault("events", [])
    journal.setdefault("started_ts", now)
    journal.setdefault("started_at_utc", utc(now))

    current_markets: set[str] = set()
    for market in sorted(set(v3_by_market) | set(v31_by_market)):
        v3 = v3_by_market.get(market) or {}
        v31 = v31_by_market.get(market) or {}
        if not should_track(v3, v31):
            continue

        current_markets.add(market)
        snapshot = classify_snapshot(v3, v31)
        price = _candidate_price(v3, v31)
        prior = state["markets"].get(market)
        memory, changed = advance_funnel_memory(
            prior,
            snapshot=snapshot,
            now=now,
            price_eur=price,
        )
        memory["market"] = market
        memory["active"] = True
        memory["last_seen_at_utc"] = utc(now)
        memory["source_v3_architecture_version"] = v3_doc.get("architecture_version")
        memory["source_v31_architecture_version"] = v31_doc.get("architecture_version")
        memory["source_v3_runtime_commit"] = v3_doc.get("runtime_commit")
        memory["source_v31_upstream_v3_runtime_commit"] = v31_doc.get("upstream_v3_runtime_commit")
        memory["near_miss_opportunity"] = bool(v3.get("near_miss_opportunity"))
        memory["credible_opportunity"] = bool(v3.get("credible_opportunity"))
        memory["thesis_reentry_hypothesis"] = bool(v3.get("thesis_reentry_hypothesis"))
        memory["v2_state"] = v3.get("v2_state")
        memory["early_quant"] = v3.get("early_quant")
        memory["selection_reason"] = v31.get("selection_reason")
        memory["execution_quality"] = v31.get("execution_quality")
        state["markets"][market] = memory

        if changed:
            seq = int(memory.get("transition_count") or 0)
            _append_event(journal, {
                "event_type": "FUNNEL_STAGE_TRANSITION",
                "market": market,
                "transition_sequence": seq,
                "attempt_id": f"{market}|{seq}|{AUDIT_VERSION}",
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": price,
                "stage": snapshot.get("stage"),
                "loss_family": snapshot.get("loss_family"),
                "blocking_reason": snapshot.get("blocking_reason"),
                "credible": snapshot.get("credible"),
                "entry_hypothesis": snapshot.get("entry_hypothesis"),
                "v2_state": snapshot.get("v2_state"),
                "v2_confirmed": snapshot.get("v2_confirmed"),
                "execution_ready": snapshot.get("execution_ready"),
                "selectable": snapshot.get("selectable"),
                "economic_score": snapshot.get("economic_score"),
                "v3_opportunity_score": snapshot.get("v3_opportunity_score"),
                "v2_score": snapshot.get("v2_score"),
                "early_quant_score": snapshot.get("early_quant_score"),
                "early_quant_evidence_count": snapshot.get("early_quant_evidence_count"),
                "entry_path": snapshot.get("entry_path"),
                "origin_price_eur": memory.get("origin_price_eur"),
                "current_return_from_origin_pct": memory.get("current_return_from_origin_pct"),
                "mfe_since_origin_pct": memory.get("mfe_since_origin_pct"),
                "mae_since_origin_pct": memory.get("mae_since_origin_pct"),
                "left_censored": rollover,
                "observation_only": True,
                "evaluation_excluded": True,
            })

    for market, memory in state["markets"].items():
        if market in current_markets:
            continue
        last_seen = finite(memory.get("last_seen_ts"), 0.0)
        if memory.get("active") and now - last_seen > INACTIVE_AFTER_SECONDS:
            memory["active"] = False
            memory["inactive_at_utc"] = utc(now)

    rows = list(state["markets"].values())
    active_rows = [x for x in rows if x.get("active")]
    unresolved = [x for x in active_rows if not x.get("resolved_selectable")]
    high_mfe_unresolved = [
        x for x in unresolved
        if finite(x.get("mfe_since_origin_pct"), -999.0) >= 10.0
    ]
    high_mfe_unresolved.sort(
        key=lambda x: finite(x.get("mfe_since_origin_pct"), -999.0),
        reverse=True,
    )
    active_rows.sort(
        key=lambda x: (
            bool(x.get("resolved_selectable")),
            -finite(x.get("mfe_since_origin_pct"), -999.0),
        )
    )

    report = {
        "schema": "solaire_funnel_audit_report_v1",
        "generated_at_utc": utc(now),
        "architecture_version": AUDIT_VERSION,
        "mode": "MEASUREMENT_ONLY",
        "source_v3_architecture_version": v3_doc.get("architecture_version"),
        "source_v31_architecture_version": v31_doc.get("architecture_version"),
        "research_only": True,
        "affects_v2": False,
        "affects_v3": False,
        "affects_v31": False,
        "affects_email": False,
        "orders_submitted": False,
        "stage_counts": stage_counts(active_rows),
        "loss_family_counts": loss_family_counts(active_rows),
        "active_count": len(active_rows),
        "resolved_selectable_count": sum(bool(x.get("resolved_selectable")) for x in active_rows),
        "unresolved_count": len(unresolved),
        "high_mfe_unresolved_count": len(high_mfe_unresolved),
        "high_mfe_unresolved": high_mfe_unresolved[:100],
        "markets": active_rows,
    }

    status = {
        "schema": "solaire_funnel_audit_status_v1",
        "checked_at_utc": utc(now),
        "status": "OK",
        "architecture_version": AUDIT_VERSION,
        "mode": "MEASUREMENT_ONLY",
        "source_v3_architecture_version": v3_doc.get("architecture_version"),
        "source_v31_architecture_version": v31_doc.get("architecture_version"),
        "active_count": len(active_rows),
        "unresolved_count": len(unresolved),
        "high_mfe_unresolved_count": len(high_mfe_unresolved),
        "stage_counts": report["stage_counts"],
        "loss_family_counts": report["loss_family_counts"],
        "research_only": True,
        "affects_v2": False,
        "affects_v3": False,
        "affects_v31": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    state["updated_at_utc"] = utc(now)
    journal["updated_at_utc"] = utc(now)
    journal["architecture_version"] = AUDIT_VERSION
    journal["events"] = journal["events"][-MAX_JOURNAL_EVENTS:]

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(REPORT, report)
    atomic_json(STATUS, status)

    print("SOLAIRE_FUNNEL_AUDIT " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
