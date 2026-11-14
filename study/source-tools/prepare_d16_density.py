from prepare_d16 import *
p=[]
for j,x in enumerate(range(450,631,30)):
    p += [[x,y] for y in (range(1140,1421,20) if j%2==0 else range(1420,1139,-20))]
save('d16-baseline-density',{'final':[red,path(p),path(p)]},'Fill remaining faint interior density traces with two contained dense passes. Original clean white canvas proves these are fill variation,not prior lantern remnants. No accepted cycle.')
