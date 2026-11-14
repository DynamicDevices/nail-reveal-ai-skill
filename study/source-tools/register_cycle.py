"""Index an explicitly inspected acceptance, never infer beauty from execution."""
import argparse,json
from pathlib import Path
from study_driver import checked_id
R=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('idea',type=checked_id);p.add_argument('attempt',type=checked_id);p.add_argument('--concept');p.add_argument('--baseline',type=checked_id);p.add_argument('--clean-base',type=checked_id);args=p.parse_args()
folder=R/'attempts'/args.attempt
assert (folder/'ASSESSMENT.md').read_text().splitlines()[0].startswith('# Accepted')
e=json.loads((folder/'execution.json').read_text());assert e['failure'] is None
assert (folder/'creation.mp4').stat().st_size>0
target=R/'study.json';s=json.loads(target.read_text());i=next((i for i in s['ideas'] if i['id']==args.idea),None)
if i is None:
    assert args.concept and args.baseline and args.clean_base
    i=dict(id=args.idea,concept=args.concept,clean_base='attempts/'+args.clean_base,baseline='attempts/'+args.baseline,accepted_cycles=[],rejected_attempts=[],best='attempts/'+args.baseline,pending=None,status='in-progress');s['ideas'].append(i)
ref='attempts/'+args.attempt
assert ref not in i['rejected_attempts']
if ref not in i['accepted_cycles']:
    assert len(i['accepted_cycles'])<s['target_accepted_cycles_per_idea']
    i['accepted_cycles'].append(ref)
i['best']=ref;i['pending']=None
s['accepted_cycles_total']=sum(len(i['accepted_cycles']) for i in s['ideas'])
target.write_text(json.dumps(s,indent=2)+'\n')
