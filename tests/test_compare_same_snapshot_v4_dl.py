import unittest

from scripts.compare_same_snapshot_v4_dl import SnapshotError, inspect_scan
from research.decision_layer import classify

def obs(market, accel, buy_ready=False, opp=8, entry=7, trend=8, quality=True, with_base=True):
    row={
        "market":market,"price_eur":0.16,"change_24h_pct":-2.0,
        "acceleration":{"state":accel} if accel is not None else None,
        "data_quality":{"ok":quality,"reasons":[] if quality else ["MISSING_5M"]},
        "exclusions":[],"category":"REENTRY",
        "chase_risk":{"score":0},"wick_setup":{"is_wick_setup":False},
        "recurrence":{"distinct_15m_periods":1},
    }
    if with_base:
        row["baseline"]={"buy_ready":buy_ready,"opportunity_score":opp,
                         "entry_score":entry,"trend_score":trend,
                         "action_status":"BUY_READY" if buy_ready else "WATCH",
                         "risk_flags":[]}
    return row

def scan(rows):
    return {"scan_id":"20261015T190628Z-7bd17fd8",
            "scan_at_utc":"2026-10-15T19:06:28+00:00","observations":rows}

class SameSnapshotTests(unittest.TestCase):
    def test_classifies_same_features(self):
        a=obs("A-EUR","CONFIRMED_ACCELERATION",buy_ready=True)
        b=obs("B-EUR","CONFIRMED_ACCELERATION",buy_ready=False)
        report=inspect_scan(scan([a,b]),source="memory",source_sha256="x"*64)
        self.assertEqual(report["counts"]["confirmed_and_immediate"],1)
        self.assertEqual(report["counts"]["confirmed_not_immediate"],1)
        self.assertFalse(report["actual_direct_production_gate_compared"])
        self.assertFalse(report["same_inputs_as_direct_production"])

    def test_missing_baseline_is_unknown_not_watch(self):
        a=obs("A-EUR","CONFIRMED_ACCELERATION",with_base=False)
        report=inspect_scan(scan([a]),source="memory",source_sha256="x"*64)
        self.assertEqual(report["counts"]["dl_DL_UNCLASSIFIABLE_NO_BASELINE"],1)
        self.assertEqual(report["counts"]["baseline_features_unknown"],1)

    def test_missing_acceleration_not_labeled_zero(self):
        a=obs("A-EUR",None)
        report=inspect_scan(scan([a]),source="memory",source_sha256="x"*64)
        self.assertEqual(report["counts"]["acceleration_state_unknown"],1)
        self.assertEqual(report["counts"]["acceleration_ACCELERATION_NOT_RECORDED"],1)

    def test_duplicate_market_fails_closed(self):
        a=obs("A-EUR","CONFIRMED_ACCELERATION")
        with self.assertRaises(SnapshotError):
            inspect_scan(scan([a,a]),source="memory",source_sha256="x"*64)

    def test_frozen_decision_replay_exact(self):
        a=obs("A-EUR","BUILDING_ACCELERATION")
        frozen={"scan_id":scan([a])["scan_id"],"ranked":[{"market":"A-EUR","action":classify(a)["action"]}]}
        out=inspect_scan(scan([a]),source="memory",source_sha256="x"*64,frozen_dl=frozen)
        self.assertTrue(out["dl_policy_replay_matches_archived"])
        self.assertEqual(out["counts"]["frozen_dl_action_matched"],1)

    def test_policy_drift_is_explicit(self):
        a=obs("A-EUR","BUILDING_ACCELERATION")
        frozen={"scan_id":scan([a])["scan_id"],"ranked":[{"market":"A-EUR","action":"VETO_STRUCTUREL"}]}
        out=inspect_scan(scan([a]),source="memory",source_sha256="x"*64,frozen_dl=frozen)
        self.assertFalse(out["dl_policy_replay_matches_archived"])
        self.assertEqual(out["counts"]["frozen_dl_action_mismatch"],1)

    def test_different_id_fails(self):
        a=obs("A-EUR","BUILDING_ACCELERATION")
        with self.assertRaises(SnapshotError):
            inspect_scan(scan([a]),source="memory",source_sha256="x"*64,frozen_dl={"scan_id":"other","ranked":[]})

if __name__=="__main__":
    unittest.main()
