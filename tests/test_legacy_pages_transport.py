from pathlib import Path

def test_legacy_pages_transport_is_nonblocking():
    x=Path(".github/workflows/update.yml").read_text()
    assert "Preserve raw replay inputs and failure diagnostics" in x
    assert "Deploy legacy public Pages feed" in x
    pages=x.split("Configure legacy public Pages feed",1)[1]
    assert pages.count("continue-on-error: true") >= 3
