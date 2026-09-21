from pathlib import Path
def test_v21_range5_shadow_is_measurement_only():
    x=Path("scripts/update_v21_range5_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "CURRENT_RANGE=6.0" in x
    assert "CANDIDATE_RANGE=5.0" in x
    assert "candidate5_only_pass" in x
    assert "structural_plan" in x
    assert "MAX_STOP_DISTANCE_PCT" in x
