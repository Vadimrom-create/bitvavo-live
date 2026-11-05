#!/usr/bin/env python3
"""Research-only Git commit time audit for already joined DIRECT/DL matches.

IMPORTANT: Git commit committer dates are NOT proof of remote availability.
Git publication and signal delivery remain unverified, especially at sub-minute
margins. This strictly reports a timing consistency check, never an A/B benefit.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCHEMA="solaire_dl_git_commit_asof_v1"
SOURCE_PATH = re.compile(r"^decision_history/\d{4}-\d{2}-\d{2}/\d{8}T\d{6}Z-[a-f0-9]{8}\.json\.gz$")
REPO="Vadimrom-create/bitvavo-live"

def utc_epoch(value):
    if not isinstance(value,str):
        raise ValueError("missing commit UTC timestamp")
    dt=datetime.fromisoformat(value.replace("Z","+00:00"))
    if dt.tzinfo is None or dt.utcoffset().total_seconds()!=0:
        raise ValueError("untrusted timezone in commit date")
    return dt.timestamp()

def choose_source_paths(joined, max_age_seconds=900):
    if joined.get("schema")!="solaire_dl_asof_comparator_v1":
        raise ValueError("invalid asof report schema")
    raw=joined.get("rows")
    if not isinstance(raw,list):
        raise ValueError("missing asof rows")
    relevant=[]
    unique=set()
    for row in raw:
        if not isinstance(row,dict):
            raise ValueError("malformed asof row")
        if row.get("machine_action")!="BUY_SENT" or row.get("join_status")!="ASOF_MATCH":
            continue
        age=row.get("shadow_age_seconds")
        path=row.get("shadow_source")
        ts=row.get("machine_ts")
        if isinstance(age,bool) or not isinstance(age,(int,float)) or not math.isfinite(age) or age<0 or age>max_age_seconds:
            continue
        if not isinstance(path,str) or not SOURCE_PATH.fullmatch(path):
            raise ValueError("invalid history file path")
        if isinstance(ts,bool) or not isinstance(ts,(int,float)) or not math.isfinite(ts) or ts<=0:
            raise ValueError("invalid machine timestamp")
        relevant.append({
            "market":row.get("market"),"decision_id":row.get("decision_id"),
            "machine_ts":float(ts),"shadow_source":path,
            "shadow_age_generated_s":round(float(age),3),
        })
        unique.add(path)
    return sorted(relevant,key=lambda z:(z["machine_ts"],z["decision_id"] or "")),sorted(unique)

def github_commits_lookup(path,token=None):
    if not SOURCE_PATH.fullmatch(path):
        raise ValueError("invalid Git history path")
    url="https://api.github.com/repos/"+REPO+"/commits?"+urllib.parse.urlencode(
        {"path":path,"per_page":2}
    )
    headers={
        "Accept":"application/vnd.github+json","User-Agent":"solaire-dl-publication-audit/1",
        "X-GitHub-Api-Version":"2022-11-28",
    }
    if token:
        headers["Authorization"]="Bearer "+token
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=12) as response:
        if response.status!=200:
            raise ValueError("unexpected GitHub status")
        data=json.loads(response.read(120000))
    if not isinstance(data,list) or not data:
        return {"status":"NO_COMMIT_FOUND"}
    if len(data)!=1:
        return {"status":"AMBIGUOUS_MULTIPLE_COMMITS"}
    row=data[0]
    raw_date=((row.get("commit") or {}).get("committer") or {}).get("date")
    if not isinstance(raw_date,str):
        return {"status":"COMMIT_DATE_MISSING"}
    ts=utc_epoch(raw_date)
    return {
        "status":"ONE_COMMIT_DATE_FOUND","commit_ts":ts,
        "commit_date_utc":raw_date,"commit_sha":row.get("sha"),
    }

def analyze(joined, resolver, max_age_seconds=900):
    events,paths=choose_source_paths(joined,max_age_seconds)
    commits={}
    for path in paths:
        try:
            result=resolver(path)
            if not isinstance(result,dict):
                raise ValueError("non-dictionary resolver result")
            status=result.get("status")
            if status=="ONE_COMMIT_DATE_FOUND":
                commit_ts=result.get("commit_ts")
                if isinstance(commit_ts,bool) or not isinstance(commit_ts,(int,float)) or not math.isfinite(commit_ts):
                    raise ValueError("missing numeric commit timestamp")
                commits[path]={
                    "status":status,"commit_ts":float(commit_ts),
                    "commit_date_utc":result.get("commit_date_utc"),
                    "commit_sha":result.get("commit_sha"),
                }
            else:
                commits[path]={"status":status or "UNKNOWN_LOOKUP"}
        except (ValueError,urllib.error.URLError,OSError,KeyError,TypeError) as exc:
            commits[path]={"status":"LOOKUP_ERROR_"+type(exc).__name__}
    observations=[]
    for row in events:
        commit=commits[row["shadow_source"]]
        margin=None
        status="UNKNOWN_COMMIT_TIME"
        if commit["status"]=="ONE_COMMIT_DATE_FOUND":
            margin=round(row["machine_ts"]-commit["commit_ts"],3)
            if margin<0:
                status="COMMIT_DATE_AFTER_SIGNAL"
            elif margin<30:
                status="COMMIT_DATE_PRIOR_LT30S_LOW_CONFIDENCE"
            elif margin<=max_age_seconds:
                status="COMMIT_DATE_PRIOR_WITHIN_WINDOW"
            else:
                status="COMMIT_DATE_PRIOR_BUT_OLDER_THAN_WINDOW"
        observations.append({**row,
            "publication_metadata_status":status,
            "git_commit_ts":commit.get("commit_ts"),
            "git_commit_sha":commit.get("commit_sha"),
            "commit_date_vs_machine_seconds":margin,
            "remote_published_at_signal_verified":False,
        })
    return {
        "schema":SCHEMA,"research_only":True,
        "source":"public GitHub commit metadata via path-scoped repository API",
        "n_matching_machine_buys":len(events),
        "n_unique_shadow_paths":len(paths),
        "git_commit_lookup_statuses":dict(Counter(x["status"] for x in commits.values())),
        "event_commit_timing_statuses":dict(Counter(x["publication_metadata_status"] for x in observations)),
        "rows":observations,
        "actual_public_visibility_at_signal_verified":False,
        "economic_effect_identified":False,
        "real_trade_fills_verified":0,
        "net_pnl_eur":None,
        "limitations":[
            "Git committer timestamps are metadata, not GitHub server receipt/visibility timestamps.",
            "Sub-30-second gaps cannot establish the DL was available to sender/user.",
            "Only events already joined by prior generated time are checked.",
            "No evidence of a same-input DL counterfactual or executable order.",
            "Unresolved GitHub lookups remain UNKNOWN and are not interpreted as vetoes.",
        ],
    }

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--asof-json",default="/tmp/dl-asof-evidence.json")
    p.add_argument("--output",default="/tmp/dl-commit-asof-evidence.json")
    p.add_argument("--max-age-seconds",type=int,default=900)
    a=p.parse_args(argv)
    if not 0<a.max_age_seconds<=3600:
        p.error("age seconds must be 1..3600")
    try:
        raw=json.loads(Path(a.asof_json).read_text(encoding="utf-8"))
        token=os.environ.get("GITHUB_TOKEN") or None
        result=analyze(raw,lambda path:github_commits_lookup(path,token),a.max_age_seconds)
        Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        print(json.dumps({k:v for k,v in result.items() if k!="rows"},ensure_ascii=False,sort_keys=True))
        return 0
    except (OSError,ValueError) as exc:
        print("DL_GIT_COMMIT_EVIDENCE_ERROR: "+str(exc),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
