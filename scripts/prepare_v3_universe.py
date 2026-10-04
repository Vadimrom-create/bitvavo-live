#!/usr/bin/env python3
"""Provide fresh neutral inputs locally to V3; no publication of production state."""
import copy,json,os,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from research.common import atomic_json,read_json,timestamp,utc
from scripts.production_scan import run as neutral_scan
DEST=ROOT/'runtime/prospective_inputs/v3_universe.json'

def prepare(source,scan,now):
    try:age=now-timestamp(source.get('generated_at_utc'))
    except (ValueError,TypeError):age=None
    if age is not None and 0<=age<=300 and source.get('rows'):
        doc=copy.deepcopy(source);mode='FRESH_PUBLISHED_NEUTRAL_INPUT'
    else:
        # The unchanged detector runs in an isolated directory. Its generated
        # candidate/status files are discarded; the real sender is never called.
        prior=Path.cwd()
        with tempfile.TemporaryDirectory(prefix='solaire-neutral-shadow-') as tmp:
            try:
                os.chdir(tmp);scan();doc=read_json('production_universe_snapshot.json',{})
            finally:os.chdir(prior)
        if not doc.get('rows'):raise RuntimeError('FRESH_NEUTRAL_INPUT_UNAVAILABLE')
        mode='FRESH_NEUTRAL_RECOMPUTED_FOR_RESEARCH_ONLY'
    doc['measurement_provenance']={'mode':mode,'original_published_age_seconds':age,
        'production_state_written':False,'sender_called':False,'prepared_at_utc':utc()}
    return doc

def main():
    try:doc=prepare(read_json(ROOT/'production_universe_snapshot.json',{}),neutral_scan,time.time());code=0
    except (ValueError,RuntimeError,OSError) as exc:
        doc={'generated_at_utc':utc(),'rows':[],'status':'DATA_UNAVAILABLE','reason':str(exc)};code=1
    atomic_json(DEST,doc)
    print(json.dumps({'status':doc.get('status','OK'),'rows':len(doc.get('rows',[])),'provenance':doc.get('measurement_provenance')}))
    return code
if __name__=='__main__':raise SystemExit(main())
