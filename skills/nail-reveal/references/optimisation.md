# Nail Reveal calibration and measured execution

Requires [the general skill](general-playtesting.md). General setup, persistent
shells, capture, contact safety, recording, recovery and crop mapping are owned
by its [canonical Android execution reference](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/android-execution.md).
This file retains only Nail Reveal observations/calibration. Historical generic
instructions remain in Git history, not as a second current procedure.

## Fallback ladder

Compatibility pointer for old recipe links: use the general skill's
[fallback ladder](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/android-execution.md#fallback-ladder).
For this game, the known individual-swipe baseline is the
[French tricolour recipe](recipes.md): 1800–2000 ms paint swipes and 0.7-second
palette delays on the calibrated phone. Preserve these until a controlled test
establishes a replacement. Missing dependency means stop, not copy a fallback.

## Focused image inspection

Compatibility pointer: the general skill owns
[image inspection and mapping](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/android-execution.md#focused-image-inspection).
For this 1080×2400 layout, the painting preview used physical rectangle
`x=140,y=400,width=800,height=1700`, displayed at 400×850 (scale 0.5).
Inspect the whole nail silhouette/rim, not only its painted middle. Palette
inspection needs the swatches/close control; modal classification needs full
text/options. These are game-specific regions, not a universal viewport map.

Observed crop operations on saved images took milliseconds while some tool
output reads took seconds. A persistent JavaScript cropper failed on a package
import restriction; ImageMagick remained the working optional fallback. Actual
model image-analysis latency improvement was not measured.

## Maintain contact instead of repeating isolated swipes

The tested Android 15 phone maintained single-pointer contact across separate
`input motionevent DOWN`, `MOVE`, `UP` calls. Continuous paths began inside the
paintable canvas. MOVE could cross overlays during an existing drag on this
layout; that is not a guarantee for other layouts or apps. Use the general
contact/recovery procedure, including explicit pointer UP; no multitouch is proved.

### Observed blue-base path (layout-specific)

Preconditions: tall second nail selected, painting stage, fifth tool/brush,
blue selected, palette closed, physical 1080×2400 screen, recorder running.
Other layouts need silhouette remapping. These are not normalised coordinates.

1. DOWN at (230,850); MOVE to (230,480); dwell 0.15 seconds.
2. MOVE down through y=1000,1500,2170; dwell 0.2 seconds.
3. MOVE across to x=360, then up through y=1500,1000,480; dwell 0.2 seconds.
4. Alternate directions at x=490,620,750,880 with the same intermediate y points
   and a 0.2-second dwell at each vertical endpoint.
5. UP at (880,480). Inspect whole silhouette and stage.

The measured batch used separate `input motionevent` calls in one fresh ADB
shell. Host wall time was 3.216 seconds, excluding screenshot/inspection. It
overpainted an already painted French tricolour, not a blank nail. Coverage was
near-complete with small edge limitations; no pixel-level coverage measure was made.

### What the tests established

| Test | Host command time | Observed result |
| --- | --- | --- |
| Select blue, close palette, two 900 ms swipes | 3.522 s | Middle covered; endpoint gaps |
| One extended 900 ms swipe | 0.983 s | Better lower reach; gap remained |
| Six-column continuous-contact blue batch | 3.216 s | Much fuller base; small edge quality limits |

These are different workloads, not a controlled speedup ratio. The historical
French flag used six 1800–2000 ms swipes plus palette actions; comparable total
wall time was not measured. Persistent-shell improvement over matched fresh-shell
work was not measured. Command time is not human/model/inspection time.

## Nail Reveal stage boundaries and limits

Tool/palette changes, dialogs and automatic stage advancement need actual state
checks until their sequence is verified. A score is not visual coverage. Inspect
real Hand projection before accepting silhouette extensions. Preserve 0.7-second
palette settling until tested otherwise. Injected-disconnect recovery, recorder
limit recovery, Windows and other-device compatibility remain untested.

Assisted-by: Briar
