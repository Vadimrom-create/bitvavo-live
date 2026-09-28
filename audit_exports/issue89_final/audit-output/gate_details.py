from replay import *
from evidence import walk_asks
from collections import defaultdict

def run():
 syms='AMP HFT 2Z RUNE COW RARE AGI'.split();prod=[e for e in rows('production_decision_journal') if e['decision_ts']<=CUTOFF and e['market'].split('-')[0] in syms]
 by=defaultdict(list)
 for e in prod:by[e['market']].append(e)
 out=[]
 for e in prod:
  reason=e['reason'];assessment='NON_IDENTIFIABLE';why=''
  if reason=='INSUFFICIENT_EXECUTION_LIQUIDITY':why='volume24h <75000; carnet non collecté par ce gate avant rejet. Conservatisme petite taille non démontré.'
  elif reason=='SPREAD_TOO_WIDE':why='spread >0.5%; coût top-book >0.4975 EUR/100 et >0.7463 EUR/150. Protection de coût conforme, valeur exacte non archivée par ce journal.'
  elif reason=='STRUCTURAL_STOP_TOO_WIDE':why='stop >10%; 150 EUR implique >15 EUR de risque brut, donc protecteur vis-à-vis plafond12. À100, verdict EUR dépend de la distance exacte non enregistrée.'
  elif reason=='STRUCTURAL_RANGE_TOO_NARROW':why='range <6%; veto structurel, pas preuve de non-exécutabilité mécanique. Effet économique seulement testé via C1.'
  elif reason=='DELIVERED':assessment='ALERTED';why='Validé puis email envoyé. Ce cas ne constitue pas un faux négatif de transport.'
  out.append({'market':e['market'],'journal_check_start_utc':iso(e['decision_ts']),'signal_price':e['signal_price_eur'],'gate':reason,'classification':assessment,'assessment_100_150':why})
 csvout('all_seven_gate_events',out)
 # A detailed table of earliest preserved execution-ready observations.
 first=json.loads((OUT/'first_events.json').read_text());books=json.loads((OUT/'first_ready_books.json').read_text());details=[]
 for s in syms:
  m=s+'-EUR';f=first.get(m,{}).get('first_v3_ready');r={'market':m,'first_production_check_utc':iso(by[m][0]['decision_ts']),'first_production_reason':by[m][0]['reason'],'production_counts':dict(Counter(e['reason'] for e in by[m]))}
  if not f:r.update(first_ready='NOT_FOUND',depth='UNKNOWN',spread='UNKNOWN',range='UNKNOWN',stop='UNKNOWN',risk100='UNKNOWN',risk150='UNKNOWN');details.append(r);continue
  e=f['event'];x=e['execution'];p=x['plan'];d=x.get('depth_benchmark_100_eur') or x.get('depth') or {};n100=d.get('vwap_eur');r.update(first_ready=f['at_utc'],entry=p['entry_eur'],stop=p['stop_eur'],stop_pct=p['stop_distance_pct'],range=x['structural_range_15m_pct'],spread=x['spread_pct'],vwap100=n100,impact100=d.get('depth_slippage_pct'),depth100_valid=d.get('valid'))
  r['risk100']=100-100/(n100*1.0025)*p['stop_eur']*.999*.9975
  b=books.get(m)
  if b and b['available_utc']==f['at_utc']:
   r.update(ask25_eur=b['ask_depth_eur'],vwap150=b['vwap_150'],impact150=b['impact_pct_150'],risk150=b['risk_eur_150'],cost_spread100=b['spread_cost_eur_100'],cost_spread150=b['spread_cost_eur_150'])
  else:r.update(ask25_eur='UNKNOWN',vwap150='UNKNOWN',impact150='UNKNOWN',risk150='UNKNOWN',cost_spread100=100*(x['spread_pct']/100)/(1+x['spread_pct']/100),cost_spread150=150*(x['spread_pct']/100)/(1+x['spread_pct']/100))
  details.append(r)
 save('seven_gate_details',details);csvout('seven_gate_details',details)
 print(json.dumps(details,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
