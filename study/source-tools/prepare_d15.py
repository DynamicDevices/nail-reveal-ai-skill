"""Original parameterised sailboat; preparing geometry does not accept cycles."""
import json,math
from pathlib import Path
R=Path(__file__).resolve().parent
def colour(x,y):return dict(type='colour',x=x,y=y)
white=colour(390,1560);black=colour(830,1560);red=colour(830,1115);gold=colour(685,1265);teal=colour(250,1410)
def path(points):return dict(type='path',points=points,initial=.4,final=.4)
def line(a,b,spacing=10):
    n=max(1,math.ceil(math.dist(a,b)/spacing))
    return path([[round(a[0]+(b[0]-a[0])*t/n),round(a[1]+(b[1]-a[1])*t/n)] for t in range(n+1)])
def fill_triangle(vertices):
    # Scanline intersections; dense serpentine supplies material before masks.
    pts=[]
    for j,y in enumerate(range(min(v[1] for v in vertices),max(v[1] for v in vertices)+1,25)):
        xs=[]
        for a,b in zip(vertices,vertices[1:]+vertices[:1]):
            if a[1]!=b[1] and min(a[1],b[1])<=y<=max(a[1],b[1]):
                xs.append(a[0]+(b[0]-a[0])*(y-a[1])/(b[1]-a[1]))
        if not xs:continue
        lo,hi=min(xs),max(xs);n=max(1,math.ceil((hi-lo)/20))
        row=[[round(lo+(hi-lo)*t/n),y] for t in range(n+1)]
        pts.extend(row if j%2==0 else row[::-1])
    return path(pts)
def outward_cuts(vertices,offset=80):
    cx=sum(x for x,y in vertices)/len(vertices);cy=sum(y for x,y in vertices)/len(vertices)
    steps=[]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy);nx,ny=-dy/length,dx/length
        if nx*((a[0]+b[0])/2-cx)+ny*((a[1]+b[1])/2-cy)<0:nx,ny=-nx,-ny
        aa=[round(a[0]+offset*nx),round(a[1]+offset*ny)];bb=[round(b[0]+offset*nx),round(b[1]+offset*ny)]
        steps.append(line(aa,bb))
    return steps
def save(a,stages,hyp,counts=False):
    f=R/'attempts'/a;f.mkdir(exist_ok=False)
    (f/'stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    (f/'recipe.json').write_text(json.dumps(dict(attempt=a,concept='Scarlet and black sailboat on porcelain',hypothesis=hyp,counts_as_cycle=counts),indent=2)+'\n')
main=[[540,850],[540,1450],[300,1450]]
jib=[[620,1050],[780,1450],[620,1450]]
if __name__=='__main__':
    save('d15-clean-base',{'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],'final':[dict(type='tool',x=100,y=1260),white,dict(type='coat-v2'),dict(type='coat-v2')]},'Strip comparison fixture and establish opaque porcelain canvas.')
    save('d15-baseline',{'final':[black,fill_triangle(main)]},'Broad black triangular material, deliberately untrimmed; beginning of main sail.')
    cuts=outward_cuts(main)
    save('d15-c01-a01',{'final':[white]+cuts+cuts},'Paired passes along outward-offset triangle edges remove brush expansion and produce a clean pointed main sail.',True)
