#!/usr/bin/env python3
"""Audit Solaire episode fragmentation and grace-period alternatives.

Production currently ends an acceleration episode immediately when a market is
absent from one tracking snapshot. A one-scan dip can therefore create a new
episode ~5 minutes later and interact with the 24h prior-thesis suppressor.

This audit replays actual production_alert_candidates.json history and compares
the current zero-grace policy with 10m and 15m gap grace periods. Research-only.
"""
from __future__ import annotations
import json, subprocess, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from research.common import atomic_json, utc

START="2026-09-21T08:00:00+00:00"
END="2026-09-21T21:45:00+00:00"
OUT="research/solaire_episode_grace_20260921.json"
GRACES=(0,600,900)

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def versions():
    shas=subprocess.check_output(
        ["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--","production_alert_candidates.json"],
        text=True,
    ).split()
    out=[]; seen=set()
    for sha in shas:
        try:
            obj=json.loads(subprocess.check_output(
                ["git","show",f"{sha}:production_alert_candidates.json"],text=True,stderr=subprocess.DEVNULL
            ))
            s=obj.get("generated_at_utc")
            if not s or s in seen: continue
            seen.add(s)
            tracked={r.get("market") for r in (obj.get("tracking") or []) if isinstance(r,dict) and r.get("market")}
            states={r.get("market"):r.get("signal_state") for r in (obj.get("tracking") or []) if isinstance(r,dict) and r.get("market")}
            out.append({"at_utc":s,"ts":ts(s),"tracked":tracked,"states":states})
        except Exception:
            continue
    return sorted(out,key=lambda x:x["ts"])

def replay(snaps,grace):
    markets=sorted(set().union(*(x["tracked"] for x in snaps))) if snaps else []
    result={}
    for market in markets:
        episodes=[]; active=None; last_seen=None
        for snap in snaps:
            present=market in snap["tracked"]
            if present:
                if active is None:
                    active={"start_ts":snap["ts"],"start_utc":snap["at_utc"],"end_ts":snap["ts"],
                            "end_utc":snap["at_utc"],"snapshots":1,"states":[snap["states"].get(market)]}
                    episodes.append(active)
                elif last_seen is not None and snap["ts"]-last_seen>grace+330:
                    # +330 tolerates normal 5m schedule jitter; a gap beyond the
                    # chosen grace starts a new episode.
                    active={"start_ts":snap["ts"],"start_utc":snap["at_utc"],"end_ts":snap["ts"],
                            "end_utc":snap["at_utc"],"snapshots":1,"states":[snap["states"].get(market)]}
                    episodes.append(active)
                else:
                    active["end_ts"]=snap["ts"];active["end_utc"]=snap["at_utc"];active["snapshots"]+=1
                    active["states"].append(snap["states"].get(market))
                last_seen=snap["ts"]
        result[market]=episodes
    return result

def main():
    snaps=versions()
    policies={str(g):replay(snaps,g) for g in GRACES}
    summaries={}
    for g,res in policies.items():
        counts={m:len(es) for m,es in res.items()}
        summaries[g]={
            "markets":len(counts),
            "episodes":sum(counts.values()),
            "markets_with_multiple_episodes":sum(n>1 for n in counts.values()),
            "max_episodes_one_market":max(counts.values()) if counts else 0,
        }

    current=policies["0"]; g10=policies["600"]; g15=policies["900"]
    rows=[]
    for market in sorted(current):
        n0=len(current[market]);n10=len(g10.get(market,[]));n15=len(g15.get(market,[]))
        if n0!=n10 or n0!=n15:
            rows.append({"market":market,"episodes_current":n0,"episodes_grace10":n10,
                         "episodes_grace15":n15,"merged_by_10m":n0-n10,"merged_by_15m":n0-n15})

    decision={}
    try:
        decision=json.loads(Path("production_decision_journal.json").read_text())
    except Exception:
        pass
    prior=defaultdict(int)
    for e in decision.get("entries",[]) or []:
        if e.get("reason")=="PRIOR_BUY_THESIS_STILL_ACTIVE":
            prior[e.get("market")]+=1
    for r in rows:
        r["prior_thesis_suppressions_today"]=prior.get(r["market"],0)

    out={
        "schema":"solaire_episode_grace_audit_v1","generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "snapshot_count":len(snaps),"summary":summaries,
        "fragmented_markets":sorted(rows,key=lambda r:(-r["merged_by_15m"],-r["prior_thesis_suppressions_today"],r["market"])),
        "prior_thesis_suppressions_total":sum(prior.values()),
        "prior_thesis_suppressions_by_market":dict(prior),
        "method_note":"normal schedule jitter <=330s is tolerated; grace extends episode across additional missing-snapshot gaps",
    }
    atomic_json(OUT,out)
    print("SOLAIRE_EPISODE_GRACE "+json.dumps({
        "snapshot_count":len(snaps),"summary":summaries,
        "fragmented_count":len(rows),"prior_thesis_suppressions_total":sum(prior.values()),
        "top":out["fragmented_markets"][:20],
    },ensure_ascii=False))

if __name__=="__main__":main()
