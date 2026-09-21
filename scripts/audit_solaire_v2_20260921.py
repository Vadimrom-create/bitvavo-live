#!/usr/bin/env python3
"""Adversarial replay of today's Solaire V2 final-gate decisions.

Research-only. Reconstructs final-gate rejections from workflow logs and measures
forward 5m-candle outcomes from Bitvavo. It never changes detection, BUY gating,
emailing, or execution.
"""
from __future__ import annotations
import json, os, re, subprocess, time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from research.common import atomic_json, finite, utc
from research.http import PublicClient

OUT="research/solaire_v2_adversarial_20260921.json"
TARGET_DAY="2026-09-21"
H=(1,4)
TRACK={"STRUCTURAL_RANGE_TOO_NARROW","STRUCTURAL_STOP_TOO_WIDE","SPREAD_TOO_WIDE","INSUFFICIENT_EXECUTION_LIQUIDITY"}

def gh(path):
    token=os.environ.get("GITHUB_TOKEN")
    if not token: raise RuntimeError("GITHUB_TOKEN_REQUIRED")
    import urllib.request
    req=urllib.request.Request("https://api.github.com"+path,headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json"})
    with urllib.request.urlopen(req,timeout=20) as r:return json.load(r)

def logs(run_id):
    # gh CLI is available on GitHub-hosted runners and handles the log archive.
    p=subprocess.run(["gh","run","view",str(run_id),"--log"],cwd=ROOT,text=True,capture_output=True,timeout=90)
    if p.returncode: return ""
    return p.stdout

def ts(x): return datetime.fromisoformat(x.replace("Z","+00:00")).timestamp()

def main():
    runs=gh("/repos/Vadimrom-create/bitvavo-live/actions/runs?per_page=100")["workflow_runs"]
    runs=[r for r in runs if r.get("name")=="Solaire direct Bitvavo scan" and r.get("created_at","").startswith(TARGET_DAY)]
    events=[]
    for r in runs:
        txt=logs(r["id"])
        for line in txt.splitlines():
            if "SOLAIRE_ALERT " not in line: continue
            try: d=json.loads(line.split("SOLAIRE_ALERT ",1)[1])
            except Exception: continue
            checked=d.get("checked_at_utc") or r["created_at"]
            for x in d.get("rejections",[]) or []:
                if x.get("reason") in TRACK:
                    events.append({"market":x.get("market"),"reason":x.get("reason"),"at_utc":checked,"run_id":r["id"]})
    # de-duplicate same market/reason episode approximately: keep first occurrence.
    uniq=[]; seen=set()
    for e in sorted(events,key=lambda z:z["at_utc"]):
        k=(e["market"],e["reason"])
        if k not in seen: seen.add(k); uniq.append(e)
    client=PublicClient(timeout=12,retries=3,requests_per_second=8); client.get("/time",cache=False)
    by_reason=defaultdict(list)
    for e in uniq:
        raw=client.get("/"+e["market"]+"/candles",{"interval":"5m","limit":400},cache=False)
        t0=ts(e["at_utc"]); rows=[]
        for x in raw:
            if not isinstance(x,list) or len(x)<6: continue
            t=finite(x[0]); hi=finite(x[2]); lo=finite(x[3]); cl=finite(x[4])
            if None not in (t,hi,lo,cl) and t>=t0*1000: rows.append((t/1000,hi,lo,cl))
        rows.sort()
        if not rows: continue
        base=rows[0][3]; e["baseline_eur"]=base; e["forward"]={}
        for h in H:
            z=[x for x in rows if x[0] < t0+h*3600]
            if not z: continue
            e["forward"][str(h)]={"mfe_pct":round((max(x[1] for x in z)/base-1)*100,3),
              "mae_pct":round((min(x[2] for x in z)/base-1)*100,3),
              "close_pct":round((z[-1][3]/base-1)*100,3),"bars":len(z)}
        by_reason[e["reason"]].append(e)
    summary={}
    for reason,es in by_reason.items():
        z=[e["forward"].get("1") for e in es if e["forward"].get("1")]
        summary[reason]={"events":len(es),"evaluated_1h":len(z),
          "mfe_ge_5pct_1h":sum(x["mfe_pct"]>=5 for x in z),
          "mae_le_minus5pct_1h":sum(x["mae_pct"]<=-5 for x in z)}
    out={"schema":"solaire_v2_adversarial_replay_v1","generated_at_utc":utc(),"day":TARGET_DAY,
      "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
      "method":"first rejection per market/reason; forward closed/available 5m candles; no hindsight classification from price alone",
      "summary":summary,"events":uniq}
    atomic_json(OUT,out); print("SOLAIRE_V2_ADVERSARIAL "+json.dumps(summary,ensure_ascii=False))
if __name__=="__main__": main()
