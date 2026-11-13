
# Nail Reveal controls — draft

Use for explicitly requested Nail Reveal play, control calibration and recording.
This is a task-local draft, not an installed skill or a device authorisation.
Do not clear app data, purchase upgrades, change account/security settings or
publish recordings as part of painting. Retain the original attempts.

## Read and observe first

- Public description: https://play.google.com/store/apps/details?id=com.onteca.nailreveal&hl=en_GB
- The publisher site https://www.cgastudio.games had no visible Nail Reveal
  manual link when checked. Do not claim a full developer manual was read.
- The app's current client brief, step card and top hint are the main available
  gameplay instructions. Some top hints rotate or mention a different tool;
  use the step card and selected tool together to establish the current task.
- Calibrated against version 1.25 (code 25), Android 15, a 1080×2400 display.
  Recheck layout after an app version, display or orientation change.
- Use a screenshot after a meaningful transition. A scaled image shown in chat
  is not the physical touch coordinate system; use the original image dimensions.

## Record before experimenting

1. Confirm the intended serial with `adb devices -l`; specify it on every call.
2. Start `adb -s SERIAL shell screenrecord --bit-rate 6000000 --time-limit 0
   /sdcard/Download/UNIQUE_NAME.mp4` as a managed long-running command.
3. This phone's `screenrecord` help explicitly supports zero for no time limit.
   Do not assume other devices do. A default recording stops after 180 seconds.
   A zero-limit recorder nevertheless stopped across an interruption in this
   session. At each resumed work batch, confirm recording before any touch;
   restart if absent, and disclose gaps rather than claiming complete coverage.
4. Confirm its PID once before touching the app. Keep recording through failures
   and revisions. If a countdown is requested, give a real timed countdown first.
5. Stop the identified recorder with SIGINT, await its exit, pull the file and
   check the finished video's duration and streams. No audio was captured with
   this method. Preserve phone and local copies; sharing is a separate action.

## Tested controls on the calibrated layout

| Control | Physical tap coordinate | Observed result |
| --- | --- | --- |
| Settings | 960,190 | Sound, vibration, language, skin tone, native recording |
| Settings Done | 540,2015 | Returns to current game view |
| Hand | 460,2200 | Toggles close-up / whole-hand preview |
| Top nail thumbnail | 165,190 | Opens current client's brief, not nail selection |
| Colours | 310,2200 | Opens polish palette in close-up painting view |
| Choose colour | 615,1920 | Also opens palette during the painting step |
| Lamp | 615,2200 | Cure control; verify current step before use |
| Done | 770,2200 | Finish control; do not assume it exports or saves |

Tapping an index nail in the hand preview did not select it in the observed
one-nail client. The client brief identifies affected nails with pink dots.
On a two-nail client, close-up left/right arrows at 90,1440 and 990,1440 and
the dots above the toolbar show navigation. Read the current selected dot;
do not assume a right-arrow tap always returns to the first affected nail.
Starting the next client introduced a fifth toolbar button (Stickers), shifting
Colours to about 230,2200, Hand to 380,2200, Stickers to 540,2200, Lamp to
690,2200 and Done to 840,2200. Hand also opened skin-tone choices in that
layout. Treat the four-button table above as layout-specific, not universal.
Use current accessibility labels/bounds or the screenshot to establish controls.
If `uiautomator dump` cannot obtain idle state, discard its output file: it can
leave a stale hierarchy from an earlier screen. Use a screenshot instead.

## Palette and timing

- Wait for the palette to settle before choosing. In recorded tests, 0.7 seconds
  between opening, selecting and closing worked; this is a tested delay, not a
  proved minimum. Verify the actual screen if a tap appears ineffective.
- Client colour: approximately 390,945. Palette grid columns are approximately
  250,395,540,685,830; rows approximately 1120,1265,1410,1555.
- Row 1 contains nudes/pinks/red; row 2 burgundy/coral/orange/yellow/mint;
  row 3 teal/light blue/blue/lilac/purple; row 4 plum/white/grey/charcoal/black.
- Close: approximately 540,1730 after the modal has settled.
- Choosing a swatch does not itself recolour the nail: paint after closing.
  Existing strokes remain and can be overpainted with another colour.
- Rapid unobserved taps can hit the wrong state. A swatch name in a script
  is not evidence that the intended colour was actually selected.

## Process and controlled tests

The observed process is gel off → file/shape → buff → colour → top coat/cure.
After the first client, an optional sticker stage appeared before curing.
On a multi-nail client, complete the current stage on each affected nail before
the next stage begins. The step card can say "This nail's done! Tap ▶ for the
next one" while the overall stage remains unchanged. Check it after a batch.
Stages can advance automatically during a batch of strokes. Stop at each stage
boundary instead of sending tool gestures that may become painting gestures.

For painting, `input swipe X1 Y1 X2 Y2 DURATION_MS` gives a held moving contact.
Moving strokes of 900–1200 ms worked. The selected brush makes broad soft edges.
Three-hundred-ms long sweeps left gel gaps in a controlled preparation test;
do not shorten full-length gestures merely to reduce batch elapsed time.
For the tall nail, 1800–2000 ms vertical painting passes produced clear stripes.
Nails do not share one bounding box: the observed thumb ended around y=1660,
whereas the next nail extended to about y=2080. Re-map each nail's silhouette.
Short taps and zero-distance swipes were unreliable for dots in the initial
portrait; short moving strokes produced visible dots. These are observations,
not proof of the app's input implementation or a minimum contact duration.

Start with one colour, then a two-colour stripe, then a flag. Use overlapping
passes, inspect edges and record whether the app's completion differs from full
visual coverage. A "Colour complete" transition was observed before all visible
edge areas were painted. Inspect the actual nail, not only the completion badge.
The first single-colour test earned three stars while retaining an unpainted
rim. Subsequent canvas strokes were followed by a completed manicure without
an intentional lamp tap; the exact cure trigger remains unverified. Stop and
inspect on colour completion rather than assuming painting can continue.
Never label a test passed merely because commands returned success.

## Batch execution

Use [the persistent-shell procedure](optimisation.md). It supersedes repeated shell startup and long independent passes where the continuous-contact method has been tested. The older swipe recipe remains a fallback and evidence of the first flag attempt.

## Later study observations: client limits, Cone Bit and finishing

Normal job completion unlocked Salon Level2 and the Cone Bit. The next chip
repair×3 job had seven stages, inserting "Tidy the base" with the Cone Bit
between file/shape and buff. Selecting it at100,950 and using the tested
continuous traversal completed that preparation stage. This did not test its
effect on painted polish. Tool availability and the stage count can change.

The earlier chip repair×2 job allowed only thumb/index edits: repeated right
arrows alternated those two canvases, and the brief explicitly marked two nails.
Five visible nails or dot graphics do not prove five editable nails. Inspect
the brief and actual navigation before promising a complete-hand design.

In the study, Lamp690,2200 produced an explicit top-coat/cure completion in Hand.
Done840,2200 ended the job and changed the toolbar and editing state. These
observations do not prove saved-gallery persistence. After a subsequent job,
the next-client route presented "An ad is coming up" with a remove-ads purchase
and Continue. Stop at that boundary if ads/purchases are outside the owner's
permission; do not silently press Continue or use another route to bypass it.

## Multi-touch: documented, not yet exercised

The app says: "Use a second finger to turn the tool."
This suggests tool rotation; it does not prove pinch-to-resize or zoom support.
The installed Android `input` usage exposes single-pointer tap, swipe and
DOWN/MOVE/UP commands, with no pointer-ID or multi-pointer arguments. Running
two swipes concurrently is not a verified two-finger gesture. Do not root the
phone, change protections or install an input injector without separate scope.
Use a supported multi-pointer tool if available, or request a manual two-finger
demonstration and record the result. Keep rotation, brush size and zoom unknown
until actually observed.
