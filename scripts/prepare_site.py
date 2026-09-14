#!/usr/bin/env python3
"""Render only files identified by their producer's manifest."""
from pathlib import Path
import shutil
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from research.common import read_json
from research.publication import file_hash
from scripts.prepare_publication import PUBLIC_FILES


def run():
    site=Path('_site');site.mkdir(exist_ok=True)
    manifest=read_json('scan_manifest.json')
    names=set(PUBLIC_FILES)|{'decision_layer.json','decision_layer.md','decision_layer_v2.json','decision_layer_v2.md','shadow_status.json'}
    for name,entry in manifest['outputs'].items():
        if name not in names: continue
        if file_hash(name)!=entry['sha256']: raise ValueError('SITE_OUTPUT_MISMATCH')
        shutil.copy2(name,site/name)
    shutil.copy2('scan_manifest.json',site/'scan_manifest.json')
    links=[('v5_report.md','Dernier scan et plans théoriques'),('v4_watch.txt','Décisions V4'),
           ('decision_layer.md','DL-V1 shadow'),('decision_layer_v2.md','DL-V2 Opportunity shadow'),
           ('market_control_current.json','Présence dans les listes courantes'),('pipeline_health.json','Qualité et fraîcheur'),
           ('scan_manifest.json','Identité du scan et des sorties')]
    # The historical producer owns its own snapshot; never label it as this scan.
    source=Path('../scan-data')
    evaluation=read_json(source/'evaluation_manifest.json',{})
    if evaluation:
        for name,sha in evaluation.get('outputs',{}).items():
            if name not in {'evaluation.json','comparison_report.json','market_control_history.json'}: continue
            if file_hash(source/name)!=sha: raise ValueError('SITE_EVALUATION_MISMATCH')
            shutil.copy2(source/name,site/name)
        shutil.copy2(source/'evaluation_manifest.json',site/'evaluation_manifest.json')
        links.extend([('evaluation.json','Évaluation séparée — sa date et son manifeste font référence'),
                      ('market_control_history.json','Contrôle du journal historique')])
    html='<!doctype html><html lang="fr"><meta charset="utf-8"><title>Bitvavo — suivi</title><h1>V4 et lectures shadow</h1>'
    html+='<p>DL-V2 reste expérimentale. Aucun ordre automatique. Aucune supériorité démontrée.</p>'
    html+=''.join('<p><a href="'+name+'">'+label+'</a></p>' for name,label in links if (site/name).exists())
    (site/'index.html').write_text(html+'</html>',encoding='utf-8')


if __name__=='__main__': run()
