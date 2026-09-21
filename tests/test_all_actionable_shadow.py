from pathlib import Path

def test_all_actionable_shadow_is_measurement_only():
    x=Path("scripts/update_all_actionable_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "select_events(payload,state,now,limit=None)" in x
    assert "actionable_after_prior_thesis_count" in x
    assert "simultaneous_actionable" in x
    assert "mark_sent" not in x
    assert "send_email" not in x
