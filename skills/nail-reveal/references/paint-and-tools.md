# Paint contact, removal and cleanup tests

Tested on Nail Reveal 1.25, Android 15, physical 1080×2400, tall second nail,
painting stage. Do not generalise these results to other stages or versions.
The test used a visually white opaque base, blue polish and eight isolated
marks. Attempts and screenshots were retained privately; original videos are
not part of the portable/public skill.

## Does DOWN paint without movement?

Yes: stationary DOWN/hold/UP contacts produced paint without any MOVE event.
No source code was inspected, so describe observed contact-painting behaviour,
not a proven internal spray implementation or a guaranteed minimum duration.

| Requested sleep while held | Stationary blue pixels | With one 20-pixel MOVE |
| --- | ---: | ---: |
| 0.05 s | 0 | 0 |
| 0.25 s | 17,878 | 18,838 |
| 1.00 s | 19,834 | 22,968 |

Stationary contacts were at x=350; moving contacts started x=700 and moved to
x=720. Rows used touch y=900,1300,1700 respectively. Moving cases split the
requested sleep equally before/after MOVE. Actual contact includes Android
command overhead and was not measured independently. Single samples, not a
statistical threshold study. Never assume 0.05 seconds will always leave no mark.

Stationary 1-second dots were denser and only modestly larger than 0.25-second
dots. Mean blue-minus-red signal in the same crop rose from 0.146686 to 0.189993.
This supports a mostly fixed brush footprint with accumulation, rather than an
ever-expanding spray. It does not prove the implementation or isolate frame rate.
Movement elongated the footprint. A roughly 120-pixel upward paint/contact offset
was visible in this layout; do not mistake touch coordinates for paint centre.

Measurement: original PNGs, isolated 220×220 crops centred at (touch x,touch y-120).
Count pixels where normalised B-R>0.08, B-G>0.04 and R<0.95. Early larger crops
included neighbouring marks and were rejected. Counts are thresholded image
measurements, not exact brush masks or game-engine values.

## What the five left icons actually established

| Icon, top to bottom | Selected tool | Observed effect on fresh painted polish |
| --- | --- | --- |
| 1, about (100,650) | E-file/drill | Removed blue AND the white base coat, exposing pink natural nail |
| 2, about (100,800) | Nail file | Crossed a test dot; its measured blue area/signal stayed unchanged |
| 3, about (100,950) | Cone Bit | Locked during the painting-stage test; later unlocked at Level2 and completed its dedicated tidy-base preparation stage. Painted-polish removal remains untested |
| 4, about (100,1100) | Pink buffer block | Crossed the same test dot; blue area/signal stayed unchanged |
| 5, about (100,1260) | Polish brush | Paints on held contact; background-colour overpainting can trim a coloured mark |

These are not five proven brush widths or five polish erasers. File/buffer may
have useful preparation-stage functions, but those broader functions were not
established by this painting-stage test. The locked Cone Bit cannot be called
a delicate remover until painted-polish removal is actually tested. Later
preparation-stage use is documented in [the study findings](generative-study.md).
Do not accept ads,
buy an upgrade or bypass progression as an implicit part of tool inspection.

Two matched 0.25-second stationary blue controls were at (540,1100) and
(540,1500). The buffer crossed the first with DOWN(450,1100), MOVE(540,1100),
0.5-second dwell, a contact screenshot, MOVE(630,1100), 0.5-second dwell, UP.
The file repeated that path. A contact screenshot confirmed each tool overlapped
the target. Buffer and file both left blue area at 18,672 pixels and mean
blue-minus-red at 0.146131. Do not call a miss a successful no-effect test.

The drill used the equivalent path at y=1500 on the second control. Blue area
fell from 18,499 to zero and the visible surface became pink, not white.
It stripped the coat rather than restoring the painted background.

Brief stationary drill follow-up: requested 0.05-second hold at (540,1100) left
18,672 blue pixels and no pink pixels in the target crop; a 0.25-second hold
at (350,1300) removed all 17,878 blue pixels and exposed 23,695 thresholded pink
pixels. The latter removal extended beyond the mark. These two controls were
separate but similarly prepared; exact contact time and a safe fine-erasing
threshold remain unknown. Do not use an assumed short-contact threshold as a
protection against unwanted removal.

## Practical cleanup that preserved the background

Select the brush, choose the SAME white as the base, and hold at (630,1700)
for a requested 1 second before UP. This overlapped the left side of the
1-second moving blue mark and made a clear white crescent cut into it.
In a matched 210×200 crop at (590,1490), blue coverage fell from 22,570 to
14,576 pixels; thresholded pink pixels remained zero before/after. The visible
result agrees: white background was restored rather than natural nail exposed.
The smaller crop excluded an existing drill hole and the idle tool graphic;
the first larger crop falsely counted those as pink in the cleanup region.

For a flat-colour base: paint the motif, then use its known background colour
to overpaint unwanted fringe, in short controlled contacts/paths. Inspect after
each new edge. This is painting over, not transparent erasing; it cannot restore
unknown textures, gradients, decals or lower layers. Do not use the drill unless
stripping all coats in that area is intended. Fine details and sharp diamond
corners still need better control than this broad brush has demonstrated.

## Recovery encountered during these tests

The persistent ADB shell and recorder exited across an interruption. No cleanup
completion marker or expected PNG existed; a fresh full screenshot still showed
the pre-cleanup state. Recording was restarted before touches and the unfinished
brush test ran through a fresh ADB invocation. The earlier recording was retained;
do not claim one uninterrupted recording. A lost process handle does not by
itself prove which actions completed. Inspect effects and artifacts before retry.

Assisted-by: Briar
