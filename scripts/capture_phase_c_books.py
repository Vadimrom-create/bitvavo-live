#!/usr/bin/env python3
"""Independent measurement of books for live veto episodes; no re-entry decision."""
import copy,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from research.common import atomic_json,read_json,utc
from research.http import PublicClient
from research.execution_observability import book_evidence,identity

STATE='phase_c_observation_state.json'
STATUS='phase_c_observation_status.json'

def collect(registry,state,client,clock=time.time,budget_seconds=120):
    start=clock();records=[];previous=copy.deepcopy(state or {});cursor=int(previous.get('cursor',0))
    episodes=sorted([e for e in (registry.get('episodes') or {}).values() if not e.get('closed') and e.get('expires_at_ts',0)>start],
                    key=lambda e:(e.get('first_veto_ts',0),e['market'],e['event_id']))
    if episodes:cursor%=len(episodes)
    ordered=episodes[cursor:]+episodes[:cursor];attempted=0
    for episode in ordered:
        now=clock();market=episode['market']
        base={'observation_id':identity('observation','PHASE_C',episode['event_id'],start),
              'registry_episode_id':episode['event_id'],'episode_id':episode.get('source_episode_id'),
              'parent_decision_id':episode.get('source_decision_id'),'market':market,
              'original_veto_ts':episode.get('first_veto_ts'),'observed_at_ts':now,
              'book_temporality':'NEW_SHADOW_SNAPSHOT_NOT_THE_ORIGINAL_VETO_BOOK',
              'research_only':True,'affects_buy_gate':False,'affects_email':False,'orders_submitted':False,
              'c3_status':'UNKNOWN/NO_AUTHORIZATION'}
        if now-start>=budget_seconds:
            records.append({**base,'status':'BUDGET_NOT_EVALUATED','execution_costs':None});continue
        attempted+=1
        try:
            book=client.get('/'+market+'/book',{'depth':1000},cache=False)
            meta=copy.deepcopy(client.metadata('/'+market+'/book',{'depth':1000}))
            observed=clock();costs=book_evidence(book,meta,observed)
            try:
                trades=client.get('/'+market+'/trades',cache=False)
                trade_meta=client.metadata('/'+market+'/trades')
                trade_error=None
            except (ValueError,RuntimeError) as exc:trades=None;trade_meta={};trade_error=str(exc)
            records.append({**base,'status':'OBSERVED','execution_costs':costs,'trades':trades,
                            'trades_retrieved_at_utc':trade_meta.get('retrieved_at_utc'),'trade_error':trade_error})
        except (ValueError,RuntimeError,KeyError) as exc:
            records.append({**base,'status':'DATA_UNAVAILABLE','error':str(exc),'execution_costs':None})
    previous['cursor']=(cursor+attempted)%len(episodes) if episodes else 0
    previous['updated_at_utc']=utc(clock());previous['research_only']=True
    return records,previous

def main():
    records,state=collect(read_json(ROOT/'production_recovery_registry_shadow.json',{}),read_json(ROOT/STATE,{}),
                          PublicClient(timeout=8,retries=2,requests_per_second=8))
    for row in records:
        dest=ROOT/'execution_observations'/(row['observation_id']+'.json')
        if not dest.exists():atomic_json(dest,row)
    atomic_json(ROOT/STATE,state)
    summary={'checked_at_utc':utc(),'eligible_episodes':len(records),'status_counts':{},'research_only':True,
             'affects_buy_gate':False,'affects_email':False,'orders_submitted':False,'c3_status':'UNKNOWN/NO_AUTHORIZATION'}
    for row in records:summary['status_counts'][row['status']]=summary['status_counts'].get(row['status'],0)+1
    atomic_json(ROOT/STATUS,summary);print(json.dumps(summary))
if __name__=='__main__':main()
