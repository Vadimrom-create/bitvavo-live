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
