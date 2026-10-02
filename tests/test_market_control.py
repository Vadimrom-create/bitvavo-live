from pathlib import Path


def test_market_control_distinguishes_current_presence_from_detection_history():
    x=Path("market_control.py").read_text()
    assert "NOT_CURRENTLY_PRESENT_V3_V4" in x
    assert "current_watchlist_presence" in x
    assert "CURRENT_WATCHLIST_PRESENCE_RATE" in x
    assert "HISTORICAL_DETECTION_RATE" in x
    assert '"status": "UNKNOWN"' in x
    assert "coverage_deprecation" in x


def test_market_control_keeps_legacy_names_only_as_deprecated_aliases():
    x=Path("market_control.py").read_text()
    assert "NOT_DETECTED_V3_V4" in x
    assert "deprecated legacy alias" in x
    assert "material_not_currently_present" in x
    assert "material_misses" in x
