from prepare_d16 import *
stages={}
for a in ['d16-clean-base','d16-baseline','d16-baseline-density','d16-c01-a01','d16-c02-a01','d16-c03-a01','d16-c04-a01']:
    for label,steps in json.loads((R/'attempts'/a/'stages.json').read_text()).items():
        if label in ('hand','returned'):continue
        stages[a+'-'+label]=steps
stages.update({'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]})
save('d16-restore-c04-after-glints',stages,'Full physical strip/white/body/density/seam/head/spots/antennae replay restores the accepted parent after failed shell-edge glints. Inspect before retry; no cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1];assert i['id']=='d16'
i['rejected_attempts'].append('attempts/d16-c05-a01');i.setdefault('restorations',[]).append('attempts/d16-restore-c04-after-glints');i['pending']='attempts/d16-restore-c04-after-glints';i['initial_baseline']='attempts/d16-baseline';i.setdefault('finishing_attempts',[]).append('attempts/d16-baseline-density');p.write_text(json.dumps(s,indent=2)+'\n')
