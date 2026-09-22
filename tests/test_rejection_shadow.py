from pathlib import Path

def test_rejection_shadow_v4_is_measurement_only_and_tracks_downgrades():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "tracking_rows" in x
    assert "first_later_execution_valid_snapshot" in x
    assert "first_later_fully_actionable_entry" in x
    assert "BUILDING_ACCELERATION" in x
    assert "HORIZONS=(1,4,12,24)" in x
    assert "mfe_pct" in x and "mae_pct" in x


def test_rejection_shadow_measures_reentry_from_execution_clean_snapshot():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "execution_valid_evaluations" in x
    assert "_evaluate_reentry" in x
    assert "closed_5m_bars_after_first_execution_valid_snapshot" in x
    assert "evaluated_reentry_horizons" in x


def test_rejection_shadow_classifies_reentry_quality():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "CONFIRMED_REENTRY" in x
    assert "BUILDING_HQ_4E" in x
    assert "BUILDING_6_3" in x
    assert "reentry_delay_seconds" in x
    assert "reentry_tier_cohorts" in x
    assert "clean_mfe_ge5_mae_gt_minus5" in x


def test_rejection_shadow_backfills_existing_reentry_metadata():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert 'if not snap.get("reentry_tier")' in x
    assert 'snap["reentry_delay_seconds"]' in x
