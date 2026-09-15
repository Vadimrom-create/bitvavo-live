import copy
import tempfile
import unittest
from pathlib import Path
from research.common import atomic_json
from research.history import connect, ingest, rebuild
from unittest.mock import patch


def scan(sid='a',ts=600,close=100):
    return {'scan_id':sid,'scan_ts':ts,'scan_at_utc':'2026-09-11T00:00:00+00:00','data_policy':'CORRECTED_INPUTS_V1',
            'policy':'V4','observations':[], 'candles_5m':{'AAA-EUR':[{'t':0,'o':100,'h':110,'l':90,'c':close,'v':1}]}}


class IndexTests(unittest.TestCase):
    def test_reverse_ingestion_uses_recorded_first_source_not_ingestion_order(self):
        a,b=scan(),scan('b',900,105)
        result=[]
        for items in ([a,b],[b,a,b]):
            db=connect()
            for item in items: ingest(db,item)
            result.append([tuple(r) for r in db.execute('SELECT * FROM candles ORDER BY market,t')])
        self.assertEqual(result[0],result[1])

    def test_changed_id_and_mixed_data_policy_fail_closed(self):
        db=connect();ingest(db,scan());bad=scan();bad['scan_ts']=700
        with self.assertRaisesRegex(ValueError,'COLLISION'): ingest(db,bad)
        bad=scan('b');bad['data_policy']='LEGACY_OBSERVED_V1'
        with self.assertRaisesRegex(ValueError,'DATA_POLICY'): ingest(db,bad)

    def test_incremental_restart_and_full_rebuild_match_and_changed_bytes_refused(self):
        from research.history import refresh_index
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'journals';path=root/'2026-09-11/a.json.gz';atomic_json(path,scan())
            file=Path(d)/'index.sqlite3';db=connect(file);refresh_index(root,db);db.close()
            atomic_json(root/'2026-09-11/b.json.gz',scan('b',900,105))
            db=connect(file);refresh_index(root,db);whole=rebuild(root,connect())
            for table in ('scans','candles','observations','journal_integrity'):
                self.assertEqual([tuple(r) for r in db.execute('SELECT * FROM '+table+' ORDER BY 1')],
                                 [tuple(r) for r in whole.execute('SELECT * FROM '+table+' ORDER BY 1')])
            atomic_json(path,scan(close=102))
            with self.assertRaisesRegex(ValueError,'JOURNAL_CHANGED'): refresh_index(root,db)

    def test_corrupt_derived_index_rebuild_preserves_journal_bytes(self):
        from research.history import open_index
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'journals';p=root/'2026-09-11/a.json.gz';atomic_json(p,scan());before=p.read_bytes()
            cache=Path(d)/'index.sqlite3';cache.write_bytes(b'broken')
            db=open_index(cache,root)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM scans').fetchone()[0],1)
            self.assertEqual(p.read_bytes(),before)

    def test_bounded_prospection_state_matches_recurrence_and_keeps_late_bar(self):
        from research.cycle_state import advance, recurrence
        old={'market':'AAA-EUR','category':'PRE-IGNITION'}
        state,delta=advance({},[old],scan()['candles_5m'],600)
        self.assertFalse(recurrence(state,'AAA-EUR',660,'IGNITION')['recurrent'])
        self.assertTrue(recurrence(state,'AAA-EUR',1800,'IGNITION')['recurrent'])
        late=copy.deepcopy(scan()['candles_5m']['AAA-EUR'][0]);late['t']=-300000
        _,delta=advance(state,[old],{'AAA-EUR':[late,*scan()['candles_5m']['AAA-EUR']]},1800)
        self.assertEqual([b['t'] for b in delta['AAA-EUR']],[-300000])

    def test_removed_source_cannot_leave_a_silently_different_index(self):
        from research.history import refresh_index
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);p=root/'2026-09-11/a.json.gz';atomic_json(p,scan())
            db=connect();refresh_index(root,db);p.unlink()
            with self.assertRaisesRegex(ValueError,'JOURNAL_REMOVED'): refresh_index(root,db)

    def test_ingestion_failure_rolls_back_and_restart_matches(self):
        bad=scan();bad['observations']=[{'market':'AAA-EUR'}]
        db=connect()
        with self.assertRaises(KeyError): ingest(db,bad)
        self.assertEqual(db.execute('SELECT COUNT(*) FROM scans').fetchone()[0],0)
        ingest(db,scan())
        self.assertEqual(db.execute('SELECT COUNT(*) FROM journal_integrity').fetchone()[0],1)

    def test_cycle_state_keeps_temporarily_absent_market_and_rebuilds(self):
        from research.cycle_state import advance, recurrence, load_cycle_state
        first=scan();first['observations']=[{'market':'AAA-EUR','category':'PRE-IGNITION'}]
        state,_=advance({},first['observations'],first['candles_5m'],600)
        state,_=advance(state,[],{},900)
        self.assertTrue(recurrence(state,'AAA-EUR',1800,'IGNITION')['recurrent'])
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'journals';atomic_json(root/'2026-09-11/a.json.gz',first)
            rebuilt=load_cycle_state(Path(d)/'missing.json',root,1800)
            self.assertEqual(recurrence(rebuilt,'AAA-EUR',1800,'IGNITION'),recurrence(state,'AAA-EUR',1800,'IGNITION'))
