"""Fifth alternative subtracts weight instead of adding decoration."""
from prepare_d17 import save,views,plum,ellipse,stem,petal,opening,spadix
if __name__=='__main__':
    save('d17-c05-a06',{'leaf-cut':[plum,ellipse(350,1600,170,100)],'stem':stem,'petal':petal+opening,'final':spadix,'hand':views([])['hand'],'returned':views([])['returned']},'Curve the leaf underside to replace the heavy straight-bottom triangle with a markedly slimmer flowing blade. Replay stem/bloom. Must improve actual silhouette and retain leaf attachment.',True)
