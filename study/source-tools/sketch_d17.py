"""Flat opaque radius80/contact-offset120 approximation, NOT game output."""
import json
from pathlib import Path
from PIL import Image,ImageDraw
from prepare_d17 import R
out=R/'plans'/'d17';out.mkdir(parents=True,exist_ok=True)
palette={(250,1560):(86,44,83),(390,1560):(255,255,255),(685,1265):(255,225,129),(250,1410):(12,138,135)}
canvas=Image.new('RGB',(1080,2400),palette[(250,1560)]);ink=palette[(250,1560)]
frames=[]
for a in ['d17-baseline']+[f'd17-c0{k}-a01' for k in range(1,4)]+['d17-c04-a02','d17-c05-a07']:
    stages=json.loads((R/'attempts'/a/'stages.json').read_text())
    draw=ImageDraw.Draw(canvas)
    for label,steps in stages.items():
        if label in ('hand','returned'):continue
        for s in steps:
            if s['type']=='colour':ink=palette[(s['x'],s['y'])]
            elif s['type'] in ('path','hold'):
                points=s.get('points',[[s.get('x'),s.get('y')]])
                pts=[(x,y-120) for x,y in points]
                if len(pts)>1:draw.line(pts,fill=ink,width=160,joint='curve')
                for x,y in pts:draw.ellipse((x-80,y-80,x+80,y+80),fill=ink)
            else:raise ValueError('Unsupported sketch primitive')
    crop=canvas.crop((140,400,940,2100)).resize((400,850))
    frame=Image.new('RGB',(400,880),'white');frame.paste(crop,(0,30))
    ImageDraw.Draw(frame).text((6,8),'SKETCH, NOT GAME: '+a,fill='black')
    frame.save(out/(a+'.png'));frames.append(frame)
sheet=Image.new('RGB',(1200,1760),'white')
for j,f in enumerate(frames):sheet.paste(f,((j%3)*400,(j//3)*880))
sheet.save(out/'progression-sketch.png')
(out/'MODEL-LIMITS.md').write_text('# Approximate preflight only\n\nOpaque radius80 brush/contact offset120. No game physics,opacity,shading,\ntexture projection or nail silhouette simulated. Palette colours approximate.\nNot an executed attempt,acceptance,or timing benchmark. Verify actual Hand view.\n')
print(str(out/'progression-sketch.png'))
