"""Decision Layer V1 over frozen V3/V4 signals.

This module deliberately does not change V4 scores or thresholds. It converts
scanner evidence into explicit, measurable decision buckets so that timing
quality (Entry) cannot silently veto a structurally strong opportunity.
"""
from __future__ import annotations

from typing import Any


BUCKET_IMMEDIATE = "MEILLEUR_ACHAT_IMMEDIAT"
BUCKET_LIMIT = "MEILLEURE_LIMITE_PASSIVE"
BUCKET_LATENT = "MEILLEUR_LATENT_ACCELERATOR"
BUCKET_REENTRY = "MEILLEUR_PULLBACK_REENTRY"
BUCKETS = (BUCKET_IMMEDIATE, BUCKET_LIMIT, BUCKET_LATENT, BUCKET_REENTRY)

# Only hard execution/data failures can veto a candidate outright. Timing and
# chase diagnostics remain inputs to the action/bucket instead of automatic
# rejection rules.
HARD_VETO_FLAGS = {
    "DATA UNAVAILABLE",
    "PIPELINE_DEGRADED",
    "EXCHANGE_CLOCK_SKEW",
    "ILLIQUID",
    "LOW_LIQUIDITY",
    "WIDE_SPREAD_RISK",
    "VERY_WIDE_SPREAD_RISK",
    "ENTRY_INPUTS_UNAVAILABLE",
    "STALE_DAILY_PROFILE",
    "MISSING_5M",
    "MISSING_15M",
    "INVALID_5M",
    "INVALID_15M",
}

# Deliberately simple, pre-declared shadow thresholds. They are not advertised
# as optimized and must be evaluated prospectively before production use.
LATENT_OPPORTUNITY_MIN = 7.40
LATENT_TREND_MIN = 7.30
IMMEDIATE_ENTRY_MIN = 6.80
PASSIVE_LIMIT_ENTRY_MIN = 5.80
REENTRY_TREND_MIN = 7.60


def _n(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def structural_vetoes(obs: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    quality = obs.get("data_quality") or {}
    if not quality.get("ok", False):
        reasons.extend(quality.get("reasons") or ["DATA UNAVAILABLE"])
    for flag in obs.get("exclusions") or []:
        text = str(flag)
        if text in HARD_VETO_FLAGS or text.startswith("MISSING_") or text.startswith("INVALID_"):
            reasons.append(text)
    return sorted(set(reasons))


def _scores(obs: dict[str, Any]) -> tuple[float, float, float]:
    b = obs.get("baseline") or {}
    return (_n(b.get("opportunity_score")), _n(b.get("entry_score")), _n(b.get("trend_score")))


def _remaining_upside_score(obs: dict[str, Any]) -> float:
    """Cross-sectional ranking score, intentionally not a probability.

    Opportunity/trend dominate. Entry is only a timing modifier. Strong chase
    or wick diagnostics reduce rank but never erase a structural candidate.
    """
    opp, entry, trend = _scores(obs)
    change24 = _n(obs.get("change_24h_pct"))
    chase = _n((obs.get("chase_risk") or {}).get("score"))
    wick = 1.0 if (obs.get("wick_setup") or {}).get("is_wick_setup") else 0.0
    recurrence = _n((obs.get("recurrence") or {}).get("distinct_15m_periods"))
    return round(
        0.46 * opp
        + 0.36 * trend
        + 0.12 * entry
        + min(recurrence, 4.0) * 0.06
        - max(change24 - 10.0, 0.0) * 0.035
        - chase * 0.055
        - wick * 0.08,
        4,
    )


def classify(obs: dict[str, Any]) -> dict[str, Any]:
    opp, entry, trend = _scores(obs)
    vetoes = structural_vetoes(obs)
    baseline = obs.get("baseline") or {}
    state = baseline.get("action_status") or baseline.get("raw_action_status") or ""
    category = str(obs.get("category") or "")
    flags = set(baseline.get("risk_flags") or []) | set(obs.get("exclusions") or [])

    result = {
        "market": obs.get("market"),
        "price_eur": obs.get("price_eur"),
        "opportunity_score": opp,
        "entry_score": entry,
        "trend_score": trend,
        "rank_score": _remaining_upside_score(obs),
        "bucket": None,
        "action": "WATCH",
        "structural_vetoes": vetoes,
        "reason": "",
    }
    if not baseline:
        result["reason"] = "No V4 structural candidate."
        return result
    if vetoes:
        result["action"] = "VETO_STRUCTUREL"
        result["reason"] = "Hard data/execution veto: " + ", ".join(vetoes)
        return result

    strong_structure = opp >= LATENT_OPPORTUNITY_MIN and trend >= LATENT_TREND_MIN
    pullback_like = (
        state in {"ENTRY_WINDOW", "REENTRY_READY"}
        or "WICK_SETUP" in flags
        or _n(obs.get("change_24h_pct")) < 0
    )

    if baseline.get("buy_ready") and entry >= IMMEDIATE_ENTRY_MIN and category != "TOO LATE":
        result.update(bucket=BUCKET_IMMEDIATE, action="ACHETE_MAINTENANT",
                      reason="V4 buy-ready with acceptable current entry; no structural veto.")
    elif strong_structure and pullback_like and trend >= REENTRY_TREND_MIN:
        result.update(bucket=BUCKET_REENTRY, action="ATTENDS_REPRISE_OU_REENTREE",
                      reason="Strong trend/opportunity retained through pullback; timing does not erase setup.")
    elif strong_structure and PASSIVE_LIMIT_ENTRY_MIN <= entry < IMMEDIATE_ENTRY_MIN and category != "TOO LATE":
        result.update(bucket=BUCKET_LIMIT, action="PLACE_LIMITE_PASSIVE",
                      reason="Strong structure but imperfect current entry; prefer passive execution.")
    elif strong_structure and entry < PASSIVE_LIMIT_ENTRY_MIN:
        # IOST-like case: a weak instantaneous entry score is not a veto when
        # opportunity + trend are already coherent.
        result.update(bucket=BUCKET_LATENT, action="LATENT_ACCELERATOR",
                      reason="Strong structural opportunity retained despite weak instantaneous entry.")
    elif state == "REENTRY_READY" or (trend >= REENTRY_TREND_MIN and pullback_like):
        result.update(bucket=BUCKET_REENTRY, action="ATTENDS_REPRISE_OU_REENTREE",
                      reason="Trend remains strong; candidate retained for re-entry instead of discarded.")
    else:
        result["reason"] = "Candidate retained as watch; no decision bucket threshold met."
    return result


def decide(observations: list[dict[str, Any]], top_n: int = 3) -> dict[str, Any]:
    """Return full ranked decisions plus one winner per mandatory bucket.

    The complete ranking is persisted so rejected/weak-entry candidates can be
    evaluated 24-72h later without reconstructing decisions retrospectively.
    """
    ranked = [classify(o) for o in observations]
    ranked.sort(key=lambda r: (r["rank_score"], r["opportunity_score"], r["trend_score"]), reverse=True)

    winners: dict[str, dict[str, Any] | None] = {b: None for b in BUCKETS}
    for row in ranked:
        bucket = row.get("bucket")
        if bucket in winners and winners[bucket] is None:
            winners[bucket] = row

    actionable = [r for r in ranked if r.get("bucket")][:top_n]
    return {
        "schema_version": 1,
        "policy": "DECISION_LAYER_V1_SHADOW",
        "frozen_scanner_policy": "V4_FROZEN_20260908",
        "principles": {
            "entry_is_timing_not_veto": True,
            "only_structural_vetoes_block": True,
            "cross_sectional_ranking": True,
            "mandatory_buckets": list(BUCKETS),
            "probabilities_calibrated": False,
            "production_orders_enabled": False,
        },
        "thresholds": {
            "latent_opportunity_min": LATENT_OPPORTUNITY_MIN,
            "latent_trend_min": LATENT_TREND_MIN,
            "immediate_entry_min": IMMEDIATE_ENTRY_MIN,
            "passive_limit_entry_min": PASSIVE_LIMIT_ENTRY_MIN,
            "reentry_trend_min": REENTRY_TREND_MIN,
        },
        "bucket_winners": winners,
        "top_actionable": actionable,
        "ranked": ranked,
    }
