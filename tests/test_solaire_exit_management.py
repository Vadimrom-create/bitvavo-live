from pathlib import Path

def test_exit_management_audit_is_research_only():
    x=Path("scripts/audit_solaire_exit_management.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "partial50_plus5_be" in x
    assert "trail_1r_distance_after_1r" in x
    assert "current_with_4h_time_stop" in x
    assert "LOW_BEFORE_HIGH_CONSERVATIVE" in x
    assert "comparisons_vs_current" in x


def test_exit_target_grid_includes_intermediate_r_levels():
    x=Path("scripts/audit_solaire_exit_management.py").read_text()
    for token in ["full_1_25r","full_1_4r","full_1_6r","full_1_75r"]:
        assert token in x
