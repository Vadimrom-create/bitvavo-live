from pathlib import Path

def test_extension_risk_audit_is_research_only():
    x=Path("scripts/audit_solaire_extension_risk.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "extension_1h_atr" in x
    assert "INSUFFICIENT_EXECUTION_LIQUIDITY" in x
    assert "correlation is not causation" in x
