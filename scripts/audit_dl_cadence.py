#!/usr/bin/env python3
"""Read-only cadence/coverage report for archived Decision Layer shadow.

Counts observed decision snapshots, never asserts cron jobs ran or were dropped.
Joins machine data using the existing as-of comparator and prints sensitivity.
No trading/execution effects, no extra API calls.
"""
from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compare_direct_decision_shadow import (
    EvidenceError, compare, load_shadow_snapshots, read_events,
)

DEFAULT_AGE_WINDOWS = (900, 1800, 3600, 7200)

def day_utc(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def diagnose_calendar_shift(daily, baseline_start, baseline_end, later_start, later_end):
    """Exploratory fixed-window archive counts; zero-archive days count as zero.

    Dates are UTC and must be fully ended at analysis time. Do not infer
    missing GitHub scheduled dispatches or causal software regressions.
    """
    count_by_day={r["date_utc"]:r["n_snapshots"] for r in daily}
    def segment(start,end):
        start_day=date.fromisoformat(start)
        end_day=date.fromisoformat(end)
        if end_day<start_day:
            raise EvidenceError("invalid date range")
        values=[]
        cursor=start_day
        while cursor<=end_day:
            values.append(count_by_day.get(cursor.isoformat(),0))
            cursor+=timedelta(days=1)
        return {"start_utc":start,"end_utc":end,"full_days":len(values),
                "total_archives":sum(values),
                "mean_per_day":round(statistics.mean(values),4),
                "median_per_day":round(statistics.median(values),4),
                "zero_archive_days":sum(n==0 for n in values)}
    if date.fromisoformat(later_start)<=date.fromisoformat(baseline_end):
        raise EvidenceError("overlapping or reversed diagnosis periods")
    old=segment(baseline_start,baseline_end)
    new=segment(later_start,later_end)
    if old["mean_per_day"]>0:
        change_pct=round(100*(new["mean_per_day"]/old["mean_per_day"]-1),2)
        decline_pct=round(-change_pct,2)
    else:
        change_pct=decline_pct=None
    return {
        "schema":"solaire_dl_archive_frequency_shift_v1",
        "research_only":True,"method":"EXPLORATORY_CALENDAR_PERIOD_COMPARE",
        "baseline":old,"later":new,
        "relative_change_pct":change_pct,"decline_pct":decline_pct,
        "shadow_continuity_degraded":change_pct is not None and change_pct<=-50,
        "causal_conclusion":None,
        "missing_cron_dispatches_proven":None,
        "note":"Counts are generated archival snapshots by completed UTC dates, not GitHub schedule runs or independent trades.",
    }

def summarize_cadence(events, snapshots, windows=DEFAULT_AGE_WINDOWS, *, full_day=None):
    if not windows or any(type(v) is not int or v <= 0 for v in windows):
        raise EvidenceError("freshness windows must be positive integer seconds")
    if len(set(windows)) != len(windows):
        raise EvidenceError("freshness windows duplicated")
    days = defaultdict(list)
    for s in snapshots:
        days[day_utc(s["available_ts"])].append(s["available_ts"])

    daily = []
    for day, values in sorted(days.items()):
        values = sorted(values)
        gaps = [(b-a)/60 for a,b in zip(values, values[1:])]
        daily.append({
            "date_utc": day, "n_snapshots": len(values),
            "first_generated_utc": datetime.fromtimestamp(values[0],timezone.utc).isoformat(),
            "last_generated_utc": datetime.fromtimestamp(values[-1],timezone.utc).isoformat(),
            "observed_gap_median_minutes": statistics.median(gaps) if gaps else None,
            "observed_gap_max_minutes": max(gaps) if gaps else None,
            "configured_15min_slots_if_full_day": 96 if day == full_day else None,
            "snapshot_fraction_of_configured_slots_if_full_day":
                round(len(values)/96, 4) if day == full_day else None,
            "interpretation": "Observed generated snapshots, not a count of scheduled GitHub jobs.",
        })
    bywin = []
    for secs in sorted(windows):
        data = compare(events, snapshots, max_age_seconds=secs)
        counts = data["join_status_counts"]
        buys = data["buy_sent_join_status_counts"]
        bywin.append({
            "max_shadow_age_seconds": secs,
            "machine_events": len(events),
            "machine_events_asof_matched": counts.get("ASOF_MATCH", 0),
            "machine_events_asof_matched_pct": round(100*counts.get("ASOF_MATCH",0)/len(events),2) if events else None,
            "machine_buys": data["n_machine_buy_sent"],
            "machine_buys_asof_matched": buys.get("ASOF_MATCH",0),
            "machine_buys_asof_matched_pct": round(100*buys.get("ASOF_MATCH",0)/data["n_machine_buy_sent"],2) if data["n_machine_buy_sent"] else None,
        })
    status = Counter(e["decision_type"] for e in events)
    return {
        "schema": "solaire_dl_cadence_audit_v1",
        "research_only": True,
        "machine_decision_counts": dict(status),
        "shadow_snapshot_count": len(snapshots),
        "daily_shadow_generated_observations": daily,
        "time_window_sensitivity": bywin,
        "actual_github_schedule_run_counts_included": False,
        "generated_not_verified_published": True,
        "causal_filtering_verified": False,
        "actual_order_fills_verified": 0,
        "paired_net_pnl_eur": None,
        "limitations": [
            "A scheduled GitHub run may not correspond to a published shadow; compare Actions run logs separately.",
            "A generated snapshot is not proof of its GitHub publication time.",
            "One shadow on a separate V4 input is not a same-signal direct-policy evaluation.",
            "More permissive freshness is sensitivity only, NOT proof old DL states remain relevant.",
        ]
    }

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--machine", default="production_direct_decision_journal.json")
    parser.add_argument("--decision-history", default="decision_history")
    parser.add_argument("--full-day-utc", default=None, help="ISO YYYY-MM-DD date known to be complete")
    parser.add_argument("--output", help="optional research JSON path")
    parser.add_argument("--compare-periods", nargs=4, metavar=("BASE_FROM","BASE_TO","LATER_FROM","LATER_TO"), help="Optional exploratory comparison of two completed UTC date periods")
    args = parser.parse_args(argv)
    try:
        source=json.loads(Path(args.machine).read_text(encoding="utf-8"))
        events=read_events(source)
        snaps, bad=load_shadow_snapshots(args.decision_history,{e["market"] for e in events})
        report=summarize_cadence(events, snaps, full_day=args.full_day_utc)
        report["unreadable_snapshot_counts"]=bad
        if args.compare_periods:
            report["cadence_shift_diagnostic"]=diagnose_calendar_shift(report["daily_shadow_generated_observations"],*args.compare_periods)
        if args.output:
            Path(args.output).write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
        return 0
    except (EvidenceError,OSError,ValueError) as exc:
        parser.exit(2, "CADENCE_EVIDENCE_REJECTED: "+str(exc)+"\n")

if __name__ == "__main__":
    raise SystemExit(main())
