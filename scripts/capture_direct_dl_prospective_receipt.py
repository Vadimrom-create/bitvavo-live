#!/usr/bin/env python3
"""Read-only, immutable same-DIRECT-scan feature evidence for DL research.

Never reinterpret the old V4 Decision Layer as computed on DIRECT features.
The V4 'baseline' inputs are absent from the direct pipeline; mark it
NOT_EVALUABLE_ON_THIS_INPUT rather than manufacturing a WATCH/BUY/veto.
No Bitvavo/API access, credentials, account operations or repo mutation.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCHEMA="solaire_direct_input_receipt_v1"
MAX_INPUT_BYTES=16_000_000

def utc_epoch(value):
    if not isinstance(value,str):
        raise ValueError("missing UTC date")
    try:
        t=datetime.fromisoformat(value.replace("Z","+00:00"))
    except ValueError as e:
        raise ValueError("invalid UTC date") from e
    if t.tzinfo is None or t.utcoffset().total_seconds()!=0:
        raise ValueError("date must be explicitly UTC")
    return t.timestamp()

def load_json_and_hash(path):
    p=Path(path)
    raw=p.read_bytes()
    if not raw or len(raw)>MAX_INPUT_BYTES:
        raise ValueError("missing/oversized input "+str(p))
    try:
        obj=json.loads(raw)
    except (ValueError,UnicodeDecodeError) as exc:
        raise ValueError("invalid JSON input "+str(p)) from exc
    if not isinstance(obj,dict):
        raise ValueError("unexpected nonobject JSON "+str(p))
    return obj,hashlib.sha256(raw).hexdigest()

def validate_packet(status,candidates,universe,dl=None,*,asof_ts,revision,hashes,max_age_seconds=900):
    if not isinstance(revision,str) or len(revision)!=40 or not all(c in "0123456789abcdef" for c in revision):
        raise ValueError("source revision must be full Git SHA")
    if status.get("schema")!="solaire_direct_scan_v2":
        raise ValueError("unexpected DIRECT status schema")
    if candidates.get("schema")!="production_alert_candidates_v6_catalyst":
        raise ValueError("unexpected DIRECT candidates schema")
    if universe.get("schema")!="solaire_production_universe_snapshot_v2_news":
        raise ValueError("unexpected DIRECT universe schema")
    scan_utc=status.get("signal_at_utc")
    direct_ts=utc_epoch(scan_utc)
    for obj,field in [(candidates,"generated_at_utc"),(universe,"generated_at_utc")]:
        if obj.get(field)!=scan_utc:
            raise ValueError("DIRECT scan timestamp mismatch: mixed cycles")
    if type(asof_ts) not in (int,float) or not math.isfinite(asof_ts):
        raise ValueError("bad observation time")
    age=asof_ts-direct_ts
    if age<0:
        raise ValueError("future DIRECT scan timestamp")
    for k in ("production_scan_status.json","production_alert_candidates.json","production_universe_snapshot.json"):
        if not isinstance(hashes.get(k),str) or len(hashes[k])!=64:
            raise ValueError("missing hash for "+k)
    rows=universe.get("rows")
    watch=candidates.get("watch")
    if not isinstance(rows,list) or not isinstance(watch,list):
        raise ValueError("missing full-market / candidate rows")
    market_by_name={}
    for row in rows:
        if not isinstance(row,dict) or not isinstance(row.get("market"),str) or not row["market"]:
            raise ValueError("bad market row")
        if row["market"] in market_by_name:
            raise ValueError("duplicate DIRECT market")
        market_by_name[row["market"]]=row
    declared=status.get("universe_snapshot_rows")
    if type(declared) is not int or declared!=len(market_by_name):
        raise ValueError("universe count disagrees with DIRECT scan status")
    if status.get("markets_collected")!=len(market_by_name):
        raise ValueError("universe count disagrees with collected markets")
    if candidates.get("decision_layer_required") is not False:
        raise ValueError("this receipt expects an independent direct gate")
    direct_candidates=[]
    used=set()
    for row in watch:
        if not isinstance(row,dict) or not isinstance(row.get("market"),str):
            raise ValueError("malformed direct candidate")
        market=row["market"]
        if market not in market_by_name or market in used:
            raise ValueError("missing/duplicate candidate market")
        used.add(market)
        source=market_by_name[market]
        # Exact same scan/market: store public direct features, not fabricated V4.
        direct_candidates.append({
            "market":market,
            "direct_action_status":row.get("action_status"),
            "direct_signal_state":row.get("signal_state"),
            "source_last_eur":row.get("last"),
            "same_cycle_market_features":source.get("features"),
            "same_cycle_acceleration":source.get("acceleration"),
            "same_cycle_data_quality":source.get("data_quality"),
            "same_cycle_timestamps":source.get("timestamps"),
            "v4_baseline_present":bool(source.get("baseline")),
            "decision_layer_v1_same_input_status":
                "UNSUPPORTED_NO_V4_BASELINE" if not source.get("baseline") else
                "BASELINE_PRESENT_BUT_UNVALIDATED_INPUT_MODEL",
            "direct_market_feature_sha256":hashlib.sha256(
                json.dumps(source,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
            ).hexdigest(),
            "actual_buy_sent_proven":False,"executed_fill_verified":False,
        })
    dl_timing="NO_DL_ARCHIVE"
    dl_age=None
    if isinstance(dl,dict):
        try:
            t=utc_epoch(dl.get("generated_at_utc"))
            dl_age=round(direct_ts-t,3)
            dl_timing=(
                "DL_GENERATED_AFTER_DIRECT_SCAN" if dl_age<0 else
                "DL_OLDER_THAN_15_MINUTES" if dl_age>900 else
                "DL_PRIOR_GEN_ONLY_DIFFERENT_V4_INPUTS"
            )
        except ValueError:
            dl_timing="DL_INVALID_TIMESTAMP"
    status_result=(
        "REJECTED_STALE_DIRECT_SNAPSHOT" if age>max_age_seconds
        else "CAPTURED_SAME_DIRECT_SCAN"
    )
    return {
        "schema":SCHEMA,
        "research_only":True,
        "receipt_status":status_result,
        "input_git_revision":revision,
        "input_git_blob_sha256":hashes,
        "captured_at_utc":datetime.fromtimestamp(asof_ts,timezone.utc).isoformat(),
        "direct_scan_at_utc":scan_utc,
        "source_age_seconds":round(age,3),
        "active_markets":len(market_by_name),
        "candidate_count":len(direct_candidates),
        "candidate_rows":direct_candidates if status_result=="CAPTURED_SAME_DIRECT_SCAN" else [],
        "prior_dl_status":dl_timing,
        "dl_generated_age_at_direct_scan_seconds":dl_age,
        "full_universe_hash_only":True,
        "no_additional_market_data_requests":True,
        "same_cycle_direct_features_proven":status_result=="CAPTURED_SAME_DIRECT_SCAN",
        "same_input_v4_dl_classification_proven":False,
        "dl_causal_effect_proven":False,
        "real_buy_sent_proven":False,
        "net_portfolio_pnl_eur":None,
        "next_requirement":"Pair with immutable V4 structural features calculated from same underlying scan; never map missing V4 scores to zero/WATCH.",
    }

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-dir",default=".")
    p.add_argument("--output",default="/tmp/direct-dl-prospective-receipt.json.gz")
    p.add_argument("--revision",default=os.getenv("DIRECT_RECEIPT_SOURCE_SHA",""))
    p.add_argument("--asof-epoch",type=float,default=None)
    opt=p.parse_args(argv)
    try:
        root=Path(opt.source_dir)
        names=["production_scan_status.json","production_alert_candidates.json","production_universe_snapshot.json"]
        objs={}
        hashes={}
        for name in names:
            objs[name],hashes[name]=load_json_and_hash(root/name)
        dl=None
        dl_path=root/"decision_layer.json"
        if dl_path.exists():
            dl,hashes["decision_layer.json"]=load_json_and_hash(dl_path)
        receipt=validate_packet(
            objs[names[0]],objs[names[1]],objs[names[2]],dl,
            asof_ts=time.time() if opt.asof_epoch is None else opt.asof_epoch,
            revision=opt.revision,hashes=hashes,
        )
        out=Path(opt.output)
        out.parent.mkdir(parents=True,exist_ok=True)
        with gzip.open(out,"wt",encoding="utf-8") as stream:
            json.dump(receipt,stream,ensure_ascii=False,sort_keys=True,separators=(",",":"))
        print(json.dumps({k:v for k,v in receipt.items() if k!="candidate_rows"},sort_keys=True))
        return 0
    except (ValueError,OSError,TypeError) as exc:
        print("DIRECT_PROSPECTIVE_RECEIPT_FAILED_CLOSED:"+str(exc),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
