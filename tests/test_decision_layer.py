import unittest

from research.decision_layer import (
    BUCKET_IMMEDIATE,
    BUCKET_LATENT,
    BUCKET_LIMIT,
    BUCKET_REENTRY,
    classify,
    decide,
)


def obs(market, opp, entry, trend, *, buy=False, action="WATCH", change24=0.0,
        quality_ok=True, exclusions=None, category="IGNITION"):
    return {
        "market": market,
        "price_eur": 1.0,
        "change_24h_pct": change24,
        "baseline": {
            "market": market,
            "opportunity_score": opp,
            "entry_score": entry,
            "trend_score": trend,
            "buy_ready": buy,
            "action_status": action,
            "risk_flags": [],
        },
        "category": category,
        "data_quality": {"ok": quality_ok, "reasons": [] if quality_ok else ["MISSING_5M"]},
        "exclusions": exclusions or [],
        "chase_risk": {"score": 0},
        "wick_setup": {"is_wick_setup": False},
        "recurrence": {"distinct_15m_periods": 1},
    }


class DecisionLayerTests(unittest.TestCase):
    def test_iost_like_signal_survives_weak_entry(self):
        row = classify(obs("IOST-EUR", 7.474, 4.5, 7.65))
        self.assertEqual(row["bucket"], BUCKET_LATENT)
        self.assertEqual(row["action"], "LATENT_ACCELERATOR")
        self.assertFalse(row["structural_vetoes"])

    def test_structural_data_failure_is_real_veto(self):
        row = classify(obs("IOST-EUR", 8.0, 4.0, 8.0, quality_ok=False))
        self.assertIsNone(row["bucket"])
        self.assertEqual(row["action"], "VETO_STRUCTUREL")
        self.assertIn("MISSING_5M", row["structural_vetoes"])

    def test_buy_ready_good_entry_is_immediate(self):
        row = classify(obs("AAA-EUR", 8.4, 7.2, 8.1, buy=True, action="BUY_READY"))
        self.assertEqual(row["bucket"], BUCKET_IMMEDIATE)

    def test_strong_structure_middle_entry_prefers_limit(self):
        row = classify(obs("BBB-EUR", 8.0, 6.2, 7.5, action="WATCH", change24=2.0))
        self.assertEqual(row["bucket"], BUCKET_LIMIT)

    def test_pullback_is_retained_for_reentry(self):
        row = classify(obs("CCC-EUR", 8.1, 6.1, 8.2, action="ENTRY_WINDOW", change24=-4.0))
        self.assertEqual(row["bucket"], BUCKET_REENTRY)

    def test_four_mandatory_buckets_are_always_present(self):
        result = decide([obs("IOST-EUR", 7.474, 4.5, 7.65)])
        self.assertEqual(
            set(result["bucket_winners"]),
            {BUCKET_IMMEDIATE, BUCKET_LIMIT, BUCKET_LATENT, BUCKET_REENTRY},
        )
        self.assertFalse(result["principles"]["production_orders_enabled"])


if __name__ == "__main__":
    unittest.main()
