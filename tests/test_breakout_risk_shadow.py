from pathlib import Path

def test_breakout_risk_shadow_is_measurement_only():
    x=Path("scripts/update_breakout_risk_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "CURRENT_15M_PLAN_ALREADY_VALID" in x
    assert "FAST_5M_PLAN_VALID" in x
    assert 'describe(closed_candles(r5,"5m",now),"5m")' in x
    assert "stop_touched" in x and "tp1_touched" in x
