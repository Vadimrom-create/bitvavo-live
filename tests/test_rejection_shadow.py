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
