from pathlib import Path

def test_regime_adaptive_range_audit_is_research_only():
    x=Path("scripts/audit_solaire_regime_adaptive_range.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "range5_broad_risk_on" in x
    assert "breadth4_ge70" in x
    assert "policy comparisons are exploratory" in x
