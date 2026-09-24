"""Independent offline chronological audit. No production writes or API calls."""
import collections,csv,datetime,gzip,json,math,pathlib,statistics,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT));OUT=pathlib.Path(__file__).resolve().parent
from research.production_acceleration import acceleration_signal
D=json.load(gzip.open(OUT/'archive_dataset.json.gz','rt'));END=D['cutoff'];snaps=D['snapshots'];B=D['bars']
def ts(x):return datetime.datetime.fromisoformat(x.replace('Z','+00:00')).timestamp()
def iso(x):return datetime.datetime.fromtimestamp(x,datetime.timezone.utc).isoformat()
def med(v):return round(statistics.median(v),4)if v else None
def pct(a,b):return (a/b-1)*100
def csvout(name,rows):
 if not rows:return
 keys=list(dict.fromkeys(k for r in rows for k in r));
 with open(OUT/name,'w') as f:
  w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader();w.writerows([{k:json.dumps(v,ensure_ascii=False)if isinstance(v,(list,dict))else v for k,v in r.items()}for r in rows])
R=[]
for p in (OUT/'runtime').glob('*.gz'):
 d=json.load(gzip.open(p,'rt'));p0=d['payload'];s=d['status'];t=ts(p0['generated_at_utc'])
 if t<=END:R.append({**d,'t':t,'alert_t':ts(s['checked_at_utc'])})
R.sort(key=lambda x:x['t']);R=list({r['t']:r for r in R}.values())
entries=json.load(open(ROOT/'production_decision_journal.json'))['entries'];buys=[e.copy()for e in entries if e['decision_type']=='BUY_SENT'];buykeys={(e['market'],e['decision_ts'])for e in buys}
for r in R:
 s=r['status']
 if s.get('email')!='DELIVERY_COMPLETED':continue
 for d in s.get('deliveries')or[s]:
  key=(d.get('market'),r['alert_t'])
  if key in buykeys:continue
  buykeys.add(key);buys.append({'market':d.get('market'),'decision_ts':r['alert_t'],'cycle_id':r['payload']['generated_at_utc'],'decision_type':'BUY_SENT',**{k:d.get(k)for k in ['entry_eur','stop_eur','tp1_eur','stake_eur']},'signal_score':next((x.get('signal_score')for x in r['payload'].get('watch',[])if x['market']==d.get('market')),None),'source_runtime_sha':r['sha']})
# Recover missing pre-journal plan fields from the exact delivery commit.
for e in buys:
 if e.get('entry_eur') or not e.get('source_runtime_sha'):continue
 p=OUT/'early_states'/(e['source_runtime_sha']+'.json.gz')
 if not p.exists():continue
 st=json.load(gzip.open(p,'rt')).get('markets',{}).get(e['market'],{})
 sent=st.get('last_sent_ts',0)
 if not e['decision_ts']<=sent<=e['decision_ts']+1200:continue
 for field in ['entry_eur','stop_eur','tp1_eur']:
  e[field]=st.get('last_sent_'+field)
 e['plan_source']='exact_delivery_commit_alert_state'
 e['actual_mark_sent_ts']=sent
buys.sort(key=lambda e:e['decision_ts'])

def sim(e,h,target_r=2,fee=.0035):
 t=e['decision_ts'];entry=e.get('entry_eur');stop=e.get('stop_eur')
 if not entry or not stop or entry<=stop:return None
 first=(int(t)//300+1)*300;end=min(t+h*3600,END);last=int(end)//300*300-300
 xs=[b for b in B.get(e['market'],[])if first<=b['t']/1000<=last]
 expected=max(0,(last-first)//300+1);coverage=len(xs)/expected if expected else 0
 if not xs:return None
 risk=entry-stop;target=e.get('tp1_eur') if target_r==2 and e.get('tp1_eur') else entry+target_r*risk
 price=xs[-1]['c'];reason='HORIZON_MARK';exit_ts=xs[-1]['t']/1000+300;ambiguous=False;gap=False
 for b in xs:
  if b['l']<=stop:
   price=stop;reason='STOP';exit_ts=b['t']/1000;ambiguous=b['h']>=target;gap=b['o']<stop;break
  if b['h']>=target:
   price=target;reason='TP';exit_ts=b['t']/1000;break
 high=max(xs,key=lambda b:b['h']);low=min(b['l']for b in xs)
 net=pct(price*(1-fee),entry*(1+fee));net_r=(price*(1-fee)-entry*(1+fee))/(entry*(1+fee)-stop*(1-fee))
 mfe=pct(high['h'],entry)
 return {'market':e['market'],'decision_utc':iso(t),'h':h,'target_r':target_r,'entry':entry,'stop':stop,'tp':target,'stake':e.get('stake_eur'),'score':e.get('signal_score'),'post_range_gate':t>=ts('2026-09-21T07:56:02+00:00'),'mature':t+h*3600<=END,'coverage':round(coverage,5),'bars':len(xs),'expected_bars':expected,'result':reason,'gross_pct':round(pct(price,entry),4),'net_pct':round(net,4),'gross_r':round((price-entry)/risk,4),'net_r':round(net_r,4),'mfe_pct':round(mfe,4),'mae_pct':round(pct(low,entry),4),'minutes_to_peak':round((high['t']/1000-t)/60,2),'exit_utc':iso(exit_ts),'ambiguous_stop_tp':ambiguous,'gap_below_stop':gap,'captured_positive_upside':round(max(0,pct(price,entry))/mfe,4)if mfe>0 else None,'net_pnl_guide_eur':round((e.get('stake_eur')or 0)*net/100,4),'fee_plus_slippage_each_side':fee}
res=[]
for e in buys:
 for h in [4,12,24]:
  for target in [1.4,1.5,1.6,2]:
   z=sim(e,h,target)
   if z:res.append(z)
csvout('buy_outcomes.csv',res)
summary={}
for h in [4,12,24]:
 summary[str(h)]={}
 for target in [1.4,1.5,1.6,2]:
  a=[r for r in res if r['h']==h and r['target_r']==target and r['mature']and r['coverage']==1 and r['post_range_gate']]
  summary[str(h)][str(target)]={'n':len(a),'positive_net':sum(r['net_pct']>0 for r in a),'stops':sum(r['result']=='STOP'for r in a),'tp':sum(r['result']=='TP'for r in a),'mean_net_pct':round(statistics.mean(r['net_pct']for r in a),4)if a else None,'median_net_pct':med([r['net_pct']for r in a]),'sum_net_pnl_guide_eur':round(sum(r['net_pnl_guide_eur']for r in a),2),'stake_known_n':sum(r['stake'] is not None for r in a),'median_net_r':med([r['net_r']for r in a]),'mfe_ge5':sum(r['mfe_pct']>=5 for r in a),'mae_le_minus5':sum(r['mae_pct']<=-5 for r in a),'ambiguous_bars':sum(r['ambiguous_stop_tp']for r in a)}
# Compare persisted outcomes, retaining evidence of incomplete archive coverage.
comparisons=[]
for e in entries:
 if e['decision_type']!='BUY_SENT':continue
 for h,old in e.get('evaluations',{}).items():
  z=sim(e,int(h))
  if not z:continue
  xs=[b for b in B.get(e['market'],[])if (int(e['decision_ts'])//300+1)*300<=b['t']/1000 and b['t']/1000+300<=min(e['decision_ts']+int(h)*3600,END)]
  comparisons.append({'market':e['market'],'decision':iso(e['decision_ts']),'h':h,'coverage':z['coverage'],'old_result':old['result'],'chronological_result':z['result'],'old_close_pct':old['close_return_pct'],'chronological_close_pct':round(pct(xs[-1]['c'],e['entry_eur']),4),'old_bars':old['bars_used'],'archive_bars':len(xs)})
csvout('journal_verification.csv',comparisons)
# Symmetric rejection outcomes: distinct shadow episodes, no claim of executability.
rej=json.load(open(ROOT/'production_rejection_shadow_journal.json'))['events'];rejsum={};reentry=[]
for reason in sorted(set(e['first_rejection_reason']for e in rej)):
 rejsum[reason]={}
 for h in [4,12,24]:
  a=[e['evaluations'][str(h)]for e in rej if e['first_rejection_reason']==reason and str(h)in e.get('evaluations',{})]
  rejsum[reason][str(h)]={'n':len(a),'mfe_ge5':sum(x['mfe_pct']>=5 for x in a),'mae_le_minus5':sum(x['mae_pct']<=-5 for x in a),'positive_close':sum(x['close_return_pct']>0 for x in a),'median_close':med([x['close_return_pct']for x in a])}
for e in rej:
 s=e.get('first_later_execution_valid_snapshot')or{};full=e.get('first_later_fully_actionable_entry')or{}
 if not s:continue
 later=next((b for b in buys if b['market']==e['market']and b['decision_ts']>=ts(s['at_utc'])-120),None)
 reentry.append({'market':e['market'],'rejected_at':e['rejected_at_utc'],'reason':e['first_rejection_reason'],'execution_valid_at':s['at_utc'],'state':s['signal_state'],'delay_minutes':s.get('reentry_delay_seconds',0)/60,'price_change_pct':s.get('return_from_rejection_pct'),'fully_actionable_at':full.get('at_utc'),'next_buy_at':iso(later['decision_ts'])if later else None,'evaluation_4h':e.get('execution_valid_evaluations',{}).get('4')})
csvout('reentries.csv',reentry)
# Rank all markets by fixed-window endpoint return, not current rolling 24h ticker.
winners={};ranking_all={}
for h in [24,72]:
 start=END-h*3600;ws=[s for s in snaps if s['at']>=start];first,last=ws[0],ws[-1]
 f={r['market']:r for r in first['rows']};l={r['market']:r for r in last['rows']};rank=[]
 for m in f.keys()&l.keys():
  if f[m].get('price')and l[m].get('price'):rank.append((pct(l[m]['price'],f[m]['price']),m))
 rank.sort(reverse=True);ranking_all[str(h)]=len(rank);rows=[]
 for ret,m in rank[:30]:
  p0=f[m]['price'];events=[];rejects=[];alerts=[]
  for r in R:
   if r['t']<start:continue
   x=next((x for x in r['payload'].get('tracking',r['payload'].get('watch',[]))if x['market']==m),None)
   if x:events.append((r['t'],x,r['sha']))
   for q in r['status'].get('rejections',[]):
    if q['market']==m:rejects.append((r['alert_t'],q['reason']))
  alerts=[e for e in buys if e['market']==m and e['decision_ts']>=start]
  bars=[b for b in B.get(m,[])if first['at']<=b['t']/1000<=last['at']]
  peak=max(bars,key=lambda b:b['h'])if bars else None
  observed_crossings={str(k):next((s['at']for s in ws if any(x['market']==m and x.get('price')and pct(x['price'],p0)>=k for x in s['rows'])),None)for k in [5,10,20]}
  det=events[0]if events else None;buy=alerts[0]if alerts else None
  detret=pct(det[1]['last'],p0)if det else None;buyret=pct(buy['entry_eur'],p0)if buy and buy.get('entry_eur')else None
  if buy and buyret is not None and buyret<5:category='BUY_OBSERVED_BEFORE_PLUS5_WINDOW_BASE'
  elif buy:category='BUY_OBSERVED_LATER_OR_PRICE_UNKNOWN'
  elif det and rejects:category='DETECTED_REJECTED_NO_BUY_OBSERVED'
  elif det:category='DETECTED_NO_BUY_REASON_UNRESOLVED'
  else:category='NO_DETECTION_TRACE_WITHIN_AVAILABLE_PRODUCTION_COVERAGE'
  rows.append({'rank':len(rows)+1,'market':m,'window_h':h,'start_utc':iso(first['at']),'end_utc':iso(last['at']),'return_pct':round(ret,4),'price_start':p0,'price_end':l[m]['price'],'category':category,'first_detection':iso(det[0])if det else None,'detection_price':det[1]['last']if det else None,'detection_extension_pct':round(detret,4)if detret is not None else None,'detection_state':det[1].get('signal_state')if det else None,'source_sha':det[2]if det else None,'first_buy':iso(buy['decision_ts'])if buy else None,'buy_price':buy.get('entry_eur')if buy else None,'buy_extension_pct':round(buyret,4)if buyret is not None else None,'delay_detection_buy_minutes':round((buy['decision_ts']-det[0])/60,2)if buy and det else None,'last_buy_before_window':next((iso(e['decision_ts']) for e in reversed(buys) if e['market']==m and e['decision_ts']<start),None),'reject_reasons':dict(collections.Counter(x[1]for x in rejects)),'peak_utc':iso(peak['t']/1000)if peak else None,'peak_gain_pct':round(pct(peak['h'],p0),4)if peak else None,**{'first_observed_plus'+k:iso(v)if v else None for k,v in observed_crossings.items()}})
 winners[str(h)]=rows;csvout(f'winners_{h}h.csv',rows)
# Geometry study on contemporaneously recorded research features, never mislabeled production.
geometry=[];statecounts=collections.Counter();qualitycounts=collections.Counter();permarket=collections.defaultdict(list)
for s in snaps:
 if s['at']<END-72*3600:continue
 for r in s['rows']:
  acc=acceleration_signal({'features':r['features']});statecounts[acc['state']]+=1
  if acc['state']!='CONFIRMED_ACCELERATION':continue
  f=r['features'].get('15m')or{};p=r.get('ask')or r.get('price');atr=f.get('atr14_eur');sup=f.get('support_eur');ran=f.get('consolidation_range_pct')
  if not p or atr is None or sup is None or ran is None:continue
  stop=min(sup-.5*atr,p-1.5*atr);dist=(p-stop)/p*100
  reason='NARROW'if ran<6 else 'WIDE_STOP'if dist>10 else 'GEOMETRY_PASS'
  z={'market':r['market'],'at':s['at'],'range':ran,'stop_distance':dist,'reason':reason,'score':acc['score'],'volume':r.get('volume'),'spread':pct(r['ask'],r['bid'])if r.get('ask')and r.get('bid')else None}
  geometry.append(z);permarket[r['market']].append(z)
transitions=[]
for m,gs in permarket.items():
 for a,b in zip(gs,gs[1:]):
  if a['reason']=='NARROW'and b['reason']=='WIDE_STOP'and b['at']-a['at']<=3600:
   transitions.append({'market':m,'from':iso(a['at']),'to':iso(b['at']),'minutes':round((b['at']-a['at'])/60,2),'range_before':a['range'],'range_after':b['range'],'stop_after':b['stop_distance']})
csvout('range_stop_transitions_research_proxy.csv',transitions)
# Runtime cadence and classifications use actual archived production, not theoretical cron.
gaps=[(b['t']-a['t'])/60 for a,b in zip(R,R[1:])];last24=[r for r in R if r['t']>=END-86400];g24=[(b['t']-a['t'])/60 for a,b in zip(last24,last24[1:])]
statuscounts=collections.Counter(r['status'].get('reason')for r in R)
scorebins={}
for label,lo,hi in [('6.5-7.49',6.5,7.5),('7.5-8.49',7.5,8.5),('8.5-10',8.5,10.1)]:
 a=[r for r in res if r['h']==4 and r['target_r']==2 and r['mature']and r['coverage']==1 and r['post_range_gate'] and r['score']is not None and lo<=r['score']<hi]
 scorebins[label]={'n':len(a),'positive_net':sum(r['net_pct']>0 for r in a),'median_net_pct':med([r['net_pct']for r in a])}
obj={'frozen_commit':'9cc5a402aa7ac42da48a71dcde7096eedc25a768','cutoff':iso(END),'archive_snapshots':len(snaps),'archive_bars':sum(len(v)for v in B.values()),'bar_conflicts':D['duplicate_bar_conflicts'],'runtime_cycles':len(R),'runtime_first':iso(R[0]['t'])if R else None,'runtime_last':iso(R[-1]['t'])if R else None,'runtime_last24_n':len(last24),'cadence_all_median_min':med(gaps),'cadence_last24_median_min':med(g24),'cadence_last24_max_min':max(g24)if g24 else None,'runtime_status_counts':dict(statuscounts),'journal_decisions':len(entries),'journal_buys':sum(e['decision_type']=='BUY_SENT'for e in entries),'reconstructed_buys':len(buys),'buy_plans_available':sum(bool(e.get('entry_eur')and e.get('stop_eur'))for e in buys),'buy_summary_complete_archive':summary,'score_bins_4h':scorebins,'rejection_counts':dict(collections.Counter(e['reason']for e in entries if e['decision_type']=='REJECTED')),'rejection_shadow_episodes':len(rej),'rejection_outcomes_as_recorded':rejsum,'reentry_execution_valid':len(reentry),'reentry_median_delay_min':med([r['delay_minutes']for r in reentry]),'reentry_median_price_change':med([r['price_change_pct']for r in reentry if r['price_change_pct']is not None]),'geometry_proxy_confirmed_observations':len(geometry),'geometry_proxy_counts':dict(collections.Counter(x['reason']for x in geometry)),'geometry_proxy_narrow_to_wide_transitions':transitions,'winners':winners,'ranked_markets':ranking_all,'journal_comparisons_complete_n':sum(x['coverage']==1 for x in comparisons),'journal_close_mismatches_complete':sum(x['coverage']==1 and abs(x['old_close_pct']-x['chronological_close_pct'])>.01 for x in comparisons),'journal_result_mismatches_complete':[x for x in comparisons if x['coverage']==1 and ((x['old_result']=='TP1')!=(x['chronological_result']=='TP')or x['old_result'].startswith('STOP')!=(x['chronological_result']=='STOP'))]}
relaxation={}
for filename in ['production_v21_range5_shadow_journal.json','production_early_building_shadow_journal.json']:
 evs=json.load(open(ROOT/filename))['events']
 if 'range5' in filename:
  evs=[e for e in evs if e.get('candidate5_passed') and not e.get('current6_passed')];eval_key='candidate5_evaluations'
 else:
  evs=[e for e in evs if e.get('passed_existing_execution_gate')];eval_key='evaluations'
 relaxation[filename]=[{'market':e['market'],'time':e.get('detected_at_utc',e.get('observed_at_utc')),'source_type':e.get('source_type'),'state':e.get('signal_state'),'evaluations':e.get(eval_key)}for e in evs]
(OUT/'relaxation_shadows.json').write_text(json.dumps(relaxation,indent=2))
(OUT/'results.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False));csvout('reconstructed_buys.csv',buys)
print(json.dumps({k:v for k,v in obj.items()if k not in ['winners','rejection_outcomes_as_recorded','geometry_proxy_narrow_to_wide_transitions']},indent=2))
