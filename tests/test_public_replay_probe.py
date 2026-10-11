"""Deterministic offline tests for the optional public-data 24h research probe."""
from __future__ import annotations

import copy
import unittest
from datetime import datetime, timedelta, timezone

from scripts.run_public_replay_probe import select_time_window, probe, capture_closed_public_candles


T = datetime(2026, 10, 1, tzinfo=timezone.utc)


def tm(v):
    return v.isoformat().replace("+00:00", "Z")


def book_join_at(event_utc=T + timedelta(minutes=1)):
    return {
        "schema": "solaire_economic_machine_book_join_v1",
        "source": {"sha256": "a" * 64},
        "records": [{
            "decision_type": "BUY_SENT", "decision_id": "trade-1",
            "market": "AAA-EUR", "observed_at_utc": tm(event_utc),
            "execution_observation_id": "obs-1",
            "machine_plan": {
                "entry_limit_eur": 10, "stop_eur": 9, "tp1_eur": 12,
                "tp2_eur": 13, "structural_plan_valid": True,
            },
            "historical_book_evidence": {
                "book_observation_status": "MATCHED_PUBLIC_BOOK_ESTIMATE",
                "book_available_at_utc": tm(event_utc + timedelta(seconds=2)),
                "book_vs_decision_seconds": 2.0,
                "stake_estimates": {
                    "100": {"entry_book_covered": True, "same_snapshot_exit_book_covered": True},
                },
            },
        }],
    }


class PublicProbeTests(unittest.TestCase):
    def test_age_only_window_selects_signal_before_fetch(self):
        window = select_time_window(book_join_at(), T + timedelta(hours=72))
        self.assertEqual(window["buy_alert_count"], 1)
        self.assertEqual(window["model_event_count"], 1)
        self.assertEqual(window["unique_markets"], ["AAA-EUR"])

    def test_out_of_window_signal_is_not_selected(self):
        w = select_time_window(book_join_at(), T + timedelta(days=6))
        self.assertEqual(w["buy_alert_count"], 0)

    def test_missing_book_evidence_cancels_entire_study(self):
        x = book_join_at()
        x["records"][0]["historical_book_evidence"]["book_observation_status"] = "INVALID"
        report, bundle = probe(x, T + timedelta(hours=72),
                               capture_fn=lambda *_: self.fail("should not fetch"))
        self.assertEqual(report["status"], "NOT_READY_BOOK_EVIDENCE_GAPS")
        self.assertIsNone(bundle)

    def test_completely_synthetic_candles_are_never_claimed_as_bitvavo_fills(self):
        def pretend_capture(markets, asof):
            self.assertEqual(markets, ["AAA-EUR"])
            bars = []
            for minutes, high in ((5, 10.5), (10, 12.5)):
                bars.append({
                    "start_utc": tm(T + timedelta(minutes=minutes)),
                    "open": 10, "high": high, "low": 9.5, "close": 10,
                })
            return {
                "schema": "solaire_closed_5m_candles_bundle_v1",
                "asof_utc": tm(asof),
                "source_sha256": "synthetic-test-only",
                "markets": {"AAA-EUR": bars},
                "market_count_requested": 1,
                "market_count_received": 1,
                "fetch_error_by_market": {},
            }
        r, _ = probe(book_join_at(), T + timedelta(hours=72),
                     capture_fn=pretend_capture)
        self.assertEqual(r["model_only"]["status"], "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF")
        self.assertGreater(r["modeled_portfolio_pnl_eur"], 0)
        self.assertIsNone(r["real_bitvavo_pnl_eur"])
        self.assertFalse(r["r2_v4_comparison_ready"])

    def test_empty_window_does_not_fetch(self):
        r, b = probe(book_join_at(), T + timedelta(days=7), capture_fn=lambda *_: self.fail("no fetch"))
        self.assertEqual(r["status"], "NOT_READY_EMPTY_24H_COHORT")
        self.assertIsNone(b)


if __name__ == "__main__":
    unittest.main()
