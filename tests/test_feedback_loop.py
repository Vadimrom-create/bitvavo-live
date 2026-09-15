import unittest

from email_alert_v4 import select_events
from research.common import utc
from research.evaluation import HORIZONS, market_control
from research.feedback_loop import (
    acceleration_signal,
    current_candidates,
    update_candidate_memory,
)
from research.history import connect, ingest


NOW = 1_788_883_200.0


def feature5():
    return {
        "valid": True,
        "return_4bar_pct": 4.0,
        "momentum_acceleration_pp": 3.0,
        "relative_volume": 2.5,
        "volume_4_vs_prev4": 2.0,
        "distance_to_breakout_pct": 1.0,
    }


def feature15():
    return {
        "valid": True,
        "return_1bar_pct": 1.5,
        "return_4bar_pct": 3.0,
        "relative_volume": 1.5,
    }


def acceleration_obs():
    return {
        "market": "FAST-EUR",
        "price_eur": 1.0,
        "change_24h_pct": 4.0,
        "category": "NO SETUP",
        "decision": "NO SETUP",
        "baseline": None,
        "data_quality": {"ok": True, "reasons": []},
        "features": {"5m": feature5(), "15m": feature15()},
        "chase_risk": {"score": 2},
        "trade_plan": None,
    }


class AccelerationTests(unittest.TestCase):
    def test_independent_detector_surfaces_non_v4_market_but_cannot_alert(self):
        obs = acceleration_obs()
        obs["acceleration"] = acceleration_signal(obs)
        self.assertTrue(obs["acceleration"]["detected"])
        self.assertEqual(obs["acceleration"]["state"], "CONFIRMED_ACCELERATION")
        self.assertFalse(obs["acceleration"]["alert_eligible"])
        candidates = current_candidates([{"market": "FAST-EUR", "rank_score": 0}], [obs])
        self.assertEqual(candidates[0]["sources"], ["ACCELERATION"])
        self.assertFalse(candidates[0]["buyable_now"])

    def test_invalid_data_fails_closed(self):
        obs = acceleration_obs()
        obs["features"]["5m"] = {"valid": False, "reasons": ["MISSING_5M"]}
        result = acceleration_signal(obs)
        self.assertEqual(result["state"], "DATA_UNAVAILABLE")
        self.assertFalse(result["detected"])

    def test_unrelated_entry_input_failure_does_not_block_acceleration(self):
        obs = acceleration_obs()
        obs["data_quality"] = {"ok": False, "reasons": ["ENTRY_INPUTS_UNAVAILABLE"]}
        result = acceleration_signal(obs)
        self.assertEqual(result["state"], "CONFIRMED_ACCELERATION")
        self.assertFalse(result["alert_eligible"])

    def test_memory_is_full_for_24h_decays_then_expires_at_72h(self):
        current = [{
            "market": "FAST-EUR", "price_eur": 1, "signal_score": 8,
            "sources": ["ACCELERATION"], "buyable_now": False,
            "buyability": "WATCH_ONLY", "alert_eligible": False,
        }]
        first = update_candidate_memory({}, current, NOW)
        at_12h = update_candidate_memory(first, [], NOW + 12 * 3600)
        self.assertEqual(at_12h["candidates"][0]["memory_score"], 8)
        self.assertEqual(at_12h["candidates"][0]["memory_state"], "MEMORY_24H")
        at_48h = update_candidate_memory(at_12h, [], NOW + 48 * 3600)
        self.assertEqual(at_48h["candidates"][0]["memory_score"], 4)
        self.assertEqual(at_48h["candidates"][0]["memory_state"], "MEMORY_DECAY_24_72H")
        expired = update_candidate_memory(at_48h, [], NOW + 72 * 3600)
        self.assertEqual(expired["candidates"], [])

    def test_memory_never_becomes_email_input(self):
        payload = {
            "generated_at_utc": utc(NOW),
            "watch": [],
            "candidate_memory": {"candidates": [{"market": "FAST-EUR", "buyable_now": True}]},
        }
        self.assertEqual(select_events(payload, {}, NOW)[0], [])


class MultilayerDiagnosticTests(unittest.TestCase):
    def test_missing_baseline_is_descriptive_coverage_not_reference_false_negative(self):
        from research.feedback_diagnostics import layers
        obs = acceleration_obs()
        result = layers(obs, acceleration_signal(obs), None, utc(NOW))
        self.assertEqual(result['diagnostic_layer'], 'SCANNER_COVERAGE')
        self.assertEqual(result['attribution'], 'DESCRIPTIVE_NOT_CAUSAL')
        self.assertNotIn('false_negative', result)
        self.assertEqual(result['reference_event_policy'], 'HISTORY_CONTINUITY_V2_UNCHANGED')


if __name__ == "__main__":
    unittest.main()
