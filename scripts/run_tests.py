#!/usr/bin/env python3
"""Independent CI gates; shadow imports never enter the monitoring gate."""
import argparse
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'tests'))
GROUPS = {'monitoring': {'test_positions', 'test_monitor_isolation', 'test_publication'},
          'executor': {'test_executor_safety'}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('suite', choices=['monitoring', 'executor', 'data', 'shadow', 'all'])
    args = parser.parse_args()
    suite = unittest.TestSuite()
    for file in sorted((ROOT/'tests').glob('test_*.py')):
        name = file.stem
        group = next((g for g, names in GROUPS.items() if name in names),
                     'shadow' if name.startswith(('test_decision_layer', 'test_comparison', 'test_prospective')) else 'data')
        if args.suite in ('all', group):
            suite.addTests(unittest.defaultTestLoader.loadTestsFromName(name))
    return not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


if __name__ == '__main__':
    raise SystemExit(main())
