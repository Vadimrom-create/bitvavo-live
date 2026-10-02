from research.production_journal import evaluate_bars, evaluate_closed_5m_path


def _series(decision_ts, horizon_hours=1):
    first = ((int(decision_ts * 1000) // 300_000) + 1) * 300_000
    end_ms = int((decision_ts + horizon_hours * 3600) * 1000)
    last = ((end_ms - 300_000) // 300_000) * 300_000
    starts = list(range(first, last + 1, 300_000))
    return starts


def _bar(ts, high=1.01, low=0.99, close=1.0):
    return [ts, 1.0, high, low, close, 10.0]


def test_evaluate_bars_sorts_newest_first_input_before_close_and_path():
    decision_ts = 1_788_883_210.0
    starts = _series(decision_ts)
    bars = [_bar(ts, close=1.0 + i * 0.001) for i, ts in enumerate(starts)]
    # Earliest bar hits stop; a later bar hits TP. Newest-first API order must
    # not let the later TP win the path race.
    bars[0] = _bar(starts[0], high=1.02, low=0.94, close=0.97)
    bars[-1] = _bar(starts[-1], high=1.11, low=1.00, close=1.08)
    entry = {
        "decision_ts": decision_ts,
        "decision_type": "BUY_SENT",
        "entry_eur": 1.0,
        "stop_eur": 0.95,
        "tp1_eur": 1.10,
    }
    result = evaluate_bars(entry, list(reversed(bars)), 1)
    assert result is not None
    assert result["result"] == "STOP"
    assert result["path_event_start_ms"] == starts[0]
    assert result["first_bar_start_ms"] == starts[0]
    assert result["last_bar_start_ms"] == starts[-1]
    assert result["bars_used"] == result["expected_bars"]
    assert result["coverage_ratio"] == 1.0
    assert result["method"] == "chronological_continuous_closed_5m_bars_after_decision_bar"
    assert result["close_return_pct"] == 8.0


def test_evaluate_bars_rejects_incomplete_horizon():
    decision_ts = 1_788_883_210.0
    starts = _series(decision_ts)
    bars = [_bar(ts) for ts in starts]
    del bars[len(bars) // 2]
    entry = {
        "decision_ts": decision_ts,
        "decision_type": "REJECTED",
        "signal_price_eur": 1.0,
    }
    assert evaluate_bars(entry, bars, 1) is None


def test_evaluate_bars_excludes_bar_not_closed_by_horizon():
    decision_ts = 1_788_883_210.0
    starts = _series(decision_ts)
    bars = [_bar(ts, close=1.0) for ts in starts]
    end_ms = int((decision_ts + 3600) * 1000)
    partial_start = (end_ms // 300_000) * 300_000
    if partial_start not in starts:
        bars.append(_bar(partial_start, high=2.0, low=0.5, close=2.0))
    entry = {
        "decision_ts": decision_ts,
        "decision_type": "REJECTED",
        "signal_price_eur": 1.0,
    }
    result = evaluate_bars(entry, list(reversed(bars)), 1)
    assert result is not None
    assert result["mfe_pct"] == 1.0
    assert result["mae_pct"] == -1.0
    assert result["close_return_pct"] == 0.0


def test_shared_causal_evaluator_exposes_incomplete_horizon():
    decision_ts = 1_788_883_210.0
    starts = _series(decision_ts)
    bars = [_bar(ts) for ts in starts]
    del bars[len(bars) // 2]
    result = evaluate_closed_5m_path(bars, decision_ts, 1.0, 1)
    assert result["status"] == "INCOMPLETE"
    assert result["reason"] == "MISSING_CLOSED_5M_BARS"
    assert result["bars_used"] == result["expected_bars"] - 1
    assert result["coverage_ratio"] < 1.0


def test_shared_causal_evaluator_is_conservative_when_stop_and_tp_touch_same_bar():
    decision_ts = 1_788_883_210.0
    starts = _series(decision_ts)
    bars = [_bar(ts) for ts in starts]
    bars[0] = _bar(starts[0], high=1.11, low=0.94, close=1.02)
    result = evaluate_closed_5m_path(
        bars,
        decision_ts,
        1.0,
        1,
        stop_eur=0.95,
        tp1_eur=1.10,
    )
    assert result["status"] == "COMPLETE"
    assert result["result"] == "STOP_SAME_BAR_CONSERVATIVE"
    assert result["path_event_start_ms"] == starts[0]
