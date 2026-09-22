from pathlib import Path

def test_rejection_shadow_v4_is_measurement_only_and_tracks_downgrades():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "tracking_rows" in x
    assert "first_later_execution_valid_snapshot" in x
    assert "first_later_fully_actionable_entry" in x
    assert "BUILDING_ACCELERATION" in x
    assert "HORIZONS=(1,4,12,24)" in x
    assert "mfe_pct" in x and "mae_pct" in x


def test_rejection_shadow_measures_reentry_from_execution_clean_snapshot():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "execution_valid_evaluations" in x
    assert "_evaluate_reentry" in x
    assert "closed_5m_bars_after_first_execution_valid_snapshot" in x
    assert "evaluated_reentry_horizons" in x


def test_rejection_shadow_classifies_reentry_quality():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "CONFIRMED_REENTRY" in x
    assert "BUILDING_HQ_4E" in x
    assert "BUILDING_6_3" in x
    assert "reentry_delay_seconds" in x
    assert "reentry_tier_cohorts" in x
    assert "clean_mfe_ge5_mae_gt_minus5" in x


def test_rejection_shadow_backfills_existing_reentry_metadata():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert 'if not snap.get("reentry_tier")' in x
    assert 'snap["reentry_delay_seconds"]' in x


def test_rejection_shadow_tracks_rapid_reentry_buckets():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "LE_60S" in x
    assert "GT_60S_LE_5M" in x
    assert "GT_5M_LE_30M" in x
    assert "GT_30M" in x
    assert "rapid_reentry_cohorts" in x


def test_rejection_shadow_compares_priority2_reentry_policies():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "SCORE_GE6_E3" in x
    assert "SCORE_GE6_E4" in x
    assert "CONFIRMATION_15M_PRESENT" in x
    assert "CONFIRMATION_15M_ABSENT" in x
    assert "reentry_policy_cohorts" in x
    assert "priority2_promotion_readiness" in x
    assert '"target_reentries":20' in x


def test_rejection_shadow_preserves_reentry_milestones():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "first_later_building_snapshot" in x
    assert "first_later_confirmed_snapshot" in x
    assert "first_later_execution_valid_snapshot" in x
    assert "first_later_execution_valid_with_15m_confirmation" in x
    assert "timeframe_confirmation_15m" in x
    assert "confirmation_15m_component" in x
