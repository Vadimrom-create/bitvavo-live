from pathlib import Path

def test_execution_clean_confirmation_audit_is_research_only():
    x=Path("scripts/audit_solaire_execution_clean_confirmation.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "FAST_COMPOSITE_ONLY" in x
    assert "MULTI_TIMEFRAME" in x
    assert "evidence_3" in x
    assert "clean_mfe_ge5_mae_gt_minus5" in x
