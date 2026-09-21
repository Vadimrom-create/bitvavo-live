#!/usr/bin/env python3
"""Prospective V2.1 candidate shadow: HQ BUILDING + CONFIRMED range rejects.

Measurement only. It compares the current 6% structural-range gate with an
otherwise-identical 5% variant on the same live market snapshot for:
1) high-quality BUILDING_ACCELERATION episodes; and
2) CONFIRMED_ACCELERATION episodes rejected by production specifically for
   STRUCTURAL_RANGE_TOO_NARROW.
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
ALERT_STATUS="production_alert_status.json"
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

    def gate(range_min):
        if rng is None or rng<range_min:
            return {"passed":False,"reason":"STRUCTURAL_RANGE_TOO_NARROW"}
        plan=structural_plan({**row,"ask":ask},features,metadata[market])
        if not plan.get("valid"):
            return {"passed":False,"reason":plan.get("reason","INVALID_PLAN")}
        if finite(plan.get("stop_distance_pct"),999)>MAX_STOP_DISTANCE_PCT:
            return {"passed":False,"reason":"STRUCTURAL_STOP_TOO_WIDE"}
        return {"passed":True,"reason":None,"trade":plan}

    return {**common,"current6":gate(CURRENT_RANGE),"candidate5":gate(CANDIDATE_RANGE),"base_reason":None}

def _append_event(*,row,source_type,payload,snap,journal,status,production_rejection_reason=None):
    now=time.time()
    market=row.get("market")
    event={
        "event_id":f"{market}|{source_type}|{int(now)}",
        "market":market,
        "source_type":source_type,
        "production_rejection_reason":production_rejection_reason,
        "detected_at_utc":payload.get("generated_at_utc"),
        "detected_ts":now,
        "signal_price_eur":finite(row.get("last")),
        "signal_score":finite(row.get("signal_score")),
        "signal_state":row.get("signal_state"),
        "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
        "context":copy.deepcopy(row.get("context") or {}),
        "spread_pct":snap.get("spread_pct"),
        "range_15m_pct":snap.get("range_15m_pct"),
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
        if source_type=="CONFIRMED_RANGE_REJECT":
            status["confirmed_range_candidate5_only_pass"]+=1
    journal["events"].append(event)
    status["new_events"]+=1
    status["events"].append(event)
    return event

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    alert=read_json(ALERT_STATUS,{})
    state=read_json(STATE,{"schema":"solaire_v21_range5_shadow_state_v2","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_v21_range5_shadow_journal_v2","events":[]})
    state["schema"]="solaire_v21_range5_shadow_state_v2"; state.setdefault("markets",{})
    journal["schema"]="solaire_v21_range5_shadow_journal_v2"; journal.setdefault("events",[])

    tracking={r.get("market"):r for r in (payload.get("tracking") or [])
              if isinstance(r,dict) and r.get("market")}

    hq={}
    for market,row in tracking.items():
        acc=row.get("acceleration") or {}
        score=finite(row.get("signal_score")); ev=int(acc.get("evidence_count") or 0)
        if row.get("signal_state")=="BUILDING_ACCELERATION" and score is not None and score>=MIN_SCORE and ev>=MIN_EVIDENCE:
            hq[market]=row

    confirmed_range={}
    for rejection in (alert.get("rejections") or []):
        market=rejection.get("market")
        if rejection.get("reason")!="STRUCTURAL_RANGE_TOO_NARROW": continue
        row=tracking.get(market)
        if row and row.get("signal_state")=="CONFIRMED_ACCELERATION":
            confirmed_range[market]=row

    status={
        "schema":"solaire_v21_range5_shadow_v2","checked_at_utc":utc(now),"status":"OK",
        "hq_candidates":len(hq),
        "confirmed_range_rejections":len(confirmed_range),
        "new_events":0,
        "current6_pass":0,"candidate5_pass":0,"candidate5_only_pass":0,
        "confirmed_range_candidate5_only_pass":0,
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

        all_markets=set(state["markets"])|set(tracking)|set(confirmed_range)
        for market in sorted(all_markets):
            st=state["markets"].setdefault(market,{"hq_active":False,"confirmed_range_active":False})

            # High-quality BUILDING episode transition.
            row=hq.get(market); is_hq=row is not None; was_hq=bool(st.get("hq_active"))
            if is_hq and not was_hq:
                snap=_gate_snapshot(row,client,metadata,time.time())
                event=_append_event(row=row,source_type="HQ_BUILDING",payload=payload,snap=snap,
                                    journal=journal,status=status)
                st["hq_active_event_id"]=event["event_id"]
            st["hq_active"]=is_hq

            # Confirmed episode rejected solely by the production range gate.
            crow=confirmed_range.get(market)
            is_cr=crow is not None; was_cr=bool(st.get("confirmed_range_active"))
            if is_cr and not was_cr:
                snap=_gate_snapshot(crow,client,metadata,time.time())
                event=_append_event(row=crow,source_type="CONFIRMED_RANGE_REJECT",payload=payload,snap=snap,
                                    journal=journal,status=status,
                                    production_rejection_reason="STRUCTURAL_RANGE_TOO_NARROW")
                st["confirmed_range_event_id"]=event["event_id"]
            st["confirmed_range_active"]=is_cr
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
