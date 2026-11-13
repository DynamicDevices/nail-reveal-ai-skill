"""Prepare original D14 geometry; generated recipes are not executed results."""
import json, math
from pathlib import Path
R=Path(__file__).resolve().parent
def colour(x,y):return dict(type='colour',x=x,y=y)
gold=colour(685,1265); black=colour(830,1560); red=colour(830,1115)
def path(p):return dict(type='path',points=p,initial=.4,final=.4)
def ellipse(cx,cy,rx,ry):
    return path([[round(cx+rx*math.cos(t*math.pi/90)),round(cy+ry*math.sin(t*math.pi/90))] for t in range(181)])
def row(y):return path([[x,y] for x in range(240,841,10)])
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Golden umbrella in the rain',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
if __name__=='__main__':
    save('d14-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')], 'final':[dict(type='tool',x=100,y=1260),black,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip D13 and establish an opaque black canvas.')
    save('d14-baseline',{'final':[gold,ellipse(540,1040,150,95),path([[x,1040] for x in range(390,691,10)])]},'Broad warm-gold oval supplies a balanced canopy mass; not yet an umbrella.')
    save('d14-c01-a01',{'final':[black,row(1130),row(1210),row(1290),row(1130)]},'A dense black lower mask converts the oval into a clean dome.',True)
