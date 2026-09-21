#!/usr/bin/env python3
"""Adversarial timing audit for Solaire V2 detector on 2026-09-21.

Replays the current acceleration detector over historical Bitvavo candles for the
whole active EUR universe. Compares current BUILDING/CONFIRMED timing with two
earlier shadow thresholds. Research-only; never changes production decisions.
"""
from __future__ import annotations
import json, math, statistics, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_acceleration import acceleration_signal

OUT="research/solaire_v2_detection_timing_20260921.json"
START_TS=1790006400.0  # 2026-09-21T16:00:00Z placeholder overwritten below
START_UTC="2026-09-21T08:00:00+00:00"
MANDATORY={"FET-EUR","NIL-EUR"}
THRESHOLDS={
    "early_4_25_e2": (4.25,2),
    "early_5_00_e2": (5.00,2),
    "current_building": (4.75,2),
    "high_quality_building": (6.00,4),
    "current_confirmed": (6.50,3),
}

def iso_ts(s):
    from datetime import datetime
    return datetime.fromisoformat(s.replace("Z","+00:00")).timestamp()

def raw_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        out.append((t/1000.0,o,h,l,c,v))
    return sorted(out)

def price_before(rows, t):
    xs=[x for x in rows if x[0]+300 <= t+1e-6]
    return xs[-1][4] if xs else None

def forward(rows,t0,base,hours=4):
    if not base or base<=0: return None
    end=t0+hours*3600
    xs=[x for x in rows if t0 <= x[0] < end]
    if not xs: return None
    return {
        "mfe_pct": round((max(x[2] for x in xs)/base-1)*100,4),
        "mae_pct": round((min(x[3] for x in xs)/base-1)*100,4),
        "close_pct": round((xs[-1][4]/base-1)*100,4),
        "bars": len(xs),
        "complete": xs[-1][0] >= end-600,
    }

def first_signals(raw5,raw15,start,now):
    result={k:None for k in THRESHOLDS}
    t=math.ceil(start/300)*300
    while t<=now:
        c5=closed_candles(raw5,"5m",t)
        c15=closed_candles(raw15,"15m",t)
        f5=describe(c5,"5m"); f15=describe(c15,"15m")
        if f5.get("valid") and f15.get("valid"):
            acc=acceleration_signal({"features":{"5m":f5,"15m":f15}})
            score=finite(acc.get("score")); ev=int(acc.get("evidence_count") or 0)
            px=finite(f5.get("last_close_eur"))
            if score is not None and px and px>0:
                for name,(smin,emin) in THRESHOLDS.items():
                    if result[name] is None and score>=smin and ev>=emin:
                        result[name]={"at_utc":utc(t),"ts":t,"price_eur":px,
                                      "score":score,"evidence_count":ev,
                                      "components":acc.get("components")}
        if all(v is not None for v in result.values()): break
        t+=300
    return result

def median(xs):
    return round(statistics.median(xs),4) if xs else None

def main():
    start=iso_ts(START_UTC); now=time.time()
    client=PublicClient(timeout=12,retries=3,requests_per_second=10)
    client.get("/time",cache=False)
    metas=[m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"]
    ticks={x["market"]:x for x in client.get("/ticker/24h") if x.get("market")}
    markets=[]
    errors=[]
    for i,m in enumerate(sorted(metas,key=lambda x:x["market"])):
        market=m["market"]
        try:
            r5=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
            r15=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            rows=raw_rows(r5)
            if not rows: continue
            base=price_before(rows,start)
            last=rows[-1][4]
            if base is None or base<=0: continue
            session_ret=(last/base-1)*100
            sig=first_signals(r5,r15,start,now)
            out={"market":market,"session_base_eur":base,"last_eur":last,
                 "session_return_pct":round(session_ret,4),
                 "quote_volume_24h_eur":finite((ticks.get(market) or {}).get("volumeQuote"),0.0),
                 "signals":sig}
            for name,event in sig.items():
                if event:
                    event["move_consumed_pct"]=(
                        round(((event["price_eur"]/base-1)/(last/base-1))*100,2)
                        if last>base and event["price_eur"]>=base else None
                    )
                    event["remaining_to_last_pct"]=round((last/event["price_eur"]-1)*100,4)
                    event["forward_4h"]=forward(rows,event["ts"],event["price_eur"],4)
            markets.append(out)
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    winners=sorted(markets,key=lambda x:x["session_return_pct"],reverse=True)[:30]
    focus={x["market"]:x for x in winners}
    for m in MANDATORY:
        row=next((x for x in markets if x["market"]==m),None)
        if row: focus[m]=row

    comparisons={}
    for name in THRESHOLDS:
        evs=[]
        evs_liquid=[]
        for row in markets:
            e=row["signals"].get(name)
            if not e: continue
            f=e.get("forward_4h")
            if not f or not f.get("complete"): continue
            evs.append(f)
            if row["quote_volume_24h_eur"]>=75000: evs_liquid.append(f)
        def stats(xs):
            return {"n":len(xs),"mfe_ge_5pct":sum(x["mfe_pct"]>=5 for x in xs),
                    "mae_le_minus5pct":sum(x["mae_pct"]<=-5 for x in xs),
                    "median_mfe_pct":median([x["mfe_pct"] for x in xs]),
                    "median_mae_pct":median([x["mae_pct"] for x in xs]),
                    "median_close_pct":median([x["close_pct"] for x in xs])}
        comparisons[name]={"all":stats(evs),"liquid_ge_75k":stats(evs_liquid)}

    payload={"schema":"solaire_v2_detection_timing_audit_v1","generated_at_utc":utc(),
             "session_start_utc":START_UTC,"research_only":True,
             "affects_detection":False,"affects_buy_gate":False,"affects_email":False,
             "thresholds":{k:{"score_min":v[0],"evidence_min":v[1]} for k,v in THRESHOLDS.items()},
             "universe_count":len(markets),"errors":errors,
             "comparisons_4h":comparisons,
             "markets":markets,
             "top_session_winners":winners,
             "focus_markets":focus}
    atomic_json(OUT,payload)
    print("SOLAIRE_DETECTION_TIMING "+json.dumps({"universe":len(markets),"comparisons":comparisons,
      "focus":{m:{k:v for k,v in focus[m].items() if k!="signals"}|{"signals":focus[m]["signals"]} for m in focus if m in MANDATORY}},ensure_ascii=False))

if __name__=="__main__": main()
