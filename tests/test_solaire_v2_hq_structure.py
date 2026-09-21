from pathlib import Path
def test_hq_structure_audit_is_research_only():
    x=Path("scripts/audit_solaire_v2_hq_structure.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "historical spread not reconstructed" in x
    assert "structure_gate_pass_ex_spread_liquidity" in x
    assert "high_quality_building" in x
