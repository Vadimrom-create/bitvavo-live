import base64
import contextlib
import importlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'executor'))
try:
    daemon = importlib.import_module('daemon')
    from bitvavo_client import BitvavoClient
finally:
    sys.path.pop(0)


class ExecutorSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ex = daemon.Executor.__new__(daemon.Executor)
        self.ex.lock = threading.RLock()
        self.ex.state = {'orders': {}, 'security_freeze': False}
        self.ex.state_file = Path(self.temp.name) / 'state.json'
        self.ex.event_log = Path(self.temp.name) / 'events.jsonl'
        self.ex.operator_id = 123456789
        self.ex.dry_run = False
        self.ex.freeze_on_unknown = True
        self.ex.auto_cancel_unknown = True
        self.ex.github_token = 'TEST_ONLY'
        self.ex.github_repo = 'owner/repo'
        self.ex.client = BitvavoClient('TEST_ONLY', 'TEST_ONLY', 1)
        self.ex.client.session.request = Mock(return_value=Mock(status_code=200, json=lambda: {}))

    def test_every_mutation_is_blocked_before_transport(self):
        for method in ('POST', 'PUT', 'PATCH', 'DELETE', 'post'):
            with self.subTest(method=method), self.assertRaises(PermissionError):
                self.ex.client.request(method, '/order', private=False)
        self.ex.client.session.request.assert_not_called()

    def test_publications_and_stdout_exclude_private_values(self):
        published = []
        self.ex._publish_github_json = lambda path, data, message: published.append(data)
        event = dict(event='order', status='new', market='PRIVATE-MARKET', orderId='PRIVATE-ORDER',
                     clientOrderId='PRIVATE-CLIENT', operatorId=123456789, side='buy', orderType='limit',
                     nested={'secret': 'PRIVATE-NESTED'})
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.ex.security_event('PRIVATE-REASON', event)
        public = json.dumps(published) + stdout.getvalue()
        for value in ('PRIVATE-', '123456789'):
            self.assertNotIn(value, public)
        self.assertIn('PRIVATE-ORDER', self.ex.event_log.read_text())
        self.ex.client.session.request.assert_not_called()
        for payload in published:
            self.assertEqual(set(payload), {'schema_version', 'generated_at_utc', 'online',
                                           'dry_run', 'security_freeze', 'execution_enabled', 'status_code'})

    def test_public_transport_does_not_trust_caller_payload(self):
        response = Mock(status_code=200, json=lambda: {'sha': 'old'})
        with patch.object(daemon.requests, 'get', return_value=response), patch.object(daemon.requests, 'put', return_value=response) as put:
            self.ex._publish_github_json('executor_status.json', {'last_approval_result': {'secret': 'PRIVATE-SENTINEL'}}, 'test')
        payload = json.loads(base64.b64decode(put.call_args.kwargs['json']['content']))
        self.assertNotIn('PRIVATE-SENTINEL', json.dumps(payload))
        self.assertFalse(payload['execution_enabled'])

    def test_missing_and_restarted_state_are_closed(self):
        self.assertTrue(self.ex._load_state()['security_freeze'])
        self.ex.state_file.write_text(json.dumps({'orders': {}, 'security_freeze': False}))
        self.assertTrue(self.ex._load_state()['security_freeze'])

    def test_corrupt_state_is_not_a_clean_account(self):
        for value in ('{broken', '[]', '{"orders": []}'):
            self.ex.state_file.write_text(value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.ex._load_state()

    def test_configuration_cannot_reenable_execution(self):
        env = {'BITVAVO_API_KEY': 'TEST_ONLY', 'BITVAVO_API_SECRET': 'TEST_ONLY',
               'STATE_DIR': self.temp.name, 'DRY_RUN': 'false', 'AUTO_CANCEL_UNKNOWN_ORDERS': 'true'}
        with patch.dict(os.environ, env, clear=True), patch.object(daemon.Executor, '_load_market_meta', return_value={}):
            ex = daemon.Executor()
        self.assertTrue(ex.dry_run)
        self.assertFalse(ex.auto_cancel_unknown)


if __name__ == '__main__':
    unittest.main()
