from prepare_d14 import *
rain=[[[400-round(20*t/10),680+5*t] for t in range(11)],[[650-round(20*t/10),730+5*t] for t in range(11)],[[760-round(20*t/10),1250+5*t] for t in range(11)]]
steps=[colour(390,1560)]+[path(p) for p in rain]+[black]+[path([[x+35,y] for x,y in p]) for p in rain]
save('d14-c05-a01',{'final':steps,'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]},'Three slender white rain slashes frame the gold umbrella asymmetrically, supplying context and balance without filling the black negative space.',True)
