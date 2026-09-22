#!/usr/bin/env python3
"""Prospective shadow for Solaire V2 final-gate rejections.

Tracks rejected CONFIRMED episodes through later scans, including periods where
the detector downgrades to BUILDING. Separates:
- execution-valid snapshots while any Solaire acceleration is still detected;
- fully actionable snapshots where the signal is CONFIRMED and execution-valid.
Also measures forward 1h/4h/12h/24h MFE/MAE/close.

Measurement only: never affects detection, BUY gating, email, or execution.
"""
from __future__ import annotations
import json, sys, time
from datetime import datetime
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
HORIZONS=(1,4,12,24)
MAX_AGE=24*3600
MAX_EVENTS=3000

def _event(journal,key):
    for e in reversed(journal.get("events",[])):
        if e.get("event_id")==key: return e
    return None

def _closed_5m(raw,now):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        t,h,l,c=finite(x[0]),finite(x[2]),finite(x[3]),finite(x[4])
        if None in (t,h,l,c): continue
        if t+300_000 <= now*1000: out.append((int(t),h,l,c))
    return sorted(out)

def _evaluate_from(bars,start_ts,baseline,hours,method):
    if start_ts is None or baseline is None or baseline<=0: return None
    first=((int(start_ts*1000)//300_000)+1)*300_000
    end=int((start_ts+hours*3600)*1000)
    xs=[x for x in bars if first<=x[0]<end]
    if not xs: return None
    high=max(x[1] for x in xs); low=min(x[2] for x in xs); close=xs[-1][3]
    return {
        "horizon_hours":hours,
        "mfe_pct":round((high/baseline-1)*100,4),
        "mae_pct":round((low/baseline-1)*100,4),
        "close_return_pct":round((close/baseline-1)*100,4),
        "bars_used":len(xs),
        "method":method,
    }

def _parse_ts(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z","+00:00")).timestamp()
    except Exception:
        return None

def _evaluate(event,bars,hours):
    return _evaluate_from(
        bars,
        finite(event.get("rejected_ts")),
        finite(event.get("rejection_price_eur")),
        hours,
        "closed_5m_bars_after_rejection",
    )

def _evaluate_reentry(event,bars,hours):
    snap=event.get("first_later_execution_valid_snapshot") or {}
    return _evaluate_from(
        bars,
        _parse_ts(snap.get("at_utc")),
        finite(snap.get("entry_eur"),finite(snap.get("signal_price_eur"))),
        hours,
        "closed_5m_bars_after_first_execution_valid_snapshot",
    )

def _reentry_tier(row):
    state=row.get("signal_state")
    score=finite(row.get("signal_score"),0)
    evidence=int((row.get("acceleration") or {}).get("evidence_count") or 0)
    if state=="CONFIRMED_ACCELERATION":
        return "CONFIRMED_REENTRY"
    if state=="BUILDING_ACCELERATION" and score>=6.0 and evidence>=4:
        return "BUILDING_HQ_4E"
    if state=="BUILDING_ACCELERATION" and score>=6.0 and evidence>=3:
        return "BUILDING_6_3"
    if state=="BUILDING_ACCELERATION":
        return "BUILDING_WEAK"
    return "OTHER"

def _signal_snapshot(row,now):
    acc=row.get("acceleration") or {}
    return {
        "at_utc":utc(now),
        "signal_state":row.get("signal_state"),
        "signal_score":finite(row.get("signal_score")),
        "evidence_count":int(acc.get("evidence_count") or 0),
        "timeframe_confirmation_15m":bool(acc.get("timeframe_confirmation_15m")),
        "confirmation_scope":acc.get("confirmation_scope"),
        "confirmation_15m_component":finite((acc.get("components") or {}).get("confirmation_15m")),
        "signal_price_eur":finite(row.get("last")),
    }

def _validated_snapshot(event,row,validated,now):
    trade=validated.get("trade") or {}
    entry=finite(trade.get("entry_eur"))
    base=finite(event.get("rejection_price_eur"))
    rejected_ts=finite(event.get("rejected_ts"))
    return {
        "at_utc":utc(now),
        "signal_state":row.get("signal_state"),
        "signal_score":finite(row.get("signal_score")),
        "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
        "timeframe_confirmation_15m":bool((row.get("acceleration") or {}).get("timeframe_confirmation_15m")),
        "confirmation_scope":(row.get("acceleration") or {}).get("confirmation_scope"),
        "confirmation_15m_component":finite(((row.get("acceleration") or {}).get("components") or {}).get("confirmation_15m")),
        "reentry_tier":_reentry_tier(row),
        "reentry_delay_seconds":round(now-rejected_ts,1) if rejected_ts is not None else None,
        "signal_price_eur":finite(row.get("last")),
        "entry_eur":entry,
        "return_from_rejection_pct":round((entry/base-1)*100,4) if entry and base else None,
        "spread_pct":validated.get("spread_pct"),
        "structural_range_15m_pct":validated.get("structural_range_15m_pct"),
        "stop_distance_pct":trade.get("stop_distance_pct"),
        "stop_eur":trade.get("stop_eur"),
        "tp1_eur":trade.get("tp1_eur"),
    }

def main():
    now=time.time()
    payload=read_json(CANDIDATES,{})
    alert=read_json(ALERT_STATUS,{})
    state=read_json(STATE,{"schema":"solaire_rejection_shadow_state_v5","markets":{}})
    journal=read_json(JOURNAL,{"schema":"solaire_rejection_shadow_journal_v5","events":[]})
    state["schema"]="solaire_rejection_shadow_state_v5"; state.setdefault("markets",{})
    journal["schema"]="solaire_rejection_shadow_journal_v5"; journal.setdefault("events",[])
    for e in journal["events"]:
        e.setdefault("evaluations",{})
        e.setdefault("execution_valid_evaluations",{})
        e.setdefault("first_later_building_snapshot",None)
        e.setdefault("first_later_confirmed_snapshot",None)
        e.setdefault("first_later_execution_valid_snapshot",None)
        e.setdefault("first_later_execution_valid_with_15m_confirmation",None)
        e.setdefault("first_later_fully_actionable_entry",e.get("first_later_qualifying_entry"))
        snap=e.get("first_later_execution_valid_snapshot") or {}
        if snap:
            if not snap.get("reentry_tier"):
                snap["reentry_tier"]=_reentry_tier({
                    "signal_state":snap.get("signal_state"),
                    "signal_score":snap.get("signal_score"),
                    "acceleration":{"evidence_count":snap.get("evidence_count")},
                })
            if snap.get("reentry_delay_seconds") is None:
                seen=_parse_ts(snap.get("at_utc"))
                rejected=finite(e.get("rejected_ts"))
                if seen is not None and rejected is not None:
                    snap["reentry_delay_seconds"]=round(seen-rejected,1)

    confirmed_rows={r.get("market"):r for r in payload.get("watch",[]) if isinstance(r,dict) and r.get("market")}
    tracking_rows={r.get("market"):r for r in payload.get("tracking",[]) if isinstance(r,dict) and r.get("market")}
    current_rej={r.get("market"):r.get("reason") for r in (alert.get("rejections") or [])
                 if r.get("market") and r.get("reason") in TRACKED}
    new_events=0

    # A rejection event can only start from a production-confirmed candidate.
    for market,reason in current_rej.items():
        st=state["markets"].setdefault(market,{})
        active_key=st.get("active_event_id")
        active=_event(journal,active_key) if active_key else None
        if active and not active.get("closed"):
            continue
        row=confirmed_rows.get(market) or tracking_rows.get(market)
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
            "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
            "timeframe_confirmation_15m":bool((row.get("acceleration") or {}).get("timeframe_confirmation_15m")),
            "confirmation_scope":(row.get("acceleration") or {}).get("confirmation_scope"),
            "reason_history":[{"at_utc":alert.get("checked_at_utc") or utc(now),"reason":reason,
                               "signal_state":row.get("signal_state")}],
            "original_condition_resolved":False,
            "first_later_building_snapshot":None,
            "first_later_confirmed_snapshot":None,
            "first_later_execution_valid_snapshot":None,
            "first_later_execution_valid_with_15m_confirmation":None,
            "first_later_fully_actionable_entry":None,
            "first_later_qualifying_entry":None,
            "evaluations":{},
            "execution_valid_evaluations":{},
            "closed":False,
            "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        }
        journal["events"].append(event)
        st["active_event_id"]=event_id
        new_events+=1

    client=PublicClient(timeout=10,retries=2,requests_per_second=8)
    errors=[]; revalidations=0; fully_actionable=0; execution_valid_while_building=0
    evaluated_horizons=0; evaluated_reentry_horizons=0
    try:
        client.get("/time",cache=False)
        metadata={m["market"]:m for m in client.get("/markets")
                  if m.get("quote")=="EUR" and m.get("status")=="trading"}

        # Revalidate against *tracking* rows, not only CONFIRMED watch rows.
        # This exposes windows where execution becomes clean while the detector
        # has downgraded to BUILDING, which the old shadow could not see.
        for market,st in state["markets"].items():
            key=st.get("active_event_id")
            event=_event(journal,key) if key else None
            if not event or event.get("closed"): continue
            age=now-finite(event.get("rejected_ts"),now)

            row=tracking_rows.get(market) or confirmed_rows.get(market)
            if row:
                try:
                    checked=time.time()
                    signal_snap=_signal_snapshot(row,checked)
                    if row.get("signal_state")=="BUILDING_ACCELERATION" and event.get("first_later_building_snapshot") is None:
                        event["first_later_building_snapshot"]=signal_snap
                    if row.get("signal_state")=="CONFIRMED_ACCELERATION" and event.get("first_later_confirmed_snapshot") is None:
                        event["first_later_confirmed_snapshot"]=signal_snap
                    validated,reason=validate(row,client,metadata,checked)
                    revalidations+=1
                    event["last_revalidation"]={
                        "checked_at_utc":utc(checked),"passed_execution_gate":bool(validated),
                        "reason":reason,"signal_state":row.get("signal_state"),
                        "signal_score":finite(row.get("signal_score")),
                    }
                    prior=(event.get("reason_history") or [])[-1].get("reason") if event.get("reason_history") else None
                    if validated:
                        snap=_validated_snapshot(event,row,validated,checked)
                        event["original_condition_resolved"]=True
                        if event.get("first_later_execution_valid_snapshot") is None:
                            event["first_later_execution_valid_snapshot"]=snap
                            if row.get("signal_state")=="BUILDING_ACCELERATION":
                                execution_valid_while_building+=1
                        if snap.get("timeframe_confirmation_15m") and event.get("first_later_execution_valid_with_15m_confirmation") is None:
                            event["first_later_execution_valid_with_15m_confirmation"]=snap
                        if row.get("signal_state")=="CONFIRMED_ACCELERATION":
                            if event.get("first_later_fully_actionable_entry") is None:
                                event["first_later_fully_actionable_entry"]=snap
                                event["first_later_qualifying_entry"]=snap  # legacy alias
                                fully_actionable+=1
                            event["closed"]=True
                            event["close_reason"]="LATER_FULLY_ACTIONABLE_ENTRY"
                            event["closed_at_utc"]=utc(checked)
                    else:
                        if reason != event.get("first_rejection_reason"):
                            event["original_condition_resolved"]=True
                        if reason != prior:
                            event.setdefault("reason_history",[]).append({
                                "at_utc":utc(checked),"reason":reason,
                                "signal_state":row.get("signal_state"),
                            })
                except (RuntimeError,ValueError,KeyError) as exc:
                    errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

            if age>MAX_AGE and not event.get("closed"):
                event["closed"]=True
                event["close_reason"]="EXPIRED_24H_WITHOUT_FULLY_ACTIONABLE_ENTRY"
                event["closed_at_utc"]=utc(now)

        due={}
        for idx,event in enumerate(journal["events"]):
            rejected=finite(event.get("rejected_ts"))
            if rejected is not None:
                for h in HORIZONS:
                    if now>=rejected+h*3600 and str(h) not in event.setdefault("evaluations",{}):
                        due.setdefault(event.get("market"),[]).append(("rejection",idx,h))
            snap=event.get("first_later_execution_valid_snapshot") or {}
            reentry_ts=_parse_ts(snap.get("at_utc"))
            if reentry_ts is not None:
                for h in HORIZONS:
                    if now>=reentry_ts+h*3600 and str(h) not in event.setdefault("execution_valid_evaluations",{}):
                        due.setdefault(event.get("market"),[]).append(("reentry",idx,h))

        for market,items in due.items():
            try:
                raw=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
                bars=_closed_5m(raw,now)
                for kind,idx,h in items:
                    event=journal["events"][idx]
                    result=_evaluate(event,bars,h) if kind=="rejection" else _evaluate_reentry(event,bars,h)
                    if result is None:
                        continue
                    if kind=="rejection":
                        event["evaluations"][str(h)]=result
                        evaluated_horizons+=1
                    else:
                        event["execution_valid_evaluations"][str(h)]=result
                        evaluated_reentry_horizons+=1
            except (RuntimeError,ValueError,KeyError) as exc:
                errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})
    except (RuntimeError,ValueError,KeyError) as exc:
        errors.append({"reason":type(exc).__name__+":"+str(exc)})

    journal["events"]=journal["events"][-MAX_EVENTS:]

    def cohort_stats(events,horizon):
        xs=[]
        for event in events:
            snap=event.get("first_later_execution_valid_snapshot") or {}
            ev=(event.get("execution_valid_evaluations") or {}).get(str(horizon))
            if not snap or not ev:
                continue
            xs.append((snap,ev))
        vals=lambda key:[finite(ev.get(key)) for _,ev in xs if finite(ev.get(key)) is not None]
        def median(values):
            values=sorted(values)
            if not values:return None
            n=len(values)
            return round(values[n//2] if n%2 else (values[n//2-1]+values[n//2])/2,4)
        return {
            "n":len(xs),
            "mfe_ge_5pct":sum(finite(ev.get("mfe_pct"),-999)>=5 for _,ev in xs),
            "clean_mfe_ge5_mae_gt_minus5":sum(
                finite(ev.get("mfe_pct"),-999)>=5 and finite(ev.get("mae_pct"),999)>-5 for _,ev in xs
            ),
            "mae_le_minus5pct":sum(finite(ev.get("mae_pct"),999)<=-5 for _,ev in xs),
            "median_mfe_pct":median(vals("mfe_pct")),
            "median_mae_pct":median(vals("mae_pct")),
            "median_close_pct":median(vals("close_return_pct")),
            "median_reentry_delay_minutes":median([
                finite(snap.get("reentry_delay_seconds"))/60
                for snap,_ in xs if finite(snap.get("reentry_delay_seconds")) is not None
            ]),
        }

    tier_names=("CONFIRMED_REENTRY","BUILDING_HQ_4E","BUILDING_6_3","BUILDING_WEAK","OTHER")
    reentry_cohorts={}
    for tier in tier_names:
        subset=[
            e for e in journal["events"]
            if (e.get("first_later_execution_valid_snapshot") or {}).get("reentry_tier")==tier
        ]
        reentry_cohorts[tier]={
            "h1":cohort_stats(subset,1),
            "h4":cohort_stats(subset,4),
        }

    policy_cohorts={}
    policy_defs={
        "SCORE_GE6_E3":lambda s: finite(s.get("signal_score"),-999)>=6 and int(s.get("evidence_count") or 0)>=3,
        "SCORE_GE6_E4":lambda s: finite(s.get("signal_score"),-999)>=6 and int(s.get("evidence_count") or 0)>=4,
        "CONFIRMATION_15M_PRESENT":lambda s: s.get("timeframe_confirmation_15m") is True,
        "CONFIRMATION_15M_ABSENT":lambda s: s.get("timeframe_confirmation_15m") is False,
    }
    for name,pred in policy_defs.items():
        subset=[
            e for e in journal["events"]
            if e.get("first_later_execution_valid_snapshot")
            and pred(e.get("first_later_execution_valid_snapshot") or {})
        ]
        policy_cohorts[name]={
            "h1":cohort_stats(subset,1),
            "h4":cohort_stats(subset,4),
        }

    reason_cohorts={}
    for reason in sorted(TRACKED):
        subset=[
            e for e in journal["events"]
            if e.get("first_rejection_reason")==reason and e.get("first_later_execution_valid_snapshot")
        ]
        reason_cohorts[reason]={
            "h1":cohort_stats(subset,1),
            "h4":cohort_stats(subset,4),
        }

    def delay_bucket(event):
        snap=event.get("first_later_execution_valid_snapshot") or {}
        delay=finite(snap.get("reentry_delay_seconds"))
        if delay is None:
            return "UNKNOWN"
        if delay<=60:
            return "LE_60S"
        if delay<=300:
            return "GT_60S_LE_5M"
        if delay<=1800:
            return "GT_5M_LE_30M"
        return "GT_30M"

    delay_names=("LE_60S","GT_60S_LE_5M","GT_5M_LE_30M","GT_30M","UNKNOWN")
    rapid_reentry_cohorts={}
    for bucket in delay_names:
        subset=[
            e for e in journal["events"]
            if e.get("first_later_execution_valid_snapshot")
            and delay_bucket(e)==bucket
        ]
        rapid_reentry_cohorts[bucket]={
            "h1":cohort_stats(subset,1),
            "h4":cohort_stats(subset,4),
            "by_reason":{},
        }
        for reason in sorted(TRACKED):
            rs=[e for e in subset if e.get("first_rejection_reason")==reason]
            rapid_reentry_cohorts[bucket]["by_reason"][reason]={
                "h1":cohort_stats(rs,1),
                "h4":cohort_stats(rs,4),
            }

    comparable_reentries=[
        e for e in journal["events"]
        if "timeframe_confirmation_15m" in (e.get("first_later_execution_valid_snapshot") or {})
    ]
    state["updated_at_utc"]=utc(); journal["updated_at_utc"]=utc()
    status={
        "schema":"solaire_rejection_shadow_v7","checked_at_utc":utc(),
        "status":"OK" if not errors else "DEGRADED_NONBLOCKING",
        "new_events":new_events,"revalidations":revalidations,
        "new_fully_actionable":fully_actionable,
        "new_execution_valid_while_building":execution_valid_while_building,
        "evaluated_horizons":evaluated_horizons,
        "evaluated_reentry_horizons":evaluated_reentry_horizons,
        "active_events":sum(not e.get("closed") for e in journal["events"]),
        "events_with_original_condition_resolved":sum(bool(e.get("original_condition_resolved")) for e in journal["events"]),
        "events_with_building_milestone":sum(bool(e.get("first_later_building_snapshot")) for e in journal["events"]),
        "events_with_confirmed_milestone":sum(bool(e.get("first_later_confirmed_snapshot")) for e in journal["events"]),
        "events_with_execution_valid_snapshot":sum(bool(e.get("first_later_execution_valid_snapshot")) for e in journal["events"]),
        "events_with_execution_valid_15m_confirmation":sum(bool(e.get("first_later_execution_valid_with_15m_confirmation")) for e in journal["events"]),
        "events_with_fully_actionable_entry":sum(bool(e.get("first_later_fully_actionable_entry")) for e in journal["events"]),
        "events_with_1h":sum("1" in (e.get("evaluations") or {}) for e in journal["events"]),
        "events_with_4h":sum("4" in (e.get("evaluations") or {}) for e in journal["events"]),
        "events_with_12h":sum("12" in (e.get("evaluations") or {}) for e in journal["events"]),
        "events_with_24h":sum("24" in (e.get("evaluations") or {}) for e in journal["events"]),
        "reentries_with_1h":sum("1" in (e.get("execution_valid_evaluations") or {}) for e in journal["events"]),
        "reentries_with_4h":sum("4" in (e.get("execution_valid_evaluations") or {}) for e in journal["events"]),
        "reentries_with_12h":sum("12" in (e.get("execution_valid_evaluations") or {}) for e in journal["events"]),
        "reentries_with_24h":sum("24" in (e.get("execution_valid_evaluations") or {}) for e in journal["events"]),
        "reentry_tier_cohorts":reentry_cohorts,
        "reentry_policy_cohorts":policy_cohorts,
        "reentry_reason_cohorts":reason_cohorts,
        "rapid_reentry_cohorts":rapid_reentry_cohorts,
        "priority2_promotion_readiness":{
            "prospective_comparable_reentries":len(comparable_reentries),
            "target_reentries":20,
            "ready":len(comparable_reentries)>=20,
        },
        "errors":errors,
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
    }
    atomic_json(STATE,state); atomic_json(JOURNAL,journal); atomic_json(STATUS,status)
    print("SOLAIRE_REJECTION_SHADOW "+json.dumps(status,ensure_ascii=False))
    return 0

if __name__=="__main__": raise SystemExit(main())
