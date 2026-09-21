from pathlib import Path
def test_hq_gate_sweep_is_research_only():
    x=Path("scripts/audit_solaire_v2_hq_gate_sweep.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "RANGES=(3.0,4.0,5.0,6.0)" in x
    assert "RRS=(1.10,1.25,1.50)" in x
    assert "historical bid/ask spread not reconstructed" in x
