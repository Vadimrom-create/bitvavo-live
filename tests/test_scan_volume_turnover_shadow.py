"""Regression tests for causal volume-turnover SHADOW only."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_volume_turnover_shadow.py"
SPEC = importlib.util.spec_from_file_location("scan_volume_turnover_shadow", SCRIPT)
shadow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(shadow)


def live():
    return {
        "generated_at_utc": "2026-10-08T21:45:00Z",
        "markets": [
            {"market": "OGN-EUR", "last": 0.044,
             "quote_volume_24h_eur": 4_000_000, "spread_pct": 0.42,
             "m15": {"volume_last_vs_prev20": 0.34,
                     "volume_4_vs_prev4": 0.90, "volume_16_vs_prev16": 1.1}},
            {"market": "RLC-EUR", "last": 0.78,
             "quote_volume_24h_eur": 6_000_000, "spread_pct": 0.14,
             "m15": {"volume_last_vs_prev20": 0.08,
                     "volume_4_vs_prev4": 0.85, "volume_16_vs_prev16": 0.85}},
        ],
    }


def cap(**kwargs):
    d = {"market": "OGN-EUR", "asset_id": "origin-protocol",
         "identity_verified": True, "market_cap_eur": 32_000_000,
         "source": "provider-with-verified-asset-id",
         "asof_utc": "2026-10-08T20:45:00Z",
         "global_volume_24h_eur": 5_000_000}
    d.update(kwargs)
    return {"rows": [d]}


class VolumeTurnoverShadowTests(unittest.TestCase):
    def test_all_markets_kept_without_marketcap(self):
        r = shadow.summarize(live())
        self.assertEqual(r["market_count"], 2)
        self.assertEqual(r["cap_coverage_pct"], 0)
        self.assertEqual(r["cap_validation_counts"]["CAP_UNAVAILABLE"], 2)
        self.assertEqual(r["observations"][0]["volume_last_1h_vs_prev_1h"], 0.9)
        self.assertIsNone(r["observations"][0]["turnover_bitvavo_24h_pct"])
        self.assertTrue(r["measurement_only"])
        self.assertFalse(r["changes_buy_gate"])

    def test_verified_asset_enables_both_turnover_denominators(self):
        r = shadow.summarize(live(), cap())
        ogn = r["observations"][0]
        self.assertEqual(ogn["turnover_bitvavo_24h_pct"], 12.5)
        self.assertEqual(ogn["turnover_global_24h_pct"], 15.625)
        self.assertEqual(ogn["cap_eur"], 32_000_000)
        self.assertEqual(r["cap_validation_counts"]["CAP_VALID"], 1)

    def test_symbol_only_mapping_is_invalid(self):
        r = shadow.summarize(live(), cap(identity_verified=False))
        self.assertEqual(r["observations"][0]["status"], "CAP_UNVERIFIED")
        self.assertIsNone(r["observations"][0]["turnover_global_24h_pct"])
        r = shadow.summarize(live(), cap(asset_id=""))
        self.assertEqual(r["observations"][0]["status"], "CAP_UNVERIFIED")

    def test_future_cap_cannot_be_used_ex_ante(self):
        r = shadow.summarize(live(), cap(asof_utc="2026-10-08T23:00:00Z"))
        self.assertEqual(r["observations"][0]["status"], "CAP_FUTURE_LOOKAHEAD")
        self.assertIsNone(r["observations"][0]["cap_eur"])

    def test_stale_marketcap_cannot_be_used(self):
        r = shadow.summarize(live(), cap(asof_utc="2026-10-06T00:00:00Z"))
        self.assertEqual(r["observations"][0]["status"], "CAP_STALE")
        self.assertIsNone(r["observations"][0]["turnover_bitvavo_24h_pct"])

    def test_duplicate_identity_refused(self):
        caps = cap()
        caps["rows"].append(dict(caps["rows"][0]))
        with self.assertRaises(shadow.BadEvidence):
            shadow.summarize(live(), caps)

    def test_missing_and_invalid_number_are_not_zero_predicted_turnover(self):
        x = live()
        x["markets"][0]["quote_volume_24h_eur"] = float("nan")
        x["markets"][1]["m15"] = {}
        r = shadow.summarize(x, cap())
        self.assertIsNone(r["observations"][0]["turnover_bitvavo_24h_pct"])
        self.assertIsNone(r["observations"][1]["volume_last_4h_vs_prev_4h"])

    def test_invalid_missing_clock_is_rejected(self):
        x = live()
        x["generated_at_utc"] = "2026-10-08T21:45:00"
        with self.assertRaises(shadow.BadEvidence):
            shadow.summarize(x)
        x = live()
        x["markets"].append(dict(x["markets"][0]))
        with self.assertRaises(shadow.BadEvidence):
            shadow.summarize(x)

    def test_cli_writes_shadow_data_not_orders(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            inp = folder / "live.json"
            capfile = folder / "caps.json"
            out = folder / "result.json"
            inp.write_text(json.dumps(live()), encoding="utf-8")
            capfile.write_text(json.dumps(cap()), encoding="utf-8")
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                exit_code = shadow.main(["--live", str(inp), "--marketcap", str(capfile), "--output", str(out)])
            self.assertEqual(exit_code, 0)
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(report["cap_coverage_pct"], 50)
            self.assertTrue(report["measurement_only"])
            self.assertNotIn("orders", report)


if __name__ == "__main__":
    unittest.main()
