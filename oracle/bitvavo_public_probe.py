#!/usr/bin/env python3
import json,re,time,urllib.parse,urllib.request,threading,os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from decimal import Decimal
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

BASE='https://api.bitvavo.com/v2'
PORT=8787
MARKET_RE=re.compile(r'^[A-Z0-9]{2,20}-EUR
def now_iso(): return datetime.now(timezone.utc).isoformat()
def D(x): return Decimal(str(x))

def get(path,params=None):
    url=BASE+path
    if params: url+='?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'bitvavo-public-probe/1.0'})
    t=time.monotonic()
    with urllib.request.urlopen(req,timeout=5) as r:
        data=json.loads(r.read().decode())
    return data,round((time.monotonic()-t)*1000,1)

def depth_eur(levels):
    return sum((D(p)*D(a) for p,a in levels),Decimal('0'))

def slippage(asks,stake):
    rem=D(stake); spent=Decimal('0'); base=Decimal('0')
    for p,a in asks:
        p=D(p); a=D(a); avail=p*a; take=min(rem,avail)
        if take>0:
            spent+=take; base+=take/p; rem-=take
        if rem<=0: break
    if base<=0: return {'stake_eur':float(stake),'fillable':False,'avg_price':None,'slippage_pct':None}
    avg=spent/base; best=D(asks[0][0]); slip=(avg/best-1)*100
    return {'stake_eur':float(stake),'fillable':rem<=Decimal('0.000001'),'avg_price':float(avg),'slippage_pct':float(slip),'unfilled_eur':float(max(rem,Decimal('0')))}

def flow(trades):
    buy=sell=Decimal('0')
    for t in trades:
        n=D(t['price'])*D(t['amount'])
        if t.get('side')=='buy': buy+=n
        elif t.get('side')=='sell': sell+=n
    total=buy+sell
    return {'trade_count':len(trades),'buy_eur':float(buy),'sell_eur':float(sell),'buy_share_eur':float(buy/total) if total else None,'latest_trade_timestamp_ms':trades[0].get('timestamp') if trades else None,'oldest_trade_timestamp_ms':trades[-1].get('timestamp') if trades else None}

def quote(market,stake):
    # The four upstream reads are independent. Running them in parallel keeps a
    # degraded Bitvavo endpoint from holding one server thread for ~20 seconds.
    with ThreadPoolExecutor(max_workers=4) as pool:
        fp=pool.submit(get,'/ticker/price',{'market':market})
        ft=pool.submit(get,'/ticker/book',{'market':market})
        fb=pool.submit(get,f'/{market}/book',{'depth':10})
        fr=pool.submit(get,f'/{market}/trades',{'limit':50})
        price,t1=fp.result(); tick,t2=ft.result(); book,t3=fb.result(); trades,t4=fr.result()
    bids=book.get('bids',[])[:10]; asks=book.get('asks',[])[:10]
    bid=D(tick['bid']); ask=D(tick['ask']); mid=(bid+ask)/2
    spread=((ask-bid)/mid*100) if mid else None
    bd=depth_eur(bids); ad=depth_eur(asks); total=bd+ad
    return {'ok':True,'timestamp_utc':now_iso(),'source':'bitvavo_public','market':market,'last_trade_price':price.get('price'),'best_bid':tick.get('bid'),'best_ask':tick.get('ask'),'spread_pct':float(spread) if spread is not None else None,'best_10_bids':bids,'best_10_asks':asks,'near_depth':{'bid_eur_top10':float(bd),'ask_eur_top10':float(ad),'imbalance':float((bd-ad)/total) if total else None},'buy_slippage':slippage(asks,stake),'recent_public_trade_flow':flow(trades),'exchange_book_timestamp':book.get('timestamp'),'latency_ms':{'price':t1,'ticker_book':t2,'order_book':t3,'trades':t4,'total':round(t1+t2+t3+t4,1)}}

class H(BaseHTTPRequestHandler):
    def sendj(self,code,obj):
        raw=json.dumps(obj,separators=(',',':')).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        global ACTIVE_QUOTES
        u=urllib.parse.urlparse(self.path)
        if u.path=='/health':
            with COUNTER_LOCK: active=ACTIVE_QUOTES
            load1=None
            try: load1=round(os.getloadavg()[0],3)
            except Exception: pass
            return self.sendj(200,{'ok':True,'service':'bitvavo-public-probe','version':2,'timestamp_utc':now_iso(),'uptime_seconds':round(time.time()-STARTED,1),'active_quotes':active,'max_concurrent_quotes':MAX_CONCURRENT_QUOTES,'loadavg_1m':load1})
        if u.path!='/quote': return self.sendj(404,{'ok':False,'error':'not_found'})
        q=urllib.parse.parse_qs(u.query); market=q.get('market',[''])[0].upper()
        if not MARKET_RE.fullmatch(market): return self.sendj(400,{'ok':False,'error':'invalid_market'})
        if not QUOTE_SLOTS.acquire(timeout=.25):
            return self.sendj(503,{'ok':False,'timestamp_utc':now_iso(),'error':'busy','retry_after_seconds':1})
        with COUNTER_LOCK: ACTIVE_QUOTES+=1
        try:
            stake=D(q.get('stake_eur',['75'])[0])
            if stake<1 or stake>10000: raise ValueError('stake_eur_out_of_range')
            return self.sendj(200,quote(market,stake))
        except Exception as e:
            return self.sendj(502,{'ok':False,'timestamp_utc':now_iso(),'error':type(e).__name__,'detail':str(e)[:300]})
        finally:
            with COUNTER_LOCK: ACTIVE_QUOTES-=1
            QUOTE_SLOTS.release()
    def log_message(self,fmt,*args): pass

class ProbeServer(ThreadingHTTPServer):
    daemon_threads=True
    block_on_close=False
    request_queue_size=64

ProbeServer(('0.0.0.0',PORT),H).serve_forever()
)
MAX_CONCURRENT_QUOTES=8
QUOTE_SLOTS=threading.BoundedSemaphore(MAX_CONCURRENT_QUOTES)
COUNTER_LOCK=threading.Lock()
ACTIVE_QUOTES=0
STARTED=time.time()

def now_iso(): return datetime.now(timezone.utc).isoformat()
def D(x): return Decimal(str(x))

def get(path,params=None):
    url=BASE+path
    if params: url+='?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'bitvavo-public-probe/1.0'})
    t=time.monotonic()
    with urllib.request.urlopen(req,timeout=5) as r:
        data=json.loads(r.read().decode())
    return data,round((time.monotonic()-t)*1000,1)

def depth_eur(levels):
    return sum((D(p)*D(a) for p,a in levels),Decimal('0'))

def slippage(asks,stake):
    rem=D(stake); spent=Decimal('0'); base=Decimal('0')
    for p,a in asks:
        p=D(p); a=D(a); avail=p*a; take=min(rem,avail)
        if take>0:
            spent+=take; base+=take/p; rem-=take
        if rem<=0: break
    if base<=0: return {'stake_eur':float(stake),'fillable':False,'avg_price':None,'slippage_pct':None}
    avg=spent/base; best=D(asks[0][0]); slip=(avg/best-1)*100
    return {'stake_eur':float(stake),'fillable':rem<=Decimal('0.000001'),'avg_price':float(avg),'slippage_pct':float(slip),'unfilled_eur':float(max(rem,Decimal('0')))}

def flow(trades):
    buy=sell=Decimal('0')
    for t in trades:
        n=D(t['price'])*D(t['amount'])
        if t.get('side')=='buy': buy+=n
        elif t.get('side')=='sell': sell+=n
    total=buy+sell
    return {'trade_count':len(trades),'buy_eur':float(buy),'sell_eur':float(sell),'buy_share_eur':float(buy/total) if total else None,'latest_trade_timestamp_ms':trades[0].get('timestamp') if trades else None,'oldest_trade_timestamp_ms':trades[-1].get('timestamp') if trades else None}

def quote(market,stake):
    price,t1=get('/ticker/price',{'market':market})
    tick,t2=get('/ticker/book',{'market':market})
    book,t3=get(f'/{market}/book',{'depth':10})
    trades,t4=get(f'/{market}/trades',{'limit':50})
    bids=book.get('bids',[])[:10]; asks=book.get('asks',[])[:10]
    bid=D(tick['bid']); ask=D(tick['ask']); mid=(bid+ask)/2
    spread=((ask-bid)/mid*100) if mid else None
    bd=depth_eur(bids); ad=depth_eur(asks); total=bd+ad
    return {'ok':True,'timestamp_utc':now_iso(),'source':'bitvavo_public','market':market,'last_trade_price':price.get('price'),'best_bid':tick.get('bid'),'best_ask':tick.get('ask'),'spread_pct':float(spread) if spread is not None else None,'best_10_bids':bids,'best_10_asks':asks,'near_depth':{'bid_eur_top10':float(bd),'ask_eur_top10':float(ad),'imbalance':float((bd-ad)/total) if total else None},'buy_slippage':slippage(asks,stake),'recent_public_trade_flow':flow(trades),'exchange_book_timestamp':book.get('timestamp'),'latency_ms':{'price':t1,'ticker_book':t2,'order_book':t3,'trades':t4,'total':round(t1+t2+t3+t4,1)}}

class H(BaseHTTPRequestHandler):
    def sendj(self,code,obj):
        raw=json.dumps(obj,separators=(',',':')).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        u=urllib.parse.urlparse(self.path)
        if u.path=='/health': return self.sendj(200,{'ok':True,'service':'bitvavo-public-probe','timestamp_utc':now_iso()})
        if u.path!='/quote': return self.sendj(404,{'ok':False,'error':'not_found'})
        q=urllib.parse.parse_qs(u.query); market=q.get('market',[''])[0].upper()
        if not MARKET_RE.fullmatch(market): return self.sendj(400,{'ok':False,'error':'invalid_market'})
        try:
            stake=D(q.get('stake_eur',['75'])[0])
            if stake<1 or stake>10000: raise ValueError('stake_eur_out_of_range')
            return self.sendj(200,quote(market,stake))
        except Exception as e:
            return self.sendj(502,{'ok':False,'timestamp_utc':now_iso(),'error':type(e).__name__,'detail':str(e)[:300]})
    def log_message(self,fmt,*args): pass

ThreadingHTTPServer(('0.0.0.0',PORT),H).serve_forever()
