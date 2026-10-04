"""Causal detector control. A control payload is never a BUY or a real fill."""
import copy
import hashlib
import json
from research.common import timestamp, utc

MAX_AGE = 300
KINDS = {'PRODUCTION_OBSERVED', 'RECOMPUTED_SHADOW'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=True).encode()).hexdigest()


def receipt(universe, control, manifest, now):
    result = {
        'schema': 'solaire_paired_c0_v1', 'status': 'UNKNOWN_CONTROL_MISSING', 'eligible': False,
        'kind': manifest.get('kind', 'UNKNOWN'), 'control_id': manifest.get('control_id'),
        'logic_commit': manifest.get('logic_commit'), 'logic_sha256': manifest.get('logic_sha256'),
        'universe_sha256': manifest.get('universe_sha256'), 'control_sha256': manifest.get('control_sha256'),
        'generated_at_utc': control.get('generated_at_utc'), 'validated_at_utc': utc(now),
        'scope': 'PRODUCTION_DETECTOR_CANDIDATES_NOT_DELIVERED_BUYS',
        'execution_comparison_eligible': False,
        'research_only': True, 'published_as_production_decision': False,
        'sender_called': False, 'orders_submitted': False,
    }
    try:
        age = now - timestamp(control.get('generated_at_utc'))
    except (TypeError, ValueError):
        result['age_seconds'] = None
        return result
    result['age_seconds'] = age
    if age < 0 or age > MAX_AGE:
        result['status'] = 'UNKNOWN_STALE_CONTROL'
    elif (manifest.get('kind') not in KINDS or manifest.get('logic_commit') in {None, '', 'UNKNOWN'} or
          not isinstance(control.get('tracking'), list) or not isinstance(control.get('watch'), list)):
        result['status'] = 'UNKNOWN_UNVERIFIED_CONTROL'
    elif (universe.get('generated_at_utc') != control.get('generated_at_utc') or
          manifest.get('universe_sha256') != digest(universe) or
          manifest.get('control_sha256') != digest(control)):
        result['status'] = 'UNKNOWN_SNAPSHOT_MISMATCH'
    else:
        result.update(status='CURRENT', eligible=True)
    return result


def tag_event(journal, event):
    """Only new events acquire their actual cycle's receipt; no legacy backfill."""
    if 'current_c0_pairing' in journal:
        event.setdefault('c0_pairing', copy.deepcopy(journal['current_c0_pairing']))
    return event


def paired_groups(events):
    """No legacy/unpaired event enters a causal control comparison."""
    return {kind: [e for e in events if (e.get('c0_pairing') or {}).get('eligible') is True
                   and e['c0_pairing'].get('kind') == kind] for kind in sorted(KINDS)}
