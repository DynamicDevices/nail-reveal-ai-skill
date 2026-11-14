"""Original ladybird geometry; preparation is never acceptance."""
import json,math
from pathlib import Path
from prepare_d15_lantern import colour,path,ellipse,line
R=Path(__file__).resolve().parent
white=colour(390,1560);red=colour(830,1115);black=colour(830,1560)
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Glossy scarlet ladybird on porcelain',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
def views(steps):return {'final':steps,'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]}
head=[black,line(470,950,610,950)]
spots=[black]+[dict(type='hold',x=x,y=y,t=1) for x,y in [(410,1180),(670,1180),(410,1410),(670,1410)]]
if __name__=='__main__':
    save('d16-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),white,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip D15 and establish an opaque clean porcelain canvas.')
    save('d16-baseline',views([red,ellipse(540,1280,170,220),line(510,1100,510,1460),line(570,1100,570,1460)]),'A broad filled scarlet oval supplies shell material; Hand checks actual sidewall margin before detail.')
    save('d16-c01-a01',{'final':[black,line(595,1140,595,1450),red,line(630,1140,630,1450)]},'Trim broad black stroke with contained scarlet to leave a centred slender wing seam. Inspect for red outside shell.',True)
    save('d16-c02-a01',views(head),'A broad black head connects to the scarlet shell and gives the motif insect anatomy; Hand before acceptance.',True)
    save('d16-c03-a01',views(spots),'Four separated black shell spots establish recognisable ladybird pattern without merging into the seam or crossing the contour.',True)
    left=[[round(500-20*math.sin(math.pi*t/40)),round(850+50*t/40)] for t in range(41)]
    right=[[round(590+20*math.sin(math.pi*t/40)),round(850+50*t/40)] for t in range(41)]
    antennae=[black,path(left),path(right),white,path([[x+35,y] for x,y in left]),path([[x-35,y] for x,y in right])]+head
    save('d16-c04-a01',views(antennae),'Paired short antennae, narrowed with white then head replay; verify complete tips and clean white gaps in Hand.',True)
    glints=[white,dict(type='hold',x=370,y=1295,t=1),dict(type='hold',x=710,y=1295,t=1),red,dict(type='hold',x=405,y=1295,t=1),dict(type='hold',x=675,y=1295,t=1)]+spots
    save('d16-c05-a01',views(glints),'Paired white shell-edge glints supply a reflective material cue; repair spots touched by broad contacts and inspect actual clean whole composition.',True)
