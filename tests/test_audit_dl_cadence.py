import unittest

from scripts.audit_dl_cadence import summarize_cadence
from scripts.compare_direct_decision_shadow import EvidenceError

class CadenceTests(unittest.TestCase):
    def test_window_coverage_counts_not_future(self):
        events = [
            {"decision_id": "d1", "signal_id": "s1", "episode_id": "e1",
             "decision_ts": 2000000000.0, "decision_type": "BUY_SENT", "market": "FET-EUR"},
            {"decision_id": "d2", "signal_id": "s2", "episode_id": "e2",
             "decision_ts": 2000004000.0, "decision_type": "REJECTED", "market": "FET-EUR"},
        ]
        shadow = [
            {"available_ts": 1999999800.0, "scan_ts": 1999999700.0,
             "source": "old", "actions": {"FET-EUR": "WATCH"}},
            {"available_ts": 2000004100.0, "scan_ts": 2000004000.0,
             "source": "future", "actions": {"FET-EUR": "ACHETE_MAINTENANT"}},
        ]
        result=summarize_cadence(events,shadow,windows=(900,3600))
        self.assertEqual([x["machine_events_asof_matched"] for x in result["time_window_sensitivity"]],[1,1])
        self.assertEqual([x["machine_buys_asof_matched"] for x in result["time_window_sensitivity"]],[1,1])
        self.assertIsNone(result["paired_net_pnl_eur"])
        self.assertFalse(result["causal_filtering_verified"])

    def test_more_lenient_window_only_changes_coverage(self):
        event = [{"decision_id":"d","signal_id":"s","episode_id":"e",
                  "decision_ts":2000000000.0,"decision_type":"BUY_SENT","market":"FET-EUR"}]
        shadow=[{"available_ts":1999998000.0,"scan_ts":1999997900.0,
                 "source":"old","actions":{"FET-EUR":"VETO_STRUCTUREL"}}]
        result=summarize_cadence(event,shadow,windows=(900,3600))
        self.assertEqual([x["machine_buys_asof_matched"] for x in result["time_window_sensitivity"]],[0,1])
        self.assertFalse(result["generated_not_verified_published"] is False)

    def test_reject_invalid_windows(self):
        with self.assertRaises(EvidenceError):
            summarize_cadence([],[],windows=(900,900))
        with self.assertRaises(EvidenceError):
            summarize_cadence([],[],windows=(0,))

    def test_empty_inputs_are_nonmeasurable(self):
        result=summarize_cadence([],[])
        self.assertEqual(result["daily_shadow_generated_observations"],[])
        self.assertIsNone(result["time_window_sensitivity"][0]["machine_buys_asof_matched_pct"])

    def test_day_count_is_not_equated_with_ran_jobs(self):
        events=[]
        shadow=[{"available_ts":1792080000.0,"scan_ts":1792079980.0,"source":"one","actions":{}},
                {"available_ts":1792080900.0,"scan_ts":1792080880.0,"source":"two","actions":{}}]
        day=summarize_cadence(events,shadow)["daily_shadow_generated_observations"][0]
        self.assertEqual(day["n_snapshots"],2)
        self.assertIsNone(day["configured_15min_slots_if_full_day"])
        self.assertIn("not a count",day["interpretation"])

if __name__ == "__main__":
    unittest.main()
