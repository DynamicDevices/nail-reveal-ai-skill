# Recorded Japan and Brazil attempts

Tested on Nail Reveal 1.25, Android 15, physical 1080×2400, tall second nail,
painting stage, fifth tool. Both designs were captured and recorded privately,
then overpainted for the next experiment. Neither was cured or scored.
These are stylised nail designs, not exact flag proportions.

All points are physical touch coordinates. Paint appeared roughly 120 pixels
above contact in these tests; do not assume a touch point is the paint centre.
Recalibrate the silhouette and tool offset on another device/layout/tool.

## Shared opaque background

Use the [serpentine procedure](optimisation.md) with alternating vertical paths
between y=480 and y=2170, passing through y=1000 and y=1500 each time.
For stronger overlapping coverage, use columns:

`200,300,400,500,600,700,800,900,850,750,650,550,450,350,250`.

Begin DOWN at (230,850), MOVE to (200,480), dwell 0.15 seconds, then follow
the columns continuously. Dwell 0.2 seconds at every vertical endpoint.
Finish UP at (250,2170). Start inside the canvas, never on a toolbar.

Palette protocol: tap (230,2200), wait 0.7 seconds; select the swatch, wait
0.7 seconds; close (540,1740), wait 0.7 seconds. Current calibrated swatches:
white (390,1560), red (840,1115), muted green (250,1410), yellow (685,1265),
blue (540,1410). Do not reuse blindly on another palette.

For the mark paths below, DOWN at the first point, dwell 0.2 seconds, MOVE
through the rest, dwell 0.25 seconds, then UP at the last point unless stated.

## Japan

The first white six-column coat left visible UK-flag ghosts. The denser shared
background pass above removed them in the inspected image. This is an opacity/
coverage issue: do not accept the game badge as evidence of an opaque recoat.

Select red and draw this filled loop:

`(540,1350),(630,1350),(604,1414),(540,1440),(476,1414),(450,1350),
(476,1286),(540,1260),(604,1286),(630,1350),(540,1350)`.

The result was a recognisable red disc on white, with slightly uneven soft edges.
The initial white six-column batch including colour selection took 5.63 seconds;
the additional dense pass took 7.53 seconds; red selection/disc/capture took
4.43 seconds. These exclude inspection and conversation, not total creation time.

## Brazil

1. Select muted green and run the dense background pass. The available swatch
   is a pastel approximation, not the flag's saturated green.
2. Select yellow. Begin at (540,850), then fill alternating horizontal rows
   y=930,1010,1090,1170,1250,1330,1410,1490,1570,1650,1730,1810.
   At each row use left/right x=540±round(240*(1-abs(y-1350)/500)).
   Alternate left-to-right/right-to-left, staying DOWN through row changes.
   End at (540,1850), dwell and UP. This filled the diamond but left scallops.
3. Still yellow, smooth the outline with
   `(540,850),(660,1100),(780,1350),(660,1600),(540,1850),
   (420,1600),(300,1350),(420,1100),(540,850)`.
4. Select blue and draw
   `(540,1350),(650,1350),(618,1428),(540,1460),(462,1428),(430,1350),
   (462,1272),(540,1240),(618,1272),(650,1350),(540,1350)`.
5. Select white and draw a broad band through
   `(430,1310),(480,1315),(540,1330),(600,1360),(650,1390)`.
   This last path used 0.15-second initial/final dwells, not 0.2/0.25.

The result has the recognisable green/yellow/blue motif and broad white band,
but rounded diamond corners, pastel colours, no stars and no lettering.
Batch times: green selection/base/capture 10.68 seconds; yellow fill selection/
capture 5.42 seconds; yellow outline plus blue selection/disc/capture 5.46 seconds;
white band selection/capture 3.85 seconds. No matched speedup comparison was run.

## Cleaner captures

These final screenshots were taken inside the finite control batch, 0.15 seconds
after UP, using `screencap -p` to a unique phone-side PNG, then pulled through ADB.
This avoided the idle animated hint hand in these captures. It is not guaranteed
on another app version. Keep the full frame and inspect a mapped nail crop;
do not hold contact open merely to hide the UI. Retain the binary-safe host
`exec-out screencap -p` route as the fallback.

Assisted-by: Briar
