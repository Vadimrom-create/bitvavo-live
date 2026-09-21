#!/usr/bin/env python3
"""Immediate high-quality BUILDING shadow for Solaire V2.

Tests whether strong BUILDING_ACCELERATION states would pass the *existing*
final execution gate earlier than CONFIRMED signals. Measurement only.
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

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    state=read_json(STATE,{"schema":"solaire_early_building_shadow_state_v1","seen":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_early_building_shadow_journal_v1","events":[]})
    rows=[]
    for row in payload.get("tracking",[]) or []:
        acc=row.get("acceleration") or {}
        if row.get("signal_state")!="BUILDING_ACCELERATION": continue
        score=finite(row.get("signal_score"))
        ev=int(acc.get("evidence_count") or 0)
        if score is not None and score>=MIN_SCORE and ev>=MIN_EVIDENCE:
            rows.append(row)

    status={"schema":"solaire_early_building_shadow_v1","checked_at_utc":utc(now),
            "status":"OK","candidates":len(rows),"qualified":0,"rejected":0,
            "criteria":{"min_score":MIN_SCORE,"min_evidence":MIN_EVIDENCE},
            "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
            "events":[],"errors":[]}
    try:
        client=PublicClient(timeout=10,retries=2)
        client.get("/time",cache=False)
        metadata={m["market"]:m for m in client.get("/markets")
                  if m.get("quote")=="EUR" and m.get("status")=="trading"}
        for row in rows:
            market=row.get("market")
            # once per acceleration episode approximation: generated snapshot + market
            key=f"{market}|{payload.get('generated_at_utc')}"
            if key in state["seen"]: continue
            checked=time.time()
            validated,reason=validate(row,client,metadata,checked)
            event={"event_id":key,"market":market,"observed_at_utc":payload.get("generated_at_utc"),
                   "signal_price_eur":finite(row.get("last")),"signal_score":finite(row.get("signal_score")),
                   "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                   "context":copy.deepcopy(row.get("context") or {}),
                   "passed_existing_execution_gate":bool(validated),
                   "rejection_reason":reason,
                   "affects_detection":False,"affects_buy_gate":False,"affects_email":False}
            if validated:
                trade=validated.get("trade") or {}
                event["entry_eur"]=trade.get("entry_eur")
                event["stop_eur"]=trade.get("stop_eur")
                event["tp1_eur"]=trade.get("tp1_eur")
                event["spread_pct"]=validated.get("spread_pct")
                event["structural_range_15m_pct"]=validated.get("structural_range_15m_pct")
                event["stop_distance_pct"]=trade.get("stop_distance_pct")
                status["qualified"]+=1
            else:
                status["rejected"]+=1
            state["seen"][key]=True
            journal["events"].append(event)
            status["events"].append(event)
    except Exception as exc:
        status["status"]="DEGRADED_NONBLOCKING"
        status["errors"].append(type(exc).__name__+":"+str(exc))

    journal["events"]=journal["events"][-MAX_EVENTS:]
    state["updated_at_utc"]=utc()
    journal["updated_at_utc"]=utc()
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_EARLY_BUILDING_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
