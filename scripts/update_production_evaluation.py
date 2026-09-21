#!/usr/bin/env python3
"""Record actual Solaire decisions and add non-blocking prospective outcomes."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.common import atomic_json, read_json, utc
from research.http import PublicClient
from research.production_journal import due_horizons, evaluate_bars, record_cycle

PAYLOAD = "production_alert_candidates.json"
ALERT_STATUS = "production_alert_status.json"
JOURNAL = "production_decision_journal.json"
STATUS = "production_evaluation_status.json"


def main() -> int:
    now = time.time()
    payload = read_json(PAYLOAD, {})
    alert_status = read_json(ALERT_STATUS, {})
    journal = record_cycle(payload, alert_status, read_json(JOURNAL, {}))

    due = {}
    for idx, entry in enumerate(journal.get("entries", [])):
        horizons = due_horizons(entry, now)
        if horizons:
            due[idx] = horizons

    status = {
        "checked_at_utc": utc(now),
        "status": "OK",
        "blocking": False,
        "recorded_entries": len(journal.get("entries", [])),
        "due_entries": len(due),
        "evaluated_horizons": 0,
        "errors": [],
    }

    if due:
        try:
            client = PublicClient(timeout=10, retries=2, requests_per_second=8)
            client.get("/time", cache=False)
            markets = sorted(
                {
                    journal["entries"][idx].get("market")
                    for idx in due
                    if journal["entries"][idx].get("market")
                }
            )
            candles = {}
            for market in markets:
                try:
                    candles[market] = client.get(
                        "/" + market + "/candles",
                        {"interval": "5m", "limit": 400},
                        cache=False,
                    )
                except (RuntimeError, ValueError, KeyError) as exc:
                    status["errors"].append(
                        {"market": market, "reason": type(exc).__name__ + ":" + str(exc)}
                    )

            for idx, horizons in due.items():
                entry = journal["entries"][idx]
                raw = candles.get(entry.get("market"))
                if not raw:
                    continue
                for hours in horizons:
                    outcome = evaluate_bars(entry, raw, hours)
                    if outcome is not None:
                        entry.setdefault("evaluations", {})[str(hours)] = outcome
                        status["evaluated_horizons"] += 1

            if status["errors"]:
                status["status"] = "DEGRADED_NONBLOCKING"
        except (RuntimeError, ValueError, KeyError) as exc:
            status["status"] = "DEGRADED_NONBLOCKING"
            status["errors"].append(
                {"reason": type(exc).__name__ + ":" + str(exc)}
            )

    journal["updated_at_utc"] = utc(now)
    atomic_json(JOURNAL, journal)
    atomic_json(STATUS, status)
    print("SOLAIRE_EVALUATION " + json.dumps(status, ensure_ascii=False))
    # Evaluation must never break the production scan/alert path.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
