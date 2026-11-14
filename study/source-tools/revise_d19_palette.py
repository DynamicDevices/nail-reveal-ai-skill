"""Recorded restoration then a new darker-field candidate; no auto acceptance."""
from prepare_d19 import R,save,views,teal,plum,white,cuts,mountain,fill_triangle
if __name__=='__main__':
    coat=[dict(type='tool',x=100,y=650),dict(type='coat-v2')]
    greenbase=[dict(type='tool',x=100,y=1260),teal,dict(type='coat-v2'),dict(type='coat-v2')]
    save('d19-restore-baseline',{'strip':coat,'base':greenbase,'final':[plum,fill_triangle(mountain)],'hand':views([])['hand'],'returned':views([])['returned']},'Restore original green field/plum broad triangle after rejected halo and failed white-undercoat cleanup. Inspect actual restoration before another candidate.')
    save('d19-c01-a02',{'strip':coat,'base':[dict(type='tool',x=100,y=1260),plum,dict(type='coat-v2'),dict(type='coat-v2')],'material':[teal,fill_triangle(mountain)],'final':[plum]+cuts+cuts,'hand':views([])['hand'],'returned':views([])['returned']},'Reverse palette: sea-green peak on plum,then sharp plum outside cuts. Dark field is the tested masking fallback; actual no-halo/Hand checks required. Shape and palette both change.',True)
    cap=[[540,1050],[455,1230],[625,1230]]
    save('d19-c02-a02',{'snow':[white,fill_triangle(cap),plum]+cuts+cuts,'final':[],'hand':views([])['hand'],'returned':views([])['returned']},'White snow cap on sea-green peak/plum sky. Contain cap and preserve all margins. Actual quality required.',True)
    (R/'attempts/d19-c02-a01/PREFLIGHT-NOT-EXECUTED.md').write_text('Unexecuted original green-background cap proposal superseded after actual c01 palette/cleanup failure. Use c02-a02 only after accepted c01-a02.\n')
