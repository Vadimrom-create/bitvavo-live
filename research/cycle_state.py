"""Bounded acquisition state; full historical evaluation belongs to another job."""
from research.input_contract import digest
from research.common import read_json
from pathlib import Path
import hashlib
import json


def recurrence(state, market, now, category):
    buckets={int(t):v for t,v in state.get('recent',{}).get(market,{}).items() if now-7200 <= v['at'] < now}
    if category in {'PRE-IGNITION','IGNITION'}:
        buckets[int(now//900)]={'at':now,'category':category}
    events=[buckets[k] for k in sorted(buckets)]
    return {'distinct_15m_periods':len(events),'recurrent':len(events)>=2,'sequence':events,'affects_baseline':False}


def advance(state, observations, candles, now):
    recent={m:{k:v for k,v in rows.items() if now-7200 <= v['at'] <= now}
            for m,rows in state.get('recent',{}).items()}
    recent={m:rows for m,rows in recent.items() if rows}
    delta={};seen=dict(state.get('seen',{}));revisions=0
    for o in observations:
        rows=recurrence(state,o['market'],now,o['category'])['sequence']
        if rows: recent[o['market']]={str(int(r['at']//900)):r for r in rows}
    for market,rows in candles.items():
        old=state.get('seen',{}).get(market,{})
        delta[market]=[b for b in rows if str(b['t']) not in old]
        revisions+=sum(str(b['t']) in old and old[str(b['t'])]!=digest(b) for b in rows)
        values={**{str(b['t']):digest(b) for b in rows},**old}
        seen[market]={k:values[k] for k in sorted(values,key=int)[-200:]}
    return {'schema_version':1,'recent':recent,'seen':seen,'updated_at':now,
            'ignored_revisions_this_cycle':revisions,'history_semantics':'first recorded observation; late unseen bars retained'},delta


def load_cycle_state(path, root, now):
    """Recover recent descriptive state without an exhaustive evaluation.

    A lost cache can repeat old bars in a new delta, but the authoritative
    first-source rule in the historical index still retains the original bar.
    """
    try:
        state=read_json(path)
        if state and state.get('state_sha256')==digest({k:v for k,v in state.items() if k!='state_sha256'}):
            source=Path(state['source_journal'])
            if hashlib.sha256(source.read_bytes()).hexdigest()!=state['source_journal_sha256']:
                raise ValueError('IMMUTABLE_JOURNAL_CHANGED')
            if state['updated_at']>now: raise ValueError('CYCLE_STATE_FROM_FUTURE')
            return state
    except (json.JSONDecodeError, KeyError, TypeError):
        pass  # Only this derived state is disposable; source errors propagate.
    scans=[]
    for p in sorted(Path(root).glob('*/*.json.gz'), reverse=True):
        scan=read_json(p)
        if scan['scan_ts']<now-7200: break
        if scan['scan_ts']<=now: scans.append(scan)
    state={}
    for scan in sorted(scans,key=lambda s:(s['scan_ts'],s['scan_id'])):
        state,_=advance(state,scan['observations'],scan.get('candles_5m',{}),scan['scan_ts'])
    return state
