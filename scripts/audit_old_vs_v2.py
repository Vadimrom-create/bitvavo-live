#!/usr/bin/env python3
from __future__ import annotations
import gzip, json, math, statistics
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

START_DAY = "2026-09-20"
ROUND_TRIP_COST_PCT = 0.70
REFERENCE_STAKE_EUR = 100.0
HORIZONS_H = (4, 24, 48, 72)

def ts_from_name(p: Path) -> float:
    s=p.name.split("-",1)[0]
    return datetime.strptime(s,"%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()

def walk(obj, path="$"):
    yield path,obj
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield from walk(v,f"{path}.{k}")
    elif isinstance(obj,list):
        for i,v in enumerate(obj):
            yield from walk(v,f"{path}[{i}]")

def fnum(x):
    try:
        v=float(x)
        return v if math.isfinite(v) else None
    except Exception:
        return None

def market_of(d):
    if not isinstance(d,dict): return None
    m=d.get("market") or d.get("symbol")
    return m if isinstance(m,str) and m.endswith("-EUR") else None

def price_of(d):
    if not isinstance(d,dict): return None
    for k in ("price_eur","last","price","entry_eur"):
        v=fnum(d.get(k))
        if v and v>0: return v
    return None

def stop_of(d):
    if not isinstance(d,dict): return None
    for k in ("stop_eur","stop","stop_loss","stop_loss_eur"):
        v=fnum(d.get(k))
        if v and v>0: return v
    tp=d.get("trade_plan")
    if isinstance(tp,dict):
        v=fnum(tp.get("stop_eur"))
        if v and v>0: return v
    return None

def load_snapshots():
    snaps=[]
    root=Path("decision_history")
    for day in sorted(root.glob("2026-*")):
        if day.name < START_DAY: continue
        for p in sorted(day.glob("*.json.gz")):
            try:
                with gzip.open(p,"rt",encoding="utf-8") as fh:
                    obj=json.load(fh)
                snaps.append((ts_from_name(p),p,obj))
            except Exception:
                continue
    return snaps

def extract_prices(obj):
    vals=defaultdict(list)
    for _,x in walk(obj):
        if isinstance(x,dict):
            m=market_of(x); px=price_of(x)
            if m and px: vals[m].append(px)
    out={}
    for m,a in vals.items():
        # median damps duplicated stale/entry/quote fields in the same snapshot
        out[m]=statistics.median(a)
    return out

def find_old_rows(obj):
    out=[]
    for path,x in walk(obj):
        if not isinstance(x,dict): continue
        policy=str(x.get("policy") or x.get("schema") or "")
        if "DECISION_LAYER_V1" in policy and isinstance(x.get("top_actionable"),list):
            for r in x["top_actionable"]:
                if isinstance(r,dict) and market_of(r):
                    rr=dict(r); rr["_source_path"]=path+".top_actionable"; out.append(rr)
    return out

def find_v2_watch(obj):
    out=[]
    for path,x in walk(obj):
        if not isinstance(x,dict): continue
        schema=str(x.get("schema") or "")
        policy=str(x.get("policy") or "")
        if ("production_alert_candidates" in schema.lower() or "FULL_UNIVERSE_DIRECT_SCAN" in policy) and isinstance(x.get("watch"),list):
            for r in x["watch"]:
                if isinstance(r,dict) and market_of(r):
                    rr=dict(r); rr["_source_path"]=path+".watch"; out.append(rr)
    return out

def find_v2_delivered(obj):
    out=[]
    for path,x in walk(obj):
        if not isinstance(x,dict): continue
        if x.get("email")=="DELIVERY_COMPLETED" and market_of(x):
            rr=dict(x); rr["_source_path"]=path; out.append(rr)
    return out

def dedupe_events(raw, cooldown_h=6):
    raw=sorted(raw,key=lambda e:e["ts"])
    last={}
    out=[]
    for e in raw:
        k=(e["system"],e["market"])
        prev=last.get(k)
        if prev is None or e["ts"]-prev >= cooldown_h*3600:
            out.append(e); last[k]=e["ts"]
    return out

def nearest_at_or_after(series, target, max_slip_s=1800):
    for ts,px in series:
        if ts>=target:
            return (ts,px) if ts-target<=max_slip_s else None
    return None

def evaluate_event(e, timeline):
    s=timeline.get(e["market"],[])
    future=[(t,p) for t,p in s if t>=e["ts"]]
    if not future: return None
    entry=e.get("entry_price")
    if not entry:
        q=nearest_at_or_after(s,e["ts"],1800)
        if not q: return None
        entry=q[1]
    out={"market":e["market"],"ts":e["ts"],"entry":entry,"stop":e.get("stop"),"system":e["system"]}
    for h in HORIZONS_H:
        end=e["ts"]+h*3600
        pts=[(t,p) for t,p in future if t<=end]
        close=nearest_at_or_after(s,end,2400)
        if not pts or not close:
            continue
        rets=[(p/entry-1)*100 for _,p in pts]
        out[str(h)]={
            "mfe_pct":max(rets),
            "mae_pct":min(rets),
            "close_pct":(close[1]/entry-1)*100,
            "net_close_pct_est":(close[1]/entry-1)*100-ROUND_TRIP_COST_PCT,
            "hit_10":max(rets)>=10,
            "hit_20":max(rets)>=20,
        }
    if e.get("stop"):
        out["stop_distance_pct"]=(e["stop"]/entry-1)*100
    return out

def summary(rows,h):
    vals=[r[str(h)] for r in rows if str(h) in r]
    if not vals: return {"n":0}
    net=[v["net_close_pct_est"] for v in vals]
    return {
        "n":len(vals),
        "mean_net_close_pct_est":round(statistics.mean(net),3),
        "median_net_close_pct_est":round(statistics.median(net),3),
        "median_mfe_pct":round(statistics.median(v["mfe_pct"] for v in vals),3),
        "median_mae_pct":round(statistics.median(v["mae_pct"] for v in vals),3),
        "mfe_ge_10":sum(v["hit_10"] for v in vals),
        "mfe_ge_20":sum(v["hit_20"] for v in vals),
        "positive_net_close":sum(v["net_close_pct_est"]>0 for v in vals),
        "stake100_pnl_eur_sum_est":round(sum(v["net_close_pct_est"] for v in vals),2),
    }

def main():
    snaps=load_snapshots()
    timeline=defaultdict(list)
    raw=[]
    schema_paths=Counter()
    for ts,p,obj in snaps:
        prices=extract_prices(obj)
        for m,px in prices.items(): timeline[m].append((ts,px))
        old=find_old_rows(obj); v2=find_v2_watch(obj); sent=find_v2_delivered(obj)
        for r in old:
            raw.append({"system":"OLD_DECISION_LAYER","market":market_of(r),"ts":ts,"entry_price":price_of(r) or prices.get(market_of(r)),"stop":stop_of(r),"row":r})
        for r in v2:
            raw.append({"system":"V2_WATCH","market":market_of(r),"ts":ts,"entry_price":price_of(r) or prices.get(market_of(r)),"stop":stop_of(r),"row":r})
        for r in sent:
            raw.append({"system":"V2_DELIVERED","market":market_of(r),"ts":ts,"entry_price":prices.get(market_of(r)),"stop":stop_of(r),"row":r})
        for path,x in walk(obj):
            if isinstance(x,dict) and ("policy" in x or "schema" in x):
                tag=str(x.get("policy") or x.get("schema"))
                if "DECISION" in tag.upper() or "PRODUCTION_ALERT" in tag.upper():
                    schema_paths[(path,tag)] += 1
    for m in timeline: timeline[m].sort()
    events=dedupe_events(raw)
    evaluated=[x for e in events if (x:=evaluate_event(e,timeline))]
    systems=sorted(set(e["system"] for e in events))
    report={
      "schema":"old_vs_solaire_v2_audit_v1",
      "generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "window":{"start_day":START_DAY,"snapshots":len(snaps),"last_snapshot_utc":datetime.fromtimestamp(snaps[-1][0],timezone.utc).isoformat() if snaps else None},
      "method":{
        "old_reference_commit":"3628856b6dceb27f82d0cceac960348c38933eed",
        "old_definition":"DECISION_LAYER_V1_SHADOW top_actionable found in archived snapshots",
        "v2_definition":"production_alert_candidates watch; actual DELIVERY_COMPLETED split separately when present",
        "dedupe_cooldown_hours":6,
        "round_trip_cost_pct_est":ROUND_TRIP_COST_PCT,
        "reference_stake_eur":REFERENCE_STAKE_EUR,
        "warning":"Signal-quality comparison from archived snapshots; stake100 PnL sums independent hypothetical positions and is not an account-equity backtest."
      },
      "event_counts":Counter(e["system"] for e in events),
      "summary":{sys:{str(h):summary([r for r in evaluated if r["system"]==sys],h) for h in HORIZONS_H} for sys in systems},
      "events":[{k:v for k,v in r.items() if k!="row"} for r in evaluated],
      "coverage":{"timeline_markets":len(timeline),"schema_paths_top":[{"path":p,"tag":t,"count":n} for (p,t),n in schema_paths.most_common(25)]}
    }
    Path("old_vs_v2_audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    lines=["# Old vs Solaire V2 — archived snapshot audit","",f"Snapshots: {len(snaps)} from {START_DAY}.","",f"Old reference commit: `{report['method']['old_reference_commit']}`.",""]
    for sys in systems:
        lines.append(f"## {sys}")
        lines.append("")
        lines.append("| Horizon | n | mean net close | median MFE | median MAE | +10% MFE | positive net close | Σ PnL / 100€ signals |")
        lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|")
        for h in HORIZONS_H:
            s=report["summary"][sys][str(h)]
            if not s.get("n"):
                lines.append(f"| {h}h | 0 | — | — | — | — | — | — |")
            else:
                lines.append(f"| {h}h | {s['n']} | {s['mean_net_close_pct_est']:.2f}% | {s['median_mfe_pct']:.2f}% | {s['median_mae_pct']:.2f}% | {s['mfe_ge_10']} | {s['positive_net_close']} | {s['stake100_pnl_eur_sum_est']:.2f} € |")
        lines.append("")
    lines += ["## Method note","","This is a same-archive signal-quality comparison. It does not claim actual executable account PnL; overlapping hypothetical positions are summed independently. V2 delivered emails are reported separately when the archive contains DELIVERY_COMPLETED state."]
    Path("old_vs_v2_audit.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"events":report["event_counts"],"summary":report["summary"],"coverage":report["coverage"]},ensure_ascii=False))

if __name__=="__main__":
    main()
