#!/usr/bin/env python3
"""Audit exit-management policies on BUY emails actually delivered by Solaire.

Uses production_decision_journal BUY_SENT entries and replays subsequent 5m
Bitvavo candles chronologically. Compares the current stop/TP1 proxy with
alternative profit-protection policies while keeping entries unchanged.

Research-only. No production signal, BUY gate, email or execution behavior is
changed.

Intrabar convention for long trades is deliberately conservative: within a
single 5m candle, the low is assumed to occur before the high. Therefore an
existing stop wins over a newly reached profit trigger if both occur in the
same bar. New break-even/trailing stops become active on the next bar.
"""
from __future__ import annotations
import json, math, statistics, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient

JOURNAL="production_decision_journal.json"
OUT="research/solaire_exit_management_20260922.json"
WINDOW_START="2026-09-21T09:00:00+00:00"
WINDOW_END="2026-09-22T09:00:00+00:00"
FEE_RATE=0.0015
HORIZONS=(4,12,24)

POLICIES={
    "current_tp1_stop":{
        "kind":"full_target","target_r":None,"target_pct":None,"time_stop_hours":None,
    },
    "full_1r":{
        "kind":"full_target","target_r":1.0,"target_pct":None,"time_stop_hours":None,
    },
    "full_1_25r":{
        "kind":"full_target","target_r":1.25,"target_pct":None,"time_stop_hours":None,
    },
    "full_1_4r":{
        "kind":"full_target","target_r":1.4,"target_pct":None,"time_stop_hours":None,
    },
    "full_1_5r":{
        "kind":"full_target","target_r":1.5,"target_pct":None,"time_stop_hours":None,
    },
    "full_1_6r":{
        "kind":"full_target","target_r":1.6,"target_pct":None,"time_stop_hours":None,
    },
    "full_1_75r":{
        "kind":"full_target","target_r":1.75,"target_pct":None,"time_stop_hours":None,
    },
    "be_after_1r":{
        "kind":"be_then_tp1","trigger_r":1.0,
    },
    "partial50_1r_be":{
        "kind":"partial_be","trigger_r":1.0,"partial_fraction":0.5,
    },
    "partial50_plus4_be":{
        "kind":"partial_be","trigger_pct":4.0,"partial_fraction":0.5,
    },
    "partial50_plus5_be":{
        "kind":"partial_be","trigger_pct":5.0,"partial_fraction":0.5,
    },
    "partial50_plus6_be":{
        "kind":"partial_be","trigger_pct":6.0,"partial_fraction":0.5,
    },
    "trail_1r_distance_after_1r":{
        "kind":"trail","trigger_r":1.0,"trail_r":1.0,
    },
    "current_with_4h_time_stop":{
        "kind":"full_target","target_r":None,"target_pct":None,"time_stop_hours":4.0,
    },
    "partial50_1r_be_4h":{
        "kind":"partial_be","trigger_r":1.0,"partial_fraction":0.5,"time_stop_hours":4.0,
    },
}

def ts(s):
    from datetime import datetime
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def median(xs):
    xs=[x for x in xs if x is not None and math.isfinite(x)]
    return round(statistics.median(xs),4) if xs else None

def candles(raw,now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        if t+300_000<=now*1000:
            out.append((int(t),o,h,l,c,v))
    return sorted(out)

def target_price(entry,risk,tp1,policy):
    if policy.get("target_r") is not None:
        return entry + policy["target_r"]*risk
    if policy.get("target_pct") is not None:
        return entry*(1+policy["target_pct"]/100)
    return tp1

def trigger_price(entry,risk,policy):
    if policy.get("trigger_r") is not None:
        return entry + policy["trigger_r"]*risk
    if policy.get("trigger_pct") is not None:
        return entry*(1+policy["trigger_pct"]/100)
    return None

def net_return_from_legs(entry,legs):
    # legs: list[(fraction, exit_price)]
    gross=sum(frac*(px/entry-1) for frac,px in legs)
    # one entry fee on 100%, exit fee weighted across all exit legs
    exit_fee=sum(frac*FEE_RATE for frac,_ in legs)
    net=gross-FEE_RATE-exit_fee
    return gross*100,net*100

def simulate(entry,stop,tp1,bars,start_ts,horizon_hours,policy):
    risk=entry-stop
    if risk<=0:return None
    horizon_end=start_ts+horizon_hours*3600
    xs=[b for b in bars if b[0]>=((int(start_ts*1000)//300_000)+1)*300_000 and b[0]<horizon_end*1000]
    if not xs:return None

    target=target_price(entry,risk,tp1,policy)
    trigger=trigger_price(entry,risk,policy)
    active_stop=stop
    remaining=1.0
    legs=[]
    triggered=False
    max_seen=entry
    exit_reason=None
    exit_ts=None
    ambiguous_bars=0
    time_stop=policy.get("time_stop_hours")
    time_stop_ts=start_ts+time_stop*3600 if time_stop else None

    for t,o,h,l,c,v in xs:
        # existing stop first (conservative low-before-high path)
        if l<=active_stop and remaining>0:
            legs.append((remaining,active_stop)); remaining=0
            exit_reason="STOP" if active_stop<entry-1e-15 else "BREAK_EVEN_OR_TRAIL"
            exit_ts=t/1000; break

        # full target
        if policy["kind"]=="full_target":
            if h>=target and remaining>0:
                legs.append((remaining,target)); remaining=0
                exit_reason="TARGET"; exit_ts=t/1000; break

        elif policy["kind"]=="be_then_tp1":
            if h>=target and remaining>0:
                legs.append((remaining,target)); remaining=0
                exit_reason="TP1"; exit_ts=t/1000; break
            if not triggered and trigger is not None and h>=trigger:
                triggered=True
                active_stop=max(active_stop,entry)

        elif policy["kind"]=="partial_be":
            # Original TP1 remains final target for remainder.
            if triggered and h>=tp1 and remaining>0:
                legs.append((remaining,tp1)); remaining=0
                exit_reason="TP1_AFTER_PARTIAL"; exit_ts=t/1000; break
            if not triggered and trigger is not None and h>=trigger and remaining>0:
                frac=min(policy.get("partial_fraction",0.5),remaining)
                legs.append((frac,trigger)); remaining-=frac
                triggered=True
                active_stop=max(active_stop,entry)
                # no same-bar BE exit: new stop activates next bar
                if remaining<=1e-12:
                    exit_reason="PARTIAL_TRIGGER_FULL"; exit_ts=t/1000; break

        elif policy["kind"]=="trail":
            if h>=target and remaining>0:
                legs.append((remaining,target)); remaining=0
                exit_reason="TP1"; exit_ts=t/1000; break
            if not triggered and trigger is not None and h>=trigger:
                triggered=True
            if triggered:
                max_seen=max(max_seen,h)
                # updated stop is active from next candle
                active_stop=max(active_stop,max_seen-policy.get("trail_r",1.0)*risk)

        if time_stop_ts is not None and t/1000>=time_stop_ts and remaining>0:
            legs.append((remaining,c)); remaining=0
            exit_reason="TIME_STOP"; exit_ts=t/1000; break

    if remaining>0:
        # horizon mark-to-market
        px=xs[-1][4]
        legs.append((remaining,px)); remaining=0
        exit_reason="HORIZON_CLOSE"; exit_ts=xs[-1][0]/1000

    gross_pct,net_pct=net_return_from_legs(entry,legs)
    stake_return_multiple=sum(frac*(px-entry)/risk for frac,px in legs)
    return {
        "gross_return_pct":round(gross_pct,4),
        "net_return_pct_est":round(net_pct,4),
        "r_multiple":round(stake_return_multiple,4),
        "exit_reason":exit_reason,
        "exit_ts":exit_ts,
        "legs":[{"fraction":round(frac,4),"exit_eur":px} for frac,px in legs],
        "triggered_profit_protection":triggered,
        "final_stop_eur":active_stop,
        "bars_used":len(xs),
        "complete_horizon": bool(xs and xs[-1][0]/1000 >= horizon_end-600),
        "intrabar_convention":"LOW_BEFORE_HIGH_CONSERVATIVE",
    }

def aggregate(rows,policy,horizon):
    vals=[]
    for r in rows:
        x=(r.get("policies") or {}).get(policy,{}).get(str(horizon))
        if x and x.get("complete_horizon"):
            vals.append((r,x))
    return {
        "n":len(vals),
        "positive_net":sum(x["net_return_pct_est"]>0 for _,x in vals),
        "negative_net":sum(x["net_return_pct_est"]<0 for _,x in vals),
        "median_net_return_pct":median([x["net_return_pct_est"] for _,x in vals]),
        "median_r_multiple":median([x["r_multiple"] for _,x in vals]),
        "sum_gross_pnl_eur":round(sum((r.get("stake_eur") or 0)*x["gross_return_pct"]/100 for r,x in vals),2),
        "sum_net_pnl_eur_est":round(sum((r.get("stake_eur") or 0)*x["net_return_pct_est"]/100 for r,x in vals),2),
        "mean_net_return_pct":round(sum(x["net_return_pct_est"] for _,x in vals)/len(vals),4) if vals else None,
        "stop_or_be_exits":sum(x["exit_reason"] in ("STOP","BREAK_EVEN_OR_TRAIL") for _,x in vals),
        "target_exits":sum("TARGET" in x["exit_reason"] or "TP1" in x["exit_reason"] for _,x in vals),
        "time_stop_exits":sum(x["exit_reason"]=="TIME_STOP" for _,x in vals),
        "markets":[r["market"] for r,_ in vals],
    }

def main():
    now=time.time()
    journal=json.loads(Path(JOURNAL).read_text())
    start=ts(WINDOW_START); end=ts(WINDOW_END)
    buys=[e for e in journal.get("entries",[])
          if e.get("decision_type")=="BUY_SENT"
          and start<=finite(e.get("decision_ts"),0)<=end
          and finite(e.get("entry_eur")) and finite(e.get("stop_eur")) and finite(e.get("tp1_eur"))]
    buys.sort(key=lambda e:e.get("decision_ts",0))

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)

    rows=[];errors=[]
    raw_cache={}
    for e in buys:
        market=e["market"]
        try:
            if market not in raw_cache:
                raw_cache[market]=candles(client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False),now)
            bars=raw_cache[market]
            entry=finite(e.get("entry_eur")); stop=finite(e.get("stop_eur")); tp1=finite(e.get("tp1_eur"))
            risk=entry-stop
            row={
                "market":market,
                "decision_at_utc":e.get("cycle_id"),
                "decision_ts":finite(e.get("decision_ts")),
                "signal_score":finite(e.get("signal_score")),
                "entry_eur":entry,"stop_eur":stop,"tp1_eur":tp1,
                "stake_eur":finite(e.get("stake_eur"),0),
                "risk_pct":round(risk/entry*100,4),
                "tp1_r":round((tp1-entry)/risk,4) if risk>0 else None,
                "context":e.get("context") or {},
                "policies":{},
            }
            for name,policy in POLICIES.items():
                row["policies"][name]={}
                for h in HORIZONS:
                    row["policies"][name][str(h)]=simulate(entry,stop,tp1,bars,row["decision_ts"],h,policy)
            rows.append(row)
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    summary={}
    for h in HORIZONS:
        summary[str(h)]={name:aggregate(rows,name,h) for name in POLICIES}

    # Pairwise improvements vs current baseline on the same complete cohort.
    comparisons={}
    for h in HORIZONS:
        base="current_tp1_stop"
        comparisons[str(h)]={}
        for name in POLICIES:
            if name==base:continue
            diffs=[]
            for r in rows:
                a=r["policies"][base][str(h)]
                b=r["policies"][name][str(h)]
                if not a or not b or not a.get("complete_horizon") or not b.get("complete_horizon"):continue
                diffs.append({
                    "market":r["market"],
                    "delta_net_pct":round(b["net_return_pct_est"]-a["net_return_pct_est"],4),
                    "delta_r":round(b["r_multiple"]-a["r_multiple"],4),
                })
            comparisons[str(h)][name]={
                "n":len(diffs),
                "improved":sum(x["delta_net_pct"]>0 for x in diffs),
                "worsened":sum(x["delta_net_pct"]<0 for x in diffs),
                "median_delta_net_pct":median([x["delta_net_pct"] for x in diffs]),
                "sum_delta_net_pct":round(sum(x["delta_net_pct"] for x in diffs),4),
                "top_improvements":sorted(diffs,key=lambda x:x["delta_net_pct"],reverse=True)[:8],
                "top_regressions":sorted(diffs,key=lambda x:x["delta_net_pct"])[:8],
            }

    out={
        "schema":"solaire_exit_management_audit_v2",
        "generated_at_utc":utc(),
        "research_only":True,
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "window":{"start_utc":WINDOW_START,"end_utc":WINDOW_END},
        "fee_assumption_per_side":FEE_RATE,
        "buy_count":len(rows),
        "policies":POLICIES,
        "summary":summary,
        "comparisons_vs_current":comparisons,
        "trades":rows,
        "errors":errors,
        "limitations":[
            "5m OHLC cannot resolve true intrabar ordering; low-before-high is used conservatively",
            "estimated fees use 0.15% per side and exclude additional stop-market slippage",
            "recent trades may lack complete 12h/24h horizons and are excluded from those aggregate cohorts",
            "audit changes exits only; entries are the exact Solaire BUY recommendations recorded in the production journal",
        ],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_EXIT_MANAGEMENT "+json.dumps({
        "buy_count":len(rows),
        "h4":summary["4"],
        "h12":summary["12"],
        "errors":errors,
    },ensure_ascii=False))

if __name__=="__main__":
    main()
