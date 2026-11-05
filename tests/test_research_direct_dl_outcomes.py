import gzip
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.research_direct_dl_outcomes import candidates, inspect, select_due

STAMP=1_800_000_000.0

def utc(t):
    return datetime.fromtimestamp(t,timezone.utc).isoformat()

def raw_machine(price=1.0):
    return {"schema":"solaire_prospective_journal_v1","updated_at_ts":STAMP+10,
        "entries":[{"decision_id":"d1","signal_id":"s1","episode_id":"e1",
                    "decision_ts":STAMP,"market":"FET-EUR","decision_type":"BUY_SENT",
                    "signal_price_eur":price,"entry_eur":0.99,
                    "stop_eur":0.92,"tp1_eur":1.1}]}

def shadow(root,available=STAMP-300,action="WATCH"):
    d=Path(root)/"2027-01-15"
    d.mkdir(exist_ok=True)
    payload={"policy":"DECISION_LAYER_V1_SHADOW",
             "scan_at_utc":utc(available-80),"generated_at_utc":utc(available),
             "ranked":[{"market":"FET-EUR","action":action}]}
    with gzip.open(d/"s.json.gz","wt") as f:
        json.dump(payload,f)

class FakeClient:
    def __init__(self):
        self.calls=0
    def get(self,url,params,cache=False):
        self.calls+=1
        return [[t,1.0,1.12,0.95,1.04,10] for t in range(params["start"],params["end"],300000)]

class DirectDLTests(unittest.TestCase):
    def test_explicit_true_machine_buy_provenance(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root)
            data,meta=candidates(raw_machine(),root)
            self.assertEqual(meta["n_time_matched_buy_sent"],1)
            self.assertEqual(data[0]["dl_action_at_previous_generated_snapshot"],"WATCH")
            self.assertEqual(data[0]["source_model_entry_limit_eur"],0.99)

    def test_stale_shadow_cannot_be_backfilled(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root,available=STAMP-4000)
            data,meta=candidates(raw_machine(),root)
            self.assertEqual(len(data),0)
            self.assertEqual(meta["unmatched_or_unusable"]["STALE_SHADOW"],1)

    def test_future_shadow_is_not_asof(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root,available=STAMP+1)
            data,meta=candidates(raw_machine(),root)
            self.assertEqual(len(data),0)
            self.assertEqual(meta["unmatched_or_unusable"]["NO_PRIOR_SHADOW"],1)

    def test_reference_missing_is_not_zero(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root)
            data,meta=candidates(raw_machine(price=None),root)
            self.assertEqual(len(data),0)
            self.assertEqual(meta["unmatched_or_unusable"]["NO_POSITIVE_SIGNAL_MARK"],1)

    def test_chronological_selection_no_72h_lookahead(self):
        event={"market":"FET-EUR","scan_ts":STAMP}
        due=select_due([event],STAMP+24*3600+301)
        self.assertEqual([x["hours"] for x in due],[24])

    def test_price_outcomes_preserve_noncausal_flags(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root,action="VETO_STRUCTUREL")
            client=FakeClient()
            result=inspect(raw_machine(),root,client,STAMP+24*3600+301)
            self.assertEqual(result["matured_sample_size"],1)
            self.assertEqual(result["results"][0]["status"],"COMPLETE")
            self.assertIsNone(result["net_portfolio_pnl_eur"])
            self.assertFalse(result["same_signal_causal_A_B"])
            self.assertFalse(result["results"][0]["actual_position_filled"])
            self.assertEqual(result["summary_by_prior_dl_action"][0]["previous_dl_action"],"VETO_STRUCTUREL")
            self.assertEqual(client.calls,1)

    def test_rejected_machine_is_never_placed_in_buy_sample(self):
        with tempfile.TemporaryDirectory() as root:
            shadow(root)
            m=raw_machine()
            m["entries"][0]["decision_type"]="REJECTED"
            rows,meta=candidates(m,root)
            self.assertEqual(rows,[])
            self.assertEqual(meta["n_direct_buy_sent"],0)

if __name__=="__main__":
    unittest.main()
