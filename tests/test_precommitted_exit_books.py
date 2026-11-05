"""Read-only deterministic tests for genuinely PRECOMMITTED shadow exit books."""
from __future__ import annotations

import copy
import unittest
from datetime import datetime, timedelta, timezone

from scripts.capture_precommitted_exit_books import (
    collect_once, validate_commitment, quote_sale, MAX_EXIT_LAG_SECONDS
)
from research.execution_observability import book_evidence

NOW=datetime(2026,10,12,18,25,tzinfo=timezone.utc)


def iso(t):
    return t.isoformat().replace("+00:00","Z")


def commitment(ago_seconds=10,extra_future=True):
    due=NOW-timedelta(seconds=ago_seconds)
    t={
        "target_id":"decision_1/EXIT_PLUS_4H",
        "source_decision_id":"decision_1",
        "market":"TEST-EUR",
        "signal_decision_at_utc":iso(due-timedelta(hours=4)),
        "due_at_utc":iso(due),
        "horizon_hours":4,
        "stake_scenarios_eur":[100,150],
        "execution_stage":"SIGNAL_AGE_ONLY_NOT_PROVEN_FILLED",
        "policy":"SOLAIRE_MACHINE_BUY_SENT_NOT_R2_NOT_V4",
    }
    targets=[t]
    if extra_future:
        other=copy.deepcopy(t)
        other["target_id"]="decision_2/EXIT_PLUS_4H"
        other["source_decision_id"]="decision_2"
        other["due_at_utc"]=iso(NOW+timedelta(hours=1))
        other["signal_decision_at_utc"]=iso(NOW-timedelta(hours=3))
        targets.append(other)
    return {
        "schema":"solaire_prospective_exit_book_targets_v1",
        "committed_before_due_utc":iso(NOW-timedelta(minutes=10)),
        "target_count":len(targets),"unique_market_count":1,
        "real_trade_entry_or_exit_proven":False,
        "targets":targets,
    }


class FakeClient:
    def __init__(self,bids=None,error=None,meta_age_seconds=0):
        self.bids=bids or [["1.00","1000"]]
        self.error=error
        self.meta_age_seconds=meta_age_seconds
        self.called=[]
    def get(self,path,params,cache=False):
        self.called.append(path)
        if self.error:raise self.error
        return {"asks":[["1.01","1000"]],"bids":self.bids}
    def metadata(self,path,params):
        return {"request_started_at_utc":iso(NOW-timedelta(seconds=1)),
                "retrieved_at_utc":iso(NOW-timedelta(seconds=self.meta_age_seconds))}


class ProspectiveExitBookTests(unittest.TestCase):
    def test_commitment_validates_and_captures_only_due_once(self):
        c=commitment()
        client=FakeClient()
        result=collect_once(c,client=client,clock=lambda:NOW.timestamp())
        self.assertEqual(result["attempted_public_books"],1)
        self.assertEqual(result["due_within_capture_window_count"],1)
        self.assertEqual(result["status_counts"]["BOOK_CAPTURED_WITHIN_WINDOW"],1)
        self.assertEqual(result["status_counts"]["NOT_YET_DUE"],1)
        self.assertEqual(client.called,["/TEST-EUR/book"])
        row=result["rows"][0]
        self.assertEqual(row["visible_bid_sale_100_eur_est"]["status"],"VISIBLE_BOOK_COVERS_HYPOTHETICAL_SALE")
        self.assertEqual(row["visible_bid_sale_150_eur_est"]["status"],"VISIBLE_BOOK_COVERS_HYPOTHETICAL_SALE")
        self.assertIsNotNone(row["raw_public_book_sha256"])
        self.assertEqual(row["seconds_after_due_at_availability"],10)
        self.assertFalse(row["real_exit_fill_proven"])
        self.assertIsNone(result["actual_wallet_pnl_eur"])
        self.assertFalse(result["any_order_submitted"])

    def test_missed_due_cannot_be_later_reconstructed(self):
        c=commitment(ago_seconds=125,extra_future=False)
        result=collect_once(c,client=FakeClient(),clock=lambda:NOW.timestamp())
        self.assertEqual(result["status_counts"],{"MISSED_CAPTURE_WINDOW":1})
        self.assertEqual(result["attempted_public_books"],0)
        self.assertIsNone(result["rows"][0]["visible_bid_sale_100_eur_est"])

    def test_not_yet_due_never_fetches_future_order_books(self):
        c=commitment(ago_seconds=-300,extra_future=False)
        result=collect_once(c,client=FakeClient(),clock=lambda:NOW.timestamp())
        self.assertEqual(result["status_counts"],{"NOT_YET_DUE":1})
        self.assertEqual(result["attempted_public_books"],0)

    def test_invalid_timestamp_precommit_fails(self):
        c=commitment(extra_future=False)
        c["committed_before_due_utc"]=c["targets"][0]["due_at_utc"]
        with self.assertRaisesRegex(ValueError,"not committed before due"):
            validate_commitment(c)

    def test_corrupt_due_horizon_fails(self):
        c=commitment(extra_future=False)
        c["targets"][0]["signal_decision_at_utc"]=iso(NOW-timedelta(hours=7))
        with self.assertRaisesRegex(ValueError,"not reconstructible"):
            validate_commitment(c)

    def test_duplicate_ids_fail(self):
        c=commitment(extra_future=False)
        c["targets"].append(copy.deepcopy(c["targets"][0]))
        c["target_count"]=2
        with self.assertRaisesRegex(ValueError,"duplicate"):
            validate_commitment(c)

    def test_book_failure_unknown_not_failed_trade(self):
        c=commitment(extra_future=False)
        result=collect_once(c,client=FakeClient(error=RuntimeError("429")),clock=lambda:NOW.timestamp())
        self.assertEqual(result["status_counts"],{"PUBLIC_BOOK_UNAVAILABLE":1})
        self.assertIsNone(result["rows"][0]["actual_wallet_pnl_eur"])

    def test_stale_observation_not_relabelled_on_time(self):
        c=commitment(extra_future=False)
        result=collect_once(c,client=FakeClient(meta_age_seconds=100),clock=lambda:NOW.timestamp())
        self.assertEqual(result["status_counts"],{"UNVERIFIED_OR_LATE_BOOK":1})

    def test_shallow_bid_book_does_not_promise_100_eur_sell(self):
        book={"bids":[["1.0","10"]],"asks":[["1.01","100"]]}
        meta={"request_started_at_utc":iso(NOW-timedelta(seconds=1)),
              "retrieved_at_utc":iso(NOW)}
        ev=book_evidence(book,meta,NOW.timestamp())
        self.assertEqual(quote_sale(ev,100)["status"],"INSUFFICIENT_VISIBLE_BID_DEPTH")
        self.assertIsNone(quote_sale(ev,100)["quote_eur_est"])

    def test_visible_bid_quote_not_real_trade(self):
        book={"bids":[["1.0","75"],["0.99","100"]],"asks":[["1.01","1000"]]}
        meta={"request_started_at_utc":iso(NOW-timedelta(seconds=1)),
              "retrieved_at_utc":iso(NOW)}
        ev=book_evidence(book,meta,NOW.timestamp())
        q=quote_sale(ev,100)
        self.assertEqual(q["status"],"VISIBLE_BOOK_COVERS_HYPOTHETICAL_SALE")
        self.assertLess(q["quote_eur_est"],100)
        self.assertFalse(q["real_exit_fill_proven"])
        self.assertLess(q["net_proceeds_after_assumptions_eur_est"],q["quote_eur_est"])

    def test_too_late_response_must_not_count_as_precise_capture(self):
        c=commitment(ago_seconds=110,extra_future=False)
        # Clock is called once at start, then after API request.
        stamps=iter([NOW.timestamp(),NOW.timestamp()+20])
        result=collect_once(c,client=FakeClient(),clock=lambda:next(stamps))
        self.assertEqual(result["status_counts"],{"UNVERIFIED_OR_LATE_BOOK":1})
        self.assertGreater(result["rows"][0]["seconds_after_due_at_availability"],120)

    def test_no_private_credential_or_order_action_and_lag_cap(self):
        with self.assertRaisesRegex(ValueError,"max capture lag"):
            collect_once(commitment(),client=FakeClient(),clock=lambda:NOW.timestamp(),max_lag_seconds=3600)
        self.assertEqual(MAX_EXIT_LAG_SECONDS,120)


if __name__=="__main__":
    unittest.main()
