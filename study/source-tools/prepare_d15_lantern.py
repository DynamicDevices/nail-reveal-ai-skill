"""Original scarlet paper lantern; exact finite generated paths are retained."""
import json,math
from pathlib import Path
R=Path(__file__).resolve().parent
def colour(x,y):return dict(type='colour',x=x,y=y)
white=colour(390,1560);red=colour(830,1115);gold=colour(685,1265)
def path(p):return dict(type='path',points=p,initial=.4,final=.4)
def ellipse(cx,cy,rx,ry):return path([[round(cx+rx*math.cos(t*math.pi/90)),round(cy+ry*math.sin(t*math.pi/90))] for t in range(181)])
def line(x0,y0,x1,y1):
    n=max(1,math.ceil(math.hypot(x1-x0,y1-y0)/10))
    return path([[round(x0+(x1-x0)*t/n),round(y0+(y1-y0)*t/n)] for t in range(n+1)])
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Scarlet paper lantern on porcelain',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
topcap=[gold,line(440,880,640,880)]
bottomcap=[gold,line(440,1480,640,1480)]
if __name__=='__main__':
    save('d15-lantern-baseline',{'final':[red,ellipse(540,1180,120,220),line(540,960,540,1400)]},'A rich broad scarlet oval establishes the paper body on clean porcelain; not yet a complete lantern.')
    save('d15-lantern-c01-a01',{'final':topcap},'A warm gold upper cap gives the red oval a structured lantern neck and contrasting focal edge.',True)
    save('d15-lantern-c02-a01',{'final':bottomcap},'A matching lower cap frames the paper body and balances its upper rim; inspect width/overlap.',True)
