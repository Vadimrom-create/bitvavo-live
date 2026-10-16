#!/usr/bin/env python3
"""Read-only, exhaustive-by-page GitHub Actions dispatch audit for V4/DL.

Counts GITHUB-RECORDED workflow runs, not GitHub's undelivered schedule events.
No workflow dispatch, rerun, production mutation, orders, or account API use.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

REPO="Vadimrom-create/bitvavo-live"
WORKFLOW_NAME="Bitvavo live data + frozen V4 + measurement + useful alerts"
SCHEMA="solaire_dl_github_dispatch_audit_v1"
DAY=re.compile(r"^\d{4}-\d{2}-\d{2}$")

def validate_date(day):
    if not isinstance(day,str) or not DAY.fullmatch(day):
        raise ValueError("UTC day must be YYYY-MM-DD")
    date.fromisoformat(day)
    return day

def fetch_page(day,page,*,token=None):
    day=validate_date(day)
    if not isinstance(page,int) or not 1<=page<=20:
        raise ValueError("invalid page")
    url="https://api.github.com/repos/"+REPO+"/actions/runs?"+urllib.parse.urlencode({
        "created":day,"per_page":100,"page":page,
    })
    headers={
        "Accept":"application/vnd.github+json",
        "User-Agent":"solaire-dl-scheduled-event-audit/1",
        "X-GitHub-Api-Version":"2022-11-28",
    }
    if token:
        headers["Authorization"]="Bearer "+token
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=14) as response:
        if response.status!=200:
            raise ValueError("unexpected GitHub API status")
        data=json.loads(response.read(850000))
    if not isinstance(data,dict) or not isinstance(data.get("workflow_runs"),list):
        raise ValueError("malformed GitHub Actions API")
    return data

def analyze_day(day,fetch,max_pages=12):
    validate_date(day)
    if not 1<=max_pages<=20:
        raise ValueError("invalid max pages")
    first=fetch(day,1)
    total=first.get("total_count")
    if type(total) is not int or total<0:
        raise ValueError("missing total_count")
    pages=(total+99)//100
    if pages>max_pages:
        return {
            "date_utc":day,"status":"INCOMPLETE_TOO_MANY_PAGES",
            "github_repo_run_count":total,"legacy_schedule_recorded":None,
            "eligible_for_frequency_comparison":False,
        }
    full=list(first["workflow_runs"])
    for page in range(2,pages+1):
        response=fetch(day,page)
        if response.get("total_count")!=total:
            raise ValueError("mutable pagination total: cannot claim exhaustive")
        full.extend(response["workflow_runs"])
    ids=[row.get("id") for row in full if isinstance(row,dict)]
    if len(full)!=total or len(set(ids))!=len(ids):
        raise ValueError("incomplete or duplicate paginated run data")
    # Check created dates as returned by GitHub's UTC date filter.
    if any(not isinstance(row,dict) or
           not isinstance(row.get("created_at"),str) or
           row["created_at"][:10]!=day for row in full):
        raise ValueError("unexpected created_at outside requested UTC day")
    legacy=[x for x in full if x.get("name")==WORKFLOW_NAME]
    events=Counter(x.get("event","UNKNOWN") for x in legacy)
    conclusions=Counter(x.get("conclusion") or "UNFINISHED" for x in legacy)
    return {
        "date_utc":day,"status":"COMPLETE_GITHUB_RECORDED_RUNS",
        "github_repo_run_count":total,"legacy_total_recorded":len(legacy),
        "legacy_schedule_recorded":events["schedule"],
        "legacy_push_recorded":events["push"],
        "legacy_manual_recorded":events["workflow_dispatch"],
        "legacy_success_recorded":conclusions["success"],
        "legacy_cancelled_recorded":conclusions["cancelled"],
        "legacy_failure_recorded":conclusions["failure"],
        "reference_15min_cron_slots":96,
        "nominal_cron_slots_without_recorded_schedule_run":max(0,96-events["schedule"]),
        "nominal_cron_gap_not_platform_failure_proof":True,
        "eligible_for_frequency_comparison":True,
    }

def report(days,fetch):
    if not days or len(set(days))!=len(days) or len(days)>10:
        raise ValueError("1..10 unique days required")
    rows=[]
    for d in days:
        try:
            rows.append(analyze_day(d,fetch))
        except (OSError,ValueError,urllib.error.URLError) as exc:
            rows.append({
                "date_utc":d,"status":"UNKNOWN_LOOKUP_"+type(exc).__name__,
                "legacy_schedule_recorded":None,"eligible_for_frequency_comparison":False,
            })
    return {
        "schema":SCHEMA,"research_only":True,
        "source":"GITHUB_ACTIONS_REST_WORKFLOW_RUNS_BY_UTC_CREATION_DATE",
        "days":rows,
        "all_days_complete":all(x["eligible_for_frequency_comparison"] for x in rows),
        "root_cause_proven":False,
        "number_of_undelivered_schedule_events_proven":None,
        "production_files_changed":False,
        "orders_sent":0,
        "limitations":[
            "GitHub Actions API includes only recorded runs, never events not delivered to GitHub.",
            "Configured 96 slots/day are nominal, not guaranteed dispatches.",
            "GitHub workflow edits, queue limits, billing and platform behavior need separate investigation.",
            "A successful scheduled run is not proof each expected DL archive was committed.",
            "No economic inference from schedule frequencies.",
        ],
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--days",nargs="+",required=True)
    p.add_argument("--output",default="/tmp/dl-github-dispatch.json")
    args=p.parse_args()
    try:
        for day in args.days:
            validate_date(day)
        token=os.environ.get("GITHUB_TOKEN") or None
        o=report(args.days,lambda day,page:fetch_page(day,page,token=token))
        Path(args.output).write_text(json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
        print(json.dumps(o,ensure_ascii=False,sort_keys=True))
        return 0
    except (OSError,ValueError) as exc:
        print("GITHUB_DL_DISPATCH_AUDIT_FAILED: "+str(exc),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
