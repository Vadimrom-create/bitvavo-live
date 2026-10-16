"""Offline tests for public tape activity; no Bitvavo account calls."""
from __future__ import annotations
import copy
import unittest
from datetime import datetime, timedelta, timezone

from scripts.audit_frozen_exit_public_tape import (
    EXPECTED_MARKET_SHA, plan_targets, analyze_target, collect
)

T = datetime(2026, 10, 9, 20, tzinfo=timezone.utc)


def frozen():
    trade = {
        "event_id": "e1", "market": "TEST-EUR",
        "modeled_closed_utc": T.isoformat(),
        "exit_reason": "HORIZON_NEXT_REAL_BAR_OPEN_PROXY",
        "modeled_sell_proceeds_eur": 96,
    }
    return {
        "schema": "solaire_frozen_exit_executability_audit_v1",
        "source_candles_sha256": EXPECTED_MARKET_SHA,
        "alerts": 75, "markets": 44,
        "modes": {
            "flat_last_price": {
                "status": "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF",
                "trades": [trade],
            },
            "next_real_print": {
                "status": "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF",
                "trades": [trade],
            },
        },
    }


def trade(id, when, euro=90, side="sell"):
    return {
        "id": id, "timestamp": int(when.timestamp() * 1000),
        "price": "10", "amount": str(euro / 10), "side": side,
    }


class Client:
    def __init__(self, data):
        self.data = data
        self.calls = []
    def get(self, path, params, cache=False):
        self.calls.append((path, params))
        if isinstance(self.data, Exception):
            raise self.data
        return self.data


class FrozenExitPublicTapeTests(unittest.TestCase):
    def test_same_market_window_deduplicated_across_models(self):
        out = plan_targets(frozen())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["event_id"], "e1")
        self.assertEqual(out[0]["bar_start_utc"], (T-timedelta(minutes=5)).isoformat())

    def test_wrong_source_sha_rejected(self):
        f=frozen()
        f["source_candles_sha256"] = "0"*64
        with self.assertRaisesRegex(ValueError, "checksum"):
            plan_targets(f)

    def test_cannot_claim_book_or_real_fill_from_public_trade_prints(self):
        target=plan_targets(frozen())[0]
        data=[
            trade("a", T-timedelta(minutes=3), euro=70),
            trade("b", T-timedelta(minutes=2), euro=20),
            trade("c", T+timedelta(minutes=1), euro=140, side="buy"),
        ]
        r=analyze_target(target, data, T+timedelta(hours=1))
        self.assertEqual(r["market_prints_5m_ending_at_model_exit"]["trade_count"],2)
        self.assertAlmostEqual(r["market_prints_5m_ending_at_model_exit"]["total_printed_notional_eur"],90)
        self.assertTrue(r["market_prints_5m_ending_at_model_exit"]["printed_notional_under_100_eur"])
        self.assertEqual(r["market_prints_5m_after_model_exit"]["trade_count"],1)
        self.assertFalse(r["historical_bid_ask_or_depth_available"])
        self.assertFalse(r["model_exit_fill_verified"])

    def test_tape_activity_cannot_prove_exit_fill_even_with_high_turnover(self):
        client=Client([trade("x", T-timedelta(minutes=2), euro=250)])
        out=collect(frozen(),client=client,asof_time=T+timedelta(hours=1))
        self.assertEqual(out["summary"]["target_count"],1)
        self.assertEqual(out["summary"]["target_bar_printed_notional_under_100_eur_count"],0)
        self.assertEqual(out["summary"]["next_5m_no_public_prints_count"],1)
        self.assertFalse(out["real_exit_execution_proven"])
        self.assertIsNone(out["actual_wallet_pnl_eur"])
        self.assertEqual(len(client.calls),1)
        self.assertEqual(client.calls[0][1]["limit"],1000)
        self.assertLess(client.calls[0][1]["end"]-client.calls[0][1]["start"],24*3600*1000)

    def test_public_query_failure_remains_unknown_not_no_liquidity(self):
        r=collect(frozen(),client=Client(RuntimeError("temporarily unavailable")),
                  asof_time=T+timedelta(hours=1))
        self.assertEqual(r["summary"]["unknown_data_count"],1)
        self.assertEqual(r["summary"]["public_prints_captured_count"],0)
        self.assertIsNone(r["records"][0]["market_prints_5m_ending_at_model_exit"])

    def test_duplicate_trade_ids_rejected(self):
        x=plan_targets(frozen())[0]
        a=trade("a",T-timedelta(minutes=2))
        with self.assertRaisesRegex(ValueError,"duplicate"):
            analyze_target(x,[a,a],T+timedelta(hours=1))

    def test_outside_public_tape_window_rejected(self):
        x=plan_targets(frozen())[0]
        with self.assertRaisesRegex(ValueError,"out-of-window"):
            analyze_target(x,[trade("x",T+timedelta(hours=2))],T+timedelta(hours=3))

    def test_public_snapshot_truncation_is_unknown_completeness(self):
        x=plan_targets(frozen())[0]
        data=[trade(str(i),T-timedelta(minutes=2),euro=1) for i in range(1000)]
        r=analyze_target(x,data,T+timedelta(hours=1))
        self.assertTrue(r["public_trade_page_truncated_or_uncertain"])

    def test_tape_10min_window_unavailable_when_current_time_is_too_early(self):
        x=plan_targets(frozen())[0]
        with self.assertRaisesRegex(ValueError,"cutoff"):
            analyze_target(x,[],T+timedelta(minutes=2))


if __name__ == "__main__":
    unittest.main()
