import unittest

from research.solaire_v3 import (
    build_asset_aliases,
    build_narrative_rotations,
    early_quant_evidence,
    evaluate_candles_strict,
    match_news_assets,
    structured_news_symbols,
    walk_asks,
)


class SolaireV3Tests(unittest.TestCase):
    def test_dynamic_news_aliases_cover_complete_universe_and_hype(self):
        universe = [
            {"market": "HYPE-EUR"},
            {"market": "BTC-EUR"},
            {"market": "MOVE-EUR"},
        ]
        assets = [
            {"symbol": "HYPE", "name": "Hyperliquid"},
            {"symbol": "BTC", "name": "Bitcoin"},
            {"symbol": "MOVE", "name": "Movement"},
        ]
        aliases = build_asset_aliases(universe, assets)
        self.assertEqual(set(aliases), {"HYPE", "BTC", "MOVE"})
        self.assertIn("Hyperliquid", aliases["HYPE"])
        hits = match_news_assets(
            "Binance Will List Hyperliquid (HYPE) with Seed Tag Applied",
            aliases,
            {"MOVE"},
        )
        self.assertIn("HYPE", hits)
        self.assertNotIn("MOVE", match_news_assets("markets move higher", aliases, {"MOVE"}))

    def test_structured_provider_symbols_are_limited_to_bitvavo_universe(self):
        hits = structured_news_symbols("HYPE|BTC|NOTLISTED", {"HYPE", "BTC", "ETH"})
        self.assertEqual(hits, ["BTC", "HYPE"])

    def test_narrative_rotation_ai(self):
        rows = []
        members = ["AIOZ", "PHA", "AKT", "NOS"]
        for i, symbol in enumerate(members):
            rows.append({
                "market": symbol + "-EUR",
                "features": {"15m": {"return_4bar_pct": 2.0 + i, "return_16bar_pct": 5.0 + i}},
            })
        for symbol in ["BTC", "ETH", "XRP", "ADA"]:
            rows.append({
                "market": symbol + "-EUR",
                "features": {"15m": {"return_4bar_pct": 0.1, "return_16bar_pct": 0.2}},
            })
        result = build_narrative_rotations(rows)
        self.assertIn("AI_COMPUTE", result)
        self.assertTrue(result["AI_COMPUTE"]["active_watch"])

    def test_early_quant_can_be_ready_before_v2_confirmation(self):
        row = {
            "features": {"5m": {
                "valid": True,
                "return_4bar_pct": 1.2,
                "momentum_acceleration_pp": 0.5,
                "relative_volume": 2.0,
                "volume_4_vs_prev4": 1.7,
                "distance_to_breakout_pct": -0.2,
            }},
            "context": {"relative_strength_1h_pp": 1.0},
        }
        ev = early_quant_evidence(row)
        self.assertTrue(ev["ready"])
        self.assertGreaterEqual(ev["evidence_count"], 3)

    def test_book_walk_uses_multiple_levels(self):
        book = {"asks": [["10", "5"], ["10.1", "10"]]}
        result = walk_asks(book, 100)
        self.assertTrue(result["valid"])
        self.assertEqual(result["levels_used"], 2)
        self.assertGreater(result["vwap_eur"], 10)

    def test_strict_evaluator_sorts_and_requires_full_coverage(self):
        decision = 0
        # Avoid zero timestamp guard.
        decision = 60
        interval = 300000
        first = ((decision * 1000 // interval) + 1) * interval
        bars = []
        for i in range(11):
            t = first + i * interval
            bars.append({"t": t, "h": 105, "l": 99, "c": 102})
        result = evaluate_candles_strict(100, decision, list(reversed(bars)), 1, interval_ms=interval)
        self.assertTrue(result["complete_horizon"])
        self.assertEqual(result["bars_used"], 11)

    def test_trailing_bar_alone_is_not_complete(self):
        decision = 60
        interval = 300000
        first = ((decision * 1000 // interval) + 1) * interval
        last = first + 10 * interval
        result = evaluate_candles_strict(
            100, decision, [{"t": last, "h": 101, "l": 99, "c": 100}], 1, interval_ms=interval
        )
        self.assertFalse(result["complete_horizon"])


if __name__ == "__main__":
    unittest.main()
