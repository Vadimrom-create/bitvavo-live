"""Build compact audit inputs from committed archives; never invokes a scanner."""
import gzip,json,pathlib,datetime,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=pathlib.Path(__file__).resolve().parent
END=datetime.datetime.fromisoformat('2026-09-22T21:45:00+00:00').timestamp();START=END-72*3600
snapshots=[];bars={};conflicts=0;manifest=[]
for p in sorted((ROOT/'history').rglob('*.gz')):
 if p.parent.name<'2026-09-19':continue
 d=json.load(gzip.open(p,'rt'));t=d['scan_ts']
 if not START-3600<=t<=END:continue
 manifest.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 rows=[]
 for o in d.get('observations',[]):
  f=o.get('features')or{};base=o.get('baseline')or{};acc=o.get('acceleration')or{}
  rows.append({'market':o['market'],'price':o.get('price_eur'),'volume':o.get('quote_volume_24h_eur'),'bid':base.get('bid'),'ask':base.get('ask'),'quality':(o.get('data_quality')or{}).get('ok'),'acceleration':acc,'features':f})
 for m,cs in d.get('candles_5m',{}).items():
  for c in cs:
   if c['t']/1000<START-3600 or c['t']/1000+300>END:continue
   dest=bars.setdefault(m,{})
   if c['t'] in dest and dest[c['t']]!=c:conflicts+=1
   # First archived version is retained; flag later differences.
   dest.setdefault(c['t'],c)
 snapshots.append({'at':t,'source':str(p.relative_to(ROOT)),'source_commit':d.get('source_commit'),'rows':rows})
data={'cutoff':END,'start':START,'snapshots':snapshots,'bars':{m:sorted(v.values(),key=lambda x:x['t'])for m,v in bars.items()},'duplicate_bar_conflicts':conflicts}
(OUT/'archive_dataset.json.gz').write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
(OUT/'archive_manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({'snapshots':len(snapshots),'markets_bars':len(bars),'bars':sum(map(len,bars.values())),'conflicts':conflicts,'first':snapshots[0]['at'],'last':snapshots[-1]['at']},indent=2))
