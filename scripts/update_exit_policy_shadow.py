#!/usr/bin/env python3
"""Prospective shadow of alternative exit policies for delivered Solaire BUYs.

Replays recent BUY_SENT recommendations over closed 5m candles and compares the
current TP1/stop plan with candidate exit policies identified by the historical
audit. Measurement only: no email, position or production decision is changed.
"""
from __future__ import annotations
import json, math, statistics, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient

JOURNAL="production_decision_journal.json"
STATE="production_exit_policy_shadow_state.json"
OUT_JOURNAL="production_exit_policy_shadow_journal.json"
STATUS="production_exit_policy_shadow_status.json"
FEE_RATE=0.0015
LOOKBACK=30*3600
HORIZONS=(4,12,24)
POLICIES={
    "current_tp1_stop":{"target_r":None},
    "full_1_4r":{"target_r":1.4},
    "full_1_5r":{"target_r":1.5},
    "full_1_6r":{"target_r":1.6},
}

def med(xs):
    xs=[x for x in xs if x is not None and math.isfinite(x)]
    return round(statistics.median(xs),4) if xs else None

def _bars(raw,now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6:continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals):continue
        t,o,h,l,c,v=vals
        if t+300_000<=now*1000:out.append((int(t),o,h,l,c,v))
    return sorted(out)

def _sim(entry,stop,tp1,start_ts,bars,horizon,target_r):
    risk=entry-stop
    if risk<=0:return None
    target=tp1 if target_r is None else entry+target_r*risk
    first=((int(start_ts*1000)//300_000)+1)*300_000
    end=int((start_ts+horizon*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs:return None
    exit_px=None;reason=None
    for t,o,h,l,c,v in xs:
        if l<=stop:
            exit_px=stop;reason="STOP";break
        if h>=target:
            exit_px=target;reason="TARGET";break
    if exit_px is None:
        exit_px=xs[-1][4];reason="HORIZON_CLOSE"
    gross=(exit_px/entry-1)*100
    net=gross-2*FEE_RATE*100
    complete=xs[-1][0]/1000>=start_ts+horizon*3600-600
    return {
        "gross_return_pct":round(gross,4),"net_return_pct_est":round(net,4),
        "r_multiple":round((exit_px-entry)/risk,4),
        "exit_reason":reason,"target_eur":target,
        "bars_used":len(xs),"complete_horizon":bool(complete),
        "intrabar_convention":"LOW_BEFORE_HIGH_CONSERVATIVE",
    }

def _summary(rows,policy,h):
    xs=[]
    for r in rows:
        z=(r.get("policies") or {}).get(policy,{}).get(str(h))
        if z and z.get("complete_horizon"):xs.append((r,z))
    return {
        "n":len(xs),
        "positive_net":sum(z["net_return_pct_est"]>0 for _,z in xs),
        "negative_net":sum(z["net_return_pct_est"]<0 for _,z in xs),
        "median_net_return_pct":med([z["net_return_pct_est"] for _,z in xs]),
        "median_r_multiple":med([z["r_multiple"] for _,z in xs]),
        "sum_net_pnl_eur_est":round(sum((r.get("stake_eur") or 0)*z["net_return_pct_est"]/100 for r,z in xs),2),
        "target_exits":sum(z["exit_reason"]=="TARGET" for _,z in xs),
        "stop_exits":sum(z["exit_reason"]=="STOP" for _,z in xs),
    }

def main():
    now=time.time()
    state=read_json(STATE,{})
    if finite(state.get("started_ts")) is None:
        state={
            "schema":"solaire_exit_policy_shadow_state_v2",
            "started_ts":now,
            "started_at_utc":utc(now),
        }
    else:
        state["schema"]="solaire_exit_policy_shadow_state_v2"
    prospective_start=finite(state.get("started_ts"),now)

    src=read_json(JOURNAL,{})
    buys=[e for e in src.get("entries",[]) or []
          if e.get("decision_type")=="BUY_SENT"
          and now-finite(e.get("decision_ts"),0)<=LOOKBACK
          and finite(e.get("entry_eur")) and finite(e.get("stop_eur")) and finite(e.get("tp1_eur"))]
    buys.sort(key=lambda e:e.get("decision_ts",0))

    rows=[];errors=[];cache={}
    client=PublicClient(timeout=10,retries=2,requests_per_second=8)
    try:
        client.get("/time",cache=False)
        for e in buys:
            m=e["market"]
            try:
                if m not in cache:
                    cache[m]=_bars(client.get("/"+m+"/candles",{"interval":"5m","limit":400},cache=False),now)
                entry=finite(e.get("entry_eur"));stop=finite(e.get("stop_eur"));tp1=finite(e.get("tp1_eur"))
                risk=entry-stop
                row={
                    "market":m,"decision_at_utc":e.get("cycle_id"),"decision_ts":finite(e.get("decision_ts")),
                    "entry_eur":entry,"stop_eur":stop,"tp1_eur":tp1,"stake_eur":finite(e.get("stake_eur"),0),
                    "risk_pct":round(risk/entry*100,4),"original_tp1_r":round((tp1-entry)/risk,4) if risk>0 else None,
                    "signal_score":finite(e.get("signal_score")),"context":e.get("context") or {},"policies":{},
                }
                for name,p in POLICIES.items():
                    row["policies"][name]={str(h):_sim(entry,stop,tp1,row["decision_ts"],cache[m],h,p["target_r"]) for h in HORIZONS}
                rows.append(row)
            except Exception as exc:
                errors.append({"market":m,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        errors.append({"reason":type(exc).__name__+":"+str(exc)})

    summary={str(h):{p:_summary(rows,p,h) for p in POLICIES} for h in HORIZONS}
    prospective_rows=[r for r in rows if finite(r.get("decision_ts"),0)>=prospective_start]
    prospective_summary={str(h):{p:_summary(prospective_rows,p,h) for p in POLICIES} for h in HORIZONS}

    comparisons={}
    for h in HORIZONS:
        k=str(h);comparisons[k]={}
        for p in POLICIES:
            if p=="current_tp1_stop":continue
            a=summary[k]["current_tp1_stop"];b=summary[k][p]
            comparisons[k][p]={
                "delta_sum_net_pnl_eur_est":round(b["sum_net_pnl_eur_est"]-a["sum_net_pnl_eur_est"],2),
                "delta_median_net_return_pct":None if a["median_net_return_pct"] is None or b["median_net_return_pct"] is None else round(b["median_net_return_pct"]-a["median_net_return_pct"],4),
            }

    prospective_comparisons={}
    for h in HORIZONS:
        k=str(h);prospective_comparisons[k]={}
        for p in POLICIES:
            if p=="current_tp1_stop":continue
            a=prospective_summary[k]["current_tp1_stop"];b=prospective_summary[k][p]
            prospective_comparisons[k][p]={
                "delta_sum_net_pnl_eur_est":round(b["sum_net_pnl_eur_est"]-a["sum_net_pnl_eur_est"],2),
                "delta_median_net_return_pct":None if a["median_net_return_pct"] is None or b["median_net_return_pct"] is None else round(b["median_net_return_pct"]-a["median_net_return_pct"],4),
            }

    journal={
        "schema":"solaire_exit_policy_shadow_journal_v2","updated_at_utc":utc(now),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "fee_assumption_per_side":FEE_RATE,"policies":POLICIES,
        "prospective_started_at_utc":state.get("started_at_utc"),
        "trades":rows,
    }
    status={
        "schema":"solaire_exit_policy_shadow_v2","checked_at_utc":utc(now),
        "status":"OK" if not errors else "DEGRADED_NONBLOCKING",
        "tracked_buys":len(rows),
        "prospective_started_at_utc":state.get("started_at_utc"),
        "prospective_tracked_buys":len(prospective_rows),
        "summary":summary,
        "prospective_summary":prospective_summary,
        "comparisons_vs_current":comparisons,
        "prospective_comparisons_vs_current":prospective_comparisons,
        "errors":errors,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    state["updated_at_utc"]=utc(now)
    atomic_json(STATE,state);atomic_json(OUT_JOURNAL,journal);atomic_json(STATUS,status)
    print("SOLAIRE_EXIT_POLICY_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__":raise SystemExit(main())
