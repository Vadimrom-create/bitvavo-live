import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_full_history_evaluate_only_smoke():
    result = subprocess.run(
        [sys.executable, "pipeline.py", "--evaluate-only"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=900,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    evaluation = ROOT / "evaluation.json"
    assert evaluation.exists()
    text = evaluation.read_text(encoding="utf-8")
    assert '"scan_count"' in text
    assert '"observation_count"' in text
    assert '"complete_buy_episodes"' in text
