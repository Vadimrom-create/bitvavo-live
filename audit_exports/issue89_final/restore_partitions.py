"""Reassemble partitioned audit input byte-for-byte; no network or replay."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
for spec in json.loads((root / 'PARTITIONS.json').read_text()):
    obj = json.loads((root / spec['metadata']).read_text())
    rows = []
    for part in spec['parts']:
        data = (root / part['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == part['sha256'], part['path']
        batch = [json.loads(line) for line in data.decode().splitlines()]
        assert len(batch) == part['records']
        rows.extend(batch)
    assert len(rows) == spec['records']
    obj[spec['array_key']] = rows
    fmt = spec['serialization']
    content = json.dumps(obj, ensure_ascii=fmt['ensure_ascii'], separators=tuple(fmt['separators']))
    if fmt['trailing_newline']:
        content += '\n'
    data = content.encode()
    assert len(data) == spec['original_bytes']
    assert hashlib.sha256(data).hexdigest() == spec['original_sha256']
    destination = root / spec['destination']
    destination.write_bytes(data)
    print(f"Restored and SHA256 verified: {spec['destination']}")
