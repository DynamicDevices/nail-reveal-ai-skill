"""Optional opaque brush preflight; never game/beauty/timing evidence."""
import json,sys
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent
idea,base,*attempts=sys.argv[1:]
palette={(250,1560):(86,44,83),(390,1560):(255,255,255),(685,1265):(255,225,129),(250,1410):(12,138,135),(395,1410):(137,199,226),(830,1560):(16,16,16),(830,1115):(208,12,49)}
canvas=Image.new('RGB',(1080,2400),palette[tuple(map(int,base.split(',')))]);ink=canvas.getpixel((0,0))
out=R/'plans'/idea;out.mkdir(parents=True,exist_ok=True);frames=[]
for a in attempts:
    draw=ImageDraw.Draw(canvas)
    for label,steps in json.loads((R/'attempts'/a/'stages.json').read_text()).items():
        # Caller supplies the flat initial base. Preparation is not simulated.
        if label in ('hand','returned','strip','base'):continue
        for s in steps:
            if s['type']=='colour':ink=palette[(s['x'],s['y'])]
            elif s['type'] in ('path','hold'):
                pts=[(x,y-120) for x,y in s.get('points',[[s.get('x'),s.get('y')]])]
                if len(pts)>1:draw.line(pts,fill=ink,width=160,joint='curve')
                for x,y in pts:draw.ellipse((x-80,y-80,x+80,y+80),fill=ink)
            else:raise ValueError('Unsupported sketch primitive')
    f=Image.new('RGB',(400,880),'white');f.paste(canvas.crop((140,400,940,2100)).resize((400,850)),(0,30))
    ImageDraw.Draw(f).text((6,8),'SKETCH, NOT GAME: '+a,fill='black');f.save(out/(a+'.png'));frames.append(f)
sheet=Image.new('RGB',(1200,880*((len(frames)+2)//3)),'white')
for j,f in enumerate(frames):sheet.paste(f,((j%3)*400,(j//3)*880))
sheet.save(out/'progression-sketch.png')
(out/'MODEL-LIMITS.md').write_text('Opaque radius80 brush/upward offset120. Approximate colours; no actual opacity,shading,nail silhouette or Hand projection. NOT GAME; no cycle,beauty,timing or containment proof.\n')
print(str(out/'progression-sketch.png'))
