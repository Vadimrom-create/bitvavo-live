import json
import tempfile
from pathlib import Path

from research.history import connect, rebuild_since, save_scan


def _scan(scan_id, ts, market="TEST-EUR"):
    return {
        "schema_version": 2,
        "scan_id": scan_id,
        "scan_ts": ts,
        "scan_at_utc": "2026-10-05T00:00:00+00:00",
        "policy": "TEST",
        "operational_policy": "TEST",
        "source": "test",
        "observations": [{
            "market": market,
            "price_eur": 1.0,
            "baseline": {"action_status": "WATCH"},
            "decision": "SURVEILLE",
        }],
        "candles_5m": {},
    }


def test_rebuild_since_excludes_old_journals_and_keeps_recent_ones():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        old = _scan("old", 1_000.0)
        recent = _scan("recent", 10_000.0)
        for scan, day in ((old, "2026-10-01"), (recent, "2026-10-05")):
            scan["scan_at_utc"] = day + "T00:00:00+00:00"
            save_scan(root, scan)

        db = rebuild_since(root, connect(), 5_000.0)
        ids = [row[0] for row in db.execute("SELECT id FROM scans ORDER BY ts").fetchall()]
        assert ids == ["recent"]


def test_rebuild_since_keeps_authoritative_timestamp_filter_inside_cutoff_day():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scan = _scan("too-old", 1_000.0)
        scan["scan_at_utc"] = "2026-10-05T00:00:00+00:00"
        save_scan(root, scan)

        db = rebuild_since(root, connect(), 5_000.0)
        assert db.execute("SELECT COUNT(*) FROM scans").fetchone()[0] == 0
