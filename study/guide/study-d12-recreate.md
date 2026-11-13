# D12 — Scarlet, black and white koi on teal

Five accepted improvements. Study total60/100. This is a graphic koi-inspired
fish with one stylised eye, not realistic anatomy or an exact koi variety.
Beauty judgement is Briar's, not Alex's endorsement.

Calibrated1080×2400 painting layout, brush1001260,palette2302200,close5401740,
0.7s settling. Teal2501410,white3901560,scarlet8301115,black8301560. Paint appears
roughly120px above contact. Exact physical stage JSON is retained for every trial.

Local geometry: P(u,v)=(540+u cosφ−v sinφ,1150+u sinφ+v cosφ),φ=−20degrees;
round to integer physical coordinates. This keeps markings aligned to the body.

1. d12-clean-base: drill strip, brush teal twice; inspect clean.
2. d12-baseline: filled white contact ellipse centred5401150,radii65×180,
   rotated−20degrees. Dense outer/inner paths and centre fill.
3. c01-a01 long tail FAILED sidewall check in c01-margin-check. Restore actual
   baseline via restore-d12-baseline-after-tail (teal twice,original body).
4. c01-a02 accepted tail: white paths P(0,230)→P(±70,330); teal hold P(0,410),1s
   cuts the fork. Recorded no-Lamp Hand check confirms teal around both lobes.
5. c02-a01: scarlet P(0,0),1s, fully inside white body.
6. c03-a02: white fin material around local(±90,70)→(±155,105); teal paths80px
   along outward normals of triangle edges toward tips(±220,100),two passes.
   Restore original white body, accepted SHORT tail/fork, then scarlet patch.
   Recorded Hand confirms pointed connected fins/margins. No extra finishing.
   c03-a01 was NEVER EXECUTED: superseded because it replays the rejected long tail.
7. c04-a01: black P(25,125),1s, contained lower dorsal patch.
8. c05-a01: black P(−30,−100),1s, then white P(−10,−80),P(−50,−80),P(10,−120),
   each1s. Three contained overpaints leave a small eye sliver. Restore scarlet
   P(0,0),1s. This changes the dorsal overlap order to scarlet-over-black.
9. d12-glaze: Lamp6902200,wait3s,capture Hand. d12-glazed-closeup: Hand3802200,
   wait3s,capture closeup. No Done or saved-gallery persistence test.

All physical attempts retain original full PNGs, mapped400×850 nail crops
(origin140400,scale0.5),creation.mp4,execution.json,recipe.json and stages.json.
Hand-detail origin3101000,size140×160 scaled4× gives an unobstructed margin check.
Working source: work/generative-study/attempts; repository publication pending.
Baselines, rejected tails, inspections and restoration never add accepted cycles.
This is one decorated nail, not one of the requested final full-hand sets.

Assisted-by: Briar
