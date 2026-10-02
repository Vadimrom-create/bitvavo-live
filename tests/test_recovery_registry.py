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
