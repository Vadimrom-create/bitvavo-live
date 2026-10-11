#!/usr/bin/env python3
"""Research-only, time-bounded public 5m price paths for matured machine BUYs.

Not a backtest of executable trades: there is no proof of an actual fill, future
order-book bid, realizable take profit, fees, or ChatGPT decision.
Never changes production state, buys, alerts, or private account data.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import finite
from research.production_journal import evaluate_closed_5m_path
from research.http import PublicClient

HORIZONS = (24, 48, 72)
FIVE_MIN_MS = 300_000
MAX_CANDLES = 1440  # documented public API maximum; 72h is < 864 bars
SCHEMA = "solaire_research_24_48_72_price_path_v1"


def iso(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat()


def validate_source(doc, asof):
    if not isinstance(doc, dict) or doc.get("schema") != "solaire_prospective_journal_v1":
        raise ValueError("unsupported machine journal")
    rows = doc.get("entries")
    if not isinstance(rows, list):
        raise ValueError("missing entries")
    result, seen = [], set()
    for e in rows:
        if not isinstance(e, dict) or e.get("decision_type") != "BUY_SENT":
            continue
        uid = e.get("decision_id")
        market = e.get("market")
        stamp = finite(e.get("decision_ts"))
        entry = finite(e.get("entry_eur"))
        if (not isinstance(uid, str) or not uid or uid in seen
                or not isinstance(market, str) or not market.endswith("-EUR")
                or stamp is None or stamp <= 0 or stamp > asof
                or entry is None or entry <= 0):
            continue
        seen.add(uid)
        result.append({
            "decision_id": uid, "signal_id": e.get("signal_id"), "market": market,
            "decision_ts": stamp, "entry_eur": entry,
            "stop_eur": finite(e.get("stop_eur")),
            "tp1_eur": finite(e.get("tp1_eur")),
        })
    return sorted(result, key=lambda x: (x["decision_ts"], x["decision_id"]), reverse=True)


def choose_due(rows, now, max_per_horizon):
    selected = []
    for horizon in HORIZONS:
        due = [r for r in rows
               if now >= r["decision_ts"] + horizon * 3600 + 300]
        # Most recently matured episodes, never cherry-pick positive outcomes.
        for r in due[:max_per_horizon]:
            selected.append({**r, "horizon_hours": horizon})
    return selected


def bounds(decision_ts, horizon_hours, now):
    first_ms = ((int(decision_ts * 1000) // FIVE_MIN_MS) + 1) * FIVE_MIN_MS
    end_ms = int((decision_ts + horizon_hours * 3600) * 1000)
    last_ms = ((end_ms - FIVE_MIN_MS) // FIVE_MIN_MS) * FIVE_MIN_MS
    request_end = last_ms + FIVE_MIN_MS
    if last_ms < first_ms or request_end > int(now * 1000):
        raise ValueError("unsafe/unmatured candle range")
    count = (last_ms - first_ms) // FIVE_MIN_MS + 1
    if count > MAX_CANDLES:
        raise ValueError("requested interval exceeds Bitvavo candle limit")
    # Public docs: start aligns to candle START and end to candle END.
    return {"start": first_ms, "end": request_end, "expected_bars": count}


def inspect_one(item, client, asof, *, observed_at=None):
    market, horizon = item["market"], item["horizon_hours"]
    b = bounds(item["decision_ts"], horizon, asof)
    params = {
        "interval": "5m",
        "start": b["start"],
        "end": b["end"],
        "limit": MAX_CANDLES,
    }
    stub = {
        "decision_id": item["decision_id"],
        "signal_id": item.get("signal_id"),
        "market": market,
        "decision_at_utc": iso(item["decision_ts"]),
        "horizon_hours": horizon,
        "due_at_utc": iso(item["decision_ts"] + horizon * 3600),
        "baseline_plan_entry_eur": item["entry_eur"],
        "request": params,
        "price_source": "BITVAVO_PUBLIC_HISTORICAL_5M",
        "actual_fill_proven": False,
        "entry_executable_proven": False,
        "future_exit_executable_proven": False,
        "net_pnl_eur": None,
        "chatgpt_decision_joined": False,
    }
    try:
        bars = client.get("/" + market + "/candles", params, cache=False)
        if not isinstance(bars, list):
            raise ValueError("expected array of 5m candles")
        # Never allow results beyond requested interval or evaluation cutoff.
        valid = []
        for bar in bars:
            if not isinstance(bar, list) or len(bar) < 6:
                continue
            ts = finite(bar[0])
            if ts is None or not b["start"] <= ts < b["end"] or ts % FIVE_MIN_MS:
                continue
            valid.append(bar)
        path = evaluate_closed_5m_path(
            valid, item["decision_ts"], item["entry_eur"], horizon,
            stop_eur=item.get("stop_eur"), tp1_eur=item.get("tp1_eur"),
            fill_no_trade_gaps=False,
        )
        record_time = time.time() if observed_at is None else observed_at
        return {
            **stub,
            "snapshot_collected_at_utc": iso(record_time),
            "status": path.get("status"),
            "reason": path.get("reason"),
            "observed_bars": len(valid),
            "expected_bars": b["expected_bars"],
            "source_coverage_pct": round(100 * len(valid) / b["expected_bars"], 2),
            "strict_complete": path.get("status") == "COMPLETE",
            "path_result": path.get("result") if path.get("status") == "COMPLETE" else None,
            "reference_mfe_pct": path.get("mfe_pct") if path.get("status") == "COMPLETE" else None,
            "reference_mae_pct": path.get("mae_pct") if path.get("status") == "COMPLETE" else None,
            "reference_close_return_pct": path.get("close_return_pct") if path.get("status") == "COMPLETE" else None,
            "path_event_start_ms": path.get("path_event_start_ms") if path.get("status") == "COMPLETE" else None,
            "path_policy": path.get("path_policy"),
            "interpretation": "PRICE_REFERENCE_ONLY_NOT_A_TRADE",
        }
    except (RuntimeError, ValueError, KeyError, TypeError) as exc:
        return {**stub, "status": "SOURCE_ERROR", "reason": type(exc).__name__,
                "strict_complete": False, "reference_close_return_pct": None,
                "interpretation": "UNKNOWN_NOT_ZERO"}


def inspect(rows, now, client, max_per_horizon):
    selected = choose_due(validate_source(rows, now), now, max_per_horizon)
    results = [inspect_one(x, client, now) for x in selected]
    by_horizon = {}
    for h in HORIZONS:
        part = [r for r in results if r["horizon_hours"] == h]
        counts = Counter(r["status"] for r in part)
        by_horizon[str(h)] = {
            "selected": len(part),
            "strict_complete": counts.get("COMPLETE", 0),
            "incomplete": counts.get("INCOMPLETE", 0),
            "source_errors": counts.get("SOURCE_ERROR", 0),
            "other_unknown": len(part) - sum(counts.get(s, 0) for s in ("COMPLETE", "INCOMPLETE", "SOURCE_ERROR")),
            "executed_trades_proven": 0,
        }
    return {
        "schema": SCHEMA,
        "collected_at_utc": iso(time.time()),
        "selection": "MOST_RECENT_MATURED_FIRST_BY_TIMESTAMP_PER_HORIZON",
        "limit_per_horizon": max_per_horizon,
        "source": "production_direct_decision_journal.json; Bitvavo PUBLIC /candles",
        "horizons": by_horizon,
        "observations": results,
        "limitations": [
            "Historical 5m candles are PUBLIC LAST TRADE data, NOT bid/ask fills.",
            "A positive reference move or MFE does not establish an executable profit.",
            "No sparse-gap interpolation: missing 5m bars are INCOMPLETE, not zero losses.",
            "No conversion of signals into actual trades; no private wallet access.",
            "Selection excludes unmatured events and uses only timestamp order.",
            "This is not matched independent ChatGPT abstention or portfolio evidence.",
        ],
        "affects_production": False,
        "orders_sent": False,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, help="public direct journal")
    p.add_argument("--output", help="research artifact path")
    p.add_argument("--max-per-horizon", type=int, default=5)
    p.add_argument("--asof", help="UTC ISO; default current time")
    a = p.parse_args(argv)
    try:
        if not 1 <= a.max_per_horizon <= 30:
            raise ValueError("max-per-horizon must be 1..30")
        if a.asof:
            at = datetime.fromisoformat(a.asof.replace("Z", "+00:00"))
            if at.tzinfo is None or at.utcoffset().total_seconds() != 0:
                raise ValueError("--asof must be UTC")
            now = at.timestamp()
            if now > time.time() + 120:
                raise ValueError("--asof in future")
        else:
            now = time.time()
        source = json.loads(Path(a.source).read_text(encoding="utf-8"))
        client = PublicClient(timeout=10, retries=1, requests_per_second=4)
        report = inspect(source, now, client, a.max_per_horizon)
        payload = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if a.output:
            Path(a.output).parent.mkdir(parents=True, exist_ok=True)
            Path(a.output).write_text(payload, encoding="utf-8")
        # Avoid flooding CI logs with detailed episode paths.
        print(json.dumps({k: report[k] for k in ("schema", "collected_at_utc", "horizons",
                                                 "affects_production", "orders_sent")},
                         ensure_ascii=False, sort_keys=True))
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"PUBLIC_PRICE_PATH_RESEARCH_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
