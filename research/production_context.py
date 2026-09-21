"""Non-blocking market context for Solaire V2.

Uses only features already collected by the direct 426-market Bitvavo scan.
It is descriptive/shadow context: it must never reduce scan coverage or act as
an execution veto unless independently validated later.
"""
from __future__ import annotations

import statistics
from typing import Any

from research.common import finite


BENCHMARKS = ("BTC-EUR", "ETH-EUR", "SOL-EUR")


def _num(value: Any) -> float | None:
    return finite(value)


def _median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def _mean(values: list[float]) -> float | None:
    return statistics.mean(values) if values else None


def _breadth(values: list[float]) -> float | None:
    return 100.0 * sum(value > 0 for value in values) / len(values) if values else None


def _round(value: float | None, digits: int = 4) -> float | None:
    return None if value is None else round(value, digits)


def build_market_context(observations: list[dict[str, Any]]) -> dict[str, Any]:
    usable = [
        obs
        for obs in observations
        if (obs.get("data_quality") or {}).get("ok", False)
    ]
    returns_1h: list[float] = []
    returns_4h: list[float] = []
    by_market: dict[str, dict[str, float | None]] = {}

    for obs in usable:
        market = obs.get("market")
        f15 = ((obs.get("features") or {}).get("15m") or {})
        r1 = _num(f15.get("return_4bar_pct"))
        r4 = _num(f15.get("return_16bar_pct"))
        if r1 is not None:
            returns_1h.append(r1)
        if r4 is not None:
            returns_4h.append(r4)
        if market:
            by_market[market] = {"return_1h_pct": r1, "return_4h_pct": r4}

    median_1h = _median(returns_1h)
    median_4h = _median(returns_4h)
    breadth_1h = _breadth(returns_1h)
    breadth_4h = _breadth(returns_4h)

    benchmark = {}
    for market in BENCHMARKS:
        row = by_market.get(market, {})
        benchmark[market] = {
            "return_1h_pct": _round(_num(row.get("return_1h_pct"))),
            "return_4h_pct": _round(_num(row.get("return_4h_pct"))),
        }

    benchmark_4h = [
        row["return_4h_pct"]
        for row in benchmark.values()
        if row.get("return_4h_pct") is not None
    ]
    positive_benchmarks = sum(value > 0 for value in benchmark_4h)
    negative_benchmarks = sum(value < 0 for value in benchmark_4h)

    # Descriptive only. These labels have no authority over BUY eligibility.
    regime = "MIXED"
    if (
        breadth_4h is not None
        and median_4h is not None
        and breadth_4h >= 60
        and median_4h > 0
        and positive_benchmarks >= 2
    ):
        regime = "BROAD_RISK_ON"
    elif (
        breadth_4h is not None
        and median_4h is not None
        and breadth_4h <= 40
        and median_4h < 0
        and negative_benchmarks >= 2
    ):
        regime = "BROAD_RISK_OFF"

    completeness = 100.0 * len(usable) / len(observations) if observations else 0.0
    return {
        "schema": "solaire_market_context_v1",
        "status": "OK" if completeness >= 95.0 else "DEGRADED",
        "affects_detection": False,
        "affects_buy_gate": False,
        "source": "same_direct_bitvavo_scan",
        "markets_total": len(observations),
        "markets_usable": len(usable),
        "completeness_pct": round(completeness, 2),
        "regime": regime,
        "breadth_positive_1h_pct": _round(breadth_1h, 2),
        "breadth_positive_4h_pct": _round(breadth_4h, 2),
        "median_return_1h_pct": _round(median_1h),
        "median_return_4h_pct": _round(median_4h),
        "mean_return_1h_pct": _round(_mean(returns_1h)),
        "mean_return_4h_pct": _round(_mean(returns_4h)),
        "benchmarks": benchmark,
    }


def candidate_context(obs: dict[str, Any], market_context: dict[str, Any]) -> dict[str, Any]:
    f15 = ((obs.get("features") or {}).get("15m") or {})
    r1 = _num(f15.get("return_4bar_pct"))
    r4 = _num(f15.get("return_16bar_pct"))
    median_1h = _num(market_context.get("median_return_1h_pct"))
    median_4h = _num(market_context.get("median_return_4h_pct"))

    return {
        "mode": "SHADOW_NON_VETO",
        "regime": market_context.get("regime"),
        "market_return_1h_pct": _round(r1),
        "market_return_4h_pct": _round(r4),
        "relative_strength_1h_pp": _round(r1 - median_1h) if r1 is not None and median_1h is not None else None,
        "relative_strength_4h_pp": _round(r4 - median_4h) if r4 is not None and median_4h is not None else None,
        "breadth_positive_1h_pct": market_context.get("breadth_positive_1h_pct"),
        "breadth_positive_4h_pct": market_context.get("breadth_positive_4h_pct"),
        "benchmarks": market_context.get("benchmarks", {}),
        "affects_buy_gate": False,
    }
