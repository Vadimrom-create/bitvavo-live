#!/usr/bin/env python3
"""Backfill 5% counterfactuals for confirmed Solaire range rejections.

For production episodes whose final rejection reason was
STRUCTURAL_RANGE_TOO_NARROW, rebuild the historical 15m structure at the
rejection timestamp and test whether a 5% range threshold would have advanced
to a valid structural plan with stop distance <=10%.

Because the *actual* production reason was RANGE_TOO_NARROW, the upstream
liquidity/spread/freshness gates had already passed at that rejection check.
Historical exact bid/ask is still not reconstructed, so rejection_price_eur is
used as the execution-price proxy for structural-plan calculation.

Research-only; no production behavior changes.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

JOURNAL="production_rejection_shadow_journal.json"
OUT="research/solaire_v21_confirmed_range5_backfill_20260921.json"
CANDIDATE_RANGE=5.0
CURRENT_RANGE=6.0
MAX_STOP=10.0

def main():
    journal=json.loads(Path(JOURNAL).read_text())
    events=[e for e in journal.get("events",[])
            if e.get("first_rejection_reason")=="STRUCTURAL_RANGE_TOO_NARROW"
            and e.get("signal_state")=="CONFIRMED_ACCELERATION"]

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets")
           if m.get("quote")=="EUR" and m.get("status")=="trading"}

    rows=[]; errors=[]
    for e in events:
        market=e.get("market")
        ts=finite(e.get("rejected_ts"))
        px=finite(e.get("rejection_price_eur"))
        if not market or ts is None or px is None or px<=0 or market not in metas:
            continue
        try:
            raw=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            f=describe(closed_candles(raw,"15m",ts),"15m")
            rng=finite(f.get("consolidation_range_pct"))
            candidate_range_pass=bool(rng is not None and rng>=CANDIDATE_RANGE)
            current_range_pass=bool(rng is not None and rng>=CURRENT_RANGE)
            plan=None
            if candidate_range_pass:
                p=structural_plan({"market":market,"ask":px},f,metas[market])
                plan={
                    "valid":bool(p.get("valid")),
                    "reason":None if p.get("valid") else p.get("reason"),
                    "stop_distance_pct":finite(p.get("stop_distance_pct")),
                    "net_rr_tp1":finite(p.get("net_rr_tp1")),
                    "entry_eur":finite(p.get("entry_eur")),
                    "stop_eur":finite(p.get("stop_eur")),
                    "tp1_eur":finite(p.get("tp1_eur")),
                }
            stop=finite((plan or {}).get("stop_distance_pct"))
            pass5=bool(candidate_range_pass and (plan or {}).get("valid")
                       and stop is not None and stop<=MAX_STOP)
            rows.append({
                "event_id":e.get("event_id"),
                "market":market,
                "rejected_at_utc":e.get("rejected_at_utc"),
                "rejection_price_eur":px,
                "signal_score":finite(e.get("signal_score")),
                "range_15m_pct":rng,
                "current6_range_pass":current_range_pass,
                "candidate5_range_pass":candidate_range_pass,
                "counterfactual5_structure_pass_proxy":pass5,
                "plan5":plan,
                "upstream_execution_gates_passed_at_rejection":True,
                "historical_exact_bid_ask_reconstructed":False,
                "evaluations":e.get("evaluations") or {},
                "original_condition_resolved":bool(e.get("original_condition_resolved")),
                "first_later_qualifying_entry":e.get("first_later_qualifying_entry"),
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    pass5=[r for r in rows if r["counterfactual5_structure_pass_proxy"]]
    out={
        "schema":"solaire_v21_confirmed_range5_backfill_v1",
        "generated_at_utc":utc(),
        "research_only":True,
        "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "criteria":{"current_range_pct":CURRENT_RANGE,"candidate_range_pct":CANDIDATE_RANGE,"max_stop_pct":MAX_STOP},
        "method":"historical 15m structure at actual confirmed range rejection; actual rejection reason proves upstream execution gates passed; rejection price used as structural-plan execution proxy",
        "limitations":["historical exact bid/ask not reconstructed","rejection_price_eur used as ask proxy","single-session evidence"],
        "summary":{
            "confirmed_range_rejections":len(rows),
            "range_5_to_6_pct":sum(r["candidate5_range_pass"] and not r["current6_range_pass"] for r in rows),
            "counterfactual5_structure_pass_proxy":len(pass5),
            "counterfactual5_pass_with_1h_mfe_ge5":sum(
                finite((r.get("evaluations") or {}).get("1",{}).get("mfe_pct"),-999)>=5 for r in pass5
            ),
            "counterfactual5_pass_with_1h_mae_le_minus5":sum(
                finite((r.get("evaluations") or {}).get("1",{}).get("mae_pct"),999)<=-5 for r in pass5
            ),
        },
        "rows":rows,
        "errors":errors,
    }
    atomic_json(OUT,out)
    print("SOLAIRE_CONFIRMED_RANGE5_BACKFILL "+json.dumps(out["summary"],ensure_ascii=False))

if __name__=="__main__": main()
