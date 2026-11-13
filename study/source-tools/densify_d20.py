"""Uncounted baseline density; revise only unexecuted globe replays."""
import json
from prepare_d20 import R,save,views,teal,path
pts=[]
for j,y in enumerate(range(1190,1311,20)):
    row=[[x,y] for x in range(480,601,20)]
    pts.extend(row if j%2==0 else row[::-1])
density=[teal,path(pts),path(pts[::-1])]
if __name__=='__main__':
    save('d20-baseline-density',views(density),'Dense confined green interior removes visible dark patches before counting. No new design cycle; preserve original baseline.')
    for a,label in [('d20-c01-a01','final'),('d20-c03-a02','globe')]:
        f=R/'attempts'/a
        assert not (f/'execution.json').exists()
        p=f/'stages.json';old=p.read_text()
        (f/'pre-density-proposal-stages.json').write_text(old)
        stages=json.loads(old);stages[label]+=density
        p.write_text(json.dumps(stages,separators=(',',':'))+'\n')
        (f/'PRE-EXECUTION-REVISION.md').write_text('Before any phone execution: add confined dense green interior,subject to actual baseline validation before candidate execution. Original unexecuted stages retained in pre-density-proposal-stages.json. No physical rejection or cycle credit.\n')
