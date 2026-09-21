from pathlib import Path
def test_early_building_shadow_is_non_actionable():
    x=Path("scripts/update_early_building_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "BUILDING_ACCELERATION" in x
    assert "MIN_SCORE=6.0" in x
    assert "MIN_EVIDENCE=4" in x
    assert "validate(row,client,metadata" in x
    assert "hq_active" in x
    assert "evaluations" in x
    assert "confirmation" in x
    assert "stop_touched" in x and "tp1_touched" in x
