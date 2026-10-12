from pathlib import Path

def test_emerging_liquidity_shadow_is_measurement_only():
    x=Path("scripts/update_emerging_liquidity_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "ONLY_24H_VOLUME_GATE_BLOCKS" in x
    assert "bid_depth_1pct_eur" in x and "ask_depth_1pct_eur" in x
    assert "quote_turnover_1h_eur" in x
    assert "BOOK_STAKES_EUR=(100.0,125.0,150.0,250.0)" in x
    assert "_buy_impact" in x
    assert "_sell_impact" in x
    assert "roundtrip_cost_pct" in x
    assert "direct_exec_pass" in x
    assert "TURNOVER_MULTIPLE_MIN=50.0" in x
    assert "reason_counts" in x and "inspections" in x

def test_emerging_liquidity_stake_costs_include_fees_and_stress():
    from scripts.update_emerging_liquidity_shadow import _book_metrics
    book={"asks":[["1.01","10000"]],"bids":[["0.99","10000"]]}
    buys,sells,costs,passes=_book_metrics(book,100_000.0)
    assert set(costs)=={"100","125","150","250"}
    assert all(buys[k]["fillable"] and sells[k]["fillable"] for k in costs)
    assert all(passes.values())
    for k in costs:
        raw=costs[k]["roundtrip_cost_pct"]
        with_fees=costs[k]["roundtrip_after_fees_pct_est"]
        stressed=costs[k]["roundtrip_stressed_pct_est"]
        assert 1.9 < raw < 2.1
        assert raw < with_fees < stressed
        assert stressed-with_fees > 0.19


def test_emerging_liquidity_unfillable_book_not_misreported_as_profit():
    from scripts.update_emerging_liquidity_shadow import _book_metrics
    book={"asks":[["1.01","10"]],"bids":[["0.99","10"]]}
    _,_,costs,passes=_book_metrics(book,100_000.0)
    assert all(not x for x in passes.values())
    assert all(x["roundtrip_after_fees_pct_est"] is None for x in costs.values())
    assert all(x["roundtrip_stressed_pct_est"] is None for x in costs.values())
