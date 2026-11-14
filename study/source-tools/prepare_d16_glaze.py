from prepare_d16 import *
save('d16-glaze',{'final':[dict(type='tool',x=690,y=2200),dict(type='wait',seconds=3)]},'Glaze after five accepted improvements and capture resulting Hand. No extra cycle.')
save('d16-glazed-closeup',{'final':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]},'Capture finished closeup after glaze/Hand; no Done or saved-gallery persistence claim.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1];assert i['id']=='d16' and len(i['accepted_cycles'])==5;i['concept']='Gold-rimmed scarlet ladybird on porcelain';p.write_text(json.dumps(s,indent=2)+'\n')
