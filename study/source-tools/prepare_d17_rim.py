"""Unexecuted gold-rim alternative preserves the clean petal silhouette."""
from prepare_d17 import R,save,views,gold,ellipse,line,petal,opening,spadix
if __name__=='__main__':
    (R/'attempts/d17-c05-a06/PREFLIGHT-NOT-EXECUTED.md').write_text('Superseded before phone execution: deeper curve detached leaf from stem in sketch. Not executed or counted.\n')
    save('d17-c05-a07',{'frame':[gold,ellipse(520,1050,135,215),line(520,835,520,1265)],'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Fine continuous gold outer petal rim echoes the spadix and enriches the white/plum contrast without a bulky extra lip. Verify full Hand margin and no isolated gold scraps.',True)
