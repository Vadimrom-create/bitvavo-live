import unittest

from research.solaire_funnel_audit import (
    FIXED_HORIZON_SECONDS,
    advance_funnel_memory,
    classify_path_snapshots,
    observe_price_only,
    should_track,
)


def by_path(rows, path):
    return next(x for x in rows if x["path"] == path)


class SolaireFunnelAuditTests(unittest.TestCase):
    def test_building_signal_creates_only_v2_real_path(self):
        v3 = {
            "v2_state": "BUILDING_ACCELERATION",
            "early_quant": {"ready": False, "score_0_10": 2.0, "evidence_count": 1},
        }
        self.assertTrue(should_track(v3, {}))
        rows = classify_path_snapshots(v3, {})
        v2 = by_path(rows, "V2_REAL")
        self.assertEqual(v2["stage"], "V2_BUILDING")
        self.assertEqual(v2["loss_family"], "PRE_CONFIRMATION")


    def test_early_quant_without_v2_state_does_not_create_fake_v2_real_path(self):
        v3 = {
            "early_quant": {"ready": True, "score_0_10": 8.0, "evidence_count": 5},
            "near_miss_opportunity": True,
            "credible_opportunity": True,
        }
        rows = classify_path_snapshots(v3, {})
        self.assertFalse(any(x["path"] == "V2_REAL" for x in rows))
        self.assertTrue(any(x["path"] == "NEAR_MISS_DIAGNOSTIC" for x in rows))

    def test_thesis_reentry_is_not_misclassified_as_early_control(self):
        v3 = {
            "thesis_reentry_hypothesis": True,
            "thesis_execution": {"ready": False, "reason": "WAITING_SPREAD"},
        }
        v31 = {
            "entry_path": "THESIS_REENTRY_WAIT",
            "selection_reason": "WAITING_SPREAD",
            "thesis_reentry_hypothesis": True,
            "thesis_execution": {"ready": False, "reason": "WAITING_SPREAD"},
        }
        thesis = by_path(classify_path_snapshots(v3, v31), "THESIS_REENTRY")
        self.assertTrue(thesis["entry_hypothesis"])
        self.assertEqual(thesis["stage"], "THESIS_REENTRY_WAITING_EXECUTION")
        self.assertEqual(thesis["blocking_reason"], "WAITING_SPREAD")

    def test_near_miss_diagnostic_ready_is_not_economic_rejection(self):
        v3 = {
            "near_miss_opportunity": True,
            "credible_opportunity": True,
            "entry_hypothesis": False,
        }
        v31 = {
            "selectable": False,
            "selection_reason": "NOT_CHECKED",
            "entry_path": "RAW",
        }
        diagnostic = by_path(
            classify_path_snapshots(
                v3,
                v31,
                near_miss_execution={
                    "ready": True,
                    "reason": "ENTRY_READY_SHADOW",
                    "available_ts": 1005.0,
                    "plan": {"entry_eur": 101.0, "stop_eur": 95.0, "tp1_eur": 112.0},
                },
            ),
            "NEAR_MISS_DIAGNOSTIC",
        )
        self.assertEqual(diagnostic["stage"], "NEAR_MISS_DIAGNOSTIC_READY")
        self.assertEqual(diagnostic["loss_family"], "DIAGNOSTIC_ONLY")
        self.assertFalse(diagnostic["selectable"])
        self.assertFalse(diagnostic["selection_checked"])

    def test_raw_ready_not_selected_is_unchecked_not_rejected(self):
        v3 = {
            "credible_opportunity": True,
            "entry_hypothesis": True,
            "execution": {
                "ready": True,
                "reason": "ENTRY_READY_SHADOW",
                "available_ts": 1005.0,
                "plan": {"entry_eur": 101.0, "stop_eur": 95.0, "tp1_eur": 112.0},
            },
        }
        v31 = {
            "entry_path": "THESIS_REENTRY_WAIT",
            "selection_reason": "NOT_CHECKED",
            "raw_execution": v3["execution"],
        }
        raw = by_path(classify_path_snapshots(v3, v31), "RAW")
        self.assertEqual(raw["stage"], "RAW_EXECUTION_READY_UNCHECKED")
        self.assertEqual(raw["loss_family"], "EXECUTION_READY_NOT_ECONOMICALLY_CHECKED")

    def test_exact_execution_price_is_used_for_execution_and_selectable_milestones(self):
        execution = {
            "ready": True,
            "reason": "ENTRY_READY_SHADOW",
            "available_ts": 1005.0,
            "plan": {"entry_eur": 102.0, "stop_eur": 96.0, "tp1_eur": 115.0},
        }
        v3 = {
            "credible_opportunity": True,
            "entry_hypothesis": True,
            "execution": execution,
        }
        v31 = {
            "entry_path": "RAW",
            "selectable": True,
            "selection_reason": "SELECTABLE",
            "economic_score": 7.2,
            "raw_execution": execution,
            "decision_id": "d1",
        }
        raw = by_path(classify_path_snapshots(v3, v31), "RAW")
        state, changed = advance_funnel_memory(
            None,
            snapshot=raw,
            now=1000.0,
            price_eur=100.0,
        )
        self.assertTrue(changed)
        self.assertEqual(state["first_execution_ready_price_eur"], 102.0)
        self.assertEqual(state["first_selectable_price_eur"], 102.0)
        self.assertEqual(state["first_selectable_entry_eur"], 102.0)
        self.assertEqual(state["first_selectable_decision_id"], "d1")
        self.assertIsNotNone(state["first_selectable_plan_id"])

    def test_signal_disappearance_does_not_stop_fixed_horizon_price_tracking(self):
        raw = {
            "path": "RAW",
            "stage": "RAW_CREDIBLE_PRE_ENTRY",
            "loss_family": "PRE_ENTRY",
            "credible": True,
            "entry_hypothesis": False,
            "v2_confirmed": False,
            "execution_ready": False,
            "selectable": False,
            "blocking_reason": "NO_ENTRY_HYPOTHESIS_YET",
            "economic_score": 5.0,
            "v3_opportunity_score": 6.0,
            "v2_score": 4.0,
            "entry_path": "RAW",
            "plan_id": None,
            "execution_entry_eur": None,
            "decision_id": None,
        }
        state, _ = advance_funnel_memory(
            None,
            snapshot=raw,
            now=1000.0,
            price_eur=100.0,
        )
        self.assertEqual(state["horizon_end_ts"], 1000.0 + FIXED_HORIZON_SECONDS)
        state = observe_price_only(state, now=1600.0, price_eur=108.0)
        state = observe_price_only(state, now=2200.0, price_eur=94.0)
        self.assertAlmostEqual(state["mfe_since_origin_pct"], 8.0)
        self.assertAlmostEqual(state["mae_since_origin_pct"], -6.0)
        self.assertAlmostEqual(state["current_return_from_origin_pct"], -6.0)


if __name__ == "__main__":
    unittest.main()
