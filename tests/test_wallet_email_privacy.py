"""Confidential WALLET->Gmail delivery and fail-closed tests.

Synthetic balances only. Never connect to Bitvavo or Gmail in CI.
"""
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from datetime import datetime, timezone

from scripts import email_private_wallet_summary as bridge


class PrivateWalletEmailTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 11, 13, 15, tzinfo=timezone.utc).timestamp()
        stamp = datetime.fromtimestamp(self.now - 10, timezone.utc).isoformat()
        self.summary = {
            "generated_at_utc": stamp,
            "cash_eur": 2200.0,
            "positions_value_eur": 150.0,
            "wallet_value_eur": 2350.0,
            "positions": [{
                "market": "FAKE-EUR",
                "quantity": 10.0,
                "pru_eur": 12.0,
                "price_eur": 15.0,
                "value_eur": 150.0,
                "management_state": "HOLD",
                "execution_evidence": {
                    "status": "OK",
                    "book_retrieved_at_utc": stamp,
                    "trades_retrieved_at_utc": stamp,
                    "best_bid": 15.0,
                    "best_ask": 15.03,
                    "spread_pct": 0.2,
                    "near_depth": {"within_1pct": {"bid_notional_eur": 1000.0, "ask_notional_eur": 1200.0}},
                    "recent_public_trade_flow": {"buy_taker_share": 0.6, "sample_trades": 100},
                    "latest_public_trade": {"age_seconds_at_write": 3.0},
                    "held_quantity_sell_estimate": {"complete_in_depth": True, "estimated_proceeds_eur": 149.0, "impact_below_best_bid_pct": 0.1},
                    "quote_volume_24h_eur": 20000.0,
                    "change_24h_pct": 5.0,
                },
            }],
            "execution_coverage": {"status_counts": {"OK": 1}},
        }

    def test_complete_digest_shows_exact_holdings_and_market_evidence(self):
        subject, body = bridge.build_digest(self.summary, now=self.now)
        self.assertEqual(subject, "SOLAIRE WALLET — relevé privé")
        for expected in ("FAKE-EUR", "2200.00", "2 350.00", "30.00", "+25.00%", "60.0%", "1/1 OK"):
            self.assertIn(expected, body.replace(" ", "") if expected == "2200.00" else body)

    def test_missing_cost_never_invents_total_pnl(self):
        self.summary["positions"][0]["pru_eur"] = None
        _, body = bridge.build_digest(self.summary, now=self.now)
        self.assertIn("PnL TOTAL : NON CALCULABLE", body)

    def test_stale_account_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "STALE_PRIVATE_WALLET"):
            bridge.build_digest(self.summary, now=self.now + 240)

    def test_stale_book_downgrades_quote_even_when_snapshot_is_fresh(self):
        self.summary["positions"][0]["execution_evidence"]["book_retrieved_at_utc"] = "2026-10-10T10:00:00+00:00"
        _, body = bridge.build_digest(self.summary, now=self.now)
        self.assertIn("fraîcheur non garantie", body)
        self.assertNotIn("Profondeur +/-1%", body)

    def test_inconsistent_totals_fail_closed(self):
        self.summary["wallet_value_eur"] = 3400.0
        with self.assertRaisesRegex(ValueError, "INCONSISTENT"):
            bridge.build_digest(self.summary, now=self.now)

    def test_wrong_recipient_never_sends(self):
        with patch.dict("os.environ", {"ALERT_GMAIL_USER": "sender@gmail.com", "GMAIL_APP_PASSWORD": "dummy", "ALERT_EMAIL_TO": "other@example.com"}):
            with patch.object(bridge, "send_email") as send:
                with redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(bridge.main(), 2)
                send.assert_not_called()
                self.assertNotIn("other@example.com", output.getvalue())

    def test_success_sends_directly_without_logging_wallet_content(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "snapshot.json"
            self.summary["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
            self.summary["positions"][0]["execution_evidence"]["book_retrieved_at_utc"] = self.summary["generated_at_utc"]
            self.summary["positions"][0]["execution_evidence"]["trades_retrieved_at_utc"] = self.summary["generated_at_utc"]
            p.write_text(json.dumps(self.summary))
            with patch.object(bridge, "SUMMARY", p), patch.object(bridge, "send_email") as send:
                with patch.dict("os.environ", {"ALERT_GMAIL_USER": "sender@gmail.com", "GMAIL_APP_PASSWORD": "dummy", "ALERT_EMAIL_TO": bridge.RECIPIENT}):
                    with redirect_stdout(io.StringIO()) as output:
                        self.assertEqual(bridge.main(), 0)
                    send.assert_called_once()
                    args = send.call_args.args
                    self.assertEqual(args[2], bridge.RECIPIENT)
                    self.assertIn("FAKE-EUR", args[4])
                    self.assertEqual(output.getvalue().strip(), "PRIVATE_WALLET_EMAIL_SENT")
                    self.assertNotIn("FAKE-EUR", output.getvalue())


if __name__ == "__main__":
    unittest.main()
