#!/usr/bin/env python3
"""Temporal robustness audit for frozen Swing Selector v1.

IMPORTANT: the historical period informed the design discussion, so this is
NOT claimed as clean out-of-sample. It is a robustness check. Clean OOS starts
from the freeze date and is accumulated in swing_history/.
"""
from __future__ import annotations

import bisect
import gzip
import json
import math
import statistics
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient
from research.swing_selector import VERSION, score_market

OUT_JSON="research/swing_selector_v1_robustness_latest.json"
OUT_MD="research/swing_selector_v1_robustness_latest.md"

SAMPLE_SECONDS=3*3600
HORIZONS=(24,48,72,168)
TARGETS=(5,10,20,30)
MIN_QV=15000.0
MAX_SPREAD=1.0
EXCLUDED_BASES={"BTC","ETH","USDT","USDC","EURC","DAI","FDUSD","PYUSD","EURQ","FRAX","USDE","USDG","USDS","GHO","RLUSD","TUSD","USDP","USD1"}
V4_ENTRY={"ENTRY_WINDOW","BUY_READY","REENTRY_READY"}

def med(xs):
    ys=[float(x) for x in xs if x is not None and math.isfinite(float(x))]
    return statistics.median(ys) if ys else None

def fmt(x,d=2):
    x=finite(x)
    return "—" if x is None else f"{x:.{d}f}"

def base(m): return str(m).split("-",1)[0].upper()

def git_paths(prefix):
    out=subprocess.check_output(["git","ls-tree","-r","--name-only","HEAD",prefix],cwd=ROOT,text=True)
    return [x.strip() for x in out.splitlines() if x.strip().endswith(".json.gz")]

def path_ts(path):
    try:
        stamp=Path(path).name.split("-",1)[0]
        return datetime.strptime(stamp,"%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()
    except Exception:
        return None

def sample_paths(paths):
    buckets={}
    for p in sorted(paths):
        ts=path_ts(p)
        if ts is None: continue
        k=int(ts//SAMPLE_SECONDS)
        prev=buckets.get(k)
        if prev is None or ts>prev[0]: buckets[k]=(ts,p)
    return [buckets[k][1] for k in sorted(buckets)]

def git_json_gz(path):
    raw=subprocess.check_output(["git","show","HEAD:"+path],cwd=ROOT)
    return json.loads(gzip.decompress(raw).decode("utf-8"))

def live_from_obs(obs):
    return {
        "quote_volume_24h_eur":finite(obs.get("quote_volume_24h_eur")),
        "spread_pct":finite(obs.get("spread_pct")),
        "change_24h_pct":finite(obs.get("change_24h_pct")),
    }

def build_snapshots():
    paths=sample_paths(git_paths("history"))
    snaps=[]
    for p in paths:
        ts=path_ts(p)
        if ts is None: continue
        doc=git_json_gz(p)
        rows=[]
        baseline_events=[]
        v4_entries=[]
        observations=[x for x in (doc.get("observations") or []) if isinstance(x,dict)]
        btc_trend={}
        for x in observations:
            if x.get("market")=="BTC-EUR":
                btc_trend=((x.get("baseline") or {}).get("trend_profile") or {})
                break
        for obs in observations:
            if not obs.get("market"): continue
            market=str(obs["market"])
            if base(market) in EXCLUDED_BASES: continue
            b=obs.get("baseline") or {}
            trend=dict(b.get("trend_profile") or {})
            for days in (3,7,14):
                key=f"rs_btc_{days}d"
                if trend.get(key) is None and trend.get(f"ret{days}d") is not None and btc_trend.get(f"ret{days}d") is not None:
                    trend[key]=float(trend[f"ret{days}d"])-float(btc_trend[f"ret{days}d"])
            live=live_from_obs(obs)
            price=finite(obs.get("price_eur"))
            qv=finite(live.get("quote_volume_24h_eur"))
            spread=finite(live.get("spread_pct"))
            if price is None or not trend: continue
            if qv is None or qv<MIN_QV: continue
            if spread is not None and spread>MAX_SPREAD: continue
            sc=score_market(market,trend,live,{})
            sc["price_eur"]=price
            sc["ts"]=ts
            rows.append(sc)
            baseline_events.append({"market":market,"ts":ts,"price_eur":price})
            if str(b.get("action_status") or "") in V4_ENTRY:
                v4_entries.append({"market":market,"ts":ts,"price_eur":price})
        rows.sort(key=lambda x:(x["score"],x["technical_score"]),reverse=True)
        snaps.append({
            "ts":ts,"path":p,"ranked":rows,
            "top20":{r["market"] for r in rows[:20]},
            "top10":{r["market"] for r in rows[:10]},
            "baseline":baseline_events,
            "v4_entries":v4_entries,
        })
    return snaps

def dedupe(events,cooldown_h=24):
    last={}
    out=[]
    for e in sorted(events,key=lambda x:x["ts"]):
        prev=last.get(e["market"])
        if prev is None or e["ts"]-prev>=cooldown_h*3600:
            out.append(e); last[e["market"]]=e["ts"]
    return out

def selection_events(snaps):
    raw_top10=[]; human=[]; baseline=[]; v4=[]
    prev=None
    for snap in snaps:
        baseline.extend(snap["baseline"])
        v4.extend(snap["v4_entries"])
        by={r["market"]:r for r in snap["ranked"]}
        for m in snap["top10"]:
            r=by[m]
            raw_top10.append({"market":m,"ts":snap["ts"],"price_eur":r["price_eur"],"score":r["score"]})
            persisted=bool(prev and snap["ts"]-prev["ts"]<=4*3600 and m in prev["top20"])
            blocking=set(r.get("flags") or []) & {"WIDE_SPREAD","HIGH_ATR","CHASE_RISK_24H","FAR_ABOVE_EMA50"}
            if persisted and not blocking:
                human.append({"market":m,"ts":snap["ts"],"price_eur":r["price_eur"],"score":r["score"]})
        prev=snap
    return {
        "baseline":dedupe(baseline,24),
        "v4_entry":dedupe(v4,24),
        "swing_top10_raw":dedupe(raw_top10,24),
        "swing_human_review":dedupe(human,24),
    }

def hourly_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        out.append((t/1000.0,o,h,l,c,v))
    return sorted(out)

def price_series(markets):
    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    out={}; errors=[]
    def one(m):
        return m,hourly_rows(client.get("/"+m+"/candles",{"interval":"1h","limit":1000},cache=False))
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
    if entry is None or entry<=0 or now<ts0+hours*3600 or not rows: return None
    ts=[r[0] for r in rows]
    i=bisect.bisect_left(ts,ts0)
    j=bisect.bisect_left(ts,ts0+hours*3600)
    xs=rows[i:j]
    if not xs: return None
    hi=max(r[2] for r in xs); lo=min(r[3] for r in xs); close=xs[-1][4]
    return {"mfe_pct":(hi/entry-1)*100,"mae_pct":(lo/entry-1)*100,"close_pct":(close/entry-1)*100}

def evaluate(events,series,now):
    out={}
    for h in HORIZONS:
        rows=[]
        for e in events:
            r=forward(series.get(e["market"]) or [],e["ts"],e["price_eur"],h,now)
            if r: rows.append(r)
        out[str(h)]={
            "n":len(rows),
            "positive_close_pct":100*sum(r["close_pct"]>0 for r in rows)/len(rows) if rows else None,
            "median_close_pct":med([r["close_pct"] for r in rows]),
            "median_mfe_pct":med([r["mfe_pct"] for r in rows]),
            "median_mae_pct":med([r["mae_pct"] for r in rows]),
            **{f"hit_{t}_pct":100*sum(r["mfe_pct"]>=t for r in rows)/len(rows) if rows else None for t in TARGETS},
        }
    return out

def split_events(events,cut):
    return [e for e in events if e["ts"]<cut],[e for e in events if e["ts"]>=cut]

def main():
    now=time.time()
    snaps=build_snapshots()
    events=selection_events(snaps)
    markets=sorted({e["market"] for xs in events.values() for e in xs})
    series,errors,httpdiag=price_series(markets)

    all_eval={k:evaluate(v,series,now) for k,v in events.items()}
    first_ts=min(s["ts"] for s in snaps); last_ts=max(s["ts"] for s in snaps)
    cut=first_ts+(last_ts-first_ts)*0.60
    temporal={}
    for k,v in events.items():
        a,b=split_events(v,cut)
        temporal[k]={
            "early_60pct":evaluate(a,series,now),
            "late_40pct":evaluate(b,series,now),
        }

    payload={
        "schema":"swing_selector_v1_temporal_robustness",
        "version":VERSION,
        "generated_at_utc":utc(),
        "measurement_only":True,
        "clean_out_of_sample":False,
        "clean_oos_reason":"The historical period informed v1 design. True OOS starts after the frozen v1 timestamp.",
        "true_oos_source":"swing_history/",
        "sampling_seconds":SAMPLE_SECONDS,
        "snapshot_count":len(snaps),
        "first_snapshot_at_utc":datetime.fromtimestamp(first_ts,timezone.utc).isoformat(),
        "last_snapshot_at_utc":datetime.fromtimestamp(last_ts,timezone.utc).isoformat(),
        "temporal_split_at_utc":datetime.fromtimestamp(cut,timezone.utc).isoformat(),
        "event_counts":{k:len(v) for k,v in events.items()},
        "metrics":all_eval,
        "temporal_robustness":temporal,
        "price_series_errors":errors,
        "http_diagnostics":httpdiag,
        "definitions":{
            "human_review":"top10 now + top20 in preceding ~3h snapshot + no major extension/risk flag",
            "event_cooldown_hours":24,
            "baseline":"all liquid eligible markets at same 3h snapshots, deduped per market/24h",
            "success":"maximum favorable excursion reaches target inside horizon",
        },
    }
    atomic_json(OUT_JSON,payload)

    lines=[
        "# Swing Selector v1 — temporal robustness",
        "",
        f"Version: {VERSION}",
        f"Generated: {payload['generated_at_utc']}",
        "**Not clean out-of-sample. True OOS starts now in swing_history/.**",
        "",
        "| Selector | Horizon | N | Close >0 | Hit +10 | Hit +20 | Hit +30 | Med MFE | Med MAE |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    labels={"baseline":"Baseline all markets","v4_entry":"V4 ENTRY","swing_top10_raw":"Swing top10 raw","swing_human_review":"Swing HUMAN_REVIEW"}
    for key in ("baseline","v4_entry","swing_top10_raw","swing_human_review"):
        for h in HORIZONS:
            r=all_eval[key][str(h)]
            lines.append(
                f"| {labels[key]} | {h}h | {r['n']} | {fmt(r['positive_close_pct'])}% | "
                f"{fmt(r['hit_10_pct'])}% | {fmt(r['hit_20_pct'])}% | {fmt(r['hit_30_pct'])}% | "
                f"{fmt(r['median_mfe_pct'])}% | {fmt(r['median_mae_pct'])}% |"
            )
    lines+=["","## Temporal split (robustness only)","",
            f"Cut: {payload['temporal_split_at_utc']}","",
            "| Selector | Segment | 7d N | 7d close >0 | Hit +20 | Hit +30 |",
            "|---|---|---:|---:|---:|---:|"]
    for key in ("baseline","v4_entry","swing_top10_raw","swing_human_review"):
        for seg in ("early_60pct","late_40pct"):
            r=temporal[key][seg]["168"]
            lines.append(
                f"| {labels[key]} | {seg} | {r['n']} | {fmt(r['positive_close_pct'])}% | "
                f"{fmt(r['hit_20_pct'])}% | {fmt(r['hit_30_pct'])}% |"
            )
    lines+=["","## Notes","",
            "- No production behavior changed.",
            "- News modifier is excluded historically because news snapshots were not archived.",
            "- 5m/15m acceleration is not an input to the swing thesis.",
            "- The forward live shadow history is the only clean OOS evidence for v1.",
            ""]
    Path(OUT_MD).write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"event_counts":payload["event_counts"],"metrics":payload["metrics"],"temporal_robustness":payload["temporal_robustness"]},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
