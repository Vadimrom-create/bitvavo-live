from __future__ import annotations

import ast
import copy
import hashlib
import json
import math
from pathlib import Path
import tempfile
import unittest

from email_alert_v4 import select_events, MARKET_COOLDOWN
from research.common import freshness, timestamp, utc, atomic_json, read_json
from research.features import closed_candles, describe, chase_risk, wick_setup, category
from research.history import connect, ingest, recurrent, save_scan
from research.evaluation import outcome, evaluate, simulate_trade, before_move
from research.risk import plan, proposed_order, execute, correlation
from research.http import ReplayClient, PublicClient

ROOT = Path(__file__).resolve().parents[1]
NOW = 1_788_883_200.0  # exact timeframe boundary
NOW = math.floor(NOW / 900) * 900


def candles(n=100, interval=900_000, start=None):
    start = int(NOW * 1000) - n * interval if start is None else start
    return [{'t': start + i * interval, 'o': 100 + i * .02, 'h': 101 + i * .02,
             'l': 99 + i * .02, 'c': 100.5 + i * .02, 'v': 100 + i} for i in range(n)]


def raw(cs):
    return [[r[k] for k in ('t', 'o', 'h', 'l', 'c', 'v')] for r in cs]


def buy_payload(now=NOW):
    return {'generated_at_utc': utc(now), 'watch': [{'market': 'TEST-EUR', 'buy_ready': True,
            'action_status': 'REENTRY_READY', 'opportunity_score': 9, 'entry_score': 8}]}


class FreshnessTests(unittest.TestCase):
    def test_open_timestamp_is_not_close_timestamp(self):
        self.assertTrue(freshness(now=NOW + 840, retrieved=utc(NOW + 830), candle_start_ms=int(NOW - 900) * 1000)['ok'])

    def test_missing_latest_closed_candle(self):
        self.assertFalse(freshness(now=NOW + 960, retrieved=utc(NOW + 950), candle_start_ms=int(NOW - 900) * 1000)['ok'])

    def test_clock_future_and_stale(self):
        self.assertFalse(freshness(now=NOW, retrieved=utc(NOW + 60))['ok'])
        self.assertFalse(freshness(now=NOW, retrieved=utc(NOW - 301))['ok'])
        self.assertFalse(freshness(now=NOW, retrieved=None)['ok'])

    def test_no_naive_or_nan_timestamp(self):
        for value in ('2026-09-08T10:00:00', float('nan')):
            with self.assertRaises(ValueError): timestamp(value)


class FeatureTests(unittest.TestCase):
    def test_excludes_open_candle_and_orders(self):
        cs = raw(candles())
        cs.append([int(NOW * 1000), 100, 900, 1, 800, 1e9])
        clean = closed_candles(list(reversed(cs)), '15m', NOW + 60)
        self.assertEqual(len(clean), 100)
        self.assertLess(describe(clean, '15m')['return_1bar_pct'], 1)

    def test_invalid_ohlcv(self):
        for value in ([int(NOW * 1000)-900000, 100, 90, 95, 100, 1],
                      [int(NOW * 1000)-900000, 100, 101, 99, float('nan'), 1]):
            with self.assertRaises(ValueError): closed_candles([value], '15m', NOW)

    def test_gaps_not_filled_with_invented_trades(self):
        cs = candles(); cs.pop(-5)
        self.assertFalse(describe(cs, '15m')['valid'])

    def test_atr(self):
        f = describe(candles(), '15m')
        self.assertAlmostEqual(f['atr14_eur'], 2)
        self.assertGreater(f['volume_4_vs_prev4'], 1)

    def test_wicks_are_not_automatic_rejection(self):
        f = describe(candles(), '15m'); f['upper_wick_max'] = .9
        row = {'quote_volume_24h_eur': 1e6, 'spread_pct': .05}
        self.assertEqual(wick_setup(f, row)['status'], 'POTENTIALLY_EXPLOITABLE')
        row['quote_volume_24h_eur'] = 500
        self.assertEqual(wick_setup(f, row)['status'], 'DANGEROUS_STRUCTURE')

    def test_chase_no_scoring_mutation(self):
        f = describe(candles(), '15m'); before = copy.deepcopy(f)
        self.assertEqual(chase_risk(f, 30)['score'], 10)
        self.assertEqual(f, before)
        self.assertEqual(category({'buy_ready': True, 'risk_flags': ['CHASE_RISK']}), 'TOO LATE')


class AlertTests(unittest.TestCase):
    def test_empty_never_sends(self):
        self.assertFalse(select_events({'generated_at_utc': utc(NOW), 'watch': []}, {}, NOW)[0])

    def test_identical_reentry_never_bypasses_cooldown(self):
        state = {'markets': {'TEST-EUR': {'last_sent_ts': NOW-1801, 'active': True, 'episode': 1,
                 'sent_episode': 1, 'opportunity': 9, 'entry': 8, 'status': 'REENTRY_READY'}}}
        self.assertFalse(select_events(buy_payload(), state, NOW)[0])
        self.assertFalse(select_events(buy_payload(NOW+20000), state, NOW+20000)[0])

    def test_new_episode_after_empty_and_cooldown(self):
        state = {'markets': {'TEST-EUR': {'last_sent_ts': NOW-MARKET_COOLDOWN-1, 'active': True,
                 'episode': 1, 'sent_episode': 1, 'opportunity': 9, 'entry': 8}}}
        _, state = select_events({'generated_at_utc': utc(NOW), 'watch': []}, state, NOW)
        self.assertEqual(len(select_events(buy_payload(), state, NOW)[0]), 1)

    def test_stale_future_and_invalid_data(self):
        self.assertFalse(select_events(buy_payload(NOW-1000), {}, NOW)[0])
        self.assertFalse(select_events(buy_payload(NOW+1000), {}, NOW)[0])
        p = buy_payload(); p['watch'][0]['data_quality'] = {'ok': False}
        self.assertFalse(select_events(p, {}, NOW)[0])

    def test_failed_send_remains_retryable(self):
        events, state = select_events(buy_payload(), {}, NOW)
        self.assertTrue(events)
        self.assertTrue(select_events(buy_payload(), state, NOW)[0])


class RiskTests(unittest.TestCase):
    def setUp(self):
        self.row = {'market': 'TEST-EUR', 'ask': 105}
        self.features = describe(candles(), '15m')
        self.meta = {'tickSize': '.01', 'quantityDecimals': 4, 'minOrderInQuoteAsset': '5', 'minOrderInBaseAsset': '.0001'}

    def test_structural_stop_and_round_down(self):
        p = plan(self.row, self.features, self.meta)
        self.assertTrue(p['valid'])
        self.assertLess(p['stop_eur'], self.features['support_eur'])
        self.assertLessEqual(p['stake_eur'], 250)
        self.assertLessEqual(p['theoretical_loss_eur'], 12)
        self.assertGreater(p['tp2_eur'], p['tp1_eur'])
        self.assertGreater(p['tp1_eur'], p['entry_eur'])

    def test_cumulative_portfolio_caps(self):
        p = plan(self.row, self.features, self.meta, reserved={'exposure': 699, 'risk': 0, 'positions': 1})
        self.assertFalse(p['valid'])
        p = plan(self.row, self.features, self.meta, reserved={'exposure': 0, 'risk': 24, 'positions': 1})
        self.assertFalse(p['valid'])
        p = plan(self.row, self.features, self.meta, reserved={'exposure': 0, 'risk': 0, 'positions': 3})
        self.assertFalse(p['valid'])

    def test_very_wide_stop_reduces_size(self):
        a = plan(self.row, self.features, self.meta)
        self.features['support_eur'] = 80
        b = plan(self.row, self.features, self.meta)
        self.assertLess(b['stake_eur'], a['stake_eur'])
        self.assertLessEqual(b['theoretical_loss_eur'], 12)

    def test_dry_run_and_live_block(self):
        self.assertFalse(execute()['submitted'])
        with self.assertRaises(PermissionError): execute(dry_run=False)
        p = plan(self.row, self.features, self.meta)
        order = proposed_order(p, 'test')
        self.assertTrue(order['requires_human_approval'])
        self.assertEqual(order['status'], 'PROPOSED_REQUIRES_HUMAN_APPROVAL')

    def test_missing_market_metadata_fails_closed(self):
        self.assertFalse(plan(self.row, self.features, {})['valid'])

    def test_correlation_uses_matching_times(self):
        cs = candles()
        self.assertAlmostEqual(correlation(cs, cs), 1)
        self.assertIsNone(correlation(cs[:5], cs))


def sample_scan(ts=NOW, sid='a', detected=False, buy=False):
    return {'scan_id': sid, 'scan_ts': ts, 'scan_at_utc': utc(ts), 'policy': 'V4_FROZEN', 'observations': [
        {'market': 'TEST-EUR', 'price_eur': 100, 'decision': 'SURVEILLE' if detected else 'NO SETUP',
         'category': 'PRE-IGNITION' if detected else 'NO SETUP',
         'baseline': {'action_status': 'BUY_READY' if buy else 'WATCH' if detected else 'NONE', 'buy_ready': buy},
         'exclusions': []}], 'candles_5m': {}}


class HistoryEvaluationTests(unittest.TestCase):
    def setUp(self): self.db = connect()
    def tearDown(self): self.db.close()

    def test_idempotent_ingestion(self):
        scan = sample_scan(); ingest(self.db, scan); ingest(self.db, scan)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM observations').fetchone()[0], 1)

    def test_recurring_deduplicates_same_15m_period(self):
        ingest(self.db, sample_scan(NOW, 'a', True))
        ingest(self.db, sample_scan(NOW+60, 'b', True))
        r = recurrent(self.db, 'TEST-EUR', NOW+120, 'PRE-IGNITION')
        self.assertFalse(r['recurrent'])
        r = recurrent(self.db, 'TEST-EUR', NOW+901, 'IGNITION')
        self.assertTrue(r['recurrent'])

    def test_missing_future_is_not_false_positive(self):
        ingest(self.db, sample_scan(buy=True))
        ev = evaluate(self.db)
        self.assertEqual(ev['by_horizon']['4h']['censored'], 1)
        self.assertIsNone(ev['by_horizon']['4h']['thresholds']['5']['precision_buy'])

    def test_false_negative_and_mae_before_target(self):
        s = sample_scan()
        cs = candles(48, 300000, int(NOW*1000))
        for c in cs: c.update(o=100, h=106, l=99, c=105)
        s['candles_5m'] = {'TEST-EUR': cs}; ingest(self.db, s)
        ev = evaluate(self.db)
        self.assertEqual(ev['by_horizon']['4h']['thresholds']['5']['fn'], 1)
        self.assertTrue(ev['false_negative_examples'])

    def test_adverse_before_gain_not_useful_recall(self):
        s = sample_scan()
        cs = candles(48, 300000, int(NOW*1000))
        for c in cs: c.update(o=100, h=106, l=88, c=105)
        s['candles_5m'] = {'TEST-EUR': cs}; ingest(self.db, s)
        ev = evaluate(self.db)
        self.assertEqual(ev['by_horizon']['4h']['thresholds']['5']['fn'], 0)
        self.assertEqual(ev['by_horizon']['4h']['thresholds']['5']['tn'], 1)

    def test_partial_pre_signal_bar_does_not_leak(self):
        s = sample_scan(NOW+30)
        cs = candles(4, 300000, int(NOW*1000))
        cs[0]['h'] = 500
        s['candles_5m'] = {'TEST-EUR': cs}; ingest(self.db, s)
        obs = self.db.execute('SELECT * FROM observations').fetchone()
        f = outcome(self.db, obs, 900)
        self.assertEqual(f['status'], 'COMPLETE')
        self.assertLess(f['mfe_pct'], 5)

    def test_lookback_never_picks_future_scan(self):
        ingest(self.db, sample_scan(NOW+10, 'future', True))
        self.assertEqual(before_move(self.db, 'TEST-EUR', NOW+900)['lookbacks']['15m']['status'], 'UNOBSERVED')

    def test_corrupt_journal_does_not_reset_history(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/'bad.json'; path.write_text('{broken')
            with self.assertRaises(json.JSONDecodeError): read_json(path)

    def test_immutable_journal(self):
        with tempfile.TemporaryDirectory() as d:
            s = sample_scan(); save_scan(d, s)
            s['observations'][0]['price_eur'] = 200
            with self.assertRaises(ValueError): save_scan(d, s)

    def test_same_bar_stop_before_target_and_gap_loss(self):
        s = sample_scan(buy=True)
        s['observations'][0]['trade_plan'] = {'valid': True, 'amount': '1', 'entry_eur': 100,
            'stop_eur': 95, 'tp1_eur': 110,
            'cost_assumptions': {'fee_rate_each_side': .0025, 'slippage_rate_each_side': .001}}
        cs = candles(48, 300000, int(NOW*1000))
        for c in cs: c.update(o=100, h=111, l=94, c=105)
        s['candles_5m'] = {'TEST-EUR': cs}; ingest(self.db, s)
        obs = self.db.execute('SELECT * FROM observations').fetchone()
        trade = simulate_trade(self.db, obs)
        self.assertEqual(trade['exit_reason'], 'STOP')
        self.assertLess(trade['pnl_eur'], -5)
        self.assertTrue(trade['ambiguous_stop_and_target_bar'])

    def test_passive_entry_target_order_is_not_fabricated(self):
        s = sample_scan(buy=True)
        s['observations'][0]['trade_plan'] = {'valid': True, 'amount': '1', 'entry_eur': 100,
            'stop_eur': 95, 'tp1_eur': 110,
            'cost_assumptions': {'fee_rate_each_side': .0025, 'slippage_rate_each_side': .001}}
        cs = candles(48, 300000, int(NOW*1000))
        for c in cs: c.update(o=105, h=111, l=99, c=105)
        s['candles_5m'] = {'TEST-EUR': cs}; ingest(self.db, s)
        obs = self.db.execute('SELECT * FROM observations').fetchone()
        self.assertEqual(simulate_trade(self.db, obs)['status'], 'AMBIGUOUS')


class TransportTests(unittest.TestCase):
    def test_replay_missing_input_cannot_fetch_present_data(self):
        with self.assertRaises(RuntimeError): ReplayClient([]).get('/BTC-EUR/candles', {'interval': '15m'})

    def test_public_pipeline_rejects_private_endpoints(self):
        for path in ('/order', '/balance', '/withdrawal', 'https://example.com'):
            with self.assertRaises(ValueError): PublicClient().get(path)


class BaselineIntegrityTests(unittest.TestCase):
    def test_archived_hashes(self):
        directory = ROOT/'baseline/v4_20260908'
        m = read_json(directory/'manifest.json')
        for name, digest in m['files'].items():
            self.assertEqual(hashlib.sha256((directory/name).read_bytes()).hexdigest(), digest)

    def test_no_scoring_rule_or_threshold_changed(self):
        directory = ROOT/'baseline/v4_20260908'
        for name in ('collector-2.py', 'v3_common.py', 'v3_scoring.py', 'early_detector.py', 'v4_common.py', 'v4_stabilizer.py', 'v4_config.json'):
            self.assertEqual((ROOT/name).read_bytes(), (directory/name).read_bytes(), name)
        reference = ast.parse((directory/'v4_detector.py').read_text())
        current = ast.parse((ROOT/'v4_detector.py').read_text())
        main = next(n for n in current.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
        main.args = ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[])
        main.body = [n for n in main.body if not (isinstance(n, ast.If) and isinstance(n.test, ast.Compare)
                     and isinstance(n.test.left, ast.Name) and n.test.left.id == 'audit_sink')]
        self.assertEqual(ast.dump(reference, include_attributes=False), ast.dump(current, include_attributes=False))


if __name__ == '__main__': unittest.main()
