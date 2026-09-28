"""Extract exact target events and recalculate size dependent ask execution."""
from replay import *

def walk_asks(asks,n):
 remain=n;qty=0;levels=0
 for p,q in sorted((float(p),float(q)) for p,q in asks):
  take=min(remain,p*q);qty+=take/p;remain-=take;levels+=1
  if remain<1e-8:return {'vwap_eur':n/qty,'quantity':qty,'levels':levels}
 return None

def run():
 prod=[e for e in rows('production_decision_journal') if e['decision_ts']<=CUTOFF]
 save('production_counts',{'all':dict(Counter(e['reason'] for e in prod)),'targets':{m:dict(Counter(e['reason'] for e in prod if e['market']==m+'-EUR')) for m in TARGETS}})
 timeline=[];first={};books=[];seen=set();v3=rows('solaire_v3_journal')
 for filename,layer in [('production_decision_journal','PRODUCTION'),('solaire_v3_journal','V3'),('solaire_v31_journal','V31'),('solaire_memory_entry_challenger_journal','MEMORY'),('solaire_policy_challengers_journal','POLICY_SHADOW')]:
  for e in rows(filename):
   ts=e.get('decision_ts',e.get('detected_ts',0));ex=e.get('execution',{});avail=max(ts,ex.get('available_ts',0))
   if not ts or avail>CUTOFF:continue
   m=e.get('market','')
   if m.split('-')[0] not in TARGETS:continue
   timeline.append({'layer':layer,'at_utc':iso(avail),'market':m,'event':strip(e)})
   ready=ex.get('ready') or e.get('ready') or (e.get('event_type','').endswith('READY_SHADOW'))
   label=None
   if layer=='V3' and ready:label='first_v3_ready'
   elif layer=='V31' and e.get('selection_reason')=='SELECTABLE':label='first_v31_selectable'
   elif layer=='PRODUCTION' and e.get('decision_type')=='BUY_SENT':label='first_production_buy'
   if label:
    x=first.setdefault(m,{})
    if label not in x or avail<x[label]['available_ts']:x[label]={'available_ts':avail,'at_utc':iso(avail),'event':strip(e)}
 for cycle in load('production_all_actionable_shadow_journal')['cycles']:
  ts=datetime.fromisoformat(cycle['checked_at_utc']).timestamp()
  if ts>CUTOFF:continue
  for e in cycle['events']:
   m=e['market']
   if m.split('-')[0] not in TARGETS:continue
   timeline.append({'layer':'ALL_ACTIONABLE_SHADOW','at_utc':iso(ts),'market':m,'event':e})
   if e.get('actionable_after_prior_thesis'):first.setdefault(m,{}).setdefault('first_shadow_actionable',{'available_ts':ts,'at_utc':iso(ts),'event':e})
 for e in v3:
  ex=e.get('execution',{});b=ex.get('book_snapshot');ts=max(e.get('decision_ts',0),ex.get('available_ts',0));key=(e['market'],ex.get('book_observed_ts'))
  if not b or ts>CUTOFF or key in seen:continue
  seen.add(key);p=ex.get('plan') or e.get('plan') or {};stop=p.get('stop_eur');bid=b.get('best_bid_eur');ask=b.get('best_ask_eur');spread=(ask/bid-1)*100 if bid and ask else None
  r={'market':e['market'],'available_utc':iso(ts),'available_ts':ts,'recorded_ready':bool(ex.get('ready',e.get('ready'))),'gate_reason':ex.get('reason',e.get('gate_reason')),'best_bid':bid,'best_ask':ask,'spread_pct':spread,'ask_depth_eur':sum(float(p)*float(q) for p,q in b['asks']),'bid_depth_present':bool(b.get('bids')),'stop_eur':stop,'range_pct':ex.get('structural_range_15m_pct')}
  for n in (100,150):
   w=walk_asks(b['asks'],n)
   if w:
    r.update({f'vwap_{n}':w['vwap_eur'],f'impact_pct_{n}':(w['vwap_eur']/ask-1)*100,f'spread_cost_eur_{n}':n*(1-bid/ask),f'levels_{n}':w['levels']})
    if stop:r[f'risk_eur_{n}']=n-n/(w['vwap_eur']*1.0025)*stop*.999*.9975
  books.append(r)
 # Funnel ledger includes independent V3.5 and memory observations, not implied production vetoes.
 if (IN/'funnel_targets.json').exists():
  f=load('funnel_targets');save('funnel_targets_extracted',f)
 csvout('timeline_journals',sorted(timeline,key=lambda x:x['at_utc']));save('first_events',first);csvout('book_sizes',books)
 firstbooks={}
 for r in sorted(books,key=lambda r:r['available_ts']):
  if r['recorded_ready'] and r['market'].split('-')[0] in TARGETS:firstbooks.setdefault(r['market'],r)
 save('first_ready_books',firstbooks);save('book_coverage',{'snapshots':len(books),'markets':len(set(r['market'] for r in books)),'full_bid_depth':sum(r['bid_depth_present'] for r in books)})
 print(json.dumps({'counts':load('production_counts') if False else json.loads((OUT/'production_counts.json').read_text()),'first_ready_books':firstbooks},ensure_ascii=False,indent=2))

if __name__=='__main__':run()
