#!/usr/bin/env python3
"""Prospective, research-only exit-time order-book observation of PRECOMMITTED signal-age targets.

No live orders, wallet keys, user holdings, thresholds, or production mutations.
One invocation checks ONLY targets due within 120 seconds; running this script
after the fact cannot reconstruct past quotes. Signal age != held trade exit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from research.capital_constrained_replay import utc
from research.execution_observability import book_evidence, walk
from research.http import PublicClient

SCHEMA="solaire_prospective_exit_book_targets_v1"
RESULT_SCHEMA="solaire_prospective_exit_book_capture_v1"
MAX_EXIT_LAG_SECONDS=120
MAX_FETCHES_PER_RUN=8


def checksum_bytes(data):
    return hashlib.sha256(data).hexdigest()


def validate_commitment(commitment):
    if not isinstance(commitment, dict) or commitment.get("schema") != SCHEMA:
        raise ValueError("precommitted target schema required")
    frozen=utc(commitment.get("committed_before_due_utc"),"commit time")
    targets=commitment.get("targets")
    if not isinstance(targets,list):
        raise ValueError("no precommitted targets list")
    if commitment.get("target_count") != len(targets):
        raise ValueError("target count mismatch")
    seen=set()
    markets=set()
    for t in targets:
        if not isinstance(t,dict):
            raise ValueError("invalid committed target object")
        ident=t.get("target_id")
        if not isinstance(ident,str) or not ident or ident in seen:
            raise ValueError("duplicate or absent target ID")
        seen.add(ident)
        market=t.get("market")
        if not isinstance(market,str) or not market.endswith("-EUR"):
            raise ValueError("invalid market")
        markets.add(market)
        due=utc(t.get("due_at_utc"),"due")
        decision=utc(t.get("signal_decision_at_utc"),"decision")
        horizon=t.get("horizon_hours")
        if horizon not in (4,12,24) or bool(t.get("execution_stage") != "SIGNAL_AGE_ONLY_NOT_PROVEN_FILLED"):
            raise ValueError("target is not declared shadow signal-age horizon")
        if abs((due-decision).total_seconds()-horizon*3600)>0.01:
            raise ValueError("exit horizon not reconstructible from original decision")
        if due<=frozen:
            raise ValueError("target was not committed before due")
        if t.get("stake_scenarios_eur") != [100,150]:
            raise ValueError("unexpected stake scenarios")
    if commitment.get("unique_market_count") != len(markets):
        raise ValueError("unique market count mismatch")
    if commitment.get("real_trade_entry_or_exit_proven") is not False:
        raise ValueError("source cannot claim real fills")


def quote_sale(book_ev, euros):
    """Hypothetical sale of base units representing EUR nominal at best bid.

    Not a matching historic trade, not a trade-fill quote guarantee. Assume
    the user would own EUR/best_bid units solely for liquidity estimation.
    """
    if book_ev.get("book_valid") is not True:
        return {"status":"UNAVAILABLE_BOOK","quote_eur_est":None,"vwap_bid_eur_est":None}
    bids=book_ev["raw_book"].get("bids")
    best=book_ev["best_bid_eur"]
    if not bids or not best or best<=0:
        return {"status":"UNAVAILABLE_BID","quote_eur_est":None,"vwap_bid_eur_est":None}
    levels=[(float(p),float(q)) for p,q in bids]
    units=euros/best
    fill=walk(levels,units,False)
    if not fill["covered"]:
        return {"status":"INSUFFICIENT_VISIBLE_BID_DEPTH","nominal_eur":euros,
                "base_quantity_est":units,"quote_eur_est":None,
                "vwap_bid_eur_est":None,"visible_depth_scope":"TOP_1000_REPORTED_LEVELS"}
    proceeds=fill["quote_eur"]
    fee=proceeds*.0025
    slippage=proceeds*.001
    return {"status":"VISIBLE_BOOK_COVERS_HYPOTHETICAL_SALE",
            "nominal_eur":euros,"base_quantity_est":units,
            "quote_eur_est":round(proceeds,8),"vwap_bid_eur_est":round(fill["vwap_eur"],12),
            "bid_impact_pct_est":round((1-fill["vwap_eur"]/best)*100,7),
            "sell_fee_0_25pct_eur_est":round(fee,8),
            "adverse_extra_slippage_0_1pct_eur_est":round(slippage,8),
            "net_proceeds_after_assumptions_eur_est":round(proceeds-fee-slippage,8),
            "visible_depth_scope":"TOP_1000_REPORTED_LEVELS",
            "orders_submitted":False,"real_exit_fill_proven":False}


def collect_once(commitment, *, client, clock=time.time, max_lag_seconds=MAX_EXIT_LAG_SECONDS):
    """Process due targets. Status for missed/early is UNKNOWN, never 0 PnL."""
    validate_commitment(commitment)
    if not isinstance(max_lag_seconds,(float,int)) or not 0<max_lag_seconds<=120:
        raise ValueError("max capture lag must be >0 and <=120 seconds")
    first_now=clock()
    frozen=utc(commitment["committed_before_due_utc"],"precommit time")
    if first_now<=frozen.timestamp():
        raise ValueError("capture time before precommit timestamp")
    ordered=sorted(commitment["targets"],key=lambda x:(x["due_at_utc"],x["target_id"]))
    due_ids=[t["target_id"] for t in ordered
             if 0<=first_now-utc(t["due_at_utc"],"due").timestamp()<=max_lag_seconds]
    actual_checked=0
    rows=[]
    for target in ordered:
        due=utc(target["due_at_utc"],"due")
        lag_before=first_now-due.timestamp()
        base={
            "target_id":target["target_id"],
            "source_decision_id":target["source_decision_id"],
            "market":target["market"],
            "horizon_hours":target["horizon_hours"],
            "due_at_utc":target["due_at_utc"],
            "precommitted_before_due":True,
            "trade_entry_status":"NOT_PROVEN",
            "trade_exit_status":"NOT_PROVEN",
            "actual_wallet_pnl_eur":None,
            "orders_submitted":False,
            "visible_bid_sale_100_eur_est":None,
            "visible_bid_sale_150_eur_est":None,
        }
        if lag_before<0:
            rows.append({**base,"status":"NOT_YET_DUE","reason":"NO_HISTORIC_QUOTE_INFERRED"})
            continue
        if lag_before>max_lag_seconds:
            rows.append({**base,"status":"MISSED_CAPTURE_WINDOW","reason":"HISTORIC_BOOK_CANNOT_BE_RECONSTRUCTED"})
            continue
        if actual_checked>=MAX_FETCHES_PER_RUN:
            rows.append({**base,"status":"CAPACITY_NOT_CAPTURED","reason":"BOUNDED_RESEARCH_JOB"})
            continue
        actual_checked+=1
        # The wall clock is checked after the request too: never relabel a
        # late capture as though it were available at the exact exit time.
        try:
            book=client.get("/"+target["market"]+"/book",{"depth":1000},cache=False)
            meta=client.metadata("/"+target["market"]+"/book",{"depth":1000})
            finished=clock()
            evidence=book_evidence(book,meta,finished)
            lag=finished-due.timestamp()
            fingerprint=checksum_bytes(json.dumps(book,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8"))
            status=("BOOK_CAPTURED_WITHIN_WINDOW" if
                    evidence["book_valid"] and evidence.get("freshness_status")=="FRESH" and
                    0<=lag<=max_lag_seconds else "UNVERIFIED_OR_LATE_BOOK")
            result={**base,"status":status,
                "request_started_at_utc":meta.get("request_started_at_utc"),
                "response_received_at_utc":meta.get("retrieved_at_utc"),
                "available_at_utc":datetime.fromtimestamp(finished,timezone.utc).isoformat(),
                "seconds_after_due_at_availability":round(lag,4),
                "freshness_status":evidence.get("freshness_status"),
                "raw_public_order_book":book,"raw_public_book_sha256":fingerprint,
                "observed_best_bid_eur":evidence.get("best_bid_eur"),
                "observed_best_ask_eur":evidence.get("best_ask_eur"),
                "observed_spread_pct":round(evidence["spread"]*100,7) if evidence.get("spread") is not None else None,
                "observable_book_valid":evidence["book_valid"],
                "visible_bid_sale_100_eur_est":quote_sale(evidence,100),
                "visible_bid_sale_150_eur_est":quote_sale(evidence,150),
                "quote_provenance":"AT_AVAILABLE_AT_NOT_DUE_AT" if lag else "AT_DUE_AT",
                "price_at_original_signal_exit":None,
                "real_exit_fill_proven":False}
            rows.append(result)
        except Exception as exc:
            rows.append({**base,"status":"PUBLIC_BOOK_UNAVAILABLE",
                         "error_type":type(exc).__name__,"reason":"NOT_A_FAILED_TRADE"})
    statuses={}
    for t in rows:
        statuses[t["status"]]=statuses.get(t["status"],0)+1
    return {
        "schema":RESULT_SCHEMA,"research_only":True,
        "capture_started_at_utc":datetime.fromtimestamp(first_now,timezone.utc).isoformat(),
        "precommit_at_utc":commitment["committed_before_due_utc"],
        "target_count":len(rows),
        "due_within_capture_window_count":len(due_ids),
        "attempted_public_books":actual_checked,
        "status_counts":statuses,
        "rows":rows,
        "actual_wallet_pnl_eur":None,"real_exit_fills_verified":0,
        "any_order_submitted":False,
        "source_policy":"MACHINE_BUY_SENT_NOT_V4_OR_R2",
        "important":(
            "At most two minutes after precommitted SIGNAL-AGE time. Not a confirmed held "
            "position or the true order exit. Best bid and VWAP reflect only the public "
            "book at request completion, not a guaranteed historical/future fill."
        ),
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--precommit",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    raw=Path(args.precommit).read_bytes()
    o=json.loads(raw)
    result=collect_once(o,client=PublicClient(timeout=10,retries=2,requests_per_second=3))
    result["source_precommit_sha256"]=checksum_bytes(raw)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("PRECOMMITTED_EXIT_BOOK_PROBE",json.dumps({
        "precommit":result["precommit_at_utc"],
        "targets":result["target_count"],
        "within_window":result["due_within_capture_window_count"],
        "attempted":result["attempted_public_books"],
        "statuses":result["status_counts"],
        "real_exit_fills_verified":0,
        "any_order_submitted":False,
    },sort_keys=True))
    if not result["due_within_capture_window_count"]:
        print("NO_DUE_SHADOW_TARGETS_IN_THIS_ONE_OFF_RUN; NOT AN AUTOMATIC MONITOR")
if __name__=="__main__":
    main()
