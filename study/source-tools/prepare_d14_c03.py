from prepare_d14 import *
shaft=path([[540,y] for y in range(1030,1441,10)])
trim=[path([[x,y] for y in range(1140,1521,10)]) for x in (430,650)]
canopy=[gold,ellipse(540,1040,150,95),path([[x,1040] for x in range(390,691,10)]),black,row(1130),row(1210),row(1290),row(1130)]+[dict(type='hold',x=x,y=1100,t=1) for x in (400,540,680)]
# Upper-only restoration would destroy the shaft if full lower masks replayed.
# Trim sides below canopy; then a contained gold bridge reconnects the shaft.
save('d14-c03-a01',{'shaft':[gold,shaft,black]+trim,'final':[gold,path([[540,y] for y in range(1020,1081,10)]),black]+[path([[x,y] for y in range(1100,1521,10)]) for x in (430,650)]},'A narrow central gold shaft establishes the umbrella structure. Paired side masks retain a slim central ribbon; inspect canopy overlap.',True)
