#!/usr/bin/env python3
"""Research-only audit of stop confirmation policies.

Goal: quantify how often an intrabar touch of the structural stop is followed by
recovery, and compare that with confirmation-based exits (5m close, two
consecutive 5m closes, 15m close) protected by a deeper catastrophe stop.

This script does not change production detection, BUY gates, emails, position
monitoring, or live order behavior.
"""
from __future__ import annotations

import json
import math
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient

JOURNAL = ROOT / "production_decision_journal.json"
MANUAL = ROOT / "research/manual_stop_cases_20261006.json"
OUT_JSON = ROOT / "research/stop_confirmation_audit_20261006.json"
OUT_MD = ROOT / "research/stop_confirmation_audit_20261006.md"

WINDOW_START = "2026-09-21T00:00:00+00:00"
MAX_ENTRY_TO_TOUCH_HOURS = 12
POST_TOUCH_HOURS = 4
HARD_R_DEFAULT = 1.50
HARD_R_GRID = (1.25, 1.50, 1.75, 2.00)
DEPTH_R_GRID = (0.25, 0.50, 0.75)
DEPTH_TIMEFRAMES = ("5m", "15m")
POLICIES = ("touch", "close_5m", "close_2x5m", "close_15m")


def ts(value):
    return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()


def median(values):
    xs = [x for x in values if x is not None and math.isfinite(x)]
    return round(statistics.median(xs), 5) if xs else None


def mean(values):
    xs = [x for x in values if x is not None and math.isfinite(x)]
    return round(sum(xs) / len(xs), 5) if xs else None


def parse_bars(raw, now):
    out = []
    for row in raw:
        if not isinstance(row, list) or len(row) < 6:
            continue
        vals = [finite(v) for v in row[:6]]
        if any(v is None for v in vals):
            continue
        t, o, h, l, c, v = vals
        if t + 300_000 <= now * 1000:
            out.append((int(t), o, h, l, c, v))
    return sorted(out)


def fetch_bars(client, market, start_ts, end_ts, now):
    raw = client.get(
        "/" + market + "/candles",
        {
            "interval": "5m",
            "limit": 500,
            "start": int(start_ts * 1000),
            "end": int(end_ts * 1000),
        },
        cache=False,
    )
    return parse_bars(raw, now)


def bar_close_ts(bar):
    return bar[0] / 1000 + 300


def first_touch_index(bars, stop, not_before):
    for i, bar in enumerate(bars):
        if bar_close_ts(bar) < not_before:
            continue
        if bar[3] <= stop:
            return i
    return None


def mark_close(bars, target_ts):
    eligible = [b for b in bars if bar_close_ts(b) <= target_ts]
    if not eligible:
        return None
    return eligible[-1][4]


def hard_stop(entry, stop, hard_r):
    risk = entry - stop
    if risk <= 0:
        return None
    return entry - hard_r * risk


def policy_exit(bars, touch_idx, stop, entry, policy, hard_r=HARD_R_DEFAULT, horizon_hours=POST_TOUCH_HOURS):
    if touch_idx is None:
        return None
    touch_bar = bars[touch_idx]
    touch_ts = bar_close_ts(touch_bar)
    horizon = touch_ts + horizon_hours * 3600
    hstop = hard_stop(entry, stop, hard_r)

    if policy == "touch":
        return {"triggered": True, "reason": "STOP_TOUCH", "exit_ts": touch_ts, "exit_eur": stop, "hard_stop_eur": hstop}

    consecutive = 0
    for bar in bars[touch_idx:]:
        t, o, h, l, c, v = bar
        close_ts = bar_close_ts(bar)
        if close_ts > horizon:
            break

        # Catastrophe guard is deliberately evaluated before close confirmation.
        if hstop is not None and l <= hstop:
            return {
                "triggered": True,
                "reason": "HARD_STOP",
                "exit_ts": close_ts,
                "exit_eur": hstop,
                "hard_stop_eur": hstop,
            }

        if policy == "close_5m":
            if c <= stop:
                return {
                    "triggered": True,
                    "reason": "CLOSE_5M",
                    "exit_ts": close_ts,
                    "exit_eur": c,
                    "hard_stop_eur": hstop,
                }

        elif policy == "close_2x5m":
            consecutive = consecutive + 1 if c <= stop else 0
            if consecutive >= 2:
                return {
                    "triggered": True,
                    "reason": "CLOSE_2X5M",
                    "exit_ts": close_ts,
                    "exit_eur": c,
                    "hard_stop_eur": hstop,
                }

        elif policy == "close_15m":
            # UTC-aligned 15m candle closes on 5m bars starting at minute 10/25/40/55.
            if (t // 300_000) % 3 == 2 and c <= stop:
                return {
                    "triggered": True,
                    "reason": "CLOSE_15M",
                    "exit_ts": close_ts,
                    "exit_eur": c,
                    "hard_stop_eur": hstop,
                }

    final = mark_close(bars[touch_idx:], horizon)
    return {
        "triggered": False,
        "reason": "HELD_TO_HORIZON",
        "exit_ts": horizon,
        "exit_eur": final,
        "hard_stop_eur": hstop,
    }

def depth_confirm_exit(
    bars,
    touch_idx,
    stop,
    entry,
    timeframe,
    depth_r,
    hard_r,
    horizon_hours=POST_TOUCH_HOURS,
):
    """Confirm invalidation only after a close materially below the soft stop.

    threshold = original stop - depth_r * original R.
    A deeper intrabar catastrophe stop remains active at entry - hard_r * R.
    """
    if touch_idx is None:
        return None
    risk = entry - stop
    if risk <= 0:
        return None
    threshold = stop - depth_r * risk
    hstop = hard_stop(entry, stop, hard_r)
    touch_ts = bar_close_ts(bars[touch_idx])
    horizon = touch_ts + horizon_hours * 3600

    for bar in bars[touch_idx:]:
        t, o, h, l, c, v = bar
        close_ts = bar_close_ts(bar)
        if close_ts > horizon:
            break
        if hstop is not None and l <= hstop:
            return {
                "triggered": True,
                "reason": "HARD_STOP",
                "exit_ts": close_ts,
                "exit_eur": hstop,
                "hard_stop_eur": hstop,
                "confirmation_threshold_eur": threshold,
            }
        aligned = timeframe == "5m" or ((t // 300_000) % 3 == 2)
        if aligned and c <= threshold:
            return {
                "triggered": True,
                "reason": f"CLOSE_{timeframe.upper()}_DEPTH_{depth_r}R",
                "exit_ts": close_ts,
                "exit_eur": c,
                "hard_stop_eur": hstop,
                "confirmation_threshold_eur": threshold,
            }

    final = mark_close(bars[touch_idx:], horizon)
    return {
        "triggered": False,
        "reason": "HELD_TO_HORIZON",
        "exit_ts": horizon,
        "exit_eur": final,
        "hard_stop_eur": hstop,
        "confirmation_threshold_eur": threshold,
    }


def analyze_case(case, bars, not_before, source):
    entry = finite(case.get("entry_eur"))
    stop = finite(case.get("stop_eur"))
    if entry is None or stop is None or not (entry > stop > 0):
        return None, "INVALID_ENTRY_OR_STOP"

    touch_idx = first_touch_index(bars, stop, not_before)
    if touch_idx is None:
        return None, "STOP_NOT_TOUCHED"

    touch_bar = bars[touch_idx]
    touch_ts = bar_close_ts(touch_bar)
    policies = {
        name: policy_exit(bars, touch_idx, stop, entry, name)
        for name in POLICIES
    }

    marks = {}
    for mins in (15, 30, 60, 240):
        px = mark_close(bars[touch_idx:], touch_ts + mins * 60)
        marks[str(mins)] = {
            "close_eur": px,
            "vs_stop_pct": round((px / stop - 1) * 100, 4) if px else None,
            "vs_entry_pct": round((px / entry - 1) * 100, 4) if px else None,
        }

    hard_grid = {}
    policy_grid = {}
    for hard_r in HARD_R_GRID:
        hstop = hard_stop(entry, stop, hard_r)
        hit = False
        hit_ts = None
        for bar in bars[touch_idx:]:
            if bar_close_ts(bar) > touch_ts + POST_TOUCH_HOURS * 3600:
                break
            if hstop is not None and bar[3] <= hstop:
                hit = True
                hit_ts = bar_close_ts(bar)
                break
        hard_grid[str(hard_r)] = {"hard_stop_eur": hstop, "hit": hit, "hit_ts": hit_ts}
        policy_grid[str(hard_r)] = {
            name: policy_exit(bars, touch_idx, stop, entry, name, hard_r=hard_r)
            for name in POLICIES
        }

    depth_policy_grid = {}
    for hard_r in HARD_R_GRID:
        hard_key = str(hard_r)
        depth_policy_grid[hard_key] = {}
        for timeframe in DEPTH_TIMEFRAMES:
            depth_policy_grid[hard_key][timeframe] = {}
            for depth_r in DEPTH_R_GRID:
                depth_policy_grid[hard_key][timeframe][str(depth_r)] = depth_confirm_exit(
                    bars, touch_idx, stop, entry, timeframe, depth_r, hard_r
                )

    actual_exit = finite(case.get("actual_exit_eur"))
    actual_slippage = None
    if actual_exit is not None:
        actual_slippage = round((actual_exit / stop - 1) * 100, 4)

    return {
        "case_id": case.get("case_id") or f"{case.get('market')}@{int(not_before)}",
        "source": source,
        "market": case.get("market"),
        "entry_eur": entry,
        "stop_eur": stop,
        "risk_pct": round((entry - stop) / entry * 100, 4),
        "touch_bar_start_utc": datetime.fromtimestamp(touch_bar[0] / 1000, tz=datetime.now().astimezone().tzinfo).astimezone().isoformat(),
        "touch_close_ts": touch_ts,
        "touch_low_eur": touch_bar[3],
        "touch_close_eur": touch_bar[4],
        "actual_exit_eur": actual_exit,
        "actual_exit_vs_stop_pct": actual_slippage,
        "marks_after_touch": marks,
        "policies": policies,
        "hard_stop_sensitivity": hard_grid,
        "policy_hard_stop_grid": policy_grid,
        "depth_policy_grid": depth_policy_grid,
        "wick_reclaim_15m": bool(
            marks["15"]["close_eur"] is not None
            and marks["15"]["close_eur"] > stop
            and not (
                policies["close_5m"]["triggered"]
                and policies["close_5m"]["exit_ts"] <= touch_ts + 15 * 60
            )
        ),
        "recovered_above_stop_60m": bool(marks["60"]["close_eur"] is not None and marks["60"]["close_eur"] > stop),
        "recovered_above_stop_240m": bool(marks["240"]["close_eur"] is not None and marks["240"]["close_eur"] > stop),
    }, None


def aggregate(rows):
    out = {
        "cases": len(rows),
        "wick_reclaim_15m": sum(bool(r.get("wick_reclaim_15m")) for r in rows),
        "recovered_above_stop_60m": sum(bool(r.get("recovered_above_stop_60m")) for r in rows),
        "recovered_above_stop_240m": sum(bool(r.get("recovered_above_stop_240m")) for r in rows),
        "policies": {},
        "hard_stop_sensitivity": {},
        "policy_hard_stop_matrix": {},
        "depth_policy_matrix": {},
    }
    for policy in POLICIES:
        exits = [r["policies"][policy] for r in rows if r.get("policies", {}).get(policy)]
        deltas_4h = []
        for r in rows:
            p = r["policies"].get(policy)
            touch = r["policies"].get("touch")
            if not p or not touch or p.get("exit_eur") is None or touch.get("exit_eur") is None:
                continue
            deltas_4h.append((p["exit_eur"] / r["entry_eur"] - touch["exit_eur"] / r["entry_eur"]) * 100)
        out["policies"][policy] = {
            "triggered": sum(bool(x.get("triggered")) for x in exits),
            "hard_stop_exits": sum(x.get("reason") == "HARD_STOP" for x in exits),
            "held_to_4h": sum(x.get("reason") == "HELD_TO_HORIZON" for x in exits),
            "mean_delta_vs_touch_pct_points": mean(deltas_4h),
            "median_delta_vs_touch_pct_points": median(deltas_4h),
        }

    for hard_r in HARD_R_GRID:
        key = str(hard_r)
        vals = [r.get("hard_stop_sensitivity", {}).get(key) for r in rows]
        vals = [x for x in vals if x]
        out["hard_stop_sensitivity"][key] = {
            "hit": sum(bool(x.get("hit")) for x in vals),
            "not_hit": sum(not bool(x.get("hit")) for x in vals),
        }
        out["policy_hard_stop_matrix"][key] = {}
        for policy in ("close_5m", "close_2x5m", "close_15m"):
            exits = []
            deltas = []
            for r in rows:
                p = r.get("policy_hard_stop_grid", {}).get(key, {}).get(policy)
                touch = r.get("policies", {}).get("touch")
                if not p or not touch:
                    continue
                exits.append(p)
                if p.get("exit_eur") is not None and touch.get("exit_eur") is not None:
                    deltas.append((p["exit_eur"] / r["entry_eur"] - touch["exit_eur"] / r["entry_eur"]) * 100)
            eps = 1e-12
            out["policy_hard_stop_matrix"][key][policy] = {
                "n": len(exits),
                "triggered": sum(bool(x.get("triggered")) for x in exits),
                "hard_stop_exits": sum(x.get("reason") == "HARD_STOP" for x in exits),
                "held_to_4h": sum(x.get("reason") == "HELD_TO_HORIZON" for x in exits),
                "improved_vs_touch": sum(x > eps for x in deltas),
                "worsened_vs_touch": sum(x < -eps for x in deltas),
                "ties": sum(abs(x) <= eps for x in deltas),
                "mean_delta_vs_touch_pct_points": mean(deltas),
                "median_delta_vs_touch_pct_points": median(deltas),
                "best_delta_pct_points": round(max(deltas), 5) if deltas else None,
                "worst_delta_pct_points": round(min(deltas), 5) if deltas else None,
            }
    for hard_r in HARD_R_GRID:
        hard_key = str(hard_r)
        out["depth_policy_matrix"][hard_key] = {}
        for timeframe in DEPTH_TIMEFRAMES:
            out["depth_policy_matrix"][hard_key][timeframe] = {}
            for depth_r in DEPTH_R_GRID:
                depth_key = str(depth_r)
                exits = []
                deltas = []
                for r in rows:
                    p = r.get("depth_policy_grid", {}).get(hard_key, {}).get(timeframe, {}).get(depth_key)
                    touch = r.get("policies", {}).get("touch")
                    if not p or not touch:
                        continue
                    exits.append(p)
                    if p.get("exit_eur") is not None and touch.get("exit_eur") is not None:
                        deltas.append((p["exit_eur"] / r["entry_eur"] - touch["exit_eur"] / r["entry_eur"]) * 100)
                eps = 1e-12
                out["depth_policy_matrix"][hard_key][timeframe][depth_key] = {
                    "n": len(exits),
                    "triggered": sum(bool(x.get("triggered")) for x in exits),
                    "hard_stop_exits": sum(x.get("reason") == "HARD_STOP" for x in exits),
                    "held_to_4h": sum(x.get("reason") == "HELD_TO_HORIZON" for x in exits),
                    "improved_vs_touch": sum(x > eps for x in deltas),
                    "worsened_vs_touch": sum(x < -eps for x in deltas),
                    "ties": sum(abs(x) <= eps for x in deltas),
                    "mean_delta_vs_touch_pct_points": mean(deltas),
                    "median_delta_vs_touch_pct_points": median(deltas),
                    "best_delta_pct_points": round(max(deltas), 5) if deltas else None,
                    "worst_delta_pct_points": round(min(deltas), 5) if deltas else None,
                }
    return out


def markdown(report):
    s = report["summary"]
    lines = [
        "# Stop confirmation audit — 2026-10-06",
        "",
        "Research-only: no production rule was changed.",
        "",
        f"- Stop-touch cases analysed: **{s['cases']}**",
        f"- Wick reclaims within 15m: **{s['wick_reclaim_15m']}**",
        f"- Back above stop after 60m: **{s['recovered_above_stop_60m']}**",
        f"- Back above stop after 4h: **{s['recovered_above_stop_240m']}**",
        "",
        "## Policy comparison",
        "",
        "| Policy | Exits | Hard-stop exits | Held to 4h | Mean delta vs touch (pp) | Median delta (pp) |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for p in POLICIES:
        x = s["policies"][p]
        lines.append(
            f"| {p} | {x['triggered']} | {x['hard_stop_exits']} | {x['held_to_4h']} | "
            f"{x['mean_delta_vs_touch_pct_points']} | {x['median_delta_vs_touch_pct_points']} |"
        )
    lines += [
        "",
        "## Hard-stop sensitivity",
        "",
        "| Hard stop | Hits | Not hit |",
        "|---|---:|---:|",
    ]
    for hard_r in HARD_R_GRID:
        x = s["hard_stop_sensitivity"][str(hard_r)]
        lines.append(f"| {hard_r}R | {x['hit']} | {x['not_hit']} |")

    lines += [
        "",
        "## Confirmation × hard-stop matrix",
        "",
        "| Hard stop | Policy | Improved | Worsened | Held 4h | Hard exits | Mean delta (pp) | Median delta (pp) | Worst (pp) | Best (pp) |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for hard_r in HARD_R_GRID:
        key = str(hard_r)
        for policy in ("close_5m", "close_2x5m", "close_15m"):
            x = s["policy_hard_stop_matrix"][key][policy]
            lines.append(
                f"| {hard_r}R | {policy} | {x['improved_vs_touch']} | {x['worsened_vs_touch']} | "
                f"{x['held_to_4h']} | {x['hard_stop_exits']} | {x['mean_delta_vs_touch_pct_points']} | "
                f"{x['median_delta_vs_touch_pct_points']} | {x['worst_delta_pct_points']} | {x['best_delta_pct_points']} |"
            )

    lines += [
        "",
        "## Depth-confirmation matrix",
        "",
        "| Hard stop | TF | Depth | Improved | Worsened | Held 4h | Hard exits | Mean delta (pp) | Median delta (pp) | Worst (pp) | Best (pp) |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for hard_r in HARD_R_GRID:
        hard_key = str(hard_r)
        for timeframe in DEPTH_TIMEFRAMES:
            for depth_r in DEPTH_R_GRID:
                x = s["depth_policy_matrix"][hard_key][timeframe][str(depth_r)]
                lines.append(
                    f"| {hard_r}R | {timeframe} | {depth_r}R | {x['improved_vs_touch']} | {x['worsened_vs_touch']} | "
                    f"{x['held_to_4h']} | {x['hard_stop_exits']} | {x['mean_delta_vs_touch_pct_points']} | "
                    f"{x['median_delta_vs_touch_pct_points']} | {x['worst_delta_pct_points']} | {x['best_delta_pct_points']} |"
                )

    manual = [r for r in report["cases"] if r.get("source") == "manual_reference"]
    if manual:
        lines += ["", "## Manual reference cases", ""]
        for r in manual:
            lines.append(
                f"- **{r['case_id']} / {r['market']}**: stop {r['stop_eur']}, "
                f"touch low {r['touch_low_eur']}, actual exit {r.get('actual_exit_eur')}, "
                f"15m vs stop {r['marks_after_touch']['15']['vs_stop_pct']}%, "
                f"60m vs stop {r['marks_after_touch']['60']['vs_stop_pct']}%, "
                f"4h vs stop {r['marks_after_touch']['240']['vs_stop_pct']}%."
            )

    lines += [
        "",
        "## Limits",
        "",
        "- 5m OHLC data cannot reveal the exact intrabar path.",
        "- Confirmation policies are diagnostic only; they intentionally ignore profit-taking to isolate stop behaviour.",
        "- The 1.50R catastrophe stop is a research candidate, not a live recommendation.",
        "- BUY_SENT entries are Solaire recommendations, not necessarily every manually executed account trade.",
    ]
    return "\n".join(lines) + "\n"


def main():
    now = time.time()
    client = PublicClient(timeout=12, retries=3, requests_per_second=6)
    client.get("/time", cache=False)

    journal = json.loads(JOURNAL.read_text())
    start = ts(WINDOW_START)
    buys = []
    seen = set()
    for e in journal.get("entries", []):
        if e.get("decision_type") != "BUY_SENT":
            continue
        decision_ts = finite(e.get("decision_ts"))
        entry = finite(e.get("entry_eur"))
        stop = finite(e.get("stop_eur"))
        market = e.get("market")
        if not market or decision_ts is None or decision_ts < start or entry is None or stop is None:
            continue
        key = (market, round(decision_ts, 3), entry, stop)
        if key in seen:
            continue
        seen.add(key)
        buys.append({
            "case_id": f"SOLAIRE_{market}_{int(decision_ts)}",
            "market": market,
            "decision_ts": decision_ts,
            "entry_eur": entry,
            "stop_eur": stop,
        })
    buys.sort(key=lambda x: x["decision_ts"])

    rows = []
    errors = []
    for case in buys:
        try:
            fetch_end = min(now, case["decision_ts"] + (MAX_ENTRY_TO_TOUCH_HOURS + POST_TOUCH_HOURS + 1) * 3600)
            bars = fetch_bars(client, case["market"], case["decision_ts"] - 600, fetch_end, now)
            row, err = analyze_case(case, bars, case["decision_ts"], "solaire_buy_sent")
            if row:
                rows.append(row)
            elif err != "STOP_NOT_TOUCHED":
                errors.append({"case_id": case["case_id"], "market": case["market"], "reason": err})
        except Exception as exc:
            errors.append({"case_id": case["case_id"], "market": case["market"], "reason": type(exc).__name__ + ":" + str(exc)})

    if MANUAL.exists():
        manual = json.loads(MANUAL.read_text())
        for case in manual.get("cases", []):
            try:
                event_ts = ts(case["event_at_utc"])
                bars = fetch_bars(client, case["market"], event_ts - 1800, min(now, event_ts + (POST_TOUCH_HOURS + 1) * 3600), now)
                # Anchor the manual case to the actual execution timestamp. Do
                # not let an earlier touch of the reference stop redefine the event.
                row, err = analyze_case(case, bars, event_ts, "manual_reference")
                if row:
                    rows.append(row)
                else:
                    errors.append({"case_id": case.get("case_id"), "market": case.get("market"), "reason": err})
            except Exception as exc:
                errors.append({"case_id": case.get("case_id"), "market": case.get("market"), "reason": type(exc).__name__ + ":" + str(exc)})

    summary = aggregate(rows)
    report = {
        "schema": "solaire_stop_confirmation_audit_v1",
        "generated_at_utc": utc(),
        "research_only": True,
        "affects_detection": False,
        "affects_buy_gate": False,
        "affects_email": False,
        "affects_position_management": False,
        "window_start_utc": WINDOW_START,
        "max_entry_to_touch_hours": MAX_ENTRY_TO_TOUCH_HOURS,
        "post_touch_hours": POST_TOUCH_HOURS,
        "hard_r_default": HARD_R_DEFAULT,
        "hard_r_grid": list(HARD_R_GRID),
        "depth_r_grid": list(DEPTH_R_GRID),
        "depth_timeframes": list(DEPTH_TIMEFRAMES),
        "source_buy_count": len(buys),
        "summary": summary,
        "cases": rows,
        "errors": errors,
        "decision_rule": {
            "status": "AUDIT_ONLY",
            "promotion_requires": "sufficient sample plus lower false-stop cost without unacceptable extra downside",
        },
        "limitations": [
            "5m OHLC cannot reveal exact intrabar ordering",
            "confirmation-policy comparison intentionally isolates stop behaviour and ignores take-profit execution",
            "1.50R catastrophe stop is a research candidate only",
            "BUY_SENT entries do not necessarily include every manual account trade",
        ],
    }
    atomic_json(OUT_JSON, report)
    OUT_MD.write_text(markdown(report))
    print("STOP_CONFIRMATION_AUDIT " + json.dumps({
        "source_buy_count": len(buys),
        "stop_touch_cases": summary["cases"],
        "wick_reclaim_15m": summary["wick_reclaim_15m"],
        "recovered_60m": summary["recovered_above_stop_60m"],
        "recovered_240m": summary["recovered_above_stop_240m"],
        "policies": summary["policies"],
        "errors": errors[:10],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
