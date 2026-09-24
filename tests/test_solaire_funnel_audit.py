import unittest

from research.solaire_funnel_audit import (
    advance_funnel_memory,
    classify_snapshot,
    should_track,
)


class SolaireFunnelAuditTests(unittest.TestCase):
    def test_building_signal_is_kept_as_control(self):
        v3 = {
            "v2_state": "BUILDING_ACCELERATION",
            "early_quant": {"ready": False, "score_0_10": 2.0, "evidence_count": 1},
        }
        self.assertTrue(should_track(v3, {}))
        snap = classify_snapshot(v3, {})
        self.assertEqual(snap["stage"], "EARLY_CONTROL")
        self.assertEqual(snap["loss_family"], "CONTROL_NOT_YET_CREDIBLE")

    def test_confirmed_but_not_executable_is_post_confirmation_loss(self):
        v3 = {
            "v2_state": "CONFIRMED_ACCELERATION",
            "entry_hypothesis": True,
            "credible_opportunity": True,
            "execution": {"ready": False, "reason": "WAITING_STOP_GEOMETRY"},
        }
        snap = classify_snapshot(v3, {"selectable": False, "selection_reason": "WAITING_STOP_GEOMETRY"})
        self.assertEqual(snap["stage"], "CONFIRMED_WAITING_EXECUTION")
        self.assertEqual(snap["loss_family"], "POST_CONFIRMATION_EXECUTION")
        self.assertEqual(snap["blocking_reason"], "WAITING_STOP_GEOMETRY")

    def test_execution_ready_but_rejected_is_post_execution_loss(self):
        v3 = {
            "v2_state": "CONFIRMED_ACCELERATION",
            "entry_hypothesis": True,
            "credible_opportunity": True,
            "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
        }
        v31 = {
            "selectable": False,
            "selection_reason": "ECONOMIC_SCORE_BELOW_THRESHOLD",
            "economic_score": 5.7,
            "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
        }
        snap = classify_snapshot(v3, v31)
        self.assertEqual(snap["stage"], "EXECUTION_READY_REJECTED")
        self.assertEqual(snap["loss_family"], "POST_EXECUTION_SELECTION")
        self.assertEqual(snap["blocking_reason"], "ECONOMIC_SCORE_BELOW_THRESHOLD")

    def test_selectable_is_resolved(self):
        v3 = {
            "v2_state": "CONFIRMED_ACCELERATION",
            "credible_opportunity": True,
            "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
        }
        v31 = {
            "selectable": True,
            "selection_reason": "SELECTABLE",
            "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
        }
        snap = classify_snapshot(v3, v31)
        self.assertEqual(snap["stage"], "SELECTABLE")
        self.assertIsNone(snap["loss_family"])
        self.assertIsNone(snap["blocking_reason"])

    def test_memory_records_cost_of_waiting_between_stages(self):
        first = classify_snapshot(
            {
                "near_miss_opportunity": True,
                "credible_opportunity": True,
                "entry_hypothesis": False,
                "v2_state": "BUILDING_ACCELERATION",
            },
            {},
        )
        state, changed = advance_funnel_memory(
            None,
            snapshot=first,
            now=1000.0,
            price_eur=100.0,
        )
        self.assertTrue(changed)
        self.assertEqual(state["first_credible_price_eur"], 100.0)

        second = classify_snapshot(
            {
                "credible_opportunity": True,
                "entry_hypothesis": True,
                "v2_state": "CONFIRMED_ACCELERATION",
                "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
            },
            {
                "selectable": False,
                "selection_reason": "ECONOMIC_SCORE_BELOW_THRESHOLD",
                "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
            },
        )
        state, changed = advance_funnel_memory(
            state,
            snapshot=second,
            now=1600.0,
            price_eur=112.0,
        )
        self.assertTrue(changed)
        self.assertAlmostEqual(state["movement_consumed_to_confirmed_pct"], 12.0)
        self.assertAlmostEqual(state["movement_consumed_to_execution_ready_pct"], 12.0)
        self.assertAlmostEqual(state["mfe_since_origin_pct"], 12.0)
        self.assertFalse(state["resolved_selectable"])

        third = classify_snapshot(
            {
                "credible_opportunity": True,
                "entry_hypothesis": True,
                "v2_state": "CONFIRMED_ACCELERATION",
                "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
            },
            {
                "selectable": True,
                "selection_reason": "SELECTABLE",
                "execution": {"ready": True, "reason": "ENTRY_READY_SHADOW"},
            },
        )
        state, _ = advance_funnel_memory(
            state,
            snapshot=third,
            now=2200.0,
            price_eur=118.0,
        )
        self.assertAlmostEqual(state["movement_consumed_to_selectable_pct"], 18.0)
        self.assertTrue(state["resolved_selectable"])


if __name__ == "__main__":
    unittest.main()
