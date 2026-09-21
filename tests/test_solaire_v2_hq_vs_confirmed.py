from pathlib import Path
def test_paired_audit_is_research_only():
    x=Path("scripts/audit_solaire_v2_hq_vs_confirmed.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "high_quality_building" in x
    assert "current_confirmed" in x
    assert "paired_deltas" in x
