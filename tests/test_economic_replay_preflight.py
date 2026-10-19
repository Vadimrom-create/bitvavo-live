"""Preflight: conversion of matched real public books into UNFILLED model signals."""
from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from scripts.prepare_economic_replay import prepare
from scripts.run_economic_portfolio_replay import evaluate_preflight

T0 = datetime(2026, 10, 1, tzinfo=timezone.utc)


def stamp(dt):
    return dt.isoformat().replace("+00:00", "Z")


def joined_book(lag=1.8, matched=True):
    return {
        "schema": "solaire_economic_machine_book_join_v1",
        "source": {"sha256": "f" * 64},
        "records": [
            {
                "decision_type": "BUY_SENT", "decision_id": "d1",
                "market": "AAA-EUR",
                "observed_at_utc": stamp(T0 + timedelta(minutes=1)),
                "execution_observation_id": "obs-1",
                "machine_plan": {
                    "entry_limit_eur": 10, "stop_eur": 9,
                    "tp1_eur": 12, "tp2_eur": 13, "stake_eur": 100,
                    "structural_plan_valid": True,
                },
                "historical_book_evidence": {
                    "book_observation_status": "MATCHED_PUBLIC_BOOK_ESTIMATE" if matched else "INVALID_BOOK_QUOTE_OR_TIMESTAMP",
                    "book_available_at_utc": stamp(T0 + timedelta(minutes=1, seconds=2)),
                    "book_vs_decision_seconds": lag,
                    "stake_estimates": {
                        "100": {"entry_book_covered": True, "same_snapshot_exit_book_covered": True},
                        "150": {"entry_book_covered": True, "same_snapshot_exit_book_covered": True},
                    },
                },
            },
            {"decision_type": "REJECTED", "decision_id": "x2", "market": "BBB-EUR"},
        ],
    }


class ReplayPreflightTests(unittest.TestCase):
    def test_only_buy_sent_with_matched_book_becomes_hypothetical_candidate(self):
        p = prepare(joined_book())
        self.assertEqual(p["alert_count"], 1)
        self.assertEqual(p["prepared_signal_count"], 1)
        self.assertEqual(p["missing_book_proof_count"], 0)
        self.assertEqual(p["events"][0]["policy_id"], "SOLAIRE_PRODUCTION_BUY_SENT_NOT_V4_NOT_R2")
        self.assertFalse(p["model_replay_ready"])

    def test_missing_book_is_evidence_gap_not_negative_trade(self):
        p = prepare(joined_book(matched=False))
        self.assertEqual(p["prepared_signal_count"], 0)
        self.assertEqual(p["missing_book_proof_count"], 1)
        self.assertEqual(p["unresolved_book_proof"][0]["reason"], "BOOK_UNAVAILABLE_OR_BAD")

    def test_lag_over_one_minute_refused(self):
        p = prepare(joined_book(lag=65))
        self.assertEqual(p["missing_book_proof_count"], 1)
        self.assertEqual(p["prepared_signal_count"], 0)

    def test_no_candle_path_pnl_must_be_unknown(self):
        p = prepare(joined_book())
        r = evaluate_preflight(p, None, None)
        self.assertEqual(r["status"], "NOT_READY_NO_PUBLIC_PRICE_PATHS_SUPPLIED")
        self.assertIsNone(r["modeled_portfolio_pnl_eur"])
        self.assertIsNone(r["real_bitvavo_pnl_eur"])

    def test_explicit_complete_candles_can_produce_model_only_pnl(self):
        p = prepare(joined_book())
        def bar(minute, high=10.5):
            return {
                "start_utc": stamp(T0 + timedelta(minutes=minute)),
                "open": 10, "high": high, "low": 9.5, "close": 10,
            }
        asof = stamp(T0 + timedelta(days=2))
        import hashlib
        import json
        markets = {"AAA-EUR": [bar(5), bar(10, high=12.5)]}
        digest = hashlib.sha256(json.dumps(markets, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
        candles = {
            "schema": "solaire_closed_5m_candles_bundle_v1",
            "asof_utc": asof,
            "source_sha256": digest,
            "markets": markets,
        }
        r = evaluate_preflight(p, candles, asof, horizon_hours=24)
        self.assertEqual(r["status"], "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF")
        self.assertGreater(r["modeled_portfolio_pnl_eur"], 0)
        self.assertIsNone(r["real_bitvavo_pnl_eur"])
        self.assertFalse(r["comparisons_ready"])

    def test_wrong_asof_for_candles_fails(self):
        p = prepare(joined_book())
        candle = {
            "schema": "solaire_closed_5m_candles_bundle_v1",
            "asof_utc": "2026-10-03T00:00:00Z",
            "source_sha256": "a" * 64,
            "markets": {},
        }
        with self.assertRaisesRegex(ValueError, "asof must exactly match"):
            evaluate_preflight(p, candle, "2026-10-04T00:00:00Z")

    def test_bogus_candle_checksum_rejected(self):
        p = prepare(joined_book())
        candles = {
            "schema": "solaire_closed_5m_candles_bundle_v1",
            "asof_utc": stamp(T0 + timedelta(days=2)),
            "source_sha256": "0" * 64,
            "markets": {"AAA-EUR": []},
        }
        with self.assertRaisesRegex(ValueError, "SHA-256 does not match"):
            evaluate_preflight(p, candles, candles["asof_utc"])

    def test_bad_stake_rejected(self):
        with self.assertRaisesRegex(ValueError, "fixed stake"):
            prepare(joined_book(), stake_eur=500)

    def test_book_costs_are_not_treated_as_real_fills(self):
        p = prepare(joined_book())
        self.assertFalse(p["events"][0]["real_order_claimed"])
        self.assertIsNone(p["real_bitvavo_pnl_eur"])


if __name__ == "__main__":
    unittest.main()
