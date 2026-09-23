import unittest

from research.solaire_v3 import advance_persistent_thesis


class PersistentThesisTests(unittest.TestCase):
    def row(self, price, fresh=False, context=False, external=0.0, evidence=0, long_support=False):
        return {
            "price_eur": price,
            "fresh_opportunity_trigger": fresh,
            "context_watch": context,
            "external_score": external,
            "early_quant": {"evidence_count": evidence},
            "opportunity_score": 5.0,
            "horizon_class": "TACTICAL",
            "long_trend": {"support": long_support},
        }

    def test_no_thesis_without_fresh_trigger(self):
        self.assertEqual(advance_persistent_thesis({}, self.row(100), 1000), {})

    def test_fresh_trigger_opens_thesis(self):
        t = advance_persistent_thesis({}, self.row(100, fresh=True), 1000)
        self.assertTrue(t["active"])
        self.assertEqual(t["state"], "ACTIVE_THESIS")
        self.assertEqual(t["opened_price_eur"], 100)

    def test_thesis_survives_missing_short_acceleration(self):
        t = advance_persistent_thesis({}, self.row(100, fresh=True), 1000)
        t = advance_persistent_thesis(t, self.row(101, fresh=False, context=False, evidence=0), 2000)
        self.assertTrue(t["active"])
        self.assertIn(t["state"], {"ACTIVE_THESIS", "CONTINUATION_THESIS"})

    def test_pullback_then_reclaim_creates_reentry_state(self):
        t = advance_persistent_thesis({}, self.row(100, fresh=True), 1000)
        t = advance_persistent_thesis(t, self.row(97, evidence=2), 2000)
        self.assertEqual(t["state"], "PULLBACK_THESIS")
        t = advance_persistent_thesis(t, self.row(98.2, evidence=2), 3000)
        self.assertEqual(t["state"], "REENTRY_READY_THESIS")

    def test_large_anchor_drawdown_invalidates(self):
        t = advance_persistent_thesis({}, self.row(100, fresh=True), 1000)
        t = advance_persistent_thesis(t, self.row(87, evidence=2), 2000)
        self.assertFalse(t["active"])
        self.assertEqual(t["state"], "INVALIDATED_THESIS")


if __name__ == "__main__":
    unittest.main()
