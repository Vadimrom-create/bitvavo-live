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


def test_liquidity_coverage_requires_every_fully_closed_bar():
    from scripts.update_emerging_liquidity_shadow import _eval
    # The 12th candle closes after the one-hour horizon and must be excluded.
    event={"detected_ts":3601.0,"entry_eur":1.0,"stop_eur":0.9,"tp1_eur":1.1}
    first=3900_000
    history=[(first+i*300_000,1.02,0.98,1.01) for i in range(11)]
    late_bar=(7200_000,3.0,0.10,3.0)
    result=_eval(event,history+[late_bar],1)
    assert result["coverage_status"]=="COMPLETE_STRICT"
    assert result["strict_complete"] is True
    assert result["expected_bars"]==11
    assert result["observed_unique_bars"]==11
    assert result["missing_bars"]==0
    assert result["bars"]==11
    assert result["strict_mfe_pct"]==2.0
    assert result["strict_mae_pct"]==-2.0
    assert result["strict_close_return_pct"]==1.0


def test_liquidity_coverage_rejects_missing_duplicate_and_partial_paths():
    from scripts.update_emerging_liquidity_shadow import _eval
    event={"detected_ts":3601.0,"entry_eur":1.0}
    first=3900_000
    complete=[(first+i*300_000,1.04,0.97,1.01) for i in range(11)]
    missing=_eval(event,complete[:-1],1)
    assert missing["coverage_status"]=="INCOMPLETE_STRICT"
    assert missing["missing_bars"]==1
    assert missing["strict_close_return_pct"] is None
    assert missing["close_return_pct"]==1.0
    duplicate=_eval(event,complete+[complete[0]],1)
    assert duplicate["coverage_status"]=="INCOMPLETE_STRICT"
    assert duplicate["strict_close_return_pct"] is None
    offgrid=_eval(event,complete+[(first+1000,4.,0.1,4.)],1)
    assert offgrid["strict_complete"] is False
    assert offgrid["strict_mfe_pct"] is None


def test_four_hour_horizon_excludes_boundary_future_wick():
    from scripts.update_emerging_liquidity_shadow import _eval
    event={"detected_ts":3601.0,"entry_eur":1.0}
    first=3900_000
    xs=[(first+i*300_000,1.01,0.99,1.0) for i in range(47)]
    x=_eval(event,xs+[(first+47*300_000,5.,0.01,5.)],4)
    assert x["coverage_status"]=="COMPLETE_STRICT"
    assert x["expected_bars"]==47
    assert x["bars"]==47
    assert x["strict_mfe_pct"]==1.0
