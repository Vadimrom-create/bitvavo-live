"""Offline regression tests for read-only candidate follow-up (#146)."""
import time
import unittest
from scripts import follow_active_candidates as f


def fixture_alert(sent=None):
    t = time.time() if sent is None else sent
    return {'markets': {'LPT-EUR': {
        'last_sent_ts': t, 'last_sent_entry_eur': 1.6328,
        'last_sent_stop_eur': 1.5034,
        'last_sent_profit_alert_eur': 1.8916,
        'alert_id': 'LPT-EUR:18:sent',
        'active': False, 'alert_lifecycle_reason': 'CANDIDATE_NO_LONGER_IN_LATEST_SCAN',
    }}}


def fixture_book():
    return {'bids': [['1.61', '2000'], ['1.60', '3000']],
            'asks': [['1.62', '3000'], ['1.63', '2000']]}


def observation(price, buy=0.4, green=False, red=False, rvol=2, liquid=True):
    return {
        'bid': price, 'ask': price*1.001, 'spread_pct': 0.1,
        'buy_taker_share': buy, 'two_green_5m': green,
        'two_red_5m': red, 'volume_ratio_5m': rvol,
        'bid_depth_1pct_eur': 2500 if liquid else 10,
        'buy_150_complete': True, 'sell_150_complete': True,
        'observed_at_utc': '2026-10-09T17:00:00+00:00',
    }


class CandidateFollowTests(unittest.TestCase):
    def test_register_preserves_sent_signal_after_latest_scan_drops_it(self):
        now = time.time()
        state = {'markets': {}}
        items = f.register(state, fixture_alert(now-120), now)
        self.assertIn('LPT-EUR', items)
        items['LPT-EUR']['status'] = 'WAIT_REBOUND'
        again = f.register(state, fixture_alert(now-120), now+60)
        self.assertEqual(again['LPT-EUR']['status'], 'WAIT_REBOUND')

    def test_old_signal_not_tracked(self):
        now = time.time()
        self.assertEqual(f.register({'markets': {}},
                                   fixture_alert(now-f.TRACK_SECONDS-60), now), {})

    def test_invalid_and_crossed_books_fail_closed(self):
        with self.assertRaises(ValueError):
            f.validated_levels({'bids': [['1.62', '50']],
                                'asks': [['1.61', '50']]})
        with self.assertRaises(ValueError):
            f.validated_levels({'bids': [], 'asks': []})
        bids, asks = f.validated_levels(fixture_book())
        self.assertEqual(bids[0][0], 1.61)
        self.assertEqual(asks[0][0], 1.62)

    def test_breakdown_needs_two_independent_observations(self):
        now = time.time()
        item = f.register({'markets': {}}, fixture_alert(now-120), now)['LPT-EUR']
        one = f.advance(item, observation(1.6075, red=True), now)
        self.assertIsNone(one)
        self.assertEqual(item['status'], 'ACTIVE')
        two = f.advance(item, observation(1.6075, red=True), now+60)
        self.assertEqual(two, 'BREAKDOWN')
        self.assertEqual(item['status'], 'BREAKDOWN')

    def test_reconfirmation_needs_pullback_volume_depth_and_two_green_candles(self):
        now = time.time()
        item = f.register({'markets': {}}, fixture_alert(now-120), now)['LPT-EUR']
        item['status'] = 'WAIT_REBOUND'
        item['min_seen_price'] = 1.6075
        self.assertEqual(f.classify(item, observation(1.62, buy=.61,
                                                      green=True, rvol=2)), 'RECONFIRMED')
        self.assertNotEqual(f.classify(item, observation(1.62, buy=.61,
                                                         green=True, liquid=False)), 'RECONFIRMED')
        self.assertNotEqual(f.classify(item, observation(1.62, buy=.61,
                                                         green=False)), 'RECONFIRMED')
        item['status'] = 'ACTIVE'
        self.assertNotEqual(f.classify(item, observation(1.62, buy=.61,
                                                         green=True)), 'RECONFIRMED')

    def test_stop_invalidation_immediate(self):
        now = time.time()
        item = f.register({'markets': {}}, fixture_alert(now-120), now)['LPT-EUR']
        alert = f.advance(item, observation(1.49), now)
        self.assertEqual(alert, 'INVALIDATED')
        self.assertEqual(item['status'], 'INVALIDATED')

    def test_no_duplicate_notice(self):
        now = time.time()
        item = f.register({'markets': {}}, fixture_alert(now-120), now)['LPT-EUR']
        f.advance(item, observation(1.6075, red=True), now)
        f.advance(item, observation(1.6075, red=True), now+60)
        item['last_notice'] = 'BREAKDOWN'
        item['last_notice_ts'] = now+60
        self.assertIsNone(f.advance(item, observation(1.6075, red=True), now+120))


if __name__ == '__main__':
    unittest.main()
