"""Prepare minimal exact bloom replay: c05 changed no stem/leaf pixels."""
import json
from prepare_d17 import R,save,views,petal,opening,spadix
if __name__=='__main__':
    save('d17-restore-c04',{'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Restore actual c04 bloom after rejected c05-a04; untouched leaf/stem remain. Inspect equivalence before another candidate.')
    p=R/'study.json';s=json.loads(p.read_text());i=next(i for i in s['ideas'] if i['id']=='d17')
    i['rejected_attempts'].append('attempts/d17-c05-a04');i['pending']='Restore and inspect actual c04 before another c05'
    p.write_text(json.dumps(s,indent=2)+'\n')
