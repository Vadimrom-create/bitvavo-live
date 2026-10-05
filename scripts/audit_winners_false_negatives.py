#!/usr/bin/env python3
"""Post-hoc causal audit of recent top 24h winners vs Solaire's live funnel.

The endpoint 24h ranking is used only to select the audit cohort. All detector,
gate and delivery milestones are reconstructed chronologically from committed
production snapshots. Forward outcomes are evaluated afterwards from Bitvavo
5m candles and never feed back into the reconstructed decisions.

Measurement only: this script never changes production thresholds, alerts,
orders or portfolio state.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient

OUT_JSON = "research/winners_false_negative_audit_latest.json"
OUT_MD = "research/winners_false_negative_audit_latest.md"

DEFAULT_HOURS = 24
DEFAULT_TOP_N = 20
FORWARD_HOURS = (1, 4, 12, 24)
CADENCE_GAP_MINUTES = 15.0


def _ts(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()
    except Exception:
        return finite(value)


def _git_text(ref: str, path: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"{ref}:{path}"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None


def _git_json(ref: str, path: str) -> dict[str, Any]:
    raw = _git_text(ref, path)
    if not raw:
        return {}
    try:
        value = json.loads(raw)
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}


def _snapshot_commits(hours: int) -> list[str]:
    lookback = max(hours + 8, 36)
    output = subprocess.check_output(
        [
            "git",
            "log",
            "--first-parent",
            "--format=%H",
            f"--since={lookback} hours ago",
            "--",
            "production_universe_snapshot.json",
        ],
        cwd=ROOT,
        text=True,
    )
    return [line.strip() for line in output.splitlines() if line.strip()][::-1]


def _rows_by_market(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("market")): row
        for row in (doc.get("rows") or [])
        if isinstance(row, dict) and row.get("market")
    }


def _extract_gate(status: dict[str, Any], market: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    checked = status.get("checked_at_utc")
    ts = _ts(checked)

    deliveries = status.get("deliveries")
    if not isinstance(deliveries, list):
        deliveries = []
    for row in deliveries:
        if isinstance(row, dict) and row.get("market") == market:
            out.append(
                {
                    "at_utc": checked,
                    "ts": ts,
                    "outcome": "BUY_SENT",
                    "reason": "DELIVERED",
                    "entry_eur": finite(row.get("entry_eur")),
                    "stop_eur": finite(row.get("stop_eur")),
                    "tp1_eur": finite(row.get("tp1_eur")),
                    "tp2_eur": finite(row.get("tp2_eur")),
                    "spread_pct": finite(row.get("spread_pct")),
                    "stop_distance_pct": finite(row.get("stop_distance_pct")),
                    "stake_eur": finite(row.get("stake_eur")),
                    "execution_evidence_path": row.get("execution_evidence_path"),
                }
            )

    if (
        status.get("email") == "DELIVERY_COMPLETED"
        and status.get("market") == market
        and not any(x["outcome"] == "BUY_SENT" for x in out)
    ):
        out.append(
            {
                "at_utc": checked,
                "ts": ts,
                "outcome": "BUY_SENT",
                "reason": "DELIVERED",
                "entry_eur": finite(status.get("entry_eur")),
                "stop_eur": finite(status.get("stop_eur")),
                "tp1_eur": finite(status.get("tp1_eur")),
                "tp2_eur": finite(status.get("tp2_eur")),
                "spread_pct": finite(status.get("spread_pct")),
                "stop_distance_pct": finite(status.get("stop_distance_pct")),
                "stake_eur": finite(status.get("stake_eur")),
                "execution_evidence_path": None,
            }
        )

    for row in status.get("rejections") or []:
        if isinstance(row, dict) and row.get("market") == market:
            out.append(
                {
                    "at_utc": checked,
                    "ts": ts,
                    "outcome": "REJECTED",
                    "reason": row.get("reason"),
                    "execution_evidence_path": row.get("execution_evidence_path"),
                }
            )
    return out


def _read_execution_evidence(ref: str, event: dict[str, Any]) -> dict[str, Any]:
    path = event.get("execution_evidence_path")
    if not path:
        return {}
    doc = _git_json(ref, str(path))
    costs = doc.get("execution_costs") or {}
    plan = doc.get("plan") or {}
    spread = finite(costs.get("spread"))
    best_bid = finite(costs.get("best_bid_eur"))
    best_ask = finite(costs.get("best_ask_eur"))
    book_checked = bool(costs.get("raw_book")) or best_bid is not None or best_ask is not None
    return {
        "execution_pass": doc.get("execution_pass"),
        "execution_reason": doc.get("execution_reason"),
        "best_bid_eur": best_bid,
        "best_ask_eur": best_ask,
        "spread_pct": spread * 100.0 if spread is not None else finite(event.get("spread_pct")),
        "bid_depth_eur": finite(costs.get("bid_depth_eur")),
        "ask_depth_eur": finite(costs.get("ask_depth_eur")),
        "book_valid": costs.get("book_valid"),
        "book_checked": book_checked,
        "stop_distance_pct": finite(plan.get("stop_distance_pct"), finite(event.get("stop_distance_pct"))),
        "entry_eur": finite(plan.get("entry_eur"), finite(event.get("entry_eur"))),
        "stop_eur": finite(plan.get("stop_eur"), finite(event.get("stop_eur"))),
    }


def _price(row: dict[str, Any] | None) -> float | None:
    if not row:
        return None
    return finite(row.get("price_eur"), finite(row.get("last")))


def _acc_state(row: dict[str, Any] | None) -> str | None:
    if not row:
        return None
    acc = row.get("acceleration") or {}
    return acc.get("state") or row.get("signal_state")


def _score(row: dict[str, Any] | None) -> float | None:
    if not row:
        return None
    acc = row.get("acceleration") or {}
    return finite(acc.get("score"), finite(row.get("signal_score")))


def _event(snapshot: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    return {
        "at_utc": snapshot["at_utc"],
        "ts": snapshot["ts"],
        "commit": snapshot["commit"],
        "price_eur": _price(row),
        "state": _acc_state(row),
        "score": _score(row),
        "evidence_count": int(((row.get("acceleration") or {}).get("evidence_count") or 0)),
    }


def _pct(a: float | None, b: float | None) -> float | None:
    a = finite(a)
    b = finite(b)
    if a is None or b is None or a <= 0:
        return None
    return (b / a - 1.0) * 100.0


def _consumed_share(base: float | None, stage: float | None, end: float | None) -> float | None:
    total = _pct(base, end)
    used = _pct(base, stage)
    if total is None or used is None or total <= 0:
        return None
    return used / total * 100.0


def _raw_candles(raw: list[Any]) -> list[dict[str, float]]:
    rows = []
    for item in raw:
        if not isinstance(item, list) or len(item) < 6:
            continue
        vals = [finite(x) for x in item[:6]]
        if any(v is None for v in vals):
            continue
        t, o, h, l, c, v = vals
        rows.append(
            {
                "ts": t / 1000.0,
                "open": o,
                "high": h,
                "low": l,
                "close": c,
                "volume": v,
            }
        )
    return sorted(rows, key=lambda x: x["ts"])


def _forward(
    rows: list[dict[str, float]],
    event_ts: float | None,
    base: float | None,
    hours: int,
    anchor_ts: float,
) -> dict[str, Any] | None:
    event_ts = finite(event_ts)
    base = finite(base)
    if event_ts is None or base is None or base <= 0:
        return None
    end = event_ts + hours * 3600
    xs = [x for x in rows if event_ts <= x["ts"] < min(end, anchor_ts + 1)]
    if not xs:
        return None
    return {
        "hours": hours,
        "mfe_pct": round((max(x["high"] for x in xs) / base - 1.0) * 100.0, 4),
        "mae_pct": round((min(x["low"] for x in xs) / base - 1.0) * 100.0, 4),
        "close_pct": round((xs[-1]["close"] / base - 1.0) * 100.0, 4),
        "bars": len(xs),
        "complete": anchor_ts >= end - 300,
    }


def _decision_base(result: dict[str, Any]) -> tuple[float | None, float | None, str]:
    buy = result.get("first_buy_sent")
    if buy:
        return (
            finite(buy.get("ts")),
            finite(buy.get("entry_eur"), finite(buy.get("scan_price_eur"))),
            "BUY_SENT",
        )
    gate = result.get("first_gate_event")
    if gate:
        return finite(gate.get("ts")), finite(gate.get("scan_price_eur")), "GATE"
    confirmed = result.get("first_confirmed")
    if confirmed:
        return finite(confirmed.get("ts")), finite(confirmed.get("price_eur")), "CONFIRMED"
    building = result.get("first_building")
    if building:
        return finite(building.get("ts")), finite(building.get("price_eur")), "BUILDING"
    return None, None, "NONE"


def _primary_cause(result: dict[str, Any]) -> str:
    if result.get("first_buy_sent"):
        return "CAPTURED_BUY"
    reasons = [
        x.get("reason")
        for x in result.get("gate_events") or []
        if x.get("outcome") == "REJECTED"
    ]
    if reasons:
        return "GATE_" + str(reasons[0] or "UNKNOWN")
    if result.get("first_confirmed"):
        return "CONFIRMED_NO_GATE_EVIDENCE"
    if result.get("first_building"):
        return "BUILDING_NEVER_CONFIRMED"
    return "DETECTOR_NEVER_BUILDING"


def _fmt(value: Any, digits: int = 2) -> str:
    value = finite(value)
    return "—" if value is None else f"{value:.{digits}f}"


def _markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Solaire — Winners / False Negatives audit",
        "",
        f"- Generated: `{payload['generated_at_utc']}`",
        f"- Anchor: `{payload['anchor_at_utc']}`",
        f"- Window: **{payload['window_hours']} h**",
        f"- Cohort: top **{payload['top_n']}** positive 24h winners at the anchor snapshot.",
        "- The endpoint ranking selects the cohort only; detector/gate milestones are reconstructed chronologically from committed production snapshots.",
        "- Forward MFE/MAE are outcome measurements only and never alter the reconstructed decision path.",
        "",
        "## Cohort",
        "",
        "| Market | 24h | First BUILDING | First CONFIRMED | First gate / BUY | Primary cause | Remaining to anchor after decision | 4h MFE after decision |",
        "|---|---:|---|---|---|---|---:|---:|",
    ]
    for row in payload["winners"]:
        b = row.get("first_building")
        c = row.get("first_confirmed")
        g = row.get("first_buy_sent") or row.get("first_gate_event")
        f4 = (row.get("forward_from_decision") or {}).get("4") or {}
        gate = "—"
        if g:
            gate = "BUY_SENT" if g.get("outcome") == "BUY_SENT" else str(g.get("reason") or "REJECTED")
        lines.append(
            "| {market} | {ret}% | {b} | {c} | {gate} | `{cause}` | {remain}% | {mfe}%{partial} |".format(
                market=row["market"],
                ret=_fmt(row.get("endpoint_24h_return_pct")),
                b=(f"{_fmt(b.get('price_eur'), 8)}" if b else "—"),
                c=(f"{_fmt(c.get('price_eur'), 8)}" if c else "—"),
                gate=gate,
                cause=row["primary_cause"],
                remain=_fmt(row.get("remaining_to_anchor_from_decision_pct")),
                mfe=_fmt(f4.get("mfe_pct")),
                partial="" if f4.get("complete") else " (partial)",
            )
        )

    lines.extend(["", "## Attribution", ""])
    for key, value in sorted(payload["cause_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: **{value}**")

    lines.extend(
        [
            "",
            "## Gate false-negative candidates",
            "",
            "Cases rejected by the execution gate whose post-decision path still reached +5% MFE within a complete 4h window while avoiding -5% MAE.",
        ]
    )
    rows = payload.get("gate_false_negative_candidates") or []
    if not rows:
        lines.append("- None mature enough to qualify in this run.")
    else:
        for item in rows:
            lines.append(
                f"- **{item['market']}** — `{item['primary_cause']}`; 4h MFE {_fmt(item['mfe_4h_pct'])}% / MAE {_fmt(item['mae_4h_pct'])}%."
            )

    lines.extend(["", "## Detector misses / late-stage diagnostics", ""])
    misses = [
        x
        for x in payload["winners"]
        if x["primary_cause"] in {"DETECTOR_NEVER_BUILDING", "BUILDING_NEVER_CONFIRMED"}
    ]
    if not misses:
        lines.append("- No detector-only misses in this cohort.")
    else:
        for item in misses:
            lines.append(
                f"- **{item['market']}** — `{item['primary_cause']}`; 24h {_fmt(item['endpoint_24h_return_pct'])}%; "
                f"largest observed scan gap {_fmt(item.get('max_scan_gap_minutes'))} min."
            )

    lines.extend(
        [
            "",
            "## Safety / interpretation",
            "",
            "- `cadence_gap_flag` is diagnostic only; it does not prove a signal would have fired inside the missing interval.",
            "- `INSUFFICIENT_EXECUTION_LIQUIDITY` currently occurs before the order book is fetched; those rows explicitly record `book_checked=false` when evidence confirms that path.",
            "- A positive post-rejection MFE does not by itself prove that a safe fill was available. Spread, depth, structural stop and exchange lifecycle risks remain separate constraints.",
            "- This audit is measurement-only and makes no production changes.",
            "",
        ]
    )
    return "\n".join(lines)


def build_audit(hours: int = DEFAULT_HOURS, top_n: int = DEFAULT_TOP_N) -> dict[str, Any]:
    commits = _snapshot_commits(hours)
    snapshots: list[dict[str, Any]] = []
    for commit in commits:
        doc = _git_json(commit, "production_universe_snapshot.json")
        at = doc.get("generated_at_utc")
        ts = _ts(at)
        if ts is None:
            continue
        snapshots.append(
            {
                "commit": commit,
                "at_utc": at,
                "ts": ts,
                "rows": _rows_by_market(doc),
                "alert_status": _git_json(commit, "production_alert_status.json"),
            }
        )
    snapshots.sort(key=lambda x: x["ts"])
    if not snapshots:
        raise RuntimeError("NO_PRODUCTION_SNAPSHOTS")

    anchor = snapshots[-1]
    anchor_ts = anchor["ts"]
    window_start = anchor_ts - hours * 3600
    in_window = [x for x in snapshots if x["ts"] >= window_start]
    if not in_window:
        raise RuntimeError("NO_SNAPSHOTS_IN_WINDOW")

    endpoint_rows = list(anchor["rows"].values())
    winners = sorted(
        [
            r
            for r in endpoint_rows
            if finite(r.get("change_24h_pct")) is not None
            and finite(r.get("change_24h_pct")) > 0
        ],
        key=lambda r: finite(r.get("change_24h_pct"), -1e9),
        reverse=True,
    )[:top_n]

    client = PublicClient(timeout=12, retries=3, requests_per_second=8)
    client.get("/time", cache=False)

    results: list[dict[str, Any]] = []
    for endpoint in winners:
        market = endpoint["market"]
        timeline: list[tuple[dict[str, Any], dict[str, Any]]] = []
        for snap in in_window:
            row = snap["rows"].get(market)
            if row:
                timeline.append((snap, row))
        if not timeline:
            continue

        base_snap, base_row = timeline[0]
        end_price = _price(endpoint)
        first_building = None
        first_confirmed = None
        first_acceleration = None
        first_accel_idx = None
        gate_events: list[dict[str, Any]] = []

        for idx, (snap, row) in enumerate(timeline):
            state = _acc_state(row)
            if first_accel_idx is None and state in {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}:
                first_accel_idx = idx
                first_acceleration = _event(snap, row)
            if (
                first_building is None
                and first_confirmed is None
                and state == "BUILDING_ACCELERATION"
            ):
                first_building = _event(snap, row)
            if first_confirmed is None and state == "CONFIRMED_ACCELERATION":
                first_confirmed = _event(snap, row)

            for gate in _extract_gate(snap["alert_status"], market):
                event = dict(gate)
                event["commit"] = snap["commit"]
                event["scan_price_eur"] = _price(row)
                event["evidence"] = _read_execution_evidence(snap["commit"], event)
                gate_events.append(event)

        before = None
        if first_accel_idx is not None and first_accel_idx > 0:
            prev_snap, prev_row = timeline[first_accel_idx - 1]
            before = _event(prev_snap, prev_row)

        dedup = []
        seen = set()
        for ev in gate_events:
            sig = (ev.get("ts"), ev.get("outcome"), ev.get("reason"))
            if sig not in seen:
                seen.add(sig)
                dedup.append(ev)
        gate_events = sorted(dedup, key=lambda x: finite(x.get("ts"), 0.0))
        first_buy = next((x for x in gate_events if x.get("outcome") == "BUY_SENT"), None)
        first_gate = gate_events[0] if gate_events else None

        scan_times = [snap["ts"] for snap, _ in timeline]
        gaps = [(b - a) / 60.0 for a, b in zip(scan_times, scan_times[1:])]
        max_gap = max(gaps) if gaps else 0.0
        preceding_gap = None
        if first_accel_idx is not None and first_accel_idx > 0:
            preceding_gap = (
                timeline[first_accel_idx][0]["ts"] - timeline[first_accel_idx - 1][0]["ts"]
            ) / 60.0

        result = {
            "market": market,
            "endpoint_at_utc": anchor["at_utc"],
            "endpoint_price_eur": end_price,
            "endpoint_24h_return_pct": finite(endpoint.get("change_24h_pct")),
            "endpoint_quote_volume_24h_eur": finite(endpoint.get("quote_volume_24h_eur")),
            "window_first_at_utc": base_snap["at_utc"],
            "window_first_price_eur": _price(base_row),
            "before_first_acceleration": before,
            "first_acceleration": first_acceleration,
            "first_building": first_building,
            "first_confirmed": first_confirmed,
            "gate_events": gate_events,
            "first_gate_event": first_gate,
            "first_buy_sent": first_buy,
            "max_scan_gap_minutes": round(max_gap, 3),
            "preceding_detection_gap_minutes": (
                round(preceding_gap, 3) if preceding_gap is not None else None
            ),
            "cadence_gap_flag": bool(
                preceding_gap is not None and preceding_gap > CADENCE_GAP_MINUTES
            ),
        }
        result["primary_cause"] = _primary_cause(result)

        base_price = result["window_first_price_eur"]
        result["move_consumed_to_building_pct"] = _consumed_share(
            base_price,
            (first_building or {}).get("price_eur") if first_building else None,
            end_price,
        )
        result["move_consumed_to_confirmed_pct"] = _consumed_share(
            base_price,
            (first_confirmed or {}).get("price_eur") if first_confirmed else None,
            end_price,
        )

        decision_ts, decision_price, decision_kind = _decision_base(result)
        result["decision_kind"] = decision_kind
        result["decision_ts"] = decision_ts
        result["decision_price_eur"] = decision_price
        result["remaining_to_anchor_from_decision_pct"] = _pct(decision_price, end_price)

        try:
            candles = _raw_candles(
                client.get(
                    "/" + market + "/candles",
                    {"interval": "5m", "limit": 400},
                    cache=False,
                )
            )
        except Exception as exc:
            candles = []
            result["outcome_data_error"] = type(exc).__name__ + ":" + str(exc)

        result["forward_from_decision"] = {
            str(h): _forward(candles, decision_ts, decision_price, h, anchor_ts)
            for h in FORWARD_HOURS
        }
        results.append(result)

    cause_counts = Counter(row["primary_cause"] for row in results)
    gate_false_negative_candidates = []
    for row in results:
        if not row["primary_cause"].startswith("GATE_"):
            continue
        f4 = row["forward_from_decision"].get("4") or {}
        if not f4.get("complete"):
            continue
        mfe = finite(f4.get("mfe_pct"))
        mae = finite(f4.get("mae_pct"))
        if mfe is not None and mae is not None and mfe >= 5.0 and mae > -5.0:
            gate_false_negative_candidates.append(
                {
                    "market": row["market"],
                    "primary_cause": row["primary_cause"],
                    "mfe_4h_pct": mfe,
                    "mae_4h_pct": mae,
                    "remaining_to_anchor_from_decision_pct": row.get(
                        "remaining_to_anchor_from_decision_pct"
                    ),
                }
            )

    return {
        "schema": "solaire_winners_false_negative_audit_v1",
        "generated_at_utc": utc(),
        "anchor_at_utc": anchor["at_utc"],
        "window_hours": hours,
        "top_n": top_n,
        "cohort_selection": "TOP_POSITIVE_CHANGE_24H_AT_ANCHOR",
        "causality": {
            "endpoint_ranking_used_only_for_cohort_selection": True,
            "decision_reconstruction_from_committed_snapshots_only": True,
            "forward_outcomes_do_not_affect_decisions": True,
        },
        "measurement_only": True,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_orders": False,
        "snapshot_count": len(in_window),
        "max_global_scan_gap_minutes": round(
            max(
                [
                    (b["ts"] - a["ts"]) / 60.0
                    for a, b in zip(in_window, in_window[1:])
                ]
                or [0.0]
            ),
            3,
        ),
        "cause_counts": dict(cause_counts),
        "gate_false_negative_candidates": gate_false_negative_candidates,
        "winners": results,
        "errors": list(client.errors),
    }


def main() -> int:
    hours = int(os.getenv("WINNERS_AUDIT_HOURS", str(DEFAULT_HOURS)))
    top_n = int(os.getenv("WINNERS_AUDIT_TOP_N", str(DEFAULT_TOP_N)))
    payload = build_audit(hours=hours, top_n=top_n)
    atomic_json(OUT_JSON, payload)
    Path(OUT_MD).write_text(_markdown(payload), encoding="utf-8")
    print(
        "SOLAIRE_WINNERS_FALSE_NEGATIVES "
        + json.dumps(
            {
                "anchor_at_utc": payload["anchor_at_utc"],
                "snapshot_count": payload["snapshot_count"],
                "cause_counts": payload["cause_counts"],
                "gate_false_negative_candidates": payload[
                    "gate_false_negative_candidates"
                ],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
