#!/usr/bin/env python3
"""Reconstruct ICX-EUR executability through the 2026-09-21 move.

Uses repository history for:
- production_alert_candidates.json: actual Solaire detector snapshots
- live_quotes.json: validated Bitvavo last/bid/ask/spread snapshots
- bitvavo_live.json: 24h-volume snapshots

Rebuilds current 15m structural features from historical Bitvavo candles.
The structural plan is computed from the detector's own signal price to avoid
look-ahead when a nearby quote snapshot is several minutes later. Historical
spread is accepted only when a validated live_quotes snapshot is close enough.

Research-only: no production decisions are changed.
"""
from __future__ import annotations
import json, subprocess, sys, time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

MARKET="ICX-EUR"
START="2026-09-21T08:00:00+00:00"
END="2026-09-21T21:20:00+00:00"
USER_BASELINE_AT="2026-09-21T08:20:11+00:00"
USER_BASELINE_PRICE=0.008557
MIN_VOL=75_000.0
MAX_SPREAD_PCT=0.5
MIN_RANGE=6.0
MAX_STOP=10.0
MAX_QUOTE_DELTA_SEC=180
OUT="research/icx_executability_timeline_20260921.json"

def ts(s):
    return datetime.fromisoformat(s.replace("Z","+00:00")).timestamp()

def git_versions(path):
    cmd=["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--",path]
    shas=subprocess.check_output(cmd,text=True).split()
    out=[]; seen=set()
    for sha in shas:
        try:
            raw=subprocess.check_output(["git","show",f"{sha}:{path}"],text=True,stderr=subprocess.DEVNULL)
            obj=json.loads(raw)
        except Exception:
            continue
        marker=(obj.get("generated_at_utc") or obj.get("checked_at_utc") or
                obj.get("requested_at_utc") or obj.get("received_at_utc") or sha)
        if marker in seen: continue
        seen.add(marker)
        out.append((sha,obj))
    return out

def market_from_live(obj):
    for r in obj.get("markets",[]) or []:
        if r.get("market")==MARKET: return r
    return None

def market_from_quotes(obj):
    row=(obj.get("markets") or {}).get(MARKET)
    return row if isinstance(row,dict) else None

def market_from_candidates(obj):
    for key in ("tracking","watch"):
        for r in obj.get(key,[]) or []:
            if r.get("market")==MARKET: return r
    return None

def nearest(rows,t0,max_sec):
    best=None
    for x in rows:
        d=abs(x["ts"]-t0)
        if best is None or d<best["delta_sec"]:
            best={**x,"delta_sec":d}
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

def forward(rows,t0,base,hours):
    if not base or base<=0: return None
    start=((int(t0*1000)//300_000)+1)*300_000
    end=int((t0+hours*3600)*1000)
    xs=[x for x in rows if start<=x[0]<end]
    if not xs: return None
    return {
        "mfe_pct":round((max(x[2] for x in xs)/base-1)*100,4),
        "mae_pct":round((min(x[3] for x in xs)/base-1)*100,4),
        "close_return_pct":round((xs[-1][4]/base-1)*100,4),
        "bars":len(xs),
    }

def first(rows,pred):
    return next((r for r in rows if pred(r)),None)

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

def main():
    volume_snaps=[]
    for sha,obj in git_versions("bitvavo_live.json"):
        s=obj.get("generated_at_utc")
        if not s: continue
        row=market_from_live(obj)
        if not row: continue
        volume_snaps.append({
            "at_utc":s,"ts":ts(s),"sha":sha,
            "last":finite(row.get("last")),
            "quote_volume_24h_eur":finite(row.get("quote_volume_24h_eur")),
            "change_24h_pct":finite(row.get("change_24h_pct")),
        })
    volume_snaps.sort(key=lambda x:x["ts"])

    quote_snaps=[]
    for sha,obj in git_versions("live_quotes.json"):
        s=obj.get("received_at_utc") or obj.get("requested_at_utc")
        if not s: continue
        row=market_from_quotes(obj)
        if not row: continue
        quote_snaps.append({
            "at_utc":s,"ts":ts(s),"sha":sha,
            "last":finite(row.get("last")),
            "bid":finite(row.get("best_bid")),
            "ask":finite(row.get("best_ask")),
            "spread_pct":finite(row.get("spread_pct")),
            "valid":bool(row.get("valid",obj.get("valid",False))),
        })
    quote_snaps.sort(key=lambda x:x["ts"])

    candidates=[]
    for sha,obj in git_versions("production_alert_candidates.json"):
        s=obj.get("generated_at_utc")
        if not s: continue
        row=market_from_candidates(obj)
        if not row: continue
        candidates.append({"at_utc":s,"ts":ts(s),"sha":sha,"row":row})
    candidates.sort(key=lambda x:x["ts"])

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    meta=next(m for m in client.get("/markets") if m.get("market")==MARKET)
    raw15=client.get("/"+MARKET+"/candles",{"interval":"15m","limit":200},cache=False)
    raw5=client.get("/"+MARKET+"/candles",{"interval":"5m","limit":400},cache=False)
    rr5=raw_rows(raw5)

    timeline=[]
    for c in candidates:
        row=c["row"]; t0=c["ts"]
        q=nearest(quote_snaps,t0,MAX_QUOTE_DELTA_SEC)
        v=nearest(volume_snaps,t0,600)
        f15=describe(closed_candles(raw15,"15m",t0),"15m")
        f5=describe(closed_candles(raw5,"5m",t0),"5m")
        rng=finite(f15.get("consolidation_range_pct"))
        volume=finite(row.get("quote_volume_24h_eur"),finite((v or {}).get("quote_volume_24h_eur"),0.0))
        spread=finite(q.get("spread_pct")) if q and q.get("valid") else None
        liquidity_pass=volume>=MIN_VOL
        spread_pass=spread is not None and spread<=MAX_SPREAD_PCT
        range_pass=rng is not None and rng>=MIN_RANGE

        px=finite(row.get("last"))
        signal_plan=None
        if f15.get("valid") and px and px>0:
            signal_plan=plan_view(structural_plan({**row,"market":MARKET,"ask":px},f15,meta))
        stop=finite((signal_plan or {}).get("stop_distance_pct"))
        plan_pass=bool((signal_plan or {}).get("valid") and stop is not None and stop<=MAX_STOP)

        quote_plan=None
        if q and f15.get("valid") and finite(q.get("ask")) and q["ask"]>0:
            quote_plan=plan_view(structural_plan({**row,"market":MARKET,"ask":q["ask"]},f15,meta))

        micro5_plan=None
        if f5.get("valid") and px and px>0:
            micro5_plan=plan_view(structural_plan({**row,"market":MARKET,"ask":px},f5,meta))
        micro5_stop=finite((micro5_plan or {}).get("stop_distance_pct"))
        micro5_plan_pass=bool((micro5_plan or {}).get("valid") and micro5_stop is not None and micro5_stop<=MAX_STOP)

        execution_clean=bool(liquidity_pass and spread_pass and range_pass and plan_pass)
        state=row.get("signal_state")
        timeline.append({
            "at_utc":c["at_utc"],
            "signal_state":state,
            "signal_score":finite(row.get("signal_score")),
            "evidence_count":int((row.get("acceleration") or {}).get("evidence_count") or 0),
            "components":(row.get("acceleration") or {}).get("components") or {},
            "signal_price_eur":px,
            "return_from_user_baseline_pct":round((px/USER_BASELINE_PRICE-1)*100,4) if px else None,
            "quote_volume_24h_eur":volume,
            "liquidity_pass":liquidity_pass,
            "nearest_validated_quote_at_utc":q.get("at_utc") if q else None,
            "quote_delta_seconds":round(q.get("delta_sec"),2) if q else None,
            "bid_eur":finite(q.get("bid")) if q else None,
            "ask_eur":finite(q.get("ask")) if q else None,
            "spread_pct":spread,
            "spread_pass":spread_pass,
            "range_15m_pct":rng,
            "range_pass_6pct":range_pass,
            "atr14_15m_pct":finite(f15.get("atr14_pct")),
            "return_1h_15m_pct":finite(f15.get("return_4bar_pct")),
            "return_4h_15m_pct":finite(f15.get("return_16bar_pct")),
            "structural_plan_signal_price":signal_plan,
            "structural_plan_near_quote":quote_plan,
            "plan_and_stop_pass":plan_pass,
            "micro5_range_pct":finite(f5.get("consolidation_range_pct")),
            "micro5_atr14_pct":finite(f5.get("atr14_pct")),
            "micro5_return_1h_pct":finite(f5.get("return_12bar_pct")),
            "micro5_structural_plan_signal_price":micro5_plan,
            "micro5_plan_and_stop_pass":micro5_plan_pass,
            "execution_clean_proxy":execution_clean,
            "fully_actionable_proxy":bool(state=="CONFIRMED_ACCELERATION" and execution_clean),
            "execution_clean_but_not_confirmed":bool(state!="CONFIRMED_ACCELERATION" and execution_clean),
            "forward_1h":forward(rr5,t0,px,1),
            "forward_4h":forward(rr5,t0,px,4),
        })

    baseline_ts=ts(USER_BASELINE_AT)
    first_volume=first(volume_snaps,lambda r:r["ts"]>=baseline_ts and finite(r.get("quote_volume_24h_eur"),0)>=MIN_VOL)
    keys={
        "first_detected":first(timeline,lambda r:True),
        "first_liquidity_pass_while_detected":first(timeline,lambda r:r["liquidity_pass"]),
        "first_liquidity_and_spread_pass_while_detected":first(timeline,lambda r:r["liquidity_pass"] and r["spread_pass"]),
        "first_execution_clean_while_detected":first(timeline,lambda r:r["execution_clean_proxy"]),
        "first_execution_clean_but_not_confirmed":first(timeline,lambda r:r["execution_clean_but_not_confirmed"]),
        "first_fully_actionable_proxy":first(timeline,lambda r:r["fully_actionable_proxy"]),
    }

    def slim(x):
        if not x: return None
        return {k:x.get(k) for k in ("at_utc","last","quote_volume_24h_eur","change_24h_pct")}

    out={
        "schema":"icx_executability_timeline_v2","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "market":MARKET,
        "user_baseline":{"at_utc":USER_BASELINE_AT,"price_eur":USER_BASELINE_PRICE},
        "rules":{"min_quote_volume_24h_eur":MIN_VOL,"max_spread_pct":MAX_SPREAD_PCT,
                 "min_range_15m_pct":MIN_RANGE,"max_stop_distance_pct":MAX_STOP,
                 "max_validated_quote_delta_seconds":MAX_QUOTE_DELTA_SEC},
        "history_coverage":{"volume_snapshots":len(volume_snaps),"validated_quote_snapshots":len(quote_snaps),
                            "detector_snapshots":len(timeline)},
        "first_historical_volume_pass":slim(first_volume),
        "key_detector_transitions":keys,
        "timeline":timeline,
        "limitations":[
            "5m structural plan is an audit counterfactual only; production uses the 15m structural plan",
            "validated book spread is paired only when live_quotes is within 180 seconds of the detector snapshot",
            "structural plan pass/fail uses the detector signal price to avoid look-ahead from a later quote",
            "15m structural features rebuilt with current feature code from historical Bitvavo candles",
            "freshness check omitted in historical replay",
        ],
    }
    atomic_json(OUT,out)
    print("ICX_EXECUTABILITY_TIMELINE "+json.dumps({
        "coverage":out["history_coverage"],
        "first_historical_volume_pass":out["first_historical_volume_pass"],
        "key_detector_transitions":keys,
    },ensure_ascii=False))

if __name__=="__main__": main()
