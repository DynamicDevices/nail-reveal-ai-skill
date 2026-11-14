"""Original calla-lily geometry; all acceptance remains screenshot-grounded."""
import json,math
from pathlib import Path
from prepare_d15_lantern import colour,path,ellipse,line
from prepare_d15 import fill_triangle,outward_cuts
R=Path(__file__).resolve().parent
plum=colour(250,1560);white=colour(390,1560);gold=colour(685,1265);teal=colour(250,1410)
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='White calla lily with golden spadix on plum',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
def views(steps):return {'final':steps,'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]}
petal=[white,ellipse(520,1050,110,190),line(520,860,520,1240)]
opening=[plum,ellipse(610,1010,100,140),line(610,870,610,1150)]
spadix=[gold,line(615,900,615,1160),plum,line(650,900,650,1160)]
stem=[teal,line(575,1300,575,1640),plum,line(610,1300,610,1640)]
leaf=[[510,1530],[780,1320],[670,1550]]
leafcuts=outward_cuts(leaf)
restore_bloom=petal+opening+spadix
if __name__=='__main__':
    save('d17-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),plum,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip D16 and establish a clean opaque plum canvas.')
    save('d17-baseline',views(petal),'Broad white petal material on plum; inspect full bloom margin in Hand before carving.')
    save('d17-c01-a01',views(opening),'Asymmetric plum inner cut opens the petal into a calla-like curled cup; inspect for detached caps and an intact white base.',True)
    save('d17-c02-a01',views(spadix),'A slender gold spadix within the bloom establishes the calla centre. Plum trim must not detach the petal base.',True)
    save('d17-c03-a01',{'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Teal stem below bloom; replay petal/opening/spadix after overlapping stem trim to preserve the flower. Hand before acceptance.',True)
    save('d17-c04-a01',{'leaf':[teal,fill_triangle(leaf),plum]+leafcuts+leafcuts,'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Pointed swept teal leaf joins the stem; external triangle masks are followed by the exact stem/flower replay. Inspect whole tip/margin in Hand.',True)
    vein=[gold,line(621,1563,771,1448),teal,line(642,1591,792,1476),plum]+leafcuts+leafcuts
    save('d17-c05-a01',{'vein':vein,'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'A contained gold leaf vein echoes the spadix and adds leaf structure. Reclip only the leaf then restore stem/flower. Judge actual containment,not intended polish.',True)
