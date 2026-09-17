import json
import multiprocessing
from pathlib import Path
import tempfile
import unittest
import urllib.error
from unittest.mock import patch
from research.api_budget import WeightedBudget, LIMIT, weight
from research.http import PublicClient


class Clock:
    def __init__(self): self.now=100.
    def time(self): return self.now
    def sleep(self, seconds): self.now+=seconds


class Response:
    headers={}
    def __enter__(self): return self
    def __exit__(self,*args): pass
    def read(self): return b'[]'


def reserve_process(path, start, result):
    budget=WeightedBudget(path)
    start.wait()
    import time
    try:
        budget.reserve(400,time.monotonic()+.2)
        result.put('reserved')
    except RuntimeError:
        result.put('deadline')


class ApiBudgetTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'budget.sqlite'
        self.clock=Clock()
        self.budget=WeightedBudget(self.path,clock=self.clock.time,sleeper=self.clock.sleep)

    def test_weighted_window_and_safety_reserve(self):
        self.budget.reserve(750)
        self.assertEqual(self.budget.reserve(25),61)
        self.assertEqual(LIMIT,750)
        self.assertEqual(weight('/ticker/24h'),25)

    def test_deadline_wait_does_not_spend_or_wait(self):
        self.budget.reserve(750)
        with self.assertRaisesRegex(RuntimeError,'DEADLINE'):self.budget.reserve(1,150)
        self.assertEqual(self.clock.now,100)
        with self.budget.connect() as db:self.assertEqual(db.execute('SELECT SUM(weight) FROM reservations').fetchone()[0],750)

    def test_processes_share_one_envelope(self):
        ctx=multiprocessing.get_context('spawn');start=ctx.Event();result=ctx.Queue()
        processes=[ctx.Process(target=reserve_process,args=(str(self.path),start,result)) for _ in range(2)]
        for p in processes:p.start()
        start.set()
        outcomes=[result.get(timeout=10) for _ in processes]
        for p in processes:p.join(10);self.assertEqual(p.exitcode,0)
        self.assertEqual(sorted(outcomes),['deadline','reserved'])

    def test_headers_can_only_tighten_not_refill(self):
        self.budget.reserve(750)
        self.budget.observe({'bitvavo-ratelimit-limit':'1000','bitvavo-ratelimit-remaining':'999','bitvavo-ratelimit-resetat':'130000'},now=100)
        self.assertEqual(self.budget.reserve(1),61)
        self.budget.observe({'bitvavo-ratelimit-limit':'1000','bitvavo-ratelimit-remaining':'200','bitvavo-ratelimit-resetat':'180000'},now=161)
        self.assertEqual(self.budget.reserve(1),20)

    def test_inconsistent_headers_are_ignored(self):
        for reset in ('99999','9999999999999','nan','invalid'):
            self.budget.observe({'bitvavo-ratelimit-limit':'1000','bitvavo-ratelimit-remaining':'0','bitvavo-ratelimit-resetat':reset},now=100)
        self.assertEqual(self.budget.reserve(1),0)

    def test_429_is_shared_cooldown_not_retry_storm(self):
        self.budget.observe({'Retry-After':'1000'},429,now=100)
        peer=WeightedBudget(self.path,clock=self.clock.time,sleeper=self.clock.sleep)
        with self.assertRaises(RuntimeError):peer.reserve(1,400)
        self.assertEqual(peer.reserve(1),1001)

    def client(self, **kwargs):
        return PublicClient(budget=self.budget,requests_per_second=100000,**kwargs)

    def test_each_retry_consumes_points(self):
        with patch('research.http.time.monotonic',self.clock.time),patch('research.http.time.sleep',self.clock.sleep):
            c=self.client()
            with patch('urllib.request.urlopen',side_effect=[urllib.error.URLError('temporary'),Response()]):c.get('/ticker/24h')
        with self.budget.connect() as db:self.assertEqual(db.execute('SELECT SUM(weight) FROM reservations').fetchone()[0],50)
        self.assertEqual(len(c.errors),1)

    def test_no_retry_after_429_and_other_client_waits(self):
        with patch('research.http.time.monotonic',self.clock.time),patch('research.http.time.sleep',self.clock.sleep):
            c=self.client()
            failure=urllib.error.HTTPError('url',429,'rate',{'Retry-After':'2'},None)
            with patch('urllib.request.urlopen',side_effect=failure) as network:
                with self.assertRaises(RuntimeError):c.get('/ticker/24h')
                self.assertEqual(network.call_count,1)
                with self.assertRaisesRegex(RuntimeError,'FRESHNESS'):self.client().get('/ticker/price')
                self.assertEqual(network.call_count,1)

    def test_response_after_freshness_deadline_is_not_cached(self):
        with patch('research.http.time.monotonic',self.clock.time):
            c=self.client(max_elapsed_seconds=5)
            def late(*args,**kwargs):
                self.assertLessEqual(kwargs['timeout'],5)
                self.clock.now+=6
                return Response()
            with patch('urllib.request.urlopen',side_effect=late):
                with self.assertRaisesRegex(RuntimeError,'FRESHNESS'):c.get('/ticker/price')
            self.assertFalse(c.records);self.assertFalse(c.cache)
            self.assertEqual(c.errors[-1]['error'],'COLLECTION_FRESHNESS_DEADLINE')

    def test_timeout_retry_cannot_extend_collection(self):
        with patch('research.http.time.monotonic',self.clock.time),patch('research.http.time.sleep',self.clock.sleep):
            c=self.client(max_elapsed_seconds=10)
            def slow(*args,**kwargs):
                self.clock.sleep(kwargs['timeout']);raise TimeoutError()
            with patch('urllib.request.urlopen',side_effect=slow) as network:
                with self.assertRaisesRegex(RuntimeError,'FRESHNESS'):c.get('/AAA-EUR/candles')
                self.assertEqual(network.call_count,1)
            self.assertEqual(self.clock.now,110)

    def test_deadline_preserves_complete_market_population(self):
        from pipeline import collect_universe
        with patch('research.http.time.monotonic',self.clock.time):
            c=self.client(max_elapsed_seconds=1);self.clock.now+=2
            with patch('urllib.request.urlopen') as network:
                rows=collect_universe(c,[{'market':m} for m in ('AAA-EUR','BBB-EUR')],{},0)
                network.assert_not_called()
        self.assertEqual(len(rows),2)
        self.assertTrue(all(len(r['errors'])==2 and all(e['reason']=='COLLECTION_FRESHNESS_DEADLINE' for e in r['errors']) for r in rows.values()))

    def test_last_attempt_timeout_is_classified_as_freshness_abandonment(self):
        with patch('research.http.time.monotonic',self.clock.time),patch('research.http.time.sleep',self.clock.sleep):
            c=self.client(max_elapsed_seconds=5,retries=1)
            def slow(*args,**kwargs):
                self.clock.sleep(kwargs['timeout']);raise TimeoutError()
            with patch('urllib.request.urlopen',side_effect=slow):
                with self.assertRaisesRegex(RuntimeError,'FRESHNESS'):c.get('/AAA-EUR/candles')
            self.assertEqual(c.errors[-1]['error'],'COLLECTION_FRESHNESS_DEADLINE')

    def test_http_date_retry_after_extends_cooldown(self):
        from email.utils import formatdate
        self.budget.observe({'Retry-After':formatdate(2100,usegmt=True)},429,now=100)
        self.assertEqual(self.budget.reserve(1),2001)

    def test_same_process_clients_share_transaction_mutex(self):
        peer=WeightedBudget(self.path,clock=self.clock.time,sleeper=self.clock.sleep)
        self.assertIs(peer._local_lock,self.budget._local_lock)
