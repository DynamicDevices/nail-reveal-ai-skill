from prepare_d14 import *
stages=json.loads((R/'attempts/d14-restore-c04-after-rain/stages.json').read_text())
save('d14-restore-c04-full-after-rain2',stages,'Known-working complete strip and recipe replay after local cleanup left residual rings; no cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1];i['restorations'].append('attempts/d14-restore-c04-full-after-rain2');i['pending']='attempts/d14-restore-c04-full-after-rain2';p.write_text(json.dumps(s,indent=2)+'\n')
