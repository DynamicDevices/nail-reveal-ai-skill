# Recorded designs: coat, cut and repaint

Three designs were made sequentially on the same tall second test nail in
Nail Reveal 1.25, Android 15, physical 1080×2400. Each was captured privately
before being overpainted. The final phone state was the sunset, still in the
painting stage. No cure, top coat, scoring, exporting or finished-manicure
persistence was verified. Do not call these tests proof of gel chemistry or
selective layer removal.

Use the [tool/contact findings](paint-and-tools.md),
[mapped image inspection and fallback ladder](optimisation.md), and
[dense background procedure](japan-brazil.md#shared-opaque-background).
Every point below is a physical contact coordinate, not a crop coordinate.
The rendered mark appeared roughly 120 pixels above contact in this layout.

## What is usable now

- **Brush:** adds colour on held contact. For a known flat background, repaint
  that colour over fringe to clean an edge. This does not restore unknown layers.
- **Drill:** strips both applied colours/base coats to pink natural nail. Use
  intentionally for negative space or a window that will be repainted.
- **File and buffer:** did not change the tested fresh polish. Their effects on
  preparation/shape/roughness are not established by these painting tests.
- **Cone Bit:** unavailable at Salon Level 1; a tap showed Level 2 unlock text.
  Do not claim it is a tested fine eraser, watch an ad or bypass the lock.

The practical pattern is **coat → intentional cut → repaint/mask → inspect**.
Do not try to correct the edge of a painted base with the drill unless exposing
natural nail is intended. It is not a colour-only eraser. For background-safe
cleanup, the known-background brush method was demonstrated separately.

## Shared primitives

1. Select the brush, choose the colour and close the settled palette. The
   calibrated palette waits were 0.7 seconds between opening, choosing and closing.
2. For a flat coat, use the dense 15-column serpentine in the linked background
   procedure, with its endpoint dwells and explicit UP. Inspect opacity before
   adding the motif; the old design should not remain visibly ghosted.
3. A circular path C(x,y,r) in these tests means DOWN at (x,y), initial dwell,
   then MOVE through right, southeast, bottom, southwest, left, northwest, top,
   northeast, right, centre. Cardinal offsets are r; diagonal offsets are
   round(r/sqrt(2)). End with a dwell and UP. The path radius is NOT the mark
   radius: the tool footprint adds to it. Stated radii are calibrated recipes,
   not a portable size setting.
4. Stop contact before capture, image processing, thinking or a human question.
   Do not leave DOWN active while another tool call runs: paint/removal can
   accumulate. These captures ran 0.15 seconds after UP and retained full frames.
5. Continuous paths are optional; use the fallback procedure when unavailable.
   The individual-swipe fallback has not independently reproduced these motifs.

Calibrated swatches: white (390,1560), black (830,1560), muted green (250,1410),
red (840,1115), yellow (685,1265), coral (395,1265). Palette opener (230,2200),
close (540,1740). Tools on the tested layout: drill (100,650), brush (100,1260).
Another layout requires remapping before input.

## 1. Crescent and pearls

- Apply a dense black coat. Inspect it before stripping.
- Select the drill; trace C(540,1300,110), with 0.25-second initial and
  0.3-second final dwells. This produced a round pink window through the coat.
- Restore the black brush; trace C(630,1250,100), with 0.25-second initial and
  0.5-second final dwells. The offset black disc masked part of the pink window,
  leaving a recognisable crescent. Inspect this overlap before decoration.
- Select white. Make stationary DOWN/1-second-hold/UP contacts at (700,800)
  and (350,1800) for two opaque pearl-like dots.

Observed result: pink negative-space crescent and two white dots on black.
Edges are soft; the narrow crescent ends are not precise vector cusps. This is
the demonstrated subtractive/repaint design, not an assumed selective eraser.

## 2. Five-petal flower

- Apply and inspect a dense white coat; the previous crescent was no longer
  visible in the inspected recoat.
- Select muted green. Draw these held paths with 0.25-second initial and
  0.4-second final dwells, UP between paths:
  - (540,1050),(540,1350),(560,1650),(580,2050)
  - (560,1670),(500,1610),(440,1550)
  - (570,1810),(630,1750),(690,1690)
- Select red. Make stationary 1-second contacts at
  (540,930),(654,1013),(611,1147),(469,1147),(426,1013), UP between each.
- Select yellow. A stationary 1-second contact at (540,1050) fills the centre.

Observed result: five round red petals, yellow centre, green stem/two rounded
leaves on white. The broad stroke makes a bold/cartoon flower, not fine botanical
linework. Deliberate held-contact dots avoided the old unreliable rapid taps.

## 3. Sunset inlay and mountains

- Apply and inspect a dense coral coat.
- Drill C(600,1550,110), with 0.25/0.3-second initial/final dwells, to expose a
  round pink window. Then use the yellow brush at C(600,1550,90) with the same
  dwells. The smaller painted trace left a pink halo around the yellow disc.
  This is an observed inlay-like visual effect, not a physical recess depth test.
- Select black. The silhouette's touch-coordinate profile was:
  (150,1920),(340,1640),(530,1920),(760,1500),(960,1850).
- Fill below that profile to y=2170 using alternating vertical paths at
  x=880,800,720,640,560,480,400,320,240,160. Interpolate the profile height at
  each x; pass through the midpoint of that height and 2170. Start DOWN at
  (880,1710), inside the canvas, with a 0.25-second dwell. Alternate down/up,
  dwell 0.2 seconds at each endpoint and stay DOWN through column changes.
- After the final column, MOVE along the profile points in order to smooth the
  upper outline. Dwell 0.3 seconds and UP at (960,1850). Inspect the full motif.

Observed result: coral sky, yellow sun/pink halo and two dark rounded peaks.
The broad footprint rounded the peaks and the right peak partly covered the
sun. Exact sharp silhouettes remain a limitation; no finer tool was assumed.

## Delivery and execution limits

Full-size recordings/screenshots stayed private. The portable skill should
contain original procedures/reference geometry, not these raw phone captures.
The three designs were not three simultaneous fingers or saved game slots.
Earlier images remain captures; replay is needed to recreate them in the game.

These experiments used finite fresh-shell batches with command completion,
capture, pull and crop combined in one host call. This retained the working
fallback after persistent-session loss and avoided interactive-output polling
between individual gestures. It is not a measured whole-session speedup ratio.
Use a retained control process only when the host can reliably manage its
lifetime/completion markers; speedups must never be required for portability.

Assisted-by: Briar
