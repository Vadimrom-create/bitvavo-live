from pathlib import Path

def test_serialization_audit_is_research_only():
    x=Path("scripts/audit_solaire_alert_serialization.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "select_events" in x
    assert "serialized_after_sent_market" in x
    assert "mark_sent" in x
    assert "PRIOR_BUY_THESIS_STILL_ACTIVE" in x
