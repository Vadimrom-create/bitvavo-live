import gzip
import json
import tempfile
import unittest
from pathlib import Path

from scripts.compare_direct_decision_shadow import (
    EvidenceError, compare, load_shadow_snapshots, read_events, utc_ts,
)

def machine(event_ts=1800000000.0, action="BUY_SENT", market="FET-EUR"):
    return {
        "schema": "solaire_prospective_journal_v1", "updated_at_ts": event_ts + 10,
        "entries": [{
            "decision_id": "d1", "signal_id": "s1", "episode_id": "e1",
            "market": market, "decision_type": action, "decision_ts": event_ts,
        }],
    }

def snapshot(ts, action="ACHETE_MAINTENANT", market="FET-EUR"):
    return {
        "available_ts": ts, "scan_ts": ts - 10, "source": "example.json.gz",
        "actions": {market: action},
    }

class JoinTests(unittest.TestCase):
    def test_future_shadow_never_attached(self):
        events = read_events(machine())
        old = snapshot(1799999999, "ATTENDS_REPRISE_OU_REENTREE")
        future = snapshot(1800000001)
        got = compare(events, [old, future])
        self.assertEqual(got["rows"][0]["shadow_action"], "ATTENDS_REPRISE_OU_REENTREE")
        self.assertIsNone(got["paired_net_pnl_eur"])
        self.assertFalse(got["shadow_availability_at_signal_verified"])

    def test_absence_is_not_refusal(self):
        x = compare(read_events(machine()), [snapshot(1800000001)])
        self.assertEqual(x["rows"][0]["join_status"], "NO_PRIOR_SHADOW")
        self.assertIsNone(x["rows"][0]["shadow_action"])

    def test_stale_is_not_rejection(self):
        x = compare(read_events(machine()), [snapshot(1799990000)])
        self.assertEqual(x["rows"][0]["join_status"], "STALE_SHADOW")
        self.assertIsNone(x["rows"][0]["shadow_action"])

    def test_market_missing(self):
        x = compare(read_events(machine()), [snapshot(1799999999, market="LINK-EUR")])
        self.assertEqual(x["rows"][0]["join_status"], "MARKET_MISSING_IN_SHADOW")

    def test_machine_rejection_not_chatgpt_veto(self):
        x = compare(read_events(machine(action="REJECTED")), [snapshot(1799999999)])
        self.assertEqual(x["asof_action_matrix"][0]["machine_action"], "REJECTED")
        self.assertEqual(x["n_machine_buy_sent"], 0)

    def test_duplicate_machine_decision_fails_closed(self):
        s = machine()
        s["entries"].append(dict(s["entries"][0]))
        with self.assertRaises(EvidenceError):
            read_events(s)

    def test_unknown_type_fails_closed(self):
        s = machine()
        s["entries"][0]["decision_type"] = "FILLED"
        with self.assertRaises(EvidenceError):
            read_events(s)

    def test_future_event_fails_closed(self):
        s = machine()
        s["entries"][0]["decision_ts"] += 50
        with self.assertRaises(EvidenceError):
            read_events(s)

    def test_non_utc_timestamp_fails_closed(self):
        with self.assertRaises(EvidenceError):
            utc_ts("2026-10-15T12:00:00+02:00")

    def test_archive_and_corrupt_file_are_separated(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d) / "2026-10-15"
            folder.mkdir()
            good = {
                "policy": "DECISION_LAYER_V1_SHADOW",
                "scan_at_utc": "2026-10-15T15:00:00+00:00",
                "generated_at_utc": "2026-10-15T15:01:00+00:00",
                "ranked": [{"market": "FET-EUR", "action": "WATCH"}],
            }
            with gzip.open(folder / "ok.json.gz", "wt") as f:
                json.dump(good, f)
            (folder / "bad.json.gz").write_text("corrupt")
            snaps, failures = load_shadow_snapshots(Path(d), {"FET-EUR"})
            self.assertEqual(len(snaps), 1)
            self.assertEqual(snaps[0]["actions"], {"FET-EUR": "WATCH"})
            self.assertEqual(sum(failures.values()), 1)

    def test_age_limit_respected(self):
        x = compare(read_events(machine()), [snapshot(1799999998)], max_age_seconds=1)
        self.assertEqual(x["join_status_counts"], {"STALE_SHADOW": 1})

if __name__ == "__main__":
    unittest.main()
