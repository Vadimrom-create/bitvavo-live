"""The WALLET path collects held assets regardless of scan watchlists."""
import unittest
from datetime import datetime, timezone
from unittest.mock import patch

from scripts.enrich_private_wallet import (
    BOOK_DEPTH, TRADES_LIMIT, collect_market, enrich,
)

NOW = datetime(2026, 10, 8, 21, 40, tzinfo=timezone.utc).timestamp()
STAMP = datetime.fromtimestamp(NOW - 2, timezone.utc).isoformat()


class FakePublicClient:
    def __init__(self, fail_book=None, fail_trades=None, stale_book=False):
        self.calls = []
        self.fail_book = fail_book
        self.fail_trades = fail_trades
        self.stale_book = stale_book

    def get(self, path, params=None, cache=True):
        self.calls.append((path, params))
        if path == "/ticker/24h":
            return [
                {
                    "market": m, "last": "1.02", "open": "1.00",
                    "volumeQuote": "350000"
                }
                for m in ("FIL-EUR", "KAS-EUR", "VTHO-EUR")
            ]
        if path.endswith("/book"):
            if path.startswith("/" + str(self.fail_book)):
                raise RuntimeError("public book unavailable")
            return {
                "bids": [["1.0", "10"], ["0.99", "100"], ["0.98", "1000"]],
                "asks": [["1.01", "10"], ["1.02", "100"], ["1.03", "1000"]],
            }
        if path.endswith("/trades"):
            if path.startswith("/" + str(self.fail_trades)):
                raise RuntimeError("public trades unavailable")
            return [
                {"price": "1.005", "amount": "4", "side": "buy", "timestamp": int((NOW - 5) * 1000)},
                {"price": "1.006", "amount": "1", "side": "sell", "timestamp": int((NOW - 3) * 1000)},
            ]
        raise AssertionError("unexpected path " + path)

    def metadata(self, path, params=None):
        age = 200 if self.stale_book and path.endswith("/book") else 2
        return {"retrieved_at_utc": datetime.fromtimestamp(NOW - age, timezone.utc).isoformat()}


class WalletExecutionTests(unittest.TestCase):
    def test_all_held_symbols_even_if_not_in_any_watchlist(self):
        balances = {
            "cash_eur": 2100,
            "positions": [
                {"market": "FIL-EUR", "quantity": 5, "pru_eur": 1.05},
                {"market": "KAS-EUR", "quantity": 25, "pru_eur": 1.1},
                {"market": "VTHO-EUR", "quantity": 10, "pru_eur": 1.4},
            ],
        }
        client = FakePublicClient()
        result = enrich(balances, client, now_fn=lambda: NOW, monotonic_fn=lambda: 10)
        self.assertEqual(result["execution_coverage"]["market_count"], 3)
        self.assertEqual(result["execution_coverage"]["attempted_count"], 3)
        self.assertEqual(result["execution_coverage"]["status_counts"]["OK"], 3)
        self.assertEqual([p["market"] for p in result["positions"]],
                         ["FIL-EUR", "KAS-EUR", "VTHO-EUR"])
        self.assertEqual(balances["positions"][0].keys(), {"market", "quantity", "pru_eur"})
        for pos in result["positions"]:
            evidence = pos["execution_evidence"]
            self.assertEqual(evidence["status"], "OK")
            self.assertEqual(evidence["book_depth_levels_requested"], BOOK_DEPTH)
            self.assertEqual(evidence["trades_limit_requested"], TRADES_LIMIT)
            self.assertEqual(len(evidence["full_observed_bids"]), 3)
            self.assertEqual(evidence["near_depth"]["within_1pct"]["bid_notional_eur"], 10)
            self.assertEqual(evidence["quote_volume_24h_eur"], 350000)
            self.assertAlmostEqual(evidence["change_24h_pct"], 2.0)
            self.assertAlmostEqual(evidence["spread_pct"], (0.01 / 1.005) * 100, places=5)
            self.assertEqual(evidence["recent_public_trade_flow"]["sample_trades"], 2)
            self.assertAlmostEqual(evidence["latest_public_trade"]["price_eur"], 1.006)
            self.assertEqual(evidence["book_age_seconds_at_write"], 2)
            self.assertEqual(evidence["trades_age_seconds_at_write"], 2)
            self.assertTrue(evidence["held_quantity_sell_estimate"]["complete_in_depth"])
            self.assertTrue(evidence["orders_submitted"] is False)
            self.assertFalse(evidence["affects_buy_gate"])
        self.assertEqual(sum(path.endswith("/book") for path, _ in client.calls), 3)
        self.assertEqual(sum(path.endswith("/trades") for path, _ in client.calls), 3)
        self.assertEqual(sum(path == "/ticker/24h" for path, _ in client.calls), 1)

    def test_trade_failure_is_partial_not_invented_buy_pressure(self):
        row = collect_market(
            FakePublicClient(fail_trades="KAS-EUR"),
            "KAS-EUR", 10, now_fn=lambda: NOW,
            ticker={"last": "1.02", "open": "1.0", "volumeQuote": "350000"},
            ticker_meta={"retrieved_at_utc": STAMP},
        )
        self.assertEqual(row["status"], "PARTIAL")
        self.assertIn("TRADES_UNAVAILABLE_OR_INVALID", row["reasons"])
        self.assertNotIn("recent_public_trade_flow", row)
        self.assertTrue(row["held_quantity_sell_estimate"]["complete_in_depth"])

    def test_book_failure_does_not_hide_recent_trades(self):
        row = collect_market(
            FakePublicClient(fail_book="FIL-EUR"),
            "FIL-EUR", 10, now_fn=lambda: NOW,
            ticker={"last": "1.02", "open": "1.0", "volumeQuote": "350000"},
            ticker_meta={"retrieved_at_utc": STAMP},
        )
        self.assertEqual(row["status"], "PARTIAL")
        self.assertIn("BOOK_UNAVAILABLE_OR_INVALID", row["reasons"])
        self.assertNotIn("near_depth", row)
        self.assertEqual(row["recent_public_trade_flow"]["sample_trades"], 2)

    def test_stale_book_not_marked_ok(self):
        row = collect_market(
            FakePublicClient(stale_book=True),
            "FIL-EUR", 10, now_fn=lambda: NOW,
            ticker={"last": "1.02", "open": "1.0", "volumeQuote": "350000"},
            ticker_meta={"retrieved_at_utc": STAMP},
        )
        self.assertEqual(row["status"], "PARTIAL")
        self.assertIn("STALE_OR_UNTIMED_BOOK", row["reasons"])

    def test_budget_marks_missing_positions_explicitly(self):
        summary = {"positions": [{"market": "FIL-EUR", "quantity": 10},
                                 {"market": "KAS-EUR", "quantity": 10}]}
        # The monotonic clock says the budget was exhausted immediately.
        ticks = iter([0, 91, 92])
        enriched = enrich(summary, FakePublicClient(), now_fn=lambda: NOW,
                          monotonic_fn=lambda: next(ticks))
        self.assertEqual(enriched["execution_coverage"]["attempted_count"], 0)
        self.assertEqual(enriched["execution_coverage"]["status_counts"]["NOT_OBSERVED"], 2)

    def test_invalid_market_never_reaches_public_api(self):
        client = FakePublicClient()
        row = collect_market(client, "FIL-EUR/../balance", 10, now_fn=lambda: NOW)
        self.assertEqual(row["status"], "UNAVAILABLE")
        self.assertEqual(row["reasons"], ["INVALID_MARKET"])
        self.assertEqual(client.calls, [])

    def test_missing_24h_ticker_does_not_fabricate_volume(self):
        row = collect_market(FakePublicClient(), "FIL-EUR", 10, now_fn=lambda: NOW)
        self.assertEqual(row["status"], "PARTIAL")
        self.assertIn("TICKER_24H_UNAVAILABLE_OR_STALE", row["reasons"])
        self.assertNotIn("quote_volume_24h_eur", row)


if __name__ == "__main__":
    unittest.main()
