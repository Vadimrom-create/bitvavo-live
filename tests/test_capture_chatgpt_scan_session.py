"""Tests for explicit, private SCAN capture. Fixtures never represent real trades."""
import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SCRIPT = SCRIPTS / "capture_chatgpt_scan_session.py"
SPEC = importlib.util.spec_from_file_location("capture_chatgpt_scan_session", SCRIPT)
capture = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(capture)
from scan_accountability_ledger import jsonl, validate_decisions, InputError

NOW = datetime.fromisoformat("2026-10-08T22:30:00+00:00")


def sample(decisions=None, **changes):
    data = {
        "schema": "chatgpt_scan_session_capture_v1",
        "scan_id": "SCAN-20261008-T0001",
        "session_started_at_utc": "2026-10-08T20:00:00Z",
        "session_completed_at_utc": "2026-10-08T20:05:00Z",
        "assistant_final_text": "SCAN vérifié. ATTENTE, réévaluation après la prochaine confirmation machine.",
        "session_status": "SCAN_WAIT",
        "machine_source_status": "FRESH",
        "machine_data_asof_utc": "2026-10-08T20:02:00Z",
        "machine_source_ref": "github-commit/test-fixture-hash",
        "reviewed_signal_ids": ["signal-ogn-001"],
        "decisions": decisions if decisions is not None else [{
            "record_type": "scan_decision",
            "decision_id": "decision-scan-001",
            "market": "OGN-EUR", "source_at_utc": "2026-10-08T20:02:00Z",
            "decision_at_utc": "2026-10-08T20:04:00Z",
            "solaire_action": "ACHETE", "chatgpt_action": "WAIT_RECHECK",
            "reason_codes": ["MACRO_PENDING"],
            "recheck_trigger": "new machine BUY confirmation",
            "recheck_due_utc": "2026-10-08T21:00:00Z",
            "spread_pct": None, "book_asof_utc": None,
            "roundtrip_150eur_pct": None
        }]
    }
    data.update(changes)
    return data


class SessionCaptureTests(unittest.TestCase):
    def test_headers_and_decisions_share_one_private_file(self):
        lines = capture.validate_session(sample(), NOW)
        self.assertEqual([x["record_type"] for x in lines],
                         ["scan_session", "scan_decision"])
        self.assertIn("assistant_final_text", lines[0])
        self.assertNotIn("_at", lines[1])
        self.assertTrue(lines[0]["answer_sha256"])

    def test_idempotent_and_duplicate_proof(self):
        lines = capture.validate_session(sample(), NOW)
        with tempfile.TemporaryDirectory() as root:
            p = Path(root) / "private.jsonl"
            p.write_text('{"record_type":"ledger_header","schema_version":1}\n', encoding="utf-8")
            self.assertEqual(capture.commit_jsonl(p, lines), ("RECORDED", 1))
            before = p.read_text()
            self.assertEqual(capture.commit_jsonl(p, lines), ("ALREADY_RECORDED", 0))
            self.assertEqual(p.read_text(), before)
            # Compatibility with existing value-attribution evaluator.
            ds = validate_decisions(jsonl(p), NOW)
            self.assertEqual(len(ds), 1)
            changed = capture.validate_session(sample(
                assistant_final_text="SCAN modifié : cette réponse est différente et ne doit pas écraser l'ancienne."
            ), NOW)
            with self.assertRaises(InputError):
                capture.commit_jsonl(p, changed)
            other = sample()
            other["decisions"][0]["reason_codes"] = ["CHANGED_CAUSAL_REASON"]
            with self.assertRaises(InputError):
                capture.commit_jsonl(p, capture.validate_session(other, NOW))

    def test_reject_lookahead_in_market_data(self):
        with self.assertRaises(InputError):
            capture.validate_session(sample(
                machine_data_asof_utc="2026-10-08T20:06:00Z"), NOW)

    def test_reject_future_or_outside_session_decision(self):
        with self.assertRaises(InputError):
            capture.validate_session(sample(
                session_completed_at_utc="2026-10-09T22:00:00Z"), NOW)
        obj = sample()
        obj["decisions"][0]["decision_at_utc"] = "2026-10-08T20:06:00Z"
        with self.assertRaises(InputError):
            capture.validate_session(obj, NOW)

    def test_no_decisions_requires_reason(self):
        with self.assertRaises(InputError):
            capture.validate_session(sample(decisions=[], reviewed_signal_ids=[]), NOW)
        lines = capture.validate_session(sample(
            decisions=[], reviewed_signal_ids=[], session_status="SCAN_NO_ACTION",
            no_decision_reason="No viable candidate in inspected snapshot."
        ), NOW)
        self.assertEqual(len(lines), 1)

    def test_no_unproven_buy(self):
        with self.assertRaises(InputError):
            capture.validate_session(sample(session_status="SCAN_WITH_BUY"), NOW)
        buy = sample()
        buy["session_status"] = "SCAN_INSUFFICIENT_DATA"
        buy["decisions"][0].update(
            chatgpt_action="BUY", book_asof_utc="2026-10-08T20:03:00Z",
            entry_limit_eur=0.021, stop_eur=0.019,
            spread_pct=0.2, roundtrip_150eur_pct=0.45,
        )
        with self.assertRaises(InputError):
            capture.validate_session(buy, NOW)
        buy["session_status"] = "SCAN_WITH_BUY"
        self.assertEqual(capture.validate_session(buy, NOW)[1]["chatgpt_action"], "BUY")
        buy["machine_source_status"] = "UNAVAILABLE"
        with self.assertRaises(InputError):
            capture.validate_session(buy, NOW)
        buy["machine_source_status"] = "FRESH"
        buy["decisions"][0]["book_asof_utc"] = "2026-10-08T19:50:00Z"
        with self.assertRaises(InputError):
            capture.validate_session(buy, NOW)

    def test_source_fresh_needs_evidence_and_timestamp(self):
        with self.assertRaises(InputError):
            capture.validate_session(sample(machine_source_ref=None), NOW)
        with self.assertRaises(InputError):
            capture.validate_session(sample(machine_data_asof_utc=None), NOW)
        x = capture.validate_session(sample(machine_source_status="UNAVAILABLE",
                                            machine_source_ref=None,
                                            machine_data_asof_utc=None), NOW)
        self.assertEqual(x[0]["machine_source_status"], "UNAVAILABLE")

    def test_private_ledger_must_preexist(self):
        with tempfile.TemporaryDirectory() as root:
            p = Path(root) / "absent.jsonl"
            with self.assertRaises(InputError):
                capture.commit_jsonl(p, capture.validate_session(sample(), NOW))
            p.write_text("{}\n")
            with self.assertRaises(InputError):
                capture.commit_jsonl(p, capture.validate_session(sample(), NOW))

    def test_missing_ledger_sources_not_proof_of_omission(self):
        lines = capture.validate_session(sample(
            machine_source_status="UNAVAILABLE",
            machine_source_ref=None,
            machine_data_asof_utc=None,
            reviewed_signal_ids=[]), NOW)
        self.assertEqual(lines[0]["machine_source_status"], "UNAVAILABLE")
        self.assertEqual(lines[0]["reviewed_signal_ids"], [])


if __name__ == "__main__":
    unittest.main()
