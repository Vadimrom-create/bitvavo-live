import unittest

from scripts.solaire_memory_entry_challenger import _current_score_map


class MemoryEntryChallengerComparatorTests(unittest.TestCase):
    def test_current_score_map_refreshes_unqualified_positions_too(self):
        current = [
            {"market": "PTB-EUR", "economic_score": 0.0, "selectable": False},
            {"market": "AAA-EUR", "economic_score": 6.2, "selectable": True},
        ]
        extra = [
            {"market": "BBB-EUR", "economic_score": 7.1},
        ]
        scores = _current_score_map(current, extra)
        self.assertEqual(scores["PTB-EUR"], 0.0)
        self.assertEqual(scores["AAA-EUR"], 6.2)
        self.assertEqual(scores["BBB-EUR"], 7.1)

    def test_incremental_challenger_score_can_raise_same_market_only(self):
        current = [{"market": "AAA-EUR", "economic_score": 5.5}]
        extra = [{"market": "AAA-EUR", "economic_score": 6.4}]
        scores = _current_score_map(current, extra)
        self.assertEqual(scores["AAA-EUR"], 6.4)


if __name__ == "__main__":
    unittest.main()
