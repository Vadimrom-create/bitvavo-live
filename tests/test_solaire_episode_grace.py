from pathlib import Path
def test_episode_grace_audit_is_research_only():
    x=Path("scripts/audit_solaire_episode_grace.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "GRACES=(0,600,900)" in x
    assert "PRIOR_BUY_THESIS_STILL_ACTIVE" in x
