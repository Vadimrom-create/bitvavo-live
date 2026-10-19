"""Offline behavioral reproductions against untouched production code."""
import json,sys,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from research.production_journal import evaluate_bars
from scripts.update_exit_policy_shadow import _sim,LOOKBACK
from research.production_alerts import select_events,mark_suppressed
from scripts.send_production_buy_alert import prior_buy_thesis_active
from research.features import closed_candles,describe
from research.common import freshness,utc

def run():
 results={}
 e={'decision_ts':0,'entry_eur':100,'stop_eur':90,'tp1_eur':120,'decision_type':'BUY_SENT'}
 raw=[[300000,100,125,99,122,1],[600000,115,119,85,88,1]]
 a=evaluate_bars(e,raw,4);b=evaluate_bars(e,list(reversed(raw)),4)
 assert a['result']=='TP1' and b['result']=='STOP'
 assert a['close_return_pct']==-12 and b['close_return_pct']==22
 results['unsorted_evaluation']={'ascending':a,'descending_api_order':b}
 # A bar starting inside the horizon but ending outside it is accepted.
 late=[[14_400_000,100,130,99,125,1]]
 h=evaluate_bars({**e,'decision_ts':60},late,4);assert h['result']=='TP1'
 results['bar_crossing_horizon']={'decision_ts':60,'horizon_end':14460,'accepted_bar_end':14700,'result':h}
 # Completeness tests only the end, not the missing initial interval.
 truncated=[(14_100_000,100,101,99,100,1)]
 sim=_sim(100,90,120,0,truncated,4,None)
 assert sim['complete_horizon'] and sim['bars_used']==1
 results['false_complete_shadow_horizon']=sim
 # Nominal age 30h removes records irrespective of frozen study membership.
 age29=[t for t in [0] if 29*3600-t<=LOOKBACK]
 age31=[t for t in [0] if 31*3600-t<=LOOKBACK]
 assert len(age29)==1 and len(age31)==0
 results['rolling_cohort_eviction']={'members_after_29h':len(age29),'members_after_31h':len(age31),'lookback_hours':LOOKBACK/3600}
 # Suppression marks whole episode handled; later prior stop breach cannot reopen it.
 row={'market':'TEST-EUR','last':100,'signal_score':8,'signal_state':'CONFIRMED_ACCELERATION','action_status':'ACCELERATION_READY','data_quality':{'ok':True}}
 payload={'generated_at_utc':utc(1000),'watch':[row],'tracking':[row]}
 state={'markets':{'TEST-EUR':{'active':False,'episode':1,'sent_episode':1,'handled_episode':1,'last_sent_ts':500,'last_sent_stop_eur':90}}}
 events,state=select_events(payload,state,1000);assert len(events)==1
 state=mark_suppressed(state,events[0],1000,'PRIOR_BUY_THESIS_STILL_ACTIVE')
 payload['generated_at_utc']=utc(1300)
 events2,state2=select_events(payload,state,1300)
 thesis,_=prior_buy_thesis_active(state,{'row':row,'quote':{'ask':89},'candles_5m':[]},1300)
 assert thesis is False and events2==[]
 results['handled_episode_blocks_later_invalidation']={'prior_thesis_active_after_stop_breach':thesis,'events_available_to_revalidate':len(events2)}
 # A transport returning only an ancient closed candle passes synthetic freshness.
 old=[[0,100,101,99,100,1]];cs=closed_candles(old,'15m',100000)
 f=describe(cs,'15m');q=freshness(now=100000,retrieved=utc(100000),candle_start_ms=cs[-1]['t'],interval='15m')
 assert f['valid'] and q['ok']
 results['synthetic_no_trade_freshness']={'feature_valid':f['valid'],'fresh':q['ok'],'no_trade_bars_last25':f['no_trade_bars_last25'],'interpretation':'documented no-trade gaps legitimate; truncated/stale response cannot be distinguished'}
 return results
if __name__=='__main__':
 results=run();p=pathlib.Path(__file__).with_name('defect_reproductions.json');p.write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
