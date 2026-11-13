from prepare_d15_lantern import *
top=[gold,line(440,980,640,980)]
bottom=[gold,line(440,1500,640,1500)]
left=[[round(480-25*math.sin(math.pi*t/80)),round(1100+320*t/80)] for t in range(81)]
right=[[round(600+25*math.sin(math.pi*t/80)),round(1100+320*t/80)] for t in range(81)]
ribs=[gold,path(left),path(right),red,path([[x+35,y] for x,y in left]),path([[x-35,y] for x,y in right])]+top+[line(440,1500,640,1500)]
stages={'strip':[dict(type='tool',x=100,y=650),dict(type='coat-v2')],
        'canvas':[dict(type='tool',x=100,y=1260),white,dict(type='coat-v2'),dict(type='coat-v2')],
        'compact-body':[red,ellipse(540,1240,120,180),line(540,1060,540,1420)],
        'caps':top+[line(440,1500,640,1500)],
        'ribs':ribs,
        'final':[gold,line(595,850,595,900),white,line(630,850,630,900)]+top,
        'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],
        'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]}
save('d15-lantern-c04-a02',stages,'From physically restored c03, rebuild a more compact lantern body and move upper suspension down so the full curl has actual Hand-view margin. Preserve ribs/palette and inspect Hand before acceptance.',True)
steps=[gold,line(595,1550,595,1700),white,line(630,1550,630,1700)]+bottom+[ellipse(540,1735,20,50),red,dict(type='hold',x=540,y=1750,t=1)]
save('d15-lantern-c05-a02',{'final':steps,'hand':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)],'returned':[dict(type='tool',x=380,y=2200),dict(type='wait',seconds=3)]},'Add gold-framed scarlet pendant to the actually accepted compact parent; repeat Hand check to ensure upper curl and lower ornament both remain whole.',True)
