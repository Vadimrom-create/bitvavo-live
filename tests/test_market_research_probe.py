"""Public market observations must cover requested symbols and remain internally coherent."""
import json
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import execution_probe


class PublicMarketResearchProbeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        self.fixed = self.path / "market_analysis_watchlist.json"
        self.fixed.write_text(json.dumps({"markets": ["FIL-EUR", "KAS-EUR", "VTHO-EUR"]}))
        self.watch = self.path / "decision_watchlist.json"
        self.watch.write_text(json.dumps({
            "priority": [{"market": "W-EUR"}] * 60,
            "continuation_wait_for_pullback": ["KAS-EUR"],
        }))
        self.v4 = self.path / "v4_watch.json"
        self.v4.write_text(json.dumps({"watch": []}))
        self.output = self.path / "execution_snapshot.json"
        self.patchers = [
            patch.object(execution_probe, "MARKET_ANALYSIS_WATCHLIST", self.fixed),
            patch.object(execution_probe, "WATCHLIST", self.watch),
            patch.object(execution_probe, "V4", self.v4),
            patch.object(execution_probe, "OUTPUT", self.output),
        ]
        for obj in self.patchers:
            obj.start()
            self.addCleanup(obj.stop)

    def test_market_research_targets_first_independent_of_scan_selection(self):
        names, sources = execution_probe.select_targets()
        self.assertEqual(names[:3], ["FIL-EUR", "KAS-EUR", "VTHO-EUR"])
        self.assertLessEqual(len(names), execution_probe.MAX_TARGETS)
        self.assertIn("public_market_analysis:requested", sources["KAS-EUR"])
        self.assertIn("decision_watchlist:continuation", sources["KAS-EUR"])

    def test_coherent_bid_ask_last_trade_and_timestamped_book(self):
        def get_json(path, params=None, retries=4):
            if path == "/ticker/price":
                return [{"market": m, "price": "1.02"} for m in
                        ("FIL-EUR", "KAS-EUR", "VTHO-EUR")]
            if path == "/ticker/book":
                # An intentionally inconsistent ticker: must not contaminate
                # the depth book's own bid/ask, spread, or slippage.
                return [{"market": m, "bid": "1.20", "ask": "1.40",
                         "bidSize": "9", "askSize": "12"} for m in
                        ("FIL-EUR", "KAS-EUR", "VTHO-EUR")]
            if path.endswith("/book"):
                return {"bids": [["1.0", "250"], ["0.99", "250"]],
                        "asks": [["1.01", "250"], ["1.02", "250"]]}
            if path.endswith("/trades"):
                now_ms = int(time.time() * 1000)
                return [
                    {"price": "1.003", "amount": "2", "side": "buy", "timestamp": now_ms - 1000},
                    {"price": "1.004", "amount": "1", "side": "sell", "timestamp": now_ms - 10000},
                ]
            raise AssertionError(path)
        with patch.object(execution_probe, "get_json", side_effect=get_json):
            execution_probe.main()
        out = json.loads(self.output.read_text())
        self.assertEqual(out["target_count"], 4)
        for row in out["markets"][:3]:
            self.assertEqual(row["status"], "OK")
            self.assertEqual(row["best_bid"], 1.0)
            self.assertEqual(row["best_ask"], 1.01)
            self.assertEqual(row["spread_pct"], round(0.01 / 1.005 * 100, 6))
            self.assertEqual(row["ticker_book_bid"], 1.2)
            self.assertEqual(row["recent_public_trade_flow"]["sample_trades"], 2)
            self.assertEqual(row["latest_public_trade"]["price_eur"], 1.003)
            self.assertLess(row["latest_trade_age_seconds_at_write"], 30)
            self.assertGreaterEqual(row["public_trade_sample_span_seconds"], 9)
            self.assertIn("book_observed_at_utc", row)
            self.assertIn("trades_observed_at_utc", row)
            self.assertLessEqual(row["buy_slippage"][0]["slippage_vs_best_ask_pct"], 1)

    def test_crossed_book_cannot_be_reported_as_valid(self):
        def bad_get(path, params=None, retries=4):
            if path in ("/ticker/price", "/ticker/book"):
                return []
            if path.endswith("/book"):
                return {"bids": [["2", "10"]], "asks": [["1", "10"]]}
            return []
        with patch.object(execution_probe, "get_json", side_effect=bad_get):
            execution_probe.main()
        d = json.loads(self.output.read_text())
        self.assertTrue(all(row["status"] == "ERROR" for row in d["markets"]))


if __name__ == "__main__":
    unittest.main()
