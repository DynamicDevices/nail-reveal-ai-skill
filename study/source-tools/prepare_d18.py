"""Original perfume-flacon proposal. Preparation never implies acceptance."""
import json
from prepare_d17 import R,views,white,gold,ellipse,line,colour
black=colour(830,1560);red=colour(830,1115)
body=[gold,ellipse(540,1300,150,210),line(540,1090,540,1510)]
inset=[black,ellipse(540,1300,110,170),line(540,1130,540,1470)]
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Golden perfume flacon with ruby seal on black',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
if __name__=='__main__':
    save('d18-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),black,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip D17 and establish opaque black canvas; inspect before motif.')
    save('d18-baseline',views(body),'Broad gold oval supplies flacon body material. Baseline only; inspect density and Hand margin.')
    save('d18-c01-a01',views(inset),'Black inner oval leaves a continuous gold bottle outline with negative-space interior. Inspect continuity and uniformity.',True)
    save('d18-c02-a01',{'neck':[gold,line(540,930,540,1030)],'final':body+inset,'hand':views([])['hand'],'returned':views([])['returned']},'Gold neck connects above the body; replay body/inset preserves frame. Hand inspection before further features.',True)
    save('d18-c03-a01',views([white,line(470,870,610,870)]),'Ivory stopper crowns the narrow neck, creating recognisable perfume-bottle proportions. Full silhouette must remain contained.',True)
    save('d18-c04-a01',views([white,ellipse(540,1300,40,40),line(540,1260,540,1340)]),'Contained ivory label gives bottle a clear focal medallion with black breathing room to the gold rim.',True)
    save('d18-c05-a01',views([red,dict(type='hold',x=540,y=1300,seconds=1)]),'A ruby-red centre inside ivory label adds a sharply framed focal seal. Reject if it breaks the ivory border or competes with bottle shape.',True)
