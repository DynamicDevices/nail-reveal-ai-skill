# D19 — Moonlit alpine peak and lake on plum

Five accepted improvements; study95/100. A clean stylised landscape,not a
physical lighting simulation. Beauty judgement:Briar,not Alex's endorsement.
One decorated nail,not a complete-hand set. Publication remains pending.

Tested1080×2400. Brush1001260,drill100650,palette2302200,close5401740,
0.7s settling. Sea-green2501410,plum2501560,white3901560,gold6851265,
light-blue3951410. The initial sketch green is much darker than the actual
palette; actual screenshots govern colour/beauty. Contact coordinates below.
Approximate brush radius80 and upward offset120 are estimates,not an API.

## Actual sequence, including the failed start

1. d19-clean-base: strip flacon; brush sea-green coat-v2 twice.
2. d19-baseline: plum fill triangle[(540,1050),(300,1560),(780,1560)].
   Broad rounded material reached the Hand sides. Baseline only,not accepted.
3. REJECTED c01-a01: sea-green cuts80px outward from triangle edges,
   extended250px beyond each endpoint,repeated twice. Shape became sharp and
   contained,but a dark rounded old-footprint halo remained outside it.
4. FAILED uncounted d19-c01-halo-undercoat: same cuts with white twice,then
   sea-green twice. Bright white path fringes remained. Recorded115.99s,not a
   cleanup success or extra cycle. Do not blindly repeat this approach.
5. d19-restore-baseline: full strip,sea-green coat-v2 twice,original broad
   plum triangle. Actual closeup and Hand checked: original material restored,
   no failed white paths. Recording78.44s. Not an accepted cycle.
6. Accepted c01-a02: full strip,PLUM coat-v2 twice,SEA-GREEN triangle fill,
   PLUM outside cuts twice using original exact geometry. Clean sharp peak and
   whole Hand margins,no visible old halo or white paths. Both palette and
   shape changed; do not claim an isolated opacity measurement. Recording126.28s.
7. c02-a02: white fill triangle[(540,1050),(455,1230),(625,1230)],then plum
   original external mountain cuts twice. Sharp contained snow cap with lightly
   curved snowline. Original c02-a01 green-background proposal NEVER executed.
8. c03-a01: gold hold680960,requested1s,UP. Whole warm disc above right
   shoulder,with plum gap from snow. First proposal called this a sun; against
   the accepted plum palette we describe it as a moon-like light source.
9. c04-a01: light-blue ellipse5401700,radii180×60,fill3601700→7201700.
   Whole lake with narrow plum shoreline below mountain. Mild internal blue
   tonal variation remains; no claim of perfect flat-colour rendering.
10. c05-a02: gold5001680→6801680,then light-blue4901695→6901695. Thin
    elongated glint,contained inside lake. Actual Hand checked. Original
    c05-a01 heavy arch was rejected in sketch only,NEVER on phone.
11. d19-glaze:Lamp6902200,wait3s,capture Hand. d19-glazed-closeup:
    Hand3802200,wait3s,capture closeup. No Done or saved-gallery persistence test.

For direct final recreation: clean plum,sea-green triangle,plum cuts,white cap,
plum cuts,gold disc,blue lake,gold glint/blue trim. Use retained stages.json
for exact scanline fills,rounding,point spacing,passes,dwells and layer order.
prepare_d19.py retains initial proposal; revise_d19_palette.py contains the
accepted palette repair; refine_d19_reflection.py contains accepted glint.

## What this taught us

Same-colour overpainting is not a universal eraser. The pale-green cleanup kept
the old material's halo; adding white underneath made brighter remnants. Dark
plum masking worked for this actual rebuilt candidate. Exact game blending,
material effects and colour-specific footprints remain unproved. Do not turn
one success into a promise that every dark colour fixes every edge.

The failure mattered more than a neat geometric sketch: the opaque flat model
could not predict it. Both original and reversed-palette sketches are preserved,
labelled NOT GAME. No nail silhouette,opacity,shading or Hand projection was
simulated; no cycle/beauty/timing proof follows from them.

Every physical attempt retains silent creation.mp4,execution.json,recipe.json,
stages.json,original PNGs and crops in work/generative-study/attempts.
Nail crop origin140400,size800×1700→400×850. Hand detail origin3101000,
size140×160→560×640,scale4. Different projections; don't interchange coordinates.
Durations above are recorded attempt durations,not measured total design time
or a matched whole-workflow speedup. Failures,cleanup and restoration do not count.

Assisted-by: Briar
