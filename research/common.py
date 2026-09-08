from __future__ import annotations

import gzip
import json
import math
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

INTERVAL_MS = {'5m': 300_000, '15m': 900_000, '1h': 3_600_000, '4h': 14_400_000, '1d': 86_400_000}


def utc(ts=None):
    return datetime.fromtimestamp(ts, timezone.utc).isoformat() if ts is not None else datetime.now(timezone.utc).isoformat()


def timestamp(value):
    if isinstance(value, (float, int)) and not isinstance(value, bool):
        result = float(value)
    else:
        dt = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        if dt.tzinfo is None:
            raise ValueError('timezone_required')
        result = dt.timestamp()
    if not math.isfinite(result):
        raise ValueError('non_finite_timestamp')
    return result


def finite(value, default=None):
    try:
        n = float(value)
        return n if math.isfinite(n) else default
    except (TypeError, ValueError):
        return default


def read_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', encoding='utf-8') as f:
        return json.load(f)  # Corruption is an error, never an empty history.


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode()
    if path.suffix == '.gz':
        data = gzip.compress(data, mtime=0)
    fd, tmp = tempfile.mkstemp(prefix=path.name, suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def freshness(*, now, retrieved, candle_start_ms=None, interval='15m', max_retrieval_age=300, grace=60):
    reasons = []
    try:
        age = now - timestamp(retrieved)
        if age < -30:
            reasons.append('FUTURE_RETRIEVAL_TIMESTAMP')
        elif age > max_retrieval_age:
            reasons.append('STALE_RETRIEVAL')
    except (ValueError, TypeError):
        age = None
        reasons.append('MISSING_RETRIEVAL_TIMESTAMP')
    close_age = None
    if candle_start_ms is not None:
        duration = INTERVAL_MS[interval]
        close_ms = int(candle_start_ms) + duration
        close_age = now - close_ms / 1000
        # The timestamp names the OPEN, not the close. A freshly CLOSED 15m
        # candle is legitimately almost 15m old just before the next close.
        expected_close = int((now - grace) * 1000 // duration) * duration
        if close_ms > now * 1000:
            reasons.append('OPEN_CANDLE')
        elif close_ms < expected_close:
            reasons.append('MISSING_LATEST_CLOSED_CANDLE')
    return {'ok': not reasons, 'reasons': reasons, 'retrieval_age_seconds': age,
            'closed_candle_age_seconds': close_age}
