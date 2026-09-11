import copy
import json
import unittest
from unittest.mock import patch
from research.common import utc
from research.http import PublicClient, ReplayClient


class Response:
    headers = {'Date': 'Fri, 11 Sep 2026 12:00:00 GMT'}
    def __init__(self, value): self.value = value
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self): return json.dumps(self.value).encode()


class TemporalTests(unittest.TestCase):
    def client(self):
        c = PublicClient(retries=1)
        c.pace = lambda: None
        return c

    def test_same_url_distinct_consumptions_replay_without_future_replacement(self):
        c = self.client()
        with patch('urllib.request.urlopen', side_effect=[Response({'p':1}), Response({'p':2})]):
            a = c.capture('/ticker/price', consumer_id='v4')
            b = c.capture('/ticker/price', cache=False, consumer_id='diagnostics')
            again = c.capture('/ticker/price', consumer_id='v4')
        self.assertNotEqual(a['response_id'], b['response_id'])
        self.assertEqual(a['data'], {'p':1})
        r = ReplayClient(c.records, c.consumptions, consumer_id='v4')
        self.assertEqual(r.get('/ticker/price'), a['data'])
        self.assertEqual(r.get('/ticker/price'), again['data'])
        with self.assertRaises(RuntimeError): r.get('/ticker/price')
        diag = ReplayClient(c.records, c.consumptions, consumer_id='diagnostics')
        self.assertEqual(diag.capture('/ticker/price'), b)

    def test_future_response_is_unavailable_even_for_old_market_bar(self):
        c = self.client()
        with patch('urllib.request.urlopen', return_value=Response([[0,1,2,1,1,1]])):
            with self.assertRaises(ValueError):
                c.capture('/AAA-EUR/candles', {'interval':'15m'}, cutoff=0, consumer_id='v4')
        self.assertEqual(c.consumptions, [])

    def test_content_and_metadata_are_copied_together(self):
        c = self.client()
        with patch('urllib.request.urlopen', return_value=Response({'p':1})):
            a = c.capture('/ticker/price')
            a['data']['p'] = 100
            a['retrieved_at_utc'] = 'wrong'
            b = c.capture('/ticker/price')
        self.assertEqual(b['data']['p'], 1)
        self.assertNotEqual(b['retrieved_at_utc'], 'wrong')

    def test_old_replay_still_reads_legacy_format(self):
        r = ReplayClient([{'path':'/ticker/price','params':{},'data':{'p':1}}])
        self.assertEqual(r.get('/ticker/price'), {'p':1})
        with self.assertRaises(RuntimeError): r.get('/markets')

    def test_consumer_identity_not_thread_completion_order(self):
        c = self.client()
        with patch('urllib.request.urlopen', side_effect=[Response({'p':1}),Response({'p':2})]):
            a = c.capture('/ticker/price', consumer_id='AAA')
            b = c.capture('/ticker/price', consumer_id='BBB', cache=False)
        r = ReplayClient(list(reversed(c.records)), list(reversed(c.consumptions)), consumer_id='AAA')
        self.assertEqual(r.capture('/ticker/price'), a)
