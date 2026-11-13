"""Matched single-fixture comparison, outside accepted design cycles."""
from prepare_d14 import *
fixture={}
for a in ('d14-clean-base','d14-baseline'):
    for label,steps in json.loads((R/'attempts'/a/'stages.json').read_text()).items():fixture[a+'-'+label]=steps
save('swipe-reference-fixture',fixture,'Prepare the same gold oval on clean black for dense-path reference; no cycle.')
save('swipe-reference-dense',{'final':[black,row(1130),row(1210),row(1290),row(1130)]},'Reference: four identical600px horizontal mask rows,10px samples,0.4s endpoint dwells. Capture quality and elapsed stage time; no cycle.')
save('swipe-restored-fixture',fixture,'Physically recreate and inspect the same oval before native candidate; no cycle.')
save('swipe-candidate-native',{'final':[black]+[dict(type='native-swipe',start=[240,y],end=[840,y],duration_ms=1200) for y in (1130,1210,1290,1130)]},'Candidate: same rows/colour, native1200ms interpolation, no added endpoint dwells. Assess completeness/edge quality and actual stage time, not assumed equivalent contacts; no cycle.')
