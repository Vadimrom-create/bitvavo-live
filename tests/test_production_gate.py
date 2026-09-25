import unittest
from unittest.mock import patch

from research.common import utc
from research.production_acceleration import acceleration_signal
from research.production_alerts import mark_sent, mark_suppressed, select_events
from research.production_gate import ACCELERATION_ACTION, build_alert_payload
from scripts.production_scan import observation as scan_observation
from scripts.send_production_buy_alert import closed_5m_lows, prior_buy_thesis_active, structural_range_ready


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


    def test_building_acceleration_is_tracked_but_not_actionable(self):
        building = confirmed(score=5.2, evidence=3)
        building["state"] = "BUILDING_ACCELERATION"
        payload = build_alert_payload(
            [observation(acceleration=building)],
            "2026-09-20T20:00:00+00:00",
        )
        self.assertEqual(len(payload["tracking"]), 1)
        self.assertEqual(payload["tracking"][0]["signal_state"], "BUILDING_ACCELERATION")
        self.assertFalse(payload["watch"])


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
        self.assertTrue(result["timeframe_confirmation_15m"])
        self.assertEqual(result["confirmation_scope"], "MULTI_TIMEFRAME")

    def test_confirmed_state_can_be_fast_composite_without_15m_evidence(self):
        obs = {
            "features": {
                "5m": {
                    "valid": True,
                    "relative_volume": 4.0,
                    "volume_4_vs_prev4": 4.0,
                    "return_4bar_pct": 4.0,
                    "momentum_acceleration_pp": 4.0,
                    "distance_to_breakout_pct": 1.0,
                },
                "15m": {
                    "valid": True,
                    "relative_volume": 0.5,
                    "return_1bar_pct": -1.0,
                    "return_4bar_pct": 0.0,
                },
            },
        }
        result = acceleration_signal(obs)
        self.assertEqual(result["state"], "CONFIRMED_ACCELERATION")
        self.assertFalse(result["timeframe_confirmation_15m"])
        self.assertEqual(result["confirmation_scope"], "FAST_COMPOSITE_ONLY")
        self.assertFalse(result["evidence_flags"]["confirmation_15m"])


class ProductionFreshnessTests(unittest.TestCase):
    def test_post_signal_retrieval_time_is_not_a_future_data_error(self):
        signal = 1_788_883_200.0
        data = {
            "meta": {"market": "TEST-EUR"},
            "timeframes": {
                "5m": {
                    "features": {"valid": True},
                    "candles": [{"t": int((signal - 300) * 1000)}],
                    "retrieved_at_utc": utc(signal + 60),
                },
                "15m": {
                    "features": {"valid": True},
                    "candles": [{"t": int((signal - 900) * 1000)}],
                    "retrieved_at_utc": utc(signal + 65),
                },
            },
        }
        ticker = {"last": "1", "open": "1", "volumeQuote": "100000"}
        with patch("scripts.production_scan.time.time", return_value=signal + 70):
            obs = scan_observation(data, ticker, signal, utc(signal + 1))
        self.assertTrue(obs["data_quality"]["ok"], obs["data_quality"])
        self.assertNotIn("FUTURE_RETRIEVAL_TIMESTAMP", obs["data_quality"]["reasons"])


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


    def test_suppressed_episode_is_handled_without_claiming_delivery(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        state = mark_suppressed(
            state,
            events[0],
            self.NOW,
            "PRIOR_BUY_THESIS_STILL_ACTIVE",
        )
        self.assertFalse(select_events(self.payload(), state, self.NOW + 60)[0])
        market = state["markets"]["A-EUR"]
        self.assertEqual(market["handled_episode"], 1)
        self.assertNotIn("sent_episode", market)
        self.assertEqual(
            market["last_suppressed_reason"],
            "PRIOR_BUY_THESIS_STILL_ACTIVE",
        )

    def test_mark_sent_persists_structural_thesis(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        trade = {
            "entry_eur": 1.01,
            "stop_eur": 0.95,
            "tp1_eur": 1.13,
            "stop_distance_pct": 5.94,
        }
        state = mark_sent(state, events[0], self.NOW, trade)
        market = state["markets"]["A-EUR"]
        self.assertEqual(market["handled_episode"], 1)
        self.assertEqual(market["sent_episode"], 1)
        self.assertEqual(market["last_sent_stop_eur"], 0.95)


class ProductionStructuralRangeTests(unittest.TestCase):
    def test_structural_range_below_six_percent_waits(self):
        self.assertFalse(structural_range_ready({"consolidation_range_pct": 5.99}))

    def test_structural_range_at_or_above_six_percent_is_ready(self):
        self.assertTrue(structural_range_ready({"consolidation_range_pct": 6.0}))
        self.assertTrue(structural_range_ready({"consolidation_range_pct": 8.5}))

    def test_missing_structural_range_fails_closed(self):
        self.assertFalse(structural_range_ready({}))


class ProductionPriorThesisTests(unittest.TestCase):
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

    def selected(self, low=0.97, ask=1.02):
        start = int((self.NOW - 300) * 1000)
        return {
            "row": {"market": "A-EUR"},
            "quote": {"ask": ask},
            "candles_5m": [
                {"t": start, "l": low},
            ],
        }

    def state(self, sent_offset=600, stop=0.95):
        return {
            "markets": {
                "A-EUR": {
                    "last_sent_ts": self.NOW - sent_offset,
                    "last_sent_stop_eur": stop,
                }
            }
        }

    def test_prior_thesis_stays_active_above_stop(self):
        active, reason = prior_buy_thesis_active(
            self.state(),
            self.selected(low=0.97),
            self.NOW,
        )
        self.assertTrue(active)
        self.assertEqual(reason, "PRIOR_BUY_THESIS_STILL_ACTIVE")

    def test_new_acceleration_episode_is_not_suppressed_by_old_thesis(self):
        state = self.state()
        state["markets"]["A-EUR"]["sent_episode"] = 1
        selected = self.selected(low=0.97)
        selected["row"]["episode"] = 2
        active, reason = prior_buy_thesis_active(state, selected, self.NOW)
        self.assertFalse(active)
        self.assertEqual(reason, "NEW_ACCELERATION_EPISODE")

    def test_same_acceleration_episode_remains_deduplicated(self):
        state = self.state()
        state["markets"]["A-EUR"]["sent_episode"] = 2
        selected = self.selected(low=0.97)
        selected["row"]["episode"] = 2
        active, reason = prior_buy_thesis_active(state, selected, self.NOW)
        self.assertTrue(active)
        self.assertEqual(reason, "PRIOR_BUY_THESIS_STILL_ACTIVE")

    def test_stop_breach_reopens_market_for_new_buy_thesis(self):
        active, reason = prior_buy_thesis_active(
            self.state(),
            self.selected(low=0.90),
            self.NOW,
        )
        self.assertFalse(active)
        self.assertEqual(reason, "PRIOR_BUY_THESIS_INVALIDATED")

    def test_old_thesis_expires_after_24h(self):
        active, reason = prior_buy_thesis_active(
            self.state(sent_offset=25 * 60 * 60),
            self.selected(),
            self.NOW,
        )
        self.assertFalse(active)
        self.assertEqual(reason, "PRIOR_BUY_THESIS_EXPIRED")


    def test_full_24h_5m_history_is_not_truncated_to_100_bars(self):
        raw = []
        start = int((self.NOW - 150 * 300) * 1000)
        for i in range(150):
            t = start + i * 300_000
            raw.append([t, "1.0", "1.1", "0.9", "1.0", "10"])
        lows = closed_5m_lows(raw, self.NOW)
        self.assertEqual(len(lows), 150)
        self.assertEqual(lows[0]["t"], start)


    def test_building_to_confirmed_preserves_episode_start(self):
        building_payload = {
            "generated_at_utc": utc(self.NOW),
            "tracking": [{
                "market": "A-EUR",
                "signal_state": "BUILDING_ACCELERATION",
                "signal_score": 5.0,
                "quote_volume_24h_eur": 200000,
                "data_quality": {"ok": True},
                "last": 1.0,
                "acceleration": {"state": "BUILDING_ACCELERATION"},
            }],
            "watch": [],
        }
        events, state = select_events(building_payload, {}, self.NOW)
        self.assertFalse(events)
        self.assertEqual(state["markets"]["A-EUR"]["episode"], 1)

        confirmed_payload = {
            "generated_at_utc": utc(self.NOW + 300),
            "tracking": [{
                "market": "A-EUR",
                "signal_state": "CONFIRMED_ACCELERATION",
                "signal_score": 7.0,
                "quote_volume_24h_eur": 200000,
                "data_quality": {"ok": True},
                "last": 1.02,
                "acceleration": {"state": "CONFIRMED_ACCELERATION"},
            }],
            "watch": [{
                "market": "A-EUR",
                "signal_state": "CONFIRMED_ACCELERATION",
                "action_status": "ACCELERATION_READY",
                "signal_score": 7.0,
                "quote_volume_24h_eur": 200000,
                "data_quality": {"ok": True},
                "last": 1.02,
                "acceleration": {"state": "CONFIRMED_ACCELERATION"},
            }],
        }
        events, state = select_events(confirmed_payload, state, self.NOW + 300)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["signal_phase"], "FIRST_CONFIRMATION")
        self.assertAlmostEqual(events[0]["episode_start_price"], 1.0)
        self.assertAlmostEqual(events[0]["episode_extension_pct"], 2.0, places=3)
        self.assertEqual(events[0]["episode_age_seconds"], 300)

    def test_confirmed_building_confirmed_stays_same_episode(self):
        events, state = select_events(self.payload(), {}, self.NOW)
        state = mark_sent(state, events[0], self.NOW)

        building_payload = {
            "generated_at_utc": utc(self.NOW + 300),
            "tracking": [{
                "market": "A-EUR",
                "signal_state": "BUILDING_ACCELERATION",
                "signal_score": 5.3,
                "quote_volume_24h_eur": 200000,
                "data_quality": {"ok": True},
                "last": 1.01,
                "acceleration": {"state": "BUILDING_ACCELERATION"},
            }],
            "watch": [],
        }
        self.assertFalse(select_events(building_payload, state, self.NOW + 300)[0])
        _, state = select_events(building_payload, state, self.NOW + 300)
        events, state = select_events(self.payload(), state, self.NOW + 600)
        self.assertFalse(events)
        self.assertEqual(state["markets"]["A-EUR"]["episode"], 1)

    def test_stronger_confirmation_is_prioritized_over_less_extended_weaker_signal(self):
        state = {
            "markets": {
                "A-EUR": {
                    "active": True, "episode": 1, "episode_started_ts": self.NOW - 300,
                    "episode_start_price": 1.0, "episode_start_score": 5.0,
                },
                "B-EUR": {
                    "active": True, "episode": 1, "episode_started_ts": self.NOW - 300,
                    "episode_start_price": 1.0, "episode_start_score": 5.0,
                },
            }
        }
        payload = {
            "generated_at_utc": utc(self.NOW),
            "tracking": [
                {"market": "A-EUR", "signal_state": "CONFIRMED_ACCELERATION", "signal_score": 6.7,
                 "quote_volume_24h_eur": 200000, "data_quality": {"ok": True}, "last": 1.01,
                 "acceleration": {"state": "CONFIRMED_ACCELERATION"}},
                {"market": "B-EUR", "signal_state": "CONFIRMED_ACCELERATION", "signal_score": 9.5,
                 "quote_volume_24h_eur": 200000, "data_quality": {"ok": True}, "last": 1.08,
                 "acceleration": {"state": "CONFIRMED_ACCELERATION"}},
            ],
            "watch": [
                {"market": "A-EUR", "signal_state": "CONFIRMED_ACCELERATION",
                 "action_status": "ACCELERATION_READY", "signal_score": 6.7,
                 "quote_volume_24h_eur": 200000, "data_quality": {"ok": True}, "last": 1.01,
                 "acceleration": {"state": "CONFIRMED_ACCELERATION"}},
                {"market": "B-EUR", "signal_state": "CONFIRMED_ACCELERATION",
                 "action_status": "ACCELERATION_READY", "signal_score": 9.5,
                 "quote_volume_24h_eur": 200000, "data_quality": {"ok": True}, "last": 1.08,
                 "acceleration": {"state": "CONFIRMED_ACCELERATION"}},
            ],
        }
        events, _ = select_events(payload, state, self.NOW)
        self.assertEqual([e["market"] for e in events], ["B-EUR", "A-EUR"])


if __name__ == "__main__":
    unittest.main()
