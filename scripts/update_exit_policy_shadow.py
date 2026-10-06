#!/usr/bin/env python3
"""Prospective shadow of alternative exit policies for delivered Solaire BUYs.

Replays recent BUY_SENT recommendations over closed 5m candles and compares the
current TP1/stop plan with candidate exit policies identified by the historical
audit. Measurement only: no email, position or production decision is changed.
"""
from __future__ import annotations
import json, math, statistics, sys, time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient

JOURNAL="production_decision_journal.json"
DIRECT_JOURNAL="production_direct_decision_journal.json"
STATE="production_exit_policy_shadow_state.json"
OUT_JOURNAL="production_exit_policy_shadow_journal.json"
STATUS="production_exit_policy_shadow_status.json"
FEE_RATE=0.0015
LOOKBACK=30*3600
HORIZONS=(4,12,24)
STUDY_ID="tp_r_grid_post_priority2_20260922"
STUDY_START_UTC="2026-09-22T18:54:05+00:00"
CHECKPOINT_COMPLETE_4H=30
DECISION_COMPLETE_12H=50
STOP_STUDY_ID="phase_aware_2x5m_hard_1_75r_20261006"
STOP_CHECKPOINT_COMPLETE_4H=10
STOP_DECISION_COMPLETE_12H=25
STOP_DEFERRED_PHASES={"MIXED_1H","EXPANSION_1H"}
STOP_HARD_R=1.75
POLICIES={
    "current_tp1_stop":{"target_r":None},
    "full_1_4r":{"target_r":1.4},
    "full_1_5r":{"target_r":1.5},
    "full_1_6r":{"target_r":1.6},
}

def med(xs):
    xs=[x for x in xs if x is not None and math.isfinite(x)]
    return round(statistics.median(xs),4) if xs else None

def avg(xs):
    xs=[x for x in xs if x is not None and math.isfinite(x)]
    return round(sum(xs)/len(xs),4) if xs else None

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

def _sim_stop_policy(entry,stop,start_ts,bars,horizon,phase,deferred):
    """Isolate stop behaviour; profit-taking is intentionally not modelled here."""
    risk=entry-stop
    if risk<=0:return None
    first=((int(start_ts*1000)//300_000)+1)*300_000
    end=int((start_ts+horizon*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs:return None
    hard=entry-STOP_HARD_R*risk
    eligible=phase in STOP_DEFERRED_PHASES
    exit_px=None;reason=None;consecutive=0
    for t,o,h,l,close,v in xs:
        if not deferred or not eligible:
            if l<=stop:
                exit_px=stop;reason="STRUCTURAL_STOP_TOUCH";break
            continue
        if l<=hard:
            exit_px=hard;reason="HARD_STOP_1_75R";break
        consecutive=consecutive+1 if close<=stop else 0
        if consecutive>=2:
            exit_px=close;reason="TWO_CONSECUTIVE_5M_CLOSES_BELOW_STOP";break
    if exit_px is None:
        exit_px=xs[-1][4];reason="HORIZON_CLOSE"
    gross=(exit_px/entry-1)*100
    net=gross-2*FEE_RATE*100
    complete=xs[-1][0]/1000>=start_ts+horizon*3600-600
    return {
        "gross_return_pct":round(gross,4),
        "net_return_pct_est":round(net,4),
        "r_multiple":round((exit_px-entry)/risk,4),
        "exit_reason":reason,
        "soft_stop_eur":stop,
        "hard_stop_eur":round(hard,12),
        "phase_at_entry":phase,
        "deferred_confirmation_eligible":eligible,
        "bars_used":len(xs),
        "complete_horizon":bool(complete),
        "intrabar_convention":"HARD_STOP_BEFORE_CLOSE_CONFIRMATION",
        "measurement_scope":"STOP_ONLY_PROFIT_MANAGEMENT_UNCHANGED",
    }

def _stop_summary(rows,h):
    pairs=[]
    for r in rows:
        base=(r.get("stop_policies") or {}).get("touch",{}).get(str(h))
        cand=(r.get("stop_policies") or {}).get("phase_aware_2x5m_hard_1_75r",{}).get(str(h))
        if not base or not cand or not base.get("complete_horizon") or not cand.get("complete_horizon"):
            continue
        a=finite(base.get("net_return_pct_est"));b=finite(cand.get("net_return_pct_est"))
        if a is None or b is None:continue
        pairs.append((r,a,b))
    deltas=[b-a for _,a,b in pairs]
    return {
        "n":len(pairs),
        "phase_counts":{
            phase:sum((r.get("context") or {}).get("short_term_phase")==phase for r,_,_ in pairs)
            for phase in ("PULLBACK_1H","MIXED_1H","EXPANSION_1H")
        },
        "baseline_stop_exits":sum(a_row.get("exit_reason")=="STRUCTURAL_STOP_TOUCH"
            for r,_,_ in pairs
            for a_row in [(r.get("stop_policies") or {}).get("touch",{}).get(str(h),{})]),
        "candidate_hard_stop_exits":sum(c_row.get("exit_reason")=="HARD_STOP_1_75R"
            for r,_,_ in pairs
            for c_row in [(r.get("stop_policies") or {}).get("phase_aware_2x5m_hard_1_75r",{}).get(str(h),{})]),
        "candidate_confirmed_exits":sum(c_row.get("exit_reason")=="TWO_CONSECUTIVE_5M_CLOSES_BELOW_STOP"
            for r,_,_ in pairs
            for c_row in [(r.get("stop_policies") or {}).get("phase_aware_2x5m_hard_1_75r",{}).get(str(h),{})]),
        "candidate_held_to_horizon":sum(c_row.get("exit_reason")=="HORIZON_CLOSE"
            for r,_,_ in pairs
            for c_row in [(r.get("stop_policies") or {}).get("phase_aware_2x5m_hard_1_75r",{}).get(str(h),{})]),
        "improved":sum(d>1e-9 for d in deltas),
        "worsened":sum(d<-1e-9 for d in deltas),
        "ties":sum(abs(d)<=1e-9 for d in deltas),
        "mean_delta_net_return_pct_points":avg(deltas),
        "median_delta_net_return_pct_points":med(deltas),
        "sum_delta_net_pnl_eur_est":round(sum(
            finite(r.get("stake_eur"),0)*(b-a)/100 for r,a,b in pairs
        ),2),
    }

def _row_key(r):
    # Market + decision timestamp is stable across canonical/direct journal
    # representations; alert_id may be absent on older retained rows.
    return "|".join([
        str(r.get("market") or ""),
        str(round(finite(r.get("decision_ts"),0),3)),
    ])

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

def _pairwise(rows,a,b,h):
    pairs=[]
    for r in rows:
        za=(r.get("policies") or {}).get(a,{}).get(str(h))
        zb=(r.get("policies") or {}).get(b,{}).get(str(h))
        if not za or not zb or not za.get("complete_horizon") or not zb.get("complete_horizon"):
            continue
        da=finite(za.get("net_return_pct_est"))
        db=finite(zb.get("net_return_pct_est"))
        if da is None or db is None:
            continue
        stake=finite(r.get("stake_eur"),0)
        pairs.append((da,db,stake))
    deltas=[(a_ret-b_ret) for a_ret,b_ret,_ in pairs]
    return {
        "n":len(pairs),
        "a_wins":sum(d>1e-9 for d in deltas),
        "b_wins":sum(d<-1e-9 for d in deltas),
        "ties":sum(abs(d)<=1e-9 for d in deltas),
        "median_delta_net_return_pct_a_minus_b":med(deltas),
        "sum_delta_net_pnl_eur_est_a_minus_b":round(
            sum(stake*(a_ret-b_ret)/100 for a_ret,b_ret,stake in pairs),2
        ),
    }

def _candidate_pairwise(rows):
    names=("full_1_4r","full_1_5r","full_1_6r")
    out={}
    for h in HORIZONS:
        out[str(h)]={}
        for i,a in enumerate(names):
            for b in names[i+1:]:
                out[str(h)][a+"_vs_"+b]=_pairwise(rows,a,b,h)
    return out

def main():
    now=time.time()
    state=read_json(STATE,{})
    study_start_ts=datetime.fromisoformat(STUDY_START_UTC).timestamp()
    if state.get("study_id")!=STUDY_ID:
        state={
            "schema":"solaire_exit_policy_shadow_state_v3",
            "study_id":STUDY_ID,
            "started_ts":study_start_ts,
            "started_at_utc":STUDY_START_UTC,
            "reset_reason":"POST_PRIORITY2_FREEZE",
        }
    else:
        state["schema"]="solaire_exit_policy_shadow_state_v3"
    prospective_start=finite(state.get("started_ts"),study_start_ts)

    stop_state=state.get("stop_confirmation_study")
    if not isinstance(stop_state,dict) or stop_state.get("study_id")!=STOP_STUDY_ID:
        stop_state={
            "study_id":STOP_STUDY_ID,
            "started_ts":now,
            "started_at_utc":utc(now),
            "policy":"PHASE_AWARE_2X5M_HARD_1_75R",
            "research_only":True,
        }
        state["stop_confirmation_study"]=stop_state
    stop_start=finite(stop_state.get("started_ts"),now)

    sources=[
        ("canonical",read_json(JOURNAL,{})),
        ("direct",read_json(DIRECT_JOURNAL,{})),
    ]
    buys=[];seen=set()
    for source_name,src in sources:
        for e in src.get("entries",[]) or []:
            if e.get("decision_type")!="BUY_SENT":
                continue
            decision_ts=finite(e.get("decision_ts"),0)
            if now-decision_ts>LOOKBACK:
                continue
            if not (finite(e.get("entry_eur")) and finite(e.get("stop_eur")) and finite(e.get("tp1_eur"))):
                continue
            key=e.get("alert_id") or "|".join([
                str(e.get("cycle_id") or ""),
                str(e.get("market") or ""),
                str(round(decision_ts,3)),
                str(e.get("entry_eur") or ""),
            ])
            if key in seen:
                continue
            seen.add(key)
            row=dict(e)
            row["_source_journal"]=source_name
            buys.append(row)
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
                    "alert_id":e.get("alert_id"),"source_journal":e.get("_source_journal"),
                    "entry_eur":entry,"stop_eur":stop,"tp1_eur":tp1,"stake_eur":finite(e.get("stake_eur"),0),
                    "risk_pct":round(risk/entry*100,4),"original_tp1_r":round((tp1-entry)/risk,4) if risk>0 else None,
                    "signal_score":finite(e.get("signal_score")),"context":e.get("context") or {},"policies":{},
                    "stop_policies":{"touch":{},"phase_aware_2x5m_hard_1_75r":{}},
                }
                for name,p in POLICIES.items():
                    row["policies"][name]={str(h):_sim(entry,stop,tp1,row["decision_ts"],cache[m],h,p["target_r"]) for h in HORIZONS}
                phase=(row.get("context") or {}).get("short_term_phase")
                for h in HORIZONS:
                    row["stop_policies"]["touch"][str(h)]=_sim_stop_policy(
                        entry,stop,row["decision_ts"],cache[m],h,phase,False
                    )
                    row["stop_policies"]["phase_aware_2x5m_hard_1_75r"][str(h)]=_sim_stop_policy(
                        entry,stop,row["decision_ts"],cache[m],h,phase,True
                    )
                rows.append(row)
            except Exception as exc:
                errors.append({"market":m,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        errors.append({"reason":type(exc).__name__+":"+str(exc)})

    # Retain completed prospective observations across the 30h live-fetch window.
    # New rows replace the same decision; older rows stay in the measurement
    # journal instead of disappearing before readiness can accumulate.
    prior=read_json(OUT_JOURNAL,{})
    retained={
        _row_key(r):r
        for r in prior.get("trades",[]) or []
        if isinstance(r,dict) and r.get("market") and finite(r.get("decision_ts")) is not None
    }
    for r in rows:
        retained[_row_key(r)]=r
    rows=sorted(retained.values(),key=lambda r:finite(r.get("decision_ts"),0))[-1200:]

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

    candidate_pairwise=_candidate_pairwise(rows)
    prospective_candidate_pairwise=_candidate_pairwise(prospective_rows)
    complete_4h=min(prospective_summary["4"][p]["n"] for p in POLICIES)
    complete_12h=min(prospective_summary["12"][p]["n"] for p in POLICIES)
    readiness={
        "complete_4h":complete_4h,
        "complete_12h":complete_12h,
        "checkpoint_complete_4h_target":CHECKPOINT_COMPLETE_4H,
        "decision_complete_12h_target":DECISION_COMPLETE_12H,
        "checkpoint_ready":complete_4h>=CHECKPOINT_COMPLETE_4H,
        "decision_ready":complete_12h>=DECISION_COMPLETE_12H,
    }

    stop_rows=[r for r in rows if finite(r.get("decision_ts"),0)>=stop_start]
    stop_summary={str(h):_stop_summary(stop_rows,h) for h in HORIZONS}
    stop_complete_4h=stop_summary["4"]["n"]
    stop_complete_12h=stop_summary["12"]["n"]
    stop_readiness={
        "complete_4h":stop_complete_4h,
        "complete_12h":stop_complete_12h,
        "checkpoint_complete_4h_target":STOP_CHECKPOINT_COMPLETE_4H,
        "decision_complete_12h_target":STOP_DECISION_COMPLETE_12H,
        "checkpoint_ready":stop_complete_4h>=STOP_CHECKPOINT_COMPLETE_4H,
        "decision_ready":stop_complete_12h>=STOP_DECISION_COMPLETE_12H,
    }

    journal={
        "schema":"solaire_exit_policy_shadow_journal_v3","updated_at_utc":utc(now),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "fee_assumption_per_side":FEE_RATE,"policies":POLICIES,
        "study_id":state.get("study_id"),
        "prospective_started_at_utc":state.get("started_at_utc"),
        "source_journals":[JOURNAL,DIRECT_JOURNAL],
        "stop_confirmation_study":{
            "study_id":STOP_STUDY_ID,
            "started_at_utc":stop_state.get("started_at_utc"),
            "policy":"PHASE_AWARE_2X5M_HARD_1_75R",
            "deferred_phases":sorted(STOP_DEFERRED_PHASES),
            "hard_stop_r":STOP_HARD_R,
            "measurement_scope":"STOP_ONLY_PROFIT_MANAGEMENT_UNCHANGED",
        },
        "trades":rows,
    }
    status={
        "schema":"solaire_exit_policy_shadow_v3","checked_at_utc":utc(now),
        "status":"OK" if not errors else "DEGRADED_NONBLOCKING",
        "tracked_buys":len(rows),
        "study_id":state.get("study_id"),
        "prospective_started_at_utc":state.get("started_at_utc"),
        "prospective_tracked_buys":len(prospective_rows),
        "summary":summary,
        "prospective_summary":prospective_summary,
        "comparisons_vs_current":comparisons,
        "prospective_comparisons_vs_current":prospective_comparisons,
        "candidate_pairwise":candidate_pairwise,
        "prospective_candidate_pairwise":prospective_candidate_pairwise,
        "decision_readiness":readiness,
        "direct_journal_available":Path(DIRECT_JOURNAL).exists(),
        "direct_source_buys":sum(r.get("source_journal")=="direct" for r in rows),
        "stop_confirmation_shadow":{
            "study_id":STOP_STUDY_ID,
            "started_at_utc":stop_state.get("started_at_utc"),
            "policy":"PHASE_AWARE_2X5M_HARD_1_75R",
            "deferred_phases":sorted(STOP_DEFERRED_PHASES),
            "fallback_policy":"IMMEDIATE_STRUCTURAL_STOP_FOR_PULLBACK_OR_UNKNOWN_PHASE",
            "hard_stop_r":STOP_HARD_R,
            "measurement_scope":"STOP_ONLY_PROFIT_MANAGEMENT_UNCHANGED",
            "prospective_tracked_buys":len(stop_rows),
            "summary":stop_summary,
            "decision_readiness":stop_readiness,
            "affects_position_management":False,
        },
        "errors":errors,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    state["updated_at_utc"]=utc(now)
    atomic_json(STATE,state);atomic_json(OUT_JOURNAL,journal);atomic_json(STATUS,status)
    print("SOLAIRE_EXIT_POLICY_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__":raise SystemExit(main())
