from pathlib import Path

def test_range_threshold_sweep_is_research_only():
    x=Path("scripts/audit_solaire_range_threshold_sweep.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "THRESHOLDS=(4.0,4.5,5.0,5.25,5.5,5.75,6.0)" in x
    assert "STRUCTURAL_RANGE_TOO_NARROW" in x
    assert "clean_mfe_ge5_mae_gt_minus5" in x
