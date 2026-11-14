"""Uncounted interior density correction, preserving the tested rim geometry."""
from prepare_d18 import save,inset,views
if __name__=='__main__':
    save('d18-c01-density-cleanup',{'inset':inset,'final':inset,'hand':views([])['hand'],'returned':views([])['returned']},'Additional same-black inset passes remove faint interior ring traces; no new shape or improvement-cycle credit.')
