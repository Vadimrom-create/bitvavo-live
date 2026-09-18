from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile
import unittest

from research.adaptive_entry import promotion_signal, promote_and_enrich


class AdaptiveEntryTests(unittest.TestCase):
    def test_emerging_mover_is_promoted(self):
        row = {
            "market": "TEST-EUR",
            "quote_volume_24h_eur": 1_000_000,
            "change_24h_pct": 9.0,
            "m15": {},
            "trajectory": {},
            "ignition_score": 5.0,
            "opportunity_score": 5.0,
        }
        signal = promotion_signal(row, {}, 1_000)
        self.assertTrue(signal["eligible"])
        self.assertIn("EMERGING_MOVER_24H", signal["reasons"])

    def test_rank_surge_plus_ignition_is_promoted_before_large_24h_move(self):
        row = {
            "market": "TEST-EUR",
            "quote_volume_24h_eur": 500_000,
            "change_24h_pct": 1.5,
            "m15": {},
            "trajectory": {"drank_15m": 60},
            "ignition_score": 7.5,
            "opportunity_score": 6.0,
        }
        signal = promotion_signal(row, {}, 1_000)
        self.assertTrue(signal["eligible"])
        self.assertIn("RANK_SURGE", signal["reasons"])
        self.assertIn("HIGH_IGNITION", signal["reasons"])

    def test_promoted_market_is_re_evaluated_in_same_cycle_with_frozen_entry_rules(self):
        row = {
            "market": "TEST-EUR",
            "last": 100.0,
            "quote_volume_24h_eur": 1_000_000,
            "change_24h_pct": 5.0,
            "spread_pct": 0.05,
            "m15": {},
            "trajectory": {},
            "ignition_score": 8.0,
            "opportunity_score": 9.0,
            "trend_profile": {"ret7d": 5.0},
            "entry_score": 4.5,
            "risk_flags": ["NOT_ENTRY_ENRICHED"],
            "entry_mode": "UNKNOWN",
            "action_status": "WATCH",
            "buy_ready": False,
        }
        enrichment = {
            "5m": {"ch1": 0.2, "ch4": 1.0, "ch16": 2.0, "wick": 0.2, "dist8high": -0.2, "vr4": 2.0},
            "15m": {"ch1": 0.2, "ch4": 1.0, "ch16": 2.0, "wick": 0.2, "dist8high": -0.2, "vr4": 2.0},
            "1h": {"ch4": 2.0, "ch16": 4.0},
            "4h": {"ch4": 3.0},
            "book": {"bid_share": 0.60},
        }

        def fake_enrich(market, _details):
            return market, enrichment

        with tempfile.TemporaryDirectory() as d:
            old = os.getcwd()
            try:
                os.chdir(d)
                Path("v4_history.json").write_text(json.dumps({
                    "version": 4,
                    "markets": {
                        "TEST-EUR": {
                            "opportunity_confirm_count": 2,
                            "watch_until_ts": 2_000,
                            "peak_since_signal": 100.0,
                        }
                    },
                }), encoding="utf-8")
                audit = promote_and_enrich([row], {}, "2026-09-19T00:00:00+00:00", 1_000,
                                           {}, enrich_func=fake_enrich)
            finally:
                os.chdir(old)

        self.assertEqual(audit["promoted_count"], 1)
        self.assertGreaterEqual(row["entry_score"], 7.4)
        self.assertEqual(row["action_status"], "BUY_READY")
        self.assertTrue(row["buy_ready"])
        self.assertNotIn("NOT_ENTRY_ENRICHED", row["risk_flags"])


if __name__ == "__main__":
    unittest.main()
