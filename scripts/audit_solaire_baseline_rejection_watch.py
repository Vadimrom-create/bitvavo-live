#!/usr/bin/env python3
"""Evidence audit for the four Sep-21 baseline rejections.

Reconstructs the trajectory of FLOCK/XVG/ICX/SAGA from the user-requested
baseline timestamp and searches repository history for later Solaire detector
snapshots. At each detector snapshot, it rebuilds the current 15m structural
gate and pairs the closest persisted Bitvavo quote/24h-volume snapshot.

This is research-only. Historical pairing is approximate; it is intended to
answer whether a documented, execution-clean Solaire window existed after the
initial rejection, not to rewrite production decisions.
"""
from __future__ import annotations
import json, subprocess, statistics, sys, time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

OUT="research/solaire_baseline_rejection_watch_20260921.json"
START="2026-09-21T08:15:00+00:00"
END="2026-09-22T09:00:00+00:00"
BASELINE_AT="2026-09-21T08:20:11+00:00"
BASELINES={
    "FLOCK-EUR":{"price_eur":0.062025,"reason":"SPREAD_TOO_WIDE"},
    "XVG-EUR":{"price_eur":0.0026847,"reason":"STRUCTURAL_RANGE_TOO_NARROW"},
    "ICX-EUR":{"price_eur":0.008557,"reason":"INSUFFICIENT_EXECUTION_LIQUIDITY"},
    "SAGA-EUR":{"price_eur":0.033396,"reason":"STRUCTURAL_STOP_TOO_WIDE"},
}
MIN_VOL=75_000.0
MAX_SPREAD_PCT=0.5
MIN_RANGE=6.0
MAX_STOP=10.0
PAIR_MAX_SEC=600

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def git_versions(path):
    shas=subprocess.check_output(
        ["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--",path],
        text=True,
    ).split()
    out=[]; seen=set()
    for sha in shas:
        try:
            raw=subprocess.check_output(["git","show",f"{sha}:{path}"],text=True,stderr=subprocess.DEVNULL)
            obj=json.loads(raw)
        except Exception:
            continue
        marker=obj.get("generated_at_utc") or obj.get("checked_at_utc") or sha
        if marker in seen: continue
        seen.add(marker)
        out.append((sha,obj))
    return out

def candidate_row(obj,market):
    for key in ("tracking","watch"):
        for row in obj.get(key,[]) or []:
            if isinstance(row,dict) and row.get("market")==market:
                return row
    return None

def live_row(obj,market):
    for row in obj.get("markets",[]) or []:
        if isinstance(row,dict) and row.get("market")==market:
            return row
    return None

def nearest(rows,t0,max_sec=PAIR_MAX_SEC):
    best=None
    for row in rows:
        delta=abs(row["ts"]-t0)
        if best is None or delta<best["delta_sec"]:
            best={**row,"delta_sec":delta}
    return best if best and best["delta_sec"]<=max_sec else None

def raw_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        out.append((int(t),o,h,l,c,v))
    return sorted(out)

def forward_path(rows,start_ts,base,end_ts):
    if base is None or base<=0:return None
    first=((int(start_ts*1000)//300_000)+1)*300_000
    end=int(end_ts*1000)
    xs=[x for x in rows if first<=x[0]<=end]
    if not xs:return None
    hi=max(x[2] for x in xs); lo=min(x[3] for x in xs); close=xs[-1][4]
    return {
        "mfe_pct":round((hi/base-1)*100,4),
        "mae_pct":round((lo/base-1)*100,4),
        "close_return_pct":round((close/base-1)*100,4),
        "bars":len(xs),
        "high_eur":hi,"low_eur":lo,"close_eur":close,
    }

def plan_view(p):
    return {
        "valid":bool(p.get("valid")),
        "reason":None if p.get("valid") else p.get("reason"),
        "stop_distance_pct":finite(p.get("stop_distance_pct")),
        "net_rr_tp1":finite(p.get("net_rr_tp1")),
        "entry_eur":finite(p.get("entry_eur")),
        "stop_eur":finite(p.get("stop_eur")),
        "tp1_eur":finite(p.get("tp1_eur")),
    }

def first(rows,pred):
    return next((x for x in rows if pred(x)),None)

def slim(x):
    if not x:return None
    keys=("at_utc","signal_state","signal_score","signal_price_eur","return_from_baseline_pct",
          "quote_volume_24h_eur","spread_pct","range_15m_pct","stop_distance_pct",
          "execution_clean_proxy","fully_actionable_proxy","production_rejection_reason")
    return {k:x.get(k) for k in keys}

def main():
    now=time.time()
    baseline_ts=ts(BASELINE_AT)
    horizon_end=min(now,baseline_ts+24*3600)
    candidate_versions=git_versions("production_alert_candidates.json")
    alert_versions=git_versions("production_alert_status.json")
    live_versions=git_versions("bitvavo_live.json")

    alerts=[]
    for sha,obj in alert_versions:
        s=obj.get("checked_at_utc")
        if not s: continue
        alerts.append({
            "sha":sha,"at_utc":s,"ts":ts(s),
            "rejections":{x.get("market"):x.get("reason") for x in (obj.get("rejections") or []) if x.get("market")},
            "email":obj.get("email"),"reason":obj.get("reason"),
        })
    alerts.sort(key=lambda x:x["ts"])

    live_by={m:[] for m in BASELINES}
    for sha,obj in live_versions:
        s=obj.get("generated_at_utc")
        if not s:continue
        for market in BASELINES:
            row=live_row(obj,market)
            if not row:continue
            live_by[market].append({
                "sha":sha,"at_utc":s,"ts":ts(s),
                "last":finite(row.get("last")),
                "bid":finite(row.get("bid")),"ask":finite(row.get("ask")),
                "spread_pct":finite(row.get("spread_pct")),
                "quote_volume_24h_eur":finite(row.get("quote_volume_24h_eur")),
            })
    for rows in live_by.values(): rows.sort(key=lambda x:x["ts"])

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets") if m.get("market") in BASELINES}

    output={}
    for market,base in BASELINES.items():
        raw15=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
        raw5=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
        rr5=raw_rows(raw5)
        path=forward_path(rr5,baseline_ts,base["price_eur"],horizon_end)

        detector=[]
        for sha,obj in candidate_versions:
            s=obj.get("generated_at_utc")
            if not s:continue
            t0=ts(s)
            if t0<baseline_ts or t0>horizon_end:continue
            row=candidate_row(obj,market)
            if not row:continue

            l=nearest(live_by[market],t0)
            a=nearest(alerts,t0,420)
            f15=describe(closed_candles(raw15,"15m",t0),"15m")
            rng=finite(f15.get("consolidation_range_pct"))
            signal=finite(row.get("last"))
            ask=finite(l.get("ask")) if l else signal
            volume=finite(row.get("quote_volume_24h_eur"),
                          finite(l.get("quote_volume_24h_eur")) if l else None)
            spread=finite(l.get("spread_pct")) if l else None

            plan=None
            if f15.get("valid") and ask and ask>0 and market in metas:
                plan=plan_view(structural_plan({**row,"market":market,"ask":ask},f15,metas[market]))
            stop=finite((plan or {}).get("stop_distance_pct"))

            liquidity_pass=volume is not None and volume>=MIN_VOL
            spread_pass=spread is not None and spread<=MAX_SPREAD_PCT
            range_pass=rng is not None and rng>=MIN_RANGE
            plan_pass=bool((plan or {}).get("valid") and stop is not None and stop<=MAX_STOP)
            exec_clean=bool(liquidity_pass and spread_pass and range_pass and plan_pass)
            state=row.get("signal_state")
            rejection=(a.get("rejections") or {}).get(market) if a else None

            detector.append({
                "at_utc":s,"ts":t0,
                "signal_state":state,"signal_score":finite(row.get("signal_score")),
                "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
                "signal_price_eur":signal,
                "return_from_baseline_pct":round((signal/base["price_eur"]-1)*100,4) if signal else None,
                "quote_snapshot_at_utc":l.get("at_utc") if l else None,
                "quote_delta_seconds":round(l.get("delta_sec"),2) if l else None,
                "quote_volume_24h_eur":volume,
                "liquidity_pass":liquidity_pass,
                "spread_pct":spread,"spread_pass":spread_pass,
                "range_15m_pct":rng,"range_pass":range_pass,
                "stop_distance_pct":stop,"plan":plan,"plan_pass":plan_pass,
                "execution_clean_proxy":exec_clean,
                "fully_actionable_proxy":bool(state=="CONFIRMED_ACCELERATION" and exec_clean),
                "execution_clean_but_not_confirmed":bool(state!="CONFIRMED_ACCELERATION" and exec_clean),
                "production_rejection_reason":rejection,
            })

        live_after=[x for x in live_by[market] if baseline_ts<=x["ts"]<=horizon_end]
        first_volume=first(live_after,lambda x:finite(x.get("quote_volume_24h_eur"),0)>=MIN_VOL)
        first_vol_spread=first(live_after,lambda x:finite(x.get("quote_volume_24h_eur"),0)>=MIN_VOL
                               and finite(x.get("spread_pct"),999)<=MAX_SPREAD_PCT)

        output[market]={
            "baseline":{"at_utc":BASELINE_AT,"price_eur":base["price_eur"],"reason":base["reason"]},
            "elapsed_hours":round((horizon_end-baseline_ts)/3600,3),
            "trajectory_to_horizon":path,
            "snapshot_count":len(detector),
            "first_volume_pass":first_volume,
            "first_volume_and_spread_pass":first_vol_spread,
            "first_tracked":slim(first(detector,lambda x:True)),
            "first_confirmed":slim(first(detector,lambda x:x["signal_state"]=="CONFIRMED_ACCELERATION")),
            "first_execution_clean":slim(first(detector,lambda x:x["execution_clean_proxy"])),
            "first_execution_clean_but_not_confirmed":slim(first(detector,lambda x:x["execution_clean_but_not_confirmed"])),
            "first_fully_actionable_proxy":slim(first(detector,lambda x:x["fully_actionable_proxy"])),
            "detector_timeline":detector,
        }

    out={
        "schema":"solaire_baseline_rejection_watch_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "baseline_at_utc":BASELINE_AT,
        "horizon_end_utc":utc(horizon_end),
        "horizon_complete_24h":bool(now>=baseline_ts+24*3600),
        "rules":{"min_quote_volume_24h_eur":MIN_VOL,"max_spread_pct":MAX_SPREAD_PCT,
                 "min_range_15m_pct":MIN_RANGE,"max_stop_distance_pct":MAX_STOP},
        "markets":output,
        "limitations":[
            "historical bid/ask and 24h volume are paired from nearest persisted bitvavo_live snapshot within 10 minutes",
            "15m structure is rebuilt with current feature/risk code and is therefore a current-code counterfactual",
            "freshness is not replayed historically",
            "classification is evidence-oriented; no automatic SUPPORTED/FALSE_NEGATIVE label is imposed",
        ],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_BASELINE_REJECTION_WATCH "+json.dumps({
        "horizon_complete_24h":out["horizon_complete_24h"],
        "markets":{m:{
            "trajectory":v["trajectory_to_horizon"],
            "first_execution_clean":v["first_execution_clean"],
            "first_fully_actionable_proxy":v["first_fully_actionable_proxy"],
        } for m,v in output.items()},
    },ensure_ascii=False))

if __name__=="__main__":
    main()
