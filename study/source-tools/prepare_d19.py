"""Original alpine lake proposals, not executed or accepted by preparation."""
import json
from prepare_d17 import R,views,plum,white,gold,teal,line,ellipse,colour,fill_triangle
from revise_d17 import extended_cuts
blue=colour(395,1410)
mountain=[[540,1050],[300,1560],[780,1560]]
cuts=extended_cuts(mountain)
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Snow-capped alpine peak and sunlit lake on teal',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
if __name__=='__main__':
    save('d19-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),teal,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip flacon; establish opaque teal canvas. Preparation,not cycle.')
    save('d19-baseline',views([plum,fill_triangle(mountain)]),'Broad plum triangular mountain material on teal. Baseline only; check density and Hand margin.')
    save('d19-c01-a01',views([teal]+cuts+cuts),'Extended outside cuts turn rounded material into a crisp triangular peak. Inspect tip,base and absence of cap remnants.',True)
    cap=[[540,1050],[455,1230],[625,1230]]
    save('d19-c02-a01',{'snow':[white,fill_triangle(cap),teal]+cuts+cuts,'final':[],'hand':views([])['hand'],'returned':views([])['returned']},'Snow cap contrasts with plum rock. Original external mountain cuts contain white at peak; actual snow line must be clean.',True)
    save('d19-c03-a01',views([gold,dict(type='hold',x=680,y=960,seconds=1)]),'Warm sun above right shoulder establishes light and balances mountain. Hand containment required before next layer.',True)
    save('d19-c04-a01',views([blue,ellipse(540,1700,180,60),line(360,1700,720,1700)]),'Pale-blue lake beneath peak anchors the scene and separates water from teal sky. Inspect shore and margin.',True)
    save('d19-c05-a01',views([gold,line(620,1680,680,1680),blue,line(620,1715,680,1715)]),'Slim warm reflection in lake echoes the sun. Reject if it breaks lake boundary or reads as a stray mark.',True)
