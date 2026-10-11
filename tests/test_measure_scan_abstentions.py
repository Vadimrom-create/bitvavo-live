"""Synthetic-only tests for SCAN buy / wait / exclusion economic accountability."""
import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("measure_scan_abstentions", SCRIPTS / "measure_scan_abstentions.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

ASOF = datetime.fromisoformat("2026-10-12T22:00:00+00:00")


def decision(identifier="d1", action="WAIT_RECHECK", **changes):
    row = {
        "record_type": "scan_decision",
        "decision_id": identifier,
        "market": "MAGIC-EUR",
        "decision_at_utc": "2026-10-10T10:00:00Z",
        "source_at_utc": "2026-10-10T09:59:00Z",
        "solaire_action": "ACHETE",
        "chatgpt_action": action,
        "reason_codes": ["AWAIT_MULTITIMEFRAME"],
    }
    if action == "WAIT_RECHECK":
        row.update(recheck_trigger="fresh confirmed candle", recheck_due_utc="2026-10-10T11:00:00Z")
    row.update(changes)
    return row


def pair(identifier="d1", horizon=24, **changes):
    data = {
        "record_type": "paired_outcome",
        "decision_id": identifier,
        "horizon_hours": horizon,
        "both_executions_validated": True,
        "matched_budget_policy_costs": True,
        "horizon_matured": True,
        "independent_episode": True,
        "solaire_net_eur": 3.0,
        "chatgpt_net_eur": 0.0,
        "evidence_observed_at_utc": "2026-10-11T11:00:00Z",
    }
    data.update(changes)
    return data


class ScanAbstentionTests(unittest.TestCase):
    def test_all_three_categories_plus_explicit_insufficient_data(self):
        d = [
            decision("a", "BUY", decision_category="ACHAT_TEST"),
            decision("b", "WAIT_RECHECK", decision_category="ATTENDRE_CONFIRMATION"),
            decision("c", "REJECT_STRUCTURAL", decision_category="ECARTER"),
            decision("d", "INSUFFICIENT_DATA", decision_category="NON_CLASSABLE"),
        ]
        r = mod.report(d, [], ASOF)
        self.assertEqual(r["decision_count"], 4)
        self.assertEqual(r["categories"], {"ACHAT_TEST": 1, "ATTENDRE_CONFIRMATION": 1, "ECARTER": 1, "NON_CLASSABLE": 1})
        self.assertEqual(r["category_provenance"]["EXPLICIT"], 4)
        self.assertEqual(r["comparison_by_category_and_horizon"]["ATTENDRE_CONFIRMATION"]["24"]["verdict"], "NON_MESURABLE")

    def test_legacy_is_inferred_not_claimed_explicit(self):
        r = mod.report([decision()], [], ASOF)
        self.assertEqual(r["decisions"][0]["category"], "ATTENDRE_CONFIRMATION")
        self.assertEqual(r["decisions"][0]["category_provenance"], "LEGACY_INFERRED")

    def test_category_mismatch_is_error(self):
        with self.assertRaises(mod.InputError):
            mod.report([decision(decision_category="ACHAT_TEST")], [], ASOF)

    def test_maturation_does_not_imply_profits(self):
        r = mod.report([decision()], [], ASOF)
        h = r["decisions"][0]["horizons"]
        self.assertEqual(h["24"]["status"], "MATURE_NO_VERIFIED_PAIR")
        self.assertEqual(h["48"]["status"], "MATURE_NO_VERIFIED_PAIR")
        self.assertEqual(h["72"]["status"], "NOT_MATURE")
        self.assertIsNone(h["24"]["chatgpt_minus_solaire_eur"])
        self.assertEqual(r["comparison_by_category_and_horizon"]["ATTENDRE_CONFIRMATION"]["24"]["verified_paired_decisions"], 0)

    def test_valid_pair_counted_only_after_maturity(self):
        r = mod.report([decision()], [pair()], ASOF)
        c = r["comparison_by_category_and_horizon"]["ATTENDRE_CONFIRMATION"]["24"]
        self.assertEqual(c["matured_machine_buy_decisions"], 1)
        self.assertEqual(c["verified_paired_decisions"], 1)
        self.assertEqual(c["chatgpt_minus_solaire_eur"], -3.0)
        self.assertEqual(c["verdict"], "DESCRIPTIVE_ONLY")
        self.assertIsNone(r["decisions"][0]["horizons"]["48"]["solaire_net_eur"])

    def test_claimed_future_proof_is_ignored(self):
        data = pair(horizon=72, evidence_observed_at_utc="2026-10-13T11:00:00Z")
        r = mod.report([decision()], [data], ASOF)
        self.assertEqual(r["decisions"][0]["horizons"]["72"]["status"], "NOT_MATURE")

    def test_observation_before_maturity_or_after_cutoff_disqualified(self):
        before = pair(evidence_observed_at_utc="2026-10-10T23:00:00Z")
        after = pair(evidence_observed_at_utc="2026-10-13T01:00:00Z")
        for p in (before, after):
            r = mod.report([decision()], [p], ASOF)
            self.assertEqual(r["decisions"][0]["horizons"]["24"]["status"], "MATURE_NO_VERIFIED_PAIR")

    def test_failing_execution_proof_not_misreported(self):
        r = mod.report([decision()], [pair(both_executions_validated=False)], ASOF)
        self.assertEqual(r["decisions"][0]["horizons"]["24"]["status"], "MATURE_NO_VERIFIED_PAIR")

    def test_non_machine_buy_not_in_economic_comparison_denominator(self):
        r = mod.report([decision(solaire_action="NONE")], [], ASOF)
        self.assertEqual(r["comparison_by_category_and_horizon"]["ATTENDRE_CONFIRMATION"]["24"]["matured_machine_buy_decisions"], 0)
        self.assertEqual(r["decisions"][0]["comparability_scope"], "OUTSIDE_MACHINE_BUY")

    def test_missing_inputs_explicit(self):
        r = mod.report([], [], ASOF)
        self.assertEqual(r["decision_count"], 0)
        self.assertEqual(r["machine_buy_decision_count"], 0)
        self.assertEqual(r["comparison_by_category_and_horizon"]["ACHAT_TEST"]["24"]["verdict"], "NON_MESURABLE")


if __name__ == "__main__":
    unittest.main()
