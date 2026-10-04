import ast,copy,hashlib,io,json,tempfile,unittest
from pathlib import Path
from contextlib import ExitStack,redirect_stdout
from unittest.mock import patch
from scripts import send_production_buy_alert as sender
from tests.test_multi_action_alerts import _validated

ROOT=Path(__file__).resolve().parents[1]
class NonRegressionTests(unittest.TestCase):
    def test_all_buy_gates_scores_risk_and_detector_identical_to_main(self):
        f=json.loads((ROOT/'tests/fixtures/phase_c_invariants.json').read_text())
        for p,h in f['files'].items():self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),h,p)
        mod=ast.parse((ROOT/'scripts/send_production_buy_alert.py').read_text())
        functions={n.name:ast.dump(n,include_attributes=False) for n in mod.body if isinstance(n,ast.FunctionDef)}
        for name,body in f['sender_functions'].items():self.assertEqual(functions[name],body,name)
        constants={n.targets[0].id:ast.dump(n.value,include_attributes=False) for n in mod.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        self.assertEqual(constants,f['constants'])
    def test_observer_disk_failure_changes_neither_email_nor_buy_plan(self):
        class Client:
            server_offset=0
            records=[]
            def __init__(self,**_):pass
            def get(self,path,**_):return [] if path=='/time' else [{'market':'CT-EUR','quote':'EUR','status':'trading'}]
        results=[]
        for disk_fails in (False,True):
            v=_validated('CT-EUR');v['row'].update(episode=2,episode_started_ts=100)
            state={'markets':{'CT-EUR':{'episode':2,'episode_started_ts':100}}};outputs={}
            with tempfile.TemporaryDirectory() as d,ExitStack() as stack,redirect_stdout(io.StringIO()):
                stack.enter_context(patch.object(sender,'read_json',side_effect=lambda p,default:copy.deepcopy({'generated_at_utc':'cycle'} if p==sender.INPUT else state)))
                stack.enter_context(patch.object(sender,'select_events',return_value=([v['row']],state)))
                stack.enter_context(patch.object(sender,'PublicClient',Client))
                stack.enter_context(patch.object(sender,'validate',return_value=(v,None)))
                stack.enter_context(patch.object(sender,'credentials',return_value=('u','p','r')))
                stack.enter_context(patch.object(sender,'atomic_json',side_effect=lambda p,value:outputs.update({p:copy.deepcopy(value)})))
                smtp=stack.enter_context(patch.object(sender.email_alert,'send_email'))
                if disk_fails:stack.enter_context(patch('research.execution_observability.atomic_json',side_effect=OSError('full')))
                else:
                    original=sender.capture_validation
                    stack.enter_context(patch.object(sender,'capture_validation',side_effect=lambda *a,**k:original(*a,**k,root=d)))
                self.assertEqual(sender.main(),0);self.assertEqual(smtp.call_count,1)
                status=outputs[sender.STATUS]
                results.append((smtp.call_args,status['email'],status['entry_eur'],status['stop_eur'],status['stake_eur']))
        self.assertEqual(results[0],results[1])
