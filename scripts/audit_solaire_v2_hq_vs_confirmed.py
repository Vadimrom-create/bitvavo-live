#!/usr/bin/env python3
"""Paired adversarial audit: high-quality BUILDING vs current CONFIRMED.

Consumes the full-universe timing replay and compares the *same market episodes*
when both milestones exist and both forward 4h windows are complete.
Research-only; no production behavior changes.
"""
from __future__ import annotations
import json, statistics, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from research.common import atomic_json, finite, utc

SRC="research/solaire_v2_detection_timing_20260921.json"
OUT="research/solaire_v2_hq_building_vs_confirmed_20260921.json"
MIN_LIQ=75_000.0

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def main():
    data=json.loads(Path(SRC).read_text())
    rows=[]
    for row in data.get("top_session_winners",[]):
        pass
    # The timing audit persists all markets only indirectly via winners/focus, so
    # use the original full-universe source when available in future revisions.
    universe=data.get("markets") or []
    if not universe:
        # Reconstruct from winners/focus without duplicating names. This still
        # provides a strict paired analysis for all persisted rows.
        seen={}
        for x in data.get("top_session_winners",[]) or []: seen[x["market"]]=x
        for k,x in (data.get("focus_markets") or {}).items(): seen[k]=x
        universe=list(seen.values())

    for row in universe:
        if finite(row.get("quote_volume_24h_eur"),0.0) < MIN_LIQ: continue
        sig=row.get("signals") or {}
        hq=sig.get("high_quality_building")
        cf=sig.get("current_confirmed")
        if not hq or not cf: continue
        hf=hq.get("forward_4h") or {}
        cfwd=cf.get("forward_4h") or {}
        if not hf.get("complete") or not cfwd.get("complete"): continue
        hp,cp=finite(hq.get("price_eur")),finite(cf.get("price_eur"))
        ht,ct=finite(hq.get("ts")),finite(cf.get("ts"))
        rows.append({
            "market":row.get("market"),
            "session_return_pct":row.get("session_return_pct"),
            "hq_at_utc":hq.get("at_utc"),"confirmed_at_utc":cf.get("at_utc"),
            "delay_minutes":round((ct-ht)/60,2) if ht is not None and ct is not None else None,
            "price_change_hq_to_confirmed_pct":round((cp/hp-1)*100,4) if hp and cp else None,
            "hq_mfe_4h_pct":finite(hf.get("mfe_pct")),
            "hq_mae_4h_pct":finite(hf.get("mae_pct")),
            "hq_close_4h_pct":finite(hf.get("close_pct")),
            "confirmed_mfe_4h_pct":finite(cfwd.get("mfe_pct")),
            "confirmed_mae_4h_pct":finite(cfwd.get("mae_pct")),
            "confirmed_close_4h_pct":finite(cfwd.get("close_pct")),
        })

    def count(pred): return sum(1 for r in rows if pred(r))
    summary={
        "paired_n":len(rows),
        "median_delay_minutes":med([r["delay_minutes"] for r in rows]),
        "median_price_change_hq_to_confirmed_pct":med([r["price_change_hq_to_confirmed_pct"] for r in rows]),
        "hq":{"mfe_ge_5pct":count(lambda r:r["hq_mfe_4h_pct"]>=5),
              "mae_le_minus5pct":count(lambda r:r["hq_mae_4h_pct"]<=-5),
              "median_mfe_pct":med([r["hq_mfe_4h_pct"] for r in rows]),
              "median_mae_pct":med([r["hq_mae_4h_pct"] for r in rows]),
              "median_close_pct":med([r["hq_close_4h_pct"] for r in rows])},
        "confirmed":{"mfe_ge_5pct":count(lambda r:r["confirmed_mfe_4h_pct"]>=5),
              "mae_le_minus5pct":count(lambda r:r["confirmed_mae_4h_pct"]<=-5),
              "median_mfe_pct":med([r["confirmed_mfe_4h_pct"] for r in rows]),
              "median_mae_pct":med([r["confirmed_mae_4h_pct"] for r in rows]),
              "median_close_pct":med([r["confirmed_close_4h_pct"] for r in rows])},
        "paired_deltas":{"median_mfe_hq_minus_confirmed_pp":med([r["hq_mfe_4h_pct"]-r["confirmed_mfe_4h_pct"] for r in rows]),
              "median_mae_hq_minus_confirmed_pp":med([r["hq_mae_4h_pct"]-r["confirmed_mae_4h_pct"] for r in rows]),
              "median_close_hq_minus_confirmed_pp":med([r["hq_close_4h_pct"]-r["confirmed_close_4h_pct"] for r in rows]),
              "hq_only_mfe_ge_5pct":count(lambda r:r["hq_mfe_4h_pct"]>=5 and r["confirmed_mfe_4h_pct"]<5),
              "confirmed_only_mfe_ge_5pct":count(lambda r:r["confirmed_mfe_4h_pct"]>=5 and r["hq_mfe_4h_pct"]<5)}
    }
    out={"schema":"solaire_v2_hq_building_vs_confirmed_v1","generated_at_utc":utc(),
         "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
         "liquidity_floor_eur_24h":MIN_LIQ,
         "method":"same persisted market episode, both HQ BUILDING and CONFIRMED present, both 4h windows complete",
         "summary":summary,"rows":rows}
    atomic_json(OUT,out)
    print("SOLAIRE_PAIRED_HQ_VS_CONFIRMED "+json.dumps(summary,ensure_ascii=False))

if __name__=="__main__": main()
