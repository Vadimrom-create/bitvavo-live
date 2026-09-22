"""Prospective Solaire decision journal helpers.

The journal records what production actually considered/sent, then later adds
objective 4h/12h/24h outcomes. It never participates in detection or BUY gating.
"""
from __future__ import annotations

import copy
from datetime import datetime
from typing import Any

from research.common import finite

HORIZONS_HOURS = (4, 12, 24)
MAX_ENTRIES = 4000


def _ts(value: Any) -> float | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def _entry_key(entry: dict[str, Any]) -> str:
    return "|".join(
        [
            str(entry.get("cycle_id", "")),
            str(entry.get("market", "")),
            str(entry.get("decision_type", "")),
            str(entry.get("reason", "")),
        ]
    )


def record_cycle(
    payload: dict[str, Any],
    alert_status: dict[str, Any],
    journal: dict[str, Any] | None,
) -> dict[str, Any]:
    journal = copy.deepcopy(journal or {})
    journal.setdefault("schema", "solaire_prospective_journal_v1")
    journal.setdefault("entries", [])
    cycle_id = str(payload.get("generated_at_utc") or "")
    cycle_ts = _ts(cycle_id)
    alert_ts = _ts(alert_status.get("checked_at_utc"))
    if not cycle_id or cycle_ts is None or alert_ts is None or abs(alert_ts - cycle_ts) > 20 * 60:
        return journal

    existing = {_entry_key(entry) for entry in journal["entries"]}
    watch = {
        row.get("market"): row
        for row in payload.get("watch", [])
        if isinstance(row, dict) and row.get("market")
    }

    def add(market: str, decision_type: str, reason: str, extra: dict[str, Any] | None = None):
        row = watch.get(market) or {}
        entry = {
            "cycle_id": cycle_id,
            "decision_ts": alert_ts,
            "market": market,
            "decision_type": decision_type,
            "reason": reason,
            "signal_price_eur": finite(row.get("last")),
            "signal_score": finite(row.get("signal_score")),
            "signal_phase": row.get("signal_phase"),
            "episode_extension_pct": finite(row.get("episode_extension_pct")),
            "context": copy.deepcopy(row.get("context") or {}),
            "evaluations": {},
        }
        if extra:
            entry.update(extra)
        key = _entry_key(entry)
        if key not in existing:
            journal["entries"].append(entry)
            existing.add(key)

    for rejected in alert_status.get("rejections", []) or []:
        if not isinstance(rejected, dict) or not rejected.get("market"):
            continue
        add(
            rejected["market"],
            "REJECTED",
            str(rejected.get("reason") or "UNKNOWN"),
        )

    if alert_status.get("email") == "DELIVERY_COMPLETED":
        deliveries = alert_status.get("deliveries")
        if not isinstance(deliveries, list) or not deliveries:
            deliveries = [alert_status] if alert_status.get("market") else []
        for delivered in deliveries:
            if not isinstance(delivered, dict) or not delivered.get("market"):
                continue
            add(
                delivered["market"],
                "BUY_SENT",
                "DELIVERED",
                {
                    "entry_eur": finite(delivered.get("entry_eur")),
                    "stop_eur": finite(delivered.get("stop_eur")),
                    "tp1_eur": finite(delivered.get("tp1_eur")),
                    "tp2_eur": finite(delivered.get("tp2_eur")),
                    "stake_eur": finite(delivered.get("stake_eur")),
                    "structural_range_15m_pct": finite(
                        delivered.get("structural_range_15m_pct")
                    ),
                    "stop_distance_pct": finite(delivered.get("stop_distance_pct")),
                },
            )

    journal["entries"] = journal["entries"][-MAX_ENTRIES:]
    journal["updated_at_ts"] = alert_ts
    return journal


def due_horizons(entry: dict[str, Any], now: float) -> list[int]:
    decision_ts = finite(entry.get("decision_ts"))
    if decision_ts is None:
        return []
    evaluations = entry.setdefault("evaluations", {})
    return [
        hours
        for hours in HORIZONS_HOURS
        if str(hours) not in evaluations and now >= decision_ts + hours * 3600
    ]


def evaluate_bars(
    entry: dict[str, Any],
    raw_bars: list[list[Any]],
    horizon_hours: int,
) -> dict[str, Any] | None:
    decision_ts = finite(entry.get("decision_ts"))
    baseline = finite(entry.get("entry_eur"))
    if baseline is None:
        baseline = finite(entry.get("signal_price_eur"))
    if decision_ts is None or baseline is None or baseline <= 0:
        return None

    # Use only complete bars that start after the decision-containing 5m bar.
    first_full_start = ((int(decision_ts * 1000) // 300_000) + 1) * 300_000
    end_ms = int((decision_ts + horizon_hours * 3600) * 1000)
    bars = []
    for row in raw_bars:
        if not isinstance(row, list) or len(row) < 6:
            continue
        t = finite(row[0])
        high = finite(row[2])
        low = finite(row[3])
        close = finite(row[4])
        if None in (t, high, low, close):
            continue
        if first_full_start <= t < end_ms:
            bars.append((int(t), high, low, close))
    if not bars:
        return None

    high = max(row[1] for row in bars)
    low = min(row[2] for row in bars)
    close = bars[-1][3]
    mfe = (high / baseline - 1) * 100
    mae = (low / baseline - 1) * 100
    close_return = (close / baseline - 1) * 100

    result = "OBSERVED"
    if entry.get("decision_type") == "BUY_SENT":
        stop = finite(entry.get("stop_eur"))
        tp1 = finite(entry.get("tp1_eur"))
        if stop is not None and tp1 is not None:
            result = "OPEN"
            for _, bar_high, bar_low, _ in bars:
                if bar_low <= stop and bar_high >= tp1:
                    result = "STOP_SAME_BAR_CONSERVATIVE"
                    break
                if bar_low <= stop:
                    result = "STOP"
                    break
                if bar_high >= tp1:
                    result = "TP1"
                    break
    elif entry.get("decision_type") == "REJECTED":
        result = "MISSED_UPSIDE_GE5" if mfe >= 5.0 else "NO_5PCT_MFE"

    return {
        "horizon_hours": horizon_hours,
        "result": result,
        "mfe_pct": round(mfe, 4),
        "mae_pct": round(mae, 4),
        "close_return_pct": round(close_return, 4),
        "bars_used": len(bars),
        "method": "closed_5m_bars_after_decision_bar",
    }
