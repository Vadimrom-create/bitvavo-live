"""Research-only marked-equity diagnostics are never real exit liquidity."""
from __future__ import annotations
import unittest
from datetime import datetime, timedelta, timezone

from research.capital_constrained_replay import ReplayError
from research.last_print_equity_diagnostic import summarize_last_print_equity

T0 = datetime(2026, 10, 1, tzinfo=timezone.utc)


def stamp(t):
    return t.isoformat().replace("+00:00", "Z")


def fixture():
    t = {
        "event_id": "event-a", "market": "AAA-EUR",
        "modeled_opened_utc": stamp(T0 + timedelta(minutes=5)),
        "modeled_closed_utc": stamp(T0 + timedelta(minutes=15)),
        "modeled_buy_cost_eur": 100,
        "modeled_sell_proceeds_eur": 105,
        "modeled_net_pnl_eur": 5,
    }
    plans = {"event-a": {"event_id": "event-a", "market": "AAA-EUR", "entry_limit_eur": 10}}
    bars = {"AAA-EUR": [
        {"start_utc": stamp(T0), "close": 10},
        {"start_utc": stamp(T0 + timedelta(minutes=5)), "close": 10.2},
        {"start_utc": stamp(T0 + timedelta(minutes=10)), "close": 10.5},
    ]}
    return [t], plans, bars


def risk(trades, plans, bars, **kw):
    return summarize_last_print_equity(
        trades, plans, bars, stamp(T0 + timedelta(hours=1)), **kw)


class LastPriceEquityTests(unittest.TestCase):
    def test_complete_marked_series_is_not_proven_exit_drawdown(self):
        trades, plans, bars = fixture()
        r = risk(trades, plans, bars)
        self.assertEqual(r["status"], "LAST_TRADED_PRICE_PROXY_ONLY")
        self.assertAlmostEqual(r["model_final_cash_eur"], 2305)
        self.assertEqual(r["max_deployed_cash_eur_est"], 100)
        self.assertIsNone(r["real_executable_drawdown_eur"])
        self.assertFalse(r["exit_liquidation_price_confirmed"])
        self.assertIsNotNone(r["max_drawdown_last_print_eur_est"])

    def test_missing_mark_is_unknown_not_zero_drawdown(self):
        trades, plans, bars = fixture()
        bars["AAA-EUR"] = []
        r = risk(trades, plans, bars)
        self.assertEqual(r["status"], "NOT_IDENTIFIABLE_MISSING_OR_STALE_MARK")
        self.assertIsNone(r["max_drawdown_last_print_eur_est"])

    def test_duplicate_event_id_refused(self):
        trades, plans, bars = fixture()
        with self.assertRaisesRegex(ReplayError, "duplicate or missing"):
            risk(trades + trades, plans, bars)

    def test_trade_cash_flow_mismatch_refused(self):
        trades, plans, bars = fixture()
        trades[0]["modeled_net_pnl_eur"] = -12
        with self.assertRaisesRegex(ReplayError, "does not reconcile"):
            risk(trades, plans, bars)

    def test_empty_cohort_does_not_prove_zero_risk(self):
        r = risk([], {}, {})
        self.assertIsNone(r["max_drawdown_last_print_eur_est"])
        self.assertNotEqual(r["status"], "LAST_TRADED_PRICE_PROXY_ONLY")

    def test_market_mismatch_rejected(self):
        trades, plans, bars = fixture()
        plans["event-a"]["market"] = "BBB-EUR"
        with self.assertRaisesRegex(ReplayError, "market mismatch"):
            risk(trades, plans, bars)

    def test_stale_price_causes_fail_closed(self):
        trades, plans, bars = fixture()
        bars["AAA-EUR"] = bars["AAA-EUR"][:1]
        r = risk(trades, plans, bars, maximum_price_staleness_minutes=0)
        self.assertEqual(r["status"], "NOT_IDENTIFIABLE_MISSING_OR_STALE_MARK")

    def test_moving_mark_can_create_deeper_drawdown_than_closed_only(self):
        trades, plans, bars = fixture()
        bars["AAA-EUR"][1]["close"] = 8
        r = risk(trades, plans, bars)
        self.assertGreater(r["max_drawdown_last_print_eur_est"], 15)

    def test_future_mark_rejected(self):
        trades, plans, bars = fixture()
        bars["AAA-EUR"][0]["start_utc"] = stamp(T0 + timedelta(days=2))
        with self.assertRaisesRegex(ReplayError, "future"):
            risk(trades, plans, bars)


if __name__ == "__main__":
    unittest.main()
