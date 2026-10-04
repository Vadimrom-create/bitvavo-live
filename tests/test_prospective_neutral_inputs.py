import copy,io,tempfile,unittest,urllib.error
from pathlib import Path
from unittest.mock import Mock,patch
from research.common import utc,atomic_json
from scripts.prepare_v3_universe import prepare

class NeutralInputTests(unittest.TestCase):
    def test_fresh_neutral_copy_and_stale_isolated_recompute(self):
        fresh={'generated_at_utc':utc(100),'rows':[{'market':'CT-EUR'}]};scanner=Mock()
        r,_,_=prepare(fresh,scanner,101,{'generated_at_utc':utc(100),'tracking':[],'watch':[]});scanner.assert_not_called();self.assertEqual(r['rows'],fresh['rows'])
        before=Path.cwd()
        def scan():
            self.assertNotEqual(Path.cwd(),before)
            atomic_json('production_universe_snapshot.json',{'generated_at_utc':utc(1000),'rows':[{'market':'NEW-EUR'}]})
        r,_,_=prepare(fresh,scan,1000);self.assertEqual(Path.cwd(),before);self.assertEqual(r['rows'][0]['market'],'NEW-EUR')
        self.assertFalse(r['measurement_provenance']['sender_called'])

    def test_all_prospective_consumers_share_the_selected_neutral_input(self):
        import os,subprocess,sys
        probe="from scripts import solaire_v3_shadow as a,solaire_v31_shadow as b,solaire_policy_challengers as c;print(a.UNIVERSE,b.UNIVERSE,c.UNIVERSE)"
        env={**os.environ,'SOLAIRE_V3_UNIVERSE_PATH':'runtime/prospective_inputs/v3_universe.json'}
        paths=subprocess.check_output([sys.executable,'-c',probe],env=env,text=True).split()
        self.assertEqual(paths,[env['SOLAIRE_V3_UNIVERSE_PATH']]*3)
        workflow=Path('.github/workflows/solaire_prospective_shadows.yml').read_text()
        self.assertEqual(workflow.count('SOLAIRE_V3_UNIVERSE_PATH: runtime/prospective_inputs/v3_universe.json'),3)
