"""Synthetic, offline regression for cash-locked 5m price-path replay."""
from __future__ import annotations

import copy
import unittest
from datetime import datetime, timedelta, timezone

from research.capital_constrained_replay import ReplayError, replay_portfolio

T0 = datetime(2026, 10, 1, tzinfo=timezone.utc)


def iso(dt):
    return dt.isoformat().replace("+00:00", "Z")


def signal(eid="one", market="AAA-EUR", stake=100, minute=1):
    return {
        "event_type": "MODEL_SIGNAL", "event_id": eid, "market": market,
        "decision_at_utc": iso(T0 + timedelta(minutes=minute)),
        "book_available_at_utc": iso(T0 + timedelta(minutes=minute, seconds=2)),
        "book_entry_covered": True, "book_exit_covered": True,
        "entry_limit_eur": 10, "stop_eur": 9, "target_eur": 12,
        "stake_eur": stake,
    }


def bar(minute, o=10, h=10.5, l=9.5, c=10):
    return {
        "start_utc": iso(T0 + timedelta(minutes=minute)),
        "open": o, "high": h, "low": l, "close": c,
    }


def replay(events, paths, **kw):
    return replay_portfolio(events, paths, iso(T0 + timedelta(days=2)), **kw)


class PortfolioReplayTests(unittest.TestCase):
    def test_one_modeled_target_exit_after_first_bar(self):
        out = replay([signal()], {"AAA-EUR": [bar(5), bar(10, h=12.5, l=9.5, c=11.5)]})
        self.assertEqual(out["status"], "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF")
        self.assertEqual(out["trade_count"], 1)
        self.assertGreater(out["modeled_portfolio_pnl_eur"], 0)
        self.assertEqual(out["trades"][0]["exit_reason"], "TARGET")
        self.assertIsNone(out["real_bitvavo_pnl_eur"])
        self.assertIsNone(out["max_drawdown_eur"])

    def test_stop_before_target_same_candle(self):
        out = replay([signal()], {"AAA-EUR": [bar(5), bar(10, h=13, l=8.5, c=10)]})
        self.assertEqual(out["trades"][0]["exit_reason"], "STOP_FIRST_CONSERVATIVE")
        self.assertLess(out["modeled_portfolio_pnl_eur"], 0)

    def test_stop_gap_uses_worse_open(self):
        out = replay([signal()], {"AAA-EUR": [bar(5), bar(10, o=8, h=13, l=7.5, c=9)]})
        self.assertEqual(out["trades"][0]["exit_reason"], "STOP_FIRST_CONSERVATIVE")
        self.assertLess(out["trades"][0]["modeled_sell_proceeds_eur"], 80)

    def test_limit_not_touched_means_no_fill(self):
        out = replay([signal()], {"AAA-EUR": [bar(5, o=10.5, h=11, l=10.25, c=10.5)]})
        self.assertEqual(out["candidate_states"], {"UNFILLED": 1})
        self.assertEqual(out["trade_count"], 0)
        self.assertEqual(out["modeled_portfolio_pnl_eur"], 0)

    def test_book_depth_missing_is_excluded_pre_trade(self):
        s = signal()
        s["book_entry_covered"] = False
        out = replay([s], {})
        self.assertEqual(out["candidate_states"], {"NOT_EXECUTABLE_BOOK": 1})
        self.assertEqual(out["trade_count"], 0)

    def test_intrabar_entry_stop_uncertainty_poison_score(self):
        out = replay([signal()], {"AAA-EUR": [bar(5, o=10, l=8.8, h=11)]})
        self.assertEqual(out["status"], "NOT_IDENTIFIABLE_INCOMPLETE_OR_EMPTY_COHORT")
        self.assertIsNone(out["modeled_portfolio_pnl_eur"])

    def test_intrabar_entry_target_uncertainty_poison_score(self):
        out = replay([signal()], {"AAA-EUR": [bar(5, o=10, l=9.5, h=12.4)]})
        self.assertEqual(out["candidate_states"], {"CENSORED": 1})
        self.assertIsNone(out["modeled_portfolio_pnl_eur"])

    def test_incomplete_path_does_not_cherry_pick_winning_trade(self):
        e = signal("win", "AAA-EUR")
        f = signal("missing", "BBB-EUR")
        out = replay(
            [e, f],
            {"AAA-EUR": [bar(5), bar(10, h=12.5)],
             "BBB-EUR": [bar(5, h=11), bar(10)]},
        )
        self.assertEqual(out["candidate_states"], {"MODELED_COMPLETED": 1, "CENSORED": 1})
        self.assertIsNone(out["modeled_portfolio_pnl_eur"])
        self.assertEqual(out["missing_or_ambiguous_event_ids"], ["missing"])

    def test_future_horizon_stays_unknown(self):
        result = replay_portfolio(
            [signal()], {"AAA-EUR": [bar(5)]},
            iso(T0 + timedelta(hours=2)),
        )
        self.assertEqual(result["candidate_states"], {"NOT_MATURED": 1})
        self.assertIsNone(result["modeled_portfolio_pnl_eur"])

    def test_missing_first_complete_post_book_bar_is_censored(self):
        out = replay([signal()], {"AAA-EUR": [bar(0), bar(10, h=12.4)]})
        self.assertEqual(out["candidate_states"], {"CENSORED": 1})

    def test_insufficient_cash_blocks_overlapping_eligible_trades(self):
        first = signal("alpha", "AAA-EUR", stake=2100)
        second = signal("beta", "BBB-EUR", stake=500)
        # No stop or target reached: both trades stay open to horizon.
        # Complete 5m grids through the end of the 24h horizon.
        full = [bar(i) for i in range(5, 24 * 60, 5)]
        result = replay([first, second], {"AAA-EUR": full, "BBB-EUR": full})
        self.assertEqual(result["trade_count"], 1)
        self.assertEqual(result["allocation_reject_count"], 1)
        self.assertEqual(result["trades"][0]["event_id"], "alpha")
        self.assertLess(result["modeled_portfolio_pnl_eur"], 0)

    def test_tie_break_is_stable_and_independent_of_profit(self):
        first = signal("alpha", "AAA-EUR", stake=2100)
        second = signal("beta", "BBB-EUR", stake=2100)
        result = replay(
            [second, first],
            {"AAA-EUR": [bar(5), bar(10, h=12.5)],
             "BBB-EUR": [bar(5), bar(10, h=12.5)]},
        )
        self.assertEqual(result["trade_count"], 1)
        self.assertEqual(result["trades"][0]["event_id"], "alpha")

    def test_duplicate_signal_fails(self):
        with self.assertRaisesRegex(ReplayError, "duplicated event ID"):
            replay([signal(), signal()], {"AAA-EUR": []})

    def test_partial_or_future_bars_rejected(self):
        with self.assertRaisesRegex(ReplayError, "partial or future candle"):
            replay_portfolio([signal()], {"AAA-EUR": [bar(5)]}, iso(T0 + timedelta(minutes=7)))

    def test_negative_fee_invalid(self):
        with self.assertRaises(ReplayError):
            replay([signal()], {"AAA-EUR": []}, fee_each_side=-0.001)

    def test_declared_horizon_only(self):
        with self.assertRaisesRegex(ReplayError, "unsupported horizon"):
            replay([signal()], {"AAA-EUR": []}, horizon_hours=4)

    def test_future_book_fails(self):
        bad = signal()
        bad["book_available_at_utc"] = iso(T0 + timedelta(days=3))
        with self.assertRaisesRegex(ReplayError, "future"):
            replay([bad], {"AAA-EUR": []})

    def test_zero_candidate_is_not_zero_profit_proof(self):
        r = replay([], {})
        self.assertEqual(r["status"], "NOT_IDENTIFIABLE_INCOMPLETE_OR_EMPTY_COHORT")
        self.assertIsNone(r["modeled_portfolio_pnl_eur"])

    def test_fee_and_slippage_reduce_model_return(self):
        bars = [bar(5), bar(10, h=12.5)]
        cheap = replay([signal()], {"AAA-EUR": bars}, fee_each_side=0, slippage_each_side=0)
        costly = replay([signal()], {"AAA-EUR": bars}, fee_each_side=0.0025, slippage_each_side=0.001)
        self.assertLess(costly["modeled_portfolio_pnl_eur"], cheap["modeled_portfolio_pnl_eur"])

    def test_proxied_no_trade_gap_allows_path_only_as_model(self):
        e = signal()
        gap = {"AAA-EUR": [bar(5), bar(15, h=12.3)]}
        strict = replay([e], gap)
        proxy = replay([e], gap, gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY")
        self.assertEqual(strict["candidate_states"], {"CENSORED": 1})
        self.assertEqual(proxy["trade_count"], 1)
        self.assertEqual(proxy["candidate_states"], {"MODELED_COMPLETED": 1})
        self.assertGreaterEqual(proxy["assumed_zero_trade_5m_intervals_n"], 1)
        self.assertIsNone(proxy["real_bitvavo_pnl_eur"])

    def test_zero_trade_first_entry_bar_is_never_filled(self):
        e = signal()
        # First real bar is at 00:00, next at 00:10. The missing 00:05
        # entry bar is a no-trade flat interval: cannot claim a trade fill.
        data = {"AAA-EUR": [bar(0), bar(10, h=12.5)]}
        proxy = replay([e], data, gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY")
        self.assertEqual(proxy["candidate_states"], {"UNFILLED": 1})
        self.assertEqual(proxy["trade_count"], 0)

    def test_long_market_staleness_not_silently_padded(self):
        e = signal()
        # A 12h+ data hole could be market inactivity, delisting or
        # incomplete provider response. Keep PnL unknown.
        data = {"AAA-EUR": [bar(5), bar(800)]}
        proxy = replay([e], data, gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY")
        self.assertEqual(proxy["candidate_states"], {"CENSORED": 1})
        self.assertIsNone(proxy["modeled_portfolio_pnl_eur"])

    def test_unknown_gap_mode_rejected(self):
        with self.assertRaisesRegex(ReplayError, "unrecognized market gap"):
            replay([signal()], {"AAA-EUR": []}, gap_mode="ASSUME_WINS")

    def test_next_real_print_exit_is_delayed_and_not_an_exchange_fill(self):
        e = signal()
        bars = [bar(i) for i in (5, 10, 700, 1390, 1460)]
        result = replay([e], {"AAA-EUR": bars},
                        gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY",
                        horizon_exit_mode="NEXT_REAL_BAR_OPEN_PROXY")
        self.assertEqual(result["status"], "MODELED_CLOSED_COHORT_ONLY_NO_EXECUTION_PROOF")
        self.assertEqual(result["trade_count"], 1)
        trade = result["trades"][0]
        self.assertEqual(trade["exit_reason"], "HORIZON_NEXT_REAL_BAR_OPEN_PROXY")
        self.assertGreater(trade["horizon_exit_delay_minutes"], 0)
        self.assertFalse(result["modeled_fills_not_real"] is False)
        self.assertIsNone(result["real_bitvavo_pnl_eur"])

    def test_no_real_trade_after_horizon_censors_whole_comparison(self):
        e = signal()
        bars = [bar(i) for i in (5, 10, 700, 1390)]
        result = replay_portfolio(
            [e], {"AAA-EUR": bars},
            iso(T0 + timedelta(hours=25)),
            gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY",
            horizon_exit_mode="NEXT_REAL_BAR_OPEN_PROXY",
        )
        self.assertEqual(result["candidate_reasons"], {"NO_REAL_TRADE_AFTER_HORIZON": 1})
        self.assertIsNone(result["modeled_portfolio_pnl_eur"])

    def test_next_print_mode_is_never_an_automatic_fix_for_missing_history(self):
        e = signal()
        result = replay([e], {"AAA-EUR": [bar(5), bar(1460)]},
                        gap_mode="BITVAVO_ZERO_TRADE_FLAT_PROXY",
                        horizon_exit_mode="NEXT_REAL_BAR_OPEN_PROXY")
        self.assertEqual(result["candidate_states"], {"CENSORED": 1})
        self.assertIsNone(result["modeled_portfolio_pnl_eur"])

    def test_invalid_exit_mode_fail_closed(self):
        with self.assertRaisesRegex(ReplayError, "unrecognized horizon exit mode"):
            replay([signal()], {"AAA-EUR": []},
                   horizon_exit_mode="OPTIMAL_FUTURE_PRICE")

    def test_no_real_fills_claimed_for_winning_model(self):
        r = replay([signal()], {"AAA-EUR": [bar(5), bar(10, h=12.5)]})
        self.assertEqual(r["actual_exchange_fills_verified"], 0)
        self.assertIsNone(r["real_bitvavo_pnl_eur"])


if __name__ == "__main__":
    unittest.main()
