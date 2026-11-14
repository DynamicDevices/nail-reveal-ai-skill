"""Preflight repair: shorten inner major radius so orbit tips stay whole."""
from prepare_d20 import R,save,views,gold,black,orbit,frame,glint
if __name__=='__main__':
    (R/'attempts/d20-c03-a01/PREFLIGHT-NOT-EXECUTED.md').write_text('Superseded before phone: equal outer/inner major radii leave vanishing/broken orbit tips in opaque sketch. Not a physical rejection or cycle.\n')
    save('d20-c03-a02',{'orbit':[gold,orbit(190,65),black,orbit(160,30)],'globe':frame,'final':glint,'hand':views([])['hand'],'returned':views([])['returned']},'Shorter inner ellipse leaves continuous orbit wings instead of vanishing tips. Actual ring/Hand margins and beauty required.',True)
