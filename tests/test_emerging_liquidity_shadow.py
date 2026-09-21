from pathlib import Path
def test_emerging_liquidity_shadow_is_measurement_only():
    x=Path("scripts/update_emerging_liquidity_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "ONLY_24H_VOLUME_GATE_BLOCKS" in x
    assert "bid_depth_1pct_eur" in x and "ask_depth_1pct_eur" in x
    assert "quote_turnover_1h_eur" in x
    assert "conservative" in x and "exploratory" in x
