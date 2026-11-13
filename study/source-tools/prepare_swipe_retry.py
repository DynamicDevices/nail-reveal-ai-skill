from prepare_d14 import *
fixture=json.loads((R/'attempts/swipe-restored-fixture/stages.json').read_text())
save('swipe-restored-fixture2',fixture,'Fresh identical oval after rejected1200ms candidate; inspect before corrected3600ms masks. No cycle.')
save('swipe-candidate-native3600',{'final':[black]+[dict(type='native-swipe',start=[240,y],end=[840,y],duration_ms=3600) for y in (1130,1210,1290,1130)]},'Increase actual native contact duration threefold to address incomplete opacity; same four rows and clean fixture. Quality first. No cycle.')
