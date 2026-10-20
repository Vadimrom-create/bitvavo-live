import copy
import gzip
import json
import tempfile
import unittest
from pathlib import Path

from scripts.capture_direct_dl_prospective_receipt import validate_packet, main

TIME="2026-10-17T07:15:07+00:00"
BASE=1792221307.0
SHA="a"*40
HASHES={
    "production_scan_status.json":"a"*64,
    "production_alert_candidates.json":"b"*64,
    "production_universe_snapshot.json":"c"*64,
}
def inputs():
    s={"schema":"solaire_direct_scan_v2","signal_at_utc":TIME,
       "universe_snapshot_rows":2,"markets_collected":2}
    c={"schema":"production_alert_candidates_v6_catalyst",
       "generated_at_utc":TIME,"decision_layer_required":False,
       "watch":[{"market":"FET-EUR","action_status":"ACCELERATION_READY",
                 "signal_state":"CONFIRMED_ACCELERATION","last":0.17}]}
    u={"schema":"solaire_production_universe_snapshot_v2_news",
       "generated_at_utc":TIME,
       "rows":[
          {"market":"FET-EUR","features":{"5m":{"valid":True}},
           "acceleration":{"state":"CONFIRMED_ACCELERATION"},
           "data_quality":{"ok":True},"timestamps":{"scan_at_utc":TIME}},
          {"market":"LINK-EUR","features":{"5m":{"valid":True}}}
       ]}
    return s,c,u

class ProspectiveReceiptTests(unittest.TestCase):
    def test_same_direct_scan_preserves_features_with_missing_dl_input(self):
        s,c,u=inputs()
        from scripts.capture_direct_dl_prospective_receipt import utc_epoch
        t=utc_epoch(TIME)
        x=validate_packet(s,c,u,None,asof_ts=t+40,revision=SHA,hashes=HASHES)
        self.assertEqual(x["receipt_status"],"CAPTURED_SAME_DIRECT_SCAN")
        self.assertEqual(x["candidate_count"],1)
        self.assertEqual(x["full_universe_market_rows_archived"],2)
        self.assertEqual(len(x["full_universe_rows"]),2)
        self.assertFalse(x["full_universe_hash_only"])
        self.assertEqual(x["candidate_rows"][0]["same_cycle_acceleration"]["state"],"CONFIRMED_ACCELERATION")
        self.assertEqual(x["candidate_rows"][0]["decision_layer_v1_same_input_status"],"UNSUPPORTED_NO_V4_BASELINE")
        self.assertFalse(x["same_input_v4_dl_classification_proven"])
        self.assertFalse(x["real_buy_sent_proven"])
        self.assertIsNone(x["net_portfolio_pnl_eur"])

    def test_mismatched_scan_id_fails_not_join_across_cycles(self):
        s,c,u=inputs()
        c["generated_at_utc"]="2026-10-17T07:20:07+00:00"
        with self.assertRaises(ValueError):
            validate_packet(s,c,u,asof_ts=1800000000,revision=SHA,hashes=HASHES)

    def test_duplicate_markets_fail(self):
        s,c,u=inputs()
        u["rows"].append(copy.deepcopy(u["rows"][0]))
        s["universe_snapshot_rows"]=3
        s["markets_collected"]=3
        with self.assertRaises(ValueError):
            validate_packet(s,c,u,asof_ts=1800000000,revision=SHA,hashes=HASHES)

    def test_missing_candidate_market_fails(self):
        s,c,u=inputs()
        c["watch"][0]["market"]="W-EUR"
        with self.assertRaises(ValueError):
            validate_packet(s,c,u,asof_ts=1800000000,revision=SHA,hashes=HASHES)

    def test_stale_capture_is_censored(self):
        from scripts.capture_direct_dl_prospective_receipt import utc_epoch
        s,c,u=inputs()
        t=utc_epoch(TIME)
        x=validate_packet(s,c,u,asof_ts=t+901,revision=SHA,hashes=HASHES)
        self.assertEqual(x["receipt_status"],"REJECTED_STALE_DIRECT_SNAPSHOT")
        self.assertEqual(x["candidate_rows"],[])
        self.assertEqual(x["full_universe_rows"],[])
        self.assertTrue(x["full_universe_hash_only"])
        self.assertFalse(x["same_cycle_direct_features_proven"])

    def test_dl_generated_after_direct_time_never_used_as_prior(self):
        from scripts.capture_direct_dl_prospective_receipt import utc_epoch
        s,c,u=inputs()
        dl={"generated_at_utc":"2026-10-17T07:15:09+00:00","policy":"DECISION_LAYER_V1_SHADOW"}
        x=validate_packet(s,c,u,dl,asof_ts=utc_epoch(TIME)+50,revision=SHA,hashes=HASHES)
        self.assertEqual(x["prior_dl_status"],"DL_GENERATED_AFTER_DIRECT_SCAN")

    def test_dl_generated_before_still_not_equivalent_input(self):
        from scripts.capture_direct_dl_prospective_receipt import utc_epoch
        s,c,u=inputs()
        dl={"generated_at_utc":"2026-10-17T07:14:00+00:00","policy":"DECISION_LAYER_V1_SHADOW"}
        x=validate_packet(s,c,u,dl,asof_ts=utc_epoch(TIME)+30,revision=SHA,hashes=HASHES)
        self.assertEqual(x["prior_dl_status"],"DL_PRIOR_GEN_ONLY_DIFFERENT_V4_INPUTS")
        self.assertFalse(x["same_input_v4_dl_classification_proven"])

    def test_direct_gate_dependency_required_false(self):
        s,c,u=inputs()
        c["decision_layer_required"]=True
        with self.assertRaises(ValueError):
            validate_packet(s,c,u,asof_ts=1800000000,revision=SHA,hashes=HASHES)

    def test_main_creates_compressed_receipt_and_no_network(self):
        from scripts.capture_direct_dl_prospective_receipt import utc_epoch
        s,c,u=inputs()
        with tempfile.TemporaryDirectory() as root:
            for name,data in zip(("production_scan_status.json","production_alert_candidates.json","production_universe_snapshot.json"),(s,c,u)):
                (Path(root)/name).write_text(json.dumps(data),encoding="utf8")
            output=Path(root)/"receipt.json.gz"
            rc=main(["--source-dir",root,"--revision",SHA,
                     "--asof-epoch",str(utc_epoch(TIME)+10),"--output",str(output)])
            self.assertEqual(rc,0)
            with gzip.open(output,"rt") as f: out=json.load(f)
            self.assertEqual(out["candidate_count"],1)
            self.assertEqual(len(out["full_universe_rows"]),2)
            self.assertEqual(out["full_universe_market_rows_archived"],2)
            self.assertTrue(out["no_additional_market_data_requests"])

if __name__=="__main__":
    unittest.main()
