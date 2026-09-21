from pathlib import Path

def test_confirmed_range5_backfill_is_research_only():
    x=Path("scripts/audit_solaire_v21_confirmed_range5.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "STRUCTURAL_RANGE_TOO_NARROW" in x
    assert "CANDIDATE_RANGE=5.0" in x
    assert "CURRENT_RANGE=6.0" in x
    assert "counterfactual5_structure_pass_proxy" in x
    assert "upstream_execution_gates_passed_at_rejection" in x
