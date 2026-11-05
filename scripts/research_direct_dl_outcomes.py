#!/usr/bin/env python3
"""Pilot: past true DIRECT BUY_SENT vs previous generated DL state + future marks.

Reports potential missed upward moves and potential avoided downside as
strict historical price references, NOT orders/fills/net economic PnL.
The DL snapshot publication time and same-input causality remain UNVERIFIED.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.http import PublicClient
from scripts.compare_direct_decision_shadow import read_events, load_shadow_snapshots, compare
from scripts.research_dl_price_paths import inspect_one, HORIZONS

SCHEMA="solaire_direct_dl_previous_shadow_price_reference_v1"

def valid_num(v):
    return type(v) in (float,int) and math.isfinite(v) and v>0

def candidates(raw, shadow_dir, max_shadow_age_seconds=900):
    """Build BEFORE future price lookup. Only exact IDs + same-market as-of links."""
    events=read_events(raw)
    books={e["decision_id"]:e for e in raw["entries"]}
    snapshots,corrupt=load_shadow_snapshots(shadow_dir,{e["market"] for e in events})
    observed=compare(events,snapshots,max_age_seconds=max_shadow_age_seconds)
    accepted=[]
    unusable=Counter()
    for row in observed["rows"]:
        if row["machine_action"]!="BUY_SENT":
            continue
        if row["join_status"]!="ASOF_MATCH":
            unusable[row["join_status"]]+=1
            continue
        original=books.get(row["decision_id"])
        if not isinstance(original,dict) or row["signal_id"]!=original.get("signal_id"):
            unusable["ID_MISMATCH"]+=1
            continue
        reference=original.get("signal_price_eur")
        if not valid_num(reference):
            unusable["NO_POSITIVE_SIGNAL_MARK"]+=1
            continue
        stop=original.get("stop_eur")
        tp1=original.get("tp1_eur")
        accepted.append({
            "market":row["market"],"decision_id":row["decision_id"],
            "signal_id":row["signal_id"],"episode_id":row["episode_id"],
            "scan_ts":row["machine_ts"],
            "scan_at_utc":datetime.fromtimestamp(row["machine_ts"],timezone.utc).isoformat(),
            "scan_id":row["decision_id"],
            "scan_price_eur":float(reference),
            "baseline_v4_available":False,
            "stop_eur":float(stop) if valid_num(stop) else None,
            "tp1_eur":float(tp1) if valid_num(tp1) else None,
            "dl_action_at_previous_generated_snapshot":row["shadow_action"],
            "dl_snapshot_generated_age_seconds":row["shadow_age_seconds"],
            "source_model_entry_limit_eur":original.get("entry_eur"),
        })
    return sorted(accepted,key=lambda x:(x["scan_ts"],x["market"],x["decision_id"])),{
        "n_direct_events":len(events),"n_direct_buy_sent":observed["n_machine_buy_sent"],
        "n_time_matched_buy_sent":len(accepted),
        "unmatched_or_unusable":dict(sorted(unusable.items())),
        "n_shadow_snapshots":len(snapshots),
        "invalid_shadow_archives":corrupt,
    }

def select_due(events,asof,max_per_horizon=6):
    if type(max_per_horizon) is not int or not 1<=max_per_horizon<=15:
        raise ValueError("max_per_horizon must be in 1..15")
    selection=[]
    for horizon in HORIZONS:
        # Prospective frozen policy: earliest matured alert per market, no
        # knowledge of its outcome enters selection.
        seen=set()
        for e in events:
            if e["scan_ts"]+horizon*3600+300>asof:
                continue
            market=e["market"]
            if market in seen:
                continue
            seen.add(market)
            selection.append({**e,"hours":horizon})
            if len(seen)>=max_per_horizon:
                break
    return selection

def inspect(raw,shadow_dir,client,asof,max_per_horizon=6):
    events,source=candidates(raw,shadow_dir)
    picked=select_due(events,asof,max_per_horizon)
    observations=[]
    for event in picked:
        result=inspect_one(event,client,asof)
        # No learned after-the-fact buying action. Keep untrusted generated
        # DL class, earlier source and plan price separate.
        result.update({
            "decision_id":event["decision_id"],
            "signal_id":event["signal_id"],
            "dl_prior_generated_action":event["dl_action_at_previous_generated_snapshot"],
            "dl_snapshot_generated_age_seconds":event["dl_snapshot_generated_age_seconds"],
            "source_model_entry_limit_eur":event["source_model_entry_limit_eur"],
            "planned_stop_eur":event["stop_eur"],
            "planned_tp1_eur":event["tp1_eur"],
            "actual_position_filled":False,
            "dl_published_by_signal_verified":False,
            "same_input_policy_causality_verified":False,
        })
        observations.append(result)
    strata=[]
    for h in HORIZONS:
        for action in sorted({z["dl_prior_generated_action"] for z in observations if z["horizon_hours"]==h}):
            cohort=[x for x in observations if x["horizon_hours"]==h and x["dl_prior_generated_action"]==action]
            complete=[x for x in cohort if x["status"]=="COMPLETE"]
            strata.append({
                "hours":h,"previous_dl_action":action,
                "n_observed":len(cohort),
                "n_strict_complete":len(complete),
                "n_incomplete":sum(x["status"]=="INCOMPLETE" for x in cohort),
                "n_source_errors":sum(x["status"]=="SOURCE_ERROR" for x in cohort),
                "reference_mfe_ge10_n":sum(x["mfe_pct"]>=10 for x in complete),
                "reference_mae_le_minus5_n":sum(x["mae_pct"]<=-5 for x in complete),
                "reference_stop_touch_first_n":sum(x["path_touch_result"] in {"STOP","STOP_SAME_BAR_CONSERVATIVE"} for x in complete),
                "reference_tp_first_n":sum(x["path_touch_result"]=="TP1" for x in complete),
                "indicative_80pct_coverage_n":sum(x.get("indicative_no_trade_gap_reference") is True for x in cohort),
                "trade_pnl_eur":None,
            })
    return {
        "schema":SCHEMA,
        "asof_utc":datetime.fromtimestamp(asof,timezone.utc).isoformat(),
        "selection_rule":"EARLIEST_MATURED_PRIOR-DL-MATCHED_DIRECT_BUY_PER_DISTINCT_MARKET_EACH_HORIZON",
        "max_shadow_age_seconds":900,
        "input":source,
        "matured_sample_size":len(observations),
        "summary_by_prior_dl_action":strata,
        "results":observations,
        "rejected_direct_events_included":False,
        "shadow_decision_published_at_buy_proven":False,
        "same_signal_causal_A_B":False,
        "orders_traded":0,"net_portfolio_pnl_eur":None,
        "evidence_class":"OBSERVED_AFTER_PRICE_REFERENCE_ONLY",
        "limitations":[
            "This is TRUE machine BUY_SENT, not an order fill or proof the human received the email.",
            "DL class generated before sender, but Git publication/delivery time is not verified.",
            "DL uses V4 baseline features from a DIFFERENT scan and not the same direct production inputs.",
            "Snapshot signal-price reference is NOT actual ask fill or entry-limit fulfillment.",
            "Price paths use public last-trade candles; missing bars remain censored.",
            "Planned stop/TP touches are conservative reference events, not sell execution.",
            "Population is limited to as-of matched machine buys; selection bias remains.",
            "Not a comparison of DIRECT vs DIRECT+DL realized profitability.",
        ],
    }

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source",default="production_direct_decision_journal.json")
    p.add_argument("--decision-history",default="decision_history")
    p.add_argument("--output",default="/tmp/direct-dl-price-reference.json")
    p.add_argument("--max-per-horizon",type=int,default=6)
    opt=p.parse_args(argv)
    try:
        now=time.time()
        source=json.loads(Path(opt.source).read_text(encoding="utf8"))
        client=PublicClient(timeout=9,retries=1,requests_per_second=2)
        result=inspect(source,opt.decision_history,client,now,opt.max_per_horizon)
        Path(opt.output).write_text(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
        print(json.dumps({k:v for k,v in result.items() if k!="results"},ensure_ascii=False,sort_keys=True))
        return 0
    except (ValueError,OSError) as e:
        print("DIRECT_DL_RESEARCH_ERROR:"+str(e),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
