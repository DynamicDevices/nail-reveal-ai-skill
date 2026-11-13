"""Record already inspected decisions; never derives aesthetic acceptance."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
p=R/'study.json'; s=json.loads(p.read_text())
if not any(i['id']=='d14' for i in s['ideas']):
    s['ideas'].append(dict(id='d14',concept='Golden umbrella in the rain',clean_base='attempts/d14-clean-base',baseline='attempts/d14-baseline',accepted_cycles=[],rejected_attempts=[],best='attempts/d14-baseline',pending=None,status='in-progress'))
i=next(i for i in s['ideas'] if i['id']=='d14')
for a in sys.argv[1:]:
    f=R/'attempts'/a
    assert (f/'ASSESSMENT.md').read_text().splitlines()[0].startswith('# Accepted')
    e=json.loads((f/'execution.json').read_text());assert e['failure'] is None
    ref='attempts/'+a
    if ref not in i['accepted_cycles']:i['accepted_cycles'].append(ref)
    i['best']=ref
s['accepted_cycles_total']=sum(len(x['accepted_cycles']) for x in s['ideas'])
p.write_text(json.dumps(s,indent=2)+'\n')
