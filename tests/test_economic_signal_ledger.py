"""Offline tests: machine alerts never become fills, cash ledger has no leverage."""
from __future__ import annotations

import copy
import unittest

from research.economic_cash_ledger import LedgerError, calculate_cash_ledger
from scripts.build_economic_signal_ledger import EventLedgerError, build_machine_event_ledger

ASOF = "2026-10-11T12:10:00Z"


def machine_fixture():
    return {
        "schema": "solaire_prospective_journal_v1",
        "updated_at_ts": 1791711000.0,
        "entries": [
            {
                "decision_id": "decision-1", "episode_id": "episode-1", "signal_id": "signal-1",
                "execution_observation_id": "obs-1", "decision_type": "BUY_SENT",
                "decision_ts": 1791710900.0, "market": "TEST-EUR", "reason": "DELIVERED",
                "entry_eur": 10, "stop_eur": 9, "tp1_eur": 12,
                "tp2_eur": 13, "stake_eur": 100, "alert_id": "test-alert",
            },
            {
                "decision_id": "decision-2", "episode_id": "episode-2", "signal_id": "signal-2",
                "decision_type": "REJECTED", "decision_ts": 1791710950.0,
                "market": "OTHER-EUR", "reason": "SPREAD_TOO_WIDE",
            },
        ],
    }


def model_fill(fid, side, qty, price, fee, ts, market="TEST-EUR"):
    return {
        "record_type": "FILL_CONFIRMED", "execution_kind": "MODEL_FILL",
        "fill_id": fid, "market": market, "side": side,
        "quantity": qty, "price_eur": price, "fee_eur": fee, "fill_ts_utc": ts,
    }


class MachineEventTests(unittest.TestCase):
    def test_valid_alerts_remain_unknown_outcomes(self):
        x = build_machine_event_ledger(machine_fixture(), "a" * 64)
        self.assertEqual(x["counts_by_machine_action"], {"BUY_SENT": 1, "REJECTED": 1})
        self.assertEqual(x["buy_sent_structurally_valid_plan_count"], 1)
        self.assertEqual(x["actual_exchange_fills_verified"], 0)
        self.assertIsNone(x["actual_net_pnl_eur"])
        self.assertIsNone(x["records"][0]["entry_fill_eur"])
        self.assertFalse(x["records"][0]["can_claim_executable_pnl"])
        self.assertEqual(x["records"][1]["decision_type"], "REJECTED")

    def test_duplicate_decisions_rejected(self):
        fixture = machine_fixture()
        fixture["entries"].append(copy.deepcopy(fixture["entries"][0]))
        with self.assertRaisesRegex(EventLedgerError, "duplicate"):
            build_machine_event_ledger(fixture, "a" * 64)

    def test_future_entry_rejected(self):
        fixture = machine_fixture()
        fixture["entries"][0]["decision_ts"] = fixture["updated_at_ts"] + 100
        with self.assertRaisesRegex(EventLedgerError, "future"):
            build_machine_event_ledger(fixture, "a" * 64)

    def test_illogical_plan_is_not_counted_as_trade(self):
        fixture = machine_fixture()
        fixture["entries"][0]["stop_eur"] = 11
        result = build_machine_event_ledger(fixture, "a" * 64)
        self.assertEqual(result["buy_sent_invalid_or_incomplete_plan_count"], 1)
        self.assertFalse(result["records"][0]["machine_plan"]["structural_plan_valid"])

    def test_rejected_machine_gate_not_human_decision(self):
        row = build_machine_event_ledger(machine_fixture(), "b" * 64)["records"][1]
        self.assertEqual(row["source_type"], "PUBLIC_MACHINE_JOURNAL_ONLY")
        self.assertIsNone(row["net_trade_pnl_eur"])


class CashLedgerTests(unittest.TestCase):
    def test_no_fills_is_not_pnl_proof(self):
        r = calculate_cash_ledger([], {}, ASOF)
        self.assertEqual(r["cash_eur"], 2300.0)
        self.assertEqual(r["evidence_class"], "NO_FILLS")
        self.assertFalse(r["real_executable_pnl_proven"])

    def test_explicit_model_fills_cash_and_cost_basis_reconcile(self):
        data = [
            model_fill("one", "BUY", "2", "100", "1", "2026-10-11T12:00:00Z"),
            model_fill("two", "SELL", "1", "110", "1", "2026-10-11T12:05:00Z"),
        ]
        marks = {"TEST-EUR": {"price_eur": 115, "asof_utc": "2026-10-11T12:09:00Z"}}
        r = calculate_cash_ledger(data, marks, ASOF)
        self.assertEqual(r["cash_eur"], 2208.0)
        self.assertEqual(r["realized_pnl_eur"], 8.5)
        self.assertEqual(r["equity_eur"], 2323.0)
        self.assertEqual(r["total_pnl_eur"], 23.0)
        self.assertFalse(r["real_executable_pnl_proven"])
        self.assertEqual(r["model_fill_count"], 2)

    def test_same_capital_cannot_fund_simultaneous_buys(self):
        data = [
            model_fill("a", "BUY", 15, 100, 0, "2026-10-11T12:00:00Z"),
            model_fill("b", "BUY", 10, 100, 0, "2026-10-11T12:01:00Z"),
        ]
        with self.assertRaisesRegex(LedgerError, "insufficient cash"):
            calculate_cash_ledger(data, {}, ASOF)

    def test_sell_before_buy_cannot_go_short(self):
        with self.assertRaisesRegex(LedgerError, "short sale"):
            calculate_cash_ledger([model_fill("x", "SELL", 1, 120, 0, "2026-10-11T12:00:00Z")], {}, ASOF)

    def test_public_buy_sent_rejected_as_fill(self):
        x = model_fill("x", "BUY", 1, 50, 0, "2026-10-11T12:00:00Z")
        x["record_type"] = "BUY_SENT"
        with self.assertRaisesRegex(LedgerError, "never fills"):
            calculate_cash_ledger([x], {}, ASOF)

    def test_stale_mark_keeps_equity_unknown(self):
        data = [model_fill("x", "BUY", 1, 100, 1, "2026-10-11T12:00:00Z")]
        marks = {"TEST-EUR": {"price_eur": 150, "asof_utc": "2026-10-11T12:01:00Z"}}
        r = calculate_cash_ledger(data, marks, ASOF, max_mark_age_seconds=60)
        self.assertIsNone(r["equity_eur"])
        self.assertIsNone(r["total_pnl_eur"])
        self.assertEqual(r["marks_missing_or_stale"], ["TEST-EUR"])

    def test_future_mark_keeps_equity_unknown(self):
        data = [model_fill("x", "BUY", 1, 100, 1, "2026-10-11T12:00:00Z")]
        marks = {"TEST-EUR": {"price_eur": 150, "asof_utc": "2026-10-11T12:11:00Z"}}
        self.assertIsNone(calculate_cash_ledger(data, marks, ASOF)["equity_eur"])

    def test_no_fee_data_fails_closed(self):
        x = model_fill("x", "BUY", 1, 100, 1, "2026-10-11T12:00:00Z")
        del x["fee_eur"]
        with self.assertRaises(LedgerError):
            calculate_cash_ledger([x], {}, ASOF)

    def test_future_fill_fails_closed(self):
        with self.assertRaisesRegex(LedgerError, "future fill"):
            calculate_cash_ledger([model_fill("x", "BUY", 1, 50, 0, "2026-10-11T12:11:00Z")], {}, ASOF)

    def test_attested_fill_requires_provenance_and_remains_unverified(self):
        x = model_fill("x", "BUY", 1, 100, 1, "2026-10-11T12:00:00Z")
        x["execution_kind"] = "OPERATOR_ATTESTED_FILL"
        with self.assertRaisesRegex(LedgerError, "proof reference"):
            calculate_cash_ledger([x], {}, ASOF)
        x["proof_ref"] = "private:example"
        y = calculate_cash_ledger([x], {}, ASOF)
        self.assertEqual(y["evidence_class"], "OPERATOR_ATTESTED_NOT_INDEPENDENTLY_VERIFIED")
        self.assertFalse(y["real_executable_pnl_proven"])

    def test_duplicate_fill_ids_fail(self):
        x = model_fill("x", "BUY", 1, 100, 0, "2026-10-11T12:00:00Z")
        with self.assertRaisesRegex(LedgerError, "duplicate fill_id"):
            calculate_cash_ledger([x, x], {}, ASOF)

    def test_negative_cost_fails(self):
        x = model_fill("x", "BUY", 1, 100, -1, "2026-10-11T12:00:00Z")
        with self.assertRaisesRegex(LedgerError, "invalid"):
            calculate_cash_ledger([x], {}, ASOF)


if __name__ == "__main__":
    unittest.main()
