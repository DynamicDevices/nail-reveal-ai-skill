from prepare_d14 import *
steps=[black]+[ellipse(x,y,35,50) for x,y in [(310,1220),(760,1210),(740,1570)]]
replay=json.loads((R/'attempts/d14-c04-a01/stages.json').read_text())['final']
save('d14-restore-c04-fringe-cleanup',{'cover-fringes':steps,'final':replay},'Expand each rain removal beyond the original footprint to remove faint residual rings, then repair shaft. No new cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1];i['restorations'].append('attempts/d14-restore-c04-fringe-cleanup');i['pending']='attempts/d14-restore-c04-fringe-cleanup';p.write_text(json.dumps(s,indent=2)+'\n')
