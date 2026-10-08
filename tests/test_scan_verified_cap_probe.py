"""Adversarial no-lookahead and identity tests for three-asset cap probe."""
import importlib.util
import sys
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_verified_cap_probe.py"
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("scan_verified_cap_probe", SCRIPT)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def cg():
    return [
        {"id": "origin-protocol", "symbol": "ogn", "current_price": 0.044,
         "market_cap": 30_000_000, "total_volume": 6_000_000,
         "last_updated": "2026-10-08T21:45:00Z"},
        {"id": "iexec-rlc", "symbol": "rlc", "current_price": 0.77,
         "market_cap": 65_000_000, "total_volume": 9_000_000,
         "last_updated": "2026-10-08T21:45:00Z"},
        {"id": "zircuit", "symbol": "zrc", "current_price": 0.0014,
         "market_cap": 9_000_000, "total_volume": 500_000,
         "last_updated": "2026-10-08T21:45:00Z"},
    ]


def bv():
    dt = datetime.fromisoformat("2026-10-08T21:47:00+00:00")
    ts = int(dt.timestamp() * 1000)
    return [
        {"market": "OGN-EUR", "last": "0.044", "bid": "0.0439",
         "ask": "0.0441", "volumeQuote": "4200000", "timestamp": ts},
        {"market": "RLC-EUR", "last": "0.77", "bid": "0.769",
         "ask": "0.771", "volumeQuote": "6000000", "timestamp": ts},
        {"market": "ZRC-EUR", "last": "0.0014", "bid": "0.00138",
         "ask": "0.00143", "volumeQuote": "320000", "timestamp": ts},
    ]


class CapProbeTests(unittest.TestCase):
    def test_verified_three_asset_turnover_and_later_exchange_snapshot(self):
        x = probe.build_observation(cg(), bv())
        self.assertEqual(x["cap_coverage_pct"], 100)
        self.assertEqual(x["market_count"], 3)
        self.assertEqual(x["observations"][0]["turnover_bitvavo_24h_pct"], 14.0)
        self.assertEqual(x["observations"][0]["turnover_global_24h_pct"], 20.0)
        self.assertTrue(x["not_a_trade_signal"])
        self.assertIsNone(x["observations"][0]["volume_last_4h_vs_prev_4h"])

    def test_future_cap_not_usable(self):
        coins = cg()
        coins[0]["last_updated"] = "2026-10-08T21:50:00Z"
        x = probe.build_observation(coins, bv())
        self.assertEqual(x["observations"][0]["status"], "CAP_FUTURE_LOOKAHEAD")
        self.assertIsNone(x["observations"][0]["turnover_global_24h_pct"])

    def test_symbol_collision_causes_unverified_status(self):
        coins = cg()
        coins[0]["symbol"] = "fake-ogn"
        x = probe.build_observation(coins, bv())
        self.assertEqual(x["observations"][0]["status"], "CAP_UNVERIFIED")
        self.assertIn("IDENTITY_OR_PRICE_SANITY_FAILED",
                      [d["reason"] for d in x["provider_gaps"]])

    def test_price_divergence_causes_unverified_status(self):
        coins = cg()
        coins[0]["current_price"] = 0.01
        x = probe.build_observation(coins, bv())
        self.assertEqual(x["observations"][0]["status"], "CAP_UNVERIFIED")

    def test_missing_coingecko_asset_retains_bitvavo_observation(self):
        x = probe.build_observation(cg()[1:], bv())
        self.assertEqual(x["market_count"], 3)
        self.assertEqual(x["observations"][0]["status"], "CAP_UNAVAILABLE")

    def test_missing_one_ticker_not_imputed(self):
        x = probe.build_observation(cg(), bv()[1:])
        self.assertEqual(x["market_count"], 2)
        self.assertIn("BITVAVO_TICKER_MISSING",
                      [d["reason"] for d in x["provider_gaps"]])

    def test_duplicate_market_rejected(self):
        rows = bv()
        with self.assertRaises(probe.BadEvidence):
            probe.build_observation(cg(), rows + [rows[0]])

    def test_duplicate_vendor_identity_rejected(self):
        rows = cg()
        with self.assertRaises(probe.BadEvidence):
            probe.build_observation(rows + [rows[0]], bv())

    def test_no_tickers_rejected(self):
        with self.assertRaises(probe.BadEvidence):
            probe.build_observation(cg(), [])

    def test_fetch_order_is_coingecko_then_bitvavo(self):
        calls = []
        def fake(url):
            calls.append(url)
            return cg() if "coingecko" in url else bv()
        import contextlib, io, json, tempfile
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(probe, "fetch_json", side_effect=fake):
                with contextlib.redirect_stdout(io.StringIO()):
                    code = probe.main(["--output", str(Path(folder) / "out.json")])
            self.assertEqual(code, 0)
            self.assertIn("coingecko", calls[0])
            self.assertIn("bitvavo", calls[1])
            self.assertEqual(json.loads((Path(folder) / "out.json").read_text())["cap_coverage_pct"], 100)


if __name__ == "__main__":
    unittest.main()
