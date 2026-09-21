#!/usr/bin/env python3
"""Shadow audit of Solaire execution-gate rejections.

Records CONFIRMED accelerations rejected by the final execution gate, then
revalidates them on later scans. Measurement only: never affects detection,
BUY gating or email delivery.
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

def main():
    now=time.time(); payload=read_json(CANDIDATES,{})
    alert=read_json(ALERT_STATUS,{})
    state=read_json(STATE,{"markets":{}})
    journal=read_json(JOURNAL,{"events":[]})
    rows={r.get("market"):r for r in payload.get("watch",[]) if r.get("market")}
    new=0
    for rej in alert.get("rejections",[]) or []:
        market,reason=rej.get("market"),rej.get("reason")
        row=rows.get(market)
        if reason not in TRACKED or not row: continue
        key=f"{market}|{reason}|{payload.get('generated_at_utc')}"
        if any(e.get("key")==key for e in journal["events"]): continue
        event={"key":key,"market":market,"reason":reason,"rejected_at_utc":alert.get("checked_at_utc") or utc(now),
          "rejected_ts":now,"rejection_price_eur":finite(row.get("last")),"signal_score":finite(row.get("signal_score")),
          "signal_state":row.get("signal_state"),"first_later_qualifying_entry":None,"resolved":False,
          "affects_detection":False,"affects_buy_gate":False,"affects_email":False}
        journal["events"].append(event); state["markets"][market]={"active_event_key":key}; new+=1

    client=PublicClient(timeout=10,retries=2); client.get("/time",cache=False)
    metadata={m["market"]:m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"}
    checked=0; errors=[]
    for event in journal["events"]:
        if event.get("resolved"): continue
        row=rows.get(event.get("market"))
        if not row: continue
        try:
            validated,reason=validate(row,client,metadata,time.time()); checked+=1
            event["last_revalidation"]={"checked_at_utc":utc(),"reason":reason,"passed":bool(validated)}
            if validated:
                entry=finite((validated.get("trade") or {}).get("entry_eur"))
                base=finite(event.get("rejection_price_eur"))
                event["resolved"]=True
                event["original_condition_resolved"]=True
                event["first_later_qualifying_entry"]={"at_utc":utc(),"entry_eur":entry,
                  "upside_consumed_pct":round((entry/base-1)*100,4) if entry and base else None,
                  "spread_pct":validated.get("spread_pct"),"structural_range_15m_pct":validated.get("structural_range_15m_pct"),
                  "stop_distance_pct":(validated.get("trade") or {}).get("stop_distance_pct")}
            elif reason != event.get("reason"):
                event["original_condition_resolved"]=True
                event["replacement_rejection_reason"]=reason
        except (RuntimeError,ValueError,KeyError) as exc:
            errors.append({"market":event.get("market"),"reason":type(exc).__name__+":"+str(exc)})
    journal["updated_at_utc"]=utc(); state["updated_at_utc"]=utc()
    status={"schema":"solaire_rejection_shadow_v1","checked_at_utc":utc(),"status":"OK" if not errors else "DEGRADED_NONBLOCKING",
      "new_rejection_events":new,"active_events":sum(not e.get("resolved") for e in journal["events"]),
      "resolved_events":sum(bool(e.get("resolved")) for e in journal["events"]),"revalidations":checked,"errors":errors,
      "affects_detection":False,"affects_buy_gate":False,"affects_email":False}
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_REJECTION_SHADOW "+json.dumps(status,ensure_ascii=False)); return 0
if __name__=="__main__": raise SystemExit(main())
