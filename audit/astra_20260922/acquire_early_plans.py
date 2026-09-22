"""Recover pre-journal delivered plans only from their exact runtime commit."""
import concurrent.futures,gzip,json,pathlib,urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
need=[]
for p in (ROOT/'runtime').glob('*.gz'):
 d=json.load(gzip.open(p,'rt'));s=d['status']
 if s.get('email')=='DELIVERY_COMPLETED' and not s.get('entry_eur')and not s.get('deliveries'):need.append(d)
cache=ROOT/'early_states';cache.mkdir(exist_ok=True)
def one(d):
 p=cache/(d['sha']+'.json.gz')
 if p.exists():return
 u=f"https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/{d['sha']}/production_alert_state.json"
 data=json.load(urllib.request.urlopen(u,timeout=30));p.write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:list(pool.map(one,need))
print('states',len(need))
