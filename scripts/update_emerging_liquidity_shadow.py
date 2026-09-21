#!/usr/bin/env python3
"""Prospective diagnostics for emerging-liquidity Solaire signals.

The production gate requires >=75k EUR quoted volume over 24h. That protects
execution but can lag a newly emerging market. This shadow isolates cases where
24h volume is the only obvious blocker and records live order-book depth plus
recent 1h quote turnover, while keeping spread, structure and risk checks.

Two alternative liquidity profiles are measured only:
- conservative: >=20k EUR 1h turnover and >=10k EUR depth on each side within 1%
- exploratory: >=10k EUR 1h turnover and >=5k EUR depth on each side within 1%

No production BUY/email behavior changes.
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
STATE="production_emerging_liquidity_shadow_state.json"
JOURNAL="production_emerging_liquidity_shadow_journal.json"
STATUS="production_emerging_liquidity_shadow_status.json"
HORIZONS=(1,4)
MAX_EVENTS=3000
HQ_MIN_SCORE=6.0
HQ_MIN_EVIDENCE=4
PROFILES={
    "conservative":{"turnover_1h_eur":20_000.0,"depth_1pct_each_side_eur":10_000.0},
    "exploratory":{"turnover_1h_eur":10_000.0,"depth_1pct_each_side_eur":5_000.0},
}

def _eligible_signal(row):
    state=row.get("signal_state")
    score=finite(row.get("signal_score")); ev=int((row.get("acceleration") or {}).get("evidence_count") or 0)
    return state=="CONFIRMED_ACCELERATION" or (
        state=="BUILDING_ACCELERATION" and score is not None and score>=HQ_MIN_SCORE and ev>=HQ_MIN_EVIDENCE
    )

def _quote_turnover_1h(raw,now):
    cs=closed_candles(raw,"5m",now)
    return sum(finite(r.get("c"),0)*finite(r.get("v"),0) for r in cs[-12:])

def _depth(book,bid,ask,pct=.01):
    mid=(bid+ask)/2
    bid_floor=mid*(1-pct); ask_ceiling=mid*(1+pct)
    bid_eur=sum(finite(p,0)*finite(q,0) for p,q,*_ in (book.get("bids") or []) if finite(p) is not None and finite(p)>=bid_floor)
    ask_eur=sum(finite(p,0)*finite(q,0) for p,q,*_ in (book.get("asks") or []) if finite(p) is not None and finite(p)<=ask_ceiling)
    return bid_eur,ask_eur

def _bars(raw,now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        t,h,l,c=finite(x[0]),finite(x[2]),finite(x[3]),finite(x[4])
        if None in (t,h,l,c): continue
        if t+300_000<=now*1000: out.append((int(t),h,l,c))
    return sorted(out)

def _eval(e,bars,h):
    t0=finite(e.get("detected_ts")); base=finite(e.get("entry_eur"),finite(e.get("signal_price_eur")))
    if t0 is None or base is None or base<=0:return None
    first=((int(t0*1000)//300_000)+1)*300_000; end=int((t0+h*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs:return None
    high=max(x[1] for x in xs); low=min(x[2] for x in xs); close=xs[-1][3]
    stop=finite(e.get("stop_eur")); tp1=finite(e.get("tp1_eur"))
    return {
        "horizon_hours":h,"mfe_pct":round((high/base-1)*100,4),
        "mae_pct":round((low/base-1)*100,4),"close_return_pct":round((close/base-1)*100,4),
        "stop_touched":bool(stop is not None and low<=stop),
        "tp1_touched":bool(tp1 is not None and high>=tp1),
        "bars":len(xs),
    }

def _snapshot(row,client,meta,now):
    market=row["market"]; volume=finite(row.get("quote_volume_24h_eur"),0)
    if volume>=MIN_QUOTE_VOLUME_EUR:
        return {"liquidity_only_blocker":False,"reason":"CURRENT_24H_VOLUME_GATE_ALREADY_PASSES"}

    book=client.get("/"+market+"/book",{"depth":100},cache=False)
    bid=finite(book["bids"][0][0]) if book.get("bids") else None
    ask=finite(book["asks"][0][0]) if book.get("asks") else None
    retrieved=client.metadata("/"+market+"/book",{"depth":100}).get("retrieved_at_utc")
    if bid is None or ask is None or not 0<bid<=ask:
        return {"liquidity_only_blocker":False,"reason":"INVALID_BOOK"}
    spread=ask/bid-1
    if spread>MAX_SPREAD:
        return {"liquidity_only_blocker":False,"reason":"SPREAD_TOO_WIDE","spread_pct":spread*100}

    r15=client.get("/"+market+"/candles",{"interval":"15m","limit":100},cache=False)
    f15=describe(closed_candles(r15,"15m",now),"15m")
    fresh=freshness(now=now,retrieved=retrieved,candle_start_ms=f15.get("last_closed_start_ms"),interval="15m",max_retrieval_age=90)
    if not f15.get("valid") or not fresh["ok"]:
        return {"liquidity_only_blocker":False,"reason":"STALE_OR_INVALID_STRUCTURE","spread_pct":spread*100}
    rng=finite(f15.get("consolidation_range_pct"))
    if rng is None or rng<MIN_15M_CONSOLIDATION_RANGE_PCT:
        return {"liquidity_only_blocker":False,"reason":"STRUCTURAL_RANGE_TOO_NARROW","spread_pct":spread*100,"range_15m_pct":rng}

    plan=structural_plan({**row,"ask":ask},f15,meta[market])
    stop=finite(plan.get("stop_distance_pct"))
    if not plan.get("valid"):
        return {"liquidity_only_blocker":False,"reason":plan.get("reason","INVALID_PLAN"),"spread_pct":spread*100,"range_15m_pct":rng}
    if stop is None or stop>MAX_STOP_DISTANCE_PCT:
        return {"liquidity_only_blocker":False,"reason":"STRUCTURAL_STOP_TOO_WIDE","spread_pct":spread*100,"range_15m_pct":rng,"stop_distance_pct":stop}

    r5=client.get("/"+market+"/candles",{"interval":"5m","limit":100},cache=False)
    turnover=_quote_turnover_1h(r5,now)
    bd,ad=_depth(book,bid,ask,.01)
    profile_pass={}
    for name,p in PROFILES.items():
        profile_pass[name]=bool(
            turnover>=p["turnover_1h_eur"]
            and bd>=p["depth_1pct_each_side_eur"]
            and ad>=p["depth_1pct_each_side_eur"]
        )
    return {
        "liquidity_only_blocker":True,"reason":"ONLY_24H_VOLUME_GATE_BLOCKS",
        "spread_pct":spread*100,"range_15m_pct":rng,
        "quote_volume_24h_eur":volume,"quote_turnover_1h_eur":turnover,
        "bid_depth_1pct_eur":bd,"ask_depth_1pct_eur":ad,
        "profile_pass":profile_pass,"plan":plan,
    }

def main():
    now=time.time(); payload=read_json(INPUT,{})
    state=read_json(STATE,{"schema":"solaire_emerging_liquidity_shadow_state_v1","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_emerging_liquidity_shadow_journal_v1","events":[]})
    state.setdefault("markets",{}); journal.setdefault("events",[])
    rows={r["market"]:r for r in payload.get("tracking",[]) or []
          if isinstance(r,dict) and r.get("market") and _eligible_signal(r)}

    status={
        "schema":"solaire_emerging_liquidity_shadow_v1","checked_at_utc":utc(now),"status":"OK",
        "tracked_signals":len(rows),"liquidity_only_blockers":0,
        "profile_pass_counts":{k:0 for k in PROFILES},"new_events":0,"evaluated_horizons":0,
        "profiles":PROFILES,"errors":[],
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    client=PublicClient(timeout=10,retries=2,requests_per_second=8)
    try:
        client.get("/time",cache=False)
        meta={m["market"]:m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"}
        for market in sorted(set(state["markets"])|set(rows)):
            st=state["markets"].setdefault(market,{"active":False}); row=rows.get(market)
            snap=None; active=False
            if row and market in meta:
                try:
                    snap=_snapshot(row,client,meta,time.time()); active=bool(snap.get("liquidity_only_blocker"))
                except Exception as exc:
                    status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
            if active:
                status["liquidity_only_blockers"]+=1
                for k,v in (snap.get("profile_pass") or {}).items():
                    if v:status["profile_pass_counts"][k]+=1
            if active and not st.get("active"):
                plan=snap.get("plan") or {}
                e={
                    "event_id":f"{market}|{int(time.time())}","market":market,
                    "detected_at_utc":payload.get("generated_at_utc"),"detected_ts":time.time(),
                    "signal_state":row.get("signal_state"),"signal_score":finite(row.get("signal_score")),
                    "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                    "signal_price_eur":finite(row.get("last")),
                    "quote_volume_24h_eur":snap.get("quote_volume_24h_eur"),
                    "quote_turnover_1h_eur":round(snap.get("quote_turnover_1h_eur",0),2),
                    "spread_pct":snap.get("spread_pct"),"range_15m_pct":snap.get("range_15m_pct"),
                    "bid_depth_1pct_eur":round(snap.get("bid_depth_1pct_eur",0),2),
                    "ask_depth_1pct_eur":round(snap.get("ask_depth_1pct_eur",0),2),
                    "profile_pass":snap.get("profile_pass") or {},
                    "entry_eur":plan.get("entry_eur"),"stop_eur":plan.get("stop_eur"),
                    "tp1_eur":plan.get("tp1_eur"),"stop_distance_pct":plan.get("stop_distance_pct"),
                    "evaluations":{},"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
                }
                journal["events"].append(e);st["active_event_id"]=e["event_id"];status["new_events"]+=1
            st["active"]=active;st["updated_at_utc"]=utc()

        due={}
        for idx,e in enumerate(journal["events"]):
            t0=finite(e.get("detected_ts"))
            if t0 is None:continue
            for h in HORIZONS:
                if now>=t0+h*3600 and str(h) not in e.setdefault("evaluations",{}):
                    due.setdefault(e["market"],[]).append((idx,h))
        for market,items in due.items():
            try:
                raw=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False); bars=_bars(raw,now)
                for idx,h in items:
                    z=_eval(journal["events"][idx],bars,h)
                    if z:
                        journal["events"][idx]["evaluations"][str(h)]=z;status["evaluated_horizons"]+=1
            except Exception as exc:
                status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        status["errors"].append({"reason":type(exc).__name__+":"+str(exc)})
    if status["errors"]:status["status"]="DEGRADED_NONBLOCKING"
    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc();journal["updated_at_utc"]=utc()
    atomic_json(STATE,state);atomic_json(JOURNAL,journal);atomic_json(STATUS,status)
    print("SOLAIRE_EMERGING_LIQUIDITY_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__":raise SystemExit(main())
