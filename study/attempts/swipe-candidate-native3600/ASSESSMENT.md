# Usable optional speedup — limited straight-mask comparison

Stage18.122s versus dense23.533s:5.411s less,23.0% lower elapsed time,about1.30×
stage throughput. Same clean recreated oval,black colour,four row endpoints and
capture pipeline; contact timing differs intentionally. Single trial,not a
statistical claim or whole-design speedup. Video18.614644s is a different measure.

Visual dome edge is comparably clean. Thresholded gold lower contour at x350..730
in10px steps:reference y921..924,mean922.33;native3600 y924..926,mean924.79.
Thus native edge is about2.46 physical pixels lower,not pixel-identical. Contour
span2px versus reference3px; rejected1200ms span6px,mean928.59.

Discarded ROI350980,size350×130:all three have0 pixels with R−B>5 and G−B>3.
Second ROI350950,size350×120:3600 mean absolute RGB difference0.08,maximum5
versus reference. Small green-channel variations remain; moving nail highlights
mean full-frame pixel identity is not a valid requirement. These thresholds do
not certify all residue colours or general opacity. Visual judgement:Briar.

Adopt only as OPTIONAL comparable horizontal mask primitive on this tested
layout,using3600ms,not1200ms. For precise inherited edge positions use dense
paths. Diagonal/vertical/curved fills,other colours/devices are not validated.
On failure release/inspect partial effects,then use the known dense path for
unfinished work; do not blindly replay a whole batch. No daemon/Node/root added.
