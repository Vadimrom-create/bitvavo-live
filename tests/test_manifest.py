import copy
from pathlib import Path
import tempfile
import unittest
from research.common import atomic_json, read_json, utc


class ManifestTests(unittest.TestCase):
    def bundle(self, root):
        from research.publication import build_manifest
        from research.policies import identities
        payload={**identities(),'scan_id':'s1','generated_at_utc':utc(1000),'watch':[]}
        scan={**identities(),'scan_id':'s1','input_cutoff_at_utc':utc(1000),'policy_ready_at':utc(1000),
              'code_commit':'a'*40,'baseline_output':{'watch':[]},'health':{'status':'OK'}}
        atomic_json(root/'alert_candidates.json',payload)
        atomic_json(root/'v4_watch.json',scan['baseline_output'])
        replay={'reference_equals_instrumented':True,'reference_equals_recorded_live':True}
        manifest=build_manifest(scan,replay,['alert_candidates.json','v4_watch.json'],root)
        return payload,manifest

    def test_buy_requires_coherent_fresh_v4_and_exact_payload(self):
        from research.publication import validate_buy_bundle
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);payload,manifest=self.bundle(root)
            self.assertTrue(validate_buy_bundle(payload,manifest,1001,root)['ok'])
            for kind in ('wrong_scan','old','wrong_policy','missing_replay','changed_payload','missing_file'):
                p,m=copy.deepcopy(payload),copy.deepcopy(manifest);now=1001
                if kind=='wrong_scan': p['scan_id']='s2'
                if kind=='old': now=2000
                if kind=='wrong_policy': m['decision_policy']='DL_V2_OPPORTUNITY_BASELINE_SHADOW'
                if kind=='missing_replay': m['replay']={}
                if kind=='changed_payload': p['watch']=[{'market':'BAD-EUR'}]
                if kind=='missing_file': (root/'alert_candidates.json').unlink()
                with self.subTest(kind=kind): self.assertFalse(validate_buy_bundle(p,m,now,root)['ok'])

    def test_manifest_refuses_wrong_baseline_and_failed_replay(self):
        from research.publication import build_manifest
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);_,m=self.bundle(root)
            scan={**m,'baseline_output':{'watch':[{'market':'OTHER-EUR'}]}}
            with self.assertRaisesRegex(ValueError,'BASELINE_OUTPUT'): build_manifest(scan,m['replay'],['v4_watch.json'],root)
            with self.assertRaisesRegex(ValueError,'REPLAY_REQUIRED'): build_manifest(scan,{},['v4_watch.json'],root)

    def test_output_owners_do_not_overlap_and_old_journals_have_no_writer(self):
        from scripts.publish_data import OWNERS
        sets=[set(s) for s in OWNERS.values()]
        for i,a in enumerate(sets):
            for b in sets[i+1:]: self.assertFalse(a&b)
        all_files=set.union(*sets)
        self.assertNotIn('history',all_files);self.assertNotIn('decision_history',all_files)

    def test_receipt_bound_to_manifest_and_cycle_does_not_rewrite_readiness(self):
        from research.publication import apply_receipt
        from research.input_contract import digest
        cycle={'scan_id':'s1','data_policy':'D','policies':{'V4':{'native':{'policy_ready_at':1000}}}}
        receipt={'scan_id':'s1','data_policy':'D','comparison_sha256':digest(cycle),
                 'publication_confirmed_at':1010,'publication_started_at':1005,'status':'PUBLISHED'}
        result=apply_receipt(cycle,receipt)
        self.assertEqual(result['policies']['V4']['native']['published_at'],1010)
        self.assertEqual(cycle['policies']['V4']['native'],{'policy_ready_at':1000})
        receipt['comparison_sha256']='wrong'
        with self.assertRaisesRegex(ValueError,'RECEIPT'): apply_receipt(cycle,receipt)
