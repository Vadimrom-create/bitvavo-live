"""Adversarial synthetic tests: no real user decisions enter the public repo."""
from __future__ import annotations

import unittest
from datetime import datetime, timezone

from scripts.reconcile_private_wait_recheck import InputError, reconcile

UTC = timezone.utc
ASOF = datetime(2026, 10, 11, 14, 0, tzinfo=UTC)


def decision(market, index=1, action="WAIT_RECHECK", at="2026-10-08T22:14:25Z"):
    return {
        "record_type": "scan_decision",
        "decision_id": f"synthetic-{market}-{index}",
        "market": market,
        "decision_at_utc": at,
        "source_at_utc": "2026-10-08T22:11:00Z",
        "chatgpt_action": action,
        "solaire_action": "WATCH",
        "reason_codes": ["TEST_ONLY"],
        "recheck_trigger": "new confirmation or clock deadline",
        "recheck_due_utc": "2026-10-09T06:00:00Z",
    }


def event(market, when, kind, signal="synthetic-signal", reason=None):
    iso = datetime.fromisoformat(when.replace("Z", "+00:00"))
    return {
        "market": market,
        "decision_ts": iso.timestamp(),
        "decision_type": kind,
        "signal_id": signal,
        "decision_id": "machine-synthetic",
        "episode_id": "episode-synthetic",
        "reason": reason,
        "signal_price_eur": 0.5,
    }


class ReconcileWaitTests(unittest.TestCase):
    def test_overdue_and_buy_followups_are_distinct(self):
        decisions = [
            decision("AMP-EUR"), decision("ZRC-EUR"), decision("GRASS-EUR"),
            decision("W-EUR"), decision("AVNT-EUR")
        ]
        events = [
            event("AMP-EUR", "2026-10-09T12:00:00Z", "REJECTED", reason="SPREAD_TOO_WIDE"),
            event("ZRC-EUR", "2026-10-10T09:00:00Z", "REJECTED", reason="STOP_TOO_WIDE"),
            event("GRASS-EUR", "2026-10-11T09:00:00Z", "BUY_SENT", signal="grass-new"),
            event("W-EUR", "2026-10-08T20:00:00Z", "BUY_SENT", signal="before-wait"),
            event("W-EUR", "2026-10-09T07:00:00Z", "BUY_SENT", signal="w-new"),
            event("W-EUR", "2026-10-09T07:00:00Z", "BUY_SENT", signal="w-new"),
            event("W-EUR", "2026-10-10T15:00:00Z", "BUY_SENT", signal="future"),
        ]
        result = reconcile(decisions, {"entries": events}, ASOF)
        by_market = {p["market"]: p for p in result["pending"]}
        self.assertEqual(result["pending_wait_count"], 5)
        self.assertEqual(result["pending_overdue_count"], 5)
        self.assertEqual(result["pending_new_machine_buy_count"], 2)
        self.assertEqual(by_market["GRASS-EUR"]["state"], "REVIEW_NEW_MACHINE_BUY")
        self.assertEqual(by_market["W-EUR"]["new_buy_sent_count"], 1)  # dedup and future
        self.assertEqual(by_market["AMP-EUR"]["new_rejections_count"], 1)
        self.assertEqual(by_market["AVNT-EUR"]["state"], "REVIEW_OVERDUE")
        self.assertFalse(by_market["AVNT-EUR"]["absence_of_new_buy_proven"])
        self.assertTrue(all(not p["auto_buy_authorized"] for p in result["pending"]))
        self.assertTrue(result["research_only"])
        self.assertFalse(result["orders_submitted"])

    def test_new_decision_supersedes_wait_without_rewriting_history(self):
        decisions = [
            decision("W-EUR"),
            decision("W-EUR", index=2, action="REJECT_STRUCTURAL",
                     at="2026-10-09T12:00:00Z"),
        ]
        result = reconcile(decisions, {"entries": [
            event("W-EUR", "2026-10-10T15:00:00Z", "BUY_SENT", signal="new")
        ]}, ASOF)
        self.assertEqual(result["pending_wait_count"], 0)
        self.assertEqual(result["private_decisions_count"], 2)

    def test_no_false_positive_on_old_buy(self):
        result = reconcile([decision("W-EUR")], {"entries": [
            event("W-EUR", "2026-10-08T21:00:00Z", "BUY_SENT", signal="old")
        ]}, ASOF)
        self.assertEqual(result["pending_new_machine_buy_count"], 0)
        self.assertEqual(result["pending_overdue_count"], 1)

    def test_future_machine_event_is_not_used(self):
        result = reconcile([decision("W-EUR")], {"entries": [
            event("W-EUR", "2026-10-12T00:00:00Z", "BUY_SENT", signal="future")
        ]}, ASOF)
        self.assertEqual(result["pending_new_machine_buy_count"], 0)

    def test_missing_private_trigger_refused(self):
        d = decision("W-EUR")
        del d["recheck_trigger"]
        with self.assertRaises(InputError):
            reconcile([d], {"entries": []}, ASOF)

    def test_duplicate_private_decision_refused(self):
        d = decision("W-EUR")
        with self.assertRaises(InputError):
            reconcile([d, d], {"entries": []}, ASOF)

    def test_missing_machine_timestamp_fails_closed(self):
        e = event("W-EUR", "2026-10-09T07:00:00Z", "BUY_SENT")
        e["decision_ts"] = None
        with self.assertRaises(InputError):
            reconcile([decision("W-EUR")], {"entries": [e]}, ASOF)

    def test_unknown_machine_schema_fails_closed(self):
        with self.assertRaises(InputError):
            reconcile([decision("W-EUR")], {"events": []}, ASOF)


if __name__ == "__main__":
    unittest.main()
