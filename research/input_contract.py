"""Small causal input contract; missing historical provenance stays unknown."""
import hashlib
import json
from research.common import timestamp
from research.policies import LEGACY_DATA


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def require_available(record, cutoff):
    if timestamp(record['retrieved_at_utc']) > timestamp(cutoff):
        raise ValueError('INPUT_NOT_AVAILABLE_AT_CUTOFF')
    return record


def source_close_bound(record):
    """HTTP Date alone does not timestamp candle content. Request start is conservative."""
    started = timestamp(record['request_started_at_utc'])
    offset = float(record['server_offset_seconds'])
    uncertainty = float(record['clock_uncertainty_seconds'])
    if uncertainty < 0:
        raise ValueError('INVALID_CLOCK_BOUND')
    # timestamp rejects nonfinite values.
    return timestamp(started + offset - uncertainty)


def read_identities(scan):
    return {name: scan.get(name, LEGACY_DATA if name == 'data_policy' else None)
            for name in ('data_policy', 'decision_policy', 'execution_policy', 'evaluation_policy')}
