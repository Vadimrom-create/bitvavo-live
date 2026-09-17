"""Offline transport load scenarios against the real PublicClient and quota ledger.

No candles, signals or historical observations are generated. Virtual time only
replaces network duration/sleep; real threads and SQLite reservations are used.
The workload counts match the certified 1575-request scan; this is a saturation
stress, not a prediction of the sequential pipeline's wall duration.
"""
from collections import Counter
import json
from pathlib import Path
import tempfile
import threading
import urllib.error
import urllib.parse
from unittest.mock import patch
from research.api_budget import WeightedBudget, weight
from research.capacity_audit import rolling_peak
from research.http import PublicClient


class VirtualClock:
    def __init__(self, workers):
        self.now=0.;self.active=workers;self.waiting={};self.condition=threading.Condition()
    def time(self): return self.now
    def advance(self):
        if self.active and len(self.waiting)==self.active:
            self.now=max(self.now,min(self.waiting.values()))
            self.waiting={k:v for k,v in self.waiting.items() if v>self.now+1e-9}
            self.condition.notify_all()
    def sleep(self, delay):
        if delay<=0:return
        ident=threading.get_ident()
        with self.condition:
            self.waiting[ident]=self.now+delay
            self.advance()
            while ident in self.waiting:self.condition.wait()
    def done(self):
        with self.condition:
            self.active-=1;self.advance()


def workload():
    calls=[('/time',{}),('/markets',{}),('/ticker/24h',{}),('/ticker/24h',{}),
           ('/ticker/book',{}),('/ticker/book',{}),('/ticker/price',{})]
    for tf,limit,count in [('15m',100,430),('15m',40,60),('15m',50,64),('5m',50,90),('5m',100,430),
                            ('1h',40,60),('1h',50,64),('4h',40,60),('4h',50,64),('1d',95,108)]:
        calls.extend((f'/M{i}-EUR/candles',{'interval':tf,'limit':limit}) for i in range(count))
    for kind,count,params in [('book',102,{'depth':50}),('book',18,{'depth':100}),('trades',18,{'limit':100})]:
        calls.extend((f'/M{i}-EUR/{kind}',params) for i in range(count))
    assert len(calls)==1575 and sum(weight(*c) for c in calls)==1695
    return calls


def simulate(error_percent=0, timeouts=False, consumers=1):
    count=8*consumers;clock=VirtualClock(count);local=threading.local()
    lock=threading.Lock();attempts=[];completed=[];abandoned=[];failures=[];errors=[]
    rows=workload()
    jobs=[[(i,*row) for i,row in enumerate(rows)] for _ in range(consumers)]
    # Fixed shard assignments make incident placement reproducible regardless of
    # which OS thread acquires the SQLite transaction first.
    with tempfile.TemporaryDirectory() as d, patch('research.http.time.monotonic',clock.time), \
         patch('research.http.time.sleep',clock.sleep),patch('research.http.time.time',lambda:1800000000+clock.time()):
        clients=[PublicClient(budget=WeightedBudget(Path(d)/'shared.sqlite',clock=clock.time,sleeper=clock.sleep)) for _ in range(consumers)]
        class Response:
            headers={}
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self):return json.dumps({'time':(1800000000+clock.time())*1000} if local.path=='/time' else []).encode()
        def transport(request,timeout):
            local.attempt+=1
            params=dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(request.full_url).query))
            incident=((local.job*37)%100)<error_percent and local.attempt <= (2 if timeouts else 1)
            row={'started_epoch':clock.time(),'weight':weight(local.path,params), 'retry':local.attempt>1,
                 'timeout':bool(incident and timeouts),'status':None if incident else 200}
            with lock:attempts.append(row)
            clock.sleep(min(timeout,12 if incident and timeouts else .25))
            if incident:
                if timeouts:raise TimeoutError('SIMULATED')
                raise urllib.error.URLError('SIMULATED_FAST_ERROR')
            return Response()
        def worker(consumer,worker_id):
            try:
                client=clients[consumer]
                for i,path,params in jobs[consumer][worker_id::8]:
                    local.job=i;local.path=path;local.attempt=0
                    try:
                        client.get(path,params,cache=False)
                        with lock:completed.append((consumer,path,params,clock.time()))
                    except RuntimeError as exc:
                        with lock:
                            (abandoned if 'DEADLINE' in str(exc) else failures).append((consumer,i,str(exc)))
            except Exception as exc:
                with lock:errors.append(repr(exc))
            finally:clock.done()
        with patch('urllib.request.urlopen',transport):
            threads=[threading.Thread(target=worker,args=(c,w)) for c in range(consumers) for w in range(8)]
            for t in threads:t.start()
            for t in threads:t.join(60)
            if any(t.is_alive() for t in threads):raise AssertionError('SIMULATION_DEADLOCK')
        if errors:raise AssertionError(errors)
        pairs=Counter((c,p) for c,p,q,t in completed if p.endswith('/candles') and q in ({'interval':'5m','limit':100},{'interval':'15m','limit':100}))
        peak=rolling_peak(attempts)['weight']
        return {'scope':'OFFLINE_TRANSPORT_STRESS_NOT_LIVE_COVERAGE', 'consumers':consumers,'markets_requested':430*consumers,
                'requests':len(attempts),'points':sum(a['weight'] for a in attempts),'peak_60s_points':peak,
                'margin_points':1000-peak,'duration_seconds':round(clock.time(),3),
                'retry_attempts':sum(a['retry'] for a in attempts),'timeouts':sum(a['timeout'] for a in attempts),'http_429':0,
                'freshness_abandoned_calls':len(abandoned),'other_failed_calls':len(failures),'completed_calls':len(completed),
                'markets_both_timeframes_completed':sum(n==2 for n in pairs.values()),
                'responses_older_than_300s_at_end':sum(clock.time()-t>300 for _,_,_,t in completed),
                'maximum_response_age_at_end':round(max((clock.time()-t for _,_,_,t in completed),default=0),3)}
