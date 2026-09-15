"""Failure boundaries, independent of the shadow test/import graph."""
import ast
import builtins
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from cryptography.fernet import Fernet
from research.common import utc

ROOT = Path(__file__).resolve().parents[1]


def load_runner():
    spec = importlib.util.spec_from_file_location('isolated_monitor', ROOT / 'scripts/send_useful_alert.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MonitorIsolationTests(unittest.TestCase):
    def test_buy_import_failure_does_not_prevent_loading_monitor(self):
        original = builtins.__import__
        def fail(name, *args, **kwargs):
            if name in {'email_alert_v4', 'research.risk', 'monitoring.buy_candidates', 'research.decision_layer'}:
                raise ImportError('optional module broken')
            return original(name, *args, **kwargs)
        with patch('builtins.__import__', side_effect=fail):
            self.assertTrue(callable(load_runner().run))

    def test_stop_email_precedes_all_candle_enrichment(self):
        runner = load_runner()
        now = 1800000000.
        order = []
        class Public:
            server_offset = 0
            def __init__(self, **kwargs): pass
            def get(self, path, *args, **kwargs):
                order.append(path)
                if path == '/time': return {'time': int(now*1000)}
                if path == '/markets':
                    return [{'market': m+'-EUR', 'quote': 'EUR', 'status': 'trading', 'tickSize': '.01',
                             'quantityDecimals': 2, 'minOrderInQuoteAsset': '5'} for m in ('AAA', 'BBB')]
                if path.endswith('/book'): return {'bids': [['8', '100']], 'asks': [['8.01', '100']]}
                if path.endswith('/candles'): raise AssertionError('enrichment must not run before exit')
                raise AssertionError(path)
            def capture(self, path, *args, **kwargs):
                return {'data': self.get(path, *args, **kwargs), **self.metadata(path)}
            def metadata(self, *args): return {'retrieved_at_utc': utc(now)}
        account = {'retrieved_at_utc': utc(now), 'balances': [dict(symbol=m, amount=10, available=10) for m in ('AAA','BBB')], 'orders': []}
        plans = {m+'-EUR': dict(position_id=m, verified=True, initial_amount=10, stop_eur=9) for m in ('AAA','BBB')}
        env = dict(BITVAVO_READ_API_KEY='fake', BITVAVO_READ_API_SECRET='fake', POSITION_STATE_KEY=Fernet.generate_key().decode(),
                   POSITION_PLANS_JSON=json.dumps(plans), ALLOW_BUY_ALERTS='true', ALERT_GMAIL_USER='fake',
                   ALERT_EMAIL_TO='bellonirom@gmail.com', GMAIL_APP_PASSWORD='fake')
        # These faults live outside the critical process; no import/read is permitted.
        for failure in ('shadow_test', 'shadow_import', 'prospection_timeout', 'corrupt_journal', 'publication_conflict', 'new_main_commit'):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as d, patch.dict('os.environ', env, clear=True), \
                 patch.object(runner, 'STATE', str(Path(d)/'state.json')), patch.object(runner, 'PublicClient', Public), \
                 patch.object(runner, 'ReadOnlyAccount') as private, patch.object(runner.time, 'time', return_value=now), \
                 patch.object(runner, 'read_json', side_effect=RuntimeError(failure)), \
                 patch.object(runner.email_alert, 'send_email') as smtp:
                private.return_value.snapshot.return_value = account
                runner.run({})
                smtp.assert_called_once()
                self.assertIn('AAA-EUR', smtp.call_args.args[-1])
                self.assertIn('BBB-EUR', smtp.call_args.args[-1])
        self.assertFalse(any(p.endswith('/candles') for p in order))

    def test_workflows_have_one_sender_and_independent_monitor(self):
        monitor = (ROOT/'.github/workflows/monitor_positions.yml').read_text()
        self.assertNotIn('needs:', monitor)
        self.assertIn('monitor_release.json', monitor)
        self.assertIn('monitor-code', monitor)
        self.assertIn('monitor-data', monitor)
        workflows = list((ROOT/'.github/workflows').glob('*.yml'))
        self.assertEqual(sum(p.read_text().count('python scripts/send_useful_alert.py') for p in workflows), 1)
        for name in ('scripts/send_useful_alert.py', 'monitoring/positions.py'):
            tree = ast.parse((ROOT/name).read_text())
            eager = [n.module for n in tree.body if isinstance(n, ast.ImportFrom)]
            self.assertNotIn('research.risk', eager)
            self.assertNotIn('email_alert_v4', eager)
        scan=(ROOT/'.github/workflows/update.yml').read_text()
        evaluation=(ROOT/'.github/workflows/evaluate.yml').read_text()
        self.assertIn('ref: ${{ github.sha }}',scan)
        self.assertIn('ref: ${{ github.sha }}',evaluation)
        self.assertNotIn('run_evaluation.py',scan)
        self.assertNotIn('send_useful_alert',evaluation)
        self.assertIn('prepare_publication.py',scan)
        self.assertIn('continue-on-error: true',scan)

    def test_persistence_delay_is_rechecked_before_smtp(self):
        runner=load_runner();now=[1800000000.]
        env=dict(BITVAVO_READ_API_KEY='fake',BITVAVO_READ_API_SECRET='fake',POSITION_STATE_KEY=Fernet.generate_key().decode(),
                 POSITION_PLANS_JSON=json.dumps({'AAA-EUR':{'position_id':'a','verified':True,'initial_amount':10,'stop_eur':9}}),
                 ALERT_GMAIL_USER='fake',ALERT_EMAIL_TO='bellonirom@gmail.com',GMAIL_APP_PASSWORD='fake')
        account={'retrieved_at_utc':utc(now[0]),'balances':[{'symbol':'AAA','amount':10,'available':10}],'orders':[]}
        quote={'bid':8,'ask':8.01,'retrieved_at_utc':utc(now[0])}
        def public_get(path):
            if path=='/time': return {'time':int(now[0]*1000)}
            return [{'market':'AAA-EUR','quote':'EUR','status':'trading','tickSize':'.01','quantityDecimals':2,'minOrderInQuoteAsset':'5'}]
        def delayed_save(*args): now[0]+=121
        with tempfile.TemporaryDirectory() as d,patch.dict('os.environ',env,clear=True), \
             patch.object(runner,'STATE',str(Path(d)/'state.json')),patch.object(runner,'ReadOnlyAccount') as private, \
             patch.object(runner,'PublicClient') as public,patch.object(runner,'market_quote',return_value=quote), \
             patch.object(runner.time,'time',side_effect=lambda:now[0]),patch.object(runner,'save_state',side_effect=delayed_save), \
             patch.object(runner.email_alert,'send_email') as smtp:
            private.return_value.snapshot.return_value=account
            public.return_value.server_offset=0;public.return_value.get.side_effect=public_get
            status={};runner.run(status)
            smtp.assert_not_called();self.assertEqual(status['email'],'BLOCKED_FINAL_FRESHNESS')

class MonitorTimingTests(unittest.TestCase):
    def test_only_successful_evaluations_advance_cadence(self):
        from monitoring.telemetry import record_cycle
        state, status = {}, {}
        for now, issues in ((1000, []), (1300, ['READ_FAILED']), (1900, [])):
            record_cycle(state, status, {'retrieved_at_utc': utc(now-2)}, {}, 0, issues, now)
        self.assertEqual(state['monitor_timing']['successful_at'], [1000, 1900])
        self.assertEqual(status['timing']['interval_max_seconds'], 900)
        self.assertEqual(status['timing']['account_age_at_decision_seconds'], 2)
        self.assertEqual(status['timing']['slo'], 'NOT_YET_DEMONSTRATED')

    def test_stale_account_or_book_is_not_successful_coverage(self):
        from monitoring.telemetry import record_cycle
        for stale_account,stale_book in ((True,False),(False,True)):
            state,status={},{}
            record_cycle(state,status,{'retrieved_at_utc':utc(800 if stale_account else 999)},
                {'AAA-EUR':({'retrieved_at_utc':utc(800 if stale_book else 999),'bid':1,'ask':1.01},{},[])},1,[],1000)
            self.assertFalse(status['timing']['successful_evaluation'])
            self.assertEqual(state['monitor_timing']['successful_at'],[])

    def test_unconfigured_availability_does_not_claim_private_monitoring(self):
        from monitoring.telemetry import record_availability
        previous={}
        for t in (0,300,700): previous=record_availability(previous,{'status':'UNCONFIGURED'},t)
        self.assertEqual(previous['successful_samples'],0)
        self.assertEqual(previous['private_validation'],'PENDING PRIVATE CONFIGURATION')
        self.assertEqual(previous['observed_unconfigured_seconds'],700)
