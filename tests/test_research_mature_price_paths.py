"""Synthetic only, no HTTP calls: strict 24/48/72h historical candle-path checks."""
import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
P = ROOT / "scripts" / "research_mature_price_paths.py"
SPEC = importlib.util.spec_from_file_location("research_mature_price_paths", P)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

BASE = datetime(2026, 10, 7, 0, 2, tzinfo=timezone.utc).timestamp()
ASOF = BASE + 74 * 3600


def row(key="s1", stamp=BASE, entry=1.0):
    return {
        "decision_id": key, "market": "TEST-EUR", "decision_type": "BUY_SENT",
        "decision_ts": stamp, "signal_id": "signal-" + key,
        "entry_eur": entry, "stop_eur": 0.9 * entry, "tp1_eur": 1.1 * entry,
    }


def source(*data):
    return {"schema": "solaire_prospective_journal_v1", "entries": list(data)}


class FakePublicClient:
    def __init__(self, *, all_bars=True, fail=False):
        self.calls = []
        self.all_bars = all_bars
        self.fail = fail

    def get(self, path, params, cache=False):
        self.calls.append((path, params, cache))
        if self.fail:
            raise RuntimeError("fixture network failure")
        times = range(params["start"], params["end"], mod.FIVE_MIN_MS)
        data = [[t, "1", "1.03", "0.98", "1.02", "100"] for t in times]
        return data if self.all_bars else data[:-1]


class MaturePricePathTests(unittest.TestCase):
    def test_strict_24h_price_path_is_not_executable_profit(self):
        client = FakePublicClient()
        item = {**row(), "horizon_hours": 24}
        r = mod.inspect_one(item, client, ASOF, observed_at=ASOF)
        self.assertEqual(r["status"], "COMPLETE")
        self.assertTrue(r["strict_complete"])
        self.assertAlmostEqual(r["reference_close_return_pct"], 2.0, places=2)
        self.assertIsNone(r["net_pnl_eur"])
        self.assertFalse(r["actual_fill_proven"])
        self.assertFalse(r["future_exit_executable_proven"])
        self.assertFalse(r["chatgpt_decision_joined"])
        self.assertEqual(r["indicative_reported_zero_trade_intervals"], 0)
        self.assertEqual(client.calls[0][1]["interval"], "5m")
        self.assertLessEqual(client.calls[0][1]["end"], int(ASOF * 1000))

    def test_missing_candle_blocks_close_performance(self):
        res = mod.inspect_one({**row(), "horizon_hours": 24},
                              FakePublicClient(all_bars=False), ASOF, observed_at=ASOF)
        self.assertEqual(res["status"], "INCOMPLETE")
        self.assertFalse(res["strict_complete"])
        self.assertIsNone(res["reference_close_return_pct"])
        self.assertIsNone(res["path_result"])
        self.assertIsNone(res["net_pnl_eur"])
        # Bitvavo zero-trade gaps may admit a separate, NON-executable mark.
        self.assertTrue(res["indicative_no_trade_gap_mark_available"])
        self.assertAlmostEqual(res["indicative_close_return_pct"], 2.0, places=2)
        self.assertGreater(res["indicative_reported_zero_trade_intervals"], 0)
        self.assertFalse(res["actual_fill_proven"])

    def test_48h_and_72h_supported_with_bounded_candles(self):
        client = FakePublicClient()
        for h in (48, 72):
            r = mod.inspect_one({**row(), "horizon_hours": h}, client, ASOF,
                                observed_at=ASOF)
            self.assertEqual(r["status"], "COMPLETE")
            self.assertGreater(r["expected_bars"], 400)
            self.assertLess(r["expected_bars"], 1440)

    def test_future_and_unmatured_events_not_selected(self):
        fresh = row("fresh", ASOF - 12 * 3600)
        old = row("old", ASOF - 80 * 3600)
        chosen = mod.choose_due(mod.validate_source(source(fresh, old), ASOF), ASOF, 5)
        self.assertEqual(len(chosen), 3)
        self.assertTrue(all(c["decision_id"] == "old" for c in chosen))
        self.assertEqual({c["horizon_hours"] for c in chosen}, {24, 48, 72})

    def test_prioritizes_most_recent_matured_not_winning_price(self):
        one = row("older", ASOF - 90 * 3600)
        two = row("newer", ASOF - 80 * 3600)
        d = mod.choose_due(mod.validate_source(source(one, two), ASOF), ASOF, 1)
        self.assertEqual(len(d), 3)
        self.assertTrue(all(e["decision_id"] == "newer" for e in d))

    def test_one_market_per_horizon_prevents_correlated_repeat_cohort(self):
        latest = row("s-latest", ASOF - 80 * 3600)
        duplicate = row("s-older", ASOF - 81 * 3600)
        distinct = row("distinct", ASOF - 82 * 3600)
        distinct["market"] = "OTHER-EUR"
        selected = mod.choose_due(
            mod.validate_source(source(latest, duplicate, distinct), ASOF),
            ASOF, 2,
        )
        for horizon in (24, 48, 72):
            markets = [r["market"] for r in selected if r["horizon_hours"] == horizon]
            self.assertEqual(markets, ["TEST-EUR", "OTHER-EUR"])

    def test_public_api_error_yields_unknown_not_loss(self):
        r = mod.inspect_one({**row(), "horizon_hours": 24},
                            FakePublicClient(fail=True), ASOF, observed_at=ASOF)
        self.assertEqual(r["status"], "SOURCE_ERROR")
        self.assertIsNone(r.get("indicative_close_return_pct"))
        self.assertIsNone(r["reference_close_return_pct"])
        self.assertIsNone(r["net_pnl_eur"])

    def test_inspect_horizon_counts_and_no_fills(self):
        client = FakePublicClient()
        r = mod.inspect(source(row()), ASOF, client, 1)
        for h in ("24", "48", "72"):
            self.assertEqual(r["horizons"][h]["strict_complete"], 1)
            self.assertEqual(r["horizons"][h]["executed_trades_proven"], 0)
        self.assertEqual(len(r["observations"]), 3)
        self.assertFalse(r["orders_sent"])
        self.assertFalse(r["affects_production"])

    def test_no_lookahead_in_time_bounds(self):
        with self.assertRaises(ValueError):
            mod.bounds(BASE, 72, BASE + 24 * 3600)
        with self.assertRaises(ValueError):
            mod.bounds(BASE, 72, BASE)

    def test_source_deduplicates_by_decision_id(self):
        a = mod.validate_source(source(row(), row(), row("two", ASOF + 1),
                                       row("invalid", BASE, entry=-5),
                                       {"decision_type": "REJECTED"}), ASOF)
        self.assertEqual(len(a), 1)

    def test_rejects_bad_journal(self):
        with self.assertRaises(ValueError):
            mod.validate_source({"schema": "bad", "entries": []}, ASOF)


if __name__ == "__main__":
    unittest.main()
