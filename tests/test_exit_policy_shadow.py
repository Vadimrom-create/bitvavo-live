from pathlib import Path

def test_exit_policy_shadow_is_measurement_only():
    x=Path("scripts/update_exit_policy_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "full_1_4r" in x and "full_1_5r" in x and "full_1_6r" in x
    assert "LOW_BEFORE_HIGH_CONSERVATIVE" in x
    assert "comparisons_vs_current" in x
