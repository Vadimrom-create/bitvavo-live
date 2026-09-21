from pathlib import Path

def test_icx_timeline_is_research_only_and_uses_validated_quotes():
    x=Path("scripts/audit_icx_executability_timeline.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "live_quotes.json" in x
    assert "production_alert_candidates.json" in x
    assert "MAX_QUOTE_DELTA_SEC=180" in x
    assert "structural_plan_signal_price" in x
    assert "execution_clean_but_not_confirmed" in x
    assert "fully_actionable_proxy" in x
    assert "ICX-EUR" in x
