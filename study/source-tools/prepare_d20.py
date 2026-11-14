"""Original ringed-planet brooch; proposals only until actual inspection."""
import json,math
from prepare_d17 import R,views,white,gold,teal,ellipse,line,colour,path
black=colour(830,1560)
body=[teal,ellipse(540,1250,110,110),line(540,1140,540,1360)]
frame=[gold,ellipse(540,1250,135,135),line(540,1115,540,1385)]+body
glint=[white,dict(type='hold',x=480,y=1180,seconds=1),teal,dict(type='hold',x=510,y=1205,seconds=1)]
def orbit(rx,ry):
    a=math.radians(-25)
    return path([[round(540+rx*math.cos(t*math.pi/90)*math.cos(a)-ry*math.sin(t*math.pi/90)*math.sin(a)),round(1250+rx*math.cos(t*math.pi/90)*math.sin(a)+ry*math.sin(t*math.pi/90)*math.cos(a))] for t in range(181)])
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Ringed sea-glass planet and crescent moon on black',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
if __name__=='__main__':
    save('d20-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),black,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip landscape and establish clean black canvas. No cycle.')
    save('d20-baseline',views(body),'Sea-glass planet material on black; inspect density and Hand margin. Baseline only.')
    save('d20-c01-a01',{'final':frame,'hand':views([])['hand'],'returned':views([])['returned']},'Fine gold rim finishes globe and contrasts with black. Actual continuous edge required.',True)
    save('d20-c02-a01',views(glint),'Contained white crescent glint gives globe depth without a notch in its silhouette.',True)
    save('d20-c03-a01',{'orbit':[gold,orbit(190,65),black,orbit(190,30)],'globe':frame,'final':glint,'hand':views([])['hand'],'returned':views([])['returned']},'Tilted gold orbit behind globe changes medallion into ringed planet. Wing-like stylisation,not physically accurate Saturn projection. Hand before dependent layers.',True)
    save('d20-c04-a01',views([white,dict(type='hold',x=460,y=850,seconds=1)]),'Separate ivory moon above planet gives the composition a second scale and a clear sky interval. Hand tip/margin required.',True)
    save('d20-c05-a01',views([black,dict(type='hold',x=495,y=850,seconds=1)]),'Carve full moon into slender crescent,contrasting with round globe and echoing its glint. Actual complete crescent/no cap fragments required.',True)
