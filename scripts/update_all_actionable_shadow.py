#!/usr/bin/env python3
"""Measure simultaneous actionable Solaire candidates before email serialization.

Production currently sends at most one BUY email per scan. This shadow runs
*before* the sender, validates every new CONFIRMED episode with the same final
execution gate and prior-thesis policy, and records whether more than one
candidate was simultaneously actionable.

Measurement only: it never marks episodes handled and never sends email.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, read_json, utc
from research.http import PublicClient
from research.production_alerts import select_events
from scripts.send_production_buy_alert import validate, prior_buy_thesis_active

INPUT="production_alert_candidates.json"
ALERT_STATE="production_alert_state.json"
JOURNAL="production_all_actionable_shadow_journal.json"
STATUS="production_all_actionable_shadow_status.json"
MAX_CYCLES=1500

def main():
    now=time.time()
    payload=read_json(INPUT,{})
    state=read_json(ALERT_STATE,{"markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_all_actionable_shadow_journal_v1","cycles":[]})
    journal["schema"]="solaire_all_actionable_shadow_journal_v1"
    journal.setdefault("cycles",[])

    events,_=select_events(payload,state,now,limit=None)
    status={
        "schema":"solaire_all_actionable_shadow_v1",
        "checked_at_utc":utc(now),
        "status":"OK",
        "new_episode_candidates":len(events),
        "execution_valid_count":0,
        "actionable_after_prior_thesis_count":0,
        "simultaneous_actionable":False,
        "events":[],
        "errors":[],
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }

    if events:
        try:
            client=PublicClient(timeout=10,retries=2,requests_per_second=8)
            client.get("/time",cache=False)
            metadata={m["market"]:m for m in client.get("/markets")
                      if m.get("quote")=="EUR" and m.get("status")=="trading"}
            for rank,row in enumerate(events,1):
                checked=time.time()
                try:
                    validated,reason=validate(row,client,metadata,checked)
                    item={
                        "rank":rank,
                        "market":row.get("market"),
                        "signal_score":finite(row.get("signal_score")),
                        "signal_state":row.get("signal_state"),
                        "episode":row.get("episode"),
                        "episode_extension_pct":finite(row.get("episode_extension_pct")),
                        "episode_age_seconds":finite(row.get("episode_age_seconds")),
                        "passed_execution_gate":bool(validated),
                        "execution_rejection_reason":reason,
                        "prior_thesis_active":None,
                        "prior_thesis_status":None,
                        "actionable_after_prior_thesis":False,
                    }
                    if validated:
                        status["execution_valid_count"]+=1
                        active,thesis_status=prior_buy_thesis_active(state,validated,checked)
                        item["prior_thesis_active"]=active
                        item["prior_thesis_status"]=thesis_status
                        item["actionable_after_prior_thesis"]=not active
                        item["entry_eur"]=(validated.get("trade") or {}).get("entry_eur")
                        item["stop_eur"]=(validated.get("trade") or {}).get("stop_eur")
                        item["tp1_eur"]=(validated.get("trade") or {}).get("tp1_eur")
                        item["spread_pct"]=validated.get("spread_pct")
                        item["structural_range_15m_pct"]=validated.get("structural_range_15m_pct")
                        item["stop_distance_pct"]=(validated.get("trade") or {}).get("stop_distance_pct")
                        if not active:
                            status["actionable_after_prior_thesis_count"]+=1
                    status["events"].append(item)
                except Exception as exc:
                    status["errors"].append({"market":row.get("market"),"reason":type(exc).__name__+":"+str(exc)})
        except Exception as exc:
            status["status"]="DEGRADED_NONBLOCKING"
            status["errors"].append({"reason":type(exc).__name__+":"+str(exc)})

    if status["errors"] and status["status"]=="OK":
        status["status"]="DEGRADED_NONBLOCKING"
    status["simultaneous_actionable"]=status["actionable_after_prior_thesis_count"]>1

    cycle={
        "at_utc":payload.get("generated_at_utc") or utc(now),
        "checked_at_utc":status["checked_at_utc"],
        "new_episode_candidates":status["new_episode_candidates"],
        "execution_valid_count":status["execution_valid_count"],
        "actionable_after_prior_thesis_count":status["actionable_after_prior_thesis_count"],
        "simultaneous_actionable":status["simultaneous_actionable"],
        "events":status["events"],
    }
    journal["cycles"].append(cycle)
    journal["cycles"]=journal["cycles"][-MAX_CYCLES:]
    journal["updated_at_utc"]=utc()
    atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_ALL_ACTIONABLE_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
