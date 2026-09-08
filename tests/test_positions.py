import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cryptography.fernet import Fernet, InvalidToken

from monitoring.account import ReadOnlyAccount
from monitoring.positions import BUY, PARTIAL, SELL, TRAIL, management_event, mark_delivered, select_actions
from monitoring.state import load_state, save_state
from research.common import utc
from research.history import connect, ingest, new_candles

spec = importlib.util.spec_from_file_location('useful_alert', Path(__file__).resolve().parents[1] / 'scripts/send_useful_alert.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class Positions(unittest.TestCase):
    def setUp(self):
        self.now = 1_800_000_000.
        self.balance = {'symbol': 'ABC', 'amount': 10., 'available': 10., 'in_order': 0}
        self.plan = {'position_id': 'lot-1', 'verified': True, 'initial_amount': 10.,
                     'cost_basis_eur': 10., 'stop_eur': 9., 'tp1_eur': 15.}
        self.quote = {'bid': 12., 'ask': 12.01, 'retrieved_at_utc': utc(self.now)}
        self.features = {'valid': True, 'atr14_eur': 1., 'support_eur': 9.,
                         'last_closed_start_ms': int(self.now // 900 - 1) * 900000}
        self.meta = {'tickSize': '.01', 'quantityDecimals': 2, 'minOrderInQuoteAsset': '5', 'minOrderInBaseAsset': '.01'}

    def assess(self, **changes):
        args = dict(balance=self.balance, plan=self.plan, quote=self.quote, features=self.features,
                    meta=self.meta, orders=[], now=self.now)
        args.update(changes)
        return management_event(**args)

    def test_hold_is_silent(self):
        self.assertEqual(self.assess(), (None, 'NO_JUSTIFIED_ACTION'))

    def test_stop_breach_does_not_need_candles_or_cost_basis(self):
        self.quote.update(bid=8.9, ask=8.91)
        del self.plan['cost_basis_eur']
        event, _ = self.assess(features={'valid': False})
        self.assertEqual(event['action'], SELL)

    def test_missing_plan_stale_book_and_added_quantity_never_guess(self):
        self.assertIsNone(self.assess(plan={})[0])
        self.assertIsNone(self.assess(quote={**self.quote, 'retrieved_at_utc': utc(self.now - 91)})[0])
        self.assertIsNone(self.assess(balance={**self.balance, 'amount': 11})[0])

    def test_partial_target_and_completed_reduction(self):
        self.quote.update(bid=15.1, ask=15.11)
        event, _ = self.assess()
        self.assertEqual((event['action'], event['amount']), (PARTIAL, 5))
        self.assertIsNone(self.assess(balance={**self.balance, 'amount': 5})[0])

    def test_partial_profit_must_be_net_positive(self):
        self.plan.update(cost_basis_eur=15.1)
        self.quote.update(bid=15.1, ask=15.11)
        self.assertIsNone(self.assess()[0])

    def test_verified_trailing_stop_never_lowered(self):
        self.features.update(support_eur=12)
        self.quote.update(bid=14, ask=14.01)
        event, _ = self.assess()
        self.assertEqual((event['action'], event['new_stop_eur']), (TRAIL, 11.5))
        self.plan['stop_eur'] = 12
        self.assertIsNone(self.assess()[0])

    def test_stale_closed_structure_blocks_trailing(self):
        self.features.update(support_eur=12, last_closed_start_ms=int(self.now - 3600) * 1000)
        self.quote.update(bid=14, ask=14.01)
        self.assertIsNone(self.assess()[0])

    def test_equivalent_exit_order_suppresses_duplicate(self):
        self.quote.update(bid=8.9, ask=8.91)
        order = {'market': 'ABC-EUR', 'side': 'sell', 'status': 'awaitingTrigger',
                 'orderType': 'stopLoss', 'triggerAmount': '9', 'amountRemaining': '10'}
        self.assertEqual(self.assess(orders=[order])[1], 'EQUIVALENT_EXIT_ORDER_ALREADY_OPEN')
        order.update(orderType='limit', price='15')
        event, _ = self.assess(orders=[order])
        self.assertEqual(event['action'], SELL)
        self.assertTrue(event['review_open_orders_first'])

    def test_one_highest_priority_action_and_no_unchanged_repeat(self):
        base = {'market': 'ABC-EUR', 'position_id': 'lot-1', 'trigger_key': 'tp1'}
        events = [{**base, 'action': PARTIAL}, {**base, 'action': SELL}]
        selected, state = select_actions(events, {}, self.now)
        self.assertEqual([e['action'] for e in selected], [SELL])
        mark_delivered(state, selected, self.now)
        self.assertEqual(select_actions(events, state, self.now + 86400)[0], [])

    def test_failed_delivery_remains_retryable(self):
        event = {'market': 'ABC-EUR', 'position_id': 'lot-1', 'action': SELL, 'trigger_key': 'stop'}
        selected, observed = select_actions([event], {}, self.now)
        self.assertEqual(len(select_actions([event], observed, self.now + 60)[0]), 1)

    def test_urgent_exit_preempts_cooldown_and_trail_requires_improvement(self):
        state = {'last_nonurgent_sent_at': self.now - 5}
        base = {'market': 'ABC-EUR', 'position_id': 'lot-1', 'trigger_key': 'stop'}
        self.assertEqual(len(select_actions([{**base, 'action': SELL}], state, self.now)[0]), 1)
        event = {**base, 'action': TRAIL, 'new_stop_eur': 11}
        selected, state = select_actions([event], {}, self.now)
        mark_delivered(state, selected, self.now)
        self.assertEqual(select_actions([{**event, 'new_stop_eur': 12}], state, self.now + 3599)[0], [])
        self.assertEqual(select_actions([event], state, self.now + 3601)[0], [])
        self.assertEqual(len(select_actions([{**event, 'new_stop_eur': 12}], state, self.now + 3601)[0]), 1)

    def test_private_adapter_has_no_trading_route(self):
        client = ReadOnlyAccount('unit-test-key', 'unit-test-secret')
        with patch.object(client.opener, 'open') as network:
            for endpoint in ['/order', '/withdrawal', '/balance?redirect=https://example.org']:
                with self.assertRaises(PermissionError):
                    client.get(endpoint)
            network.assert_not_called()

    def test_encrypted_state_rebuild_and_tamper_refusal(self):
        key = Fernet.generate_key().decode()
        state = {'positions': {'PRIVATE-EUR': {'amount': 1234567}}, 'deliveries': {}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            save_state(path, key, state)
            self.assertNotIn('PRIVATE-EUR', path.read_text())
            self.assertNotIn('1234567', path.read_text())
            self.assertEqual(load_state(path, key), state)
            with self.assertRaises(InvalidToken):
                load_state(path, Fernet.generate_key().decode())

    def test_unconfigured_account_does_not_send_or_invent_empty_portfolio(self):
        with patch.dict('os.environ', {}, clear=True), patch.object(runner.email_alert, 'send_email') as send:
            status = {}
            self.assertEqual(runner.run(status), 0)
            self.assertEqual(status['status'], 'UNCONFIGURED')
            self.assertEqual(status['buy_alerts'], 'BLOCKED_ACCOUNT_UNKNOWN')
            send.assert_not_called()

    def test_book_still_available_when_candles_fail(self):
        class Client:
            def get(self, path, *args, **kwargs):
                if path.endswith('/candles'):
                    raise RuntimeError('unavailable')
                return {'bids': [['8.9', '10']], 'asks': [['8.91', '10']]}
            def metadata(self, *args):
                return {'retrieved_at_utc': utc(1_800_000_000.)}
        quote, features, _ = runner.market_inputs(Client(), 'ABC-EUR', self.now)
        self.assertEqual(self.assess(quote=quote, features=features)[0]['action'], SELL)

    def test_every_holding_checked_without_prospecting_and_smtp_failure_retry(self):
        account = {'retrieved_at_utc': utc(self.now), 'balances': [self.balance,
                   {**self.balance, 'symbol': 'XYZ'}], 'orders': []}
        metadata = [dict(self.meta, market=m, quote='EUR', status='trading') for m in ['ABC-EUR', 'XYZ-EUR']]
        class Public:
            server_offset = 0
            def __init__(self, **kwargs):
                pass
            def get(self, path):
                return metadata if path == '/markets' else {'time': 1800000000000}
        inputs = lambda client, market, now: ({**self.quote, 'bid': 8.9 if market == 'ABC-EUR' else 12}, self.features, [])
        key = Fernet.generate_key().decode()
        env = {'BITVAVO_READ_API_KEY': 'fake', 'BITVAVO_READ_API_SECRET': 'fake', 'POSITION_STATE_KEY': key,
               'POSITION_PLANS_JSON': json.dumps({'ABC-EUR': self.plan, 'XYZ-EUR': {**self.plan, 'position_id': 'lot-2'}}),
               'ALLOW_BUY_ALERTS': 'false', 'ALERT_GMAIL_USER': 'unit-test', 'ALERT_EMAIL_TO': 'bellonirom@gmail.com',
               'GMAIL_APP_PASSWORD': 'fake'}
        with tempfile.TemporaryDirectory() as directory, patch.dict('os.environ', env, clear=True), \
                patch.object(runner, 'STATE', str(Path(directory) / 'state.json')), \
                patch.object(runner, 'ReadOnlyAccount') as private, patch.object(runner, 'PublicClient', Public), \
                patch.object(runner, 'market_inputs', side_effect=inputs) as markets, \
                patch.object(runner.time, 'time', return_value=self.now), \
                patch.object(runner.email_alert, 'send_email') as send:
            private.return_value.snapshot.return_value = account
            send.side_effect = RuntimeError('SMTP unavailable')
            with self.assertRaises(RuntimeError):
                runner.run({})
            self.assertEqual({c.args[1] for c in markets.call_args_list}, {'ABC-EUR', 'XYZ-EUR'})
            self.assertEqual(load_state(runner.STATE, key)['deliveries'], {})
            send.side_effect = None
            status = {}
            self.assertEqual(runner.run(status), 0)
            self.assertEqual(status['email'], 'DELIVERY_COMPLETED')
            send.reset_mock()
            self.assertEqual(runner.run({}), 0)
            send.assert_not_called()
            self.assertNotIn('ABC-EUR', json.dumps(status))
            # Re-arm a genuinely different position while prospecting is broken.
            import os
            os.environ['ALLOW_BUY_ALERTS'] = 'true'
            os.environ['POSITION_PLANS_JSON'] = json.dumps({'ABC-EUR': {**self.plan, 'position_id': 'lot-3'},
                                                          'XYZ-EUR': {**self.plan, 'position_id': 'lot-2'}})
            with patch.object(runner, 'read_json', side_effect=ValueError('corrupt public prospecting')):
                self.assertEqual(runner.run({}), 0)
            send.assert_called_once()

    def test_candle_deltas_preserve_late_bars_and_original_values(self):
        db = connect()
        bar = {'t': 300000, 'o': 1, 'h': 2, 'l': 1, 'c': 2, 'v': 4}
        ingest(db, {'scan_id': 'a', 'scan_ts': 600, 'policy': 'V4', 'observations': [], 'candles_5m': {'X-EUR': [bar]}})
        late = {**bar, 't': 0}
        revision = {**bar, 'c': 1.5}
        delta = new_candles(db, {'X-EUR': [late, revision]})
        self.assertEqual(delta['X-EUR'], [late])
        self.assertEqual(db.execute('SELECT c FROM candles WHERE t=300000').fetchone()[0], 2)
