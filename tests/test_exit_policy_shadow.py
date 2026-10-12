from pathlib import Path

def test_exit_policy_shadow_is_measurement_only():
    x=Path("scripts/update_exit_policy_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "full_1_4r" in x and "full_1_5r" in x and "full_1_6r" in x
    assert "LOW_BEFORE_HIGH_CONSERVATIVE" in x
    assert "comparisons_vs_current" in x


def test_exit_policy_shadow_separates_true_prospective_cohort():
    x=Path("scripts/update_exit_policy_shadow.py").read_text()
    assert "production_exit_policy_shadow_state.json" in x
    assert "prospective_started_at_utc" in x
    assert "prospective_tracked_buys" in x
    assert "prospective_summary" in x
    assert "prospective_comparisons_vs_current" in x


def test_exit_policy_shadow_resets_after_priority2_freeze():
    x=Path("scripts/update_exit_policy_shadow.py").read_text()
    assert "tp_r_grid_post_priority2_20260922" in x
    assert "2026-09-22T18:54:05+00:00" in x
    assert "POST_PRIORITY2_FREEZE" in x


def test_exit_policy_shadow_compares_candidates_directly_and_tracks_readiness():
    x=Path("scripts/update_exit_policy_shadow.py").read_text()
    assert "prospective_candidate_pairwise" in x
    assert "full_1_4r_vs_full_1_5r" not in x  # generated programmatically
    assert "CHECKPOINT_COMPLETE_4H=30" in x
    assert "DECISION_COMPLETE_12H=50" in x
    assert "decision_readiness" in x


def test_exit_policy_strict_grid_prevents_future_wick_and_marks_missing_bars():
    from scripts.update_exit_policy_shadow import _sim, _sim_stop_policy
    entry={"price":1.0,"stop":0.9,"tp":1.1,"ts":3601.0}
    first=3900_000
    bars=[(first+i*300_000,1.,1.02,0.98,1.0,100.) for i in range(47)]
    future=(first+47*300_000,1.,5.,0.01,5.,100.)
    actual=_sim(1.0,0.9,1.1,3601.0,bars+[future],4,None)
    assert actual["quality_version"]=="STRICT_CLOSED_GRID_V1"
    assert actual["expected_bars"]==47
    assert actual["bars_used"]==47
    assert actual["complete_horizon"] is True
    assert actual["exit_reason"]=="HORIZON_CLOSE"
    assert actual["gross_return_pct"]==0.0
    phase=_sim_stop_policy(1.0,0.9,3601.0,bars+[future],4,"MIXED_1H",True)
    assert phase["complete_horizon"] is True
    assert phase["gross_return_pct"]==0.0

    missing=_sim(1.0,0.9,1.1,3601.0,bars[:5]+bars[6:],4,None)
    assert missing["complete_horizon"] is False
    assert missing["coverage_status"]=="INCOMPLETE_STRICT"
    assert missing["missing_bars"]==1
    duplicate=_sim(1.0,0.9,1.1,3601.0,bars+[bars[0]],4,None)
    assert duplicate["complete_horizon"] is False


def test_exit_shadow_summary_excludes_legacy_false_complete():
    from scripts.update_exit_policy_shadow import _summary, _sim, _strictly_complete
    first=3900_000
    bars=[(first+i*300_000,1.,1.02,0.98,1.0,100.) for i in range(47)]
    strict=_sim(1.,0.9,1.1,3601.,bars,4,None)
    legacy={"complete_horizon":True,"net_return_pct_est":99.0,"r_multiple":999.0,
            "exit_reason":"TARGET"}
    assert _strictly_complete(legacy) is False
    rows=[
        {"stake_eur":150.0,"policies":{"current_tp1_stop":{"4":legacy}}},
        {"stake_eur":150.0,"policies":{"current_tp1_stop":{"4":strict}}},
    ]
    x=_summary(rows,"current_tp1_stop",4)
    assert x["n"]==1
    assert x["sum_net_pnl_eur_est"]==-0.45
