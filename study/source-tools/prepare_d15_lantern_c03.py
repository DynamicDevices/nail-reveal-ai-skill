from prepare_d15_lantern import *
left=[[round(480-25*math.sin(math.pi*t/80)),round(1000+400*t/80)] for t in range(81)]
right=[[round(600+25*math.sin(math.pi*t/80)),round(1000+400*t/80)] for t in range(81)]
steps=[gold,path(left),path(right),red,path([[x+35,y] for x,y in left]),path([[x-35,y] for x,y in right])]+topcap+bottomcap
save('d15-lantern-c03-a01',{'final':steps},'Two gold curved ribs, trimmed inward with scarlet, add paper-lantern volume. Restore both gold caps after red masks; inspect outside-body spill.',True)
