#!/usr/bin/env python3
"""Audit one-email-per-scan serialization in Solaire V2.

Replays production_alerts.select_events over historical candidate snapshots,
applies actual sent/suppressed episode state from production_alert_status, and
identifies new actionable episodes that were never evaluated in a cycle because
the sender stopped after the first delivered BUY.

For those serialized-away events, current execution rules are reconstructed
historically and 1h/4h outcomes are measured.

Research-only. No production behavior changes.
"""
from __future__ import annotations
import json, subprocess, statistics, sys
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_alerts import select_events, mark_sent, mark_suppressed
from research.risk import structural_plan

START="2026-09-21T08:00:00+00:00"
END="2026-09-22T07:30:00+00:00"
OUT="research/solaire_alert_serialization_audit_20260921.json"
MIN_VOL=75_000.0
MAX_SPREAD_PCT=0.5
MIN_RANGE=6.0
MAX_STOP=10.0
PAIR_MAX_SEC=600

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def git_versions(path):
    shas=subprocess.check_output(
        ["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--",path],
        text=True,
    ).split()
    out=[]; seen=set()
    for sha in shas:
        try:
            obj=json.loads(subprocess.check_output(
                ["git","show",f"{sha}:{path}"],text=True,stderr=subprocess.DEVNULL
            ))
        except Exception:
            continue
        marker=obj.get("generated_at_utc") or obj.get("checked_at_utc") or sha
        if marker in seen: continue
        seen.add(marker); out.append((sha,obj))
    return out

def live_row(obj,market):
    for r in obj.get("markets",[]) or []:
        if isinstance(r,dict) and r.get("market")==market:return r
    return None

def nearest(rows,t0,max_sec):
    best=None
    for r in rows:
        d=abs(r["ts"]-t0)
        if best is None or d<best["delta_sec"]:best={**r,"delta_sec":d}
    return best if best and best["delta_sec"]<=max_sec else None

def raw_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6:continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals):continue
        t,o,h,l,c,v=vals;out.append((int(t),o,h,l,c,v))
    return sorted(out)

def forward(rows,t0,base,hours):
    if not base or base<=0:return None
    first=((int(t0*1000)//300_000)+1)*300_000
    end=int((t0+hours*3600)*1000)
    xs=[x for x in rows if first<=x[0]<end]
    if not xs:return None
    return {
        "mfe_pct":round((max(x[2] for x in xs)/base-1)*100,4),
        "mae_pct":round((min(x[3] for x in xs)/base-1)*100,4),
        "close_return_pct":round((xs[-1][4]/base-1)*100,4),
        "bars":len(xs),
    }

def gate_proxy(row,t0,live,raw15,meta):
    q=nearest(live,t0,PAIR_MAX_SEC)
    vol=finite(row.get("quote_volume_24h_eur"),finite(q.get("quote_volume_24h_eur")) if q else None)
    spread=finite(q.get("spread_pct")) if q else None
    ask=finite(q.get("ask")) if q else finite(row.get("last"))
    f15=describe(closed_candles(raw15,"15m",t0),"15m")
    rng=finite(f15.get("consolidation_range_pct"))
    plan=None
    if f15.get("valid") and ask and ask>0:
        p=structural_plan({**row,"ask":ask},f15,meta)
        plan={
            "valid":bool(p.get("valid")),
            "reason":None if p.get("valid") else p.get("reason"),
            "stop_distance_pct":finite(p.get("stop_distance_pct")),
            "entry_eur":finite(p.get("entry_eur")),
            "stop_eur":finite(p.get("stop_eur")),
            "tp1_eur":finite(p.get("tp1_eur")),
        }
    stop=finite((plan or {}).get("stop_distance_pct"))
    passes={
        "liquidity":vol is not None and vol>=MIN_VOL,
        "spread":spread is not None and spread<=MAX_SPREAD_PCT,
        "range":rng is not None and rng>=MIN_RANGE,
        "plan_and_stop":bool((plan or {}).get("valid") and stop is not None and stop<=MAX_STOP),
    }
    return {
        "passed":all(passes.values()),
        "passes":passes,
        "quote_volume_24h_eur":vol,"spread_pct":spread,"range_15m_pct":rng,
        "stop_distance_pct":stop,"plan":plan,
        "quote_at_utc":q.get("at_utc") if q else None,
        "quote_delta_seconds":round(q.get("delta_sec"),2) if q else None,
    }

def main():
    candidates=[]
    for sha,obj in git_versions("production_alert_candidates.json"):
        s=obj.get("generated_at_utc")
        if s:candidates.append({"sha":sha,"at_utc":s,"ts":ts(s),"payload":obj})
    candidates.sort(key=lambda x:x["ts"])

    alerts=[]
    for sha,obj in git_versions("production_alert_status.json"):
        s=obj.get("checked_at_utc")
        if not s:continue
        alerts.append({
            "sha":sha,"at_utc":s,"ts":ts(s),"obj":obj,
            "rejections":{x.get("market"):x.get("reason") for x in (obj.get("rejections") or []) if x.get("market")},
            "sent_market":obj.get("market") if obj.get("email")=="DELIVERY_COMPLETED" else None,
        })
    alerts.sort(key=lambda x:x["ts"])

    markets=set()
    for c in candidates:
        for r in c["payload"].get("tracking",[]) or []:
            if isinstance(r,dict) and r.get("market"):markets.add(r["market"])

    live_by={m:[] for m in markets}
    for sha,obj in git_versions("bitvavo_live.json"):
        s=obj.get("generated_at_utc")
        if not s:continue
        t0=ts(s)
        for m in markets:
            r=live_row(obj,m)
            if not r:continue
            live_by[m].append({
                "at_utc":s,"ts":t0,"last":finite(r.get("last")),
                "bid":finite(r.get("bid")),"ask":finite(r.get("ask")),
                "spread_pct":finite(r.get("spread_pct")),
                "quote_volume_24h_eur":finite(r.get("quote_volume_24h_eur")),
            })
    for xs in live_by.values():xs.sort(key=lambda x:x["ts"])

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets") if m.get("market") in markets}
    raw15={};raw5={}

    state={"markets":{}}
    cycles=[];skipped=[]
    for c in candidates:
        payload=c["payload"];t0=c["ts"]
        events,state=select_events(payload,state,t0+1,limit=None)
        a=nearest(alerts,t0,420)
        sent=a.get("sent_market") if a else None
        rejs=a.get("rejections",{}) if a else {}

        sent_index=None
        if sent:
            for i,e in enumerate(events):
                if e.get("market")==sent:
                    sent_index=i;break

        cycle_events=[]
        for i,row in enumerate(events):
            market=row.get("market")
            if market not in metas:continue
            if market not in raw15:
                raw15[market]=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
                raw5[market]=raw_rows(client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False))
            proxy=gate_proxy(row,t0,live_by.get(market,[]),raw15[market],metas[market])
            serialized=bool(sent_index is not None and i>sent_index)
            actual_reason=rejs.get(market)
            f1=forward(raw5[market],t0,finite(row.get("last")),1)
            f4=forward(raw5[market],t0,finite(row.get("last")),4)
            item={
                "rank":i+1,"market":market,
                "signal_score":finite(row.get("signal_score")),
                "signal_price_eur":finite(row.get("last")),
                "episode_extension_pct":finite(row.get("episode_extension_pct")),
                "actual_sent":market==sent,
                "actual_rejection_reason":actual_reason,
                "serialized_after_sent_market":serialized,
                "gate_proxy":proxy,
                "forward_1h":f1,"forward_4h":f4,
            }
            cycle_events.append(item)
            if serialized and proxy["passed"]:
                skipped.append({
                    "cycle_at_utc":c["at_utc"],"sent_market":sent,**item
                })

        # Apply actual episode-handling state so the replay preserves production
        # semantics in later snapshots.
        for row in events:
            m=row.get("market");reason=rejs.get(m)
            if reason=="PRIOR_BUY_THESIS_STILL_ACTIVE":
                state=mark_suppressed(state,row,(a or {}).get("ts",t0+1),reason)
            if m==sent:
                state=mark_sent(state,row,(a or {}).get("ts",t0+1),trade=None)
                break

        if sent or any(x["serialized_after_sent_market"] for x in cycle_events):
            cycles.append({
                "at_utc":c["at_utc"],"alert_at_utc":a.get("at_utc") if a else None,
                "sent_market":sent,"event_count":len(cycle_events),"events":cycle_events,
            })

    complete=[x for x in skipped if (x.get("forward_4h") or {}).get("bars",0)>=36]
    summary={
        "candidate_cycles":len(candidates),
        "delivery_cycles":sum(1 for x in cycles if x.get("sent_market")),
        "serialization_skipped_execution_clean_events":len(skipped),
        "with_substantial_4h_observation":len(complete),
        "mfe_ge_5pct_4h":sum(finite((x.get("forward_4h") or {}).get("mfe_pct"),-999)>=5 for x in complete),
        "mae_le_minus5pct_4h":sum(finite((x.get("forward_4h") or {}).get("mae_pct"),999)<=-5 for x in complete),
        "median_mfe_4h_pct":med([finite((x.get("forward_4h") or {}).get("mfe_pct")) for x in complete]),
        "median_mae_4h_pct":med([finite((x.get("forward_4h") or {}).get("mae_pct")) for x in complete]),
        "median_close_4h_pct":med([finite((x.get("forward_4h") or {}).get("close_return_pct")) for x in complete]),
    }
    out={
        "schema":"solaire_alert_serialization_audit_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "summary":summary,
        "skipped_execution_clean_events":skipped,
        "delivery_cycles":cycles,
        "limitations":[
            "execution gate is reconstructed using nearest persisted Bitvavo snapshot within 10 minutes",
            "prior-thesis handling is replayed only when explicitly present in the persisted alert status",
            "historical freshness is not replayed",
        ],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_ALERT_SERIALIZATION "+json.dumps(summary,ensure_ascii=False))

if __name__=="__main__":main()
