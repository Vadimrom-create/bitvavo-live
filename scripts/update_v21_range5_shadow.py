#!/usr/bin/env python3
"""Prospective V2.1 candidate shadow: HQ BUILDING + 5% structural range.

This is measurement only. It compares the current 6% final structure gate with
an otherwise-identical 5% range variant on the same live market snapshot.
It never sends email, changes detection, or alters production BUY decisions.
"""
from __future__ import annotations
import copy, json, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, freshness, read_json, utc
from research.http import PublicClient
from research.risk import structural_plan
from scripts.send_production_buy_alert import (
    market_inputs,
    MIN_QUOTE_VOLUME_EUR,
    MAX_SPREAD,
    MAX_STOP_DISTANCE_PCT,
)

INPUT="production_alert_candidates.json"
STATE="production_v21_range5_shadow_state.json"
JOURNAL="production_v21_range5_shadow_journal.json"
STATUS="production_v21_range5_shadow_status.json"
MIN_SCORE=6.0
MIN_EVIDENCE=4
CURRENT_RANGE=6.0
CANDIDATE_RANGE=5.0
HORIZONS=(1,4)
MAX_EVENTS=3000

def _closed_5m(raw, now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        t,h,l,c=finite(x[0]),finite(x[2]),finite(x[3]),finite(x[4])
        if None in (t,h,l,c): continue
        if t+300_000 <= now*1000: out.append((int(t),h,l,c))
    return sorted(out)

def _evaluate(event,bars,hours,baseline_key,stop_key,tp1_key):
    detected=finite(event.get("detected_ts"))
    baseline=finite(event.get(baseline_key))
    if detected is None or baseline is None or baseline<=0: return None
    first=((int(detected*1000)//300_000)+1)*300_000
    end=int((detected+hours*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs: return None
    high=max(x[1] for x in xs); low=min(x[2] for x in xs); close=xs[-1][3]
    stop=finite(event.get(stop_key)); tp1=finite(event.get(tp1_key))
    return {
        "horizon_hours":hours,
        "mfe_pct":round((high/baseline-1)*100,4),
        "mae_pct":round((low/baseline-1)*100,4),
        "close_return_pct":round((close/baseline-1)*100,4),
        "bars_used":len(xs),
        "stop_touched":bool(stop is not None and low<=stop),
        "tp1_touched":bool(tp1 is not None and high>=tp1),
        "intrabar_order_if_both_touched":"UNKNOWN" if stop is not None and tp1 is not None and low<=stop and high>=tp1 else None,
        "method":"closed_5m_bars_after_shadow_detection",
    }

def _gate_snapshot(row,client,metadata,now):
    market=row.get("market")
    if not market or market not in metadata:
        return {"base_reason":"MARKET_UNAVAILABLE"}
    volume=finite(row.get("quote_volume_24h_eur"),0.0)
    if volume<MIN_QUOTE_VOLUME_EUR:
        return {"base_reason":"INSUFFICIENT_EXECUTION_LIQUIDITY"}

    quote,features,_=market_inputs(client,market,now)
    bid=finite(quote.get("bid")); ask=finite(quote.get("ask"))
    signal=finite(row.get("last"))
    if bid is None or ask is None or signal is None or not 0<bid<=ask:
        return {"base_reason":"INVALID_BOOK"}
    spread=ask/bid-1
    if spread>MAX_SPREAD:
        return {"base_reason":"SPREAD_TOO_WIDE","spread_pct":spread*100}
    fresh=freshness(
        now=now,retrieved=quote.get("retrieved_at_utc"),
        candle_start_ms=features.get("last_closed_start_ms"),interval="15m",
        max_retrieval_age=90,
    )
    if not features.get("valid") or not fresh["ok"]:
        return {"base_reason":"STALE_OR_INVALID_STRUCTURE","spread_pct":spread*100}

    rng=finite(features.get("consolidation_range_pct"))
    common={
        "spread_pct":spread*100,
        "range_15m_pct":rng,
        "ask_eur":ask,
        "price_drift_pct":(ask/signal-1)*100,
    }

    # Current 6% gate stops here if the range is too narrow.
    if rng is None or rng<CURRENT_RANGE:
        current={"passed":False,"reason":"STRUCTURAL_RANGE_TOO_NARROW"}
    else:
        p6=structural_plan({**row,"ask":ask},features,metadata[market])
        if not p6.get("valid"):
            current={"passed":False,"reason":p6.get("reason","INVALID_PLAN")}
        elif finite(p6.get("stop_distance_pct"),999)>MAX_STOP_DISTANCE_PCT:
            current={"passed":False,"reason":"STRUCTURAL_STOP_TOO_WIDE"}
        else:
            current={"passed":True,"reason":None,"trade":p6}

    # Candidate 5% gate is otherwise identical.
    if rng is None or rng<CANDIDATE_RANGE:
        candidate={"passed":False,"reason":"STRUCTURAL_RANGE_TOO_NARROW"}
    else:
        p5=structural_plan({**row,"ask":ask},features,metadata[market])
        if not p5.get("valid"):
            candidate={"passed":False,"reason":p5.get("reason","INVALID_PLAN")}
        elif finite(p5.get("stop_distance_pct"),999)>MAX_STOP_DISTANCE_PCT:
            candidate={"passed":False,"reason":"STRUCTURAL_STOP_TOO_WIDE"}
        else:
            candidate={"passed":True,"reason":None,"trade":p5}
    return {**common,"current6":current,"candidate5":candidate,"base_reason":None}

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    state=read_json(STATE,{"schema":"solaire_v21_range5_shadow_state_v1","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_v21_range5_shadow_journal_v1","events":[]})
    state.setdefault("markets",{}); journal.setdefault("events",[])
    tracking={r.get("market"):r for r in (payload.get("tracking") or [])
              if isinstance(r,dict) and r.get("market")}

    hq={}
    for market,row in tracking.items():
        acc=row.get("acceleration") or {}
        score=finite(row.get("signal_score")); ev=int(acc.get("evidence_count") or 0)
        if row.get("signal_state")=="BUILDING_ACCELERATION" and score is not None and score>=MIN_SCORE and ev>=MIN_EVIDENCE:
            hq[market]=row

    status={
        "schema":"solaire_v21_range5_shadow_v1","checked_at_utc":utc(now),"status":"OK",
        "hq_candidates":len(hq),"new_events":0,
        "current6_pass":0,"candidate5_pass":0,"candidate5_only_pass":0,
        "evaluated_signal_horizons":0,"evaluated_candidate_horizons":0,
        "criteria":{"hq_min_score":MIN_SCORE,"hq_min_evidence":MIN_EVIDENCE,
                    "current_range_pct":CURRENT_RANGE,"candidate_range_pct":CANDIDATE_RANGE},
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "errors":[],"events":[],
    }

    try:
        client=PublicClient(timeout=10,retries=2,requests_per_second=8)
        client.get("/time",cache=False)
        metadata={m["market"]:m for m in client.get("/markets")
                  if m.get("quote")=="EUR" and m.get("status")=="trading"}

        for market in sorted(set(state["markets"])|set(tracking)):
            st=state["markets"].setdefault(market,{"hq_active":False})
            row=hq.get(market); is_hq=row is not None; was=bool(st.get("hq_active"))
            if is_hq and not was:
                snap=_gate_snapshot(row,client,metadata,time.time())
                event={
                    "event_id":f"{market}|{int(time.time())}","market":market,
                    "detected_at_utc":payload.get("generated_at_utc"),"detected_ts":time.time(),
                    "signal_price_eur":finite(row.get("last")),"signal_score":finite(row.get("signal_score")),
                    "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                    "context":copy.deepcopy(row.get("context") or {}),
                    "spread_pct":snap.get("spread_pct"),"range_15m_pct":snap.get("range_15m_pct"),
                    "base_reason":snap.get("base_reason"),
                    "current6_passed":bool((snap.get("current6") or {}).get("passed")),
                    "current6_reason":(snap.get("current6") or {}).get("reason") or snap.get("base_reason"),
                    "candidate5_passed":bool((snap.get("candidate5") or {}).get("passed")),
                    "candidate5_reason":(snap.get("candidate5") or {}).get("reason") or snap.get("base_reason"),
                    "signal_evaluations":{},"candidate5_evaluations":{},
                    "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
                }
                if event["current6_passed"]: status["current6_pass"]+=1
                if event["candidate5_passed"]:
                    status["candidate5_pass"]+=1
                    tr=(snap.get("candidate5") or {}).get("trade") or {}
                    event.update(
                        candidate5_entry_eur=tr.get("entry_eur"),
                        candidate5_stop_eur=tr.get("stop_eur"),
                        candidate5_tp1_eur=tr.get("tp1_eur"),
                        candidate5_tp2_eur=tr.get("tp2_eur"),
                        candidate5_stop_distance_pct=tr.get("stop_distance_pct"),
                    )
                if event["candidate5_passed"] and not event["current6_passed"]:
                    status["candidate5_only_pass"]+=1
                journal["events"].append(event)
                st["active_event_id"]=event["event_id"]
                status["new_events"]+=1; status["events"].append(event)
            st["hq_active"]=is_hq
            st["updated_at_utc"]=utc()

        due={}
        for idx,event in enumerate(journal["events"]):
            detected=finite(event.get("detected_ts"))
            if detected is None: continue
            for h in HORIZONS:
                if now<detected+h*3600: continue
                if str(h) not in event.setdefault("signal_evaluations",{}):
                    due.setdefault(event["market"],[]).append((idx,h,"signal"))
                if event.get("candidate5_passed") and str(h) not in event.setdefault("candidate5_evaluations",{}):
                    due.setdefault(event["market"],[]).append((idx,h,"candidate5"))

        for market,items in due.items():
            try:
                raw=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
                bars=_closed_5m(raw,now)
                for idx,h,kind in items:
                    event=journal["events"][idx]
                    if kind=="signal":
                        res=_evaluate(event,bars,h,"signal_price_eur","candidate5_stop_eur","candidate5_tp1_eur")
                        if res is not None:
                            event["signal_evaluations"][str(h)]=res; status["evaluated_signal_horizons"]+=1
                    else:
                        res=_evaluate(event,bars,h,"candidate5_entry_eur","candidate5_stop_eur","candidate5_tp1_eur")
                        if res is not None:
                            event["candidate5_evaluations"][str(h)]=res; status["evaluated_candidate_horizons"]+=1
            except Exception as exc:
                status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        status["status"]="DEGRADED_NONBLOCKING"
        status["errors"].append({"reason":type(exc).__name__+":"+str(exc)})

    if status["errors"] and status["status"]=="OK": status["status"]="DEGRADED_NONBLOCKING"
    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc(); journal["updated_at_utc"]=utc()
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_V21_RANGE5_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
