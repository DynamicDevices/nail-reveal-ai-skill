from prepare_d15_lantern import *
def rows(ys):
    pts=[]
    for j,y in enumerate(ys):pts += [[x,y] for x in (range(230,851,10) if j%2==0 else range(850,229,-10))]
    return path(pts)
save('d15-lantern-restore-c03',{'upper':[white,rows([600,680,760]),rows([600,680,760])],'lower':[white,rows([1560,1640,1720,1800]),rows([1560,1640,1720,1800])],'final':topcap+[line(440,1480,640,1480)]},'Broad white planes remove upper cord and pendant; original caps restore their overlap. Inspect actual c03; if residue remains use full strip/replay. No cycle.')
p=R/'study.json';s=json.loads(p.read_text());i=s['ideas'][-1];assert i['id']=='d15'
i['accepted_cycles'].remove('attempts/d15-lantern-c04-a01');i['rejected_attempts']+=['attempts/d15-lantern-c04-a01','attempts/d15-lantern-c05-a01'];i['best']='attempts/d15-lantern-c03-a01';i['pending']='attempts/d15-lantern-restore-c03';i.setdefault('restorations',[]).append('attempts/d15-lantern-restore-c03');s['accepted_cycles_total']=sum(len(z['accepted_cycles']) for z in s['ideas']);p.write_text(json.dumps(s,indent=2)+'\n')
