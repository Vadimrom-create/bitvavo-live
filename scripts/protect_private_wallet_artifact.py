#!/usr/bin/env python3
"""Fail-closed privacy boundary for private wallet GitHub Actions artifacts.

Public repositories may publish only authenticated ciphertext. Private
repositories may publish the existing plaintext summary for connected readers.
This script never prints amounts, balances, symbols, or ciphertext.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from cryptography.fernet import Fernet
from research.common import atomic_json

SUMMARY = Path("wallet_private_summary.json")
ENCRYPTED = Path("wallet_private_summary.enc.json")


def protect(summary_path=SUMMARY, encrypted_path=ENCRYPTED, *, repo_private=False, state_key=""):
    summary_path = Path(summary_path)
    encrypted_path = Path(encrypted_path)
    if not summary_path.is_file():
        raise RuntimeError("WALLET_SUMMARY_MISSING")
    # An unknown visibility must be treated as public.
    if repo_private is True:
        if encrypted_path.exists():
            encrypted_path.unlink()
        return "PRIVATE_REPO_PLAINTEXT_ARTIFACT"

    if not state_key:
        raise RuntimeError("ENCRYPTION_KEY_REQUIRED_PUBLIC_REPO")
    cipher = Fernet(state_key.encode())  # raises for malformed key
    original = summary_path.read_bytes()
    payload = json.loads(original)
    if not isinstance(payload, dict) or not isinstance(payload.get("positions"), list):
        raise RuntimeError("INVALID_PRIVATE_WALLET_PAYLOAD")
    token = cipher.encrypt(original)
    envelope = {
        "schema": "wallet_summary_encrypted_fernet_v1",
        "confidential": True,
        "ciphertext": token.decode("ascii"),
    }
    atomic_json(encrypted_path, envelope)
    # Verify integrity and round-trip before deleting the source.
    restored = cipher.decrypt(json.loads(encrypted_path.read_text())["ciphertext"].encode())
    if restored != original:
        encrypted_path.unlink(missing_ok=True)
        raise RuntimeError("WALLET_ENCRYPTION_VERIFICATION_FAILED")
    summary_path.unlink()
    return "PUBLIC_REPO_ENCRYPTED_ARTIFACT"


def main():
    private = os.getenv("GITHUB_REPOSITORY_IS_PRIVATE", "").strip().lower() == "true"
    result = protect(repo_private=private, state_key=os.getenv("POSITION_STATE_KEY", ""))
    print("WALLET_ARTIFACT_PRIVACY", result)


if __name__ == "__main__":
    main()
