# Recorded UK-flag painting attempt

Tested with Nail Reveal 1.25, Android 15, physical 1080×2400, tall second nail,
painting stage, fifth tool (polish brush), existing French tricolour overpainted.
The result was a recognisable stylised Union Jack with blue corners, a white
underlay, red diagonals and a red central cross. The red diagonal strips are
symmetric, not the flag's correct counterchanged/offset arrangement. Broad soft
edges and elongated proportions remain. The nail was left in painting stage;
no cure, score or saved-manicure acceptance was tested.

All coordinates below are physical phone coordinates. Another layout/nail needs
new mapping. The measured sequence is evidence, not permission to replay it.
Record experiments privately. Inspect the current state before each layer;
stop on an unexpected stage/dialog. Keep full frames but inspect the nail crop.

## Blue base

Select blue and close the settled palette. Use the six-column serpentine batch
in [optimisation](optimisation.md#observed-blue-base-path-layout-specific).
It took 3.216 seconds in a fresh shell, excluding capture/inspection, and
produced near-complete blue coverage on the already painted nail.

## Path execution

The white/red layers used the same persistent ADB control shell.
For each row below: DOWN at the first point, dwell 0.2 seconds, MOVE to each
remaining point in order, dwell 0.25 seconds at the last point, then UP there.
Use `input motionevent` only where the device supports it and the continuity
test has passed. These are single-pointer paths, not multitouch.
If interrupted, release contact and inspect before resuming; never replay all
layers blindly. Fall back to inspected individual swipes when needed, but that
fallback has not independently reproduced this UK design.

## White underlay

Open Colours at (230,2200), wait 0.7 seconds; select white at (390,1560), wait
0.7 seconds; close at (540,1740), wait 0.7 seconds. Choosing a colour alone does
not repaint the nail.

The first diagonal was tested and inspected separately. After that succeeded,
the remaining nine paths were sent as one finite batch, then inspected.

| Path | Physical points in execution order |
| --- | --- |
| First diagonal probe | (260,700), (450,1150), (650,1600), (850,2050) |
| Widen first diagonal | (195,700), (385,1150), (585,1600), (785,2050) |
| Widen first diagonal | (325,700), (515,1150), (715,1600), (915,2050) |
| Second diagonal | (755,700), (565,1150), (365,1600), (165,2050) |
| Second diagonal | (820,700), (630,1150), (430,1600), (230,2050) |
| Second diagonal | (885,700), (695,1150), (495,1600), (295,2050) |
| Vertical cross | (480,480), (480,1000), (480,1500), (480,2170) |
| Vertical cross | (600,480), (600,1000), (600,1500), (600,2170) |
| Horizontal cross | (180,1310), (430,1310), (680,1310), (940,1310) |
| Horizontal cross | (180,1430), (430,1430), (680,1430), (940,1430) |

## Red layer

Open Colours at (230,2200), wait 0.7 seconds; select red at (840,1115), wait
0.7 seconds; close at (540,1740), wait 0.7 seconds. Then execute these six paths
using the same dwell and UP procedure:

| Path | Physical points in execution order |
| --- | --- |
| Diagonal | (260,700), (450,1150), (650,1600), (850,2050) |
| Diagonal | (820,700), (630,1150), (430,1600), (230,2050) |
| Vertical cross | (510,480), (510,1000), (510,1500), (510,2170) |
| Vertical cross | (570,480), (570,1000), (570,1500), (570,2170) |
| Horizontal cross | (180,1350), (430,1350), (680,1350), (940,1350) |
| Horizontal cross | (180,1390), (430,1390), (680,1390), (940,1390) |

Android shell `time` reported 7.19 seconds real time for red selection/settling
plus these six paths. It excludes capture, agent inspection, earlier layers and
human conversation. It is not a matched persistent-versus-fresh-shell comparison
or a measured total-nail speedup.

## Evidence and limits

The first attempt was recorded and original/cropped screenshots retained
privately. No personal recordings or device identifiers belong in the public
skill. The crop used origin (140,400), size 800×1700, displayed at 400×850.
Preview coordinates require the mapping in [focused inspection](optimisation.md#focused-image-inspection).
The image included game hint/step-card overlays; coverage under them was not
fully visible in the final inspection. Do not call this a pixel-perfect, cured
or complete manicure.

Assisted-by: Briar
