#!/usr/bin/env python3
"""Episode-normalized audit of Solaire production decisions.

Raw production decisions can repeat when the same market remains/re-enters a
signal episode. This audit reconstructs tracking episodes from historical
production_alert_candidates snapshots and recomputes rejection/BUY outcome
statistics after deduplicating the same reason inside one episode.

Research-only; production behavior is unchanged.
"""
from __future__ import annotations
import json, subprocess, statistics, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from research.common import atomic_json, finite, utc

START="2026-09-21T08:00:00+00:00"
END="2026-09-21T23:30:00+00:00"
JOURNAL="production_decision_journal.json"
OUT="research/solaire_episode_normalized_outcomes_20260921.json"
GRACES=(0,600,900)

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z","+00:00")).timestamp()

def med(xs):
    xs=[x for x in xs if x is not None]
    return round(statistics.median(xs),4) if xs else None

def candidate_versions():
    shas=subprocess.check_output(
        ["git","log","--format=%H","--reverse",f"--since={START}",f"--until={END}","--","production_alert_candidates.json"],
        text=True,
    ).split()
    out=[]; seen=set()
    for sha in shas:
        try:
            obj=json.loads(subprocess.check_output(
                ["git","show",f"{sha}:production_alert_candidates.json"],
                text=True,stderr=subprocess.DEVNULL,
            ))
            s=obj.get("generated_at_utc")
            if not s or s in seen: continue
            seen.add(s)
            tracked={r.get("market") for r in (obj.get("tracking") or [])
                     if isinstance(r,dict) and r.get("market")}
            out.append({"at_utc":s,"ts":ts(s),"tracked":tracked})
        except Exception:
            continue
    return sorted(out,key=lambda x:x["ts"])

def episodes(snaps,grace):
    markets=sorted(set().union(*(s["tracked"] for s in snaps))) if snaps else []
    out={}
    for market in markets:
        eps=[]; active=None; last=None
        for s in snaps:
            if market not in s["tracked"]: continue
            if active is None or last is None or s["ts"]-last>grace+330:
                active={
                    "episode_index":len(eps)+1,
                    "start_ts":s["ts"],"start_utc":s["at_utc"],
                    "end_ts":s["ts"],"end_utc":s["at_utc"],
                }
                eps.append(active)
            else:
                active["end_ts"]=s["ts"]; active["end_utc"]=s["at_utc"]
            last=s["ts"]
        out[market]=eps
    return out

def assign_episode(e,eps,grace):
    t=finite(e.get("decision_ts"))
    if t is None:return None
    best=None
    for ep in eps.get(e.get("market"),[]):
        if ep["start_ts"]-330<=t<=ep["end_ts"]+grace+330:
            if best is None or abs(t-ep["start_ts"])<abs(t-best["start_ts"]):
                best=ep
    return best

def outcome_stats(rows):
    f=[r["evaluation"] for r in rows if r.get("evaluation")]
    return {
        "n":len(f),
        "mfe_ge_5pct":sum(finite(x.get("mfe_pct"),-999)>=5 for x in f),
        "mae_le_minus5pct":sum(finite(x.get("mae_pct"),999)<=-5 for x in f),
        "median_mfe_pct":med([finite(x.get("mfe_pct")) for x in f]),
        "median_mae_pct":med([finite(x.get("mae_pct")) for x in f]),
        "median_close_pct":med([finite(x.get("close_return_pct")) for x in f]),
    }

def summarize(rows):
    by=defaultdict(list)
    for r in rows:
        key="BUY_SENT" if r["decision_type"]=="BUY_SENT" else r["reason"]
        by[key].append(r)
    return {k:outcome_stats(v) for k,v in sorted(by.items())}

def main():
    snaps=candidate_versions()
    journal=json.loads(Path(JOURNAL).read_text())
    raw=[]
    for e in journal.get("entries",[]) or []:
        ev=(e.get("evaluations") or {}).get("4")
        if not ev: continue
        raw.append({
            "market":e.get("market"),
            "decision_ts":finite(e.get("decision_ts")),
            "at_utc":e.get("cycle_id"),
            "decision_type":e.get("decision_type"),
            "reason":e.get("reason"),
            "signal_price_eur":finite(e.get("signal_price_eur")),
            "signal_score":finite(e.get("signal_score")),
            "evaluation":ev,
        })

    policies={}
    for grace in GRACES:
        eps=episodes(snaps,grace)
        tagged=[]
        for e in raw:
            ep=assign_episode(e,eps,grace)
            tagged.append({**e,
                "episode_index":ep.get("episode_index") if ep else None,
                "episode_start_utc":ep.get("start_utc") if ep else None,
            })

        # First occurrence of the same decision reason inside the reconstructed
        # episode. This preserves reason transitions but removes retry duplicates.
        seen=set(); unique_reason=[]
        for e in sorted(tagged,key=lambda x:x["decision_ts"] or 0):
            key=(e["market"],e.get("episode_index"),
                 "BUY_SENT" if e["decision_type"]=="BUY_SENT" else e["reason"])
            if key in seen: continue
            seen.add(key); unique_reason.append(e)

        # Also report the first production decision of each episode, regardless
        # of later gate-reason transitions.
        seen_ep=set(); first_episode=[]
        for e in sorted(tagged,key=lambda x:x["decision_ts"] or 0):
            key=(e["market"],e.get("episode_index"))
            if key in seen_ep: continue
            seen_ep.add(key); first_episode.append(e)

        policies[str(grace)]={
            "raw_decisions_with_4h":len(tagged),
            "unique_episode_reason_decisions":len(unique_reason),
            "first_decision_per_episode":len(first_episode),
            "unique_episode_reason_stats":summarize(unique_reason),
            "first_decision_per_episode_stats":summarize(first_episode),
        }

    # A market-level sensitivity check prevents one highly fragmented market
    # (e.g. ICX) from dominating the interpretation.
    first_market_reason=[]; seen=set()
    for e in sorted(raw,key=lambda x:x["decision_ts"] or 0):
        key=(e["market"],"BUY_SENT" if e["decision_type"]=="BUY_SENT" else e["reason"])
        if key in seen:continue
        seen.add(key); first_market_reason.append(e)

    out={
        "schema":"solaire_episode_normalized_outcomes_v1",
        "generated_at_utc":utc(),
        "research_only":True,"affects_detection":False,"affects_buy_gate":False,"affects_email":False,
        "snapshot_count":len(snaps),"raw_row_count":len(raw),
        "grace_seconds":list(GRACES),
        "policies":policies,
        "first_market_reason_stats":summarize(first_market_reason),
        "method_note":"same reason is counted once per reconstructed tracking episode; reason transitions within an episode remain visible",
        "limitations":["single-session evidence","episode assignment uses persisted 5m snapshots and schedule-jitter tolerance"],
    }
    atomic_json(OUT,out)
    print("SOLAIRE_EPISODE_NORMALIZED "+json.dumps({
        "raw":len(raw),
        "grace10":policies["600"],
        "grace15":policies["900"],
        "market_reason":out["first_market_reason_stats"],
    },ensure_ascii=False))

if __name__=="__main__":main()
