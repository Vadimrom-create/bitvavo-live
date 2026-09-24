"""Independent arithmetic checks of the published audit tables; offline only."""
import csv,json,pathlib,statistics,datetime,collections,sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[1];sys.path.insert(0,str(ROOT))
from scripts.update_exit_policy_shadow import _sim

def readcsv(name):
 with open(HERE/name,newline='')as f:return list(csv.DictReader(f))
def t(s):return datetime.datetime.fromisoformat(s.replace('Z','+00:00')).timestamp()
R=json.loads((HERE/'results.json').read_text());rows=readcsv('buy_outcomes.csv');checks=[]
for h in [4,12,24]:
 members=[]
 for policy in [1.4,1.5,1.6,2]:
  a=[x for x in rows if int(x['h'])==h and float(x['target_r'])==policy and x['mature']=='True' and float(x['coverage'])==1 and x['post_range_gate']=='True']
  exp=R['buy_summary_complete_archive'][str(h)][str(policy)]
  assert len(a)==exp['n']
  assert round(statistics.mean(float(x['net_pct'])for x in a),4)==exp['mean_net_pct']
  assert sum(float(x['net_pct'])>0 for x in a)==exp['positive_net']
  assert sum(x['result']=='STOP'for x in a)==exp['stops']
  assert sum(x['result']=='TP'for x in a)==exp['tp']
  assert len({(x['market'],x['decision_utc'])for x in a})==len(a)
  members.append({(x['market'],x['decision_utc'])for x in a})
  checks.append({'horizon':h,'target_r':policy,'n':len(a),'mean_net_pct':exp['mean_net_pct'],'status':'PASS'})
 assert all(x==members[0]for x in members)
verify=readcsv('journal_verification.csv');complete=[x for x in verify if float(x['coverage'])==1]
assert len(complete)==67
assert sum(abs(float(x['old_close_pct'])-float(x['chronological_close_pct']))>.01 for x in complete)==67
mismatch=[x for x in complete if (x['old_result']=='TP1')!=(x['chronological_result']=='TP')or x['old_result'].startswith('STOP')!=(x['chronological_result']=='STOP')]
assert len(mismatch)==1 and mismatch[0]['market']=='ZETA-EUR'and mismatch[0]['h']=='12'
runs=json.loads((HERE/'workflow_runs.json').read_text());end=t(R['cutoff']);a=sorted([x for x in runs if end-86400<=t(x['created_at'])<=end and x['event']=='schedule'],key=lambda x:x['created_at']);gaps=[(t(b['created_at'])-t(a['created_at']))/60 for a,b in zip(a,a[1:])]
assert len(a)==83 and round(statistics.median(gaps),2)==17.23 and round(max(gaps),2)==27.35
# Additional coverage defect: completeness can become true before the horizon matures.
z=_sim(100,90,120,0,[(13_800_000,100,101,99,100,1)],4,None)
assert z['complete_horizon']
extra={'horizon_end_seconds':14400,'last_bar_close_seconds':14100,'premature_by_seconds':300,'complete_horizon_returned':True,'synthetic_behavioral_test':True}
positive=[x for x in rows if x['target_r']=='2'and x['h']=='4'and x['mature']=='True'and float(x['coverage'])==1 and x['post_range_gate']=='True'and x['result']=='TP']
assert {x['market']for x in positive}=={'TREAD-EUR','ZETA-EUR'}
output={'source_audit_commit':'ff386ffe635602e60ab01161c0497584cdfdf62b','arithmetic_checks':checks,'journal_verified_horizons':len(complete),'close_mismatches':67,'tp_stop_mismatches':mismatch,'scheduled_runs_last24h':len(a),'median_scheduled_interval_minutes':statistics.median(gaps),'max_scheduled_interval_minutes':max(gaps),'premature_completeness_reproduction':extra,'demonstrated_tp_examples':positive,'note':'Checks arithmetic and behavioral defects; does not certify market fills or recompute unavailable raw responses.'}
(HERE/'final_verification.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'arithmetic_comparisons':len(checks),'journal_horizons':len(complete),'tp_stop_mismatches':len(mismatch),'scheduled_runs':len(a),'extra_completeness_test':'PASS'},indent=2))
