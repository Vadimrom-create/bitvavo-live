import unittest

from scripts.live_quotes import build_snapshot


class FakeClient:
    def __init__(self, *, offset=0.0, price=None, book=None, retrieved="2026-09-12T07:15:00+00:00"):
        self.server_offset = offset
        self.price = price or [{"market": "ETHFI-EUR", "price": "0.57"}]
        self.book = book or [{"market": "ETHFI-EUR", "bid": "0.569", "ask": "0.571"}]
        self.retrieved = retrieved

    def get(self, path, params=None, cache=True):
        if path == "/time":
            return {"time": 1789197300000}
        if path == "/ticker/price":
            return self.price
        if path == "/ticker/book":
            return self.book
        raise AssertionError(path)

    def metadata(self, path, params=None):
        if path in {"/ticker/price", "/ticker/book"}:
            return {"retrieved_at_utc": self.retrieved}
        return {}


class LiveQuotesTests(unittest.TestCase):
    def test_valid_ethfi_quote(self):
        times = iter([100.0, 101.0, 101.2, 101.3, 101.3])
        snap = build_snapshot(FakeClient(), now_fn=lambda: next(times))
        self.assertTrue(snap["valid"])
        row = snap["markets"]["ETHFI-EUR"]
        self.assertEqual(row["last"], 0.57)
        self.assertEqual(row["best_bid"], 0.569)
        self.assertEqual(row["best_ask"], 0.571)
        self.assertTrue(row["valid"])

    def test_exchange_clock_skew_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "EXCHANGE_CLOCK_SKEW"):
            build_snapshot(FakeClient(offset=31.0), now_fn=lambda: 100.0)

    def test_crossed_book_is_not_valid_market_quote(self):
        times = iter([100.0, 101.0, 101.1, 101.2, 101.2])
        client = FakeClient(book=[{"market": "ETHFI-EUR", "bid": "0.572", "ask": "0.571"}])
        snap = build_snapshot(client, now_fn=lambda: next(times))
        self.assertFalse(snap["markets"]["ETHFI-EUR"]["valid"])


if __name__ == "__main__":
    unittest.main()
