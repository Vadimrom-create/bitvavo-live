#!/usr/bin/env python3
from __future__ import annotations
import gzip,json,math,statistics
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path

COST=0.70
H=24

def f(x):
    try:
        y=float(x); return y if math.isfinite(y) else None
    except Exception:return None

def tsn(p):
    return datetime.strptime(p.name.split("-",1)[0],"%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc).timestamp()

def med(a):
    a=sorted(a)
    if not a:return None
    return a[len(a)//2] if len(a)%2 else (a[len(a)//2-1]+a[len(a)//2])/2

def load_timeline():
    tl=defaultdict(list)
    for day in sorted(Path("decision_history").glob("2026-*")):
        if day.name<"2026-09-21":continue
        for p in sorted(day.glob("*.json.gz")):
            try:
                with gzip.open(p,"rt",encoding="utf-8") as fh:o=json.load(fh)
            except Exception:continue
            if o.get("policy")!="DECISION_LAYER_V1_SHADOW":continue
            t=tsn(p)
            for r in o.get("ranked",[]):
                m=r.get("market"); px=f(r.get("price_eur"))
                if m and px:tl[m].append((t,px))
    for m in tl:tl[m].sort()
    return tl

def first_at(tl,m,target,maxlag=1800):
    for t,p in tl.get(m,[]):
        if t>=target:
            return (t,p) if t-target<=maxlag else None
    return None

def evaluate(tl,m,ets,epx,stop=None):
    pts=[(t,p) for t,p in tl.get(m,[]) if ets<=t<=ets+H*3600]
    close=first_at(tl,m,ets+H*3600,2700)
    if not pts or not close:return None
    rr=[(p/epx-1)*100 for _,p in pts]
    return {"mfe":max(rr),"mae":min(rr),"net":(close[1]/epx-1)*100-COST,
            "stop_proxy":bool(stop and min(p for _,p in pts)<=stop)}

def delayed(tl,b,mins,band=None):
    q=first_at(tl,b["market"],b["decision_ts"]+mins*60,1800)
    if not q:return None
    t,p=q; base=b["entry_eur"]; ch=(p/base-1)*100
    if band and not (band[0]<=ch<=band[1]):return None
    return t,p

def pullback_reclaim(tl,b,dip=-2.0,reclaim=1.0,window_h=6):
    base=b["entry_eur"]; low=None
    for t,p in tl.get(b["market"],[]):
        if t<b["decision_ts"]:continue
        if t>b["decision_ts"]+window_h*3600:break
        ch=(p/base-1)*100
        if low is None:
            if ch<=dip:low=(t,p)
        else:
            lowp=low[1]
            if p<lowp:low=(t,p);lowp=p
            if (p/lowp-1)*100>=reclaim and p<=base*1.03:
                return t,p
    return None

def summarize(rows):
    if not rows:return {"n":0}
    return {"n":len(rows),"mean_net":round(statistics.mean(x["net"] for x in rows),3),
            "median_net":round(med([x["net"] for x in rows]),3),
            "median_mfe":round(med([x["mfe"] for x in rows]),3),
            "median_mae":round(med([x["mae"] for x in rows]),3),
            "mfe10":sum(x["mfe"]>=10 for x in rows),
            "mae7":sum(x["mae"]<=-7 for x in rows),
            "stop_proxy":sum(x["stop_proxy"] for x in rows),
            "positive":sum(x["net"]>0 for x in rows)}

def main():
    tl=load_timeline()
    j=json.loads(Path("production_decision_journal.json").read_text())
    buys=[e for e in j.get("entries",[]) if e.get("decision_type")=="BUY_SENT" and e.get("evaluations",{}).get("24")]
    policies={
      "baseline_snapshot":[],
      "delay30":[],
      "delay60":[],
      "persist30_band_-2_+3":[],
      "persist60_band_-2_+3":[],
      "pullback2_reclaim1":[],
      "strength_score8_rel4_4_then_delay30":[],
    }
    details=[]
    for b in buys:
        m=b["market"]; ts=f(b.get("decision_ts")); ep=f(b.get("entry_eur")); stop=f(b.get("stop_eur"))
        if ts is None or ep is None:continue
        base=evaluate(tl,m,ts,ep,stop)
        if base:policies["baseline_snapshot"].append(base)
        choices={}
        for name,mins,band in [
          ("delay30",30,None),("delay60",60,None),
          ("persist30_band_-2_+3",30,(-2,3)),("persist60_band_-2_+3",60,(-2,3))]:
            q=delayed(tl,b,mins,band)
            if q:
                ev=evaluate(tl,m,q[0],q[1],stop)
                if ev:policies[name].append(ev);choices[name]={"delay_min":round((q[0]-ts)/60,1),"price_delta_pct":round((q[1]/ep-1)*100,3),**ev}
        q=pullback_reclaim(tl,b)
        if q:
            ev=evaluate(tl,m,q[0],q[1],stop)
            if ev:policies["pullback2_reclaim1"].append(ev);choices["pullback2_reclaim1"]={"delay_min":round((q[0]-ts)/60,1),"price_delta_pct":round((q[1]/ep-1)*100,3),**ev}
        if f(b.get("signal_score")) is not None and b["signal_score"]>=8 and f((b.get("context") or {}).get("relative_strength_4h_pp")) is not None and b["context"]["relative_strength_4h_pp"]>=4:
            q=delayed(tl,b,30,(-2,3))
            if q:
                ev=evaluate(tl,m,q[0],q[1],stop)
                if ev:policies["strength_score8_rel4_4_then_delay30"].append(ev);choices["strength_score8_rel4_4_then_delay30"]={"delay_min":round((q[0]-ts)/60,1),"price_delta_pct":round((q[1]/ep-1)*100,3),**ev}
        details.append({"market":m,"v2_result24":b["evaluations"]["24"]["result"],"signal_score":b.get("signal_score"),"rel4":(b.get("context") or {}).get("relative_strength_4h_pp"),"choices":choices})
    report={"schema":"v2_entry_timing_variants_v1","generated_at_utc":datetime.now(timezone.utc).isoformat(),
      "method":{"population":"V2 BUY_SENT with mature 24h outcome","prices":"archived Old Decision Layer snapshot prices (~15m cadence)","warning":"Coarse snapshot counterfactual; stop_proxy can miss intrabar stop touches."},
      "summary":{k:summarize(v) for k,v in policies.items()},"details":details}
    Path("v2_entry_timing_variants.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
    lines=["# V2 entry timing variants","",
      "| Policy | n | mean net 24h | median MFE | median MAE | MFE >=10 | MAE <= -7 | stop proxy | positive |",
      "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for k,d in report["summary"].items():
        if d.get("n"):lines.append(f"| {k} | {d['n']} | {d['mean_net']:.2f}% | {d['median_mfe']:.2f}% | {d['median_mae']:.2f}% | {d['mfe10']} | {d['mae7']} | {d['stop_proxy']} | {d['positive']} |")
    Path("v2_entry_timing_variants.md").write_text("\n".join(lines)+"\n")
    print(json.dumps(report["summary"],ensure_ascii=False))
if __name__=="__main__":main()
