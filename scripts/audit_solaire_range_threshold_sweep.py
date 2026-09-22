#!/usr/bin/env python3
"""Sweep structural-range thresholds for actual CONFIRMED range rejections.

Uses persisted rejection events, rebuilds 15m structure at each rejection, and
asks whether thresholds from 4.0% to 6.0% would have advanced to a valid
structural plan with stop <=10%. Forward outcomes come from the prospective
rejection journal.

Research-only. No production behavior changes.
"""
from __future__ import annotations
import json, statistics, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.risk import structural_plan

JOURNAL="production_rejection_shadow_journal.json"
OUT="research/solaire_range_threshold_sweep_20260921.json"
THRESHOLDS=(4.0,4.5,5.0,5.25,5.5,5.75,6.0)
MAX_STOP=10.0

def med(xs):
    xs=[x for x in xs if x is not None]
    if not xs:return None
    xs=sorted(xs); n=len(xs)
    return round(xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2,4)

def summarize(rows,h):
    xs=[r for r in rows if r.get("evaluations",{}).get(str(h))]
    ev=[r["evaluations"][str(h)] for r in xs]
    return {
        "n":len(ev),
        "mfe_ge_5pct":sum(finite(x.get("mfe_pct"),-999)>=5 for x in ev),
        "clean_mfe_ge5_mae_gt_minus5":sum(
            finite(x.get("mfe_pct"),-999)>=5 and finite(x.get("mae_pct"),999)>-5 for x in ev
        ),
        "mae_le_minus5pct":sum(finite(x.get("mae_pct"),999)<=-5 for x in ev),
        "median_mfe_pct":med([finite(x.get("mfe_pct")) for x in ev]),
        "median_mae_pct":med([finite(x.get("mae_pct")) for x in ev]),
        "median_close_pct":med([finite(x.get("close_return_pct")) for x in ev]),
    }

def main():
    journal=json.loads(Path(JOURNAL).read_text())
    events=[e for e in journal.get("events",[])
            if e.get("first_rejection_reason")=="STRUCTURAL_RANGE_TOO_NARROW"
            and e.get("signal_state")=="CONFIRMED_ACCELERATION"]

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    metas={m["market"]:m for m in client.get("/markets")
           if m.get("quote")=="EUR" and m.get("status")=="trading"}

    rows=[];errors=[]
    for e in events:
        market=e.get("market"); t=finite(e.get("rejected_ts")); px=finite(e.get("rejection_price_eur"))
        if not market or t is None or px is None or px<=0 or market not in metas:continue
        try:
            raw=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            f=describe(closed_candles(raw,"15m",t),"15m")
            rng=finite(f.get("consolidation_range_pct"))
            plan=None
            if f.get("valid"):
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
            structurally_valid=bool((plan or {}).get("valid") and stop is not None and stop<=MAX_STOP)
            passes={str(th):bool(rng is not None and rng>=th and structurally_valid) for th in THRESHOLDS}
            rows.append({
                "event_id":e.get("event_id"),"market":market,
                "rejected_at_utc":e.get("rejected_at_utc"),
                "rejection_price_eur":px,"signal_score":finite(e.get("signal_score")),
                "range_15m_pct":rng,"plan":plan,"passes":passes,
                "evaluations":e.get("evaluations") or {},
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    summary={}
    for th in THRESHOLDS:
        chosen=[r for r in rows if r["passes"][str(th)]]
        summary[str(th)]={
            "selected_events":len(chosen),
            "h1":summarize(chosen,1),
            "h4":summarize(chosen,4),
            "markets":[r["market"] for r in chosen],
        }

    out={
        "schema":"solaire_range_threshold_sweep_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "thresholds_pct":list(THRESHOLDS),"max_stop_pct":MAX_STOP,
        "confirmed_range_rejections":len(rows),
        "summary":summary,"rows":rows,"errors":errors,
        "limitations":[
            "single-session evidence",
            "rejection price is used as historical ask proxy for structural-plan calculation",
            "only actual production STRUCTURAL_RANGE_TOO_NARROW rejections are included",
        ],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_RANGE_THRESHOLD_SWEEP "+json.dumps(summary,ensure_ascii=False))

if __name__=="__main__":main()
