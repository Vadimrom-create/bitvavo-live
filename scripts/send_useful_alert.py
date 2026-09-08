#!/usr/bin/env python3
"""Call the existing Gmail transport with quality-checked candidates only."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import email_alert_v4

email_alert_v4.V4_JSON = Path('alert_candidates.json')

if __name__ == '__main__':
    raise SystemExit(email_alert_v4.main())
