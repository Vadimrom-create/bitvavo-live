"""Final causal availability, revalidation challenger, all-universe controls."""
from replay import *
from collections import defaultdict
import statistics

def main():
 db=sqlite3.connect(OUT/'bars.sqlite');sets=candidate_sets();mail={r['id']:r for r in load('mail_availability')['matched']};assert len(mail)==125
 original=sets['C1_baseline'];base=[dict(e,ts=mail[e['id']]['mail_ts'],journal_ts=e['ts']) for e in original]
 r5=[e for e in sets['C1_range5'] if e['source']=='RANGE5'];v31=[e for e in sets['C2_v31'] if e['source']=='V31']
 start=load('solaire_v31_journal')['events'][0]['decision_ts'];watch=load('revalidation_publication_evidence');raw=[];pattern=[]
 for pub in watch['results']:
  for e in pub['found']:
   s=e['snapshot'];t=datetime.fromisoformat(pub['published_utc'].replace('Z','+00:00')).timestamp();checked=datetime.fromisoformat(s['at_utc']).timestamp();assert t>=checked
   qualifies=s['signal_state']=='CONFIRMED_ACCELERATION' and s['signal_score']>=6.5 and s['evidence_count']>=3 and t-checked<=90
   rec={'id':'RV:'+e['event_id'],'source':'REVALIDATION','market':e['market'],'ts':t,'quote':s['entry_eur'],'stop':s['stop_eur'],'score':s['signal_score'],'check_started_ts':checked,'publication_sha':pub['sha'],'initial_reject_at':e['rejected_at_utc'],'initial_reason':e['first_rejection_reason'],'spread_pct':s['spread_pct'],'range_pct':s['structural_range_15m_pct'],'stop_distance_pct':s['stop_distance_pct']}
   if qualifies and t<=CUTOFF:raw.append(rec)
   following=[b for b in base if b['market']==e['market'] and checked<=b['ts']<=min(CUTOFF,checked+4*3600)]
   pattern.append({**rec,'production_buy_next4h':bool(following),'next4h_complete':checked+4*3600<=CUTOFF,'qualifies':qualifies})
 # Conservatively preserve prior alerted theses. No future BUY absence enters selection.
 ledger={};retry=[];reject=[]
 for e in sorted(base+raw,key=lambda e:(e['ts'],e['source'],e['market'])):
  m=e['market'];t=e['ts'];prev=ledger.get(m)
  if e['source']=='REVALIDATION' and prev:
   first=(int(prev['ts']//300)+1)*300000
   low=db.execute('select min(l) from bars where m=? and t>=? and t+300000<=? and available<=?',(m,first,t*1000,t)).fetchone()[0]
   active=t-prev['ts']<=86400 and e['quote']>prev['stop'] and (low is None or low>prev['stop'])
   if active:reject.append(dict(e,status='PRIOR_ALERT_THESIS_ACTIVE_OR_UNOBSERVED'));continue
  ledger[m]=e
  if e['source']=='REVALIDATION':retry.append(e)
 save('revalidation_candidates',{'raw':raw,'admitted':retry,'prior_thesis_held':reject});csvout('revalidation_pattern',pattern)
 common={'F_Baseline':[e for e in base if e['ts']>=start], 'F_C1_range5':[e for e in base+r5 if e['ts']>=start], 'F_C2_v31':[e for e in base+v31 if e['ts']>=start], 'F_C3_revalidation':[e for e in base+retry if e['ts']>=start]}
 full={'F_full_Baseline':base,'F_full_C1':base+r5,'F_full_C3':base+retry}
 metrics=[]
 for n in (100,150):
  for h in (4,24):
   for name,es in common.items():metrics.append(simulate(name,es,n,h,db))
  for name,es in full.items():metrics.append(simulate(name,es,n,4,db))
 save('final_metrics',metrics);save('final_candidate_sets',common);csvout('final_metrics',metrics)
 cohort=[];deltas=[];targetset={x+'-EUR' for x in TARGETS}
 for met in metrics:
  name=met['policy'];n=met['stake'];h=met['horizon_hours'];es=list(csv.DictReader((OUT/f'trades_{name}_{n}_{h}h.csv').open()))
  for label,pred in [('10_winners',lambda e:e['market'] in targetset),('negative_controls',lambda e:e['market'] not in targetset)]:
   a=[e for e in es if pred(e)];pnl=sum(float(e['pnl_eur']) for e in a)
   cohort.append({'policy':name,'stake':n,'horizon':h,'cohort':label,'trades':len(a),'markets':len(set(e['market'] for e in a)),'wins':sum(float(e['pnl_eur'])>0 for e in a),'losses':sum(float(e['pnl_eur'])<0 for e in a),'pnl':pnl,'expectancy':pnl/len(a) if a else None,'median_mfe':statistics.median(float(e['mfe_horizon_pct']) for e in a) if a else None,'median_mae':statistics.median(float(e['mae_horizon_pct']) for e in a) if a else None,'stops':sum(e['exit_reason']=='STOP' for e in a)})
  if name not in ('F_Baseline','F_full_Baseline'):
   base_name='F_full_Baseline' if name.startswith('F_full') else 'F_Baseline';bs=list(csv.DictReader((OUT/f'trades_{base_name}_{n}_{h}h.csv').open()));bi={e['id'] for e in bs};ci={e['id'] for e in es};extra=[e for e in es if e['id'] not in bi];drop=[e for e in bs if e['id'] not in ci]
   deltas.append({'policy':name,'stake':n,'horizon':h,'extra_trades':len(extra),'extra_losers':sum(float(e['pnl_eur'])<0 for e in extra),'displaced':len(drop),'displaced_losers':sum(float(e['pnl_eur'])<0 for e in drop),'extra_targets':sorted(set(e['market'] for e in es if e['market'] in targetset)-set(e['market'] for e in bs if e['market'] in targetset))})
 save('final_cohorts',cohort);save('final_deltas',deltas);csvout('final_cohorts',cohort);csvout('final_deltas',deltas)
 save('revalidation_summary',{'raw_records':len(raw),'markets':len(set(e['market'] for e in raw)),'admitted_after_prior':len(retry),'held_prior':len(reject),'published_delay_min':min(e['ts']-e['check_started_ts'] for e in raw),'published_delay_max':max(e['ts']-e['check_started_ts'] for e in raw),'no_production_buy_in_next4h':sum(not e['production_buy_next4h'] for e in pattern),'mature_next4h':sum(e['next4h_complete'] for e in pattern),'no_production_buy_mature':sum(e['next4h_complete'] and not e['production_buy_next4h'] for e in pattern),'common_start':iso(start),'email_rows_matched':len(mail),'bar_shifted':sum(int(e['ts']//300)!=int(e['journal_ts']//300) for e in base)})
 print(json.dumps(read_result if False else json.loads((OUT/'revalidation_summary.json').read_text()),indent=2))
 for x in metrics:
  if x['horizon_hours']==4:print(x['policy'],x['stake'],x['fills'],x['wins'],x['losses'],round(x['net_pnl_eur'],2),round(x['mtm_drawdown_eur'],2),x['targets_captured'])

if __name__=='__main__':main()
