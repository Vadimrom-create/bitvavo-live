from pathlib import Path

from scripts.update_exit_policy_shadow import _sim_stop_policy


def _bars(*rows):
    # rows: (start_ms, high, low, close)
    return [(t, 1.0, h, l, c, 1.0) for t, h, l, c in rows]


def test_pullback_keeps_immediate_structural_stop():
    start = 1_800_000_010.0
    first = ((int(start * 1000) // 300_000) + 1) * 300_000
    bars = _bars(
        (first, 1.01, 0.94, 0.99),
        (first + 300_000, 1.02, 0.98, 1.01),
    )
    result = _sim_stop_policy(1.0, 0.95, start, bars, 4, "PULLBACK_1H", True)
    assert result["exit_reason"] == "STRUCTURAL_STOP_TOUCH"
    assert result["exit_eur"] if "exit_eur" in result else result["gross_return_pct"] == -5.0


def test_mixed_requires_two_consecutive_5m_closes_below_soft_stop():
    start = 1_800_000_010.0
    first = ((int(start * 1000) // 300_000) + 1) * 300_000
    bars = _bars(
        # Touches the stop intrabar but closes back above it: no exit.
        (first, 1.00, 0.94, 0.97),
        # First close below soft stop.
        (first + 300_000, 0.97, 0.93, 0.94),
        # Recovers: confirmation count resets.
        (first + 600_000, 0.98, 0.94, 0.96),
        # Two consecutive closes below soft stop.
        (first + 900_000, 0.96, 0.93, 0.94),
        (first + 1_200_000, 0.95, 0.92, 0.93),
    )
    result = _sim_stop_policy(1.0, 0.95, start, bars, 4, "MIXED_1H", True)
    assert result["exit_reason"] == "TWO_CONSECUTIVE_5M_CLOSES_BELOW_STOP"
    assert result["deferred_confirmation_eligible"] is True


def test_hard_stop_preempts_confirmation():
    start = 1_800_000_010.0
    first = ((int(start * 1000) // 300_000) + 1) * 300_000
    # R=0.05 -> 1.75R hard stop = 0.9125.
    bars = _bars((first, 1.0, 0.90, 0.96))
    result = _sim_stop_policy(1.0, 0.95, start, bars, 4, "EXPANSION_1H", True)
    assert result["exit_reason"] == "HARD_STOP_1_75R"
    assert result["hard_stop_eur"] == 0.9125


def test_direct_buy_journal_is_wired_into_sender_and_shadow():
    sender = Path("scripts/send_production_buy_alert.py").read_text()
    shadow = Path("scripts/update_exit_policy_shadow.py").read_text()
    evaluator = Path("scripts/update_production_evaluation.py").read_text()
    heartbeat = Path(".github/workflows/production_scan_fast.yml").read_text()
    watchdog = Path(".github/workflows/production_scan_watchdog.yml").read_text()

    assert "production_direct_decision_journal.json" in sender
    assert "record_cycle(" in sender
    assert 'DIRECT_JOURNAL="production_direct_decision_journal.json"' in shadow
    assert "PHASE_AWARE_2X5M_HARD_1_75R" in shadow
    assert "STOP_DEFERRED_PHASES" in shadow
    assert 'DIRECT_JOURNAL = "production_direct_decision_journal.json"' in evaluator
    assert "production_direct_decision_journal.json" in heartbeat
    assert "production_direct_decision_journal.json" in watchdog
