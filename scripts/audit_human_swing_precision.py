#!/usr/bin/env python3
"""Precision audit for Solaire Human/Swing.

Measurement only. Compares Solaire's hourly-persistent states with a neutral
all-market daily baseline and evaluates forward 24h/48h/72h/7d outcomes.

No production scoring, thresholds, alerts, orders, stops or positions change.
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
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.http import PublicClient

OUT_JSON="research/human_swing_precision_latest.json"
OUT_MD="research/human_swing_precision_latest.md"

SAMPLE_SECONDS=3600
HORIZONS=(24,48,72,168)
TARGETS=(5,10,20,30)
V4_WATCH={"WATCH","ENTRY_WINDOW","BUY_READY","REENTRY_READY"}
V4_ENTRY={"ENTRY_WINDOW","BUY_READY","REENTRY_READY"}
ACCEL={"BUILDING_ACCELERATION","CONFIRMED_ACCELERATION"}

SIGNALS=(
    "v4_watch",
    "v4_entry",
    "v4_buy_ready",
    "acceleration",
    "confirmed_acceleration",
    "pipeline_buy",
    "dl_actionable",
    "dl_buy_now",
)

FEATURES=(
    "opportunity_score","trend_score","entry_score","ignition_score",
    "change_24h_pct","quote_volume_24h_eur","confirm_count","since_first_signal_pct",
    "ret3d","ret7d","ret14d","ret30d","dist_ema20_pct","dist_ema50_pct",
    "ema20_slope_5d_pct","breakout20_pct","drawdown_30d_high_pct",
    "vol3_vs_prev20","green_days_7","rs_btc_3d","rs_btc_7d","rs_btc_14d","rs_btc_30d",
)

def med(xs):
    ys=[float(x) for x in xs if x is not None and math.isfinite(float(x))]
    return statistics.median(ys) if ys else None

def mean(xs):
    ys=[float(x) for x in xs if x is not None and math.isfinite(float(x))]
    return statistics.fmean(ys) if ys else None

def fmt(x,d=2):
    x=finite(x)
    return "—" if x is None else f"{x:.{d}f}"

def git_paths(prefix):
    out=subprocess.check_output(["git","ls-tree","-r","--name-only","HEAD",prefix],cwd=ROOT,text=True)
    return [x.strip() for x in out.splitlines() if x.strip().endswith(".json.gz")]

def path_ts(path):
    stamp=Path(path).name.split("-",1)[0]
    try:
        return datetime.strptime(stamp,"%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()
    except ValueError:
        return None

def sample_paths(paths,seconds=SAMPLE_SECONDS):
    buckets={}
    for p in sorted(paths):
        ts=path_ts(p)
        if ts is None: continue
        k=int(ts//seconds)
        prev=buckets.get(k)
        if prev is None or ts>prev[0]:
            buckets[k]=(ts,p)
    return [buckets[k][1] for k in sorted(buckets)]

def git_json_gz(path):
    raw=subprocess.check_output(["git","show","HEAD:"+path],cwd=ROOT)
    v=json.loads(gzip.decompress(raw).decode("utf-8"))
    return v if isinstance(v,dict) else {}

def extract_features(obs):
    b=obs.get("baseline") or {}
    t=b.get("trend_profile") or {}
    f={
        "opportunity_score":finite(b.get("opportunity_score")),
        "trend_score":finite(b.get("trend_score")),
        "entry_score":finite(b.get("entry_score")),
        "ignition_score":finite(b.get("ignition_score")),
        "change_24h_pct":finite(obs.get("change_24h_pct")),
        "quote_volume_24h_eur":finite(obs.get("quote_volume_24h_eur")),
        "confirm_count":finite(b.get("confirm_count")),
        "since_first_signal_pct":finite(b.get("since_first_signal_pct")),
    }
    for k in ("ret3d","ret7d","ret14d","ret30d","dist_ema20_pct","dist_ema50_pct",
              "ema20_slope_5d_pct","breakout20_pct","drawdown_30d_high_pct",
              "vol3_vs_prev20","green_days_7","rs_btc_3d","rs_btc_7d","rs_btc_14d","rs_btc_30d"):
        f[k]=finite(t.get(k))
    return f

def event_from_obs(ts,market,obs):
    b=obs.get("baseline") or {}
    a=obs.get("acceleration") or {}
    action=str(b.get("action_status") or "UNOBSERVED")
    accel=str(a.get("state") or "NO_ACCELERATION")
    decision=str(obs.get("decision") or "")
    return {
        "ts":ts,"market":market,"price_eur":finite(obs.get("price_eur")),
        "action_status":action,"buy_ready":bool(b.get("buy_ready")),
        "acceleration_state":accel,"decision":decision,
        "features":extract_features(obs),
        "signals":{
            "v4_watch":action in V4_WATCH,
            "v4_entry":action in V4_ENTRY,
            "v4_buy_ready":bool(b.get("buy_ready")),
            "acceleration":accel in ACCEL,
            "confirmed_acceleration":accel=="CONFIRMED_ACCELERATION",
            "pipeline_buy":decision=="ACHÈTE",
        }
    }

def read_hourly_history():
    events=[]
    paths_all=git_paths("history")
    paths=sample_paths(paths_all)
    for p in paths:
        ts=path_ts(p)
        if ts is None: continue
        doc=git_json_gz(p)
        for obs in doc.get("observations") or []:
            if not isinstance(obs,dict) or not obs.get("market"): continue
            events.append(event_from_obs(ts,str(obs["market"]),obs))
    return events,{"all_files":len(paths_all),"sampled_files":len(paths)}

def read_hourly_dl():
    rows=[]
    paths_all=git_paths("decision_history")
    paths=sample_paths(paths_all)
    for p in paths:
        ts=path_ts(p)
        if ts is None: continue
        doc=git_json_gz(p)
        for r in doc.get("ranked") or []:
            if not isinstance(r,dict) or not r.get("market"): continue
            action=str(r.get("action") or "WATCH")
            rows.append({
                "ts":ts,"market":str(r["market"]),"price_eur":finite(r.get("price_eur")),
                "signals":{
                    "dl_actionable": bool(r.get("bucket")) and action not in {"WATCH","VETO_STRUCTUREL"},
                    "dl_buy_now": action=="ACHETE_MAINTENANT",
                }
            })
    return rows,{"all_files":len(paths_all),"sampled_files":len(paths)}

def hourly_rows(raw):
    out=[]
    for item in raw:
        if not isinstance(item,list) or len(item)<6: continue
        vals=[finite(x) for x in item[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        out.append((t/1000.0,o,h,l,c,v))
    return sorted(out)

def build_price_series(markets):
    client=PublicClient(timeout=12,retries=3,requests_per_second=8)
    series={}
    errors=[]
    def one(m):
        raw=client.get("/"+m+"/candles",{"interval":"1h","limit":1000},cache=False)
        return m,hourly_rows(raw)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs={pool.submit(one,m):m for m in markets}
        for fut in as_completed(futs):
            m=futs[fut]
            try:
                k,v=fut.result(); series[k]=v
            except Exception as exc:
                errors.append({"market":m,"error":type(exc).__name__+":"+str(exc)})
    return series,errors,client.diagnostics()

def forward(series,event_ts,entry,hours,now_ts):
    entry=finite(entry)
    if entry is None or entry<=0 or now_ts<event_ts+hours*3600:
        return None
    rows=series
    if not rows: return None
    ts=[x[0] for x in rows]
    i=bisect.bisect_left(ts,event_ts)
    j=bisect.bisect_left(ts,event_ts+hours*3600)
    xs=rows[i:j]
    if not xs: return None
    high=max(x[2] for x in xs); low=min(x[3] for x in xs); close=xs[-1][4]
    return {
        "mfe_pct":(high/entry-1)*100,
        "mae_pct":(low/entry-1)*100,
        "close_pct":(close/entry-1)*100,
        "bars":len(xs),
    }

def episode_starts(events,signal):
    by=defaultdict(list)
    for e in events:
        if e.get("signals",{}).get(signal):
            by[e["market"]].append(e)
    out=[]
    for m,xs in by.items():
        xs.sort(key=lambda e:e["ts"])
        prev=None
        for e in xs:
            if prev is None or e["ts"]-prev>2*SAMPLE_SECONDS:
                out.append(e)
            prev=e["ts"]
    return out

def first_per_market(events,signal):
    out={}
    for e in sorted(events,key=lambda x:x["ts"]):
        if e.get("signals",{}).get(signal) and e["market"] not in out:
            out[e["market"]]=e
    return list(out.values())

def daily_baseline(events):
    # One all-market observation per UTC day: first sampled observation per market/day.
    out={}
    for e in sorted(events,key=lambda x:x["ts"]):
        day=datetime.fromtimestamp(e["ts"],timezone.utc).date().isoformat()
        k=(day,e["market"])
        if k not in out and finite(e.get("price_eur")):
            out[k]=e
    return list(out.values())

def eval_events(events,series,now_ts):
    results={h:[] for h in HORIZONS}
    for e in events:
        s=series.get(e["market"]) or []
        for h in HORIZONS:
            r=forward(s,e["ts"],e.get("price_eur"),h,now_ts)
            if r is not None:
                results[h].append({**r,"market":e["market"],"ts":e["ts"],"features":e.get("features") or {}})
    return results

def summarize(results):
    out={}
    for h,rows in results.items():
        out[str(h)]={
            "n":len(rows),
            "positive_close_pct":100*sum(r["close_pct"]>0 for r in rows)/len(rows) if rows else None,
            "median_close_pct":med([r["close_pct"] for r in rows]),
            "median_mfe_pct":med([r["mfe_pct"] for r in rows]),
            "median_mae_pct":med([r["mae_pct"] for r in rows]),
            **{f"hit_{t}_pct":100*sum(r["mfe_pct"]>=t for r in rows)/len(rows) if rows else None for t in TARGETS},
        }
    return out

def feature_split(rows,target=20):
    winners=[r for r in rows if r["mfe_pct"]>=target]
    misses=[r for r in rows if r["mfe_pct"]<target]
    out={}
    for k in FEATURES:
        a=[(r.get("features") or {}).get(k) for r in winners]
        b=[(r.get("features") or {}).get(k) for r in misses]
        ma,mb=med(a),med(b)
        out[k]={
            "winner_median":ma,"miss_median":mb,
            "delta":(ma-mb) if ma is not None and mb is not None else None,
            "winner_n":sum(x is not None for x in a),
            "miss_n":sum(x is not None for x in b),
        }
    return out

def build():
    now=time.time()
    history,hmeta=read_hourly_history()
    dl,dmeta=read_hourly_dl()
    markets=sorted(set(e["market"] for e in history))
    series,errors,httpdiag=build_price_series(markets)

    # Merge DL states into separate event collection; keep source prices.
    all_signal_events={s:[] for s in SIGNALS}
    for s in ("v4_watch","v4_entry","v4_buy_ready","acceleration","confirmed_acceleration","pipeline_buy"):
        all_signal_events[s]=episode_starts(history,s)
    for s in ("dl_actionable","dl_buy_now"):
        all_signal_events[s]=episode_starts(dl,s)

    baseline=daily_baseline(history)
    baseline_eval=eval_events(baseline,series,now)
    baseline_summary=summarize(baseline_eval)

    episode_eval={}
    episode_summary={}
    first_summary={}
    for s in SIGNALS:
        ev=all_signal_events[s]
        er=eval_events(ev,series,now)
        episode_eval[s]=er
        episode_summary[s]=summarize(er)
        source=history if s not in {"dl_actionable","dl_buy_now"} else dl
        fr=eval_events(first_per_market(source,s),series,now)
        first_summary[s]=summarize(fr)

    watch7=episode_eval["v4_watch"][168]
    feature_analysis=feature_split(watch7,20)

    # Rank features by absolute median separation, only where both groups have enough data.
    ranked=[]
    for k,v in feature_analysis.items():
        if v["delta"] is not None and v["winner_n"]>=20 and v["miss_n"]>=20:
            ranked.append({"feature":k,**v})
    ranked.sort(key=lambda x:abs(x["delta"]),reverse=True)

    return {
        "schema":"human_swing_precision_v1",
        "generated_at_utc":utc(),
        "measurement_only":True,
        "affects_production":False,
        "history_sampling":hmeta,
        "decision_history_sampling":dmeta,
        "markets_with_history":len(markets),
        "price_series_errors":errors,
        "http_diagnostics":httpdiag,
        "definitions":{
            "sampling":"last committed Solaire state in each UTC hour",
            "episode":"new signal episode after >2h without that signal",
            "baseline":"first sampled observation per market per UTC day, regardless of Solaire state",
            "forward_metric":"MFE/MAE/close from event price over complete 24h/48h/72h/7d windows",
            "human_relevance":"intrahour-only signals intentionally do not count as durable evidence",
        },
        "baseline_daily_all_markets":baseline_summary,
        "signal_episode_summary":episode_summary,
        "signal_first_per_market_summary":first_summary,
        "episode_counts":{s:len(all_signal_events[s]) for s in SIGNALS},
        "watch_7d_feature_split_target_20pct_mfe":feature_analysis,
        "watch_7d_feature_ranked_abs_median_delta":ranked,
    }

def render(p):
    lines=[
        "# Solaire Human/Swing precision audit","",
        f"Generated: {p['generated_at_utc']}",
        "Measurement only. No production behavior changed.","",
        "## Baseline vs Solaire signal precision","",
        "Success below means the price reached the target at least once within the forward window (MFE).",
        "",
        "| Source | Horizon | N | Close >0 | Hit +5 | Hit +10 | Hit +20 | Hit +30 | Median MFE | Median MAE |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    order=[
        ("BASELINE",p["baseline_daily_all_markets"]),
        ("V4 WATCH episodes",p["signal_episode_summary"]["v4_watch"]),
        ("V4 ENTRY episodes",p["signal_episode_summary"]["v4_entry"]),
        ("V4 BUY_READY episodes",p["signal_episode_summary"]["v4_buy_ready"]),
        ("ACCELERATION episodes",p["signal_episode_summary"]["acceleration"]),
        ("CONFIRMED ACCEL episodes",p["signal_episode_summary"]["confirmed_acceleration"]),
        ("PIPELINE ACHETE episodes",p["signal_episode_summary"]["pipeline_buy"]),
        ("DL actionable episodes",p["signal_episode_summary"]["dl_actionable"]),
        ("DL ACHETE_MAINTENANT episodes",p["signal_episode_summary"]["dl_buy_now"]),
    ]
    for label,block in order:
        for h in HORIZONS:
            r=block[str(h)]
            lines.append(
                f"| {label} | {h}h | {r['n']} | {fmt(r.get('positive_close_pct'))}% | "
                f"{fmt(r.get('hit_5_pct'))}% | {fmt(r.get('hit_10_pct'))}% | {fmt(r.get('hit_20_pct'))}% | "
                f"{fmt(r.get('hit_30_pct'))}% | {fmt(r.get('median_mfe_pct'))}% | {fmt(r.get('median_mae_pct'))}% |"
            )
    lines+=["","## Signal episode counts",""]
    for s,n in p["episode_counts"].items():
        lines.append(f"- {s}: {n}")
    lines+=["","## WATCH features: 7d episodes that reached +20% vs misses","",
            "| Feature | Winner median | Miss median | Delta | Winner N | Miss N |",
            "|---|---:|---:|---:|---:|---:|"]
    for r in p["watch_7d_feature_ranked_abs_median_delta"][:20]:
        lines.append(
            f"| {r['feature']} | {fmt(r['winner_median'])} | {fmt(r['miss_median'])} | "
            f"{fmt(r['delta'])} | {r['winner_n']} | {r['miss_n']} |"
        )
    lines+=["","## Method notes","",
            f"- History: {p['history_sampling']['sampled_files']} hourly samples from {p['history_sampling']['all_files']} committed journals.",
            f"- Decision Layer: {p['decision_history_sampling']['sampled_files']} hourly samples from {p['decision_history_sampling']['all_files']} journals.",
            "- Repeated hourly presence is collapsed into episodes; a new episode begins only after more than two hours without the state.",
            "- Baseline is not a trading strategy; it is a neutral reference for how easy the market regime was.",
            "- MFE is ex-post maximum favorable excursion, so hit rates measure opportunity presence, not realized PnL.",
            "- Only complete forward windows are included.",
            ""]
    return "\n".join(lines)

def main():
    p=build()
    atomic_json(OUT_JSON,p)
    Path(OUT_MD).write_text(render(p),encoding="utf-8")
    print(json.dumps({
        "markets":p["markets_with_history"],
        "episode_counts":p["episode_counts"],
        "baseline":p["baseline_daily_all_markets"],
        "v4_watch":p["signal_episode_summary"]["v4_watch"],
        "dl_buy_now":p["signal_episode_summary"]["dl_buy_now"],
        "top_feature_deltas":p["watch_7d_feature_ranked_abs_median_delta"][:10],
    },ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
