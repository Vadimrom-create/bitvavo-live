#!/usr/bin/env python3
"""Clean forward OOS evaluator for frozen Swing Selector R2 snapshots.

Reads only snapshots created after the selector was frozen. It never changes
selector rules, production trading, orders, alerts, stops, or Decision Layer.
"""
from __future__ import annotations

import bisect
import gzip
import json
import math
import statistics
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient
from research.swing_selector import VERSION

OUT_JSON="research/swing_selector_oos_latest.json"
OUT_MD="research/swing_selector_oos_latest.md"
HORIZONS=(24,48,72,168)
TARGETS=(5,10,20,30)
COOLDOWN_H=24
MIN_7D_HUMAN_EVENTS_FOR_PROVISIONAL=50

def med(xs):
    ys=[float(x) for x in xs if x is not None and math.isfinite(float(x))]
    return statistics.median(ys) if ys else None

def fmt(x,d=2):
    x=finite(x)
    return "—" if x is None else f"{x:.{d}f}"

def load_snapshots():
    out=[]
    for p in sorted((ROOT/"swing_history").glob("*/*.json.gz")):
        try:
            doc=json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))
        except Exception:
            continue
        if doc.get("version") != VERSION:
            continue
        if not doc.get("ranked_summary"):
            continue
        ts=finite(doc.get("generated_ts"))
        if ts is None:
            continue
        doc["_path"]=str(p.relative_to(ROOT))
        out.append(doc)
    return out

def dedupe(events):
    last={}
    out=[]
    for e in sorted(events,key=lambda x:x["ts"]):
        prev=last.get(e["market"])
        if prev is None or e["ts"]-prev>=COOLDOWN_H*3600:
            out.append(e)
            last[e["market"]]=e["ts"]
    return out

def event_sets(snaps):
    baseline=[]; top10=[]; human=[]
    for s in snaps:
        ts=float(s["generated_ts"])
        for r in s.get("ranked_summary") or []:
            p=finite(r.get("last_eur"))
            if p is not None:
                baseline.append({"market":r["market"],"ts":ts,"price_eur":p})
        for r in s.get("top10") or []:
            p=finite(r.get("last_eur"))
            if p is not None:
                top10.append({"market":r["market"],"ts":ts,"price_eur":p})
        for r in s.get("human_review") or []:
            p=finite(r.get("last_eur"))
            if p is not None:
                human.append({"market":r["market"],"ts":ts,"price_eur":p})
    return {
        "baseline":dedupe(baseline),
        "swing_top10":dedupe(top10),
        "swing_human_review":dedupe(human),
    }

def hourly_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6:
            continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals):
            continue
        t,o,h,l,c,v=vals
        out.append((t/1000.0,o,h,l,c,v))
    return sorted(out)

def price_series(markets):
    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    out={}; errors=[]
    def one(m):
        raw=client.get("/"+m+"/candles",{"interval":"1h","limit":1000},cache=False)
        return m,hourly_rows(raw)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs={pool.submit(one,m):m for m in markets}
        for fut in as_completed(futs):
            m=futs[fut]
            try:
                k,v=fut.result(); out[k]=v
            except Exception as exc:
                errors.append({"market":m,"error":type(exc).__name__+":"+str(exc)})
    return out,errors,client.diagnostics()

def forward(rows,ts0,entry,hours,now):
    if entry is None or entry<=0 or now<ts0+hours*3600 or not rows:
        return None
    ts=[r[0] for r in rows]
    i=bisect.bisect_left(ts,ts0)
    j=bisect.bisect_left(ts,ts0+hours*3600)
    xs=rows[i:j]
    if not xs:
        return None
    hi=max(r[2] for r in xs)
    lo=min(r[3] for r in xs)
    close=xs[-1][4]
    return {
        "mfe_pct":(hi/entry-1)*100,
        "mae_pct":(lo/entry-1)*100,
        "close_pct":(close/entry-1)*100,
    }

def evaluate(events,series,now):
    out={}
    for h in HORIZONS:
        rows=[]
        for e in events:
            r=forward(series.get(e["market"]) or [],e["ts"],e["price_eur"],h,now)
            if r is not None:
                rows.append(r)
        out[str(h)]={
            "n":len(rows),
            "positive_close_pct":100*sum(r["close_pct"]>0 for r in rows)/len(rows) if rows else None,
            "median_close_pct":med([r["close_pct"] for r in rows]),
            "median_mfe_pct":med([r["mfe_pct"] for r in rows]),
            "median_mae_pct":med([r["mae_pct"] for r in rows]),
            **{f"hit_{t}_pct":100*sum(r["mfe_pct"]>=t for r in rows)/len(rows) if rows else None for t in TARGETS},
        }
    return out

def delta(a,b,key):
    x=finite(a.get(key)); y=finite(b.get(key))
    return (x-y) if x is not None and y is not None else None

def main():
    now=time.time()
    snaps=load_snapshots()
    events=event_sets(snaps)
    markets=sorted({e["market"] for xs in events.values() for e in xs})
    series,errors,httpdiag=price_series(markets) if markets else ({},[],{})

    metrics={k:evaluate(v,series,now) for k,v in events.items()}
    base7=metrics["baseline"]["168"]
    human7=metrics["swing_human_review"]["168"]
    top7=metrics["swing_top10"]["168"]

    if human7["n"] < MIN_7D_HUMAN_EVENTS_FOR_PROVISIONAL:
        verdict="INSUFFICIENT_MATURE_7D_DATA"
    else:
        excess20=delta(human7,base7,"hit_20_pct")
        excess30=delta(human7,base7,"hit_30_pct")
        excesspos=delta(human7,base7,"positive_close_pct")
        if all(x is not None and x>0 for x in (excess20,excess30,excesspos)):
            verdict="PROVISIONAL_EDGE_POSITIVE"
        elif excess20 is not None and excess20<0 and excess30 is not None and excess30<0:
            verdict="PROVISIONAL_EDGE_NEGATIVE"
        else:
            verdict="PROVISIONAL_MIXED"

    payload={
        "schema":"swing_selector_clean_oos_v1",
        "version":VERSION,
        "generated_at_utc":utc(),
        "measurement_only":True,
        "clean_out_of_sample":True,
        "snapshot_count":len(snaps),
        "first_snapshot_at_utc":snaps[0].get("generated_at_utc") if snaps else None,
        "last_snapshot_at_utc":snaps[-1].get("generated_at_utc") if snaps else None,
        "event_counts":{k:len(v) for k,v in events.items()},
        "metrics":metrics,
        "seven_day_excess_vs_baseline":{
            "top10_hit20_pp":delta(top7,base7,"hit_20_pct"),
            "top10_hit30_pp":delta(top7,base7,"hit_30_pct"),
            "top10_positive_close_pp":delta(top7,base7,"positive_close_pct"),
            "human_hit20_pp":delta(human7,base7,"hit_20_pct"),
            "human_hit30_pp":delta(human7,base7,"hit_30_pct"),
            "human_positive_close_pp":delta(human7,base7,"positive_close_pct"),
        },
        "provisional_verdict":verdict,
        "min_7d_human_events_for_provisional":MIN_7D_HUMAN_EVENTS_FOR_PROVISIONAL,
        "price_series_errors":errors,
        "http_diagnostics":httpdiag,
        "notes":[
            "No selector parameters are changed by this evaluator.",
            "MFE target hits measure opportunity presence, not realized PnL.",
            "Events are deduplicated per market over 24h.",
            "A provisional 7d verdict is withheld until at least 50 matured HUMAN_REVIEW events.",
        ],
    }
    atomic_json(OUT_JSON,payload)

    lines=[
        "# Swing Selector R2 — clean forward OOS",
        "",
        f"Version: {VERSION}",
        f"Generated: {payload['generated_at_utc']}",
        f"Snapshots: {len(snaps)}",
        f"Verdict: **{verdict}**",
        "",
        "| Cohort | Horizon | N | Close >0 | Hit +10 | Hit +20 | Hit +30 | Med close | Med MFE | Med MAE |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    labels={"baseline":"Baseline","swing_top10":"Swing top10","swing_human_review":"HUMAN_REVIEW"}
    for key in ("baseline","swing_top10","swing_human_review"):
        for h in HORIZONS:
            r=metrics[key][str(h)]
            lines.append(
                f"| {labels[key]} | {h}h | {r['n']} | {fmt(r['positive_close_pct'])}% | "
                f"{fmt(r['hit_10_pct'])}% | {fmt(r['hit_20_pct'])}% | {fmt(r['hit_30_pct'])}% | "
                f"{fmt(r['median_close_pct'])}% | {fmt(r['median_mfe_pct'])}% | {fmt(r['median_mae_pct'])}% |"
            )
    ex=payload["seven_day_excess_vs_baseline"]
    lines+=["","## 7d excess vs baseline","",
            f"- Top10: +20 target {fmt(ex['top10_hit20_pp'])} pp; +30 target {fmt(ex['top10_hit30_pp'])} pp; positive close {fmt(ex['top10_positive_close_pp'])} pp.",
            f"- HUMAN_REVIEW: +20 target {fmt(ex['human_hit20_pp'])} pp; +30 target {fmt(ex['human_hit30_pp'])} pp; positive close {fmt(ex['human_positive_close_pp'])} pp.",
            "",
            "The R2 rules remain frozen regardless of these interim results.",
            ""]
    Path(OUT_MD).write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"snapshot_count":len(snaps),"event_counts":payload["event_counts"],"verdict":verdict},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
