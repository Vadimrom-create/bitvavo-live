import copy
import unittest
from unittest.mock import patch
from research.common import utc
from research.surveillance import candle_window, observe, collect_public_watch
from scripts.measure_public_coverage import summarize, INTERVALS

NOW = 1800000000


def source(data, identity='source'):
    return {'data': data, 'response_id': identity, 'request_started_at_utc': utc(NOW),
            'retrieved_at_utc': utc(NOW), 'clock_uncertainty_seconds': 0, 'server_offset_seconds': 0}


def candles(interval='5m'):
    span=INTERVALS[interval];end=NOW*1000//span*span
    return [[end-i*span,1,1,1,1,1] for i in range(1,31)]


class PublicSurveillanceTests(unittest.TestCase):
    def setUp(self):
        self.markets=[{'market':'AAA-EUR'},{'market':'BBB-EUR'}]
        self.tickers=source([{'market':m['market'],'last':'1','open':'.9','volumeQuote':'100'} for m in self.markets],'ticker')
        self.books=source([{'market':m['market'],'bid':'.99','ask':'1.01'} for m in self.markets],'book')

    def test_four_native_intervals_and_no_trade_holes_are_not_collection_failures(self):
        for interval in INTERVALS:
            r=source(candles(interval));before=copy.deepcopy(r)
            self.assertTrue(summarize(r,interval,NOW)['usable'])
            self.assertEqual(r,before)
            r['data'].pop(3)
            d=summarize(r,interval,NOW)
            self.assertTrue(d['response_obtained']);self.assertFalse(d['usable'])
            self.assertEqual(d['primary_reason'],'SOURCE_CANDLE_GAPS')

    def test_absence_grid_has_no_prices_or_volume_and_preserves_source(self):
        raw=candles();raw.pop(3)
        tf={'source':source(raw),'candles':[dict(zip(('t','o','h','l','c','v'),r)) for r in reversed(raw)]}
        before=copy.deepcopy(tf);window=candle_window(tf,'5m')
        self.assertEqual(len(window['missing_slots']),1)
        self.assertEqual(window['missing_slots'][0]['status'],'ABSENT_FROM_SUCCESSFUL_SOURCE')
        self.assertFalse(set(window['missing_slots'][0]) & {'o','h','l','c','v'})
        self.assertEqual(tf,before);self.assertFalse(window['synthetic_candles'])

    def test_short_empty_and_failed_responses_do_not_prove_no_trade(self):
        self.assertEqual(candle_window({},'5m')['inference'],'UNKNOWN')
        self.assertTrue(all(not s['no_trade_inferred'] for s in candle_window({'source':source([]),'candles':[]},'5m')['missing_slots']))
        row=dict(zip(('t','o','h','l','c','v'),candles()[0]))
        window=candle_window({'source':source([]),'candles':[row]},'5m')
        self.assertTrue(all(s['status']=='OUTSIDE_RETURNED_HISTORY' for s in window['missing_slots']))

    def test_entire_universe_observed_despite_zero_optional_enrichment_budget(self):
        from pipeline import collect_universe
        from research.http import PublicClient
        client=PublicClient()
        with patch('pipeline.time.monotonic',return_value=100),patch('urllib.request.urlopen') as network:
            universe=collect_universe(client,self.markets,{},NOW,budget_seconds=0)
        network.assert_not_called()
        with patch.object(client,'capture',side_effect=[self.tickers,self.books]) as capture,patch('time.time',return_value=NOW):
            result=collect_public_watch(client,self.markets,universe)
        self.assertEqual(result['status_counts'],{'PUBLIC_MARKET_WATCH':2})
        self.assertTrue(all(o['candle_collection_errors'] for o in result['markets']))
        self.assertTrue(all('deadline' not in c.kwargs for c in capture.call_args_list))

    def test_missing_api_data_is_not_counted_as_surveillance(self):
        result=observe(self.markets,{},None,None,NOW)
        self.assertEqual(result['status_counts'],{'PUBLIC_SNAPSHOT_UNAVAILABLE':2})
        self.assertTrue(all('MISSING_BOOK' in r['reasons'] for r in result['markets']))

    def test_crossed_nonfinite_and_stale_quotes_are_refused(self):
        for bad in ('nan','inf','-1','2'):
            with self.subTest(bad=bad):
                books=copy.deepcopy(self.books);books['data'][0]['bid']=bad
                r=observe(self.markets,{},self.tickers,books,NOW)['markets'][0]
                self.assertIn('INVALID_OR_CROSSED_BOOK',r['reasons'])
        result=observe(self.markets,{},self.tickers,self.books,NOW+301)
        self.assertEqual(result['status_counts'],{'PUBLIC_SNAPSHOT_UNAVAILABLE':2})

    def test_missing_new_market_is_explicit_and_never_activates_decision(self):
        self.markets.append({'market':'NEW-EUR'})
        result=observe(self.markets,{},self.tickers,self.books,NOW)
        self.assertEqual(len(result['markets']),3)
        self.assertEqual(result['markets'][-1]['status'],'PUBLIC_SNAPSHOT_UNAVAILABLE')
        self.assertTrue(all(not o['active_alerts_enabled'] and not o['fixed_period_trading_eligibility_changed'] for o in result['markets']))

    def test_bulk_failure_keeps_every_market_and_records_actual_error(self):
        from research.http import PublicClient
        with patch.object(PublicClient,'capture',side_effect=[RuntimeError('HTTP_429'),self.books]),patch('time.time',return_value=NOW):
            result=collect_public_watch(PublicClient(),self.markets,{})
        self.assertEqual(len(result['markets']),2)
        self.assertEqual(result['collection_errors'],[{'source':'ticker','reason':'HTTP_429'}])


if __name__=='__main__':unittest.main()
