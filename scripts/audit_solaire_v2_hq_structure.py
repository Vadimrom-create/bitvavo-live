#!/usr/bin/env python3
"""Targeted historical structure audit for delayed HQ BUILDING episodes.

For same-market episodes where high-quality BUILDING preceded CONFIRMED, rebuilds
the 15m structure at both timestamps from Bitvavo candles. It tests the
structure/risk parts of the current final gate using historical closes as price.
Historical bid/ask spread and exact historical rolling 24h volume are not
reconstructed and are explicitly excluded from the verdict.
"""
from __future__ import annotations
import json, statistics, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

PAIRED="research/solaire_v2_hq_building_vs_confirmed_20260921.json"
TIMING="research/solaire_v2_detection_timing_20260921.json"
OUT="research/solaire_v2_hq_structure_20260921.json"
MIN_RANGE=6.0
MAX_STOP=10.0

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def snapshot(raw, ts, price, meta, market):
    cs=closed_candles(raw,"15m",ts)
    f=describe(cs,"15m")
    rng=finite(f.get("consolidation_range_pct"))
    plan=structural_plan({"market":market,"ask":price},f,meta) if f.get("valid") else {"valid":False,"reason":"INVALID_STRUCTURE"}
    stop=finite(plan.get("stop_distance_pct"))
    return {
        "price_eur":price,
        "range_15m_pct":rng,
        "range_ready_6pct":bool(rng is not None and rng>=MIN_RANGE),
        "atr14_pct":finite(f.get("atr14_pct")),
        "support_eur":finite(f.get("support_eur")),
        "plan_valid":bool(plan.get("valid")),
        "plan_reason":None if plan.get("valid") else plan.get("reason"),
        "stop_distance_pct":stop,
        "stop_within_10pct":bool(stop is not None and stop<=MAX_STOP),
        "structure_gate_pass_ex_spread_liquidity":bool(
            rng is not None and rng>=MIN_RANGE and plan.get("valid") and stop is not None and stop<=MAX_STOP
        ),
    }

def main():
    paired=json.loads(Path(PAIRED).read_text())
    timing=json.loads(Path(TIMING).read_text())
    timing_by={r["market"]:r for r in timing.get("markets",[]) if r.get("market")}
    delayed=[r for r in paired.get("rows",[]) if finite(r.get("delay_minutes"),0)>0]

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"}

    rows=[]; errors=[]
    for p in delayed:
        market=p.get("market")
        trow=timing_by.get(market) or {}
        sig=trow.get("signals") or {}
        hq=sig.get("high_quality_building") or {}
        cf=sig.get("current_confirmed") or {}
        hq_ts=finite(hq.get("ts")); cf_ts=finite(cf.get("ts"))
        hq_price=finite(hq.get("price_eur")); cf_price=finite(cf.get("price_eur"))
        if None in (hq_ts,cf_ts,hq_price,cf_price) or market not in metas: continue
        try:
            raw=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            hs=snapshot(raw,hq_ts,hq_price,metas[market],market)
            cs=snapshot(raw,cf_ts,cf_price,metas[market],market)
            rows.append({
                "market":market,
                "delay_minutes":p.get("delay_minutes"),
                "price_change_hq_to_confirmed_pct":p.get("price_change_hq_to_confirmed_pct"),
                "hq_mfe_4h_pct":p.get("hq_mfe_4h_pct"),
                "confirmed_mfe_4h_pct":p.get("confirmed_mfe_4h_pct"),
                "hq_mae_4h_pct":p.get("hq_mae_4h_pct"),
                "confirmed_mae_4h_pct":p.get("confirmed_mae_4h_pct"),
                "hq":hs,"confirmed":cs,
                "historical_spread_available":False,
                "historical_rolling_24h_volume_available":False,
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    hq_range=[r for r in rows if r["hq"]["range_ready_6pct"]]
    cf_range=[r for r in rows if r["confirmed"]["range_ready_6pct"]]
    hq_struct=[r for r in rows if r["hq"]["structure_gate_pass_ex_spread_liquidity"]]
    cf_struct=[r for r in rows if r["confirmed"]["structure_gate_pass_ex_spread_liquidity"]]
    summary={
        "delayed_pairs_evaluated":len(rows),
        "hq_range_ready_6pct":len(hq_range),
        "confirmed_range_ready_6pct":len(cf_range),
        "hq_structure_gate_pass_ex_spread_liquidity":len(hq_struct),
        "confirmed_structure_gate_pass_ex_spread_liquidity":len(cf_struct),
        "median_hq_range_pct":med([r["hq"]["range_15m_pct"] for r in rows]),
        "median_confirmed_range_pct":med([r["confirmed"]["range_15m_pct"] for r in rows]),
        "median_hq_stop_distance_pct":med([r["hq"]["stop_distance_pct"] for r in rows]),
        "median_confirmed_stop_distance_pct":med([r["confirmed"]["stop_distance_pct"] for r in rows]),
        "hq_range_blocked_but_mfe_ge5":sum((not r["hq"]["range_ready_6pct"]) and finite(r.get("hq_mfe_4h_pct"),-999)>=5 for r in rows),
        "hq_structure_pass_and_mfe_ge5":sum(r["hq"]["structure_gate_pass_ex_spread_liquidity"] and finite(r.get("hq_mfe_4h_pct"),-999)>=5 for r in rows),
    }
    out={"schema":"solaire_v2_hq_structure_audit_v1","generated_at_utc":utc(),
         "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
         "limitations":["historical spread not reconstructed","historical rolling 24h volume not reconstructed","historical close used as execution-price proxy"],
         "summary":summary,"rows":rows,"errors":errors}
    atomic_json(OUT,out)
    print("SOLAIRE_HQ_STRUCTURE "+json.dumps(summary,ensure_ascii=False))

if __name__=="__main__": main()
