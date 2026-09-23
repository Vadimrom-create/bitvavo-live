#!/usr/bin/env python3
from __future__ import annotations
import gzip, json, math, statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

COST_PCT=0.70
MAX_MATCH_LAG_S=30*60
GREENLIGHT_WINDOW_H=24
HORIZONS=(4,12,24)

def f(x):
    try:
        y=float(x)
        return y if math.isfinite(y) else None
    except Exception:
        return None

def ts_name(p):
    return datetime.strptime(p.name.split("-",1)[0],"%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()

def med(xs):
    xs=sorted(xs)
    if not xs:return None
    n=len(xs)
    return xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2

def load_old():
    snaps=[]
    timeline=defaultdict(list)
    for day in sorted(Path("decision_history").glob("2026-*")):
        if day.name < "2026-09-21": continue
        for p in sorted(day.glob("*.json.gz")):
            try:
                with gzip.open(p,"rt",encoding="utf-8") as fh: o=json.load(fh)
            except Exception:
                continue
            if o.get("policy")!="DECISION_LAYER_V1_SHADOW": continue
            ts=ts_name(p)
            rows={}
            for r in o.get("ranked",[]):
                m=r.get("market")
                px=f(r.get("price_eur"))
                if m and px:
                    rows[m]=r
                    timeline[m].append((ts,px))
            snaps.append((ts,rows))
    for m in timeline: timeline[m].sort()
    return snaps,timeline

def old_state_at(snaps, market, ts):
    best=None
    for t,rows in snaps:
        if t>ts: break
        if ts-t<=MAX_MATCH_LAG_S and market in rows:
            best=(t,rows[market])
    return best

def first_greenlight(snaps, market, ts):
    end=ts+GREENLIGHT_WINDOW_H*3600
    for t,rows in snaps:
        if t<ts: continue
        if t>end: break
        r=rows.get(market)
        if not r: continue
        if r.get("action")=="ACHETE_MAINTENANT":
            return t,r
    return None

def price_eval(timeline, market, entry_ts, entry_px, horizon_h):
    pts=[(t,p) for t,p in timeline.get(market,[]) if t>=entry_ts and t<=entry_ts+horizon_h*3600]
    after=[(t,p) for t,p in timeline.get(market,[]) if t>=entry_ts+horizon_h*3600]
    if not pts or not after or after[0][0]-entry_ts-horizon_h*3600>45*60: return None
    vals=[(p/entry_px-1)*100 for _,p in pts]
    close=(after[0][1]/entry_px-1)*100
    return {"mfe_pct":max(vals),"mae_pct":min(vals),"close_pct":close,"net_close_pct_est":close-COST_PCT}

def summarize(rows,key,h):
    vals=[r.get(key,{}).get(str(h)) for r in rows]
    vals=[v for v in vals if v]
    if not vals:return {"n":0}
    return {
      "n":len(vals),
      "mean_net_close_pct_est":round(statistics.mean(v["net_close_pct_est"] for v in vals),3),
      "median_net_close_pct_est":round(med([v["net_close_pct_est"] for v in vals]),3),
      "median_mfe_pct":round(med([v["mfe_pct"] for v in vals]),3),
      "median_mae_pct":round(med([v["mae_pct"] for v in vals]),3),
      "mfe_ge_10":sum(v["mfe_pct"]>=10 for v in vals),
      "positive_net_close":sum(v["net_close_pct_est"]>0 for v in vals),
      "mae_le_minus5":sum(v["mae_pct"]<=-5 for v in vals),
    }

def main():
    snaps,timeline=load_old()
    j=json.loads(Path("production_decision_journal.json").read_text(encoding="utf-8"))
    buys=[e for e in j.get("entries",[]) if e.get("decision_type")=="BUY_SENT"]
    rows=[]
    for b in buys:
        m=b["market"]; ts=f(b.get("decision_ts")); entry=f(b.get("entry_eur"))
        if ts is None or entry is None: continue
        state=old_state_at(snaps,m,ts)
        green=first_greenlight(snaps,m,ts)
        rec={
          "market":m,"v2_ts":ts,"v2_entry":entry,
          "v2_stop":f(b.get("stop_eur")),"v2_tp1":f(b.get("tp1_eur")),
          "v2_24_result":(b.get("evaluations",{}).get("24") or {}).get("result"),
          "old_at_v2":None,"greenlight":None,"v2_eval":{},"hybrid_eval":{}
        }
        if state:
            ot,orow=state
            rec["old_at_v2"]={
              "lag_min":round((ts-ot)/60,2),
              "action":orow.get("action"),
              "bucket":orow.get("bucket"),
              "entry_score":f(orow.get("entry_score")),
              "opportunity_score":f(orow.get("opportunity_score")),
              "trend_score":f(orow.get("trend_score")),
              "price_eur":f(orow.get("price_eur")),
              "reason":orow.get("reason"),
            }
        for h in HORIZONS:
            ev=b.get("evaluations",{}).get(str(h))
            if ev:
                rec["v2_eval"][str(h)]={
                  "mfe_pct":f(ev.get("mfe_pct")),
                  "mae_pct":f(ev.get("mae_pct")),
                  "close_pct":f(ev.get("close_return_pct")),
                  "net_close_pct_est":f(ev.get("close_return_pct"))-COST_PCT if f(ev.get("close_return_pct")) is not None else None,
                  "result":ev.get("result"),
                }
        if green:
            gt,grow=green; gpx=f(grow.get("price_eur"))
            rec["greenlight"]={
              "delay_min":round((gt-ts)/60,2),"entry_eur":gpx,
              "price_vs_v2_pct":round((gpx/entry-1)*100,3) if gpx else None,
              "old_entry_score":f(grow.get("entry_score")),
              "old_opportunity_score":f(grow.get("opportunity_score")),
              "old_trend_score":f(grow.get("trend_score")),
            }
            if gpx:
                for h in HORIZONS:
                    ev=price_eval(timeline,m,gt,gpx,h)
                    if ev: rec["hybrid_eval"][str(h)]=ev
        rows.append(rec)

    matched=[r for r in rows if r["old_at_v2"]]
    cats=Counter((r["old_at_v2"] or {}).get("action","NO_MATCH") for r in rows)
    by_action={}
    for action in sorted(cats):
        rr=[r for r in matched if r["old_at_v2"]["action"]==action]
        mature=[r for r in rr if "24" in r["v2_eval"]]
        if mature:
            by_action[action]={
              "count":len(rr),"mature24":len(mature),
              "v2_stop24":sum(r["v2_eval"]["24"].get("result")=="STOP" for r in mature),
              "v2_tp124":sum(r["v2_eval"]["24"].get("result")=="TP1" for r in mature),
              "median_v2_mae24":round(med([r["v2_eval"]["24"]["mae_pct"] for r in mature]),3),
              "median_v2_mfe24":round(med([r["v2_eval"]["24"]["mfe_pct"] for r in mature]),3),
              "mean_v2_net_close24":round(statistics.mean(r["v2_eval"]["24"]["net_close_pct_est"] for r in mature),3),
            }
    greenrows=[r for r in rows if r["greenlight"]]
    report={
      "schema":"v2_detection_old_timing_counterfactual_v1",
      "generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "method":{
        "v2_population":"actual BUY_SENT events from production_decision_journal.json",
        "old_timing":"nearest prior DECISION_LAYER_V1_SHADOW classification, max 30m lag",
        "hybrid_rule":"after V2 BUY_SENT, delay entry until first Old action ACHETE_MAINTENANT within 24h; skip if no greenlight",
        "cost_pct":COST_PCT,
        "warning":"Counterfactual audit from archived decision snapshots; not proof of future edge."
      },
      "counts":{
        "v2_buy_sent":len(rows),"old_state_matched":len(matched),
        "hybrid_greenlight":len(greenrows),"hybrid_skipped":len(rows)-len(greenrows),
        "old_action_at_v2":dict(cats)
      },
      "v2_outcome_by_old_action":by_action,
      "baseline_v2":{str(h):summarize(rows,"v2_eval",h) for h in HORIZONS},
      "hybrid_old_greenlight":{str(h):summarize(greenrows,"hybrid_eval",h) for h in HORIZONS},
      "rows":rows,
    }
    Path("v2_old_timing_audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    md=["# V2 detection + Old timing counterfactual","",
        f"V2 BUY_SENT: {len(rows)}; Old matched: {len(matched)}; hybrid greenlights: {len(greenrows)}; skipped: {len(rows)-len(greenrows)}.","",
        "## Old action at the exact V2 buy moment","",
        "| Old action | V2 buys | mature 24h | V2 stops | V2 TP1 | median MAE | median MFE | mean net close |",
        "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for a,d in sorted(by_action.items(),key=lambda kv:-kv[1]["count"]):
        md.append(f"| {a} | {d['count']} | {d['mature24']} | {d['v2_stop24']} | {d['v2_tp124']} | {d['median_v2_mae24']:.2f}% | {d['median_v2_mfe24']:.2f}% | {d['mean_v2_net_close24']:.2f}% |")
    md += ["","## Counterfactual","",
           "| Policy | Horizon | n | mean net close | median MFE | median MAE | +10% MFE | positive net close | MAE <= -5% |",
           "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for h in HORIZONS:
        for label,key in (("V2 actual","baseline_v2"),("V2 detect + Old greenlight","hybrid_old_greenlight")):
            d=report[key][str(h)]
            if not d.get("n"): continue
            md.append(f"| {label} | {h}h | {d['n']} | {d['mean_net_close_pct_est']:.2f}% | {d['median_mfe_pct']:.2f}% | {d['median_mae_pct']:.2f}% | {d['mfe_ge_10']} | {d['positive_net_close']} | {d['mae_le_minus5']} |")
    Path("v2_old_timing_audit.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("counts","v2_outcome_by_old_action","baseline_v2","hybrid_old_greenlight")},ensure_ascii=False))

if __name__=="__main__": main()
