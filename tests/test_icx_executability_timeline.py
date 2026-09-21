from pathlib import Path

def test_icx_timeline_is_research_only():
    x=Path("scripts/audit_icx_executability_timeline.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "bitvavo_live.json" in x
    assert "production_alert_candidates.json" in x
    assert "execution_clean_but_not_confirmed" in x
    assert "fully_actionable_proxy" in x
    assert "micro5_structural_plan_signal_price" in x
    assert "micro5_plan_and_stop_pass" in x
    assert "nearest_quote_source" in x
    assert "ICX-EUR" in x
