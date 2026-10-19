#!/usr/bin/env python3
"""Offline synthetic regression tests for read-only economic evidence gate."""
from __future__ import annotations

import copy
import unittest

from scripts.economic_evidence_gate import EvidenceError, assess


def fixture():
    horizons = {}
    comparisons = {}
    for hour, n in (("4", 12), ("12", 9), ("24", 6)):
        horizons[hour] = {
            "current_tp1_stop": {
                "n": n, "positive_net": n // 3, "negative_net": n - n // 3,
                "median_net_return_pct": -1.2, "sum_net_pnl_eur_est": -15.0,
            },
            "full_1_4r": {
                "n": n, "positive_net": n // 3 + 1,
                "negative_net": n - n // 3 - 1,
                "median_net_return_pct": -0.7, "sum_net_pnl_eur_est": -10.0,
            },
        }
        comparisons[hour] = {
            "full_1_4r": {"delta_sum_net_pnl_eur_est": 5.0}
        }
    return (
        {
            "schema": "solaire_exit_policy_shadow_v3",
            "status": "OK",
            "checked_at_utc": "2026-10-11T00:00:00Z",
            "study_id": "synthetic-fixture",
            "summary": horizons,
            "comparisons_vs_current": comparisons,
        },
        {
            "schema": "swing_selector_clean_oos_v1",
            "generated_at_utc": "2026-10-11T00:00:00Z",
            "version": "synthetic",
            "metrics": {k: {"168": {"n": 0}} for k in
                        ("baseline", "swing_top10", "swing_human_review")},
        },
    )


class EconomicEvidenceGateTests(unittest.TestCase):
    def test_valid_shadow_does_not_become_executable_pnl(self):
        a, b = fixture()
        r = assess(a, b)
        self.assertEqual(r["status"], "NOT_IDENTIFIABLE_AS_EXECUTABLE_PORTFOLIO_PNL")
        self.assertIsNone(r["net_executable_portfolio_pnl_eur"])
        self.assertIsNone(r["actual_chatgpt_incremental_pnl_eur"])
        self.assertFalse(r["seven_day_observations_exist"])
        self.assertFalse(r["paired_exit_shadow_diagnostics"][0]["event_id_pairing_verified"])
        self.assertEqual(len(r["paired_exit_shadow_diagnostics"]), 3)
        self.assertEqual(r["paired_exit_shadow_diagnostics"][0]["candidate_minus_reference_eur_est"], 5.0)

    def test_unmatched_n_fails_closed(self):
        a, b = fixture()
        a["summary"]["4"]["full_1_4r"]["n"] = 11
        with self.assertRaisesRegex(EvidenceError, "equally mature"):
            assess(a, b)

    def test_outcome_counts_must_balance(self):
        a, b = fixture()
        a["summary"]["12"]["full_1_4r"]["positive_net"] = 8
        with self.assertRaisesRegex(EvidenceError, "count mismatch"):
            assess(a, b)

    def test_shadow_delta_must_reconcile(self):
        a, b = fixture()
        a["comparisons_vs_current"]["24"]["full_1_4r"]["delta_sum_net_pnl_eur_est"] = 7.0
        with self.assertRaisesRegex(EvidenceError, "inconsistent"):
            assess(a, b)

    def test_non_finite_pnl_rejected(self):
        a, b = fixture()
        a["summary"]["4"]["full_1_4r"]["sum_net_pnl_eur_est"] = float("nan")
        with self.assertRaisesRegex(EvidenceError, "finite number"):
            assess(a, b)

    def test_no_zero_substitution_for_missing_data(self):
        a, b = fixture()
        del a["summary"]["4"]["full_1_4r"]["sum_net_pnl_eur_est"]
        with self.assertRaises(EvidenceError):
            assess(a, b)

    def test_oos_maturity_positive_not_go_decision(self):
        a, b = fixture()
        for series in b["metrics"].values():
            series["168"]["n"] = 100
        r = assess(a, b)
        self.assertTrue(r["seven_day_observations_exist"])
        self.assertEqual(r["status"], "NOT_IDENTIFIABLE_AS_EXECUTABLE_PORTFOLIO_PNL")

    def test_incompatible_oos_schema_rejected(self):
        a, b = fixture()
        b["schema"] = "other"
        with self.assertRaises(EvidenceError):
            assess(a, b)

    def test_bool_is_not_sample_count(self):
        a, b = fixture()
        b["metrics"]["baseline"]["168"]["n"] = True
        with self.assertRaises(EvidenceError):
            assess(a, b)


if __name__ == "__main__":
    unittest.main()
