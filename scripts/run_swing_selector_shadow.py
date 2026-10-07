#!/usr/bin/env python3
"""Run the frozen Human/Swing Selector v1 in SHADOW mode."""
from __future__ import annotations

import gzip
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.common import atomic_json, utc
from research.swing_selector import VERSION, score_market

TREND_PATH=ROOT/"v4_trend_cache.json"
LIVE_PATH=ROOT/"bitvavo_live.json"
NEWS_PATH=ROOT/"production_news_context.json"
STATE_PATH=ROOT/"swing_selector_shadow_state.json"
OUT_PATH=ROOT/"swing_selector_shadow.json"
OUT_MD=ROOT/"swing_selector_shadow.md"

EXCLUDED_BASES={"BTC","ETH","USDT","USDC","EURC","DAI","FDUSD","PYUSD","EURQ","FRAX","USDE","USDG","USDS","GHO","RLUSD","TUSD","USDP","USD1"}
TOP20=20
TOP10=10
MIN_REVIEW_PERSISTENCE_HOURS=3.0
MIN_QUOTE_VOLUME_EUR=15000.0
MAX_SPREAD_PCT=1.0

def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def parse_base(market):
    return market.split("-",1)[0].upper()

def main():
    now=time.time()
    trend_doc=load(TREND_PATH,{})
    trends=trend_doc.get("markets") or {}
    live_doc=load(LIVE_PATH,{})
    live_by={str(x.get("market")):x for x in (live_doc.get("markets") or []) if isinstance(x,dict) and x.get("market")}
    news_doc=load(NEWS_PATH,{})
    news_by=news_doc.get("markets") or {}
    prev=load(STATE_PATH,{"markets":{}})
    if prev.get("version") != VERSION:
        prev={"markets":{}}
    prev_markets=prev.get("markets") or {}

    btc=trends.get("BTC-EUR") or {}
    ranked=[]
    excluded=[]
    for market,trend in trends.items():
        if parse_base(market) in EXCLUDED_BASES:
            continue
        live=live_by.get(market,{})
        news=news_by.get(market,{})
        trend=dict(trend)
        for days in (3,7,14):
            key=f"rs_btc_{days}d"
            if trend.get(key) is None and trend.get(f"ret{days}d") is not None and btc.get(f"ret{days}d") is not None:
                trend[key]=float(trend[f"ret{days}d"])-float(btc[f"ret{days}d"])
        row=score_market(market,trend,live,news)
        row["last_eur"]=trend.get("last")
        qv=live.get("quote_volume_24h_eur")
        spread=live.get("spread_pct")
        liquid=(qv is not None and float(qv)>=MIN_QUOTE_VOLUME_EUR)
        spread_ok=(spread is None or float(spread)<=MAX_SPREAD_PCT)
        row["eligible_universe"]=bool(liquid and spread_ok)
        if not row["eligible_universe"]:
            row["universe_exclusion"]="LOW_LIQUIDITY" if not liquid else "WIDE_SPREAD"
            excluded.append(row)
        else:
            ranked.append(row)

    ranked.sort(key=lambda r:(r["score"],r["technical_score"]),reverse=True)
    top20_markets={r["market"] for r in ranked[:TOP20]}
    top10_markets={r["market"] for r in ranked[:TOP10]}

    state_markets={}
    for idx,row in enumerate(ranked,1):
        market=row["market"]
        old=prev_markets.get(market) or {}
        was_active=bool(old.get("in_top20"))
        first_seen=float(old.get("first_seen_ts") or now) if was_active else now
        streak=int(old.get("consecutive_runs") or 0)+1 if was_active else 1
        in_top20=market in top20_markets
        if not in_top20:
            first_seen=now
            streak=0
        persistence_h=(now-first_seen)/3600.0 if in_top20 else 0.0

        state_markets[market]={
            "in_top20":in_top20,
            "first_seen_ts":first_seen if in_top20 else None,
            "last_seen_ts":now if in_top20 else old.get("last_seen_ts"),
            "consecutive_runs":streak,
            "last_rank":idx,
            "last_score":row["score"],
        }

        row["rank"]=idx
        row["persistence_hours"]=round(persistence_h,3)
        row["consecutive_runs"]=streak

        blocking=set(row.get("flags") or {}) & {"WIDE_SPREAD","HIGH_ATR","CHASE_RISK_24H","FAR_ABOVE_EMA50"}
        if market not in top20_markets:
            row["shadow_status"]="RANKED_ONLY"
        elif persistence_h < MIN_REVIEW_PERSISTENCE_HOURS:
            row["shadow_status"]="PREWATCH_PERSISTENCE_REQUIRED"
        elif market in top10_markets and blocking:
            row["shadow_status"]="WAIT_PULLBACK_OR_NORMALIZATION"
        elif market in top10_markets:
            row["shadow_status"]="HUMAN_REVIEW"
        else:
            row["shadow_status"]="PERSISTENT_TOP20"

        row["human_review_eligible"]=row["shadow_status"]=="HUMAN_REVIEW"

    eth=trends.get("ETH-EUR") or {}
    market_context={
        "btc_ret3d":btc.get("ret3d"),"btc_ret7d":btc.get("ret7d"),"btc_ret14d":btc.get("ret14d"),
        "eth_ret3d":eth.get("ret3d"),"eth_ret7d":eth.get("ret7d"),"eth_ret14d":eth.get("ret14d"),
    }

    payload={
        "schema":"solaire_swing_selector_shadow_v1",
        "version":VERSION,
        "generated_at_utc":utc(),
        "generated_ts":now,
        "mode":"SHADOW_ONLY",
        "no_orders":True,
        "no_alerts":True,
        "no_decision_layer_changes":True,
        "horizon":"24h/48h/72h/7d",
        "policy":{
            "top20_tracking":TOP20,"top10_review":TOP10,
            "min_review_persistence_hours":MIN_REVIEW_PERSISTENCE_HOURS,
            "min_quote_volume_eur_24h":MIN_QUOTE_VOLUME_EUR,
            "max_spread_pct":MAX_SPREAD_PCT,
            "micro_5m_15m_used_for_thesis":False,
            "news_modifier_backtested":False,
        },
        "market_context":market_context,
        "universe_count":len(ranked),
        "excluded_count":len(excluded),
        "top20":ranked[:TOP20],
        "top10":ranked[:TOP10],
        "human_review":[r for r in ranked[:TOP20] if r.get("human_review_eligible")],
        "ranked_summary":[{
            "market":r["market"],"rank":r["rank"],"score":r["score"],
            "technical_score":r["technical_score"],"news_modifier":r["news_modifier"],
            "last_eur":r.get("last_eur"),"shadow_status":r.get("shadow_status"),
            "flags":r.get("flags") or []
        } for r in ranked],
        "notes":[
            "A PREWATCH is not a buy recommendation.",
            "HUMAN_REVIEW requires at least 3h persistence in top20 and top10 rank.",
            "True out-of-sample evaluation starts with this frozen version.",
            "News/catalyst contribution is capped at +/-5 and is not yet historically backtested.",
        ],
    }

    state={
        "schema":"solaire_swing_selector_shadow_state_v1",
        "version":VERSION,
        "updated_at_utc":utc(),
        "updated_ts":now,
        "markets":state_markets,
    }
    atomic_json(str(OUT_PATH.relative_to(ROOT)),payload)
    atomic_json(str(STATE_PATH.relative_to(ROOT)),state)

    lines=[
        "# Solaire Swing Selector — SHADOW",
        "",
        f"Generated: {payload['generated_at_utc']}",
        f"Version: {VERSION}",
        "No orders, no alerts, no Decision Layer changes.",
        "",
        "| Rank | Market | Score | Status | 3d | 7d | 14d | RS BTC 7d | Dist EMA50 | News mod |",
        "|---:|---|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in ranked[:TOP20]:
        i=r["inputs"]
        def f(v):
            try:return f"{float(v):.2f}"
            except:return "—"
        lines.append(
            f"| {r['rank']} | {r['market']} | {r['score']:.2f} | {r['shadow_status']} | "
            f"{f(i.get('ret3d'))}% | {f(i.get('ret7d'))}% | {f(i.get('ret14d'))}% | "
            f"{f(i.get('rs_btc_7d'))}% | {f(i.get('dist_ema50_pct'))}% | {r['news_modifier']:+.2f} |"
        )
    OUT_MD.write_text("\n".join(lines)+"\n",encoding="utf-8")

    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    day=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    hpath=ROOT/"swing_history"/day/f"{stamp}.json.gz"
    hpath.parent.mkdir(parents=True,exist_ok=True)
    hpath.write_bytes(gzip.compress(json.dumps(payload,separators=(",",":"),ensure_ascii=False).encode("utf-8")))

    print(json.dumps({
        "version":VERSION,
        "universe_count":len(ranked),
        "top10":[{"market":r["market"],"score":r["score"],"status":r["shadow_status"]} for r in ranked[:10]],
        "human_review":[r["market"] for r in payload["human_review"]],
        "history_path":str(hpath.relative_to(ROOT)),
    },ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
