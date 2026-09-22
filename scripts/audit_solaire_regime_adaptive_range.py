#!/usr/bin/env python3
"""Audit regime-adaptive structural-range policies for Solaire V2.

Joins the range-threshold sweep with the prospective decision journal context,
then compares counterfactual policies that relax the 6% range only in broad
risk-on conditions.

Research-only. No production behavior changes.
"""
from __future__ import annotations
import json, statistics
from datetime import datetime
from pathlib import Path

SWEEP="research/solaire_range_threshold_sweep_20260921.json"
JOURNAL="production_decision_journal.json"
OUT="research/solaire_regime_adaptive_range_20260921.json"

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def finite(v):
    try:return float(v)
    except (TypeError,ValueError):return None

def med(xs):
    xs=[x for x in xs if x is not None]
    if not xs:return None
    xs=sorted(xs); n=len(xs)
    return round(xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2,4)

def nearest_context(entries,market,t0):
    candidates=[]
    for e in entries:
        if e.get("market")!=market or e.get("reason")!="STRUCTURAL_RANGE_TOO_NARROW":continue
        try:dt=abs(ts(e.get("cycle_id"))-t0)
        except Exception:continue
        if dt<=900:candidates.append((dt,e))
    if not candidates:return {}
    return min(candidates,key=lambda x:x[0])[1].get("context") or {}

def stats(rows,h="4"):
    xs=[r for r in rows if (r.get("evaluations") or {}).get(h)]
    ev=[r["evaluations"][h] for r in xs]
    return {
        "n":len(ev),
        "mfe_ge_5pct":sum(finite(x.get("mfe_pct")) is not None and finite(x.get("mfe_pct"))>=5 for x in ev),
        "clean_mfe_ge5_mae_gt_minus5":sum(
            finite(x.get("mfe_pct")) is not None and finite(x.get("mfe_pct"))>=5
            and finite(x.get("mae_pct")) is not None and finite(x.get("mae_pct"))>-5 for x in ev
        ),
        "mae_le_minus5pct":sum(finite(x.get("mae_pct")) is not None and finite(x.get("mae_pct"))<=-5 for x in ev),
        "median_mfe_pct":med([finite(x.get("mfe_pct")) for x in ev]),
        "median_mae_pct":med([finite(x.get("mae_pct")) for x in ev]),
        "median_close_pct":med([finite(x.get("close_return_pct")) for x in ev]),
    }

def main():
    sweep=json.loads(Path(SWEEP).read_text())
    journal=json.loads(Path(JOURNAL).read_text())
    entries=journal.get("entries") or []

    rows=[]
    for r in sweep.get("rows") or []:
        t0=ts(r.get("rejected_at_utc"))
        ctx=nearest_context(entries,r.get("market"),t0)
        rows.append({
            **r,
            "regime":ctx.get("regime"),
            "regime_phase":ctx.get("regime_phase") or ctx.get("short_term_phase"),
            "breadth_1h_pct":finite(ctx.get("breadth_positive_1h_pct")),
            "breadth_4h_pct":finite(ctx.get("breadth_positive_4h_pct")),
        })

    policies={
        "range5_all":lambda r:r["passes"].get("5.0",False),
        "range5_broad_risk_on":lambda r:r["passes"].get("5.0",False) and r.get("regime")=="BROAD_RISK_ON",
        "range5_broad_risk_on_breadth4_ge70":lambda r:r["passes"].get("5.0",False) and r.get("regime")=="BROAD_RISK_ON" and finite(r.get("breadth_4h_pct")) is not None and r["breadth_4h_pct"]>=70,
        "range5_5_broad_risk_on":lambda r:r["passes"].get("5.5",False) and r.get("regime")=="BROAD_RISK_ON",
        "range5_mixed":lambda r:r["passes"].get("5.0",False) and r.get("regime")=="MIXED",
    }
    summary={}
    for name,pred in policies.items():
        chosen=[r for r in rows if pred(r)]
        summary[name]={
            "selected_events":len(chosen),
            "h1":stats(chosen,"1"),
            "h4":stats(chosen,"4"),
            "markets":[r["market"] for r in chosen],
        }

    out={
        "schema":"solaire_regime_adaptive_range_audit_v1",
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "summary":summary,"rows":rows,
        "limitations":[
            "single-session evidence",
            "context joined to nearest same-market range rejection within 15 minutes",
            "inherits range-sweep ask-proxy limitation",
            "policy comparisons are exploratory and not production recommendations",
        ],
    }
    Path(OUT).write_text(json.dumps(out,ensure_ascii=False,separators=(",",":"))+"\n")
    print("SOLAIRE_REGIME_ADAPTIVE_RANGE "+json.dumps(summary,ensure_ascii=False))

if __name__=="__main__":main()
