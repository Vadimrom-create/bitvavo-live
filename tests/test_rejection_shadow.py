from pathlib import Path
def test_rejection_shadow_v3_is_measurement_only():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "LATER_QUALIFYING_ENTRY" in x
    assert "original_condition_resolved" in x
    assert "MAX_AGE=24*3600" in x
    assert "HORIZONS=(1,4,12,24)" in x
    assert "mfe_pct" in x and "mae_pct" in x
    assert "evaluated_horizons" in x
