import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_winners_false_negatives",
    ROOT / "scripts" / "audit_winners_false_negatives.py",
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MOD)


def test_primary_cause_prefers_delivered_buy_over_rejections():
    row = {
        "first_buy_sent": {"outcome": "BUY_SENT"},
        "first_confirmed": {"price_eur": 1.0},
        "first_building": {"price_eur": 0.9},
        "gate_events": [
            {"outcome": "REJECTED", "reason": "SPREAD_TOO_WIDE"},
            {"outcome": "BUY_SENT", "reason": "DELIVERED"},
        ],
    }
    assert MOD._primary_cause(row) == "CAPTURED_BUY"


def test_primary_cause_attributes_first_gate_when_no_buy():
    row = {
        "first_buy_sent": None,
        "first_confirmed": {"price_eur": 1.0},
        "first_building": {"price_eur": 0.9},
        "gate_events": [
            {"outcome": "REJECTED", "reason": "STRUCTURAL_STOP_TOO_WIDE"},
            {"outcome": "REJECTED", "reason": "SPREAD_TOO_WIDE"},
        ],
    }
    assert MOD._primary_cause(row) == "GATE_STRUCTURAL_STOP_TOO_WIDE"


def test_primary_cause_distinguishes_detector_stages():
    assert MOD._primary_cause({
        "first_buy_sent": None,
        "first_confirmed": None,
        "first_building": {"price_eur": 1.0},
        "gate_events": [],
    }) == "BUILDING_NEVER_CONFIRMED"
    assert MOD._primary_cause({
        "first_buy_sent": None,
        "first_confirmed": None,
        "first_building": None,
        "gate_events": [],
    }) == "DETECTOR_NEVER_BUILDING"


def test_extract_gate_supports_multi_delivery_and_rejection():
    status = {
        "checked_at_utc": "2026-10-05T20:00:00+00:00",
        "email": "DELIVERY_COMPLETED",
        "deliveries": [
            {"market": "AAA-EUR", "entry_eur": 1.01, "stop_eur": 0.95},
        ],
        "rejections": [
            {"market": "BBB-EUR", "reason": "SPREAD_TOO_WIDE"},
        ],
    }
    a = MOD._extract_gate(status, "AAA-EUR")
    b = MOD._extract_gate(status, "BBB-EUR")
    assert len(a) == 1 and a[0]["outcome"] == "BUY_SENT"
    assert a[0]["entry_eur"] == 1.01
    assert len(b) == 1 and b[0]["reason"] == "SPREAD_TOO_WIDE"


def test_forward_metrics_use_future_bars_only():
    rows = [
        {"ts": 1000, "high": 10.0, "low": 9.0, "close": 9.5},
        {"ts": 1300, "high": 11.0, "low": 9.8, "close": 10.5},
        {"ts": 1600, "high": 12.0, "low": 10.0, "close": 11.5},
    ]
    out = MOD._forward(rows, 1200, 10.0, 1, 5000)
    assert out["bars"] == 2
    assert out["mfe_pct"] == 20.0
    assert out["mae_pct"] == -2.0


def test_consumed_share_is_descriptive_not_boolean_veto():
    share = MOD._consumed_share(100.0, 110.0, 120.0)
    assert round(share, 6) == 50.0


def test_confirmed_before_building_does_not_create_fake_first_building():
    building = confirmed = first = None
    confirmed_event = {"price_eur": 1.0, "state": "CONFIRMED_ACCELERATION"}
    building, confirmed, first = MOD._advance_acceleration_milestones(
        building, confirmed, first, "CONFIRMED_ACCELERATION", confirmed_event
    )
    assert confirmed is confirmed_event
    assert first is confirmed_event
    assert building is None

    later_building = {"price_eur": 0.98, "state": "BUILDING_ACCELERATION"}
    building, confirmed, first = MOD._advance_acceleration_milestones(
        building, confirmed, first, "BUILDING_ACCELERATION", later_building
    )
    assert building is None
    assert confirmed is confirmed_event
    assert first is confirmed_event


def test_building_before_confirmed_preserves_true_order():
    building = confirmed = first = None
    building_event = {"price_eur": 0.9, "state": "BUILDING_ACCELERATION"}
    building, confirmed, first = MOD._advance_acceleration_milestones(
        building, confirmed, first, "BUILDING_ACCELERATION", building_event
    )
    assert building is building_event
    assert first is building_event
    assert confirmed is None

    confirmed_event = {"price_eur": 1.0, "state": "CONFIRMED_ACCELERATION"}
    building, confirmed, first = MOD._advance_acceleration_milestones(
        building, confirmed, first, "CONFIRMED_ACCELERATION", confirmed_event
    )
    assert building is building_event
    assert confirmed is confirmed_event
    assert first is building_event


def test_late_entry_diagnostic_flags_buy_after_rejection_with_price_premium():
    row = {
        "market": "ORCA-EUR",
        "first_confirmed": {"price_eur": 1.86261},
        "first_buy_sent": {
            "ts": 2000.0,
            "at_utc": "2026-10-05T22:15:00+00:00",
            "entry_eur": 2.07231,
            "outcome": "BUY_SENT",
        },
        "gate_events": [
            {
                "ts": 1000.0,
                "at_utc": "2026-10-05T18:33:00+00:00",
                "outcome": "REJECTED",
                "reason": "STRUCTURAL_RANGE_TOO_NARROW",
                "scan_price_eur": 1.86261,
            },
            {
                "ts": 2000.0,
                "at_utc": "2026-10-05T22:15:00+00:00",
                "outcome": "BUY_SENT",
                "reason": "DELIVERED",
                "entry_eur": 2.07231,
            },
        ],
    }
    out = MOD._late_entry_diagnostic(row)
    assert out is not None
    assert out["late_entry_flag"] is True
    assert round(out["buy_premium_vs_first_rejection_pct"], 2) == 11.26
    assert round(out["buy_premium_vs_first_confirmed_pct"], 2) == 11.26


def test_late_entry_diagnostic_ignores_buy_without_prior_rejection():
    row = {
        "market": "FIL-EUR",
        "first_confirmed": {"price_eur": 1.0},
        "first_buy_sent": {"ts": 1000.0, "entry_eur": 1.01, "outcome": "BUY_SENT"},
        "gate_events": [{"ts": 1000.0, "outcome": "BUY_SENT", "reason": "DELIVERED"}],
    }
    assert MOD._late_entry_diagnostic(row) is None
