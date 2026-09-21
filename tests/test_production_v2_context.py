import unittest

from research.production_context import build_market_context
from research.production_gate import build_alert_payload
from research.production_journal import due_horizons, evaluate_bars, record_cycle


class ProductionContextTests(unittest.TestCase):
    def obs(self, market, r1, r4, score=7.0):
        return {
            "market": market,
            "price_eur": 1.0,
            "change_24h_pct": 2.0,
            "quote_volume_24h_eur": 200000,
            "data_quality": {"ok": True, "reasons": []},
            "features": {
                "15m": {
                    "return_4bar_pct": r1,
                    "return_16bar_pct": r4,
                }
            },
            "acceleration": {
                "state": "CONFIRMED_ACCELERATION",
                "score": score,
                "evidence_count": 4,
            },
        }

    def test_context_uses_same_scan_and_is_non_veto(self):
        observations = [
            self.obs("BTC-EUR", -1.0, -2.0),
            self.obs("ETH-EUR", -1.0, -2.0),
            self.obs("SOL-EUR", -1.0, -2.0),
            self.obs("A-EUR", 4.0, 7.0),
        ]
        context = build_market_context(observations)
        self.assertEqual(context["source"], "same_direct_bitvavo_scan")
        self.assertFalse(context["affects_detection"])
        self.assertFalse(context["affects_buy_gate"])
        payload = build_alert_payload(observations, "2026-09-21T10:00:00+00:00", context)
        self.assertEqual(len(payload["watch"]), 4)
        a = next(row for row in payload["watch"] if row["market"] == "A-EUR")
        self.assertEqual(a["context"]["mode"], "SHADOW_NON_VETO")
        self.assertFalse(a["context"]["affects_buy_gate"])

    def test_context_degrades_without_suppressing_candidate(self):
        observations = [self.obs("A-EUR", 2.0, 3.0)]
        # Add invalid observations so context completeness falls below 95%.
        observations.extend(
            {
                "market": f"X{i}-EUR",
                "price_eur": 1.0,
                "quote_volume_24h_eur": 100000,
                "data_quality": {"ok": False, "reasons": ["TEST"]},
                "features": {"15m": {}},
                "acceleration": {"state": "NONE", "score": 0, "evidence_count": 0},
            }
            for i in range(2)
        )
        context = build_market_context(observations)
        self.assertEqual(context["status"], "DEGRADED")
        payload = build_alert_payload(observations, "2026-09-21T10:00:00+00:00", context)
        self.assertEqual([row["market"] for row in payload["watch"]], ["A-EUR"])


class ProductionJournalTests(unittest.TestCase):
    def payload(self):
        return {
            "generated_at_utc": "2026-09-21T10:00:00+00:00",
            "watch": [
                {
                    "market": "A-EUR",
                    "last": 1.0,
                    "signal_score": 7.5,
                    "context": {"regime": "MIXED"},
                },
                {
                    "market": "B-EUR",
                    "last": 2.0,
                    "signal_score": 8.0,
                },
            ],
        }

    def test_record_cycle_records_actual_rejection_and_delivery(self):
        status = {
            "checked_at_utc": "2026-09-21T10:01:00+00:00",
            "rejections": [{"market": "A-EUR", "reason": "SPREAD_TOO_WIDE"}],
            "email": "DELIVERY_COMPLETED",
            "market": "B-EUR",
            "entry_eur": 2.01,
            "stop_eur": 1.90,
            "tp1_eur": 2.23,
            "tp2_eur": 2.34,
            "stake_eur": 180.0,
        }
        journal = record_cycle(self.payload(), status, {})
        self.assertEqual(len(journal["entries"]), 2)
        rejected = next(x for x in journal["entries"] if x["decision_type"] == "REJECTED")
        sent = next(x for x in journal["entries"] if x["decision_type"] == "BUY_SENT")
        self.assertEqual(rejected["reason"], "SPREAD_TOO_WIDE")
        self.assertEqual(sent["entry_eur"], 2.01)
        # Replaying the same cycle is idempotent.
        journal = record_cycle(self.payload(), status, journal)
        self.assertEqual(len(journal["entries"]), 2)

    def test_due_horizons_and_rejection_outcome(self):
        entry = {
            "decision_ts": 1_000_000.0,
            "decision_type": "REJECTED",
            "signal_price_eur": 1.0,
            "evaluations": {},
        }
        self.assertEqual(due_horizons(entry, 1_000_000.0 + 5 * 3600), [4])
        start = ((int(entry["decision_ts"] * 1000) // 300_000) + 1) * 300_000
        bars = [
            [start, 1.0, 1.06, 0.98, 1.04, 10],
            [start + 300_000, 1.04, 1.07, 1.01, 1.05, 12],
        ]
        outcome = evaluate_bars(entry, bars, 4)
        self.assertEqual(outcome["result"], "MISSED_UPSIDE_GE5")
        self.assertGreaterEqual(outcome["mfe_pct"], 5.0)

    def test_buy_outcome_is_conservative_when_stop_and_tp_touch_same_bar(self):
        entry = {
            "decision_ts": 1_000_000.0,
            "decision_type": "BUY_SENT",
            "entry_eur": 1.0,
            "stop_eur": 0.95,
            "tp1_eur": 1.05,
            "evaluations": {},
        }
        start = ((int(entry["decision_ts"] * 1000) // 300_000) + 1) * 300_000
        bars = [[start, 1.0, 1.06, 0.94, 1.0, 10]]
        outcome = evaluate_bars(entry, bars, 4)
        self.assertEqual(outcome["result"], "STOP_SAME_BAR_CONSERVATIVE")


if __name__ == "__main__":
    unittest.main()
