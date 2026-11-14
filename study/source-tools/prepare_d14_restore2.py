from prepare_d14 import *
rain=[(310,1200),(760,1190),(740,1550)]
steps=[black]+[path([[x,y+j] for j in range(0,41,5)]) for x,y in rain]*2
replay=json.loads((R/'attempts/d14-c04-a01/stages.json').read_text())['final']
save('d14-restore-c04-after-rain2',{'remove-rain':steps,'final':replay},'Remove every white mark in black; restore exact shaft and its side masks to undo possible rain-mask overlap. Inspect against c04; no cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1]
i['rejected_attempts'].append('attempts/d14-c05-a02');i['restorations'].append('attempts/d14-restore-c04-after-rain2');i['pending']='attempts/d14-restore-c04-after-rain2'
p.write_text(json.dumps(s,indent=2)+'\n')
save('d14-c05-a03',{'final':[red,dict(type='hold',x=540,y=970,t=1)],'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]},'A contained scarlet round inset adds a warm focal colour to the gold canopy without competing marks or fragile short-line geometry.',True)
