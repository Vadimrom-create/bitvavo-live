import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "oracle_probe_request",
    Path(__file__).resolve().parents[1] / "scripts/oracle_probe_request.py",
)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


class OracleProbeRequestTests(unittest.TestCase):
    def test_oracle_timeout_uses_direct_public_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            output = Path(directory) / "output.json"
            request.write_text(json.dumps({"market": "BTC-EUR", "stake_eur": 75}), encoding="utf-8")
            fallback = {"ok": True, "source": "bitvavo_public_direct_fallback", "market": "BTC-EUR"}
            with patch.object(probe, "REQUEST", request), patch.object(probe, "OUTPUT", output), \
                    patch.object(probe, "get_json", side_effect=TimeoutError("down")), \
                    patch.object(probe, "direct_bitvavo_quote", return_value=fallback):
                probe.main()
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(payload["transport_ok"])
            self.assertEqual(payload["probe"]["source"], "bitvavo_public_direct_fallback")
            self.assertTrue(payload["probe"]["ok"])

    def test_live_oracle_response_remains_primary(self):
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            output = Path(directory) / "output.json"
            request.write_text(json.dumps({"market": "BTC-EUR", "stake_eur": 75}), encoding="utf-8")
            live = {"ok": True, "source": "bitvavo_public", "market": "BTC-EUR"}
            with patch.object(probe, "REQUEST", request), patch.object(probe, "OUTPUT", output), \
                    patch.object(probe, "get_json", return_value=live), \
                    patch.object(probe, "direct_bitvavo_quote") as fallback:
                probe.main()
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(payload["transport_ok"])
            self.assertEqual(payload["probe"], live)
            fallback.assert_not_called()


if __name__ == "__main__":
    unittest.main()
