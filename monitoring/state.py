"""Authenticated encryption of private observations and delivery markers."""
from __future__ import annotations

import json
from pathlib import Path

from cryptography.fernet import Fernet

from research.common import atomic_json, read_json


def load_state(path, key):
    cipher = Fernet(key.encode())  # Validate even before the first alert.
    if not Path(path).exists():
        return {'positions': {}, 'deliveries': {}}
    envelope = read_json(path)
    # Authentication failures are fatal, never interpreted as an empty ledger.
    return json.loads(cipher.decrypt(envelope['ciphertext'].encode()))


def save_state(path, key, state):
    clear = json.dumps(state, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    atomic_json(path, {'schema_version': 1, 'ciphertext': Fernet(key.encode()).encrypt(clear).decode()})
