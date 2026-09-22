from pathlib import Path

def test_baseline_rejection_watch_is_research_only():
    x=Path("scripts/audit_solaire_baseline_rejection_watch.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "FLOCK-EUR" in x and "XVG-EUR" in x and "ICX-EUR" in x and "SAGA-EUR" in x
    assert "first_fully_actionable_proxy" in x
    assert "classification is evidence-oriented" in x
