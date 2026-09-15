"""Sealed optional producers, independent of the scan and its active alerts."""
from pathlib import Path
import re
import uuid

from research.common import atomic_json, read_json, timestamp, utc
from research.input_contract import code_revision
from research.publication import file_hash, immutable_json

OUTPUTS = {
    'quotes': {'live_quotes.json', 'ethfi_live.json'},
    'feedback': {'feedback_report.json'},
}


def allowed(producer, name):
    p = Path(name)
    if p.is_absolute() or '..' in p.parts or p.as_posix() != name:
        return False
    return name in OUTPUTS[producer] or (producer == 'feedback' and
        re.fullmatch(r'feedback_(?:state|history)/[A-Z0-9_]+/[A-Z0-9_]+(?:/[A-Za-z0-9_-]+)?\.json', name) is not None)


def begin(producer):
    """Invalidate an old success pointer before any fallible work."""
    if producer not in OUTPUTS:
        raise ValueError('UNKNOWN_OPTIONAL_PRODUCER')
    pointer = Path('runtime') / ('current_' + producer + '.json')
    pointer.unlink(missing_ok=True)
    return uuid.uuid4().hex


def seal(producer, attempt, outputs, sources=None, **identity):
    if not re.fullmatch('[0-9a-f]{32}', attempt):
        raise ValueError('INVALID_PRODUCTION_ID')
    if not OUTPUTS[producer].issubset(outputs) or any(not allowed(producer, p) for p in outputs):
        raise ValueError('OPTIONAL_OUTPUT_NOT_OWNED')
    manifest = {'schema_version': 1, 'producer': producer, 'production_id': attempt,
                'code_commit': code_revision(), 'ready_at_utc': utc(),
                'active_alerts_enabled': False, **identity,
                'sources': sources or {}, 'outputs': {p: file_hash(p) for p in outputs}}
    manifest['archive_path'] = f'producer_manifests/{producer}/{attempt}.json'
    immutable_json(manifest['archive_path'], manifest)
    atomic_json(producer + '_manifest.json', manifest)
    atomic_json(f'runtime/current_{producer}.json', {'production_id': attempt})
    return manifest


def validate(producer, root='.', require_current=True):
    root = Path(root)
    m = read_json(root / (producer + '_manifest.json'), {})
    if m.get('producer') != producer or m.get('active_alerts_enabled') is not False:
        raise ValueError('OPTIONAL_MANIFEST_REQUIRED')
    attempt = m.get('production_id', '')
    if not re.fullmatch('[0-9a-f]{32}', attempt):
        raise ValueError('INVALID_PRODUCTION_ID')
    if require_current and read_json(root / f'runtime/current_{producer}.json') != {'production_id': attempt}:
        raise ValueError('CURRENT_OPTIONAL_PRODUCTION_REQUIRED')
    archive = f'producer_manifests/{producer}/{attempt}.json'
    if m.get('archive_path') != archive or read_json(root / archive) != m:
        raise ValueError('OPTIONAL_MANIFEST_ARCHIVE_MISMATCH')
    if not OUTPUTS[producer].issubset(m['outputs']):
        raise ValueError('MISSING_OPTIONAL_OUTPUT')
    for name, sha in m['outputs'].items():
        if not allowed(producer, name) or file_hash(root / name) != sha:
            raise ValueError('OPTIONAL_OUTPUT_MISMATCH')
    if require_current:
        for name, sha in m['sources'].items():
            p = Path(name)
            if p.is_absolute() or '..' in p.parts or file_hash(root / p) != sha:
                raise ValueError('OPTIONAL_SOURCE_MISMATCH')
        if producer == 'feedback':
            current = read_json(root / 'runtime/current_scan.json', {})
            if current.get('scan_id') != m.get('scan_id') or current.get('journal') not in m['sources']:
                raise ValueError('FEEDBACK_SCAN_MISMATCH')
        else:
            from scripts.live_quotes import MAX_SNAPSHOT_AGE_SECONDS
            import time
            quote = read_json(root / 'live_quotes.json')
            ages = [time.time() - timestamp(quote[k]) for k in ('price_retrieved_at_utc', 'book_retrieved_at_utc')]
            if quote.get('valid') is not True or any(a < -2 or a > MAX_SNAPSHOT_AGE_SECONDS for a in ages):
                raise ValueError('STALE_OPTIONAL_QUOTES')
    return m
