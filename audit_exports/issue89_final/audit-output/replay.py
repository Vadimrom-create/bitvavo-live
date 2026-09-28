"""Issue 89: offline causal decision replay. Never sends orders or changes production.
Run from parent: python3 audit-output/replay.py
Decisions consume recorded fields only; future bars are used solely for fills/outcomes.
"""
import base64, gzip, json, csv, math, sqlite3, sys, importlib.util
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

ROOT=Path(__file__).resolve().parent.parent
IN=ROOT/'audit-input'; OUT=ROOT/'audit-output'; OUT.mkdir(exist_ok=True)
CUTOFF=datetime.fromisoformat('2026-09-27T00:47:00+00:00').timestamp()
TARGETS='QNT AMP RARE HFT 2Z RUNE KMNO COW AGI TREAD'.split()
def iso(t): return datetime.fromtimestamp(t,timezone.utc).isoformat()
def load(n): return json.loads((IN/(n+'.json')).read_text())
def rows(n):
 x=load(n); return x.get('entries',x.get('events',[]))
def save(n,x): (OUT/(n+'.json')).write_text(json.dumps(x,ensure_ascii=False,indent=2))
def csvout(n,rs):
 if not rs:return
 fields=list(dict.fromkeys(k for r in rs for k in r))
 with (OUT/(n+'.csv')).open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in rs)
def strip(e): return {k:v for k,v in e.items() if 'evaluation' not in k}
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def rebuild():
 manifest=load('manifest')['archives'];missing=[x['path'] for x in manifest if not (IN/(x['path']+'.b64')).exists()]
 if missing:raise RuntimeError(f'{len(missing)} archives missing')
 db=sqlite3.connect(OUT/'bars.sqlite');db.execute('CREATE TABLE IF NOT EXISTS bars(m TEXT,t INTEGER,o REAL,h REAL,l REAL,c REAL,v REAL,status TEXT,available REAL,PRIMARY KEY(m,t))')
 old=module('old',IN/'research/decision_layer_old.py');new=module('new',IN/'research/decision_layer.py')
 switch=datetime.fromisoformat('2026-09-25T21:42:35+00:00').timestamp()
 counts=Counter();scans=[];timeline=[];first={};seen={}
 for x in sorted(manifest,key=lambda x:x['path']):
  b=base64.b64decode((IN/(x['path']+'.b64')).read_text())
  import hashlib
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['sha'],x['path']
  a=json.loads(gzip.decompress(b));ts=a['scan_ts']
  if ts>CUTOFF:continue
  scans.append({'scan_id':a['scan_id'],'scan_ts':ts,'source_commit':a.get('source_commit'),'markets':len(a['observations'])})
  records=[]
  for m,bs in a['candles_5m'].items():
   for r in bs:
    if r['t']/1000+300<=min(ts,CUTOFF):records.append((m,r['t'],r['o'],r['h'],r['l'],r['c'],r.get('v',0),r.get('bar_status',''),ts))
  db.executemany('INSERT OR IGNORE INTO bars VALUES(?,?,?,?,?,?,?,?,?)',records)
  dl=(old if ts<switch else new).decide(a['observations']);top={r['market'] for r in dl['top_actionable']};buys=[r for r in dl['ranked'] if r['action']=='ACHETE_MAINTENANT']
  counts['scans']+=1;counts['immediate_occurrences']+=len(buys);counts['immediate_in_top3']+=sum(r['market'] in top for r in buys);counts['scans_with_immediate']+=bool(buys);counts['scans_with_immediate_but_none_top3']+=bool(buys) and not any(r['market'] in top for r in buys)
  bydl={r['market']:(i+1,r) for i,r in enumerate(dl['ranked'])}
  for o in a['observations']:
   m=o['market'];sym=m.split('-')[0]
   if sym not in TARGETS:continue
   acc=o.get('acceleration',{})
   if not acc:acc=o.get('solaire_v2',{})
   rank,r=bydl[m];state=acc.get('state',acc.get('status'))
   key=(state,r['action'],r['bucket'])
   if seen.get(m)!=key or state in ('BUILDING_ACCELERATION','CONFIRMED_ACCELERATION'):
    timeline.append({'layer':'ARCHIVE_V2_V4_DL','market':m,'at_utc':iso(ts),'price':o.get('price_eur'),'acceleration':acc,'decision':r,'rank':rank,'top3':m in top,'baseline':o.get('baseline'),'scan_id':a['scan_id']})
   seen[m]=key
   for label,ok in [('first_building_or_confirmed',state in ('BUILDING_ACCELERATION','CONFIRMED_ACCELERATION')),('first_confirmed',state=='CONFIRMED_ACCELERATION'),('first_dl_immediate',r['action']=='ACHETE_MAINTENANT')]:
    if ok:first.setdefault(m,{}).setdefault(label,{'at_utc':iso(ts),'price':o.get('price_eur'),'acceleration':acc,'decision':r,'rank':rank,'trade_plan':(o.get('baseline') or {}).get('trade_plan')})
   if r['action']=='ACHETE_MAINTENANT':counts[m+'_immediate']+=1;counts[m+'_top3']+=m in top
 db.commit();save('archive_summary',{'counts':dict(counts),'first':first,'scans':scans,'bars':db.execute('select count(*) from bars').fetchone()[0]});csvout('timeline_archive',timeline);db.close()

def candidate_sets():
 prod=[e for e in rows('production_decision_journal') if e['decision_ts']<=CUTOFF]
 base=[]
 for i,e in enumerate(prod):
  if e['decision_type']=='BUY_SENT':base.append({'id':'B'+str(i),'source':'BASELINE','market':e['market'],'ts':e['decision_ts'],'quote':e['entry_eur'],'stop':e['stop_eur'],'score':e.get('signal_score',0)})
 extra=[]
 for i,e in enumerate(rows('production_v21_range5_shadow_journal')):
  if e.get('detected_ts',CUTOFF+1)<=CUTOFF and e.get('source_type')=='CONFIRMED_RANGE_REJECT' and e.get('signal_state')=='CONFIRMED_ACCELERATION' and e.get('candidate5_passed') and not e.get('current6_passed') and e.get('current6_reason')=='STRUCTURAL_RANGE_TOO_NARROW':
   extra.append({'id':'R'+str(i),'source':'RANGE5','market':e['market'],'ts':e['detected_ts'],'quote':e['candidate5_entry_eur'],'stop':e['candidate5_stop_eur'],'score':e.get('signal_score',0)})
 vs=rows('solaire_v31_journal');start=min(e['decision_ts'] for e in vs);ve=[]
 for i,e in enumerate(vs):
  if e['decision_ts']<=CUTOFF and e.get('event_type','').endswith('QUALIFIED_ENTRY') and e.get('selection_reason')=='SELECTABLE' and not e.get('evaluation_excluded'):
   ve.append({'id':'V'+str(i),'source':'V31','market':e['market'],'ts':e['decision_ts'],'quote':e['entry_eur'],'stop':e['stop_eur'],'score':e.get('economic_score',0)})
 save('candidate_sets',{'baseline':base,'range5_additions':extra,'v31_additions':ve,'v31_start':start})
 return {'C1_baseline':base,'C1_range5':base+extra,'C2_baseline':[e for e in base if e['ts']>=start],'C2_v31':[e for e in base if e['ts']>=start]+ve}

def simulate(name,candidates,stake,horizon,db,require_trade_bar=False):
 fee=.0025;slip=.001;capital=2331.61;cash=capital;maxpos=10;riskcap=12
 end=db.execute('select max(t) from bars').fetchone()[0]/1000+300
 active=[];trades=[];disp=[];cache={};maxconc=0
 def bars(m):
  if m not in cache:cache[m]={r[0]:r[1:] for r in db.execute('select t,o,h,l,c,v from bars where m=? order by t',(m,))}
  return cache[m]
 for e in sorted(candidates,key=lambda e:(e['ts'],-e['score'],e['market'])):
  et=(math.floor(e['ts']/300)+1)*300
  remaining=[]
  for a in active:
   if a['exit_ts']<=et:cash+=stake+a['pnl_eur']
   else:remaining.append(a)
  active=remaining;status=None
  if any(a['market']==e['market'] for a in active):status='ACTIVE_POSITION'
  elif len(active)>=maxpos or cash<stake:status='PORTFOLIO_CAP'
  elif et+horizon*3600>end:status='RIGHT_CENSORED'
  b=bars(e['market']);path=[b.get(int(t*1000)) for t in range(int(et),int(et+horizon*3600),300)]
  if not status and any(p is None for p in path):status='INCOMPLETE_DATA'
  if status:disp.append({**e,'status':status});continue
  entry=path[0][0]*(1+slip)
  if entry>e['quote']*1.005 or entry<=e['stop']:status='NO_FILL'
  if require_trade_bar and path[0][4]<=0:status='NO_TRANSACTION_ENTRY_BAR'
  qty=stake/(entry*(1+fee));risk=stake-qty*e['stop']*(1-slip)*(1-fee)
  if not status and risk>riskcap:status='RISK_CAP'
  if status:disp.append({**e,'status':status});continue
  exitprice=path[-1][3]*(1-slip);exitts=et+horizon*3600;reason='HORIZON';stopidx=None
  for j,p in enumerate(path):
   if p[2]<=e['stop']:
    exitprice=min(e['stop'],p[0])*(1-slip);exitts=et+(j+1)*300;reason='STOP';stopidx=j;break
  pnl=qty*exitprice*(1-fee)-stake;through=path if stopidx is None else path[:stopidx+1]
  tr={**e,'entry_utc':iso(et),'entry_ts':et,'entry_eur':entry,'quantity':qty,'stake_eur':stake,'risk_eur':risk,'exit_utc':iso(exitts),'exit_ts':exitts,'exit_eur':exitprice,'exit_reason':reason,'pnl_eur':pnl,'mfe_horizon_pct':(max(p[1] for p in path)/entry-1)*100,'mae_horizon_pct':(min(p[2] for p in path)/entry-1)*100,'mfe_through_exit_bar_pct':(max(p[1] for p in through)/entry-1)*100,'mae_through_exit_bar_pct':(min(p[2] for p in through)/entry-1)*100,'entry_bar_volume':path[0][4]}
  trades.append(tr);active.append(tr);cash-=stake;maxconc=max(maxconc,len(active));disp.append({**e,'status':'FILLED'})
 # Equity at closed bars, with conservative liquidation costs for open positions.
 peak=capital;dd=0;min_equity=capital
 if trades:
  for t in range(int(min(x['entry_ts'] for x in trades)),int(max(x['exit_ts'] for x in trades))+1,300):
   equity=capital
   for x in trades:
    if x['entry_ts']>t:continue
    if x['exit_ts']<=t:equity+=x['pnl_eur']
    else:
     p=bars(x['market']).get((t-300)*1000);mark=p[3] if p else x['entry_eur']/(1+slip)
     equity+=x['quantity']*mark*(1-slip)*(1-fee)-stake
   peak=max(peak,equity);dd=max(dd,peak-equity);min_equity=min(min_equity,equity)
 total=sum(t['pnl_eur'] for t in trades);wins=sum(t['pnl_eur']>0 for t in trades)
 met={'policy':name,'stake':stake,'horizon_hours':horizon,'signals':len(candidates),'fills':len(trades),'wins':wins,'losses':len(trades)-wins,'win_rate_pct':100*wins/len(trades) if trades else None,'expectancy_eur':total/len(trades) if trades else None,'net_pnl_eur':total,'buy_turnover_eur':len(trades)*stake,'gross_turnover_eur':len(trades)*stake+sum(x['quantity']*x['exit_eur'] for x in trades),'mtm_drawdown_eur':dd,'max_concurrent':maxconc,'stops':sum(x['exit_reason']=='STOP' for x in trades),'targets_captured':sorted(set(x['market'] for x in trades if x['market'].split('-')[0] in TARGETS)),'dispositions':dict(Counter(x['status'] for x in disp)),'zero_volume_entry_bars':sum(x['entry_bar_volume']==0 for x in trades)}
 tag=f'{name}_{stake}_{horizon}h';csvout('trades_'+tag,trades);csvout('dispositions_'+tag,disp);return met

if __name__=='__main__':
 if not (OUT/'archive_summary.json').exists():rebuild()
 sets=candidate_sets();db=sqlite3.connect(OUT/'bars.sqlite');metrics=[]
 for stake in (100,150):
  for h in (4,24):
   for name,es in sets.items():metrics.append(simulate(name,es,stake,h,db))
 save('metrics',metrics);print(json.dumps(metrics,ensure_ascii=False,indent=2))
