# D01 baseline — Blush moon and pearls

Status: executed baseline, not an accepted improvement cycle. Study total: 0/100
accepted improvement cycles. No cure/top coat/persistent manicure was tested.

## Visual review by Briar

The blush crescent is readable against an opaque glossy black base, with useful
negative space. The two white circles give a clear diagonal but are too large
and stark: they compete with the moon rather than behaving as delicate pearls.
The crescent's outer edge is visibly soft and slightly polygonal, and its mass
leans left. This is a useful, genuinely considered baseline, not evidence that
project P0 has been met or that the design is brilliant. These are aesthetic
judgements, not objective measurements or Alex's approval.

Next candidate hypothesis: replace the eight-direction loops with more evenly
sampled curves, improve the moon's placement/proportion, and subordinate the
decoration. A colour change alone will not count. Compare the actual nail against
this saved image; reject regressions and replay this complete recipe if needed.

## Reproduction and evidence

Start in the calibrated tall-second-nail painting stage (1080x2400), brush
available, palette closed. Read `recipe.json` and `stages.json`; execute stages
in this order: black-base, crescent-cut, crescent-mask, pearls-final. The saved
`render_batch.py` compiles the exact finite fallback batches. Record before
touching. Full frames and cropped previews are retained; crop origin (140,400),
size 800x1700, preview 400x850 (scale .5). Pointer UP is explicit.

The initial interactive helper confirmed recording but never returned a paint
batch marker or expected capture. It was interrupted; a fresh capture established
the black canvas before any replay. Cause is not established. Its 319.706-second
recording is retained as `interrupted-creation.mp4`; it is not presented as
successful design creation. Recorder loss at interruption was reconciled.

The known finite ADB fallback then completed the design with a newly confirmed
recorder. `creation-segment02.mp4` contains that creation, including pauses;
duration 131.187 seconds. The black-base batch plus capture took 10.75 seconds;
cut 2.888, mask 5.384, pearls 6.145. These are different batch workloads and
exclude model review/conversation, so they do not establish a speedup ratio.
Every executed motif stage has its exact Android command file and batch receipt.
Final original: `pearls-final-gameplay.png`; mapped preview: `pearls-final-nail.png`.

The final white pearls are broad held contacts, not fine-point brush control.
The drill strips to natural pink; the black mask paints over part of that window.
No selective polish-only removal or brush-size setting was assumed.

Assisted-by: Briar
