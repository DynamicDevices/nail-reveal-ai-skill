# D16 — Gold-rimmed scarlet ladybird on porcelain

Five accepted improvements; study80/100. A bold enamel-brooch insect,not realistic
anatomy. Beauty judgement:Briar,not Alex's endorsement. One decorated nail,not
one of the requested complete-hand sets. Repository publication remains pending.

Tested1080×2400 layout. Brush1001260,drill100650,palette2302200,close5401740,
0.7s settling. White3901560,scarlet8301115,black8301560,gold6851265.
Paint~120px above contact; nominal brush radius~80px is an estimate,not an API.
Use retained stages.json for exact samples,passes,dwells and layer ordering.

1. d16-clean-base: strip D15,brush white coat-v2 twice; inspect clean.
2. d16-baseline: scarlet contact ellipse5401280,radii170×220,fill vertical
   x510/570,y1100..1460. Recorded Hand checks full shell/white margin.
3. d16-baseline-density: faint interior fill traces required two contained dense
   red serpentine passes,x450..630 every30px,y1140..1420 every20px. This is
   baseline cleanup,not an improvement. It is study.json's effective baseline.
4. c01-a01: black x595,y1140..1450,red x630,same y. Leaves a slender central
   division with tapered curved ends. Red masks stay inside the shell.
5. c02-a01: black horizontal470950→610950 gives connected rounded head.
   Hand inspection before acceptance verifies both sides and top margin.
6. c03-a01: black holds4101180,6701180,4101410,6701410,1s each.
   Four separate spots,none touching seam or outside field. Hand confirmed.
7. c04-a01: black curves x=500−20sin(πt) and590+20sin(πt),y=850+50t,
   41 samples each. White masks respectively35px right/left; replay black head.
   Hand confirms complete tips and open gap. Upper margin is small,not measured.
8. c05-a01 is REJECTED: white3701295/7101295,red4051295/6751295,spot replay
   makes white notches connected to the background,not contained reflections.
   Actual c04 restored via d16-restore-c04-after-glints:full strip/white/original
   shell+density/seam/head/spots/antennae replay. Inspected whole and clean;
   recorded146.57s. No cycle counted for rejection or restoration.
9. Accepted c05-a02: gold outer ellipse5401280,radii170×220; red inner ellipse
   same centre,radii145×195 plus fill x510/570,1100..1460. Repeat dense interior
   cleanup from step3. New seam black5951140..1420,red630,same range; head
   replay. Move spots inward:black4301200,6501200,4301400,6501400,1s each.
   This keeps a clean gold frame and separated black pattern. The shortened seam
   stays inside the inset red shell. Antennae survive unchanged. Hand confirms.
10. d16-glaze:Lamp6902200,wait3s,capture Hand. d16-glazed-closeup:
    Hand3802200,wait3s,capture closeup. No Done or saved-gallery persistence test.

To recreate directly,use clean white,accepted antenna/head geometry and the
gold-frame/red-inset/density/final-detail stages from c05-a02; retain the actual
study sequence above for comparisons. Do not use rejected white-notch recipe.
The accepted fifth attempt video is90.64s; this is not a speed benchmark.

All physical attempts retain creation.mp4(silent),execution.json,recipe.json,
stages.json,original PNGs and mapped crops. Nail crop origin140400,size800×1700
→400×850. Hand detail origin3101000,size140×160→560×640,scale4. Different
projections; do not reuse closeup mapping for Hand. Original evidence under
work/generative-study/attempts; preserve failed images and actual restoration.

Lessons:wide body/large separated spots suit the fixed brush. A white crescent
at the silhouette edge can read as damage rather than shine. A gold outline is
a different material treatment,not proof that every extra accent improves art.
Early Hand checks worked here for body,head and antennae; keep them before
acceptance whenever a new feature extends the silhouette.

Assisted-by: Briar
