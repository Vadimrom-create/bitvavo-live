from pathlib import Path
def test_detection_timing_audit_is_shadow_only():
    x=Path("scripts/audit_solaire_v2_detection_timing.py").read_text()
    assert '"affects_buy_gate":False' in x
    assert '"affects_email":False' in x
    assert "current_confirmed" in x
    assert "early_4_25_e2" in x
    assert "FET-EUR" in x and "NIL-EUR" in x
