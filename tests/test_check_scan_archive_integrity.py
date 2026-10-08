"""Tests for the first real SCAN's accounting failures, with synthetic fixtures."""
import importlib.util
import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from datetime import datetime, timezone
D = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(D))
SPEC = importlib.util.spec_from_file_location("check_scan_archive_integrity", D / "check_scan_archive_integrity.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
ASOF = datetime.fromisoformat("2026-10-08T22:20:00+00:00")


def records():
    text = "Analyse des cours et du contexte ; aucune entrée immédiate, attente de nouvelles données."
    session = {
        "record_type": "scan_session", "scan_id": "SCAN-20261009-001213-CEST",
        "session_started_at_utc": "2026-10-08T22:11:30Z",
        "session_completed_at_utc": "2026-10-08T22:14:25Z",
        "machine_source_status": "PARTIAL",
        "machine_source_ref": "github:commit-sha",
        "decision_count": 1, "assistant_final_text": text,
        "answer_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "archived_text_scope": "explicit_decision_verdict_and_rationale_text_not_full_UI_transcript",
    }
    decision = {
        "record_type": "scan_decision", "scan_id": session["scan_id"],
        "decision_id": "SCAN-20261009-001213-CEST-01",
        "market": "AMP-EUR", "source_at_utc": "2026-10-08T22:04:55Z",
        "decision_at_utc": "2026-10-08T22:14:25Z",
        "solaire_action": "WATCH", "chatgpt_action": "WAIT_RECHECK",
        "reason_codes": ["SPREAD_TOO_WIDE"],
        "recheck_trigger": "spread lower with order book",
        "recheck_due_utc": "2026-10-09T06:00:00Z",
    }
    return [{"record_type": "ledger_header", "decisions_recorded": 0}, session, decision]


class ArchiveIntegrityTests(unittest.TestCase):
    def setup_files(self, folder, records_=None, manifest=None):
        p = Path(folder) / "ledger.jsonl"
        p.write_text("".join(json.dumps(x) + "\n" for x in (records_ or records())), encoding="utf-8")
        m = Path(folder) / "manifest.json"
        m.write_text(json.dumps(manifest if manifest is not None else {"status":"EMPTY_READY_FOR_NEW_SCANS"}), encoding="utf-8")
        return p, m

    def test_real_first_scan_style_flags(self):
        with tempfile.TemporaryDirectory() as d:
            p, m = self.setup_files(d)
            out = mod.check(p, ASOF, m)
            self.assertEqual(out["sessions"], 1)
            self.assertEqual(out["decisions"], 1)
            self.assertEqual(out["decisions_by_action"]["WAIT_RECHECK"], 1)
            self.assertEqual(out["verified_paired_execution_outcomes"], 0)
            self.assertEqual(out["financial_verdict"], "NON_MESURABLE")
            self.assertIn("MANIFEST_EMPTY_DESPITE_SESSIONS", out["flags"])
            self.assertIn("ONLY_SUMMARY_NOT_FULL_CHAT_PROOF", out["flags"])
            self.assertIn("IMMUTABLE_HEADER_INITIAL_COUNT_NOT_LIVE", out["flags"])
            self.assertEqual(out["latest_waits_overdue"], 0)

    def test_horizon_elapsed_does_not_fabricate_outcome(self):
        with tempfile.TemporaryDirectory() as d:
            p, m = self.setup_files(d)
            later = datetime.fromisoformat("2026-10-09T03:00:00+00:00")
            out = mod.check(p, later, m)
            self.assertEqual(out["time_elapsed_horizon_session_count_NOT_TRADE_OUTCOMES"]["4"], 1)
            self.assertIsNone(out["chatgpt_financial_value_eur"])

    def test_recheck_due_8am_paris_and_overdue(self):
        with tempfile.TemporaryDirectory() as d:
            p, m = self.setup_files(d)
            out = mod.check(p, datetime.fromisoformat("2026-10-09T06:01:00+00:00"), m)
            self.assertEqual(out["latest_waits_overdue"], 1)

    def test_summary_hash_tampering(self):
        with tempfile.TemporaryDirectory() as d:
            rr = records()
            rr[1]["assistant_final_text"] = "this text was altered"
            p, m = self.setup_files(d, rr, {"status":"HAS_SESSIONS","observed_session_count":1})
            out = mod.check(p, ASOF, m)
            self.assertEqual(out["session_text_hash_mismatch_count"], 1)
            self.assertIn("ARCHIVED_TEXT_HASH_MISMATCH", out["flags"])
            self.assertNotIn("MANIFEST_EMPTY_DESPITE_SESSIONS", out["flags"])

    def test_missing_or_duplicate_decisions(self):
        with tempfile.TemporaryDirectory() as d:
            rr = records()
            rr[1]["decision_count"] = 2
            p, m = self.setup_files(d, rr)
            out = mod.check(p, ASOF, m)
            self.assertIn("SESSION_DECISION_COUNT_MISMATCH", out["flags"])
            rr.append(dict(rr[2]))
            p, m = self.setup_files(d, rr)
            with self.assertRaises(mod.InputError):
                mod.check(p, ASOF, m)

    def test_no_full_ui_transcript_claim_from_summary(self):
        with tempfile.TemporaryDirectory() as d:
            p, m = self.setup_files(d, manifest={"status": "ACTIVE","observed_session_count":1})
            out = mod.check(p, ASOF, m)
            self.assertEqual(out["session_text_scope_summary_not_full"], 1)
            self.assertNotIn("MANIFEST_EMPTY_DESPITE_SESSIONS", out["flags"])

    def test_capture_public_paths_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p, m = self.setup_files(d)
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                success = mod.main(["--ledger", str(p), "--manifest", str(m), "--asof", "2026-10-08T22:20:00Z"])
            self.assertEqual(success, 0)
            with contextlib.redirect_stderr(io.StringIO()):
                failed = mod.main(["--ledger", str(D / "scan_accountability_ledger.py"), "--asof", "2026-10-08T22:20:00Z"])
            self.assertEqual(failed, 2)


if __name__ == "__main__":
    unittest.main()
