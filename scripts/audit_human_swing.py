#!/usr/bin/env python3
"""Audit Solaire against human swing horizons (7d/14d/30d).

Measurement only. This script never changes production scoring, thresholds,
alerts, orders, stops, positions, or Decision Layer behavior.

Purpose:
1) Measure actual 7d/14d/30d performance across the full active Bitvavo EUR universe.
2) For major 30d winners, reconstruct when Solaire first noticed them.
3) Quantify how much of the move had already been consumed at first detection.
4) Quantify how much upside remained after first detection.
5) Measure accept/reject churn at an hourly sampling resolution suitable for a human workflow.
"""
from __future__ import annotations

import gzip
import json
import math
import statistics
import subprocess
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient

OUT_JSON = "research/human_swing_audit_latest.json"
OUT_MD = "research/human_swing_audit_latest.md"

HORIZONS = (7, 14, 30)
THRESHOLDS = (10, 20, 30, 50, 100)
SAMPLE_SECONDS = 3600

# User-provided visual examples. They are not used to select the market-wide
# cohort; they are only reported as a named diagnostic subset.
USER_CASES = {
    "AERO-EUR", "NIL-EUR", "MAGIC-EUR", "POND-EUR", "API3-EUR",
    "MANA-EUR", "SUPER-EUR", "PLUME-EUR", "LSK-EUR", "SYN-EUR",
    "ATH-EUR", "PYTH-EUR", "FIL-EUR", "VVV-EUR", "ALGO-EUR",
    "GRASS-EUR", "GALA-EUR", "SKY-EUR", "PHA-EUR", "DRIFT-EUR",
    "SEI-EUR", "KAS-EUR", "STX-EUR", "ARB-EUR", "LPT-EUR",
    "JUP-EUR", "GTC-EUR", "MET-EUR", "AAVE-EUR", "ZRO-EUR",
}

V4_WATCH_STATES = {"WATCH", "ENTRY_WINDOW", "BUY_READY", "REENTRY_READY"}
V4_ENTRY_STATES = {"ENTRY_WINDOW", "BUY_READY", "REENTRY_READY"}
ACCEL_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}


def _pct(a: float | None, b: float | None) -> float | None:
    a, b = finite(a), finite(b)
    if a is None or b is None or a <= 0:
        return None
    return (b / a - 1.0) * 100.0


def _median(values: list[float | None]) -> float | None:
    xs = [float(x) for x in values if x is not None and math.isfinite(float(x))]
    return statistics.median(xs) if xs else None


def _fmt(value: Any, digits: int = 2) -> str:
    value = finite(value)
    return "—" if value is None else f"{value:.{digits}f}"


def _daily_rows(raw: list[Any]) -> list[dict[str, float]]:
    rows = []
    for item in raw:
        if not isinstance(item, list) or len(item) < 6:
            continue
        vals = [finite(x) for x in item[:6]]
        if any(v is None for v in vals):
            continue
        t, o, h, l, c, v = vals
        rows.append({
            "ts": t / 1000.0,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": v,
        })
    return sorted(rows, key=lambda x: x["ts"])


def _start_for_horizon(rows: list[dict[str, float]], now_ts: float, days: int) -> dict[str, float] | None:
    target = now_ts - days * 86400
    closed = [x for x in rows if x["ts"] + 86400 <= target + 60]
    return closed[-1] if closed else None


def _market_returns(client: PublicClient, market: str, last: float, now_ts: float) -> dict[str, Any]:
    raw = client.get("/" + market + "/candles", {"interval": "1d", "limit": 45}, cache=False)
    rows = _daily_rows(raw)
    result = {"market": market, "last_eur": last, "daily_candle_count": len(rows)}
    for days in HORIZONS:
        start = _start_for_horizon(rows, now_ts, days)
        result[f"start_{days}d_eur"] = start["close"] if start else None
        result[f"start_{days}d_at_utc"] = (
            datetime.fromtimestamp(start["ts"] + 86400, timezone.utc).isoformat() if start else None
        )
        result[f"return_{days}d_pct"] = _pct(start["close"], last) if start else None
    return result


def _git_paths(prefix: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", prefix],
        cwd=ROOT,
        text=True,
    )
    return [x.strip() for x in out.splitlines() if x.strip().endswith(".json.gz")]


def _path_ts(path: str) -> float | None:
    name = Path(path).name
    stamp = name.split("-", 1)[0]
    try:
        return datetime.strptime(stamp, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()
    except ValueError:
        return None


def _sample_paths(paths: list[str], seconds: int = SAMPLE_SECONDS) -> list[str]:
    # Keep the last journal within each sampling bucket.
    buckets: dict[int, tuple[float, str]] = {}
    for path in sorted(paths):
        ts = _path_ts(path)
        if ts is None:
            continue
        key = int(ts // seconds)
        prev = buckets.get(key)
        if prev is None or ts > prev[0]:
            buckets[key] = (ts, path)
    return [buckets[k][1] for k in sorted(buckets)]


def _git_json_gz(path: str) -> dict[str, Any]:
    raw = subprocess.check_output(["git", "show", "HEAD:" + path], cwd=ROOT)
    value = json.loads(gzip.decompress(raw).decode("utf-8"))
    return value if isinstance(value, dict) else {}


def _event(ts: float, path: str, price: Any, **extra: Any) -> dict[str, Any]:
    return {
        "ts": ts,
        "at_utc": datetime.fromtimestamp(ts, timezone.utc).isoformat(),
        "path": path,
        "price_eur": finite(price),
        **extra,
    }


def _first(slot: dict[str, Any], key: str, event: dict[str, Any]) -> None:
    if slot.get(key) is None:
        slot[key] = event


def _scan_history(cohort: set[str]) -> tuple[dict[str, Any], dict[str, Any]]:
    states = {
        m: {
            "first_observed": None,
            "first_v4_watch": None,
            "first_v4_entry": None,
            "first_v4_buy_ready": None,
            "first_acceleration": None,
            "first_confirmed_acceleration": None,
            "first_pipeline_buy": None,
            "eligibility_flips": 0,
            "eligible_hours": 0,
            "observed_hours": 0,
            "_last_eligible": None,
        }
        for m in cohort
    }

    paths_all = _git_paths("history")
    paths = _sample_paths(paths_all)
    first_ts = None
    last_ts = None
    read_errors = []

    for path in paths:
        ts = _path_ts(path)
        if ts is None:
            continue
        first_ts = ts if first_ts is None else min(first_ts, ts)
        last_ts = ts if last_ts is None else max(last_ts, ts)
        try:
            doc = _git_json_gz(path)
        except Exception as exc:
            read_errors.append({"path": path, "error": type(exc).__name__ + ":" + str(exc)})
            continue

        for obs in doc.get("observations") or []:
            if not isinstance(obs, dict):
                continue
            market = obs.get("market")
            if market not in cohort:
                continue
            s = states[market]
            price = finite(obs.get("price_eur"))
            baseline = obs.get("baseline") or {}
            action_status = str(baseline.get("action_status") or "UNOBSERVED")
            buy_ready = bool(baseline.get("buy_ready"))
            acceleration = obs.get("acceleration") or {}
            accel_state = str(acceleration.get("state") or "NO_ACCELERATION")
            decision = str(obs.get("decision") or "")

            s["observed_hours"] += 1
            _first(s, "first_observed", _event(ts, path, price))

            if action_status in V4_WATCH_STATES:
                _first(
                    s,
                    "first_v4_watch",
                    _event(
                        ts,
                        path,
                        price,
                        action_status=action_status,
                        opportunity_score=finite(baseline.get("opportunity_score")),
                    ),
                )
            if action_status in V4_ENTRY_STATES:
                _first(
                    s,
                    "first_v4_entry",
                    _event(
                        ts,
                        path,
                        price,
                        action_status=action_status,
                        opportunity_score=finite(baseline.get("opportunity_score")),
                    ),
                )
            if buy_ready:
                _first(
                    s,
                    "first_v4_buy_ready",
                    _event(
                        ts,
                        path,
                        price,
                        action_status=action_status,
                        opportunity_score=finite(baseline.get("opportunity_score")),
                    ),
                )
            if accel_state in ACCEL_STATES:
                _first(
                    s,
                    "first_acceleration",
                    _event(
                        ts,
                        path,
                        price,
                        acceleration_state=accel_state,
                        acceleration_score=finite(acceleration.get("score")),
                    ),
                )
            if accel_state == "CONFIRMED_ACCELERATION":
                _first(
                    s,
                    "first_confirmed_acceleration",
                    _event(
                        ts,
                        path,
                        price,
                        acceleration_state=accel_state,
                        acceleration_score=finite(acceleration.get("score")),
                    ),
                )
            if decision == "ACHÈTE":
                _first(
                    s,
                    "first_pipeline_buy",
                    _event(ts, path, price, decision=decision),
                )

            eligible = (
                action_status in V4_WATCH_STATES
                or accel_state in ACCEL_STATES
                or decision == "ACHÈTE"
            )
            if eligible:
                s["eligible_hours"] += 1
            if s["_last_eligible"] is not None and eligible != s["_last_eligible"]:
                s["eligibility_flips"] += 1
            s["_last_eligible"] = eligible

    for s in states.values():
        s.pop("_last_eligible", None)

    meta = {
        "all_journal_files": len(paths_all),
        "sampled_files": len(paths),
        "sampling_seconds": SAMPLE_SECONDS,
        "first_sample_at_utc": datetime.fromtimestamp(first_ts, timezone.utc).isoformat() if first_ts else None,
        "last_sample_at_utc": datetime.fromtimestamp(last_ts, timezone.utc).isoformat() if last_ts else None,
        "read_error_count": len(read_errors),
        "read_errors": read_errors[:20],
    }
    return states, meta


def _scan_decision_history(cohort: set[str]) -> tuple[dict[str, Any], dict[str, Any]]:
    states = {
        m: {
            "first_dl_actionable": None,
            "first_dl_buy_now": None,
            "dl_action_flips": 0,
            "observed_hours": 0,
            "_last_action": None,
        }
        for m in cohort
    }

    paths_all = _git_paths("decision_history")
    paths = _sample_paths(paths_all)
    first_ts = None
    last_ts = None
    read_errors = []

    for path in paths:
        ts = _path_ts(path)
        if ts is None:
            continue
        first_ts = ts if first_ts is None else min(first_ts, ts)
        last_ts = ts if last_ts is None else max(last_ts, ts)
        try:
            doc = _git_json_gz(path)
        except Exception as exc:
            read_errors.append({"path": path, "error": type(exc).__name__ + ":" + str(exc)})
            continue

        by_market = {
            str(row.get("market")): row
            for row in (doc.get("ranked") or [])
            if isinstance(row, dict) and row.get("market") in cohort
        }
        for market, row in by_market.items():
            s = states[market]
            action = str(row.get("action") or "NONE")
            bucket = row.get("bucket")
            price = finite(row.get("price_eur"))
            s["observed_hours"] += 1

            if bucket is not None and action not in {"WATCH", "VETO_STRUCTUREL"}:
                _first(
                    s,
                    "first_dl_actionable",
                    _event(
                        ts,
                        path,
                        price,
                        action=action,
                        bucket=bucket,
                        rank_score=finite(row.get("rank_score")),
                    ),
                )
            if action == "ACHETE_MAINTENANT":
                _first(
                    s,
                    "first_dl_buy_now",
                    _event(
                        ts,
                        path,
                        price,
                        action=action,
                        bucket=bucket,
                        rank_score=finite(row.get("rank_score")),
                    ),
                )

            if s["_last_action"] is not None and action != s["_last_action"]:
                s["dl_action_flips"] += 1
            s["_last_action"] = action

    for s in states.values():
        s.pop("_last_action", None)

    meta = {
        "all_journal_files": len(paths_all),
        "sampled_files": len(paths),
        "sampling_seconds": SAMPLE_SECONDS,
        "first_sample_at_utc": datetime.fromtimestamp(first_ts, timezone.utc).isoformat() if first_ts else None,
        "last_sample_at_utc": datetime.fromtimestamp(last_ts, timezone.utc).isoformat() if last_ts else None,
        "read_error_count": len(read_errors),
        "read_errors": read_errors[:20],
    }
    return states, meta


def _annotate_event(event: dict[str, Any] | None, market_row: dict[str, Any], now_ts: float) -> dict[str, Any] | None:
    if not event:
        return None
    out = dict(event)
    start = finite(market_row.get("start_30d_eur"))
    end = finite(market_row.get("last_eur"))
    price = finite(out.get("price_eur"))
    total = _pct(start, end)
    move_to_event = _pct(start, price)
    if total is not None and total > 0 and move_to_event is not None:
        out["move_consumed_pct_of_30d_gain"] = 100.0 * move_to_event / total
    else:
        out["move_consumed_pct_of_30d_gain"] = None
    out["remaining_to_endpoint_pct"] = _pct(price, end)
    out["hours_before_endpoint"] = (now_ts - out["ts"]) / 3600.0
    return out


def _threshold_counts(rows: list[dict[str, Any]], horizon: int) -> dict[str, int]:
    vals = [finite(r.get(f"return_{horizon}d_pct")) for r in rows]
    vals = [v for v in vals if v is not None]
    return {
        "measured": len(vals),
        **{f"gte_{t}_pct": sum(v >= t for v in vals) for t in THRESHOLDS},
        "positive": sum(v > 0 for v in vals),
        "negative": sum(v < 0 for v in vals),
    }


def _coverage(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    eligible = [r for r in rows if finite(r.get("return_30d_pct")) is not None and finite(r.get("return_30d_pct")) >= 30]
    events = [r.get(key) for r in eligible if r.get(key)]
    remaining = [finite(e.get("remaining_to_endpoint_pct")) for e in events]
    consumed = [finite(e.get("move_consumed_pct_of_30d_gain")) for e in events]
    return {
        "winner_count_gte_30pct": len(eligible),
        "event_count": len(events),
        "coverage_pct": (100.0 * len(events) / len(eligible)) if eligible else None,
        "with_at_least_10pct_remaining": sum(v is not None and v >= 10 for v in remaining),
        "with_at_least_20pct_remaining": sum(v is not None and v >= 20 for v in remaining),
        "median_remaining_pct": _median(remaining),
        "median_move_consumed_pct": _median(consumed),
        "detected_before_half_move": sum(v is not None and v <= 50 for v in consumed),
    }


def build() -> dict[str, Any]:
    client = PublicClient(timeout=12, retries=3, requests_per_second=8)
    now = time.time()
    client.get("/time", cache=False)
    markets_raw = client.get("/markets", cache=False)
    tickers = {
        str(r.get("market")): r
        for r in client.get("/ticker/24h", cache=False)
        if isinstance(r, dict) and r.get("market")
    }
    markets = sorted(
        m["market"]
        for m in markets_raw
        if m.get("quote") == "EUR" and m.get("status") == "trading" and m.get("market")
    )

    market_rows = []
    errors = []

    def one(market: str) -> dict[str, Any]:
        last = finite((tickers.get(market) or {}).get("last"))
        if last is None:
            raise RuntimeError("missing_last")
        return _market_returns(client, market, last, now)

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(one, market): market for market in markets}
        for future in as_completed(futures):
            market = futures[future]
            try:
                market_rows.append(future.result())
            except Exception as exc:
                errors.append({"market": market, "error": type(exc).__name__ + ":" + str(exc)})

    market_rows.sort(key=lambda r: r["market"])
    top30 = sorted(
        [r for r in market_rows if finite(r.get("return_30d_pct")) is not None],
        key=lambda r: finite(r.get("return_30d_pct"), -1e9),
        reverse=True,
    )

    # Audit all >=20% 30d winners, at least the top 80, plus the named user cases.
    cohort = {
        r["market"]
        for r in top30
        if finite(r.get("return_30d_pct")) is not None and finite(r.get("return_30d_pct")) >= 20
    }
    cohort.update(r["market"] for r in top30[:80])
    cohort.update(m for m in USER_CASES if m in set(markets))

    hist, hist_meta = _scan_history(cohort)
    dl, dl_meta = _scan_decision_history(cohort)
    by_market = {r["market"]: r for r in market_rows}

    cohort_rows = []
    for market in sorted(cohort):
        base = by_market.get(market)
        if not base:
            continue
        row = dict(base)
        hs = hist.get(market) or {}
        ds = dl.get(market) or {}
        for key in (
            "first_v4_watch",
            "first_v4_entry",
            "first_v4_buy_ready",
            "first_acceleration",
            "first_confirmed_acceleration",
            "first_pipeline_buy",
        ):
            row[key] = _annotate_event(hs.get(key), row, now)
        for key in ("first_dl_actionable", "first_dl_buy_now"):
            row[key] = _annotate_event(ds.get(key), row, now)
        row["eligibility_flips"] = hs.get("eligibility_flips", 0)
        row["eligible_hours"] = hs.get("eligible_hours", 0)
        row["history_observed_hours"] = hs.get("observed_hours", 0)
        row["dl_action_flips"] = ds.get("dl_action_flips", 0)
        row["dl_observed_hours"] = ds.get("observed_hours", 0)
        row["user_case"] = market in USER_CASES
        cohort_rows.append(row)

    winners30 = [r for r in cohort_rows if finite(r.get("return_30d_pct")) is not None and finite(r.get("return_30d_pct")) >= 30]

    payload = {
        "schema": "solaire_human_swing_audit_v1",
        "generated_at_utc": utc(),
        "measurement_only": True,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
        "objective": "Evaluate Solaire for human-actionable 24h-7d swing selection rather than 5m scalping.",
        "active_eur_markets": len(markets),
        "market_return_rows": len(market_rows),
        "market_return_errors": errors,
        "http_diagnostics": client.diagnostics(),
        "threshold_counts": {str(h): _threshold_counts(market_rows, h) for h in HORIZONS},
        "history_sampling": hist_meta,
        "decision_history_sampling": dl_meta,
        "cohort_rule": "all >=20% 30d winners + top 80 30d + named user cases",
        "cohort_count": len(cohort_rows),
        "winner_30d_gte_30_count": len(winners30),
        "coverage": {
            "first_v4_watch": _coverage(cohort_rows, "first_v4_watch"),
            "first_v4_buy_ready": _coverage(cohort_rows, "first_v4_buy_ready"),
            "first_acceleration": _coverage(cohort_rows, "first_acceleration"),
            "first_confirmed_acceleration": _coverage(cohort_rows, "first_confirmed_acceleration"),
            "first_pipeline_buy": _coverage(cohort_rows, "first_pipeline_buy"),
            "first_dl_actionable": _coverage(cohort_rows, "first_dl_actionable"),
            "first_dl_buy_now": _coverage(cohort_rows, "first_dl_buy_now"),
        },
        "churn": {
            "median_eligibility_flips_gte30_winners": _median([r.get("eligibility_flips") for r in winners30]),
            "median_dl_action_flips_gte30_winners": _median([r.get("dl_action_flips") for r in winners30]),
            "gte30_winners_with_4plus_eligibility_flips": sum((r.get("eligibility_flips") or 0) >= 4 for r in winners30),
            "gte30_winners_with_10plus_eligibility_flips": sum((r.get("eligibility_flips") or 0) >= 10 for r in winners30),
        },
        "top_30d": top30[:100],
        "cohort": sorted(cohort_rows, key=lambda r: finite(r.get("return_30d_pct"), -1e9), reverse=True),
    }
    return payload


def render(payload: dict[str, Any]) -> str:
    lines = [
        "# Solaire Human / Swing audit",
        "",
        f"Generated: {payload['generated_at_utc']}",
        f"Active EUR markets: {payload['active_eur_markets']}",
        "Measurement only. No production behavior was changed.",
        "",
        "## Full-universe returns",
        "",
        "| Horizon | Measured | Positive | >=10% | >=20% | >=30% | >=50% | >=100% |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for h in HORIZONS:
        c = payload["threshold_counts"][str(h)]
        lines.append(
            f"| {h}d | {c['measured']} | {c['positive']} | {c['gte_10_pct']} | {c['gte_20_pct']} | "
            f"{c['gte_30_pct']} | {c['gte_50_pct']} | {c['gte_100_pct']} |"
        )

    lines.extend([
        "",
        "## Existing Solaire coverage of >=30% 30d winners",
        "",
        "| Milestone | Coverage | >=10% remaining | >=20% remaining | Median remaining | Median move consumed |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    labels = [
        ("first_v4_watch", "First V4 WATCH+"),
        ("first_v4_buy_ready", "First V4 BUY_READY"),
        ("first_acceleration", "First acceleration"),
        ("first_confirmed_acceleration", "First CONFIRMED acceleration"),
        ("first_pipeline_buy", "First pipeline ACHETE"),
        ("first_dl_actionable", "First Decision Layer actionable"),
        ("first_dl_buy_now", "First Decision Layer ACHETE_MAINTENANT"),
    ]
    for key, label in labels:
        c = payload["coverage"][key]
        lines.append(
            f"| {label} | {_fmt(c.get('coverage_pct'))}% ({c['event_count']}/{c['winner_count_gte_30pct']}) | "
            f"{c['with_at_least_10pct_remaining']} | {c['with_at_least_20pct_remaining']} | "
            f"{_fmt(c.get('median_remaining_pct'))}% | {_fmt(c.get('median_move_consumed_pct'))}% |"
        )

    churn = payload["churn"]
    lines.extend([
        "",
        "## Churn",
        "",
        f"- Median eligible/ineligible flips among >=30% winners: {_fmt(churn.get('median_eligibility_flips_gte30_winners'), 1)}.",
        f"- >=30% winners with at least 4 flips: {churn.get('gte30_winners_with_4plus_eligibility_flips')}.",
        f"- >=30% winners with at least 10 flips: {churn.get('gte30_winners_with_10plus_eligibility_flips')}.",
        f"- Median Decision Layer action flips among >=30% winners: {_fmt(churn.get('median_dl_action_flips_gte30_winners'), 1)}.",
        "",
        "## Top 30d performers",
        "",
        "| Market | 7d | 14d | 30d | First WATCH remaining | First DL BUY remaining | Flips |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    for row in payload["cohort"][:60]:
        fw = row.get("first_v4_watch") or {}
        fb = row.get("first_dl_buy_now") or {}
        lines.append(
            f"| {row['market']} | {_fmt(row.get('return_7d_pct'))}% | {_fmt(row.get('return_14d_pct'))}% | "
            f"{_fmt(row.get('return_30d_pct'))}% | {_fmt(fw.get('remaining_to_endpoint_pct'))}% | "
            f"{_fmt(fb.get('remaining_to_endpoint_pct'))}% | {row.get('eligibility_flips', 0)} |"
        )

    lines.extend([
        "",
        "## Named user cases",
        "",
        "| Market | 30d | First WATCH consumed | First WATCH remaining | First DL BUY remaining | Flips |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    named = [r for r in payload["cohort"] if r.get("user_case")]
    named.sort(key=lambda r: finite(r.get("return_30d_pct"), -1e9), reverse=True)
    for row in named:
        fw = row.get("first_v4_watch") or {}
        fb = row.get("first_dl_buy_now") or {}
        lines.append(
            f"| {row['market']} | {_fmt(row.get('return_30d_pct'))}% | "
            f"{_fmt(fw.get('move_consumed_pct_of_30d_gain'))}% | {_fmt(fw.get('remaining_to_endpoint_pct'))}% | "
            f"{_fmt(fb.get('remaining_to_endpoint_pct'))}% | {row.get('eligibility_flips', 0)} |"
        )

    hs = payload["history_sampling"]
    ds = payload["decision_history_sampling"]
    lines.extend([
        "",
        "## Interpretation limits",
        "",
        f"- Historical Solaire journals are sampled hourly for this human-workflow audit: {hs['sampled_files']} samples from {hs['all_journal_files']} files.",
        f"- Decision Layer journals are sampled hourly: {ds['sampled_files']} samples from {ds['all_journal_files']} files.",
        f"- Solaire journal coverage begins at {hs.get('first_sample_at_utc')}; a 30d market move may therefore start before Solaire history exists.",
        "- Remaining upside and move-consumed metrics are ex-post diagnostics. They are not used as trading inputs.",
        "- A missed hourly state does not prove Solaire never emitted a shorter-lived intrahour signal. For a human workflow, that short-lived signal is intentionally not treated as sufficient evidence.",
        "- This report evaluates whether the existing system produces durable, human-actionable opportunities; it does not optimize thresholds.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    payload = build()
    atomic_json(OUT_JSON, payload)
    Path(OUT_MD).write_text(render(payload), encoding="utf-8")
    print(json.dumps({
        "active_eur_markets": payload["active_eur_markets"],
        "threshold_counts": payload["threshold_counts"],
        "coverage": payload["coverage"],
        "churn": payload["churn"],
        "history_sampling": payload["history_sampling"],
        "decision_history_sampling": payload["decision_history_sampling"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
