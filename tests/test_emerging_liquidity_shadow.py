from pathlib import Path

def test_emerging_liquidity_shadow_is_measurement_only():
    x=Path("scripts/update_emerging_liquidity_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "ONLY_24H_VOLUME_GATE_BLOCKS" in x
    assert "bid_depth_1pct_eur" in x and "ask_depth_1pct_eur" in x
    assert "quote_turnover_1h_eur" in x
    assert "BOOK_STAKES_EUR=(100.0,250.0)" in x
    assert "_buy_impact" in x
    assert "_sell_impact" in x
    assert "roundtrip_cost_pct" in x
    assert "direct_exec_pass" in x
    assert "TURNOVER_MULTIPLE_MIN=50.0" in x
    assert "reason_counts" in x and "inspections" in x
