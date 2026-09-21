from pathlib import Path

def test_rejection_structure_details_is_research_only():
    x=Path("scripts/audit_solaire_rejection_structure_details.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "STRUCTURAL_RANGE_TOO_NARROW" in x
    assert "STRUCTURAL_STOP_TOO_WIDE" in x
    assert "range_to_atr_ratio" in x
    assert "stop_distance_pct" in x
    assert "XVG-EUR" in x and "SAGA-EUR" in x
