import unittest

from scripts.audit_dl_dispatches import analyze_day, report

NAME="Bitvavo live data + frozen V4 + measurement + useful alerts"

def row(i,date="2026-10-15",name=NAME,event="schedule",conclusion="success"):
    return {"id":i,"name":name,"event":event,"conclusion":conclusion,
            "created_at":date+"T12:34:56Z"}

class GithubDispatchTests(unittest.TestCase):
    def test_only_legacy_workflow_schedule_counted(self):
        sample=[row(1),row(2,event="push"),row(3,name="Other workflow")]
        o=analyze_day("2026-10-15",lambda day,page:{
            "total_count":3,"workflow_runs":sample})
        self.assertEqual(o["legacy_schedule_recorded"],1)
        self.assertEqual(o["legacy_push_recorded"],1)
        self.assertEqual(o["legacy_success_recorded"],2)
        self.assertEqual(o["nominal_cron_slots_without_recorded_schedule_run"],95)
        self.assertTrue(o["nominal_cron_gap_not_platform_failure_proof"])

    def test_complete_two_page_pagination(self):
        a=[row(i) for i in range(1,101)]
        b=[row(101,event="push")]
        calls=[]
        def fetch(day,p):
            calls.append(p)
            return {"total_count":101,"workflow_runs":a if p==1 else b}
        x=analyze_day("2026-10-15",fetch)
        self.assertEqual(calls,[1,2])
        self.assertEqual(x["legacy_schedule_recorded"],100)
        self.assertEqual(x["legacy_push_recorded"],1)

    def test_refuse_github_paginated_total_change(self):
        def fetch(day,p):
            return {"total_count":101 if p==1 else 102,
                    "workflow_runs":[row(i) for i in range(1,101)] if p==1 else [row(101)]}
        with self.assertRaises(ValueError):
            analyze_day("2026-10-15",fetch)

    def test_duplicate_runs_fail_closed(self):
        def fetch(day,p):
            return {"total_count":2,"workflow_runs":[row(1),row(1)]}
        with self.assertRaises(ValueError):
            analyze_day("2026-10-15",fetch)

    def test_lookups_are_unknown_not_zero(self):
        def bad(day,page):
            raise ValueError("API unavailable")
        x=report(["2026-10-15"],bad)
        self.assertFalse(x["all_days_complete"])
        self.assertIsNone(x["days"][0]["legacy_schedule_recorded"])
        self.assertIsNone(x["number_of_undelivered_schedule_events_proven"])

    def test_total_pages_cap(self):
        x=analyze_day("2026-10-15",lambda day,page:{"total_count":1500,"workflow_runs":[]})
        self.assertEqual(x["status"],"INCOMPLETE_TOO_MANY_PAGES")
        self.assertIsNone(x["legacy_schedule_recorded"])

    def test_wrong_day_run_rejected(self):
        with self.assertRaises(ValueError):
            analyze_day("2026-10-15",lambda day,page:{"total_count":1,
                "workflow_runs":[row(1,date="2026-10-14")]})

    def test_no_rows_means_zero_recorded_not_root_cause(self):
        x=report(["2026-10-15"],lambda d,p:{"total_count":0,"workflow_runs":[]})
        self.assertEqual(x["days"][0]["legacy_schedule_recorded"],0)
        self.assertFalse(x["root_cause_proven"])

if __name__=="__main__":
    unittest.main()
