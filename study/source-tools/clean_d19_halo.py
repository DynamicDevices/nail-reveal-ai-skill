"""Uncounted changed cleanup hypothesis: seal the old dark footprint first."""
from prepare_d19 import save,cuts,teal,white,views
if __name__=='__main__':
    save('d19-c01-halo-undercoat',{'white-undercoat':[white]+cuts+cuts,'green-recoat':[teal]+cuts+cuts,'final':[],'hand':views([])['hand'],'returned':views([])['returned']},'Same exact outside edges with white undercoat before green; test whether old dark triangle halo disappears. No cycle credit; cause not assumed.')
