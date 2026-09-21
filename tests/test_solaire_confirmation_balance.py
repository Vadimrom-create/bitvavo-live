from pathlib import Path

def test_confirmation_balance_audit_is_research_only():
    x=Path("scripts/audit_solaire_confirmation_balance.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "C15_FLOORS=(0.0,0.5,1.0,1.5,2.0,3.0)" in x
    assert "confirmed_c15_1_0" in x
    assert "hq_c15_1_0" in x
    assert "current_confirmed_confirmation15_split" in x
