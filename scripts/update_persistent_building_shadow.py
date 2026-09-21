#!/usr/bin/env python3
"""Update shadow persistent-BUILDING state and prospective outcomes."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.persistent_building import update_shadow

PAYLOAD = "production_alert_candidates.json"
STATE = "production_persistent_building_state.json"
JOURNAL = "production_persistent_building_journal.json"
STATUS = "production_persistent_building_status.json"
HORIZONS = (4, 12, 24)


def due_horizons(event: dict, now: float) -> list[int]:
    detected = finite(event.get("detected_ts"))
    if detected is None:
        return []
    evaluations = event.setdefault("evaluations", {})
    return [
        hours
        for hours in HORIZONS
        if str(hours) not in evaluations and now >= detected + hours * 3600
    ]


def evaluate_event(event: dict, raw: list, horizon_hours: int) -> dict | None:
    detected = finite(event.get("detected_ts"))
    baseline = finite(event.get("baseline_price_eur"))
    if detected is None or baseline is None or baseline <= 0:
        return None

    first_full_start = ((int(detected * 1000) // 300_000) + 1) * 300_000
    end_ms = int((detected + horizon_hours * 3600) * 1000)
    bars = []
    for row in raw:
        if not isinstance(row, list) or len(row) < 6:
            continue
        ts = finite(row[0])
        high = finite(row[2])
        low = finite(row[3])
        close = finite(row[4])
        if None in (ts, high, low, close):
            continue
        if first_full_start <= ts < end_ms:
            bars.append((int(ts), high, low, close))
    if not bars:
        return None

    high = max(x[1] for x in bars)
    low = min(x[2] for x in bars)
    close = bars[-1][3]
    mfe = (high / baseline - 1.0) * 100.0
    mae = (low / baseline - 1.0) * 100.0
    close_return = (close / baseline - 1.0) * 100.0
    return {
        "horizon_hours": horizon_hours,
        "mfe_pct": round(mfe, 4),
        "mae_pct": round(mae, 4),
        "close_return_pct": round(close_return, 4),
        "mfe_ge_5pct": mfe >= 5.0,
        "mfe_ge_10pct": mfe >= 10.0,
        "bars_used": len(bars),
        "method": "closed_5m_bars_after_shadow_detection",
    }


def main() -> int:
    now = time.time()
    payload = read_json(PAYLOAD, {})
    state, journal, status = update_shadow(
        payload,
        read_json(STATE, {}),
        read_json(JOURNAL, {}),
    )
    status.update(
        checked_at_utc=utc(now),
        evaluated_horizons=0,
        evaluation_errors=[],
    )

    due = {}
    for idx, event in enumerate(journal.get("events", [])):
        horizons = due_horizons(event, now)
        if horizons:
            due[idx] = horizons

    if due:
        try:
            client = PublicClient(timeout=10, retries=2, requests_per_second=8)
            client.get("/time", cache=False)
            markets = sorted(
                {
                    journal["events"][idx].get("market")
                    for idx in due
                    if journal["events"][idx].get("market")
                }
            )
            candles = {}
            for market in markets:
                try:
                    candles[market] = client.get(
                        "/" + market + "/candles",
                        {"interval": "5m", "limit": 400},
                        cache=False,
                    )
                except (RuntimeError, ValueError, KeyError) as exc:
                    status["evaluation_errors"].append(
                        {"market": market, "reason": type(exc).__name__ + ":" + str(exc)}
                    )

            for idx, horizons in due.items():
                event = journal["events"][idx]
                raw = candles.get(event.get("market"))
                if not raw:
                    continue
                for hours in horizons:
                    result = evaluate_event(event, raw, hours)
                    if result is not None:
                        event.setdefault("evaluations", {})[str(hours)] = result
                        status["evaluated_horizons"] += 1

            if status["evaluation_errors"]:
                status["status"] = "DEGRADED_NONBLOCKING"
        except (RuntimeError, ValueError, KeyError) as exc:
            status["status"] = "DEGRADED_NONBLOCKING"
            status["evaluation_errors"].append(
                {"reason": type(exc).__name__ + ":" + str(exc)}
            )

    journal["updated_at_utc"] = utc(now)
    atomic_json(STATE, state)
    atomic_json(JOURNAL, journal)
    atomic_json(STATUS, status)
    print("SOLAIRE_PERSISTENT_BUILDING " + json.dumps(status, ensure_ascii=False))
    # Shadow measurement must never break production.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
