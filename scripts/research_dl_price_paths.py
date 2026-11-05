#!/usr/bin/env python3
"""Strict read-only 24/48/72h price-path pilot on frozen V4 CONFIRMED events.

This is a legacy V4 acceleration cohort, NOT direct BUY_SENT, NOT DL trade
fills, NOT an executable comparative PnL. Samples are selected by timestamps
and market identity BEFORE loading any future prices.
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from glob import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.http import PublicClient
from research.production_journal import evaluate_closed_5m_path

FIVE_MS=300000
HORIZONS=(24,48,72)
SCHEMA="solaire_legacy_v4_accel_price_paths_pilot_v1"
MARKET=re.compile(r"^[A-Z0-9]+-EUR$")

def parse_utc(s):
    if not isinstance(s,str):
        raise ValueError("missing UTC scan time")
    d=datetime.fromisoformat(s.replace("Z","+00:00"))
    if d.tzinfo is None or d.utcoffset().total_seconds()!=0:
        raise ValueError("scan time is not UTC")
    return d.timestamp()

def frozen_confirmed(paths):
    """Select earliest recorded confirmed observation per distinct market."""
    best={}
    bad=Counter()
    for p in sorted(paths):
        try:
            with gzip.open(p,"rt",encoding="utf8") as f:
                scan=json.load(f)
            ts=parse_utc(scan["scan_at_utc"])
            if not isinstance(scan.get("observations"),list):
                raise ValueError("missing observations")
            for obs in scan["observations"]:
                if not isinstance(obs,dict) or not isinstance(obs.get("acceleration"),dict):
                    continue
                if obs["acceleration"].get("state")!="CONFIRMED_ACCELERATION":
                    continue
                market=obs.get("market")
                price=obs.get("price_eur")
                if not isinstance(market,str) or not MARKET.fullmatch(market):
                    bad["INVALID_MARKET"]+=1
                    continue
                if isinstance(price,bool) or not isinstance(price,(int,float)) or not math.isfinite(price) or price<=0:
                    bad["INVALID_SCAN_PRICE"]+=1
                    continue
                key=(ts,scan.get("scan_id",""))
                if market not in best or key < best[market]["_key"]:
                    best[market]={
                        "_key":key, "market":market, "scan_at_utc":scan["scan_at_utc"],
                        "scan_ts":ts,"scan_id":scan.get("scan_id"),
                        "scan_price_eur":float(price),
                        "baseline_v4_available":bool(obs.get("baseline")),
                    }
        except (OSError,ValueError,KeyError,TypeError) as exc:
            bad["INVALID_ARCHIVE_"+type(exc).__name__]+=1
    return sorted(best.values(),key=lambda x:(x["scan_ts"],x["market"])),dict(bad)

def select_due(items,asof,max_per_horizon=10):
    if not isinstance(max_per_horizon,int) or isinstance(max_per_horizon,bool) or not 1<=max_per_horizon<=20:
        raise ValueError("max per horizon must be between 1 and 20")
    out=[]
    for hours in HORIZONS:
        due=[e for e in items if e["scan_ts"]+hours*3600+300<=asof]
        # Avoid outcome-driven sampling: earliest times/market alphabetical.
        for e in due[:max_per_horizon]:
            out.append({**e, "hours":hours})
    return out

def bounds(ts,hours,asof):
    if hours not in HORIZONS or ts+hours*3600+300>asof:
        raise ValueError("horizon not fully matured")
    first=((int(ts*1000)//FIVE_MS)+1)*FIVE_MS
    end_ms=int((ts+hours*3600)*1000)
    last=((end_ms-FIVE_MS)//FIVE_MS)*FIVE_MS
    if last<first or last+FIVE_MS>int(asof*1000):
        raise ValueError("unsafe candle cutoff")
    count=(last-first)//FIVE_MS+1
    if count>1440:
        raise ValueError("unsupported candle count")
    return {"start":first,"end":last+FIVE_MS,"limit":1440,"interval":"5m"},count

def inspect_one(item,client,asof):
    record={
        "market":item["market"],"scan_id":item["scan_id"],
        "scan_at_utc":item["scan_at_utc"],"horizon_hours":item["hours"],
        "scan_price_eur":item["scan_price_eur"],
        "price_reference_not_filled":True,
        "real_trades_proven":0,"executable_net_pnl_eur":None,
        "status":"UNKNOWN","mfe_pct":None,"mae_pct":None,"close_pct":None,
        "baseline_v4_available":item["baseline_v4_available"],
    }
    try:
        query,expected=bounds(item["scan_ts"],item["hours"],asof)
        raw=client.get("/"+item["market"]+"/candles",query,cache=False)
        if not isinstance(raw,list):
            raise ValueError("non-array candle response")
        bars=[]
        for bar in raw:
            if not isinstance(bar,list) or len(bar)<6:
                continue
            ms=bar[0]
            if isinstance(ms,(int,float)) and not isinstance(ms,bool) and math.isfinite(ms) and ms%FIVE_MS==0 and query["start"]<=ms<query["end"]:
                bars.append(bar)
        strict=evaluate_closed_5m_path(
            bars,item["scan_ts"],item["scan_price_eur"],item["hours"],
            stop_eur=item.get("stop_eur"), tp1_eur=item.get("tp1_eur"),
            fill_no_trade_gaps=False,
        )
        # Diagnostic only: last-traded-price marks are NOT evidence of fills.
        # Suppress derived indicative returns if more than 20% of bars are absent.
        observed_ratio=len({bar[0] for bar in bars})/expected if expected else 0.0
        sparse=(evaluate_closed_5m_path(
            bars,item["scan_ts"],item["scan_price_eur"],item["hours"],
            stop_eur=item.get("stop_eur"),tp1_eur=item.get("tp1_eur"),
            fill_no_trade_gaps=True,
        ) if bars and observed_ratio>=0.80 else {})
        sparse_ok=sparse.get("status")=="COMPLETE"
        record.update({
            "status":strict["status"],"reason":strict.get("reason"),
            "expected_bars":expected,"observed_bars":len(bars),
            "source_coverage":strict.get("coverage_ratio"),
            "mfe_pct":strict.get("mfe_pct") if strict["status"]=="COMPLETE" else None,
            "mae_pct":strict.get("mae_pct") if strict["status"]=="COMPLETE" else None,
            "close_pct":strict.get("close_return_pct") if strict["status"]=="COMPLETE" else None,
            "future_book_depth_verified":False,
            "path_touch_result":strict.get("result") if strict["status"]=="COMPLETE" else None,
            "indicative_no_trade_gap_reference":sparse_ok,
            "indicative_mark_only_no_fill":True,
            "observed_5m_source_coverage_pct":round(100*observed_ratio,2),
            "indicative_mfe_pct":sparse.get("mfe_pct") if sparse_ok else None,
            "indicative_mae_pct":sparse.get("mae_pct") if sparse_ok else None,
            "indicative_close_pct":sparse.get("close_return_pct") if sparse_ok else None,
            "indicative_stop_before_tp_touch":sparse.get("result") if sparse_ok else None,
        })
    except (ValueError,RuntimeError,KeyError,TypeError,OSError) as exc:
        record.update(status="SOURCE_ERROR",reason=type(exc).__name__)
    return record

def report_for_archive(paths,client,asof,max_per_horizon=10):
    events,invalid=frozen_confirmed(paths)
    due=select_due(events,asof,max_per_horizon)
    rows=[inspect_one(e,client,asof) for e in due]
    summary={}
    for h in HORIZONS:
        subset=[x for x in rows if x["horizon_hours"]==h]
        complete=[x for x in subset if x["status"]=="COMPLETE"]
        summary[str(h)]={
            "eligible_sample":len(subset),"strict_complete":len(complete),
            "incomplete":sum(x["status"]=="INCOMPLETE" for x in subset),
            "source_error":sum(x["status"]=="SOURCE_ERROR" for x in subset),
            "hit_5pct_reference_n":sum(x["mfe_pct"]>=5 for x in complete),
            "hit_10pct_reference_n":sum(x["mfe_pct"]>=10 for x in complete),
            "mae_le_minus5pct_n":sum(x["mae_pct"]<=-5 for x in complete),
            "indicative_80pct_coverage_marks":sum(x.get("indicative_no_trade_gap_reference") is True for x in subset),
            "executed_trades":0, "real_pnl_eur":None,
        }
    return {
        "schema":SCHEMA,"asof_utc":datetime.fromtimestamp(asof,timezone.utc).isoformat(),
        "measurement_only":True,"sample_rule":"FIRST_V4_CONFIRMED_PER_DISTINCT_MARKET_EARLIEST",
        "archived_scans":len(paths),"distinct_confirmed_market_events":len(events),
        "invalid_source_observations":invalid,"max_per_horizon":max_per_horizon,
        "horizons":summary,"samples":rows,
        "modern_direct_buy_sent_compared":False,
        "same_causal_DL_policy_compared":False,
        "executable_pnl_comparable":False,"net_pnl_eur":None,
        "limitations":[
            "These V4 acceleration observations are not DIRECT BUY_SENT opportunities.",
            "Price at archived scan is NOT proof of an executable ask-side entry.",
            "Public last-trade 5m candles do not imply entry, exit, or stop fills.",
            "Strict missing bars mean INCOMPLETE, not zero or interpolate.",
            "Cohort is only a few scans in one date/regime, not independent OOS trades.",
            "24/48/72-hour maturity enforced; future/unavailable horizons excluded.",
        ],
    }

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--history-glob",default="history/2026-10-15/*.json.gz")
    p.add_argument("--output",default="/tmp/dl-frozen-paths.json")
    p.add_argument("--max-per-horizon",type=int,default=10)
    a=p.parse_args(argv)
    try:
        paths=sorted(glob(a.history_glob))
        if not paths:
            raise ValueError("NO_ARCHIVED_SCAN_INPUT")
        now=time.time()
        client=PublicClient(timeout=9,retries=1,requests_per_second=2)
        result=report_for_archive(paths,client,now,a.max_per_horizon)
        Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf8")
        print(json.dumps({k:v for k,v in result.items() if k!="samples"},ensure_ascii=False,sort_keys=True))
        return 0
    except (ValueError,OSError) as exc:
        print("DL_PRICE_PATH_EVIDENCE_ERROR:"+str(exc),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
