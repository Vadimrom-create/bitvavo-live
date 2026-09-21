from pathlib import Path
def test_adversarial_replay_is_research_only():
    x=Path("scripts/audit_solaire_v2_20260921.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "STRUCTURAL_RANGE_TOO_NARROW" in x
    assert "mfe_pct" in x and "mae_pct" in x
