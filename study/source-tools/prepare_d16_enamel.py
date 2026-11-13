from prepare_d16 import *
fill=[]
for j,x in enumerate(range(450,631,30)):
    fill += [[x,y] for y in (range(1140,1421,20) if j%2==0 else range(1420,1139,-20))]
newspots=[dict(type='hold',x=x,y=y,t=1) for x,y in [(430,1200),(650,1200),(430,1400),(650,1400)]]
stages={'frame':[colour(685,1265),ellipse(540,1280,170,220),red,ellipse(540,1280,145,195),line(510,1100,510,1460),line(570,1100,570,1460)],
        'density':[red,path(fill),path(fill)],
        'final':[black,line(595,1140,595,1420),red,line(630,1140,630,1420)]+head+newspots,
        'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],
        'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]}
save('d16-c05-a02',stages,'After actual c04 restoration,add a thin gold enamel rim around a slightly inset scarlet shell. Shorten seam end30px and bring spots inward to preserve clean framed margins. Judge whole composition and Hand; no white contour cuts.',True)
