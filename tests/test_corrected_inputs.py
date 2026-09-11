import copy
import tempfile
from pathlib import Path
import unittest
from research.common import utc


def record(now, count=40, interval=86400):
    start = int(now//interval-count)*interval
    return {'response_id': 'r-'+str(now), 'request_started_at_utc': utc(now), 'retrieved_at_utc': utc(now+.2),
            'server_offset_seconds': 0., 'clock_uncertainty_seconds': 0.,
            'data': [[(start+i*interval)*1000, 100+i, 102+i, 99+i, 101+i, 100] for i in range(count)]}


class CorrectedInputTests(unittest.TestCase):
    def test_new_empty_market_does_not_refresh_other_market_clock(self):
        from research.trend_cache import TrendCache
        now=1800000000.
        calls=[]
        def fetch(m):
            calls.append(m)
            return record(now, 0 if m=='NEW-EUR' else 40)
        with tempfile.TemporaryDirectory() as d:
            cache=TrendCache(Path(d)/'cache.json', fetch)
            cache.refresh(['AAA-EUR','NEW-EUR'], now)
            acquired=cache.state['profiles']['AAA-EUR']['last_valid_acquisition_ts']
            now+=5400.2
            cache.refresh(['NEW-EUR'], now)
            cache.refresh(['AAA-EUR'], now)
            self.assertEqual(calls.count('AAA-EUR'), 2)
            self.assertGreater(cache.state['profiles']['AAA-EUR']['last_valid_acquisition_ts'], acquired)
            self.assertEqual(cache.state['profiles']['NEW-EUR']['status'], 'INSUFFICIENT_HISTORY')

    def test_failure_restart_expiry_and_dependency_freshness(self):
        from research.trend_cache import TrendCache
        now=1800000000.
        def fetch(m): return record(now)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'cache.json';cache=TrendCache(p, fetch)
            cache.refresh(['AAA-EUR','BTC-EUR','ETH-EUR'], now)
            def fail(m): raise RuntimeError('unavailable')
            cache=TrendCache(p, fail)
            old=cache.state['profiles']['BTC-EUR']['last_valid_acquisition_ts']
            cache.refresh(['BTC-EUR'], now+5401)
            self.assertEqual(cache.state['profiles']['BTC-EUR']['last_valid_acquisition_ts'], old)
            now+=10801
            cache.fetch=fetch
            result=cache.refresh(['AAA-EUR'], now)
            self.assertFalse(result['markets']['AAA-EUR']['dependencies_fresh'])
            self.assertNotIn('BTC-EUR', result['markets'])
            self.assertEqual(cache.state['profiles']['BTC-EUR']['status'], 'STALE')

    def test_source_close_not_later_read_or_http_date(self):
        from research.features import candles_from_response
        for started, received, later, expected in [(890,910,920,0),(910,915,1800,1)]:
            r=record(started,0)
            r.update(data=[[0,1,2,1,1,2]], retrieved_at_utc=utc(received), server_http_date=utc(later))
            self.assertEqual(len(candles_from_response(r,'15m')), expected)
        r['clock_uncertainty_seconds']=20
        self.assertEqual(candles_from_response(r,'15m'), [])

    def test_profile_formula_identical_for_same_closed_candles(self):
        from research.trend_cache import TrendCache
        from research.features import closed_candles
        from v4_common import daily_profile_from_candles
        now=1800000000.;r=record(now)
        expected=daily_profile_from_candles(closed_candles(r['data'],'1d',now))
        with tempfile.TemporaryDirectory() as d:
            result=TrendCache(Path(d)/'cache.json', lambda _:r).refresh(['AAA-EUR'],now)
            actual=result['markets']['AAA-EUR']
            self.assertEqual({k:actual[k] for k in expected}, expected)
