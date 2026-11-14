"""Revise unexecuted leaf proposal, retaining the superseded preflight files."""
import json, math
from prepare_d17 import R, save, views, teal, plum, petal, opening, spadix, stem, gold, line, fill_triangle

leaf = [[550,1540],[320,1300],[360,1530]]
def extended_cuts(vertices):
    cx=sum(x for x,y in vertices)/3;cy=sum(y for x,y in vertices)/3
    cuts=[]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        dx=b[0]-a[0];dy=b[1]-a[1];d=math.hypot(dx,dy)
        ux,uy=dx/d,dy/d;nx,ny=-uy,ux
        if nx*((a[0]+b[0])/2-cx)+ny*((a[1]+b[1])/2-cy)<0:nx,ny=-nx,-ny
        cuts.append(line(round(a[0]+80*nx-250*ux),round(a[1]+80*ny-250*uy),round(b[0]+80*nx+250*ux),round(b[1]+80*ny+250*uy)))
    return cuts
cuts=extended_cuts(leaf)
if __name__=='__main__':
    for a in ['d17-c04-a01','d17-c05-a01']:
        f=R/'attempts'/a/'PREFLIGHT-NOT-EXECUTED.md'
        assert not (f.parent/'execution.json').exists()
        f.write_text('Superseded before phone execution: approximate sketch showed disconnected leaf and isolated cap. Not a physical failure or accepted cycle.\n')
    save('d17-c04-a02',{'leaf':[teal,fill_triangle(leaf),plum]+cuts+cuts,'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Left-facing pointed leaf avoids the right-side stem mask; extended cuts remove endpoint remnants. Inspect connection and full Hand silhouette.',True)
    save('d17-c05-a02',{'vein':[gold,line(385,1430,480,1515),teal,line(360,1470,455,1555),plum]+cuts+cuts,'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Proposed gold leaf vein; preflight and actual containment required. Never automatic acceptance.',True)
