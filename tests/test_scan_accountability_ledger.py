"""Tests for private SCAN accountability sidecar, deliberately independent of trading."""
import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_accountability_ledger.py"
SPEC = importlib.util.spec_from_file_location("scan_accountability_ledger", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

ASOF = datetime.fromisoformat("2026-10-09T00:00:00+00:00")


def decision(**overrides):
    base = dict(record_type="scan_decision", decision_id="s1-ogn",
                market="OGN-EUR", source_at_utc="2026-10-08T10:00:00Z",
                decision_at_utc="2026-10-08T10:02:00Z",
                solaire_action="ACHETE", chatgpt_action="WAIT_RECHECK",
                reason_codes=["MACRO_PENDING"], recheck_trigger="new machine BUY",
                recheck_due_utc="2026-10-08T12:00:00Z",
                spread_pct=0.2, book_asof_utc="2026-10-08T10:01:00Z",
                roundtrip_150eur_pct=0.42)
    base.update(overrides)
    return base


class ScanAccountabilityTests(unittest.TestCase):
    def test_refusal_and_overdue_no_claimed_pnl(self):
        items = mod.validate_decisions([decision()], ASOF)
        result = mod.aggregate(items, [], [], ASOF)
        self.assertEqual(result["machine_buy_refused_ids"], ["s1-ogn"])
        self.assertEqual(result["overdue_recheck_ids"], ["s1-ogn"])
        self.assertEqual(result["paired_net"]["4"]["verdict"], "NON_MESURABLE")
        self.assertEqual(result["chatgpt_value_verdict"], "NON_MESURABLE")

    def test_new_machine_confirmation_after_refusal_is_reported(self):
        ds = mod.validate_decisions([decision()], ASOF)
        alerts = mod.validate_alerts([dict(record_type="machine_alert", market="OGN-EUR",
                                            signal_id="signal-2", action="ACHETE",
                                            signal_at_utc="2026-10-08T13:00:00Z")], ASOF)
        result = mod.aggregate(ds, alerts, [], ASOF)
        self.assertEqual(result["unreviewed_new_machine_alerts"][0]["new_signal_ids"],
                         ["signal-2"])

    def test_newer_chatgpt_decision_overrides_recheck(self):
        ds = mod.validate_decisions([
            decision(),
            decision(decision_id="s2-ogn", decision_at_utc="2026-10-08T13:01:00Z",
                     source_at_utc="2026-10-08T13:00:00Z",
                     chatgpt_action="BUY", reason_codes=["NEW_CONFIRMATION"],
                     recheck_due_utc=None, recheck_trigger=None),
        ], ASOF)
        alerts = mod.validate_alerts([dict(record_type="machine_alert", market="OGN-EUR",
                                            signal_id="signal-2", action="ACHETE",
                                            signal_at_utc="2026-10-08T13:00:00Z")], ASOF)
        result = mod.aggregate(ds, alerts, [], ASOF)
        self.assertEqual(result["overdue_recheck_ids"], [])
        self.assertEqual(result["unreviewed_new_machine_alerts"], [])

    def test_pair_requires_all_four_proofs(self):
        ds = mod.validate_decisions([decision()], ASOF)
        good = dict(record_type="paired_outcome", decision_id="s1-ogn", horizon_hours=4,
                    both_executions_validated=True, matched_budget_policy_costs=True,
                    horizon_matured=True, independent_episode=True,
                    solaire_net_eur=2.5, chatgpt_net_eur=-1.2)
        pairs = mod.validate_pairs([good], {d["decision_id"] for d in ds})
        result = mod.aggregate(ds, [], pairs, ASOF)
        self.assertEqual(result["paired_net"]["4"]["chatgpt_minus_solaire_eur"], -3.7)
        self.assertEqual(result["chatgpt_value_verdict"], "PROVISIONAL_DESCRIPTIVE_ONLY")
        bad = dict(good, both_executions_validated=False)
        self.assertEqual(mod.validate_pairs([bad], {"s1-ogn"}), [])

    def test_no_lookahead(self):
        with self.assertRaises(mod.InputError):
            mod.validate_decisions([decision(source_at_utc="2026-10-08T10:03:00Z")], ASOF)
        with self.assertRaises(mod.InputError):
            mod.validate_decisions([decision(decision_at_utc="2026-10-10T10:00:00Z")], ASOF)

    def test_malformed_or_duplicate_records_rejected(self):
        with self.assertRaises(mod.InputError):
            mod.validate_decisions([decision(), decision()], ASOF)
        with self.assertRaises(mod.InputError):
            mod.validate_decisions([decision(reason_codes=[])], ASOF)
        with self.assertRaises(mod.InputError):
            mod.validate_pairs([dict(record_type="paired_outcome",
                                     decision_id="bad", horizon_hours=4)], {"s1-ogn"})

    def test_private_path_policy_and_header_skip(self):
        mod.outside_public_repo("/tmp/scan_decisions_private_v1.jsonl")
        with self.assertRaises(mod.InputError):
            mod.outside_public_repo(str(SCRIPT))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "private.jsonl"
            p.write_text('{"record_type":"ledger_header","schema_version":1}\n'
                         + json.dumps(decision()) + "\n", encoding="utf-8")
            self.assertEqual(len(mod.jsonl(p)), 1)


if __name__ == "__main__":
    unittest.main()
