#!/usr/bin/env python3
"""Run unittest cases AND existing plain test_* functions (no pytest dependency)."""
import importlib,inspect,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))

def main():
    loader=unittest.TestLoader();suite=loader.discover(str(ROOT/'tests'))
    plain=unittest.TestSuite();fixture_delegated=[];pytest_only_modules=[]
    for path in sorted((ROOT/'tests').rglob('test_*.py')):
        name='.'.join(path.relative_to(ROOT/'tests').with_suffix('').parts)
        try:
            module=importlib.import_module(name)
        except ModuleNotFoundError as exc:
            if exc.name != 'pytest' or 'import pytest' not in path.read_text():
                raise
            # This CI intentionally has no pytest; a dedicated workflow executes
            # the pytest-only module with pytest installed and reports its result.
            pytest_only_modules.append(name)
            continue
        for attr,fn in inspect.getmembers(module,inspect.isfunction):
            if attr.startswith('test_') and fn.__module__==name:
                if inspect.signature(fn).parameters:
                    fixture_delegated.append(name+'.'+attr)
                    continue  # pytest-only fixtures run in dedicated pytest workflow CI
                plain.addTest(unittest.FunctionTestCase(fn,description=name+'.'+attr))
    print('Discovery:',suite.countTestCases(),'unittest cases +',plain.countTestCases(),'function tests;',len(fixture_delegated),'pytest-fixture tests and',len(pytest_only_modules),'pytest-only modules delegated to pytest CI',flush=True)
    suite.addTest(plain);result=unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
