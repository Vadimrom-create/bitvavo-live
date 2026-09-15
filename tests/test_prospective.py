"""Prospective enrollment, descriptive sizing and future freeze boundaries."""
import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from research.common import atomic_json, read_json
from research.input_contract import digest


class ProspectiveTests(unittest.TestCase):
    def test_failed_report_cannot_republish_stale_report(self):
        from scripts.run_prospective import report_and_publish
        from scripts.publish_data import EVALUATION_FILES
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            atomic_json(root/'prospective_report.json',{'report_id':'old'})
            with patch('scripts.run_prospective.report',side_effect=ValueError('evaluation failed')), \
                    patch('scripts.publish_data.publish') as publish:
                with self.assertRaisesRegex(ValueError,'evaluation failed'): report_and_publish(root)
                publish.assert_not_called()
            self.assertEqual(read_json(root/'prospective_report.json'),{'report_id':'old'})
        self.assertNotIn('prospective_report.json',EVALUATION_FILES)
        self.assertNotIn('prospective_reports',EVALUATION_FILES)
        workflow=Path('.github/workflows/evaluate.yml').read_text()
        self.assertIn("if: always() && steps.pilot_report.outcome == 'success'",workflow)

    def test_publication_binds_current_report_and_exact_archive(self):
        from scripts.run_prospective import report_and_publish
        from research.publication import immutable_json
        result={'status':'TECHNICAL_PILOT_DEVELOPMENT_ONLY','generated_at':100}
        rid=digest(result);archive='prospective_reports/'+rid+'.json.gz'
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            immutable_json(root/archive,result)
            atomic_json(root/'prospective_report.json',{'report_id':rid,**result})
            with patch('scripts.run_prospective.report',return_value=result), \
                    patch('scripts.publish_data.publish') as publish:
                self.assertEqual(report_and_publish(root),result)
                self.assertEqual(publish.call_args.args[0],['prospective_report.json',archive])
                atomic_json(root/'prospective_report.json',{'report_id':'old'})
                publish.reset_mock()
                with self.assertRaisesRegex(ValueError,'CURRENT_PILOT_REPORT_MISMATCH'): report_and_publish(root)
                publish.assert_not_called()

    def test_pilot_refuses_retrospective_synthetic_and_wrong_version(self):
        from research.prospective import validate_enrollment
        session={'started_at':100,'code_fingerprint':'f','data_policy':'CORRECTED_INPUTS_V1'}
        code={'fingerprint':'f','commit':'a'*40}
        scan={'scan_ts':101,'input_cutoff_at_utc':102,'source':'live','stage':'TECHNICAL_PILOT',
              'data_policy':'CORRECTED_INPUTS_V1','code_commit':'a'*40}
        validate_enrollment(session,scan,code,103)
        for key,value in [('scan_ts',99),('source','synthetic'),('stage','DEVELOPMENT_REPLAY'),
                          ('code_commit','b'*40),('input_cutoff_at_utc',104)]:
            bad={**scan,key:value}
            with self.subTest(key=key),self.assertRaises(ValueError): validate_enrollment(session,bad,code,103)

    def test_metrics_deduplicate_and_preserve_missing_labels_and_delivery(self):
        from research.prospective import sizing_metrics
        from test_comparison import ComparisonTests
        c=ComparisonTests().cycles();c['policies']['DL2']['selected']=[]
        labels={('s1','AAA-EUR'):{'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}}
        a=sizing_metrics([c],labels,c['cutoff'],c['cutoff']+14400,[14400,86400])
        self.assertEqual(a,sizing_metrics([c,c],labels,c['cutoff'],c['cutoff']+14400,[14400,86400]))
        contrast=a['contrasts']['DL2_minus_V4_common']
        self.assertEqual(contrast['discordant_pairs'],1)
        self.assertEqual(contrast['paired_differences'],[-1])
        self.assertIsNone(contrast['sample_variance'])
        self.assertFalse(a['held_out_performed']);self.assertIsNone(a['recommended_sample_size'])
        self.assertEqual(sizing_metrics([c],{},c['cutoff'],c['cutoff']+14400,[14400])['observable_label_fraction'],0)
        c['policies']['V4']['native']['publication_status']='UNKNOWN'
        b=sizing_metrics([c],labels,c['cutoff'],c['cutoff']+14400,[14400])
        self.assertEqual(b['contrasts']['DL2_minus_V4_native']['unknown_pairs'],1)

    def protocol(self):
        return {'schema_version':1,'primary_contrast':'DL2_minus_V4_common','primary_metric':'recall_at_3',
                'useful_effect':.04,'error_rate':.04,'precision_target':.03,
                'multiplicity':'primary_only','block_seconds':86400,'sensitivity_block_seconds':[14400,86400],
                'planned_days':35,'minimum_informative_pairs':200,'embargo_seconds':14400,
                'analysis_rule':'fixed_calendar_then_information_gate','justification':{
                    k:'Example test justification, not scientific evidence' for k in
                    ('effect','error','precision','multiplicity','blocks','duration','sample_size','costs_and_delays')},
                'cost_delay_sensitivity':{'fee_multipliers':[1,2],'delay_seconds':[0,300]},
                'pilot_report_sha256':'p','validation_start':100000}

    def test_freeze_rejects_unset_protocol_bad_dates_and_short_validation(self):
        from research.prospective import validate_protocol
        p=self.protocol();validate_protocol(p,50000,50000,'p')
        for key,value in [('useful_effect',None),('planned_days',29),('embargo_seconds',1),
                          ('validation_start',51000),('pilot_report_sha256','wrong'),('minimum_informative_pairs',0),
                          ('primary_contrast','best_historical_winner')]:
            with self.subTest(key=key),self.assertRaises(ValueError): validate_protocol({**p,key:value},50000,50000,'p')

    def test_holdout_eligibility_enforces_version_future_boundary_and_purge(self):
        from research.prospective import holdout_eligibility
        frozen={'code_fingerprint':'a','validation_start':100000,'analysis_at':3000000,
                'embargo_seconds':14400,'last_development_cutoff':50000,'data_policy':'CORRECTED_INPUTS_V1'}
        scan={'code_commit':'c','scan_ts':100001,'input_cutoff_at_utc':100002,'source':'live','data_policy':'CORRECTED_INPUTS_V1'}
        scan.update(stage='HELD_OUT_FROZEN',freeze_id=digest(frozen))
        code={'fingerprint':'a','commit':'c'}
        self.assertTrue(holdout_eligibility(frozen,scan,code)['eligible'])
        for override in ({'code_fingerprint':'b'},{'validation_start':200000},{'last_development_cutoff':90000}):
            self.assertFalse(holdout_eligibility({**frozen,**override},scan,code)['eligible'])

    def test_public_state_snapshot_excludes_private_files(self):
        from research.prospective import public_bootstrap
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);atomic_json(root/'policy_state/CORRECTED_INPUTS_V1/v4_history.json',{'x':1})
            atomic_json(root/'position_alert_state.enc.json',{'secret':'NEVER_COPY'})
            result=public_bootstrap(root)
            self.assertEqual(set(result),{'policy_state/CORRECTED_INPUTS_V1/v4_history.json'})
            self.assertNotIn('NEVER_COPY',str(result))

    def test_code_identity_detects_uncommitted_policy_change(self):
        from research.prospective import code_identity
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for args in [('init',),('config','user.name','Test'),('config','user.email','test@example.invalid')]:
                subprocess.run(['git','-C',d,*args],check=True,capture_output=True)
            (root/'policy.py').write_text('x=1\n')
            subprocess.run(['git','-C',d,'add','policy.py'],check=True)
            subprocess.run(['git','-C',d,'commit','-m','fixture'],check=True,capture_output=True)
            first=code_identity(root);self.assertTrue(first['fingerprint'])
            (root/'policy.py').write_text('x=2\n')
            with self.assertRaisesRegex(ValueError,'UNCOMMITTED'):code_identity(root)

    def test_pilot_lifecycle_no_data_then_record_restart_and_report(self):
        from scripts import run_prospective as runner
        from research.policies import identities
        from research.common import utc
        code={'commit':'a'*40,'fingerprint':'f','blobs':{'policy.py':'b'}}
        with tempfile.TemporaryDirectory() as d,patch.object(runner,'code_identity',return_value=code):
            root=Path(d)
            self.assertEqual(runner.report(root,100)['status'],'NO_PILOT_STARTED')
            session=runner.start(root,100)
            self.assertEqual(runner.start(root,101),session)
            empty=runner.report(root,101)['sessions'][session['session_id']]
            self.assertEqual(empty['enrolled_scan_count'],0)
            scan={**identities(),'scan_id':'s1','scan_ts':102,'input_cutoff_at_utc':103,'source':'live',
                  'stage':'TECHNICAL_PILOT','code_commit':code['commit'],'observations':[],
                  'policy':'V4_FROZEN_20260908','scan_at_utc':utc(102)}
            journal='history_corrected/1970-01-01/s1.json.gz'
            atomic_json(root/journal,scan)
            atomic_json(root/'runtime/current_scan.json',{'journal':journal,'scan_id':'s1'})
            before=(root/journal).read_bytes()
            enrollment=runner.record(root,104)
            self.assertEqual(runner.record(root,105),enrollment)
            result=runner.report(root,106)
            group=result['sessions'][session['session_id']]
            self.assertEqual(group['enrolled_scan_count'],1)
            self.assertEqual(group['missing_comparison_scans'],1)
            self.assertEqual(group['comparison_coverage'],0)
            self.assertFalse(result['held_out_performed'])
            self.assertEqual((root/journal).read_bytes(),before)
            # A failed scan publication remains explicit, never silently counts as no event.
            (root/journal).unlink()
            missing=runner.report(root,107)['sessions'][session['session_id']]
            self.assertEqual(missing['unavailable_sources'][0]['reason'],'SOURCE_NOT_PUBLISHED')
            self.assertEqual(missing['enrolled_scan_count'],1)

    def test_report_censors_immature_live_fixture_and_refuses_changed_journal(self):
        from scripts import run_prospective as runner
        from test_comparison import ComparisonTests
        from research.policies import identities
        from research.common import utc
        c=ComparisonTests().cycles();now=c['cutoff']
        code={'commit':'a'*40,'fingerprint':'f','blobs':{'policy.py':'b'}}
        with tempfile.TemporaryDirectory() as d,patch.object(runner,'code_identity',return_value=code):
            root=Path(d);session=runner.start(root,now-10)
            # Synthetic fixture of the live ingestion path; never written to real history.
            scan={**identities(),'scan_id':'s1','scan_ts':now,'input_cutoff_at_utc':now,'source':'live',
                  'stage':'TECHNICAL_PILOT','code_commit':code['commit'],'observations':[],
                  'policy':'V4_FROZEN_20260908','scan_at_utc':utc(now)}
            journal='history_corrected/'+utc(now)[:10]+'/s1.json.gz'
            cp='comparison_history/CORRECTED_INPUTS_V1/'+utc(now)[:10]+'/s1.json.gz'
            c['source_snapshot_sha256']=digest(scan)
            atomic_json(root/journal,scan);atomic_json(root/cp,c)
            atomic_json(root/'runtime/current_scan.json',{'journal':journal,'scan_id':'s1'})
            atomic_json(root/'runtime/current_comparison.json',{'journal':cp,'scan_id':'s1'})
            runner.record(root,now+1)
            group=runner.report(root,now+2)['sessions'][session['session_id']]
            self.assertEqual(group['metrics']['episode_count'],1)
            self.assertEqual(group['metrics']['observable_labels'],0)
            self.assertIsNone(group['metrics']['recommended_sample_size'])
            atomic_json(root/journal,{**scan,'changed':True})
            with self.assertRaisesRegex(ValueError,'JOURNAL_CHANGED'):runner.report(root,now+3)

    def test_old_code_cohort_is_not_reinterpreted_by_new_evaluator(self):
        from scripts import run_prospective as runner
        with tempfile.TemporaryDirectory() as d,patch.object(runner,'code_identity',return_value={'commit':'a','fingerprint':'f','blobs':{}}) as code:
            s=runner.start(d,100)
            code.return_value={'commit':'b','fingerprint':'g','blobs':{}}
            r=runner.report(d,101)
            self.assertEqual(r['sessions'][s['session_id']]['status'],'REQUIRES_ORIGINAL_EVALUATOR')

    def test_protocol_template_cannot_freeze_and_no_live_routes_added(self):
        from research.prospective import validate_protocol
        import ast
        root=Path(__file__).resolve().parents[1]
        template=read_json(root/'config/pilot_protocol_template.json')
        with self.assertRaises(ValueError):validate_protocol(template,100,100,'none')
        for p in [root/'pipeline.py',root/'scripts/send_useful_alert.py',*list((root/'monitoring').glob('*.py'))]:
            tree=ast.parse(p.read_text())
            imports=[n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]
            self.assertNotIn('research.prospective',imports)
        workflow=(root/'.github/workflows/update.yml').read_text()
        for step in workflow.split('      - name:'):
            if 'run_prospective.py' in step:
                self.assertIn('continue-on-error: true',step);self.assertIn('timeout-minutes:',step)
        self.assertNotIn('run_prospective.py freeze',workflow)

    def test_freeze_captures_exact_state_and_refuses_stale_evidence(self):
        from scripts import run_prospective as runner
        code={'commit':'a'*40,'fingerprint':'f','blobs':{'policy.py':'b'}}
        with tempfile.TemporaryDirectory() as d,patch.object(runner,'code_identity',return_value=code):
            root=Path(d);session=runner.start(root,100)
            sid=session['session_id'];sp='prospective_sessions/'+sid+'.json.gz'
            from research.publication import file_hash
            # Controlled protocol fixture; never evidence of a real completed pilot.
            evidence={'generated_at':50000,'evaluator_code':code,'sessions':{sid:{
                'enrolled_scan_count':2,'last_development_cutoff':49000,'code_fingerprint':'f',
                'metrics':{'contrasts':{'DL2_minus_V4_common':{'sample_variance':.5}}},
                'source_hashes':{sp:file_hash(root/sp)}}}}
            eid=digest(evidence);ep=root/'prospective_reports'/(eid+'.json.gz');atomic_json(ep,evidence)
            protocol={**self.protocol(),'session_id':sid,'pilot_report_sha256':eid}
            pp=root/'protocol.json';atomic_json(pp,protocol)
            atomic_json(root/'policy_state/CORRECTED_INPUTS_V1/v4_history.json',{'unchanged':True})
            frozen=runner.freeze(pp,ep,root,50001)
            self.assertEqual(frozen['stage'],'FROZEN_PROTOCOL_NOT_ACTIVATED')
            self.assertEqual(frozen['analysis_at'],100000+35*86400)
            self.assertEqual(frozen['bootstrap_sha256'],digest(frozen['bootstrap']))
            self.assertFalse(frozen['promotion_allowed'])
            self.assertEqual(len(list((root/'prospective_freezes').glob('*.json.gz'))),1)
            atomic_json(root/'prospective_observations'/sid/'new.json',{})
            with self.assertRaisesRegex(ValueError,'STALE'):runner.freeze(pp,ep,root,50002)

    def test_analysis_gate_waits_and_insufficient_information_stays_inconclusive(self):
        from research.prospective import analysis_gate
        frozen={'analysis_at':1000,'protocol':{'minimum_informative_pairs':200}}
        self.assertEqual(analysis_gate(frozen,999,10000)['status'],'WAIT_FOR_FIXED_ANALYSIS_DATE')
        self.assertEqual(analysis_gate(frozen,1001,199)['status'],'INCONCLUSIVE_INSUFFICIENT_INFORMATION')
        self.assertFalse(analysis_gate(frozen,1001,200)['promotion_allowed'])

    def test_time_blocks_pool_markets_without_inventing_independent_samples(self):
        from research.prospective import sizing_metrics
        from test_comparison import ComparisonTests
        base=ComparisonTests().cycles();cycles=[];labels={}
        for i in range(4):
            c=copy.deepcopy(base);c['scan_id']='s'+str(i);c['cutoff']+=i*14400
            c['observations']['BBB-EUR']=copy.deepcopy(c['observations']['AAA-EUR'])
            for p in c['policies'].values():
                p['selected']=['AAA-EUR','BBB-EUR'];p['native'].update(policy_ready_at=c['cutoff']+1,published_at=c['cutoff']+2)
            if i%2: c['policies']['DL2']['selected']=[]
            cycles.append(c)
            for m in c['observations']:labels[(c['scan_id'],m)]={'status':'COMPLETE','positive':True,'first_target_at':c['cutoff']+3600}
        result=sizing_metrics(cycles,labels,base['cutoff'],base['cutoff']+4*14400,[14400])
        c=result['contrasts']['DL2_minus_V4_common']['block_sensitivity']['14400']
        self.assertEqual(len(c['blocks']),4)
        self.assertTrue(all(b['n']==2 for b in c['blocks']))
        self.assertFalse(c['independence_assumed'])
        self.assertAlmostEqual(c['cross_market_correlations'][0]['correlation'],1)
