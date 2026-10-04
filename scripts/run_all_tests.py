#!/usr/bin/env python3
"""Run unittest cases AND existing plain test_* functions (no pytest dependency)."""
import importlib,inspect,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))

def main():
    loader=unittest.TestLoader();suite=loader.discover(str(ROOT/'tests'))
    plain=unittest.TestSuite()
    for path in sorted((ROOT/'tests').rglob('test_*.py')):
        name='.'.join(path.relative_to(ROOT/'tests').with_suffix('').parts);module=importlib.import_module(name)
        for attr,fn in inspect.getmembers(module,inspect.isfunction):
            if attr.startswith('test_') and fn.__module__==name:
                if inspect.signature(fn).parameters:raise RuntimeError('Unsupported fixture test:'+name+'.'+attr)
                plain.addTest(unittest.FunctionTestCase(fn,description=name+'.'+attr))
    print('Discovery:',suite.countTestCases(),'unittest cases +',plain.countTestCases(),'function tests',flush=True)
    suite.addTest(plain);result=unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
