"""Solaire V3 prospective-shadow helpers.

V3 is deliberately separate from the frozen Solaire V2 decision path.
It provides independent research layers for context/narratives, adaptive time
horizons, capital rotation, global price discovery, entry timing and persistent
opportunity theses.

Nothing in this module sends mail or submits orders.
"""
from __future__ import annotations

import math
import re
import statistics
from typing import Any

from research.common import finite

FROZEN_V2_COMMIT = "34b042121bb8425b0e4b46e3d1a694d4b1f4ec75"
REFERENCE_STAKE_EUR = 100.0
REFERENCE_CAPITAL_EUR = 2400.0
MAX_SHADOW_POSITIONS = 3
ROUND_TRIP_COST_PCT = 0.70
HORIZONS_HOURS = (4, 24, 48, 72, 96, 168, 336, 720)

THESIS_MAX_AGE_SECONDS = 7 * 24 * 3600
THESIS_PULLBACK_MIN_PCT = -2.0
THESIS_RECLAIM_MIN_PCT = 1.0
THESIS_INVALIDATION_FROM_ANCHOR_PCT = -12.0

NARRATIVES = {
    "AI_COMPUTE": {"AIOZ", "PHA", "AKT", "NOS", "FET", "TAO", "RENDER", "RNDR", "GRASS", "VVV"},
    "DEPIN": {"AIOZ", "AKT", "NOS", "GRASS", "RENDER", "RNDR", "FIL", "AR"},
    "RWA_TOKENIZATION": {"ONDO", "QNT", "LINK", "POLYX", "CFG"},
    "DEFI": {"UNI", "AAVE", "MKR", "ENA", "CRV", "LDO", "KMNO", "DRIFT"},
    "SOLANA_ECOSYSTEM": {"SOL", "JUP", "JTO", "KMNO", "DRIFT", "PENGU", "BONK", "WIF", "RAY", "ZETA"},
    "PRIVACY": {"ZEC", "XMR", "SCRT", "ZAMA", "ARRR"},
    "STORAGE_DATA": {"FIL", "AR", "GRT", "AIOZ", "FLUX"},
    "L1_L2": {"ETH", "SOL", "SEI", "SUI", "AVAX", "NEAR", "TIA", "SAGA", "ICX", "ZETA"},
    "MEME_HIGH_BETA": {"DOGE", "SHIB", "BONK", "PENGU", "FARTCOIN", "GOAT", "WIF", "PEPE"},
}

TOKEN_ALIASES = {
    "BTC": ("bitcoin", "btc"),
    "ETH": ("ethereum", "ether", "eth"),
    "SOL": ("solana", "sol"),
    "BCH": ("bitcoin cash", "bch"),
    "ZETA": ("zetachain", "zeta"),
    "ZRO": ("layerzero", "zro"),
    "SEI": ("sei network", "sei"),
    "AIOZ": ("aioz",),
    "PHA": ("phala", "pha"),
    "AKT": ("akash", "akt"),
    "NOS": ("nosana", "nos"),
    "FET": ("fetch.ai", "fetch ai", "artificial superintelligence alliance", "fet"),
    "TAO": ("bittensor", "tao"),
    "GRASS": ("grass network", "grass"),
    "DRIFT": ("drift protocol", "drift"),
    "KMNO": ("kamino", "kmno"),
    "KERNEL": ("kerneldao", "kernel"),
    "NIL": ("nillion", "nil"),
    "NEAR": ("near protocol", "near"),
    "ICX": ("icon network", "icx"),
    "ZRC": ("zircuit", "zrc"),
    "SAGA": ("saga protocol", "saga"),
    "ZEC": ("zcash", "zec"),
    "GRT": ("the graph", "grt"),
    "FLUX": ("flux network",),
    "PENGU": ("pudgy penguins", "pengu"),
    "BONK": ("bonk",),
    "QNT": ("quant network", "qnt"),
}


def build_asset_aliases(
    universe_rows: list[dict[str, Any]],
    asset_rows: list[dict[str, Any]] | None = None,
    supplemental_aliases: dict[str, tuple[str, ...]] | None = None,
) -> dict[str, tuple[str, ...]]:
    """Build news aliases for every Bitvavo EUR asset, not a hand-picked subset.

    The market universe supplies complete ticker coverage. Bitvavo /assets adds
    the canonical project name dynamically; TOKEN_ALIASES is retained only as
    supplemental synonym data for names that are commonly written differently.
    """
    symbols = {
        base_symbol(row.get("market"))
        for row in universe_rows
        if row.get("market")
    }
    symbols.discard("")
    names: dict[str, str] = {}
    for row in asset_rows or []:
        symbol = str(row.get("symbol") or "").upper().strip()
        name = str(row.get("name") or "").strip()
        if symbol and name:
            names[symbol] = name

    supplemental = supplemental_aliases if supplemental_aliases is not None else TOKEN_ALIASES
    result: dict[str, tuple[str, ...]] = {}
    for symbol in sorted(symbols):
        aliases: set[str] = set()
        name = names.get(symbol)
        if name:
            aliases.add(name)
            low = name.lower().strip()
            for suffix in (" token", " protocol", " network"):
                if low.endswith(suffix):
                    short = name[: -len(suffix)].strip()
                    if len(short) >= 4:
                        aliases.add(short)
        for alias in supplemental.get(symbol, ()):
            alias = str(alias or "").strip()
            if alias:
                aliases.add(alias)
        result[symbol] = tuple(sorted(aliases, key=lambda x: (len(x), x.lower()), reverse=True))
    return result


def match_news_assets(
    text: str,
    asset_aliases: dict[str, tuple[str, ...]],
    generic_symbols: set[str] | None = None,
) -> list[str]:
    """Resolve arbitrary news text to the complete Bitvavo asset map.

    Project names and aliases are matched case-insensitively. Tickers are
    matched only when explicitly formatted ($ABC, (ABC), [ABC]) or written in
    uppercase, which limits false positives from ordinary words such as NEAR,
    SAFE or MOVE.
    """
    original = " " + re.sub(r"\\s+", " ", str(text or "")) + " "
    low = original.lower()
    generic = {str(x).upper() for x in (generic_symbols or set())}
    hits: list[str] = []
    for symbol, aliases in asset_aliases.items():
        symbol = symbol.upper()
        matched = False
        for alias in aliases:
            a = str(alias or "").lower().strip()
            if len(a) < 4 or a == symbol.lower():
                continue
            if re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", low):
                matched = True
                break
        if not matched:
            explicit_patterns = (
                r"\\$" + re.escape(symbol) + r"(?![A-Z0-9])",
                r"\\(" + re.escape(symbol) + r"\\)",
                r"\\[" + re.escape(symbol) + r"\\]",
            )
            if any(re.search(p, original) for p in explicit_patterns):
                matched = True
            elif len(symbol) >= 3 and symbol not in generic:
                matched = bool(re.search(r"(?<![A-Za-z0-9])" + re.escape(symbol) + r"(?![A-Za-z0-9])", original))
        if matched:
            hits.append(symbol)
    return sorted(set(hits))


def structured_news_symbols(value: Any, allowed_symbols: set[str]) -> list[str]:
    """Use provider-supplied categories/tickers when they map to Bitvavo."""
    if value is None:
        return []
    allowed = {str(x).upper() for x in allowed_symbols}
    tokens = re.findall(r"[A-Za-z0-9]{1,20}", str(value).upper())
    return sorted({token for token in tokens if token in allowed})


def _n(value: Any, default: float = 0.0) -> float:
    result = finite(value)
    return default if result is None else result


def base_symbol(market: str | None) -> str:
    return str(market or "").upper().split("-")[0]


def median(values: list[float]) -> float | None:
    vals = [x for x in values if x is not None and math.isfinite(x)]
    return statistics.median(vals) if vals else None


def narratives_for_market(market: str) -> list[str]:
    symbol = base_symbol(market)
    return [name for name, members in NARRATIVES.items() if symbol in members]


def build_narrative_rotations(universe: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Describe sector rotation without using it as an automatic BUY rule."""
    market_1h = []
    market_4h = []
    rows = {}
    for row in universe:
        f15 = ((row.get("features") or {}).get("15m") or {})
        r1 = finite(f15.get("return_4bar_pct"))
        r4 = finite(f15.get("return_16bar_pct"))
        if r1 is not None:
            market_1h.append(r1)
        if r4 is not None:
            market_4h.append(r4)
        rows[base_symbol(row.get("market"))] = (r1, r4)
    global_1h = median(market_1h) or 0.0
    global_4h = median(market_4h) or 0.0

    result = {}
    for name, members in NARRATIVES.items():
        values = [(s, *rows[s]) for s in members if s in rows]
        r1s = [x[1] for x in values if x[1] is not None]
        r4s = [x[2] for x in values if x[2] is not None]
        if len(values) < 3 or len(r1s) < 2 or len(r4s) < 2:
            continue
        m1 = median(r1s) or 0.0
        m4 = median(r4s) or 0.0
        breadth = 100.0 * sum((x[1] or -999) > global_1h for x in values if x[1] is not None) / len(r1s)
        rel1 = m1 - global_1h
        rel4 = m4 - global_4h
        score = 0.0
        score += min(1.2, max(0.0, rel1 / 1.25))
        score += min(1.2, max(0.0, rel4 / 3.0))
        score += min(0.6, max(0.0, (breadth - 50.0) / 50.0 * 0.6))
        result[name] = {
            "members_observed": len(values),
            "median_1h_pct": round(m1, 4),
            "median_4h_pct": round(m4, 4),
            "relative_1h_pp": round(rel1, 4),
            "relative_4h_pp": round(rel4, 4),
            "breadth_above_market_1h_pct": round(breadth, 2),
            "rotation_score_0_3": round(score, 3),
            "active_watch": score >= 1.2,
        }
    return result


def early_quant_evidence(row: dict[str, Any]) -> dict[str, Any]:
    """Earlier confirmation hypothesis than V2, but still requires multiple facts."""
    f5 = ((row.get("features") or {}).get("5m") or {})
    context = row.get("context") or {}
    if not f5.get("valid"):
        return {"ready": False, "score_0_10": 0.0, "evidence_count": 0, "flags": {}}

    flags = {
        "positive_20m": _n(f5.get("return_4bar_pct")) >= 0.40,
        "momentum_acceleration": _n(f5.get("momentum_acceleration_pp")) >= 0.10,
        "volume_expansion": max(_n(f5.get("relative_volume")), _n(f5.get("volume_4_vs_prev4"))) >= 1.25,
        "relative_strength_1h": _n(context.get("relative_strength_1h_pp")) >= 0.50,
        "near_or_above_breakout": _n(f5.get("distance_to_breakout_pct"), -999.0) >= -1.0,
    }
    evidence_count = sum(flags.values())
    raw = (
        min(2.2, max(0.0, _n(f5.get("return_4bar_pct")) * 1.8))
        + min(2.0, max(0.0, _n(f5.get("momentum_acceleration_pp")) * 2.5))
        + min(2.0, max(0.0, (max(_n(f5.get("relative_volume")), _n(f5.get("volume_4_vs_prev4"))) - 1.0) * 2.5))
        + min(2.0, max(0.0, _n(context.get("relative_strength_1h_pp")) * 1.2))
        + min(1.8, max(0.0, (_n(f5.get("distance_to_breakout_pct")) + 1.0) * 1.2))
    )
    score = round(min(10.0, raw), 3)
    return {
        "ready": evidence_count >= 3 and score >= 4.0,
        "score_0_10": score,
        "evidence_count": evidence_count,
        "flags": flags,
    }


def walk_asks(book: dict[str, Any], notional_eur: float = REFERENCE_STAKE_EUR) -> dict[str, Any]:
    """Walk visible ask depth rather than trusting best ask alone."""
    asks = book.get("asks") or []
    remaining = float(notional_eur)
    acquired = 0.0
    spent = 0.0
    best = None
    levels = 0
    for level in asks:
        if not isinstance(level, (list, tuple)) or len(level) < 2:
            continue
        px = finite(level[0])
        qty = finite(level[1])
        if px is None or qty is None or px <= 0 or qty <= 0:
            continue
        if best is None:
            best = px
        level_eur = px * qty
        take = min(remaining, level_eur)
        acquired += take / px
        spent += take
        remaining -= take
        levels += 1
        if remaining <= 1e-9:
            break
    if best is None or remaining > 0 or acquired <= 0:
        return {
            "valid": False,
            "reason": "INSUFFICIENT_VISIBLE_ASK_DEPTH",
            "target_eur": notional_eur,
            "visible_filled_eur": round(spent, 6),
            "levels_used": levels,
        }
    vwap = spent / acquired
    return {
        "valid": True,
        "target_eur": notional_eur,
        "vwap_eur": vwap,
        "best_ask_eur": best,
        "depth_slippage_pct": (vwap / best - 1.0) * 100.0,
        "levels_used": levels,
    }


def score_opportunity(
    early_quant_score: float,
    news_score: float,
    narrative_score: float,
    external_score: float,
) -> float:
    """Research ranking only. This is not a calibrated probability."""
    score = (
        0.35 * min(10.0, max(0.0, early_quant_score))
        + 0.20 * min(10.0, max(0.0, news_score))
        + 0.20 * min(10.0, max(0.0, narrative_score))
        + 0.25 * min(10.0, max(0.0, external_score))
    )
    return round(score, 3)


def classify_horizon(row: dict[str, Any]) -> str:
    """Provisional opportunity role, allowed to evolve as evidence changes."""
    news = _n(row.get("news_score"))
    narrative = _n(row.get("narrative_score"))
    external = _n(row.get("external_score"))
    quant = _n((row.get("early_quant") or {}).get("score_0_10"))
    if news >= 5.0 and narrative >= 4.0 and external >= 4.0:
        return "POSITION"
    if narrative >= 3.0 and quant >= 4.0:
        return "SWING"
    if external >= 3.0 or quant >= 5.0:
        return "TACTICAL"
    return "WATCH"



def advance_persistent_thesis(
    prior: dict[str, Any] | None,
    row: dict[str, Any],
    now: float,
) -> dict[str, Any]:
    """Advance a research-only opportunity thesis independently of entry.

    A thesis can survive the disappearance of the short acceleration that
    created it.  The thresholds are deliberately simple hypotheses to measure
    prospectively, not calibrated production rules.
    """
    thesis = dict(prior or {})
    price = finite(row.get("price_eur"))
    fresh = bool(row.get("fresh_opportunity_trigger"))
    long_trend = row.get("long_trend") or {}
    long_support = bool(long_trend.get("support"))
    early = row.get("early_quant") or {}
    short_support = (
        fresh
        or bool(row.get("context_watch"))
        or _n(row.get("external_score")) >= 1.0
        or int(early.get("evidence_count") or 0) >= 2
    )
    support = bool(short_support or long_support)

    if not thesis.get("active"):
        if not fresh or price is None or price <= 0:
            return thesis
        thesis_id = int(thesis.get("thesis_id") or 0) + 1
        return {
            "thesis_id": thesis_id,
            "active": True,
            "state": "ACTIVE_THESIS",
            "opened_ts": now,
            "opened_price_eur": price,
            "last_seen_ts": now,
            "last_price_eur": price,
            "peak_eur": price,
            "low_eur": price,
            "pullback_seen": False,
            "pullback_low_eur": None,
            "start_opportunity_score": _n(row.get("opportunity_score")),
            "best_opportunity_score": _n(row.get("opportunity_score")),
            "start_horizon_class": row.get("horizon_class"),
            "last_horizon_class": row.get("horizon_class"),
            "last_long_trend": long_trend,
            "last_support": support,
            "fresh_trigger_count": 1,
        }

    if price is None or price <= 0:
        thesis["last_seen_ts"] = now
        thesis["last_support"] = support
        if long_trend:
            thesis["last_long_trend"] = long_trend
        return thesis

    anchor = finite(thesis.get("opened_price_eur"), price)
    previous_peak = finite(thesis.get("peak_eur"), price)
    previous_low = finite(thesis.get("low_eur"), price)
    peak = max(previous_peak, price)
    low = min(previous_low, price)
    thesis["peak_eur"] = peak
    thesis["low_eur"] = low
    thesis["last_price_eur"] = price
    thesis["last_seen_ts"] = now
    thesis["last_support"] = support
    thesis["last_horizon_class"] = row.get("horizon_class")
    thesis["best_opportunity_score"] = max(
        _n(thesis.get("best_opportunity_score")),
        _n(row.get("opportunity_score")),
    )
    if long_trend:
        thesis["last_long_trend"] = long_trend
    if fresh:
        thesis["fresh_trigger_count"] = int(thesis.get("fresh_trigger_count") or 0) + 1

    anchor_return = (price / anchor - 1.0) * 100.0 if anchor else 0.0
    drawdown_from_peak = (price / peak - 1.0) * 100.0 if peak else 0.0
    thesis["return_from_open_pct"] = round(anchor_return, 4)
    thesis["drawdown_from_peak_pct"] = round(drawdown_from_peak, 4)
    thesis["age_hours"] = round(max(0.0, now - _n(thesis.get("opened_ts"), now)) / 3600.0, 3)

    if drawdown_from_peak <= THESIS_PULLBACK_MIN_PCT:
        thesis["pullback_seen"] = True
        existing_pullback_low = finite(thesis.get("pullback_low_eur"), price)
        thesis["pullback_low_eur"] = min(existing_pullback_low, price)

    pullback_low = finite(thesis.get("pullback_low_eur"))
    reclaim = None
    if pullback_low is not None and pullback_low > 0:
        reclaim = (price / pullback_low - 1.0) * 100.0
        thesis["reclaim_from_pullback_low_pct"] = round(reclaim, 4)

    age = max(0.0, now - _n(thesis.get("opened_ts"), now))
    if anchor_return <= THESIS_INVALIDATION_FROM_ANCHOR_PCT:
        thesis["active"] = False
        thesis["state"] = "INVALIDATED_THESIS"
        thesis["ended_ts"] = now
        thesis["end_reason"] = "ANCHOR_DRAWDOWN"
    elif age >= THESIS_MAX_AGE_SECONDS and not support:
        thesis["active"] = False
        thesis["state"] = "EXPIRED_THESIS"
        thesis["ended_ts"] = now
        thesis["end_reason"] = "MAX_AGE_WITHOUT_SUPPORT"
    elif bool(thesis.get("pullback_seen")) and reclaim is not None and reclaim >= THESIS_RECLAIM_MIN_PCT and support:
        thesis["state"] = "REENTRY_READY_THESIS"
    elif bool(thesis.get("pullback_seen")):
        thesis["state"] = "PULLBACK_THESIS"
    elif anchor_return >= 2.0 and support:
        thesis["state"] = "CONTINUATION_THESIS"
    else:
        thesis["state"] = "ACTIVE_THESIS"
    return thesis


def evaluate_candles_strict(
    baseline: float,
    decision_ts: float,
    candles: list[dict[str, Any]],
    horizon_hours: int,
    *,
    interval_ms: int,
    stop_eur: float | None = None,
    round_trip_cost_pct: float = ROUND_TRIP_COST_PCT,
) -> dict[str, Any] | None:
    """Chronological evaluator with strict start/end coverage.

    It rejects incomplete horizons rather than declaring them complete from a
    trailing candle. The decision-containing bar is excluded.
    """
    if baseline <= 0 or decision_ts <= 0:
        return None
    first_start = ((int(decision_ts * 1000) // interval_ms) + 1) * interval_ms
    horizon_end = int((decision_ts + horizon_hours * 3600) * 1000)
    last_start = ((horizon_end // interval_ms) * interval_ms)
    if last_start + interval_ms > horizon_end:
        last_start -= interval_ms
    rows = []
    for bar in candles:
        t = finite(bar.get("t"))
        h = finite(bar.get("h"))
        l = finite(bar.get("l"))
        c = finite(bar.get("c"))
        if None in (t, h, l, c):
            continue
        if first_start <= int(t) <= last_start:
            rows.append((int(t), h, l, c))
    rows.sort(key=lambda x: x[0])
    expected_count = 0
    if last_start >= first_start:
        expected_count = (last_start - first_start) // interval_ms + 1
    complete = (
        expected_count > 0
        and len(rows) == expected_count
        and rows[0][0] == first_start
        and rows[-1][0] == last_start
        and all(b[0] - a[0] == interval_ms for a, b in zip(rows, rows[1:]))
        and rows[-1][0] + interval_ms <= horizon_end
    )
    if not rows:
        return None

    high = max(x[1] for x in rows)
    low = min(x[2] for x in rows)
    close = rows[-1][3]
    mfe = (high / baseline - 1.0) * 100.0
    mae = (low / baseline - 1.0) * 100.0
    close_ret = (close / baseline - 1.0) * 100.0
    result = {
        "horizon_hours": horizon_hours,
        "complete_horizon": complete,
        "bars_used": len(rows),
        "bars_expected": int(expected_count),
        "mfe_pct": round(mfe, 4),
        "mae_pct": round(mae, 4),
        "close_return_pct": round(close_ret, 4),
        "net_close_return_pct_est": round(close_ret - round_trip_cost_pct, 4),
        "stop_hit": bool(stop_eur and low <= stop_eur),
        "method": "strict_chronological_complete_intervals",
    }
    for target in (10, 20, 50, 100):
        result[f"mfe_ge_{target}pct"] = mfe >= target
        first = next((t for t, h, _, _ in rows if h >= baseline * (1 + target / 100)), None)
        result[f"first_plus_{target}_ts"] = None if first is None else first / 1000
    return result
