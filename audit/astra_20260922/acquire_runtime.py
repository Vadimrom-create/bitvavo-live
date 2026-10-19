"""Read-only acquisition of production inputs/status pinned to GitHub commits."""
import concurrent.futures,gzip,json,pathlib,time,urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
commits=json.loads((ROOT/'runtime_commits.json').read_text())
out=ROOT/'runtime';out.mkdir(exist_ok=True)
def get(row):
 sha=row['sha'];p=out/(sha+'.json.gz')
 if p.exists():return 'cached'
 result={'sha':sha,'committed_at':row['commit']['committer']['date']}
 for key,path in [('payload','production_alert_candidates.json'),('status','production_alert_status.json')]:
  url=f'https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/{sha}/{path}'
  for attempt in range(3):
   try:
    result[key]=json.load(urllib.request.urlopen(url,timeout=25));break
   except Exception:
    if attempt==2:raise
    time.sleep(1)
 p.write_bytes(gzip.compress(json.dumps(result,separators=(',',':')).encode(),mtime=0));return 'saved'
errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 futures={pool.submit(get,r):r['sha'] for r in commits}
 for i,f in enumerate(concurrent.futures.as_completed(futures),1):
  try:f.result()
  except Exception as e:errors.append({'sha':futures[f],'error':str(e)})
  if i%25==0:print(i,'/',len(commits),flush=True)
(ROOT/'acquisition_errors.json').write_text(json.dumps(errors,indent=2))
print('done',len(commits),'errors',len(errors),flush=True)
