#!/usr/bin/env python3
"""Prospective challenger: allow MEMORY_ONLY near-misses to seed a thesis.

This script is intentionally isolated from V3/V3.1 baseline state.  The live
baseline keeps near-miss memory and diagnostics observation-only.  This
challenger changes exactly one policy: a near-miss that would NOT seed/open a
baseline thesis may seed an experimental persistent thesis.  Any eventual
re-entry must still pass the unchanged V3 execution gates and unchanged V3.1
economic selection/sizing before it can enter the challenger portfolio.

No email and no real order can be produced here.
"""
from __future__ import annotations

import copy
import json
import time
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.solaire_v3 import (
    V3_ARCHITECTURE_VERSION,
    advance_persistent_thesis,
    classify_horizon,
    early_quant_evidence,
    select_fair_batch,
    select_priority_fair_batch,
)
from research.solaire_v31 import (
    V31_ARCHITECTURE_VERSION,
    execution_freshness,
    final_economic_score,
    preliminary_economic_score,
    reprice_execution_for_stake,
    shadow_sizing,
)
from scripts.solaire_v3_shadow import (
    execution_check,
    fetch_long_trend_profiles,
)
from scripts.solaire_v31_shadow import update_portfolio

V3_CANDIDATES = "solaire_v3_candidates.json"
V31_CANDIDATES = "solaire_v31_candidates.json"
UNIVERSE = "production_universe_snapshot.json"
BASELINE_PORTFOLIO = "solaire_v31_portfolio.json"

STATE = "solaire_memory_entry_challenger_state.json"
JOURNAL = "solaire_memory_entry_challenger_journal.json"
CANDIDATES = "solaire_memory_entry_challenger_candidates.json"
PORTFOLIO = "solaire_memory_entry_challenger_portfolio.json"
STATUS = "solaire_memory_entry_challenger_status.json"

CHALLENGER_VERSION = "memory-entry-challenger-v3-comparator-hardening-20260925"
MAX_PROFILE_MARKETS = 24
MAX_EXECUTION_MARKETS = 20


def _event_key(event: dict[str, Any]) -> str:
    if event.get("attempt_id"):
        return str(event["attempt_id"])
    return "|".join([
        str(event.get("market") or ""),
        str(event.get("thesis_id") or ""),
        str(event.get("event_type") or ""),
        str(event.get("architecture_version") or ""),
    ])


def _append_event(journal: dict[str, Any], event: dict[str, Any]) -> bool:
    event.setdefault("architecture_version", CHALLENGER_VERSION)
    keys = {_event_key(x) for x in journal.get("events", [])}
    if _event_key(event) in keys:
        return False
    journal.setdefault("events", []).append(event)
    return True


def _baseline_seeded(candidate: dict[str, Any]) -> bool:
    """True when baseline thesis machinery already has an ordinary seed."""
    return bool(candidate.get("thesis_seed") or candidate.get("entry_hypothesis"))


def _experimental_seed(candidate: dict[str, Any]) -> bool:
    """The single treatment factor: near-miss may seed when baseline cannot."""
    return bool(
        candidate.get("near_miss_opportunity")
        and not _baseline_seeded(candidate)
        and not candidate.get("strong_negative_news")
    )


def _minimal_observation(
    market: str,
    universe_row: dict[str, Any],
    prior: dict[str, Any],
) -> dict[str, Any]:
    early = early_quant_evidence(universe_row)
    return {
        **universe_row,
        "market": market,
        "early_quant": early,
        "near_miss_opportunity": bool(early.get("ready")),
        "credible_opportunity": bool(early.get("ready")),
        "fresh_opportunity_trigger": False,
        "entry_hypothesis": False,
        "thesis_seed": False,
        "positive_context": False,
        "context_watch": False,
        "external_score": 0.0,
        "external": {
            "venues_available": 0,
            "external_score_0_10": 0.0,
            "reason": "CHALLENGER_ACTIVE_THESIS_NO_CURRENT_V3_CANDIDATE",
        },
        "news_positive_score": 0.0,
        "news_negative_score": 0.0,
        "news_score": 0.0,
        "active_narratives": [],
        "narrative_score": 0.0,
        "opportunity_score": finite(prior.get("best_opportunity_score"), 0.0),
        "long_trend": prior.get("last_long_trend") or {},
        "horizon_class": prior.get("last_horizon_class"),
    }


def _score_execution(
    candidate: dict[str, Any],
    universe_row: dict[str, Any],
    execution: dict[str, Any],
    now: float,
) -> dict[str, Any]:
    """Apply the unchanged V3.1 economic engine to an experimental re-entry."""
    execution = execution_freshness(execution, now) or {}
    preliminary = preliminary_economic_score(candidate, universe_row)
    final = final_economic_score(preliminary, execution)
    sizing = None

    if final.get("selectable"):
        sizing = shadow_sizing(
            finite(final.get("score"), 0.0),
            execution,
            finite(universe_row.get("quote_volume_24h_eur")),
        )
        if not sizing.get("valid"):
            final = {**final, "selectable": False, "reason": sizing.get("reason")}
            sizing = None
        else:
            execution = reprice_execution_for_stake(
                execution,
                finite(sizing.get("stake_eur"), 0.0),
            )
            final = final_economic_score(preliminary, execution)
            if not final.get("selectable"):
                sizing = None
            else:
                resized = shadow_sizing(
                    finite(final.get("score"), 0.0),
                    execution,
                    finite(universe_row.get("quote_volume_24h_eur")),
                )
                if not resized.get("valid"):
                    final = {**final, "selectable": False, "reason": resized.get("reason")}
                    sizing = None
                else:
                    old_stake = finite(sizing.get("stake_eur"), 0.0)
                    new_stake = finite(resized.get("stake_eur"), 0.0)
                    if abs(new_stake - old_stake) > 0.01:
                        execution = reprice_execution_for_stake(execution, new_stake)
                        final = final_economic_score(preliminary, execution)
                    sizing = resized if final.get("selectable") else None

    return {
        "preliminary": preliminary,
        "final": final,
        "execution": execution,
        "sizing": sizing,
    }


def _current_score_map(
    v31_candidates: list[dict[str, Any]],
    qualified_extra: list[dict[str, Any]],
) -> dict[str, float]:
    """Refresh the challenger with the same complete current score surface as baseline."""
    scores = {
        row.get("market"): finite(row.get("economic_score"), 0.0)
        for row in v31_candidates
        if row.get("market")
    }
    for row in qualified_extra:
        market = row.get("market")
        if market:
            scores[market] = max(
                scores.get(market, 0.0),
                finite(row.get("economic_score"), 0.0),
            )
    return scores


def _baseline_qualified_rows(v31_candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for row in v31_candidates:
        execution = row.get("execution") or {}
        plan = execution.get("plan") or {}
        if not row.get("selectable") or not execution.get("ready"):
            continue
        entry = finite(plan.get("entry_eur"))
        stop = finite(plan.get("stop_eur"))
        if entry is None or stop is None:
            continue
        rows.append({
            **row,
            "entry_eur": entry,
            "stop_eur": stop,
            "entry_path": row.get("entry_path") or "RAW",
        })
    return rows


def main() -> int:
    now = time.time()
    v3_doc = read_json(V3_CANDIDATES, {}) or {}
    v31_doc = read_json(V31_CANDIDATES, {}) or {}
    universe_doc = read_json(UNIVERSE, {}) or {}
    baseline_portfolio = read_json(BASELINE_PORTFOLIO, {}) or {}
    state = read_json(STATE, {}) or {}
    journal = read_json(JOURNAL, {}) or {}
    portfolio = read_json(PORTFOLIO, {}) or {}

    v3_candidates = v3_doc.get("candidates") or []
    v31_candidates = v31_doc.get("candidates") or []
    universe_rows = universe_doc.get("rows") or []
    universe_by_market = {
        row.get("market"): row for row in universe_rows if row.get("market")
    }
    candidate_by_market = {
        row.get("market"): row for row in v3_candidates if row.get("market")
    }
    v31_by_market = {
        row.get("market"): row for row in v31_candidates if row.get("market")
    }

    state.setdefault("schema", "solaire_memory_entry_challenger_state_v1")
    prior_version = state.get("architecture_version")
    rollover = prior_version != CHALLENGER_VERSION
    state["architecture_version"] = CHALLENGER_VERSION
    state.setdefault("theses", {})
    state.setdefault("markets", {})
    state.setdefault("profile_cursor", 0)
    state.setdefault("execution_cursor", 0)
    if rollover:
        state["architecture_migrated_at_utc"] = utc(now)
        state["architecture_migrated_from"] = prior_version
        state["prospective_start_ts"] = now
        state["prospective_start_at_utc"] = utc(now)
        # A challenger version is a distinct prospective experiment.  Keep the
        # journal history, but never carry treatment theses/attempt state across
        # experiment versions.
        state["theses"] = {}
        state["markets"] = {}
        state["profile_cursor"] = 0
        state["execution_cursor"] = 0

    journal.setdefault("schema", "solaire_memory_entry_challenger_journal_v1")
    journal.setdefault("events", [])
    journal.setdefault("started_ts", now)
    journal.setdefault("started_at_utc", utc(now))

    # Treatment population: baseline cannot seed a thesis, challenger may.
    treatment_markets = {
        row["market"] for row in v3_candidates
        if row.get("market") and _experimental_seed(row)
    }
    active_markets = {
        market for market, thesis in state["theses"].items()
        if thesis.get("active")
    }
    thesis_markets = sorted(treatment_markets | active_markets)

    observations: list[dict[str, Any]] = []
    for market in thesis_markets:
        current = candidate_by_market.get(market)
        prior = state["theses"].get(market) or {}
        if current is not None:
            obs = dict(current)
        else:
            universe_row = universe_by_market.get(market)
            if universe_row is None:
                continue
            obs = _minimal_observation(market, universe_row, prior)

        # Only the treatment branch may flip thesis_seed from False to True.
        if market in treatment_markets and not _baseline_seeded(obs):
            obs["thesis_seed"] = True
            obs["challenger_seed"] = True
        else:
            obs["challenger_seed"] = False
        observations.append(obs)

    # Same thesis long-trend machinery, bounded/fair like baseline.
    profile_rows, state["profile_cursor"], profile_fairness = select_fair_batch(
        observations,
        MAX_PROFILE_MARKETS,
        state.get("profile_cursor", 0),
        key=lambda x: x.get("market") or "",
    )
    long_trends: dict[str, dict[str, Any]] = {}
    source_errors: list[dict[str, Any]] = []
    if profile_rows:
        try:
            trend_client = PublicClient(timeout=8, retries=1, requests_per_second=8)
            long_trends, trend_errors = fetch_long_trend_profiles(
                trend_client,
                [x["market"] for x in profile_rows],
                now,
            )
            source_errors.extend(trend_errors)
        except Exception as exc:
            source_errors.append({"source": "long_trend", "reason": type(exc).__name__})

    reentry_rows: list[dict[str, Any]] = []
    for obs in observations:
        market = obs["market"]
        prior = state["theses"].get(market) or {}
        prior_active = bool(prior.get("active"))
        prior_state = prior.get("state")
        obs["long_trend"] = (
            long_trends.get(market)
            or prior.get("last_long_trend")
            or obs.get("long_trend")
            or {}
        )
        thesis = advance_persistent_thesis(prior, obs, now)
        if thesis:
            state["theses"][market] = thesis

        opened = bool(thesis.get("active")) and not prior_active
        if opened:
            thesis["experimental_branch"] = "MEMORY_ENTRY_CHALLENGER"
            thesis["baseline_seed_was_false"] = True
            thesis["origin_left_censored"] = rollover
            _append_event(journal, {
                "event_type": "MEMORY_ENTRY_THESIS_START",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(obs.get("price_eur")),
                "early_quant": obs.get("early_quant"),
                "baseline_thesis_seed": bool((candidate_by_market.get(market) or {}).get("thesis_seed")),
                "baseline_entry_hypothesis": bool((candidate_by_market.get(market) or {}).get("entry_hypothesis")),
                "left_censored": rollover,
                "evaluations": {},
            })

        reentry_ready = bool(
            thesis.get("active")
            and thesis.get("state") == "REENTRY_READY_THESIS"
        )
        if reentry_ready:
            row = dict(obs)
            row["persistent_thesis"] = thesis
            row["thesis_reentry_hypothesis"] = True
            row["candidate_source"] = "MEMORY_ENTRY_CHALLENGER"
            reentry_rows.append(row)

        if reentry_ready and prior_state != "REENTRY_READY_THESIS":
            _append_event(journal, {
                "event_type": "MEMORY_ENTRY_REENTRY_READY",
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "decision_ts": now,
                "decision_at_utc": utc(now),
                "price_eur": finite(obs.get("price_eur")),
                "left_censored": bool(thesis.get("origin_left_censored")),
                "evaluations": {},
            })

    # Same V3 execution gate, bounded/fair.
    execution_rows, state["execution_cursor"], execution_fairness = select_priority_fair_batch(
        reentry_rows,
        MAX_EXECUTION_MARKETS,
        state.get("execution_cursor", 0),
        priority_count=min(8, MAX_EXECUTION_MARKETS),
        priority_key=lambda x: (
            finite((x.get("early_quant") or {}).get("score_0_10"), 0.0),
            finite(x.get("opportunity_score"), 0.0),
        ),
        key=lambda x: x.get("market") or "",
    )

    client = None
    metadata: dict[str, dict[str, Any]] = {}
    try:
        client = PublicClient(timeout=8, retries=1, requests_per_second=10)
        client.get("/time", cache=False)
        metadata = {
            row["market"]: row for row in client.get("/markets")
            if row.get("quote") == "EUR" and row.get("status") == "trading"
        }
    except Exception as exc:
        source_errors.append({"source": "execution", "reason": type(exc).__name__})
        client = None

    checks: dict[str, dict[str, Any]] = {}
    if client is not None and metadata:
        for row in execution_rows:
            checks[row["market"]] = execution_check(client, metadata, row, time.time())

    qualified_extra: list[dict[str, Any]] = []
    ranked_extra: list[dict[str, Any]] = []
    for row in reentry_rows:
        market = row["market"]
        thesis = state["theses"].get(market) or {}
        check = checks.get(market)
        if check is None:
            continue
        universe_row = universe_by_market.get(market)
        if universe_row is None:
            continue

        scored = _score_execution(row, universe_row, check, now)
        final = scored["final"]
        execution = scored["execution"]
        sizing = scored["sizing"]
        plan = execution.get("plan") or {}
        selectable = bool(final.get("selectable") and sizing and execution.get("ready"))

        baseline_v31 = v31_by_market.get(market) or {}
        result = {
            "market": market,
            "thesis_id": thesis.get("thesis_id"),
            "price_eur": finite(row.get("price_eur")),
            "entry_path": "MEMORY_ENTRY_CHALLENGER",
            "execution": execution,
            "preliminary": scored["preliminary"],
            "economic_score": finite(final.get("score"), 0.0),
            "selectable": selectable,
            "selection_reason": final.get("reason"),
            "sizing": sizing,
            "baseline_v31_selectable_same_cycle": bool(baseline_v31.get("selectable")),
            "baseline_v31_entry_path_same_cycle": baseline_v31.get("entry_path"),
            "baseline_thesis_seed_same_cycle": bool((candidate_by_market.get(market) or {}).get("thesis_seed")),
            "baseline_entry_hypothesis_same_cycle": bool((candidate_by_market.get(market) or {}).get("entry_hypothesis")),
        }
        ranked_extra.append(result)

        ms = state["markets"].setdefault(market, {})
        signature = "|".join([
            "QUALIFIED" if selectable else "REJECTED",
            str(final.get("reason") or ""),
            str(execution.get("reason") or ""),
            str(thesis.get("thesis_id") or ""),
        ])
        if ms.get("last_decision_signature") != signature:
            ms["decision_sequence"] = int(ms.get("decision_sequence", 0)) + 1
            attempt_id = (
                f"{market}|{thesis.get('thesis_id')}|"
                f"{ms['decision_sequence']}|{CHALLENGER_VERSION}"
            )
            event = {
                "event_type": (
                    "MEMORY_ENTRY_CHALLENGER_QUALIFIED"
                    if selectable
                    else "MEMORY_ENTRY_CHALLENGER_REJECTED"
                ),
                "market": market,
                "thesis_id": thesis.get("thesis_id"),
                "attempt_id": attempt_id,
                "decision_id": attempt_id,
                "decision_ts": finite(execution.get("available_ts"), now),
                "decision_at_utc": execution.get("available_at_utc") or utc(now),
                "price_eur": finite(row.get("price_eur")),
                "entry_eur": finite(plan.get("entry_eur")),
                "stop_eur": finite(plan.get("stop_eur")),
                "tp1_eur": finite(plan.get("tp1_eur")),
                "stake_eur": finite((sizing or {}).get("stake_eur")),
                "economic_score": finite(final.get("score"), 0.0),
                "selection_reason": final.get("reason"),
                "execution": execution,
                "preliminary": scored["preliminary"],
                "sizing": sizing,
                "entry_path": "MEMORY_ENTRY_CHALLENGER",
                "baseline_v31_selectable_same_cycle": bool(baseline_v31.get("selectable")),
                "baseline_v31_entry_path_same_cycle": baseline_v31.get("entry_path"),
                "origin_left_censored": bool(thesis.get("origin_left_censored")),
                "evaluations": {},
            }
            _append_event(journal, event)
            ms["last_decision_signature"] = signature
            ms["last_attempt_id"] = attempt_id
        else:
            attempt_id = ms.get("last_attempt_id")

        if selectable:
            qualified_extra.append({
                **result,
                "episode": thesis.get("thesis_id"),
                "decision_id": attempt_id,
                "entry_eur": finite(plan.get("entry_eur")),
                "stop_eur": finite(plan.get("stop_eur")),
            })

    # Full-system variant C: fork the baseline once, then feed it baseline
    # qualifications PLUS the incremental challenger qualifications.
    if (
        portfolio.get("challenger_version") != CHALLENGER_VERSION
        or not portfolio.get("challenger_inception_at_utc")
    ):
        portfolio = copy.deepcopy(baseline_portfolio)
        portfolio["challenger_inception_at_utc"] = utc(now)
        portfolio["challenger_inception_ts"] = now
        portfolio["challenger_inception_marked_value_eur"] = finite(
            baseline_portfolio.get("marked_value_eur")
        )
        portfolio["challenger_inception_baseline_closed_count"] = len(
            baseline_portfolio.get("closed") or []
        )
        portfolio["challenger_version"] = CHALLENGER_VERSION
        portfolio.setdefault("actions", []).append({
            "at_utc": utc(now),
            "action": "FORK_BASELINE_FOR_MEMORY_ENTRY_CHALLENGER",
            "marked_value_eur": finite(baseline_portfolio.get("marked_value_eur")),
        })

    baseline_qualified = _baseline_qualified_rows(v31_candidates)
    combined = baseline_qualified + qualified_extra
    # Comparator hygiene: refresh every current V3.1 market score exactly as the
    # baseline portfolio does.  This prevents stale scores from changing rotation
    # behavior independently of the memory treatment.
    scores = _current_score_map(v31_candidates, qualified_extra)

    portfolio = update_portfolio(
        portfolio,
        combined,
        universe_by_market,
        scores,
        now,
        client=client,
        allow_score_rotation=True,
    )
    portfolio["challenger_version"] = CHALLENGER_VERSION
    portfolio["treatment"] = (
        "BASELINE_PLUS_NEAR_MISS_MAY_SEED_PERSISTENT_THESIS;"
        "UNCHANGED_EXECUTION_AND_V31_SELECTION;"
        "CURRENT_SCORE_REFRESH_IDENTICAL_TO_BASELINE"
    )

    ranked_extra.sort(key=lambda x: finite(x.get("economic_score"), 0.0), reverse=True)
    candidate_doc = {
        "schema": "solaire_memory_entry_challenger_candidates_v1",
        "generated_at_utc": utc(now),
        "architecture_version": CHALLENGER_VERSION,
        "baseline_v3_architecture_version": V3_ARCHITECTURE_VERSION,
        "baseline_v31_architecture_version": V31_ARCHITECTURE_VERSION,
        "research_only": True,
        "single_treatment": "NEAR_MISS_CAN_SEED_PERSISTENT_THESIS",
        "candidates": ranked_extra,
    }

    baseline_marked = finite(baseline_portfolio.get("marked_value_eur"))
    challenger_marked = finite(portfolio.get("marked_value_eur"))
    status = {
        "schema": "solaire_memory_entry_challenger_status_v1",
        "checked_at_utc": utc(now),
        "status": "OK_WITH_SOURCE_GAPS" if source_errors else "OK",
        "architecture_version": CHALLENGER_VERSION,
        "baseline_v3_architecture_version": V3_ARCHITECTURE_VERSION,
        "baseline_v31_architecture_version": V31_ARCHITECTURE_VERSION,
        "treatment_seed_markets": len(treatment_markets),
        "active_experimental_theses": sum(
            bool(x.get("active")) for x in state["theses"].values()
        ),
        "reentry_ready_count": len(reentry_rows),
        "execution_checks": len(checks),
        "qualified_extra_count": len(qualified_extra),
        "profile_fairness": profile_fairness,
        "execution_fairness": execution_fairness,
        "challenger_portfolio_marked_value_eur": challenger_marked,
        "baseline_portfolio_marked_value_eur": baseline_marked,
        "challenger_minus_baseline_eur": (
            None
            if baseline_marked is None or challenger_marked is None
            else round(challenger_marked - baseline_marked, 2)
        ),
        "source_errors": source_errors[:40],
        "research_only": True,
        "affects_v3": False,
        "affects_v31": False,
        "affects_v2": False,
        "affects_email": False,
        "orders_submitted": False,
    }

    state["initialized"] = True
    state["updated_at_utc"] = utc(now)
    journal["updated_at_utc"] = utc(now)
    journal["architecture_version"] = CHALLENGER_VERSION
    journal["events"] = journal["events"][-10000:]

    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(CANDIDATES, candidate_doc)
    atomic_json(PORTFOLIO, portfolio)
    atomic_json(STATUS, status)

    print("SOLAIRE_MEMORY_ENTRY_CHALLENGER " + json.dumps(status, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
