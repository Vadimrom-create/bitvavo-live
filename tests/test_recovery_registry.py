from research.recovery_registry import (
    TTL_SECONDS,
    new_registry,
    observe_episode,
    register_episode,
)


def _event():
    return {
        "event_id": "ABC-EUR|1000",
        "market": "ABC-EUR",
        "rejected_ts": 1000.0,
        "rejected_at_utc": "1970-01-01T00:16:40+00:00",
        "first_rejection_reason": "SPREAD_TOO_WIDE",
        "rejection_price_eur": 1.0,
        "signal_state": "CONFIRMED_ACCELERATION",
        "signal_score": 7.0,
        "evidence_count": 4,
    }


def _row(*, episode=1, state="CONFIRMED_ACCELERATION", score=7.0, evidence=4):
    return {
        "market": "ABC-EUR",
        "episode": episode,
        "last": 1.01,
        "signal_state": state,
        "signal_score": score,
        "acceleration": {"evidence_count": evidence},
    }


def test_absence_does_not_invalidate_or_promote():
    registry = register_episode(new_registry(), _event(), _row(), 1001.0)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        None,
        1100.0,
        execution_pass=None,
        execution_reason="SIGNAL_ABSENT_NOT_EVALUATED",
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "BLOCKED_BUT_ALIVE"
    assert record["closed"] is False
    assert record["proposal_count"] == 0
    assert record["attempts"][-1]["signal_quality_reason"] == "ABSENT_CURRENT_SCAN"


def test_execution_pass_without_signal_quality_is_not_candidate():
    registry = register_episode(new_registry(), _event(), _row(), 1001.0)
    low = _row(state="BUILDING_ACCELERATION", score=5.9, evidence=4)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        low,
        1200.0,
        execution_pass=True,
        plan={"entry_eur": 1.02, "stop_eur": 0.98},
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "TECHNICAL_PASS_SIGNAL_NOT_QUALIFIED"
    assert record["closed"] is False
    assert record["first_execution_pass"] is not None
    assert record["first_shadow_candidate"] is None


def test_first_qualified_recovery_emits_one_shadow_candidate_only():
    registry = register_episode(new_registry(), _event(), _row(), 1001.0)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        _row(),
        1300.0,
        execution_pass=True,
        plan={"entry_eur": 1.02, "stop_eur": 0.98},
        prior_thesis_clear=True,
        prior_thesis_status="NO_TRACKED_PRIOR_BUY_THESIS",
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "SHADOW_RECOVERY_CANDIDATE"
    assert record["closed"] is True
    assert record["proposal_count"] == 1

    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        _row(),
        1400.0,
        execution_pass=True,
        plan={"entry_eur": 1.03, "stop_eur": 0.99},
        prior_thesis_clear=True,
        prior_thesis_status="NO_TRACKED_PRIOR_BUY_THESIS",
    )
    assert registry["episodes"]["ABC-EUR|1000"]["proposal_count"] == 1


def test_new_episode_invalidates_old_registry_episode():
    registry = register_episode(new_registry(), _event(), _row(episode=2), 1001.0)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        _row(episode=3),
        1100.0,
        execution_pass=False,
        execution_reason="SPREAD_TOO_WIDE",
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "INVALIDATED_NEW_EPISODE"
    assert record["closed"] is True


def test_ttl_is_fixed_at_24h_and_expires_without_retrospective_extension():
    registry = register_episode(new_registry(), _event(), _row(), 1001.0)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        None,
        1000.0 + TTL_SECONDS + 1,
        execution_pass=None,
        execution_reason="SIGNAL_ABSENT_NOT_EVALUATED",
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "EXPIRED_24H"
    assert record["closed"] is True


def test_registry_module_has_no_sender_mail_or_order_dependency():
    from pathlib import Path

    x = Path("research/recovery_registry.py").read_text()
    assert "send_production_buy_alert" not in x
    assert "email_alert" not in x
    assert "mark_sent" not in x
    assert '"affects_buy_gate": False' in x
    assert '"affects_email": False' in x
    assert '"affects_orders": False' in x


def test_prior_thesis_block_prevents_shadow_candidate():
    registry = register_episode(new_registry(), _event(), _row(), 1001.0)
    registry = observe_episode(
        registry,
        "ABC-EUR|1000",
        _row(),
        1300.0,
        execution_pass=True,
        plan={"entry_eur": 1.02, "stop_eur": 0.98},
        prior_thesis_clear=False,
        prior_thesis_status="PRIOR_BUY_THESIS_STILL_ACTIVE",
    )
    record = registry["episodes"]["ABC-EUR|1000"]
    assert record["state"] == "TECHNICAL_PASS_PRIOR_THESIS_BLOCKED"
    assert record["closed"] is False
    assert record["proposal_count"] == 0


def test_heartbeat_is_sole_persistent_recovery_registry_writer():
    from pathlib import Path

    fast = Path(".github/workflows/production_scan_fast.yml").read_text()
    heavy = Path(".github/workflows/production_scan.yml").read_text()
    rejection = Path("scripts/update_rejection_shadow.py").read_text()

    assert "python scripts/update_recovery_registry_heartbeat.py" in fast
    assert "production_recovery_registry_shadow.json" in fast
    assert "production_recovery_registry_status.json" in fast
    assert "production_recovery_registry_shadow.json" not in heavy
    assert "atomic_json(REGISTRY,registry)" not in rejection


def test_recovery_registry_heartbeat_exposes_freshness_and_frozen_invariants():
    from pathlib import Path

    x = Path("scripts/update_recovery_registry_heartbeat.py").read_text()
    assert "FRESHNESS_LIMIT_SECONDS = 15 * 60" in x
    assert '"previous_registry_was_stale"' in x
    assert '"policy_drift_detected_before_normalization"' in x
    assert '"policy_frozen"' in x
    assert '"invariant_flags_ok"' in x
    assert '"affects_detection": False' in x
    assert '"affects_buy_gate": False' in x
    assert '"affects_email": False' in x
    assert '"affects_orders": False' in x


def test_incomplete_forward_evaluations_are_retried_and_stale_health_is_exposed():
    from pathlib import Path

    x = Path("scripts/update_rejection_shadow.py").read_text()
    assert 'existing.get("status")=="INCOMPLETE"' in x
    assert '"stale_incomplete_rejection_evaluations"' in x
    assert '"stale_incomplete_reentry_evaluations"' in x
    assert '"stale_incomplete_evaluations"' in x
    assert "INCOMPLETE_GRACE_SECONDS=15*60" in x

def test_shadow_evaluations_fetch_the_episode_historical_window():
    from pathlib import Path

    x = Path("scripts/update_rejection_shadow.py").read_text()
    assert '"start":start_ms' in x
    assert '"end":end_ms' in x
    assert 'groups.setdefault((kind,idx),[]).append(h)' in x
    assert '{"interval":"5m","limit":400},cache=False' not in x


def test_historical_candle_query_aligns_end_to_5m_boundary():
    from pathlib import Path

    x = Path("scripts/update_rejection_shadow.py").read_text()
    assert "last_full_start=((horizon_end_ms-300_000)//300_000)*300_000" in x
    assert "end_ms=last_full_start+300_000" in x
    assert '"incomplete_zero_bar_evaluations"' in x
    assert '"incomplete_partial_coverage_evaluations"' in x


def test_delisted_market_horizons_are_censored_not_reported_as_api_failures():
    from pathlib import Path

    x = Path("scripts/update_rejection_shadow.py").read_text()
    assert '"status":"CENSORED"' in x
    assert '"reason":"MARKET_NOT_TRADING"' in x
    assert '"method":"market_lifecycle_censoring"' in x
    assert '"censored_market_inactive_evaluations"' in x
    assert "if market not in metadata:" in x
    assert '"UNLISTED_OR_REMOVED"' in x


def test_registry_deduplicates_same_production_episode_identity():
    event1 = _event()
    event1["source_episode_id"] = "episode_same"
    event1["source_decision_id"] = "decision_one"
    registry = register_episode(new_registry(), event1, _row(), 1001.0)

    event2 = dict(event1)
    event2["event_id"] = "ABC-EUR|1005"
    event2["source_decision_id"] = "decision_two"
    registry = register_episode(registry, event2, _row(), 1005.0)

    assert len(registry["episodes"]) == 1
    assert "ABC-EUR|1000" in registry["episodes"]
