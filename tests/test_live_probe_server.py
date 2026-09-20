import importlib.util
import json
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path


def load_probe_module():
    path = Path(__file__).resolve().parents[1] / "oracle" / "bitvavo_public_probe.py"
    spec = importlib.util.spec_from_file_location("live_probe_server", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class LiveProbeServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.probe = load_probe_module()
        cls.server = cls.probe.ProbeServer(("127.0.0.1", 0), cls.probe.Handler)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get_json(self, path):
        with urllib.request.urlopen(
            f"http://127.0.0.1:{self.port}{path}", timeout=2
        ) as response:
            return response.status, json.loads(response.read().decode("utf-8"))

    def test_health_is_fast_and_independent_of_bitvavo(self):
        status, payload = self.get_json("/health")
        self.assertEqual(status, 200)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["service"], "bitvavo-public-probe")
        self.assertGreaterEqual(payload["max_concurrent_quotes"], 1)

    def test_invalid_market_is_rejected_without_upstream_call(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.get_json("/quote?market=NOT_A_MARKET")
        self.assertEqual(ctx.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
