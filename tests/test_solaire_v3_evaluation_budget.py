import unittest
from unittest.mock import patch

from research.http import PublicClient
import scripts.update_solaire_v3_evaluation as evaluator


def _event(market="TEST-EUR", ts=1_000_000.0):
    return {
        "market": market,
        "decision_ts": ts,
        "price_eur": 1.0,
        "event_type": "ENTRY_READY_SHADOW",
        "evaluations": {},
    }


def _telemetry():
    return {
        "logical_attempts": 0,
        "fetch_wall_seconds": 0.0,
        "complete_results": 0,
        "incomplete_results": 0,
        "incomplete_market_counts": {},
        "incomplete_horizon_counts": {},
        "incomplete_samples": [],
        "error_market_counts": {},
    }


class V3EvaluationBudgetTests(unittest.TestCase):
    def test_repeated_failures_remain_due_and_are_measured_without_market_blacklist(self):
        now = 1_000_000.0 + 5 * 3600
        events = [_event("DEAD-EUR", 1_000_000.0 - i) for i in range(3)]
        errors = []
        telemetry = _telemetry()

        with patch.object(evaluator, "_fetch_evaluation", side_effect=RuntimeError("source unavailable")) as fetch:
            completed, attempted = evaluator._evaluate_event_collection(
                object(), events, now, success_budget=40,
                errors=errors, telemetry=telemetry,
            )

        self.assertEqual(completed, 0)
        self.assertEqual(attempted, 3)
        self.assertEqual(fetch.call_count, 3)
        self.assertEqual(len(errors), 3)
        self.assertEqual(telemetry["error_market_counts"], {"DEAD-EUR": 3})
        self.assertTrue(all(event["evaluations"] == {} for event in events))
        self.assertEqual(len(evaluator._due(events[0], now)), 1)

    def test_success_budget_keeps_existing_success_semantics(self):
        now = 1_000_000.0 + 5 * 3600
        events = [_event(f"M{i}-EUR", 1_000_000.0 - i) for i in range(5)]
        errors = []
        telemetry = _telemetry()

        with patch.object(evaluator, "_fetch_evaluation", return_value={"complete_horizon": True}) as fetch:
            completed, attempted = evaluator._evaluate_event_collection(
                object(), events, now, success_budget=2,
                errors=errors, telemetry=telemetry,
            )

        self.assertEqual(completed, 2)
        self.assertEqual(attempted, 2)
        self.assertEqual(fetch.call_count, 2)
        self.assertEqual(errors, [])
        self.assertEqual(sum(bool(event["evaluations"]) for event in events), 2)

    def test_incomplete_source_result_remains_due_and_is_classified(self):
        now = 1_000_000.0 + 5 * 3600
        event = _event("QUIET-EUR")
        telemetry = _telemetry()

        with patch.object(evaluator, "_fetch_evaluation", return_value={"complete_horizon": False}):
            completed, attempted = evaluator._evaluate_event_collection(
                object(), [event], now, success_budget=40,
                errors=[], telemetry=telemetry,
            )

        self.assertEqual((completed, attempted), (0, 1))
        self.assertEqual(event["evaluations"], {})
        self.assertEqual(telemetry["incomplete_results"], 1)
        self.assertEqual(telemetry["incomplete_market_counts"], {"QUIET-EUR": 1})
        self.assertEqual(telemetry["incomplete_horizon_counts"], {"4": 1})
        self.assertEqual(telemetry["incomplete_samples"][0]["market"], "QUIET-EUR")
        self.assertEqual(len(evaluator._due(event, now)), 1)

    def test_due_backlog_count_does_not_create_evaluations(self):
        now = 1_000_000.0 + 5 * 3600
        events = [_event("A-EUR"), _event("B-EUR")]
        count = evaluator._due_horizon_count([events], now)
        self.assertEqual(count, 2)
        self.assertTrue(all(event["evaluations"] == {} for event in events))

    def test_public_client_diagnostics_are_additive_and_zero_before_requests(self):
        client = PublicClient()
        diagnostics = client.diagnostics()
        self.assertEqual(diagnostics["request_attempts"], 0)
        self.assertEqual(diagnostics["successful_responses"], 0)
        self.assertEqual(diagnostics["rate_limit_wait_seconds"], 0.0)
        self.assertEqual(diagnostics["retry_backoff_seconds"], 0.0)


if __name__ == "__main__":
    unittest.main()
