#!/usr/bin/env python3
"""Adversarial replay of Solaire's 15m confirmation balance.

The current CONFIRMED_ACCELERATION label can be reached even when the
confirmation_15m component is zero, because evidence can come entirely from
5m momentum/acceleration, volume and breakout pressure. This audit replays the
full Bitvavo EUR universe and sweeps small minimum floors on confirmation_15m
for both current-confirmed and HQ-BUILDING-style thresholds.

Research-only; no production decisions are changed.
"""
from __future__ import annotations
import json, math, statistics, sys, time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from research.common import atomic_json, finite, utc
from research.features import closed_candles, describe
from research.http import PublicClient
from research.production_acceleration import acceleration_signal

OUT="research/solaire_confirmation_balance_20260921.json"
START_UTC="2026-09-21T08:00:00+00:00"
END_UTC="2026-09-21T21:05:00+00:00"
FOCUS={"FET-EUR","WIF-EUR","AIOZ-EUR","PHA-EUR","ICX-EUR","XVG-EUR","SAGA-EUR","EPIC-EUR"}
C15_FLOORS=(0.0,0.5,1.0,1.5,2.0,3.0)
LIQ_PROXY=75_000.0

def to_ts(s):
    return datetime.fromisoformat(s.replace("Z","+00:00")).timestamp()

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def raw_rows(raw):
    out=[]
    for x in raw:
        if not isinstance(x,list) or len(x)<6: continue
        vals=[finite(v) for v in x[:6]]
        if any(v is None for v in vals): continue
        t,o,h,l,c,v=vals
        out.append((int(t),o,h,l,c,v))
    return sorted(out)

def price_before(rows,t):
    xs=[x for x in rows if x[0]+300_000<=t*1000+1]
    return xs[-1][4] if xs else None

def turnover_proxy(rows,t,hours):
    start=(t-hours*3600)*1000
    end=t*1000
    xs=[x for x in rows if start<=x[0]+300_000<=end+1]
    return sum(x[4]*x[5] for x in xs)

def forward(rows,t0,base,hours=4):
    if not base or base<=0: return None
    first=((int(t0*1000)//300_000)+1)*300_000
    end=int((t0+hours*3600)*1000)
    xs=[x for x in rows if first<=x[0]<end]
    if not xs: return None
    complete=xs[-1][0]>=end-600_000
    return {
        "mfe_pct":round((max(x[2] for x in xs)/base-1)*100,4),
        "mae_pct":round((min(x[3] for x in xs)/base-1)*100,4),
        "close_pct":round((xs[-1][4]/base-1)*100,4),
        "bars":len(xs),"complete":complete,
    }

def match_policy(acc,kind,floor):
    score=finite(acc.get("score")); ev=int(acc.get("evidence_count") or 0)
    c15=finite((acc.get("components") or {}).get("confirmation_15m"),0.0)
    if score is None or c15<floor: return False
    if kind=="confirmed": return score>=6.5 and ev>=3
    if kind=="hq": return score>=6.0 and ev>=4
    raise ValueError(kind)

def stats(events):
    xs=[e for e in events if (e.get("forward_4h") or {}).get("complete")]
    f=[e["forward_4h"] for e in xs]
    return {
        "n":len(xs),
        "mfe_ge_5pct":sum(x["mfe_pct"]>=5 for x in f),
        "clean_mfe_ge5_mae_gt_minus5":sum(x["mfe_pct"]>=5 and x["mae_pct"]>-5 for x in f),
        "mae_le_minus5pct":sum(x["mae_pct"]<=-5 for x in f),
        "median_mfe_pct":med([x["mfe_pct"] for x in f]),
        "median_mae_pct":med([x["mae_pct"] for x in f]),
        "median_close_pct":med([x["close_pct"] for x in f]),
        "median_confirmation_15m":med([e["components"]["confirmation_15m"] for e in xs]),
        "median_quote_turnover_24h_proxy_eur":med([e["quote_turnover_24h_proxy_eur"] for e in xs]),
    }

def main():
    start=to_ts(START_UTC); end=to_ts(END_UTC); now=time.time()
    policies={}
    for kind in ("confirmed","hq"):
        for floor in C15_FLOORS:
            policies[f"{kind}_c15_{str(floor).replace('.','_')}"]={"kind":kind,"c15_floor":floor}

    client=PublicClient(timeout=12,retries=3,requests_per_second=10)
    client.get("/time",cache=False)
    markets=[m for m in client.get("/markets") if m.get("quote")=="EUR" and m.get("status")=="trading"]
    results={name:[] for name in policies}
    focus={}; errors=[]

    for meta in sorted(markets,key=lambda x:x["market"]):
        market=meta["market"]
        try:
            raw5=client.get("/"+market+"/candles",{"interval":"5m","limit":400},cache=False)
            raw15=client.get("/"+market+"/candles",{"interval":"15m","limit":200},cache=False)
            rows5=raw_rows(raw5)
            firsts={name:None for name in policies}
            t=math.ceil(start/300)*300
            while t<=min(end,now):
                c5=closed_candles(raw5,"5m",t)
                c15=closed_candles(raw15,"15m",t)
                f5=describe(c5,"5m"); f15=describe(c15,"15m")
                if f5.get("valid") and f15.get("valid"):
                    acc=acceleration_signal({"features":{"5m":f5,"15m":f15}})
                    px=finite(f5.get("last_close_eur"))
                    if px and px>0:
                        for name,p in policies.items():
                            if firsts[name] is None and match_policy(acc,p["kind"],p["c15_floor"]):
                                ev={
                                    "market":market,"at_utc":utc(t),"ts":t,"price_eur":px,
                                    "score":finite(acc.get("score")),
                                    "evidence_count":int(acc.get("evidence_count") or 0),
                                    "components":acc.get("components") or {},
                                    "quote_turnover_1h_proxy_eur":round(turnover_proxy(rows5,t,1),2),
                                    "quote_turnover_24h_proxy_eur":round(turnover_proxy(rows5,t,24),2),
                                    "forward_4h":forward(rows5,t,px,4),
                                }
                                firsts[name]=ev
                                results[name].append(ev)
                if all(v is not None for v in firsts.values()): break
                t+=300
            if market in FOCUS:
                focus[market]=firsts
        except Exception as exc:
            errors.append({"market":market,"reason":type(exc).__name__+":"+str(exc)})

    summary={}
    for name,events in results.items():
        complete=[e for e in events if (e.get("forward_4h") or {}).get("complete")]
        liquid=[e for e in complete if e.get("quote_turnover_24h_proxy_eur",0)>=LIQ_PROXY]
        summary[name]={"all":stats(complete),"liquid_proxy_ge75k":stats(liquid)}

    current={e["market"]:e for e in results["confirmed_c15_0_0"]
             if (e.get("forward_4h") or {}).get("complete")}
    paired={}
    for name,events in results.items():
        if name=="confirmed_c15_0_0": continue
        rows=[]
        for e in events:
            c=current.get(e["market"])
            if not c or not (e.get("forward_4h") or {}).get("complete"): continue
            if e.get("quote_turnover_24h_proxy_eur",0)<LIQ_PROXY or c.get("quote_turnover_24h_proxy_eur",0)<LIQ_PROXY:
                continue
            rows.append({
                "market":e["market"],
                "delay_vs_current_min":round((e["ts"]-c["ts"])/60,2),
                "price_change_vs_current_pct":round((e["price_eur"]/c["price_eur"]-1)*100,4),
                "candidate_mfe":e["forward_4h"]["mfe_pct"],"current_mfe":c["forward_4h"]["mfe_pct"],
                "candidate_mae":e["forward_4h"]["mae_pct"],"current_mae":c["forward_4h"]["mae_pct"],
                "candidate_close":e["forward_4h"]["close_pct"],"current_close":c["forward_4h"]["close_pct"],
            })
        paired[name]={
            "n":len(rows),
            "median_delay_vs_current_min":med([r["delay_vs_current_min"] for r in rows]),
            "median_price_change_vs_current_pct":med([r["price_change_vs_current_pct"] for r in rows]),
            "median_mfe_delta_pp":med([r["candidate_mfe"]-r["current_mfe"] for r in rows]),
            "median_mae_delta_pp":med([r["candidate_mae"]-r["current_mae"] for r in rows]),
            "median_close_delta_pp":med([r["candidate_close"]-r["current_close"] for r in rows]),
        }

    # Explicitly isolate current CONFIRMED signals whose 15m component is tiny.
    cur_complete=[e for e in results["confirmed_c15_0_0"] if (e.get("forward_4h") or {}).get("complete")]
    weak15=[e for e in cur_complete if finite(e["components"].get("confirmation_15m"),0)<1.0]
    strong15=[e for e in cur_complete if finite(e["components"].get("confirmation_15m"),0)>=1.0]

    out={
        "schema":"solaire_confirmation_balance_audit_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "session":{"start_utc":START_UTC,"end_utc":END_UTC},
        "liquidity_proxy_note":"historical 5m base volume multiplied by candle close; used only for cohort screening",
        "policies":policies,
        "summary_4h":summary,
        "paired_vs_current_confirmed":paired,
        "current_confirmed_confirmation15_split":{
            "lt_1":stats(weak15),
            "ge_1":stats(strong15),
        },
        "focus_markets":focus,
        "errors":errors,
    }
    atomic_json(OUT,out)
    print("SOLAIRE_CONFIRMATION_BALANCE "+json.dumps({
        "current":summary["confirmed_c15_0_0"]["liquid_proxy_ge75k"],
        "confirmed_c15_1":summary["confirmed_c15_1_0"]["liquid_proxy_ge75k"],
        "hq_c15_1":summary["hq_c15_1_0"]["liquid_proxy_ge75k"],
        "current_split":out["current_confirmed_confirmation15_split"],
        "focus":focus,
    },ensure_ascii=False))

if __name__=="__main__": main()
