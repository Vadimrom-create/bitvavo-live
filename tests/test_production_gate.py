import unittest

from research.common import utc
from research.production_acceleration import acceleration_signal
from research.production_alerts import mark_sent, select_events
from research.production_gate import ACCELERATION_ACTION, build_alert_payload


def confirmed(score=7.1, evidence=4):
    return {
        "state": "CONFIRMED_ACCELERATION",
        "score": score,
        "evidence_count": evidence,
        "buyability": "REQUIRES_FINAL_EXECUTION_VALIDATION",
    }


def observation(*, quality_ok=True, volume=250000, price=1.0, change24=0.0, acceleration=None):
    return {
        "market": "TEST-EUR",
        "price_eur": price,
        "change_24h_pct": change24,
        "quote_volume_24h_eur": volume,
        "data_quality": {"ok": quality_ok, "reasons": [] if quality_ok else ["INVALID_5M"]},
        "acceleration": acceleration or confirmed(),
    }


class ProductionGateTests(unittest.TestCase):
    def test_confirmed_acceleration_is_candidate_without_old_layers(self):
        payload = build_alert_payload(
            [observation()],
            "2026-09-20T20:00:00+00:00",
        )
        self.assertEqual(len(payload["watch"]), 1)
        row = payload["watch"][0]
        self.assertEqual(row["action_status"], ACCELERATION_ACTION)
        self.assertEqual(row["signal_source"], "DIRECT_ACCELERATION")
        self.assertFalse(payload["v4_required"])
        self.assertFalse(payload["decision_layer_required"])

    def test_low_volume_does_not_erase_detection(self):
        payload = build_alert_payload(
            [observation(volume=1000)],
            "2026-09-20T20:00:00+00:00",
        )
        self.assertEqual(len(payload["watch"]), 1)
        self.assertEqual(payload["watch"][0]["quote_volume_24h_eur"], 1000)

    def test_bad_data_or_weak_acceleration_fails_closed(self):
        self.assertFalse(
            build_alert_payload(
                [observation(quality_ok=False)],
                "2026-09-20T20:00:00+00:00",
            )["watch"]
        )
        self.assertFalse(
            build_alert_payload(
                [observation(acceleration=confirmed(score=6.0))],
                "2026-09-20T20:00:00+00:00",
            )["watch"]
        )

    def test_large_24h_move_does_not_erase_confirmed_acceleration(self):
        payload = build_alert_payload(
            [observation(change24=55.0)],
            "2026-09-20T20:00:00+00:00",
        )
        self.assertEqual(len(payload["watch"]), 1)


class PureAccelerationTests(unittest.TestCase):
    def test_detector_has_no_chase_or_24h_veto(self):
        obs = {
            "change_24h_pct": 80.0,
            "chase_risk": {"score": 10.0},
            "category": "TOO LATE",
            "features": {
                "5m": {
                    "valid": True,
                    "relative_volume": 4.0,
                    "volume_4_vs_prev4": 4.0,
                    "return_4bar_pct": 3.0,
                    "momentum_acceleration_pp": 3.0,
                    "distance_to_breakout_pct": 1.0,
                },
                "15m": {
                    "valid": True,
                    "relative_volume": 3.0,
                    "return_1bar_pct": 2.0,
                    "return_4bar_pct": 4.0,
                },
            },
        }
        result = acceleration_signal(obs)
        self.assertEqual(result["state"], "CONFIRMED_ACCELERATION")
        self.assertEqual(result["buyability"], "REQUIRES_FINAL_EXECUTION_VALIDATION")


class ProductionAlertPolicyTests(unittest.TestCase):
    NOW = 1_788_883_200.0

    def payload(self, markets=("A-EUR",)):
        return {
            "generated_at_utc": utc(self.NOW),
            "watch": [
                {
                    "market": market,
                    "action_status": "ACCELERATION_READY",
                    "signal_score": 7.0,
                    "quote_volume_24h_eur": 200000,
                    "data_quality": {"ok": True},
                    "last": 1.0,
                }
                for market in markets
            ],
        }

    def test_no_global_cooldown_between_independent_markets(self):
        events, state = select_events(self.payload(("A-EUR",)), {}, self.NOW)
        state = mark_sent(state, events[0], self.NOW)
        events, _ = select_events(self.payload(("A-EUR", "B-EUR")), state, self.NOW + 60)
        self.assertEqual([row["market"] for row in events], ["B-EUR"])

    def test_continuous_episode_is_not_repeated(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        state = mark_sent(state, events[0], self.NOW)
        self.assertFalse(select_events(self.payload(), state, self.NOW + 60)[0])

    def test_new_episode_same_market_has_no_four_hour_wait(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        state = mark_sent(state, events[0], self.NOW)
        _, state = select_events(
            {"generated_at_utc": utc(self.NOW + 60), "watch": []},
            state,
            self.NOW + 60,
        )
        events, _ = select_events(self.payload(), state, self.NOW + 120)
        self.assertEqual(len(events), 1)

    def test_failed_delivery_remains_retryable(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        self.assertTrue(events)
        self.assertTrue(select_events(self.payload(), state, self.NOW + 60)[0])


if __name__ == "__main__":
    unittest.main()
