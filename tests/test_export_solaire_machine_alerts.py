"""Prove that public Solaire causal records are not confused with ChatGPT trades."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "export_solaire_machine_alerts.py"
SPEC = importlib.util.spec_from_file_location("export_solaire_machine_alerts", SCRIPT)
# The exporter expects the existing sidecar from the same directory.
import sys
sys.path.insert(0, str(SCRIPT.parent))
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


def event(decision_type, i=1, **kw):
    d = {"cycle_id": "cycle", "decision_ts": 1791492667.396356+i,
         "market": "OGN-EUR", "decision_type": decision_type,
         "reason": "DELIVERED" if decision_type == "BUY_SENT" else "SPREAD_TOO_WIDE",
         "signal_id": f"signal_{i}", "decision_id": f"decision_{i}",
         "episode_id": f"episode_{i}", "entry_eur": 0.0211,
         "stake_eur": 150}
    d.update(kw)
    return d


class MachineJournalBridgeTests(unittest.TestCase):
    def test_buy_sent_only_and_redacted(self):
        buy = event("BUY_SENT")
        rejected = event("REJECTED", i=2)
        alerts, s = bridge.export_records({"schema":"s","entries":[buy,rejected]})
        self.assertEqual(len(alerts), 1)
        self.assertEqual(s["buy_sent_count"], 1)
        self.assertEqual(s["rejected_count"], 1)
        self.assertEqual(alerts[0]["action"], "ACHETE")
        self.assertEqual(alerts[0]["market"], "OGN-EUR")
        self.assertNotIn("entry_eur", alerts[0])
        self.assertNotIn("stake_eur", alerts[0])
        self.assertEqual(s["historical_coverage"], "OBSERVED_WINDOW_ONLY")

    def test_unknown_prehistory(self):
        alerts, s = bridge.export_records({"entries":[event("BUY_SENT")]})
        self.assertNotIn("FULL_HISTORY", s["historical_coverage"])
        self.assertIn("UNKNOWN", " ".join(s["limitations"]))

    def test_duplicate_provider_record_not_counted_twice(self):
        buy = event("BUY_SENT")
        alerts, s = bridge.export_records({"entries":[buy, dict(buy)]})
        self.assertEqual(len(alerts), 1)
        self.assertEqual(s["buy_sent_count"], 1)

    def test_non_buy_rejected_is_not_chatgpt_decision(self):
        alerts, s = bridge.export_records({"entries":[event("REJECTED")]})
        self.assertEqual(alerts, [])
        self.assertEqual(s["rejection_reasons"]["SPREAD_TOO_WIDE"], 1)

    def test_out_of_order_records_are_sorted(self):
        alerts, _ = bridge.export_records({"entries":[event("BUY_SENT",i=3), event("BUY_SENT",i=1)]})
        self.assertEqual(alerts[0]["signal_id"], "solaire:signal_1:decision_1")

    def test_incomplete_record_rejected(self):
        with self.assertRaises(bridge.InputError):
            bridge.export_records({"entries":[event("BUY_SENT",signal_id=None)]})
        with self.assertRaises(bridge.InputError):
            bridge.export_records({"entries":[event("BUY_SENT",decision_ts=None)]})
        with self.assertRaises(bridge.InputError):
            bridge.export_records({"x":[]})

    def test_outputs_outside_public_repo_and_cli(self):
        import contextlib, io
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)
            journal=p/"journal.json"
            out=p/"machine.jsonl"
            summary=p/"summary.json"
            journal.write_text(json.dumps({"entries":[event("BUY_SENT"),event("REJECTED",i=2)]}),encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                result=bridge.main(["--journal",str(journal),"--output",str(out),"--summary",str(summary)])
            self.assertEqual(result, 0)
            records=[json.loads(x) for x in out.read_text().splitlines()]
            self.assertEqual(len(records),1)
            self.assertEqual(json.loads(summary.read_text())["buy_sent_count"],1)
            with contextlib.redirect_stderr(io.StringIO()):
                result=bridge.main(["--journal",str(journal),"--output",str(SCRIPT),"--summary",str(summary)])
            self.assertEqual(result,2)


if __name__ == "__main__":
    unittest.main()
