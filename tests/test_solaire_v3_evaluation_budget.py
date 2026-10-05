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
        "cooldown_skipped": 0,
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
                errors=errors, telemetry=telemetry, retry_state={"entries": {}},
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
                errors=errors, telemetry=telemetry, retry_state={"entries": {}},
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
                errors=[], telemetry=telemetry, retry_state={"entries": {}},
            )

        self.assertEqual((completed, attempted), (0, 1))
        self.assertEqual(event["evaluations"], {})
        self.assertEqual(telemetry["incomplete_results"], 1)
        self.assertEqual(telemetry["incomplete_market_counts"], {"QUIET-EUR": 1})
        self.assertEqual(telemetry["incomplete_horizon_counts"], {"4": 1})
        self.assertEqual(telemetry["incomplete_samples"][0]["market"], "QUIET-EUR")
        self.assertEqual(len(evaluator._due(event, now)), 1)


    def test_incomplete_horizon_is_cooled_down_but_remains_due(self):
        now = 1_000_000.0 + 5 * 3600
        event = _event("QUIET-EUR")
        telemetry = _telemetry()
        retry_state = {"entries": {}}

        with patch.object(evaluator, "_fetch_evaluation", return_value={"complete_horizon": False}) as fetch:
            completed, attempted = evaluator._evaluate_event_collection(
                object(), [event], now, success_budget=40,
                errors=[], telemetry=telemetry, retry_state=retry_state,
            )
            completed2, attempted2 = evaluator._evaluate_event_collection(
                object(), [event], now + 60, success_budget=40,
                errors=[], telemetry=telemetry, retry_state=retry_state,
            )

        self.assertEqual((completed, attempted), (0, 1))
        self.assertEqual((completed2, attempted2), (0, 0))
        self.assertEqual(fetch.call_count, 1)
        self.assertEqual(telemetry["cooldown_skipped"], 1)
        self.assertEqual(event["evaluations"], {})
        self.assertEqual(len(evaluator._due(event, now + 60)), 1)
        self.assertEqual(len(retry_state["entries"]), 1)

    def test_incomplete_horizon_retries_after_cooldown_and_can_complete(self):
        now = 1_000_000.0 + 5 * 3600
        event = _event("QUIET-EUR")
        telemetry = _telemetry()
        retry_state = {"entries": {}}

        with patch.object(
            evaluator,
            "_fetch_evaluation",
            side_effect=[{"complete_horizon": False}, {"complete_horizon": True}],
        ) as fetch:
            evaluator._evaluate_event_collection(
                object(), [event], now, success_budget=40,
                errors=[], telemetry=telemetry, retry_state=retry_state,
            )
            completed, attempted = evaluator._evaluate_event_collection(
                object(), [event], now + evaluator.INCOMPLETE_RETRY_BASE_SECONDS + 1,
                success_budget=40, errors=[], telemetry=telemetry, retry_state=retry_state,
            )

        self.assertEqual((completed, attempted), (1, 1))
        self.assertEqual(fetch.call_count, 2)
        self.assertIn("4", event["evaluations"])
        self.assertEqual(retry_state["entries"], {})

    def test_error_uses_shorter_retry_without_blacklisting_market(self):
        now = 1_000_000.0 + 5 * 3600
        event = _event("FLAKY-EUR")
        telemetry = _telemetry()
        retry_state = {"entries": {}}

        with patch.object(evaluator, "_fetch_evaluation", side_effect=RuntimeError("temporary")):
            evaluator._evaluate_event_collection(
                object(), [event], now, success_budget=40,
                errors=[], telemetry=telemetry, retry_state=retry_state,
            )

        entry = next(iter(retry_state["entries"].values()))
        self.assertEqual(entry["last_status"], "ERROR")
        self.assertEqual(entry["next_retry_ts"] - now, evaluator.ERROR_RETRY_BASE_SECONDS)
        self.assertEqual(event["evaluations"], {})
        self.assertEqual(len(evaluator._due(event, now)), 1)

    def test_public_client_diagnostics_classify_transport_errors_without_changing_client_state(self):
        client = PublicClient()
        client.errors.extend([
            {"path": "/A-EUR/candles", "error": "HTTPError", "http_status": 404},
            {"path": "/A-EUR/candles", "error": "HTTPError", "http_status": 404},
            {"path": "/ICX-EUR/candles", "error": "URLError", "http_status": None},
        ])
        diagnostics = client.diagnostics()
        self.assertEqual(diagnostics["http_status_counts"], {"404": 2, "NONE": 1})
        self.assertEqual(diagnostics["error_type_counts"], {"HTTPError": 2, "URLError": 1})
        self.assertEqual(diagnostics["error_path_counts"]["/A-EUR/candles"], 2)
        self.assertEqual(diagnostics["error_attempt_count"], 3)

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
