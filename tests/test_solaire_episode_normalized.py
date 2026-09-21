from pathlib import Path

def test_episode_normalized_audit_is_research_only():
    x=Path("scripts/audit_solaire_episode_normalized_outcomes.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "unique_episode_reason_decisions" in x
    assert "GRACES=(0,600,900)" in x
    assert "first_market_reason_stats" in x
