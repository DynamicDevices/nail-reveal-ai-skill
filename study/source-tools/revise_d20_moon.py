"""Restore only affected sky,then try an inward moon; no automatic acceptance."""
from prepare_d20 import R,save,views,black,white,path
pts=[]
for j,y in enumerate(range(790,911,20)):
    row=[[x,y] for x in range(400,521,20)]
    pts.extend(row if j%2==0 else row[::-1])
if __name__=='__main__':
    save('d20-restore-c03',views([black,path(pts),path(pts[::-1])]),'Remove failed moon with dense black patch fully covering its footprint,clear of planet. Actual Hand/closeup must confirm c03 restoration before another candidate.')
    save('d20-c04-a02',views([white,dict(type='hold',x=570,y=900,seconds=1)]),'Move moon110px inward/right and50px down to clear Hand tip/left boundary. Require actual whole-disc/black-margin inspection.',True)
    save('d20-c05-a02',views([black,dict(type='hold',x=605,y=900,seconds=1)]),'Carve accepted inward moon into a thin crescent,echoing globe glint. Only after accepted c04-a02 and actual containment check.',True)
    (R/'attempts/d20-c05-a01/PREFLIGHT-NOT-EXECUTED.md').write_text('Never executed: parent c04-a01 moon clipped in actual Hand. New c05-a02 follows inward moon only after its acceptance. No physical rejection or cycle credit.\n')
