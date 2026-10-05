from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline.py"


def test_pipeline_emits_additive_history_phase_timing_with_async_full_evaluation():
    text = PIPELINE.read_text(encoding="utf-8")
    for key in (
        "recent_history_rebuild",
        "observation_build",
        "portfolio_selection",
        "history_save_ingest",
        "full_history_evaluation",
        "market_control",
    ):
        assert f"phase_seconds['{key}']" in text
    assert "PIPELINE_PHASE_TIMING " in text
    assert "rebuild_since('history', connect(), baseline_ts - LIVE_HISTORY_WINDOW_SECONDS)" in text
    assert "evaluation = read_json('evaluation.json', {})" in text
    assert "atomic_json('evaluation.json', evaluation)" not in text
    assert "evaluate(rebuild('history', connect()))" in text
    assert "control = market_control(db, observations, baseline_ts, candles15)" in text
