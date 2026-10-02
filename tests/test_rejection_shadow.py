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
    assert "evaluate_closed_5m_path" in x
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


def test_rejection_shadow_separates_reason_change_from_execution_pass():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "initial_veto_reason_changed" in x
    assert "execution_pass_observed" in x
    assert "events_with_execution_pass" in x
    assert "events_with_initial_veto_reason_changed" in x
    assert "legacy_events_with_original_condition_resolved" in x


def test_rejection_shadow_uses_production_rejection_timestamp_and_explicit_incomplete_results():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "rejected_ts=_parse_ts(rejected_at) or now" in x
    assert "evaluate_closed_5m_path" in x
    assert "incomplete_rejection_evaluations" in x
    assert "incomplete_reentry_evaluations" in x


def test_rejection_shadow_persists_blocked_alive_registry_without_sender_activation():
    x=Path("scripts/update_rejection_shadow.py").read_text()
    assert "production_recovery_registry_shadow.json" in x
    assert "register_episode" in x
    assert "observe_episode" in x
    assert "SIGNAL_ABSENT_NOT_EVALUATED" in x
    assert "recovery_registry" in x
