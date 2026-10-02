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


def evaluate_closed_5m_path(
    raw_bars: list[list[Any]],
    start_ts: float | None,
    baseline: float | None,
    horizon_hours: int,
    *,
    stop_eur: float | None = None,
    tp1_eur: float | None = None,
) -> dict[str, Any]:
    """Causal 5m evaluator shared by production and measurement-only shadows.

    It only uses fully closed 5m bars strictly after the bar containing the
    start timestamp. Missing intervals are explicit INCOMPLETE results rather
    than being interpreted as flat prices or silently shortened horizons.

    If both stop and TP1 occur inside the same 5m bar, the path result is
    conservative: STOP_SAME_BAR_CONSERVATIVE.
    """
    start_ts = finite(start_ts)
    baseline = finite(baseline)
    if start_ts is None or baseline is None or baseline <= 0:
        return {
            "status": "UNKNOWN",
            "reason": "INVALID_START_OR_BASELINE",
            "horizon_hours": horizon_hours,
            "method": "chronological_continuous_closed_5m_bars_after_decision_bar",
        }

    first_full_start = ((int(start_ts * 1000) // 300_000) + 1) * 300_000
    end_ms = int((start_ts + horizon_hours * 3600) * 1000)
    last_full_start = ((end_ms - 300_000) // 300_000) * 300_000
    if last_full_start < first_full_start:
        return {
            "status": "INCOMPLETE",
            "reason": "NO_FULL_CLOSED_BAR_IN_HORIZON",
            "horizon_hours": horizon_hours,
            "bars_used": 0,
            "expected_bars": 0,
            "coverage_ratio": 0.0,
            "method": "chronological_continuous_closed_5m_bars_after_decision_bar",
        }

    parsed: dict[int, tuple[int, float, float, float]] = {}
    for row in raw_bars:
        if not isinstance(row, list) or len(row) < 6:
            continue
        t = finite(row[0])
        high = finite(row[2])
        low = finite(row[3])
        close = finite(row[4])
        if None in (t, high, low, close):
            continue
        start_ms = int(t)
        if start_ms % 300_000:
            continue
        if first_full_start <= start_ms <= last_full_start:
            parsed[start_ms] = (start_ms, high, low, close)

    expected_starts = list(range(first_full_start, last_full_start + 1, 300_000))
    missing_starts = [start for start in expected_starts if start not in parsed]
    if missing_starts:
        present = len(expected_starts) - len(missing_starts)
        return {
            "status": "INCOMPLETE",
            "reason": "MISSING_CLOSED_5M_BARS",
            "horizon_hours": horizon_hours,
            "bars_used": present,
            "expected_bars": len(expected_starts),
            "missing_bars": len(missing_starts),
            "coverage_ratio": round(present / len(expected_starts), 6)
            if expected_starts
            else 0.0,
            "first_expected_bar_start_ms": first_full_start,
            "last_expected_bar_start_ms": last_full_start,
            "method": "chronological_continuous_closed_5m_bars_after_decision_bar",
        }

    bars = [parsed[start] for start in expected_starts]
    if not bars:
        return {
            "status": "INCOMPLETE",
            "reason": "NO_USABLE_CLOSED_5M_BARS",
            "horizon_hours": horizon_hours,
            "bars_used": 0,
            "expected_bars": len(expected_starts),
            "coverage_ratio": 0.0,
            "method": "chronological_continuous_closed_5m_bars_after_decision_bar",
        }

    high = max(row[1] for row in bars)
    low = min(row[2] for row in bars)
    close = bars[-1][3]
    mfe = (high / baseline - 1) * 100
    mae = (low / baseline - 1) * 100
    close_return = (close / baseline - 1) * 100

    path_result = "OBSERVED"
    path_event_ts = None
    stop_eur = finite(stop_eur)
    tp1_eur = finite(tp1_eur)
    if stop_eur is not None or tp1_eur is not None:
        path_result = "OPEN"
        for bar_ts, bar_high, bar_low, _ in bars:
            stop_hit = stop_eur is not None and bar_low <= stop_eur
            tp1_hit = tp1_eur is not None and bar_high >= tp1_eur
            if stop_hit and tp1_hit:
                path_result = "STOP_SAME_BAR_CONSERVATIVE"
                path_event_ts = bar_ts
                break
            if stop_hit:
                path_result = "STOP"
                path_event_ts = bar_ts
                break
            if tp1_hit:
                path_result = "TP1"
                path_event_ts = bar_ts
                break

    return {
        "status": "COMPLETE",
        "horizon_hours": horizon_hours,
        "result": path_result,
        "mfe_pct": round(mfe, 4),
        "mae_pct": round(mae, 4),
        "close_return_pct": round(close_return, 4),
        "bars_used": len(bars),
        "expected_bars": len(expected_starts),
        "coverage_ratio": 1.0,
        "first_bar_start_ms": bars[0][0],
        "last_bar_start_ms": bars[-1][0],
        "path_event_start_ms": path_event_ts,
        "path_policy": "stop_before_tp1_if_both_touched_same_5m_bar",
        "method": "chronological_continuous_closed_5m_bars_after_decision_bar",
    }


def evaluate_bars(
    entry: dict[str, Any],
    raw_bars: list[list[Any]],
    horizon_hours: int,
) -> dict[str, Any] | None:
    """Backward-compatible production-journal evaluator.

    Existing production behavior is preserved: incomplete/unknown horizons
    still return None. Shadows can call evaluate_closed_5m_path directly to
    keep INCOMPLETE/UNKNOWN provenance visible.
    """
    decision_ts = finite(entry.get("decision_ts"))
    baseline = finite(entry.get("entry_eur"))
    if baseline is None:
        baseline = finite(entry.get("signal_price_eur"))
    if decision_ts is None or baseline is None or baseline <= 0:
        return None

    stop = None
    tp1 = None
    if entry.get("decision_type") == "BUY_SENT":
        stop = finite(entry.get("stop_eur"))
        tp1 = finite(entry.get("tp1_eur"))

    path = evaluate_closed_5m_path(
        raw_bars,
        decision_ts,
        baseline,
        horizon_hours,
        stop_eur=stop,
        tp1_eur=tp1,
    )
    if path.get("status") != "COMPLETE":
        return None

    result = path["result"]
    if entry.get("decision_type") == "REJECTED":
        result = (
            "MISSED_UPSIDE_GE5"
            if finite(path.get("mfe_pct"), -999) >= 5.0
            else "NO_5PCT_MFE"
        )

    # Preserve the historical output contract exactly for production journals.
    return {
        "horizon_hours": horizon_hours,
        "result": result,
        "mfe_pct": path["mfe_pct"],
        "mae_pct": path["mae_pct"],
        "close_return_pct": path["close_return_pct"],
        "bars_used": path["bars_used"],
        "expected_bars": path["expected_bars"],
        "coverage_ratio": path["coverage_ratio"],
        "first_bar_start_ms": path["first_bar_start_ms"],
        "last_bar_start_ms": path["last_bar_start_ms"],
        "path_event_start_ms": path["path_event_start_ms"],
        "method": path["method"],
    }
