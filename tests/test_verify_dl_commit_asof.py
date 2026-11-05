import unittest

from scripts.verify_dl_commit_asof import analyze, choose_source_paths

FILE="decision_history/2026-10-15/20261015T150857Z-47580a9e.json.gz"

def joined(*,action="BUY_SENT",age=120,ts=1800000000.0,path=FILE):
    return {"schema":"solaire_dl_asof_comparator_v1",
        "rows":[{"machine_action":action,"join_status":"ASOF_MATCH",
                 "shadow_age_seconds":age,"shadow_source":path,
                 "decision_id":"d1","machine_ts":ts,"market":"FIL-EUR"}]}

class CommitAuditTests(unittest.TestCase):
    def test_commit_date_prior_is_only_metadata(self):
        z=analyze(joined(),lambda _:{"status":"ONE_COMMIT_DATE_FOUND",
                                    "commit_ts":1799999960.0,"commit_sha":"abc"})
        self.assertEqual(z["event_commit_timing_statuses"],{"COMMIT_DATE_PRIOR_WITHIN_WINDOW":1})
        self.assertFalse(z["actual_public_visibility_at_signal_verified"])
        self.assertFalse(z["rows"][0]["remote_published_at_signal_verified"])
        self.assertIsNone(z["net_pnl_eur"])

    def test_sub_30_seconds_is_low_confidence(self):
        z=analyze(joined(),lambda _:{"status":"ONE_COMMIT_DATE_FOUND","commit_ts":1799999997.0})
        self.assertEqual(z["event_commit_timing_statuses"],{"COMMIT_DATE_PRIOR_LT30S_LOW_CONFIDENCE":1})

    def test_commit_date_after_signal_is_not_available(self):
        z=analyze(joined(),lambda _:{"status":"ONE_COMMIT_DATE_FOUND","commit_ts":1800000001.0})
        self.assertEqual(z["event_commit_timing_statuses"],{"COMMIT_DATE_AFTER_SIGNAL":1})

    def test_missing_commit_is_unknown(self):
        z=analyze(joined(),lambda _:{"status":"NO_COMMIT_FOUND"})
        self.assertEqual(z["event_commit_timing_statuses"],{"UNKNOWN_COMMIT_TIME":1})

    def test_outside_900s_generated_window_is_not_selected(self):
        z=analyze(joined(age=1400),lambda _:self.fail("should not be fetched"))
        self.assertEqual(z["n_matching_machine_buys"],0)

    def test_non_buy_excluded(self):
        z=analyze(joined(action="REJECTED"),lambda _:self.fail("should not be fetched"))
        self.assertEqual(z["n_matching_machine_buys"],0)

    def test_invalid_path_rejected(self):
        with self.assertRaises(ValueError):
            choose_source_paths(joined(path="../../secrets.txt"))

    def test_duplicate_archive_lookup_cached(self):
        j=joined()
        extra=dict(j["rows"][0],decision_id="d2",machine_ts=1800000100.0)
        j["rows"].append(extra)
        seen=[]
        def resolve(p):
            seen.append(p)
            return {"status":"ONE_COMMIT_DATE_FOUND","commit_ts":1799999950.0}
        z=analyze(j,resolve)
        self.assertEqual(len(seen),1)
        self.assertEqual(z["n_matching_machine_buys"],2)
        self.assertEqual(z["n_unique_shadow_paths"],1)

    def test_unexpected_lookup_errors_fail_closed(self):
        def fail(_):
            raise ValueError("network validation error")
        z=analyze(joined(),fail)
        self.assertEqual(z["git_commit_lookup_statuses"],{"LOOKUP_ERROR_ValueError":1})
        self.assertFalse(z["economic_effect_identified"])

    def test_commit_metadata_older_than_900s_not_fresh(self):
        z=analyze(joined(),lambda _:{"status":"ONE_COMMIT_DATE_FOUND","commit_ts":1799998000.0})
        self.assertEqual(z["event_commit_timing_statuses"],{"COMMIT_DATE_PRIOR_BUT_OLDER_THAN_WINDOW":1})

if __name__=="__main__":
    unittest.main()
