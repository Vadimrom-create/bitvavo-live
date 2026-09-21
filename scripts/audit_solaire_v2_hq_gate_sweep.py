#!/usr/bin/env python3
"""Adversarial gate sweep for high-quality BUILDING episodes on 2026-09-21.

Uses the historical full-universe timing replay and rebuilds the 15m structure
at the first HQ BUILDING timestamp. Sweeps the fixed consolidation-range
threshold and structural-plan net-RR threshold while keeping the 10% maximum
stop unchanged. Research-only: historical bid/ask spread and exact historical
rolling 24h volume are not reconstructed, so this does not authorize production
changes by itself.
"""
from __future__ import annotations
import json, statistics, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

TIMING="research/solaire_v2_detection_timing_20260921.json"
OUT="research/solaire_v2_hq_gate_sweep_20260921.json"
MIN_LIQ=75_000.0
MAX_STOP=10.0
RANGES=(3.0,4.0,5.0,6.0)
RRS=(1.10,1.25,1.50)

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def stats(xs):
    return {
        "n":len(xs),
        "mfe_ge_5pct":sum(x["mfe_pct"]>=5 for x in xs),
        "clean_mfe_ge5_mae_gt_minus5":sum(x["mfe_pct"]>=5 and x["mae_pct"]>-5 for x in xs),
        "mae_le_minus5pct":sum(x["mae_pct"]<=-5 for x in xs),
        "median_mfe_pct":med([x["mfe_pct"] for x in xs]),
        "median_mae_pct":med([x["mae_pct"] for x in xs]),
        "median_close_pct":med([x["close_pct"] for x in xs]),
    }

def main():
    data=json.loads(Path(TIMING).read_text())
    markets=data.get("markets") or []
    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets")
           if m.get("quote")=="EUR" and m.get("status")=="trading"}

    episodes=[]; errors=[]
    for row in markets:
        market=row.get("market")
        if finite(row.get("quote_volume_24h_eur"),0.0)<MIN_LIQ: continue
        hq=((row.get("signals") or {}).get("high_quality_building") or {})
        fwd=hq.get("forward_4h") or {}
        if not hq or not fwd.get("complete"): continue
        ts=finite(hq.get("ts")); price=finite(hq.get("price_eur"))
        if ts is None or price is None or price<=0 or market not in metas: continue
        try:
            raw=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            features=describe(closed_candles(raw,"15m",ts),"15m")
            if not features.get("valid"): continue
            rng=finite(features.get("consolidation_range_pct"))
            atr=finite(features.get("atr14_pct"))
            plans={}
            for rr in RRS:
                p=structural_plan({"market":market,"ask":price},features,metas[market],min_net_rr=rr)
                plans[str(rr)]={
                    "valid":bool(p.get("valid")),
                    "reason":None if p.get("valid") else p.get("reason"),
                    "stop_distance_pct":finite(p.get("stop_distance_pct")),
                    "net_rr_tp1":finite(p.get("net_rr_tp1")),
                }
            episodes.append({
                "market":market,
                "hq_at_utc":hq.get("at_utc"),
                "price_eur":price,
                "score":finite(hq.get("score")),
                "evidence_count":int(hq.get("evidence_count") or 0),
                "range_15m_pct":rng,
                "atr14_pct":atr,
                "mfe_pct":finite(fwd.get("mfe_pct")),
                "mae_pct":finite(fwd.get("mae_pct")),
                "close_pct":finite(fwd.get("close_pct")),
                "plans":plans,
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    matrix={}
    for rmin in RANGES:
        matrix[str(rmin)]={}
        for rr in RRS:
            eligible=[]
            for e in episodes:
                p=e["plans"][str(rr)]
                stop=finite(p.get("stop_distance_pct"))
                if e["range_15m_pct"] is None or e["range_15m_pct"]<rmin: continue
                if not p.get("valid") or stop is None or stop>MAX_STOP: continue
                eligible.append(e)
            matrix[str(rmin)][str(rr)]=stats(eligible)

    baseline=matrix["6.0"]["1.5"]
    by_reason=Counter()
    by_reason_outcomes={}
    for e in episodes:
        p=e["plans"]["1.5"]
        if p.get("valid"):
            reason="VALID_PLAN"
        else:
            reason=p.get("reason") or "UNKNOWN"
        by_reason[reason]+=1
        by_reason_outcomes.setdefault(reason,[]).append(e)
    reason_summary={k:stats(v) for k,v in by_reason_outcomes.items()}

    # Transparent candidate frontier: no winner is selected. Show deltas versus
    # the current structure/RR pair so a human can assess trade-offs.
    deltas=[]
    for rmin in RANGES:
        for rr in RRS:
            s=matrix[str(rmin)][str(rr)]
            deltas.append({
                "range_min_pct":rmin,"min_net_rr":rr,
                **s,
                "delta_n_vs_current":s["n"]-baseline["n"],
                "delta_mfe_ge5_vs_current":s["mfe_ge_5pct"]-baseline["mfe_ge_5pct"],
                "delta_mae_le_minus5_vs_current":s["mae_le_minus5pct"]-baseline["mae_le_minus5pct"],
                "delta_median_close_pp_vs_current":(
                    round(s["median_close_pct"]-baseline["median_close_pct"],4)
                    if s["median_close_pct"] is not None and baseline["median_close_pct"] is not None else None
                ),
            })

    out={
        "schema":"solaire_v2_hq_gate_sweep_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "population":"first HQ BUILDING per market; current 24h quote volume >=75k; complete 4h outcome",
        "limitations":[
            "historical bid/ask spread not reconstructed",
            "exact historical rolling 24h quote volume not reconstructed; current replay volume used as liquidity screen",
            "historical close used as execution-price proxy",
            "single-session stress test; not sufficient alone for production promotion",
        ],
        "episode_count":len(episodes),
        "current_pair":{"range_min_pct":6.0,"min_net_rr":1.5,"max_stop_pct":MAX_STOP,"stats":baseline},
        "matrix":matrix,
        "deltas_vs_current":deltas,
        "plan_reason_summary_rr_1_5":reason_summary,
        "episodes":episodes,
        "errors":errors,
    }
    atomic_json(OUT,out)
    print("SOLAIRE_HQ_GATE_SWEEP "+json.dumps({
        "episode_count":len(episodes),"current":baseline,"matrix":matrix,
        "plan_reason_summary_rr_1_5":reason_summary
    },ensure_ascii=False))

if __name__=="__main__": main()
