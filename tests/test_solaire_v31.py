import unittest

from scripts.solaire_v31_shadow import _first_stop_observation
from research.solaire_v31 import (
    final_economic_score,
    preliminary_economic_score,
    select_execution_path,
    shadow_sizing,
    timing_variants,
)


def universe(*, r20=1.0, r1=2.0, r4=5.0, rs1=2.0, rs4=4.0, change24=8.0, extension=2.0):
    return {
        "change_24h_pct": change24,
        "quote_volume_24h_eur": 500000,
        "features": {
            "5m": {
                "return_4bar_pct": r20,
                "relative_volume": 2.0,
                "volume_4_vs_prev4": 1.8,
                "momentum_acceleration_pp": 0.5,
            },
            "15m": {
                "return_4bar_pct": r1,
                "return_16bar_pct": r4,
                "extension_ma20_pct": extension,
                "distance_to_breakout_pct": 0.3,
                "upper_wick_max": 0.2,
            },
        },
        "context": {
            "relative_strength_1h_pp": rs1,
            "relative_strength_4h_pp": rs4,
        },
    }


def candidate(*, early=6.0, v2_score=7.0, v3_score=7.0):
    return {
        "early_quant": {"score_0_10": early},
        "external": {
            "median_return_20m_pct": 1.0,
            "median_return_60m_pct": 2.0,
            "breadth_positive_20m_pct": 80.0,
        },
        "external_score": 5.0,
        "narrative_score": 4.0,
        "news_score": 2.0,
        "v2_score": v2_score,
        "opportunity_score": v3_score,
    }


def execution(stop_distance=6.0, spread=0.15, slippage=0.1):
    entry = 100.0
    stop = entry * (1 - stop_distance / 100)
    return {
        "ready": True,
        "spread_pct": spread,
        "depth": {"depth_slippage_pct": slippage},
        "plan": {
            "entry_eur": entry,
            "stop_eur": stop,
            "stop_distance_pct": stop_distance,
            "net_rr_tp1": 2.2,
        },
    }


class SolaireV31Tests(unittest.TestCase):
    def test_legacy_score_cannot_override_economic_evidence(self):
        strong = preliminary_economic_score(candidate(v2_score=5.0, v3_score=5.0), universe())
        weak = preliminary_economic_score(
            candidate(v2_score=10.0, v3_score=10.0),
            universe(r20=-1.0, r1=-0.5, r4=-3.0, rs1=-1.0, rs4=-4.0, change24=25.0, extension=8.0),
        )
        self.assertGreater(strong["preliminary_score"], weak["preliminary_score"])
        self.assertGreater(weak["contradiction_penalty"], 0)

    def test_multi_horizon_conflict_is_penalised(self):
        clean = preliminary_economic_score(candidate(), universe(r4=6.0, rs4=5.0))
        conflict = preliminary_economic_score(candidate(), universe(r4=-3.0, rs4=-4.0))
        self.assertGreater(clean["preliminary_score"], conflict["preliminary_score"])
        self.assertIn("negative_4h_trend", conflict["penalties"])
        self.assertIn("negative_4h_relative_strength", conflict["penalties"])

    def test_not_ready_execution_is_never_selectable(self):
        pre = preliminary_economic_score(candidate(), universe())
        result = final_economic_score(pre, {"ready": False, "reason": "WAITING_SPREAD"})
        self.assertFalse(result["selectable"])
        self.assertEqual(result["reason"], "WAITING_SPREAD")

    def test_risk_sizing_reduces_stake_for_wider_stop(self):
        tight = shadow_sizing(8.0, execution(stop_distance=4.0), 500000)
        wide = shadow_sizing(8.0, execution(stop_distance=9.0), 500000)
        self.assertTrue(tight["valid"])
        self.assertTrue(wide["valid"])
        self.assertGreater(tight["stake_eur"], wide["stake_eur"])

    def test_low_liquidity_caps_stake(self):
        sized = shadow_sizing(9.0, execution(stop_distance=3.0), 100000)
        self.assertTrue(sized["valid"])
        self.assertLessEqual(sized["stake_eur"], 100.0)


    def test_ondo_style_thesis_reentry_is_first_class_and_retryable(self):
        ready = {"ready": True, "reason": "ENTRY_READY_SHADOW", "plan": {"entry_eur": 1.0}}
        waiting = {"ready": False, "reason": "WAITING_INSUFFICIENT_NET_RISK_REWARD"}
        selected, path = select_execution_path({
            "execution": None,
            "thesis_reentry_hypothesis": True,
            "thesis_execution": ready,
        })
        self.assertIs(selected, ready)
        self.assertEqual(path, "THESIS_REENTRY")

        selected, path = select_execution_path({
            "execution": None,
            "thesis_reentry_hypothesis": True,
            "thesis_execution": waiting,
        })
        self.assertIs(selected, waiting)
        self.assertEqual(path, "THESIS_REENTRY_WAIT")

        selected, path = select_execution_path({
            "execution": None,
            "thesis_reentry_hypothesis": True,
            "thesis_execution": None,
        })
        self.assertIsNone(selected)
        self.assertEqual(path, "THESIS_REENTRY_PENDING_CHECK")

    def test_timing_variants_follow_v3_recorded_episode(self):
        candidate_row = {
            "timing_state": {
                "episode": 3,
                "persist30_recorded_episode": 3,
                "reclaim_recorded_episode": 2,
            }
        }
        paths = timing_variants(candidate_row)
        self.assertTrue(paths["PERSIST_30M"])
        self.assertFalse(paths["PULLBACK_RECLAIM"])

    def test_timing_variants_do_not_reimplement_thresholds(self):
        # Metrics alone are insufficient: V3 must have recorded the timing event.
        candidate_row = {
            "timing_state": {
                "episode": 4,
                "current_drift_pct": 0.5,
                "max_pullback_pct": -3.0,
                "reclaim_from_low_pct": 2.0,
            }
        }
        paths = timing_variants(candidate_row)
        self.assertFalse(paths["PERSIST_30M"])
        self.assertFalse(paths["PULLBACK_RECLAIM"])


class FakeStopClient:
    def __init__(self, *, trades=None, candles=None):
        self.trades = trades or []
        self.candles = candles or []

    def get(self, path, params=None, cache=False):
        if path.endswith("/trades"):
            return list(self.trades)
        if path.endswith("/candles"):
            return list(self.candles)
        raise AssertionError(path)


class SolaireStopCoverageTests(unittest.TestCase):
    def test_stop_touch_inside_opening_partial_minute_is_not_missed(self):
        client = FakeStopClient(trades=[
            {"timestamp": 1005_000, "price": "94.0", "amount": "1", "side": "sell"},
        ])
        hit = _first_stop_observation(
            client,
            "TEST-EUR",
            since_ts=1000.5,
            now=1010.0,
            stop_eur=95.0,
        )
        self.assertIsNotNone(hit)
        self.assertEqual(hit["coverage"], "EXACT_PUBLIC_TRADES_PARTIAL_MINUTE")
        self.assertEqual(hit["exit_eur"], 94.0)

    def test_stop_touch_in_completed_one_minute_bar_is_detected(self):
        client = FakeStopClient(
            trades=[],
            candles=[
                [1020_000, "100", "101", "94", "96", "10"],
            ],
        )
        hit = _first_stop_observation(
            client,
            "TEST-EUR",
            since_ts=1000.0,
            now=1130.0,
            stop_eur=95.0,
        )
        self.assertIsNotNone(hit)
        self.assertEqual(hit["coverage"], "COMPLETED_1M_BARS_BETWEEN_CHECKS")
        self.assertEqual(hit["exit_eur"], 95.0)


if __name__ == "__main__":
    unittest.main()
