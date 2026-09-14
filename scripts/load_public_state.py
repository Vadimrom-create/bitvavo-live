#!/usr/bin/env python3
"""Read a current data checkout into immutable code, copying only named data."""
import argparse
from pathlib import Path
import shutil
import subprocess
import os

STATE=['scan_history.json','signal_log.json','v4_history.json','v4_signal_log.json','v4_trend_cache.json','v4_stability_state.json','policy_state']
JOURNALS=['history','history_corrected','history_legacy_diagnostics','comparison_history','publication_history','scan_attempts']


def load(source, target='.', owner='prospection'):
    source,target=Path(source).resolve(),Path(target).resolve()
    names=STATE+['history_corrected','history_legacy_diagnostics'] if owner=='prospection' else JOURNALS
    before=subprocess.check_output(['git','-C',str(target),'rev-parse','HEAD'],text=True).strip()
    for name in names:
        src,dst=source/name,target/name
        if not src.exists(): continue
        if src.is_symlink(): raise ValueError('DATA_SYMLINK_REFUSED')
        if src.is_dir():
            for p in src.rglob('*'):
                if p.is_symlink(): raise ValueError('DATA_SYMLINK_REFUSED')
                q=dst/p.relative_to(src)
                if name in JOURNALS and p.is_file() and q.exists() and p.read_bytes()!=q.read_bytes():
                    raise ValueError('HISTORICAL_DATA_DIVERGENCE')
            shutil.copytree(src,dst,dirs_exist_ok=True)
        else:
            if src.is_symlink(): raise ValueError('DATA_SYMLINK_REFUSED')
            shutil.copy2(src,dst)
    after=subprocess.check_output(['git','-C',str(target),'rev-parse','HEAD'],text=True).strip()
    if before!=after: raise ValueError('CODE_REVISION_CHANGED')
    base=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
    if os.getenv('GITHUB_ENV'):
        with open(os.environ['GITHUB_ENV'],'a') as f: f.write('PUBLISH_BASE_SHA='+base+'\n')
    return base


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--owner',choices=['prospection','evaluation'],required=True)
    a=p.parse_args();load(a.source,owner=a.owner)
