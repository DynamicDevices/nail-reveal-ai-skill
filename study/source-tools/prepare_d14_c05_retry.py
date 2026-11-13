from prepare_d14 import *
rain=[(310,1200),(760,1190),(740,1550)]
steps=[colour(390,1560)]+[path([[x,y+j] for j in range(0,41,5)]) for x,y in rain]+[black]
for x,y in rain:
    for shift in (-105,105):steps.append(path([[x+shift,y+j] for j in range(0,41,5)]))
save('d14-c05-a02',{'final':steps,'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]},'Paired parallel black masks narrow three vertical white contacts into rain dashes. Keep all below canopy, away from tip, handle and shaft. Inspect actual restoration first.',True)
