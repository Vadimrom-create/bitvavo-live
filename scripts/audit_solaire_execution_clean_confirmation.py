#!/usr/bin/env python3
"""Audit first-confirmed execution-clean Solaire episodes by confirmation scope.

Reconstructs the first CONFIRMED observation of each tracking episode, rebuilds
the current execution gate from historical Bitvavo snapshots, and measures
forward 1h/4h outcomes. Splits MULTI_TIMEFRAME vs FAST_COMPOSITE_ONLY and
3-vs-4+-evidence confirmations.

Research-only. No production behavior changes.
"""
from __future__ import annotations
import json, statistics, subprocess, sys, time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

START="2026-09-21T08:00:00+00:00"
END="2026-09-22T08:30:00+00:00"
OUT="research/solaire_execution_clean_confirmation_20260921.json"
MIN_VOL=75_000.0
MAX_SPREAD_PCT=0.5
MIN_RANGE=6.0
MAX_STOP=10.0
PAIR_MAX_SEC=600

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def med(xs):
    xs=[x for x in xs if x is not None]
    if not xs:return None
    xs=sorted(xs); n=len(xs)
    return round(xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2,4)

def git_versions(path):
    shas=subprocess.check_output(
        ["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--",path],
        text=True,
    ).split()
    out=[];seen=set()
    for sha in shas:
        try:
            obj=json.loads(subprocess.check_output(["git","show",f"{sha}:{path}"],text=True,stderr=subprocess.DEVNULL))
        except Exception:
            continue
        marker=obj.get("generated_at_utc") or obj.get("checked_at_utc") or sha
        if marker in seen:continue
        seen.add(marker); out.append((sha,obj))
    return out

def live_row(obj,market):
    for r in obj.get("markets",[]) or []:
        if isinstance(r,dict) and r.get("market")==market:return r
    return None

def nearest(rows,t0):
    best=None
    for r in rows:
        d=abs(r["ts"]-t0)
        if best is None or d<best["delta_sec"]:best={**r,"delta_sec":d}
    return best if best and best["delta_sec"]<=PAIR_MAX_SEC else None

def raw_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6:continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals):continue
        t,o,h,l,c,v=vals; out.append((int(t),o,h,l,c,v))
    return sorted(out)

def forward(rows,start_ts,base,hours):
    if base is None or base<=0:return None
    first=((int(start_ts*1000)//300_000)+1)*300_000
    end=int((start_ts+hours*3600)*1000)
    xs=[x for x in rows if first<=x[0]<end]
    if not xs:return None
    return {
        "mfe_pct":round((max(x[2] for x in xs)/base-1)*100,4),
        "mae_pct":round((min(x[3] for x in xs)/base-1)*100,4),
        "close_return_pct":round((xs[-1][4]/base-1)*100,4),
        "bars":len(xs),
    }

def gate(row,t0,live,raw15,meta):
    q=nearest(live,t0)
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
            "entry_eur":finite(p.get("entry_eur")),
            "stop_distance_pct":finite(p.get("stop_distance_pct")),
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
        "quote_volume_24h_eur":vol,
        "spread_pct":spread,
        "range_15m_pct":rng,
        "stop_distance_pct":stop,
        "entry_eur":finite((plan or {}).get("entry_eur")),
        "quote_delta_seconds":round(q.get("delta_sec"),2) if q else None,
    }

def stats(rows):
    f=[r for r in rows if r.get("forward_4h") and r["forward_4h"].get("bars",0)>=36]
    return {
        "n":len(f),
        "mfe_ge_5pct":sum(r["forward_4h"]["mfe_pct"]>=5 for r in f),
        "clean_mfe_ge5_mae_gt_minus5":sum(r["forward_4h"]["mfe_pct"]>=5 and r["forward_4h"]["mae_pct"]>-5 for r in f),
        "mae_le_minus5pct":sum(r["forward_4h"]["mae_pct"]<=-5 for r in f),
        "median_mfe_pct":med([r["forward_4h"]["mfe_pct"] for r in f]),
        "median_mae_pct":med([r["forward_4h"]["mae_pct"] for r in f]),
        "median_close_pct":med([r["forward_4h"]["close_return_pct"] for r in f]),
    }

def main():
    cvs=[]
    for sha,obj in git_versions("production_alert_candidates.json"):
        s=obj.get("generated_at_utc")
        if s:cvs.append({"sha":sha,"at_utc":s,"ts":ts(s),"obj":obj})
    cvs.sort(key=lambda x:x["ts"])

    markets=set()
    for c in cvs:
        for r in c["obj"].get("tracking",[]) or []:
            if isinstance(r,dict) and r.get("market"):markets.add(r["market"])

    live_by={m:[] for m in markets}
    for sha,obj in git_versions("bitvavo_live.json"):
        s=obj.get("generated_at_utc")
        if not s:continue
        t0=ts(s)
        for m in markets:
            row=live_row(obj,m)
            if not row:continue
            live_by[m].append({
                "at_utc":s,"ts":t0,
                "last":finite(row.get("last")),"bid":finite(row.get("bid")),"ask":finite(row.get("ask")),
                "spread_pct":finite(row.get("spread_pct")),
                "quote_volume_24h_eur":finite(row.get("quote_volume_24h_eur")),
            })
    for xs in live_by.values():xs.sort(key=lambda x:x["ts"])

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets") if m.get("market") in markets}
    raw15={};raw5={}

    active=set(); handled=set(); episode_no={}; rows=[]
    for c in cvs:
        tracking={r.get("market"):r for r in (c["obj"].get("tracking") or []) if isinstance(r,dict) and r.get("market")}
        watch={r.get("market"):r for r in (c["obj"].get("watch") or []) if isinstance(r,dict) and r.get("market")}
        current=set(tracking)
        ended=active-current
        for m in ended:
            handled.discard((m,episode_no.get(m,0)))
        for m in current-active:
            episode_no[m]=episode_no.get(m,0)+1
        active=current

        for market,row in watch.items():
            key=(market,episode_no.get(market,0))
            if key in handled:continue
            handled.add(key)
            if market not in metas:continue
            if market not in raw15:
                raw15[market]=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
                raw5[market]=raw_rows(client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False))
            g=gate(row,c["ts"],live_by.get(market,[]),raw15[market],metas[market])
            if not g["passed"]:continue
            acc=row.get("acceleration") or {}
            comp=acc.get("components") or {}
            c15=finite(comp.get("confirmation_15m"),0)
            tf=acc.get("timeframe_confirmation_15m")
            if tf is None:tf=c15>=3.0
            scope=acc.get("confirmation_scope") or ("MULTI_TIMEFRAME" if tf else "FAST_COMPOSITE_ONLY")
            evidence=int(acc.get("evidence_count") or 0)
            baseline=g.get("entry_eur") or finite(row.get("last"))
            rows.append({
                "market":market,"episode":episode_no.get(market,0),"at_utc":c["at_utc"],
                "signal_price_eur":finite(row.get("last")),"entry_eur":baseline,
                "signal_score":finite(row.get("signal_score")),"evidence_count":evidence,
                "confirmation_15m_component":c15,"confirmation_scope":scope,
                "timeframe_confirmation_15m":bool(tf),
                "gate":g,
                "forward_1h":forward(raw5[market],c["ts"],baseline,1),
                "forward_4h":forward(raw5[market],c["ts"],baseline,4),
            })

    cohorts={
        "all_execution_clean":rows,
        "multi_timeframe":[r for r in rows if r["confirmation_scope"]=="MULTI_TIMEFRAME"],
        "fast_composite_only":[r for r in rows if r["confirmation_scope"]=="FAST_COMPOSITE_ONLY"],
        "evidence_3":[r for r in rows if r["evidence_count"]==3],
        "evidence_4plus":[r for r in rows if r["evidence_count"]>=4],
        "fast_evidence_3":[r for r in rows if r["confirmation_scope"]=="FAST_COMPOSITE_ONLY" and r["evidence_count"]==3],
    }
    out={
        "schema":"solaire_execution_clean_confirmation_audit_v1",
        "generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "episode_count":len(rows),
        "summary_4h":{k:stats(v) for k,v in cohorts.items()},
        "events":rows,
        "limitations":[
            "single-session evidence",
            "execution gate reconstructed with nearest persisted Bitvavo snapshot within 10 minutes",
            "historical freshness is not replayed",
            "current structural/risk code is used as the counterfactual gate",
        ],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_EXECUTION_CLEAN_CONFIRMATION "+json.dumps(out["summary_4h"],ensure_ascii=False))

if __name__=="__main__":main()
