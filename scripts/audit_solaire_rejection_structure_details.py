#!/usr/bin/env python3
"""Historical structural diagnostics for Solaire final-gate rejections.

Rebuilds 5m/15m detector features and the structural plan at the rejection
timestamp for STRUCTURAL_RANGE_TOO_NARROW and STRUCTURAL_STOP_TOO_WIDE events.
Research-only; historical exact bid/ask is not reconstructed and the recorded
rejection price is used as the ask proxy.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_acceleration import acceleration_signal
from research.risk import structural_plan

JOURNAL="production_rejection_shadow_journal.json"
OUT="research/solaire_rejection_structure_details_20260921.json"
REASONS={"STRUCTURAL_RANGE_TOO_NARROW","STRUCTURAL_STOP_TOO_WIDE"}

def main():
    journal=json.loads(Path(JOURNAL).read_text())
    events=[e for e in journal.get("events",[]) if e.get("first_rejection_reason") in REASONS]

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets")
           if m.get("quote")=="EUR" and m.get("status")=="trading"}

    rows=[]; errors=[]
    for e in events:
        market=e.get("market"); ts=finite(e.get("rejected_ts")); px=finite(e.get("rejection_price_eur"))
        if not market or ts is None or px is None or px<=0 or market not in metas: continue
        try:
            r5=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
            r15=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            f5=describe(closed_candles(r5,"5m",ts),"5m")
            f15=describe(closed_candles(r15,"15m",ts),"15m")
            acc=acceleration_signal({"features":{"5m":f5,"15m":f15}})
            plan=structural_plan({"market":market,"ask":px},f15,metas[market])
            rng=finite(f15.get("consolidation_range_pct"))
            atr=finite(f15.get("atr14_pct"))
            rows.append({
                "market":market,
                "event_id":e.get("event_id"),
                "first_rejection_reason":e.get("first_rejection_reason"),
                "rejected_at_utc":e.get("rejected_at_utc"),
                "rejection_price_eur":px,
                "recorded_signal_score":finite(e.get("signal_score")),
                "replayed_signal_score":finite(acc.get("score")),
                "replayed_evidence_count":int(acc.get("evidence_count") or 0),
                "replayed_components":acc.get("components") or {},
                "range_15m_pct":rng,
                "atr14_15m_pct":atr,
                "range_to_atr_ratio":round(rng/atr,4) if rng is not None and atr not in (None,0) else None,
                "return_1h_pct":finite(f15.get("return_4bar_pct")),
                "return_4h_pct":finite(f15.get("return_16bar_pct")),
                "relative_volume_15m":finite(f15.get("relative_volume")),
                "volume_4_vs_prev4_15m":finite(f15.get("volume_4_vs_prev4")),
                "support_eur":finite(f15.get("support_eur")),
                "structural_plan_valid":bool(plan.get("valid")),
                "structural_plan_reason":None if plan.get("valid") else plan.get("reason"),
                "stop_distance_pct":finite(plan.get("stop_distance_pct")),
                "net_rr_tp1":finite(plan.get("net_rr_tp1")),
                "stop_eur":finite(plan.get("stop_eur")),
                "tp1_eur":finite(plan.get("tp1_eur")),
                "evaluations":e.get("evaluations") or {},
                "original_condition_resolved":bool(e.get("original_condition_resolved")),
                "first_later_qualifying_entry":e.get("first_later_qualifying_entry"),
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    out={
        "schema":"solaire_rejection_structure_details_v1",
        "generated_at_utc":utc(),
        "research_only":True,
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "limitations":["historical exact bid/ask not reconstructed","rejection price used as ask proxy"],
        "rows":rows,
        "focus":{
            "XVG-EUR":next((r for r in rows if r["market"]=="XVG-EUR"),None),
            "SAGA-EUR":next((r for r in rows if r["market"]=="SAGA-EUR"),None),
        },
        "errors":errors,
    }
    atomic_json(OUT,out)
    print("SOLAIRE_REJECTION_STRUCTURE_DETAILS "+json.dumps(out["focus"],ensure_ascii=False))

if __name__=="__main__": main()
