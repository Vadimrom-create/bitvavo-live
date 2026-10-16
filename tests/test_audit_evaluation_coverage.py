"""Read-only evaluation coverage audit: synthetic source journals only."""
import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "scripts" / "audit_evaluation_coverage.py"
SPEC = importlib.util.spec_from_file_location("audit_evaluation_coverage", P)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
ASOF = datetime(2026, 10, 11, 20, 0, tzinfo=timezone.utc).timestamp()


def entry(did, ts, decision_type="BUY_SENT", evaluations=None):
    return {
        "decision_id": did, "market": "TEST-EUR", "decision_type": decision_type,
        "decision_ts": ts, "evaluations": evaluations or {},
    }


def journal(*rows):
    return {"schema": "solaire_prospective_journal_v1", "entries": list(rows)}


class CoverageTests(unittest.TestCase):
    def test_distinguishes_missing_evidence_from_trade_failure(self):
        old = entry("old", ASOF - 90 * 3600, evaluations={"24": {"status": "COMPLETE", "result": "OPEN"}})
        recent = entry("recent", ASOF - 24 * 3600)
        unripe = entry("unripe", ASOF - 3600)
        d = mod.audit(journal(old, recent, unripe), journal(), ASOF)
        h24 = d["horizons"]["24"]
        self.assertEqual(h24["matured"], 2)
        self.assertEqual(h24["recorded_evaluation_count"], 1)
        self.assertEqual(h24["mature_missing_evaluation_count"], 1)
        self.assertEqual(h24["missing_and_now_older_than_400_candles"], 0)
        self.assertEqual(h24["not_mature"], 1)
        self.assertNotIn("pnl_eur", json.dumps(d))

    def test_48_and_72h_are_not_supported_by_production(self):
        old = entry("old", ASOF - 90 * 3600)
        report = mod.audit(journal(old), journal(), ASOF)
        for hours in ("48", "72"):
            row = report["horizons"][hours]
            self.assertFalse(row["pipeline_supports_horizon"])
            self.assertEqual(row["matured"], 1)
            self.assertEqual(row["recorded_evaluation_count"], 0)
            self.assertEqual(row["missing_and_now_older_than_400_candles"], 1)

    def test_direct_overlap_deduplicated_and_evaluations_preserved(self):
        canonical = journal(entry("a", ASOF - 90 * 3600))
        direct = journal(entry("a", ASOF - 90 * 3600, evaluations={"24": {"status": "COMPLETE"}}),
                         entry("b", ASOF - 90 * 3600, decision_type="REJECTED"))
        result = mod.audit(canonical, direct, ASOF)
        self.assertEqual(result["overlap_rows"], 1)
        self.assertEqual(result["unique_retained_machine_decisions"], 2)
        self.assertEqual(result["horizons"]["24"]["matured"], 2)
        self.assertEqual(result["horizons"]["24"]["recorded_evaluation_count"], 1)
        self.assertEqual(result["horizons"]["24"]["missing_and_now_older_than_400_candles"], 1)

    def test_explicit_future_decision_refused(self):
        with self.assertRaises(mod.AuditError):
            mod.audit(journal(entry("f", ASOF + 1)), journal(), ASOF)

    def test_bad_input_rejected(self):
        with self.assertRaises(mod.AuditError):
            mod.audit({"schema": "other", "entries": []}, journal(), ASOF)
        with self.assertRaises(mod.AuditError):
            mod.audit(journal({"market": "X-EUR", "decision_ts": None}), journal(), ASOF)

    def test_missing_48h_not_confused_with_no_matching_market(self):
        x = entry("a", ASOF - 60 * 3600)
        result = mod.audit(journal(), journal(x), ASOF)
        self.assertEqual(result["horizons"]["48"]["matured"], 1)
        self.assertEqual(result["horizons"]["72"]["not_mature"], 1)
        self.assertEqual(result["horizons"]["48"]["recorded_evaluation_coverage_pct"], 0)

    def test_utc_asof_required(self):
        self.assertEqual(mod.parse_asof("2026-10-11T20:00:00Z"), ASOF)
        with self.assertRaises(mod.AuditError):
            mod.parse_asof("2026-10-11T20:00:00+02:00")
        with self.assertRaises(mod.AuditError):
            mod.parse_asof("2026-10-11T20:00:00")


if __name__ == "__main__":
    unittest.main()
