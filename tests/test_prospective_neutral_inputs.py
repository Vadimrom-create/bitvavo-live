import copy,io,tempfile,unittest,urllib.error
from pathlib import Path
from unittest.mock import Mock,patch
from research.common import utc,atomic_json
from scripts.prepare_v3_universe import prepare

class NeutralInputTests(unittest.TestCase):
    def test_fresh_neutral_copy_and_stale_isolated_recompute(self):
        fresh={'generated_at_utc':utc(100),'rows':[{'market':'CT-EUR'}]};scanner=Mock()
        r=prepare(fresh,scanner,101);scanner.assert_not_called();self.assertEqual(r['rows'],fresh['rows'])
        before=Path.cwd()
        def scan():
            self.assertNotEqual(Path.cwd(),before)
            atomic_json('production_universe_snapshot.json',{'generated_at_utc':utc(1000),'rows':[{'market':'NEW-EUR'}]})
        r=prepare(fresh,scan,1000);self.assertEqual(Path.cwd(),before);self.assertEqual(r['rows'][0]['market'],'NEW-EUR')
        self.assertFalse(r['measurement_provenance']['sender_called'])
