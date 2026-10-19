"""Synthetic-only tests for private-to-public SCAN signal identity and chronology."""
import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "link_private_scan_to_machine", ROOT / "scripts" / "link_private_scan_to_machine.py"
)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)

ASOF = datetime.fromisoformat("2026-10-11T20:30:00+00:00")
EVENT_TIME = datetime.fromisoformat("2026-10-11T20:00:00+00:00").timestamp()


def event(signal="signal-1", market="MAGIC-EUR", kind="BUY_SENT", stamp=EVENT_TIME):
    return {
        "signal_id": signal, "decision_id": "machine-decision-" + signal,
        "episode_id": "episode-" + signal, "market": market,
        "decision_type": kind, "decision_ts": stamp,
    }


def machine(*entries):
    return {
        "schema": "solaire_prospective_journal_v1",
        "updated_at_ts": ASOF.timestamp() - 20,
        "entries": list(entries),
    }


def decision(signal="signal-1", **kw):
    row = {
        "record_type": "scan_decision",
        "decision_id": "private-1",
        "market": "MAGIC-EUR",
        "decision_at_utc": "2026-10-11T20:04:00Z",
        "source_at_utc": "2026-10-11T20:03:00Z",
        "solaire_action": "ACHETE",
        "chatgpt_action": "WAIT_RECHECK",
        "reason_codes": ["AWAIT_CONFIRMATION"],
        "recheck_trigger": "fresh confirmation",
        "recheck_due_utc": "2026-10-11T20:10:00Z",
    }
    if signal is not None:
        row["machine_signal_id"] = signal
    row.update(kw)
    return row


class LinkageTests(unittest.TestCase):
    def test_exact_link_uses_machine_signal_id_only(self):
        d = m.link([decision()], machine(event()), ASOF)
        self.assertEqual(d["causally_matched"], 1)
        joined = d["links"][0]
        self.assertEqual(joined["link_status"], "EXACT_CAUSAL_MACHINE_BUY")
        self.assertEqual(joined["machine_decision_id"], "machine-decision-signal-1")
        self.assertEqual(joined["machine_episode_id"], "episode-signal-1")
        self.assertTrue(joined["eligible_for_event_level_audit"])
        self.assertFalse(joined["eligible_for_economic_pairing"])
        self.assertFalse(joined["fills_proven"])
        self.assertIsNone(joined["net_pnl_eur"])

    def test_missing_explicit_signal_id_never_guess_by_market_or_time(self):
        d = m.link([decision(signal=None)], machine(event()), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "MISSING_EXPLICIT_SIGNAL_ID")
        self.assertEqual(d["causally_matched"], 0)

    def test_missing_from_retention_is_unknown_not_refusal(self):
        d = m.link([decision()], machine(event("signal-other")), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "SIGNAL_NOT_IN_RETAINED_JOURNAL")
        self.assertFalse(d["links"][0]["eligible_for_economic_pairing"])

    def test_conflicting_market_cannot_join(self):
        d = m.link([decision()], machine(event(market="STRK-EUR")), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "MARKET_IDENTITY_MISMATCH")

    def test_machine_rejection_is_not_a_machine_buy(self):
        d = m.link([decision()], machine(event(kind="REJECTED")), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "NOT_A_MATCHED_MACHINE_BUY")

    def test_duplicate_signal_collision_not_silently_joined(self):
        d = m.link([decision()], machine(event(), event()), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "AMBIGUOUS_SIGNAL_ID")

    def test_future_event_after_source_excluded(self):
        d = m.link([decision()], machine(event(stamp=EVENT_TIME + 190)), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "MACHINE_EVENT_AFTER_RECORDED_SOURCE")

    def test_stale_signal_not_comparable_even_with_exact_id(self):
        d = m.link([decision(
            decision_at_utc="2026-10-11T20:15:00Z",
            source_at_utc="2026-10-11T20:14:00Z",
        )], machine(event()), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "STALE_MACHINE_BUY")
        self.assertFalse(d["links"][0]["eligible_for_economic_pairing"])

    def test_non_achete_chatgpt_field_not_misclassified(self):
        d = m.link([decision(solaire_action="WATCH")], machine(event()), ASOF)
        self.assertEqual(d["links"][0]["link_status"], "NOT_A_MATCHED_MACHINE_BUY")

    def test_future_timestamp_in_machine_journal_is_rejected(self):
        with self.assertRaises(m.InputError):
            m.machine_index(machine(event(stamp=ASOF.timestamp() + 60)), ASOF)

    def test_public_audit_uses_no_private_records(self):
        output = m.public_audit(machine(event(), event("signal-2"), event("signal-2")), ASOF)
        self.assertEqual(output["machine_retained_counts"]["BUY_SENT"], 3)
        self.assertEqual(output["duplicate_signal_ids"], 1)
        self.assertFalse(output["private_decisions_loaded"])
        self.assertEqual(output["chatgpt_attribution"], "UNKNOWN_NO_PRIVATE_INPUT")

    def test_private_input_location_must_be_outside_public_repository(self):
        with self.assertRaises(m.InputError):
            m.outside_public_repo(str(ROOT / "tests" / "synthetic-test.jsonl"))
        with tempfile.TemporaryDirectory() as path:
            m.outside_public_repo(str(Path(path) / "scan-private.jsonl"))


if __name__ == "__main__":
    unittest.main()
