import unittest

from monitoring.post_entry import METHOD, assess_post_entry


def features(ret, accel, extension):
    return {
        "valid": True,
        "return_4bar_pct": ret,
        "momentum_acceleration_pp": accel,
        "extension_ma20_pct": extension,
    }


class PostEntryAssessment(unittest.TestCase):
    def test_acceleration_disappearance_does_not_invalidate_open_thesis(self):
        result = assess_post_entry(
            market="TREAD-EUR",
            bid=1.03859,
            cost_basis_eur=1.0366,
            stop_eur=0.98799,
            timeframes={
                "15m": features(0.4, 0.2, 0.3),
                "1h": features(0.8, 0.1, 0.5),
                "4h": features(1.0, 0.2, 0.7),
            },
            source_alert={
                "signal_score": 9.701,
                "last_sent_entry_eur": 1.0366,
                "last_sent_stop_eur": 0.98799,
                "alert_lifecycle_state": "REVALIDATION_REQUIRED",
                "alert_lifecycle_reason": "CANDIDATE_NO_LONGER_IN_LATEST_SCAN",
            },
        )
        self.assertIn(result["thesis_status"], {"VALID", "VALID_STRONG"})
        self.assertFalse(result["acceleration_decay_is_invalidation"])
        self.assertFalse(result["is_entry_signal"])
        self.assertFalse(result["is_return_forecast"])
        self.assertEqual(result["method"], METHOD)
        self.assertEqual(
            result["source_entry_signal"]["lifecycle_reason"],
            "CANDIDATE_NO_LONGER_IN_LATEST_SCAN",
        )

    def test_stop_breach_is_actual_invalidation(self):
        result = assess_post_entry(
            market="ABC-EUR",
            bid=8.99,
            cost_basis_eur=10.0,
            stop_eur=9.0,
            timeframes={"15m": features(2, 1, 1)},
        )
        self.assertEqual(result["thesis_status"], "INVALIDATED_STOP_BREACH")
        self.assertEqual(result["management_outlook_24h"], 0.0)
        self.assertEqual(result["management_outlook_72h"], 0.0)

    def test_slower_timeframes_drive_longer_horizon_more_than_15m(self):
        strong_slow = assess_post_entry(
            market="ABC-EUR",
            bid=10.5,
            cost_basis_eur=10.0,
            stop_eur=9.0,
            timeframes={
                "15m": features(-1, -1, -1),
                "1h": features(1, 1, 1),
                "4h": features(1, 1, 1),
            },
        )
        weak_slow = assess_post_entry(
            market="ABC-EUR",
            bid=10.5,
            cost_basis_eur=10.0,
            stop_eur=9.0,
            timeframes={
                "15m": features(1, 1, 1),
                "1h": features(-1, -1, -1),
                "4h": features(-1, -1, -1),
            },
        )
        self.assertGreater(
            strong_slow["management_outlook_72h"],
            weak_slow["management_outlook_72h"],
        )
        self.assertLess(
            strong_slow["management_outlook_24h"],
            strong_slow["management_outlook_72h"],
        )

    def test_missing_timeframes_is_incomplete_not_bearish_forecast(self):
        result = assess_post_entry(
            market="ABC-EUR",
            bid=10.2,
            cost_basis_eur=10.0,
            stop_eur=9.0,
            timeframes={},
        )
        self.assertEqual(result["thesis_status"], "VALID_DATA_INCOMPLETE")
        self.assertIsNone(result["management_outlook_24h"])
        self.assertEqual(result["outlook_labels"]["72h"], "UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
