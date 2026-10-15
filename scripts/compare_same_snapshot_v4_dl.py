#!/usr/bin/env python3
"""Compare archived V4 acceleration evidence and DL on the SAME frozen scan.

Research only. The acceleration feature in a V4 archive is NOT the modern
independent Solaire-direct production BUY gate; never label proxy as DIRECT.
No external API calls, order, account access or production mutation.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.decision_layer import classify

SCHEMA = "legacy_same_snapshot_v4_accel_dl_v1"
ACCEL_STATES = {"BUILDING_ACCELERATION", "CONFIRMED_ACCELERATION"}

class SnapshotError(ValueError):
    pass

def inspect_scan(scan, *, source, source_sha256, frozen_dl=None):
    if not isinstance(scan,dict) or not isinstance(scan.get("observations"),list):
        raise SnapshotError("missing immutable observations")
    sid=scan.get("scan_id")
    sat=scan.get("scan_at_utc")
    if not isinstance(sid,str) or not sid or not isinstance(sat,str) or not sat:
        raise SnapshotError("missing scan identity or scan time")
    seen=set()
    counts=Counter()
    cross=Counter()
    exceptions=[]
    dl_lookup={}
    if frozen_dl is not None:
        if frozen_dl.get("scan_id") != sid:
            raise SnapshotError("decision archive and scan have different scan_ids")
        ranked=frozen_dl.get("ranked")
        if not isinstance(ranked,list):
            raise SnapshotError("decision archive missing ranked")
        for row in ranked:
            m=row.get("market") if isinstance(row,dict) else None
            if not isinstance(m,str) or m in dl_lookup:
                raise SnapshotError("duplicate/malformed DL market")
            dl_lookup[m]=row.get("action")
    for obs in scan["observations"]:
        if not isinstance(obs,dict) or not isinstance(obs.get("market"),str):
            raise SnapshotError("malformed V4 observation")
        market=obs["market"]
        if market in seen:
            raise SnapshotError("duplicate market in scan")
        seen.add(market)
        if not (obs.get("data_quality") or {}).get("ok",False):
            counts["data_quality_not_ok"]+=1
        accel=obs.get("acceleration")
        state=accel.get("state") if isinstance(accel,dict) else None
        if state is None:
            state="ACCELERATION_NOT_RECORDED"
            counts["acceleration_state_unknown"]+=1
        base=obs.get("baseline")
        baseline_present=isinstance(base,dict) and bool(base)
        if not baseline_present:
            counts["baseline_features_unknown"]+=1
        dl_action=classify(obs)["action"] if baseline_present else "DL_UNCLASSIFIABLE_NO_BASELINE"
        counts["observations"]+=1
        counts["acceleration_"+state]+=1
        counts["dl_"+dl_action]+=1
        if state in ACCEL_STATES:
            counts["acceleration_building_or_confirmed"]+=1
        cross[(state,dl_action)]+=1
        if frozen_dl is not None:
            if market not in dl_lookup:
                counts["missing_frozen_dl_market"]+=1
            elif dl_action!=dl_lookup[market]:
                counts["frozen_dl_action_mismatch"]+=1
                if len(exceptions)<15:
                    exceptions.append({"market":market,"recomputed":dl_action,"original":dl_lookup[market]})
            else:
                counts["frozen_dl_action_matched"]+=1
        if state == "CONFIRMED_ACCELERATION":
            if dl_action=="ACHETE_MAINTENANT":
                counts["confirmed_and_immediate"]+=1
            elif dl_action not in ("DL_UNCLASSIFIABLE_NO_BASELINE",):
                counts["confirmed_not_immediate"]+=1
    return {
        "scan_id":sid,"scan_at_utc":sat,"source":source,"source_sha256":source_sha256,
        "total_markets":len(seen),"counts":dict(sorted(counts.items())),
        "acceleration_dl_cross":[{"legacy_acceleration":state,"dl_action":action,"n":n}
                                 for (state,action),n in sorted(cross.items())],
        "frozen_dl_archive_present":frozen_dl is not None,
        "dl_policy_replay_matches_archived":(
            None if frozen_dl is None else
            counts["missing_frozen_dl_market"] == 0 and counts["frozen_dl_action_mismatch"] == 0
            and len(dl_lookup)==len(seen)),
        "policy_mismatches_sample":exceptions,
        "actual_direct_production_gate_compared":False,
        "same_inputs_as_direct_production":False,
        "real_executable_pnl_eur":None,
    }

def inspect_file(path, decision_dir):
    raw=path.read_bytes()
    try:
        scan=json.loads(gzip.decompress(raw))
    except (OSError,ValueError) as e:
        raise SnapshotError("unreadable scan gzip") from e
    sid=scan.get("scan_id","") if isinstance(scan,dict) else ""
    expected=Path(decision_dir)/str(scan.get("scan_at_utc",""))[:10]/(sid+".json.gz")
    frozen=None
    if expected.is_file():
        try:
            frozen=json.loads(gzip.decompress(expected.read_bytes()))
        except (OSError,ValueError) as e:
            raise SnapshotError("unreadable archived decision") from e
    return inspect_scan(scan,source=str(path),source_sha256=hashlib.sha256(raw).hexdigest(),frozen_dl=frozen)

def run(paths, decision_dir):
    if not paths:
        raise SnapshotError("no frozen scans supplied")
    reports=[inspect_file(Path(p),decision_dir) for p in paths]
    count=Counter()
    table=Counter()
    for report in reports:
        count.update(report["counts"])
        for cell in report["acceleration_dl_cross"]:
            table[(cell["legacy_acceleration"],cell["dl_action"])]+=cell["n"]
    return {
        "schema":SCHEMA,
        "measurement_only":True,
        "snapshots":len(reports),
        "total_observations":count["observations"],
        "frozen_dl_replay_mismatches":count["frozen_dl_action_mismatch"],
        "missing_dl_archives":sum(not x["frozen_dl_archive_present"] for x in reports),
        "total_confirmed_acceleration":count["acceleration_CONFIRMED_ACCELERATION"],
        "confirmed_also_dl_immediate":count["confirmed_and_immediate"],
        "confirmed_dl_not_immediate":count["confirmed_not_immediate"],
        "unclassifiable_confirmed":count["acceleration_CONFIRMED_ACCELERATION"]-count["confirmed_and_immediate"]-count["confirmed_not_immediate"],
        "cross_tab":[{"legacy_acceleration":s,"dl_action":a,"n":n}
                     for (s,a),n in sorted(table.items())],
        "snapshot_reports":reports,
        "direct_production_gate_compared":False,
        "economic_profit_comparable":False,
        "real_fills_verified":0,"net_pnl_eur":None,
        "limitations":[
            "V4 acceleration is a legacy feature, not an independent modern direct production BUY.",
            "Same-scan classification does not establish trade fills, forward paths or net returns.",
            "Recorded DL may be generated after source scan; replay is descriptive, not proof of delivery-time decision.",
            "Missing base profiles remain DL_UNCLASSIFIABLE, not WATCH or structural veto.",
        ],
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--history-glob",default="history/2026-10-15/*.json.gz")
    p.add_argument("--decision-history",default="decision_history")
    p.add_argument("--output",help="local research-only JSON report")
    args=p.parse_args()
    from glob import glob
    try:
        result=run(sorted(glob(args.history_glob)),args.decision_history)
        body=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
        if args.output:
            Path(args.output).write_text(body,encoding="utf-8")
        print(json.dumps({k:v for k,v in result.items() if k not in ("snapshot_reports","cross_tab")},ensure_ascii=False,sort_keys=True,indent=2))
        print(json.dumps({"cross_tab":result["cross_tab"]},ensure_ascii=False))
        return 0
    except (OSError,ValueError,SnapshotError) as e:
        p.exit(2,"FROZEN_SHADOW_COMPARISON_FAILED: "+str(e)+"\n")

if __name__=="__main__":
    raise SystemExit(main())
