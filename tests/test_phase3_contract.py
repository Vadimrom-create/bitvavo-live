"""Immutable starting references and separate methodological identities."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReferenceContractTests(unittest.TestCase):
    def test_protected_starting_objects_are_unchanged(self):
        reference = json.loads((ROOT / 'config/phase3_reference.json').read_text())
        for name, expected in reference['protected_blobs'].items():
            data = (ROOT / name).read_bytes()
            digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            self.assertEqual(digest, expected, name)

    def test_policy_dimensions_are_distinct_and_shadow(self):
        from research.policies import identities, CANDIDATE
        ids = identities(decision_policy=CANDIDATE)
        for key in ('data_policy', 'decision_policy', 'execution_policy', 'evaluation_policy'):
            self.assertIsInstance(ids[key], str)
            self.assertTrue(ids[key])
        self.assertEqual(len(set(ids.values())), 4)
        self.assertIn('SHADOW', ids['decision_policy'])


if __name__ == '__main__':
    unittest.main()
