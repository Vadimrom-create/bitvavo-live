#!/usr/bin/env python3
"""Public pipeline plus sidecar telemetry; no publisher, pilot or alert sender.

Run in an expendable checkout: pipeline writes its ordinary scan outputs.
"""
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from research.capacity_audit import Audit
from research.common import atomic_json
from research.input_contract import code_revision


def main():
    import pipeline
    audit, start, code = Audit(), time.time(), None
    try:
        with audit.observe():
            code = pipeline.run('CORRECTED_INPUTS_V1')
        return code
    finally:
        result = audit.result()
        result.update(code_commit=code_revision(), started_epoch=start, finished_epoch=time.time(),
                      duration_seconds=time.time()-start, pipeline_exit_code=code)
        atomic_json('runtime/capacity-audit.json.gz', result)
        print('CAPACITY_AUDIT', __import__('json').dumps(result['summary']), flush=True)


if __name__ == '__main__':
    raise SystemExit(main())
