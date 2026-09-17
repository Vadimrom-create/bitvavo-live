import io
import unittest
import urllib.error
import urllib.request
from email.message import Message
from unittest.mock import patch
from research.capacity_audit import Audit, weight, rolling_peak
from research.http import PublicClient


class Response(io.BytesIO):
    status = 200
    headers = {'bitvavo-ratelimit-limit': '1000', 'bitvavo-ratelimit-remaining': '950',
               'bitvavo-ratelimit-resetat': '9999999999999'}


class CapacityAuditTests(unittest.TestCase):
    def test_official_weights(self):
        self.assertEqual(weight('/ticker/24h'),25)
        self.assertEqual(weight('/ticker/24h',{'market':'BTC-EUR'}),1)
        self.assertEqual(weight('/BTC-EUR/trades'),5)
        self.assertEqual(weight('/BTC-EUR/candles'),1)

    def test_weighted_rolling_not_calendar_minutes(self):
        result=rolling_peak([{'started_epoch':t,'weight':w} for t,w in [(59,25),(61,5),(119,1)]])
        self.assertEqual(result['weight'],30)
        self.assertEqual(result['requests'],2)
        self.assertEqual(rolling_peak([])['weight'],0)

    def test_cache_and_atomic_response_unchanged(self):
        with patch('urllib.request.urlopen',side_effect=lambda *a,**k:Response(b'[]')):
            client=PublicClient(requests_per_second=100000)
            with Audit().observe() as audit:
                first=client.capture('/ticker/24h')
                second=client.capture('/ticker/24h')
            self.assertEqual(first,second)
            r=audit.result()
            self.assertEqual(r['summary']['http_attempts'],1)
            self.assertEqual(r['summary']['cache_only_calls'],1)
            self.assertEqual(r['summary']['weight_total'],25)
            self.assertEqual(r['attempts'][0]['headers']['bitvavo-ratelimit-remaining'],'950')
            self.assertNotIn('headers',first)

    def test_retry_failure_headers_and_restore(self):
        headers=Message();headers['Retry-After']='2'
        failure=urllib.error.HTTPError('https://api.bitvavo.com/v2/time',500,'error',headers,None)
        with patch('urllib.request.urlopen',side_effect=[failure,Response(b'[]')]) as transport, patch('research.http.time.sleep'):
            with Audit().observe() as audit:
                PublicClient(requests_per_second=100000).get('/markets')
            self.assertIs(urllib.request.urlopen,transport)
        r=audit.result()
        self.assertEqual(r['summary']['retry_attempts'],1)
        self.assertEqual(r['attempts'][0]['status'],500)
        self.assertEqual(r['attempts'][0]['headers']['retry-after'],'2')

    def test_timeout_count_and_failure_propagation(self):
        with patch('urllib.request.urlopen',side_effect=TimeoutError):
            with Audit().observe() as audit:
                with self.assertRaises(RuntimeError):PublicClient(retries=1).get('/time')
        self.assertEqual(audit.result()['summary']['timeouts'],1)

    def test_deadline_before_network_is_not_http_attempt(self):
        with patch('urllib.request.urlopen') as transport:
            with Audit().observe() as audit:
                with self.assertRaises(RuntimeError):PublicClient().capture('/time',deadline=0)
            transport.assert_not_called()
        self.assertEqual(audit.result()['summary']['http_attempts'],0)
        self.assertEqual(audit.calls[0]['reason'],'OPTIONAL_COLLECTION_DEADLINE')

    def test_private_auth_rejected(self):
        with Audit().observe():
            with self.assertRaisesRegex(ValueError,'AUDIT_NO_PRIVATE_AUTH'):
                urllib.request.urlopen(urllib.request.Request('https://api.bitvavo.com/v2/time',headers={'Bitvavo-Access-Key':'test'}))
