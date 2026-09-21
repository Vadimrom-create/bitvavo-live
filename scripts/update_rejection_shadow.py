#!/usr/bin/env python3
"""Prospective shadow for Solaire V2 final-gate rejections.

Tracks each rejected CONFIRMED episode through later production scans until the
same market becomes execution-valid or 24h elapse. Measurement only.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from scripts.send_production_buy_alert import validate

CANDIDATES="production_alert_candidates.json"
ALERT_STATUS="production_alert_status.json"
STATE="production_rejection_shadow_state.json"
JOURNAL="production_rejection_shadow_journal.json"
STATUS="production_rejection_shadow_status.json"
TRACKED={"STRUCTURAL_RANGE_TOO_NARROW","SPREAD_TOO_WIDE","INSUFFICIENT_EXECUTION_LIQUIDITY","STRUCTURAL_STOP_TOO_WIDE"}
MAX_AGE=24*3600
MAX_EVENTS=3000

def _event(journal,key):
    for e in reversed(journal.get("events",[])):
        if e.get("event_id")==key: return e
    return None

def main():
    now=time.time()
    payload=read_json(CANDIDATES,{})
    alert=read_json(ALERT_STATUS,{})
    state=read_json(STATE,{"schema":"solaire_rejection_shadow_state_v2","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_rejection_shadow_journal_v2","events":[]})
    rows={r.get("market"):r for r in payload.get("watch",[]) if isinstance(r,dict) and r.get("market")}
    current_rej={r.get("market"):r.get("reason") for r in (alert.get("rejections") or [])
                 if r.get("market") and r.get("reason") in TRACKED}
    new_events=0

    # Start one shadow episode per market when a tracked final-gate rejection appears
    # and no still-open episode already exists.
    for market,reason in current_rej.items():
        st=state["markets"].setdefault(market,{})
        active_key=st.get("active_event_id")
        active=_event(journal,active_key) if active_key else None
        if active and not active.get("closed"):
            continue
        row=rows.get(market)
        if not row: continue
        event_id=f"{market}|{int(now)}"
        event={
            "event_id":event_id,"market":market,
            "first_rejection_reason":reason,
            "rejected_at_utc":alert.get("checked_at_utc") or utc(now),
            "rejected_ts":now,
            "rejection_price_eur":finite(row.get("last")),
            "signal_score":finite(row.get("signal_score")),
            "signal_state":row.get("signal_state"),
            "reason_history":[{"at_utc":alert.get("checked_at_utc") or utc(now),"reason":reason}],
            "original_condition_resolved":False,
            "first_later_qualifying_entry":None,
            "closed":False,
            "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        }
        journal["events"].append(event)
        st["active_event_id"]=event_id
        new_events+=1

    client=PublicClient(timeout=10,retries=2)
    errors=[]; revalidations=0; newly_qualified=0
    try:
        client.get("/time",cache=False)
        metadata={m["market"]:m for m in client.get("/markets")
                  if m.get("quote")=="EUR" and m.get("status")=="trading"}
        for market,st in state["markets"].items():
            key=st.get("active_event_id")
            event=_event(journal,key) if key else None
            if not event or event.get("closed"): continue
            age=now-finite(event.get("rejected_ts"),now)
            if age>MAX_AGE:
                event["closed"]=True
                event["close_reason"]="EXPIRED_24H_WITHOUT_LATER_QUALIFYING_ENTRY"
                event["closed_at_utc"]=utc(now)
                continue

            row=rows.get(market)
            if not row:
                event["last_seen_candidate_at_utc"]=event.get("last_seen_candidate_at_utc")
                continue
            try:
                validated,reason=validate(row,client,metadata,time.time())
                revalidations+=1
                event["last_revalidation"]={"checked_at_utc":utc(),"passed":bool(validated),"reason":reason}
                prior=(event.get("reason_history") or [])[-1].get("reason") if event.get("reason_history") else None
                if validated:
                    entry=finite((validated.get("trade") or {}).get("entry_eur"))
                    base=finite(event.get("rejection_price_eur"))
                    event["original_condition_resolved"]=True
                    event["first_later_qualifying_entry"]={
                        "at_utc":utc(),"entry_eur":entry,
                        "return_from_rejection_pct":round((entry/base-1)*100,4) if entry and base else None,
                        "spread_pct":validated.get("spread_pct"),
                        "structural_range_15m_pct":validated.get("structural_range_15m_pct"),
                        "stop_distance_pct":(validated.get("trade") or {}).get("stop_distance_pct"),
                    }
                    event["closed"]=True
                    event["close_reason"]="LATER_QUALIFYING_ENTRY"
                    event["closed_at_utc"]=utc()
                    newly_qualified+=1
                else:
                    if reason != event.get("first_rejection_reason"):
                        event["original_condition_resolved"]=True
                    if reason != prior:
                        event.setdefault("reason_history",[]).append({"at_utc":utc(),"reason":reason})
            except (RuntimeError,ValueError,KeyError) as exc:
                errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except (RuntimeError,ValueError,KeyError) as exc:
        errors.append({"reason":type(exc).__name__+":"+str(exc)})

    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc()
    journal["updated_at_utc"]=utc()
    status={
        "schema":"solaire_rejection_shadow_v2","checked_at_utc":utc(),
        "status":"OK" if not errors else "DEGRADED_NONBLOCKING",
        "new_events":new_events,"revalidations":revalidations,
        "newly_qualified":newly_qualified,
        "active_events":sum(not e.get("closed") for e in journal["events"]),
        "events_with_original_condition_resolved":sum(bool(e.get("original_condition_resolved")) for e in journal["events"]),
        "errors":errors,
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_REJECTION_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
