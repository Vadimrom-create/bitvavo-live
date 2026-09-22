from pathlib import Path

def test_health_reports_all_nonblocking_shadows():
    x=Path("scripts/check_production_health.py").read_text()
    for token in [
        "EARLY_BUILDING_OUTCOME",
        "V21_RANGE5_OUTCOME",
        "REJECTION_SHADOW_OUTCOME",
        "EXIT_POLICY_OUTCOME",
        "all_shadows_block_anything",
        "solaire_production_health_v2",
    ]:
        assert token in x

def test_ci_critical_path_does_not_require_oracle_or_railway():
    x=Path(".github/workflows/ci.yml").read_text()
    critical=x.split("Legacy Oracle and Railway syntax checks")[0]
    assert "oracle/bootstrap_oracle_deploy.sh" not in critical
    assert "railway.toml" not in critical
    assert "Validate direct Solaire production sources" in critical
