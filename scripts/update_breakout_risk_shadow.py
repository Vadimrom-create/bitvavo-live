#!/usr/bin/env python3
"""Prospective shadow for a faster breakout-risk plan.

The production execution gate uses 15m support/ATR (8 bars ~= 2h) to place a
structural stop. During vertical breakouts that support can be far below price,
making the required stop 20-70% wide. This shadow keeps production liquidity,
spread and 15m-range requirements unchanged, but compares the current 15m risk
plan with a 5m structural plan (8 bars ~= 40m).

Measurement only. No BUY gate, email or order behavior is changed.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, freshness, read_json, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan
from scripts.send_production_buy_alert import (
    MIN_QUOTE_VOLUME_EUR, MAX_SPREAD, MAX_STOP_DISTANCE_PCT,
    MIN_15M_CONSOLIDATION_RANGE_PCT,
)

INPUT="production_alert_candidates.json"
STATE="production_breakout_risk_shadow_state.json"
JOURNAL="production_breakout_risk_shadow_journal.json"
STATUS="production_breakout_risk_shadow_status.json"
HORIZONS=(1,4)
MAX_EVENTS=3000
HQ_MIN_SCORE=6.0
HQ_MIN_EVIDENCE=4

def _closed_rows(raw,now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        t,h,l,c=finite(x[0]),finite(x[2]),finite(x[3]),finite(x[4])
        if None in (t,h,l,c): continue
        if t+300_000<=now*1000: out.append((int(t),h,l,c))
    return sorted(out)

def _eval(event,bars,h):
    t0=finite(event.get("detected_ts")); base=finite(event.get("fast_entry_eur"))
    if t0 is None or base is None or base<=0: return None
    first=((int(t0*1000)//300_000)+1)*300_000
    end=int((t0+h*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs: return None
    high=max(x[1] for x in xs); low=min(x[2] for x in xs); close=xs[-1][3]
    stop=finite(event.get("fast_stop_eur")); tp1=finite(event.get("fast_tp1_eur"))
    return {
        "horizon_hours":h,
        "mfe_pct":round((high/base-1)*100,4),
        "mae_pct":round((low/base-1)*100,4),
        "close_return_pct":round((close/base-1)*100,4),
        "stop_touched":bool(stop is not None and low<=stop),
        "tp1_touched":bool(tp1 is not None and high>=tp1),
        "intrabar_order_if_both_touched":"UNKNOWN" if stop is not None and tp1 is not None and low<=stop and high>=tp1 else None,
        "bars":len(xs),
    }

def _eligible_signal(row):
    state=row.get("signal_state")
    score=finite(row.get("signal_score")); ev=int((row.get("acceleration") or {}).get("evidence_count") or 0)
    return state=="CONFIRMED_ACCELERATION" or (
        state=="BUILDING_ACCELERATION" and score is not None and score>=HQ_MIN_SCORE and ev>=HQ_MIN_EVIDENCE
    )

def _snapshot(row,client,meta,now):
    market=row["market"]
    volume=finite(row.get("quote_volume_24h_eur"),0)
    if volume<MIN_QUOTE_VOLUME_EUR:
        return {"candidate":False,"reason":"INSUFFICIENT_EXECUTION_LIQUIDITY"}

    book=client.get("/"+market+"/book",{"depth":25},cache=False)
    bid=finite(book["bids"][0][0]) if book.get("bids") else None
    ask=finite(book["asks"][0][0]) if book.get("asks") else None
    retrieved=client.metadata("/"+market+"/book",{"depth":25}).get("retrieved_at_utc")
    if bid is None or ask is None or not 0<bid<=ask:
        return {"candidate":False,"reason":"INVALID_BOOK"}
    spread=ask/bid-1
    if spread>MAX_SPREAD:
        return {"candidate":False,"reason":"SPREAD_TOO_WIDE","spread_pct":spread*100}

    r15=client.get("/"+market+"/candles",{"interval":"15m","limit":100},cache=False)
    f15=describe(closed_candles(r15,"15m",now),"15m")
    fresh=freshness(now=now,retrieved=retrieved,candle_start_ms=f15.get("last_closed_start_ms"),interval="15m",max_retrieval_age=90)
    if not f15.get("valid") or not fresh["ok"]:
        return {"candidate":False,"reason":"STALE_OR_INVALID_STRUCTURE","spread_pct":spread*100}
    rng=finite(f15.get("consolidation_range_pct"))
    if rng is None or rng<MIN_15M_CONSOLIDATION_RANGE_PCT:
        return {"candidate":False,"reason":"STRUCTURAL_RANGE_TOO_NARROW","spread_pct":spread*100,"range_15m_pct":rng}

    current=structural_plan({**row,"ask":ask},f15,meta[market])
    current_stop=finite(current.get("stop_distance_pct"))
    current_pass=bool(current.get("valid") and current_stop is not None and current_stop<=MAX_STOP_DISTANCE_PCT)
    if current_pass:
        return {
            "candidate":False,"reason":"CURRENT_15M_PLAN_ALREADY_VALID",
            "spread_pct":spread*100,"range_15m_pct":rng,
            "current_plan":current,
        }

    r5=client.get("/"+market+"/candles",{"interval":"5m","limit":100},cache=False)
    f5=describe(closed_candles(r5,"5m",now),"5m")
    if not f5.get("valid"):
        return {"candidate":False,"reason":"INVALID_FAST_STRUCTURE","spread_pct":spread*100,"range_15m_pct":rng}

    fast=structural_plan({**row,"ask":ask},f5,meta[market])
    fast_stop=finite(fast.get("stop_distance_pct"))
    fast_pass=bool(fast.get("valid") and fast_stop is not None and fast_stop<=MAX_STOP_DISTANCE_PCT)
    reason=(
        "FAST_5M_PLAN_VALID"
        if fast_pass else
        (fast.get("reason") if not fast.get("valid") else "FAST_5M_STOP_TOO_WIDE")
    )
    return {
        "candidate":fast_pass,"reason":reason,
        "spread_pct":spread*100,"range_15m_pct":rng,
        "ask_eur":ask,
        "current_plan":current,
        "current_plan_reason":None if current.get("valid") else current.get("reason"),
        "current_stop_distance_pct":current_stop,
        "fast_plan":fast,
        "fast_stop_distance_pct":fast_stop,
        "fast_range_5m_pct":finite(f5.get("consolidation_range_pct")),
        "fast_atr14_pct":finite(f5.get("atr14_pct")),
        "fast_support_eur":finite(f5.get("support_eur")),
    }

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    state=read_json(STATE,{"schema":"solaire_breakout_risk_shadow_state_v1","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_breakout_risk_shadow_journal_v1","events":[]})
    state.setdefault("markets",{}); journal.setdefault("events",[])
    rows={r["market"]:r for r in payload.get("tracking",[]) or []
          if isinstance(r,dict) and r.get("market") and _eligible_signal(r)}

    status={
        "schema":"solaire_breakout_risk_shadow_v1","checked_at_utc":utc(now),"status":"OK",
        "tracked_signals":len(rows),"fast_recovery_candidates":0,"new_events":0,
        "evaluated_horizons":0,"errors":[],
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    client=PublicClient(timeout=10,retries=2,requests_per_second=8)
    try:
        client.get("/time",cache=False)
        meta={m["market"]:m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"}
        for market in sorted(set(state["markets"])|set(rows)):
            st=state["markets"].setdefault(market,{"active":False})
            row=rows.get(market)
            snap=None
            is_candidate=False
            if row and market in meta:
                try:
                    snap=_snapshot(row,client,meta,time.time())
                    is_candidate=bool(snap.get("candidate"))
                except Exception as exc:
                    status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
            if is_candidate:
                status["fast_recovery_candidates"]+=1
            if is_candidate and not st.get("active"):
                fast=snap.get("fast_plan") or {}
                current=snap.get("current_plan") or {}
                event={
                    "event_id":f"{market}|{int(time.time())}","market":market,
                    "detected_at_utc":payload.get("generated_at_utc"),"detected_ts":time.time(),
                    "signal_state":row.get("signal_state"),"signal_score":finite(row.get("signal_score")),
                    "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                    "signal_price_eur":finite(row.get("last")),
                    "quote_volume_24h_eur":finite(row.get("quote_volume_24h_eur")),
                    "spread_pct":snap.get("spread_pct"),"range_15m_pct":snap.get("range_15m_pct"),
                    "current_plan_valid":bool(current.get("valid")),
                    "current_plan_reason":snap.get("current_plan_reason"),
                    "current_stop_distance_pct":snap.get("current_stop_distance_pct"),
                    "fast_entry_eur":fast.get("entry_eur"),"fast_stop_eur":fast.get("stop_eur"),
                    "fast_tp1_eur":fast.get("tp1_eur"),"fast_tp2_eur":fast.get("tp2_eur"),
                    "fast_stop_distance_pct":snap.get("fast_stop_distance_pct"),
                    "fast_net_rr_tp1":fast.get("net_rr_tp1"),
                    "fast_range_5m_pct":snap.get("fast_range_5m_pct"),
                    "fast_atr14_pct":snap.get("fast_atr14_pct"),
                    "fast_support_eur":snap.get("fast_support_eur"),
                    "evaluations":{},
                    "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
                }
                journal["events"].append(event); st["active_event_id"]=event["event_id"]; status["new_events"]+=1
            st["active"]=is_candidate
            st["updated_at_utc"]=utc()

        due={}
        for idx,e in enumerate(journal["events"]):
            t0=finite(e.get("detected_ts"))
            if t0 is None: continue
            for h in HORIZONS:
                if now>=t0+h*3600 and str(h) not in e.setdefault("evaluations",{}):
                    due.setdefault(e["market"],[]).append((idx,h))
        for market,items in due.items():
            try:
                raw=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
                bars=_closed_rows(raw,now)
                for idx,h in items:
                    result=_eval(journal["events"][idx],bars,h)
                    if result:
                        journal["events"][idx]["evaluations"][str(h)]=result
                        status["evaluated_horizons"]+=1
            except Exception as exc:
                status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        status["errors"].append({"reason":type(exc).__name__+":"+str(exc)})
    if status["errors"]: status["status"]="DEGRADED_NONBLOCKING"
    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc(); journal["updated_at_utc"]=utc()
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_BREAKOUT_RISK_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
