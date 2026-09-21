#!/usr/bin/env python3
"""Adversarial audit of extension/chase risk in Solaire decisions.

Rebuilds 15m ATR at each recorded production decision with a complete 4h outcome
and measures how pre-entry extension (1h/4h return divided by ATR) relates to
future MFE/MAE/close. This is research-only; it does not add a chase veto.
"""
from __future__ import annotations
import json, statistics, sys
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient

JOURNAL="production_decision_journal.json"
OUT="research/solaire_extension_risk_20260921.json"

RATIO_BINS=(
    ("lt1",None,1.0),
    ("1to2",1.0,2.0),
    ("2to3",2.0,3.0),
    ("3to5",3.0,5.0),
    ("ge5",5.0,None),
)
RETURN_BINS=(
    ("lt1",None,1.0),
    ("1to3",1.0,3.0),
    ("3to6",3.0,6.0),
    ("6to10",6.0,10.0),
    ("ge10",10.0,None),
)

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def in_bin(v,lo,hi):
    if v is None:return False
    if lo is not None and v<lo:return False
    if hi is not None and v>=hi:return False
    return True

def stats(rows):
    return {
        "n":len(rows),
        "mfe_ge_5pct":sum(r["mfe_4h_pct"]>=5 for r in rows),
        "clean_mfe_ge5_mae_gt_minus5":sum(r["mfe_4h_pct"]>=5 and r["mae_4h_pct"]>-5 for r in rows),
        "mae_le_minus5pct":sum(r["mae_4h_pct"]<=-5 for r in rows),
        "median_mfe_pct":med([r["mfe_4h_pct"] for r in rows]),
        "median_mae_pct":med([r["mae_4h_pct"] for r in rows]),
        "median_close_pct":med([r["close_4h_pct"] for r in rows]),
        "median_signal_score":med([r["signal_score"] for r in rows]),
        "median_return_1h_pct":med([r["return_1h_pct"] for r in rows]),
        "median_return_4h_pct":med([r["return_4h_pct"] for r in rows]),
        "median_atr15_pct":med([r["atr15_pct"] for r in rows]),
        "median_extension_1h_atr":med([r["extension_1h_atr"] for r in rows]),
        "median_extension_4h_atr":med([r["extension_4h_atr"] for r in rows]),
    }

def main():
    journal=json.loads(Path(JOURNAL).read_text())
    entries=[]
    for e in journal.get("entries",[]) or []:
        f=e.get("evaluations",{}).get("4")
        if not f:continue
        t=finite(e.get("decision_ts"))
        market=e.get("market")
        px=finite(e.get("signal_price_eur"),finite(e.get("entry_eur")))
        if t is None or not market or px is None:continue
        entries.append((e,f,t,market,px))

    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    client.get("/time",cache=False)
    raws={}; errors=[]; rows=[]
    for e,f,t,market,px in entries:
        try:
            if market not in raws:
                raws[market]=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            feat=describe(closed_candles(raws[market],"15m",t),"15m")
            atr=finite(feat.get("atr14_pct"))
            ctx=e.get("context") or {}
            r1=finite(ctx.get("market_return_1h_pct"))
            r4=finite(ctx.get("market_return_4h_pct"))
            x1=(max(r1,0)/atr) if r1 is not None and atr not in (None,0) else None
            x4=(max(r4,0)/atr) if r4 is not None and atr not in (None,0) else None
            rows.append({
                "market":market,"at_utc":e.get("cycle_id"),
                "decision_type":e.get("decision_type"),"reason":e.get("reason"),
                "signal_price_eur":px,"signal_score":finite(e.get("signal_score")),
                "return_1h_pct":r1,"return_4h_pct":r4,
                "relative_strength_1h_pp":finite(ctx.get("relative_strength_1h_pp")),
                "relative_strength_4h_pp":finite(ctx.get("relative_strength_4h_pp")),
                "breadth_1h_pct":finite(ctx.get("breadth_positive_1h_pct")),
                "breadth_4h_pct":finite(ctx.get("breadth_positive_4h_pct")),
                "atr15_pct":atr,
                "extension_1h_atr":round(x1,4) if x1 is not None else None,
                "extension_4h_atr":round(x4,4) if x4 is not None else None,
                "mfe_4h_pct":finite(f.get("mfe_pct"),0),
                "mae_4h_pct":finite(f.get("mae_pct"),0),
                "close_4h_pct":finite(f.get("close_return_pct"),0),
            })
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    cohorts={}
    for name,pred in {
        "all":lambda r:True,
        "buy_sent":lambda r:r["decision_type"]=="BUY_SENT",
        "low_24h_liquidity_reject":lambda r:r["reason"]=="INSUFFICIENT_EXECUTION_LIQUIDITY",
        "spread_reject":lambda r:r["reason"]=="SPREAD_TOO_WIDE",
        "range_reject":lambda r:r["reason"]=="STRUCTURAL_RANGE_TOO_NARROW",
        "stop_reject":lambda r:r["reason"]=="STRUCTURAL_STOP_TOO_WIDE",
    }.items():
        xs=[r for r in rows if pred(r)]
        ratio1={label:stats([r for r in xs if in_bin(r["extension_1h_atr"],lo,hi)])
                for label,lo,hi in RATIO_BINS}
        ratio4={label:stats([r for r in xs if in_bin(r["extension_4h_atr"],lo,hi)])
                for label,lo,hi in RATIO_BINS}
        ret1={label:stats([r for r in xs if in_bin(max(r["return_1h_pct"],0) if r["return_1h_pct"] is not None else None,lo,hi)])
              for label,lo,hi in RETURN_BINS}
        cohorts[name]={
            "overall":stats(xs),
            "extension_1h_atr_bins":ratio1,
            "extension_4h_atr_bins":ratio4,
            "positive_return_1h_bins":ret1,
        }

    low=[r for r in rows if r["reason"]=="INSUFFICIENT_EXECUTION_LIQUIDITY"]
    low_sorted=sorted(low,key=lambda r:r["mfe_4h_pct"],reverse=True)
    out={
        "schema":"solaire_extension_risk_audit_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "method":"current 15m ATR rebuilt at each actual decision; positive 1h/4h return divided by ATR; actual 4h journal outcomes",
        "limitations":["single session","correlation is not causation","historical spread/depth not reconstructed in this audit"],
        "row_count":len(rows),"cohorts":cohorts,
        "low_liquidity_top_mfe":low_sorted[:25],
        "errors":errors,
    }
    atomic_json(OUT,out)
    print("SOLAIRE_EXTENSION_RISK "+json.dumps({
        "rows":len(rows),
        "low_liquidity":cohorts["low_24h_liquidity_reject"],
    },ensure_ascii=False))

if __name__=="__main__":main()
