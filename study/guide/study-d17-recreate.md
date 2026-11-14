# D17 — Gold-edged calla-inspired flower on plum

Five accepted improvements; study85/100. An abstract crescent flower, not
botanical realism. Beauty judgement: Briar, not Alex's endorsement. One decorated
nail, not one of the requested complete-hand sets. Publication remains pending.

Tested1080×2400 layout. Brush1001260,drill100650,palette2302200,close5401740,
0.7s settling. Plum2501560,white3901560,gold6851265,green2501410.
Paint roughly120px above contact, nominal radius80px: estimates, not an API.
Exact points, dwells, ordering and screenshots live in each retained stages.json.

1. d17-clean-base: strip previous nail with drill coat-v2; brush plum coat-v2
   twice. Inspect whole nail for old motif remnants before continuing.
2. d17-baseline: white contact ellipse centre5201050,radii110×190; vertical
   fill520860→5201240. Record and inspect Hand; baseline is not a cycle.
3. c01-a01: plum ellipse6101010,radii100×140 and fill610870→6101150.
   This carves an asymmetric crescent petal, with whole tapered ends.
4. c02-a01: gold615900→6151160,then plum650900→6501160. The overlapping
   mask leaves a slim gold centre. Inspect white base continuity and both tips.
5. c03-a01: green5751300→5751640,plum6101300→6101640. Replay petal,
   opening and centre after overlapping masks. Stem must connect beneath bloom.
6. c04-a02: fill green triangle[(550,1540),(320,1300),(360,1530)]. Plum
   cuts are80px outward from each edge, extended250px beyond both endpoints;
   repeat cuts twice. Replay stem,petal,opening,centre. Inspect leaf root and tip
   in actual Hand before another layer. Exact rounding in revise_d17.py.
7. Physical c05-a04 is REJECTED: white5701220→6401140 and plum660960→7601090
   made a bulky mitten-like lip. It stayed contained but was not prettier.
   d17-restore-c04 replayed exact petal/opening/centre while leaving untouched
   stem/leaf. Recorded restoration60.84s; closeup and Hand inspected before retry.
8. Accepted c05-a07: gold ellipse5201050,radii135×215; fill520835→5201265.
   Replay original white petal,plum opening,gold centre/plum trim. This exposes
   a continuous gold outer frame, echoing the centre without broadening the
   white petal. Hand verified whole tips and visible surrounding plum.
9. Glaze ONLY after the five accepted changes: Lamp6902200,wait3s,capture Hand;
   Hand3802200,wait3s,capture closeup. No Done or saved-gallery persistence test.

To recreate the final design directly: clean plum, accepted leaf/cuts, stem,
gold outer frame,white petal,plum opening,gold centre/plum trim. Keep the study
sequence above for comparisons; never replay rejected lip as part of final art.

Unexecuted proposals are not physical failures or cycles: c04-a01 disconnected
right leaf; c05-a01 inherited leaf/vein problems; c05-a02 broad gold vein;
c05-a03 petal mask erased centre; c05-a05 too-small leaf change;c05-a06 detached
leaf. Their recipes and sketches are preserved, labelled NOT GAME/NOT EXECUTED.
Flat sketch uses opaque radius80 and upward offset120 with approximate colours;
no actual opacity,shading,nail silhouette or Hand projection. It catches some
mask conflicts but cannot certify beauty, margins, timings or game behaviour.

All physical attempts retain silent creation.mp4,execution.json,recipe.json,
stages.json,original PNGs and mapped crops. Nail crop origin140400,size800×1700
→400×850. Hand detail origin3101000,size140×160→560×640,scale4. These are
different projections. Original evidence:work/generative-study/attempts.
Accepted fifth recording81.99s; restoration and rejected work are additional.
No matched workflow-speedup claim follows from using sketches or these timings.

The useful failure: preserving pixels and staying within the nail are necessary
but not enough. A bulkier recognisable flower can still be less beautiful than
a restrained abstract one. Restore the actual previous best before changing tack.

Assisted-by: Briar
