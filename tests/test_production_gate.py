import unittest

from research.production_gate import ACCELERATION_ACTION, build_alert_payload


def observation(*, baseline=None, acceleration=None, quality_ok=True, volume=250000, price=1.0):
    return {
        "market": "TEST-EUR",
        "price_eur": price,
        "quote_volume_24h_eur": volume,
        "baseline": baseline,
        "category": "IGNITION",
        "data_quality": {"ok": quality_ok, "reasons": [] if quality_ok else ["INVALID_5M"]},
        "trade_plan": {"valid": True, "entry_eur": price},
        "acceleration": acceleration or {
            "state": "NO_ACCELERATION",
            "score": 0.0,
            "evidence_count": 0,
            "buyability": "NOT_APPLICABLE",
        },
        "features": {"5m": {"valid": True}, "15m": {"valid": True}},
        "exclusions": [],
        "chase_risk": {"score": 0},
        "wick_setup": {"is_wick_setup": False},
        "recurrence": {"distinct_15m_periods": 1},
        "decision": "SURVEILLE",
    }


class ProductionGateTests(unittest.TestCase):
    def test_confirmed_full_universe_acceleration_can_alert_without_v4(self):
        obs = observation(acceleration={
            "state": "CONFIRMED_ACCELERATION",
            "score": 7.1,
            "evidence_count": 4,
            "buyability": "REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION",
        })
        payload = build_alert_payload([obs], [], "2026-09-20T20:00:00+00:00")
        self.assertEqual(len(payload["watch"]), 1)
        row = payload["watch"][0]
        self.assertEqual(row["action_status"], ACCELERATION_ACTION)
        self.assertEqual(row["signal_source"], "DIRECT_ACCELERATION")
        self.assertTrue(row["buy_ready"])
        self.assertFalse(payload["oracle_required"])

    def test_too_late_or_bad_data_acceleration_fails_closed(self):
        for kwargs in (
            {"quality_ok": False},
            {"acceleration": {
                "state": "CONFIRMED_ACCELERATION",
                "score": 7.1,
                "evidence_count": 4,
                "buyability": "DETECTED_BUT_TOO_LATE",
            }},
            {"volume": 1000},
        ):
            base = {
                "acceleration": {
                    "state": "CONFIRMED_ACCELERATION",
                    "score": 7.1,
                    "evidence_count": 4,
                    "buyability": "REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION",
                }
            }
            base.update(kwargs)
            obs = observation(**base)
            self.assertFalse(build_alert_payload([obs], [], "2026-09-20T20:00:00+00:00")["watch"])

    def test_v4_buy_is_preserved_and_acceleration_is_additive(self):
        baseline = {
            "market": "TEST-EUR",
            "last": 1.0,
            "buy_ready": True,
            "action_status": "BUY_READY",
            "opportunity_score": 8.8,
            "entry_score": 7.6,
            "trend_score": 8.0,
            "risk_flags": [],
            "quote_volume_24h_eur": 300000,
        }
        obs = observation(
            baseline=baseline,
            acceleration={
                "state": "CONFIRMED_ACCELERATION",
                "score": 7.2,
                "evidence_count": 4,
                "buyability": "REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION",
            },
        )
        payload = build_alert_payload([obs], [obs], "2026-09-20T20:00:00+00:00")
        row = payload["watch"][0]
        self.assertIn("V4", row["signal_sources"])
        self.assertIn("DIRECT_ACCELERATION", row["signal_sources"])
        self.assertEqual(row["action_status"], "BUY_READY")


if __name__ == "__main__":
    unittest.main()
