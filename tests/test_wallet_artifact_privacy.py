"""Safety regressions for public GitHub wallet artifact publication."""
import json
import tempfile
import unittest
from pathlib import Path

from cryptography.fernet import Fernet

from scripts.protect_private_wallet_artifact import protect


class WalletArtifactPrivacyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.plain = Path(self.tmp.name) / "wallet_private_summary.json"
        self.enc = Path(self.tmp.name) / "wallet_private_summary.enc.json"
        self.data = {
            "cash_eur": 2109.30,
            "wallet_value_eur": 2349.29,
            "positions": [{"market": "FIL-EUR", "quantity": 148.22134, "pru_eur": 1.01355}],
        }
        self.plain.write_text(json.dumps(self.data))
        self.key = Fernet.generate_key().decode()

    def test_public_repo_encrypts_and_erases_plaintext(self):
        result = protect(self.plain, self.enc, repo_private=False, state_key=self.key)
        self.assertEqual(result, "PUBLIC_REPO_ENCRYPTED_ARTIFACT")
        self.assertFalse(self.plain.exists())
        content = self.enc.read_text()
        for sensitive in ("FIL-EUR", "148.22134", "2109.3"):
            self.assertNotIn(sensitive, content)
        envelope = json.loads(content)
        decoded = Fernet(self.key.encode()).decrypt(envelope["ciphertext"].encode())
        self.assertEqual(json.loads(decoded), self.data)

    def test_private_repo_may_publish_unencrypted(self):
        result = protect(self.plain, self.enc, repo_private=True, state_key="")
        self.assertEqual(result, "PRIVATE_REPO_PLAINTEXT_ARTIFACT")
        self.assertTrue(self.plain.exists())
        self.assertFalse(self.enc.exists())

    def test_public_repo_without_key_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "ENCRYPTION_KEY_REQUIRED"):
            protect(self.plain, self.enc, repo_private=False, state_key="")
        self.assertTrue(self.plain.exists())
        self.assertFalse(self.enc.exists())

    def test_public_repo_with_invalid_key_fails_closed(self):
        with self.assertRaises(ValueError):
            protect(self.plain, self.enc, repo_private=False, state_key="bad-key")
        self.assertTrue(self.plain.exists())
        self.assertFalse(self.enc.exists())

    def test_public_invalid_wallet_never_uploads(self):
        self.plain.write_text(json.dumps({"positions": "INVALID"}))
        with self.assertRaisesRegex(RuntimeError, "INVALID_PRIVATE_WALLET"):
            protect(self.plain, self.enc, repo_private=False, state_key=self.key)
        self.assertFalse(self.enc.exists())


if __name__ == "__main__":
    unittest.main()
