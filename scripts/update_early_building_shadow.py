#!/usr/bin/env python3
"""Prospective high-quality BUILDING shadow for Solaire V2.

Tests whether strong BUILDING_ACCELERATION states can pass the *existing*
execution gate earlier than CONFIRMED, then measures their forward outcomes.
Measurement only: never changes detection, BUY gating, email, or execution.
"""
from __future__ import annotations
import copy, json, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from scripts.send_production_buy_alert import validate

INPUT="production_alert_candidates.json"
STATE="production_early_building_shadow_state.json"
JOURNAL="production_early_building_shadow_journal.json"
STATUS="production_early_building_shadow_status.json"
MIN_SCORE=6.0
MIN_EVIDENCE=4
MAX_EVENTS=3000
HORIZONS=(1,4)
MAX_CONFIRM_AGE=24*3600

def _event(journal,key):
    for e in reversed(journal.get("events",[])):
        if e.get("event_id")==key: return e
    return None

def _closed_5m(raw, now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        t,h,l,c=finite(x[0]),finite(x[2]),finite(x[3]),finite(x[4])
        if None in (t,h,l,c): continue
        if t+300_000 <= now*1000:
            out.append((int(t),h,l,c))
    return sorted(out)

def _evaluate(event, bars, hours):
    detected=finite(event.get("detected_ts"))
    baseline=finite(event.get("entry_eur"),finite(event.get("signal_price_eur")))
    if detected is None or baseline is None or baseline<=0: return None
    first=((int(detected*1000)//300_000)+1)*300_000
    end=int((detected+hours*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs: return None
    high=max(x[1] for x in xs); low=min(x[2] for x in xs); close=xs[-1][3]
    stop=finite(event.get("stop_eur")); tp1=finite(event.get("tp1_eur"))
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

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    state=read_json(STATE,{"schema":"solaire_early_building_shadow_state_v2","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_early_building_shadow_journal_v2","events":[]})
    state["schema"]="solaire_early_building_shadow_state_v2"
    state.setdefault("markets",{})
    journal["schema"]="solaire_early_building_shadow_journal_v2"
    journal.setdefault("events",[])
    tracking={r.get("market"):r for r in (payload.get("tracking") or [])
              if isinstance(r,dict) and r.get("market")}
    hq={}
    confirmed={}
    for market,row in tracking.items():
        acc=row.get("acceleration") or {}
        st=row.get("signal_state")
        score=finite(row.get("signal_score"))
        ev=int(acc.get("evidence_count") or 0)
        if st=="BUILDING_ACCELERATION" and score is not None and score>=MIN_SCORE and ev>=MIN_EVIDENCE:
            hq[market]=row
        if st=="CONFIRMED_ACCELERATION":
            confirmed[market]=row

    status={"schema":"solaire_early_building_shadow_v2","checked_at_utc":utc(now),
            "status":"OK","candidates":len(hq),"new_events":0,
            "qualified_existing_gate":0,"rejected_existing_gate":0,
            "new_confirmations":0,"evaluated_horizons":0,
            "criteria":{"min_score":MIN_SCORE,"min_evidence":MIN_EVIDENCE},
            "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
            "events":[],"errors":[]}
    try:
        client=PublicClient(timeout=10,retries=2,requests_per_second=8)
        client.get("/time",cache=False)
        metadata={m["market"]:m for m in client.get("/markets")
                  if m.get("quote")=="EUR" and m.get("status")=="trading"}

        # Episode transitions: only create a new event when a market enters the
        # high-quality BUILDING state, not on every five-minute scan.
        for market in sorted(set(state["markets"]) | set(tracking)):
            st=state["markets"].setdefault(market,{"hq_active":False})
            row=hq.get(market)
            was=bool(st.get("hq_active"))
            is_hq=row is not None
            if is_hq and not was:
                checked=time.time()
                validated,reason=validate(row,client,metadata,checked)
                event_id=f"{market}|{int(checked)}"
                event={
                    "event_id":event_id,"market":market,
                    "detected_at_utc":payload.get("generated_at_utc"),
                    "detected_ts":checked,
                    "signal_price_eur":finite(row.get("last")),
                    "signal_score":finite(row.get("signal_score")),
                    "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                    "context":copy.deepcopy(row.get("context") or {}),
                    "passed_existing_execution_gate":bool(validated),
                    "rejection_reason":reason,
                    "confirmation":None,"evaluations":{},
                    "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
                }
                if validated:
                    trade=validated.get("trade") or {}
                    event.update(
                        entry_eur=trade.get("entry_eur"),
                        stop_eur=trade.get("stop_eur"),
                        tp1_eur=trade.get("tp1_eur"),
                        tp2_eur=trade.get("tp2_eur"),
                        spread_pct=validated.get("spread_pct"),
                        structural_range_15m_pct=validated.get("structural_range_15m_pct"),
                        stop_distance_pct=trade.get("stop_distance_pct"),
                    )
                    status["qualified_existing_gate"]+=1
                else:
                    status["rejected_existing_gate"]+=1
                journal["events"].append(event)
                st["active_event_id"]=event_id
                status["new_events"]+=1
                status["events"].append(event)
            st["hq_active"]=is_hq
            st["updated_at_utc"]=utc()

        # Attach the first later CONFIRMED observation to the active/recent HQ event.
        for market,row in confirmed.items():
            st=state["markets"].get(market) or {}
            event=_event(journal,st.get("active_event_id"))
            if not event or event.get("confirmation"): continue
            detected=finite(event.get("detected_ts"))
            if detected is None or now-detected>MAX_CONFIRM_AGE: continue
            price=finite(row.get("last"))
            base=finite(event.get("signal_price_eur"))
            event["confirmation"]={
                "at_utc":payload.get("generated_at_utc"),
                "price_eur":price,
                "score":finite(row.get("signal_score")),
                "minutes_after_hq":round((now-detected)/60,2),
                "price_change_from_hq_pct":round((price/base-1)*100,4) if price and base else None,
            }
            status["new_confirmations"]+=1

        # Evaluate due 1h/4h horizons prospectively.
        due={}
        for idx,event in enumerate(journal.get("events",[])):
            detected=finite(event.get("detected_ts"))
            if detected is None: continue
            for h in HORIZONS:
                if str(h) not in event.setdefault("evaluations",{}) and now>=detected+h*3600:
                    due.setdefault(event.get("market"),[]).append((idx,h))
        for market,items in due.items():
            try:
                raw=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
                bars=_closed_5m(raw,now)
                for idx,h in items:
                    result=_evaluate(journal["events"][idx],bars,h)
                    if result is not None:
                        journal["events"][idx]["evaluations"][str(h)]=result
                        status["evaluated_horizons"]+=1
            except (RuntimeError,ValueError,KeyError) as exc:
                status["errors"].append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except Exception as exc:
        status["status"]="DEGRADED_NONBLOCKING"
        status["errors"].append({"reason":type(exc).__name__+":"+str(exc)})

    if status["errors"] and status["status"]=="OK":
        status["status"]="DEGRADED_NONBLOCKING"
    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc()
    journal["updated_at_utc"]=utc()
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_EARLY_BUILDING_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
