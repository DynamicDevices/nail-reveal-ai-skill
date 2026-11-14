from prepare_d14 import *
stages={}
for a in ['d14-clean-base','d14-baseline','d14-c01-a01','d14-c02-a01','d14-c03-a01','d14-c04-a01']:
    data=json.loads((R/'attempts'/a/'stages.json').read_text())
    for label,steps in data.items():stages[a+'-'+label]=steps
save('d14-restore-c04-after-rain',stages,'Full physical replay of accepted c04 after rejected crescents. Must inspect before retry; no cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1]
i['rejected_attempts'].append('attempts/d14-c05-a01')
i.setdefault('restorations',[]).append('attempts/d14-restore-c04-after-rain')
i['pending']='attempts/d14-restore-c04-after-rain'
p.write_text(json.dumps(s,indent=2)+'\n')
