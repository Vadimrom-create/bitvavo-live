import unittest

from research.persistent_building import qualifies, update_shadow


class PersistentBuildingShadowTests(unittest.TestCase):
    def metrics(self, **overrides):
        base = {
            "samples_6h": 4,
            "span_minutes": 35.0,
            "net_progress_pct": 2.5,
            "max_score": 5.8,
            "positive_step_ratio": 0.67,
        }
        base.update(overrides)
        return base

    def test_qualification_is_shadow_only_threshold(self):
        self.assertTrue(qualifies(self.metrics()))
        self.assertFalse(qualifies(self.metrics(samples_6h=3)))
        self.assertFalse(qualifies(self.metrics(span_minutes=29.9)))
        self.assertFalse(qualifies(self.metrics(net_progress_pct=1.99)))
        self.assertFalse(qualifies(self.metrics(max_score=4.99)))
        self.assertFalse(qualifies(self.metrics(positive_step_ratio=0.59)))

    def payload(self, ts, price, score=5.5, state="BUILDING_ACCELERATION"):
        return {
            "generated_at_utc": ts,
            "tracking": [
                {
                    "market": "FET-EUR",
                    "last": price,
                    "signal_score": score,
                    "signal_state": state,
                }
            ],
        }

    def test_repeated_building_creates_one_shadow_event(self):
        state = {}
        journal = {}
        rows = [
            ("2026-09-21T08:00:00+00:00", 0.1500, 5.1),
            ("2026-09-21T08:10:00+00:00", 0.1510, 5.3),
            ("2026-09-21T08:20:00+00:00", 0.1520, 5.4),
            ("2026-09-21T08:35:00+00:00", 0.1540, 5.8),
        ]
        for ts, price, score in rows:
            state, journal, status = update_shadow(
                self.payload(ts, price, score),
                state,
                journal,
            )
        self.assertEqual(status["active_shadow_markets"], 1)
        self.assertEqual(status["new_shadow_events"], 1)
        self.assertEqual(len(journal["events"]), 1)
        event = journal["events"][0]
        self.assertEqual(event["shadow_type"], "PERSISTENT_BUILDING")
        self.assertFalse(event["affects_detection"])
        self.assertFalse(event["affects_buy_gate"])
        self.assertFalse(event["affects_email"])

        # Same snapshot is idempotent and does not create another event.
        state, journal, status = update_shadow(
            self.payload("2026-09-21T08:35:00+00:00", 0.1540, 5.8),
            state,
            journal,
        )
        self.assertEqual(len(journal["events"]), 1)
        self.assertEqual(status["new_shadow_events"], 0)

    def test_later_confirmation_is_attached_without_changing_gate(self):
        state = {}
        journal = {}
        for ts, price in [
            ("2026-09-21T08:00:00+00:00", 1.00),
            ("2026-09-21T08:10:00+00:00", 1.01),
            ("2026-09-21T08:20:00+00:00", 1.02),
            ("2026-09-21T08:35:00+00:00", 1.04),
        ]:
            state, journal, _ = update_shadow(self.payload(ts, price), state, journal)

        state, journal, _ = update_shadow(
            self.payload(
                "2026-09-21T08:40:00+00:00",
                1.05,
                score=7.2,
                state="CONFIRMED_ACCELERATION",
            ),
            state,
            journal,
        )
        event = journal["events"][0]
        self.assertTrue(event["confirmed_after_detection"])
        self.assertAlmostEqual(event["confirmation"]["minutes_after_shadow"], 5.0)
        self.assertFalse(event["affects_buy_gate"])

    def test_non_building_does_not_create_shadow_sample(self):
        state, journal, status = update_shadow(
            self.payload(
                "2026-09-21T08:00:00+00:00",
                1.0,
                score=8.0,
                state="CONFIRMED_ACCELERATION",
            ),
            {},
            {},
        )
        self.assertEqual(status["active_shadow_markets"], 0)
        self.assertEqual(len(journal["events"]), 0)


if __name__ == "__main__":
    unittest.main()
