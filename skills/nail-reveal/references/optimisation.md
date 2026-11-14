# Efficient ADB nail creation

## Fallback ladder

Optimisation must not become a prerequisite for using the skill. Start with
supported mechanisms, retain the working baseline, and disable only the failed
speedup. Do not install a daemon, inject privileged input, change security
settings or silently add dependencies to preserve a speedup.

| Optional speedup | When it fails or is unsupported | Baseline to use |
| --- | --- | --- |
| Persistent control shell | Disconnect, unusable stdin, missing marker, or terminal API cannot retain a process | Inspect current state, then use a fresh `adb -s SERIAL shell` invocation for the next unfinished action/batch |
| Multiple actions per batch | Effects are unclear, modal appears, or stage/tool changes unexpectedly | Inspect, then send one known action per invocation and inspect its result |
| Continuous DOWN/MOVE/UP painting | `motionevent` unsupported, contact continuity uncertain, or coverage inadequate | Release any held contact if supported; inspect; use the previously tested individual `input swipe` recipe with its original timings |
| Resized previews/image conversion | Converter missing, output invalid, or detail insufficient | Inspect the original PNG at its physical dimensions; no image package is required |
| Region-only image inspection | Crop omits relevant state, unexpected overlay appears, or coordinate mapping is uncertain | Inspect the retained full frame; recalculate the crop before resuming |
| Accessibility hierarchy | Idle timeout, missing/invalid dump, or suspected stale file | Use a fresh screenshot; never reuse the failed dump |
| Agent screenshot inspection | Agent cannot open or interpret the image | Ask the human to inspect and describe the current state; stop unattended input until state is clear |
| Unlimited screen recording | Device rejects zero limit or recorder exits | Use the device-supported finite limit; verify startup, stop paint before expiry, finalise the segment, and start the next segment before resuming |

Fallbacks preserve the same chosen device, authority, privacy and dialog rules.
If ADB is unavailable/unauthorised or a fresh screenshot cannot establish state,
stop and help the human restore access. Do not switch devices automatically.
If recording cannot be restored, pause experiments and ask before proceeding
unrecorded; never describe missing footage as recorded.

### Recover without duplicating actions

1. Stop sending dependent commands. Save the error and last completion marker.
2. If DOWN may still be held, send UP at the last known position through the
   working transport where supported. If release/state cannot be established,
   ask the human to release/inspect the phone before continuing.
3. Obtain a fresh screenshot. Establish the tool, stage, selected nail, palette
   or dialog, current paint and recorder state. Successful transport alone is
   not evidence that the game action completed.
4. Choose the applicable baseline above. Resume only unfinished actions from
   the observed state. Do not blindly retry palette taps, navigation, curing,
   completion, purchases or an entire partly painted recipe.
5. Inspect the recovered result. Record the failed speedup and actual fallback
   used in the existing test notes. Do not repeatedly retry an unchanged failure.

### Platform limits and evidence

`adb -s SERIAL shell input tap X Y` and
`adb -s SERIAL shell input swipe X1 Y1 X2 Y2 DURATION_MS` are the baseline
host invocations; ADB sends those Android commands from Linux or Windows.
Android command availability still needs checking on the actual device.
The retained [French tricolour recipe](recipes.md) records successful separate
1800–2000 ms paint swipes and 0.7-second palette delays on the calibrated phone.
Use those known timings rather than substituting the failed 900 ms shortcut.
Preparation swipes have different tested timings in [controls](controls.md).
All coordinates remain layout-specific; a fallback does not validate geometry.

Shell syntax is not a cross-platform API. The examples below execute inside
Android's shell, not PowerShell/cmd.exe. If a host cannot preserve quoting for a
compound command, send individual ADB invocations instead. Capture PNG bytes
with a binary-safe process/file API, or have the human run the equivalent
trusted command; never silently use text decoding/redirection that corrupts them.

Live evidence currently covers the Linux host and the specified Android phone.
Windows execution, injected disconnect recovery, recorder-limit recovery and
other-device compatibility have NOT been tested. The fallback policy is now
documented; it is not evidence that those failure cases have passed live tests.

## Keep the control connection open

Open one managed terminal/process:

```sh
adb -s SERIAL shell
```

Keep its process/session handle. Send subsequent control batches to that same
stdin; do not start another `adb shell` for each batch. Do not share its stdin
between workers or send a second batch before the first completion marker.
Never insert untrusted game text into shell commands.

Wrap each finite batch with an explicit exit-status marker:

```sh
(input tap 230 2200 && sleep 0.7)
batch_rc=$?
printf '\nNAIL_BATCH_001_DONE:%s\n' "$batch_rc"
```

Use a new marker per batch. Read through the matching marker, not merely the
prompt. A missing marker/disconnection is an unknown partial result: inspect
before retrying. Preserve stderr. Do not send unknown modal actions as a batch.

This avoids repeated host/ADB shell setup, but Android still starts each
`input` command. Persistent-shell latency improvement has NOT yet been measured
against a matched fresh-shell batch. Do not claim otherwise.

## Separate screenshots from terminal output

Use a separate host command and a fresh file:

```sh
adb -s SERIAL exec-out screencap -p > capture.png
```

This is a POSIX-shell example. On Windows, use a binary-safe subprocess/file
writer; do not assume older PowerShell redirection preserves PNG bytes.
Never mix PNG bytes into the interactive shell/PTY. Keep physical dimensions
for touch coordinates; reduced previews are only for inspection. Accessibility
dumps are optional; animated scenes can fail idle detection and leave stale XML.

## Focused image inspection

Keep the original full-frame PNG locally, but normally present only the region
needed for the next decision to the agent's image viewer. Nail art needs the
whole nail silhouette and edge coverage, not the rest of the phone interface.
Palette selection needs all relevant swatches and the close control; dialog
classification needs its full text and choices, not just a button crop.

Inspect the full frame at initial/resumed state, unfamiliar stage/tool changes,
unexpected outcomes or suspected overlays. A crop cannot establish that no
off-crop dialog/control exists. Do not continue blindly because the last crop
looked unchanged. Expand the view whenever missing context could affect input.

One tested-layout painting crop from the physical 1080×2400 screenshot:

```sh
magick capture.png -crop 800x1700+140+400 +repage -resize 400x850 nail.png
```

This crop's physical origin is (140,400) and preview scale is 0.5. A preview
point (u,v) therefore maps to phone coordinates (140+2u,400+2v). For a general
crop (x0,y0,w,h) displayed at (W,H), map x=x0+u*w/W and y=y0+v*h/H.
Record these values when the crop is created; never apply crop coordinates
directly to ADB. Remap after orientation, layout or nail changes.

ImageMagick is optional. Use an existing image-viewer crop/zoom or another
available binary-safe image tool; if unavailable or inadequate, inspect the
original image. Do not install a daemon or image dependency merely to retain
this speedup. The intended reduction is irrelevant image content; actual image
analysis latency improvement has not been measured.

Do not assume converter startup is the delay. In the observed host workflow,
saved-image crop operations took milliseconds while some interactive-output
reads waited seconds. Where supported, combine finite command completion,
capture, crop, measurement and image display into one host/tool call. Retain
state boundaries; do not compensate by sending unknown actions blindly.
An existing in-process cropper can be optional, but do not install a daemon
or dependency simply to replace a working millisecond-scale crop. The available
persistent JavaScript runtime failed to load its cropper because of a package
import restriction; the working ImageMagick route remained the fallback.

## Maintain contact instead of repeating isolated swipes

On the tested Android 15 phone, separate `input motionevent DOWN`, `MOVE`, and
`UP` commands maintained one contact through a serpentine paint path. This is
single-pointer input, not multitouch. Keep the chosen paint colour throughout
the batch. Inspect after a colour change before attempting an unfamiliar path.

Continuous paths must start inside the paintable canvas, not on a toolbar.
Avoid DOWN on cards/buttons. MOVE can cross overlays during an existing drag
on this tested layout, but that is not a guarantee for another layout/app.
Finish with UP; if the batch fails or is interrupted, explicitly send UP at the
last known coordinate before changing tools or exiting. Then inspect.

### Observed blue-base path (layout-specific)

Preconditions: tall second nail selected, painting stage, fifth tool/brush,
blue selected and palette closed, 1080×2400 physical screen, recorder running.
Other layouts need new silhouette mapping. These are not normalised coordinates.

1. DOWN at (230,850); MOVE to (230,480); dwell 0.15 seconds.
2. MOVE down through y=1000,1500,2170; dwell 0.2 seconds.
3. MOVE across to x=360, then up through y=1500,1000,480; dwell 0.2 seconds.
4. Repeat alternating directions at x=490,620,750,880, with the same intermediate
   y points and a 0.2-second dwell at each vertical endpoint.
5. UP at (880,480). Inspect the whole silhouette and the current stage.

The measured batch used separate `input motionevent` calls in one **fresh** ADB
shell. It took 3.216 seconds of host wall time, excluding screenshot/inspection.
It overpainted an already painted French tricolour; this was not a blank-nail
test. It produced near-complete blue coverage, including much of the previous
unpainted lower rim. No pixel-level coverage measurement was performed.

### What the necessary tests established

| Test | Host command time | Observed result |
| --- | --- | --- |
| Select blue, close palette, two 900 ms swipes | 3.522 s | Middle covered; endpoint gaps |
| One extended 900 ms swipe | 0.983 s | Better lower reach; gap remained |
| Six-column continuous-contact blue batch | 3.216 s | Much fuller base; small edge quality limits remain |

These are different workloads, not a controlled speedup ratio. The historical
French flag used six 1800–2000 ms swipes plus palette actions; its comparable
total wall time was not measured. Do not claim a whole-nail speedup from these
numbers or confuse command time with human/model/inspection time.

## Where to inspect and stop

- Batch known strokes for ONE colour/stage; one screenshot afterwards.
- Tool changes, palette changes, dialogs and automatic stage advancement are
  boundaries until their exact sequence has been verified.
- Keep palette settling delays that have worked (0.7 seconds); reduce them
  only in a controlled test, not by assumption.
- Do not run status polling/watchers. A finite completion-marker read is not
  permission for an autonomous loop. Use one startup recorder check and another
  at resumed test batches; keep recording gaps explicit.
- Do not root, change security settings or install a privileged input injector
  just to save time. A game score is not evidence of visual coverage.

Assisted-by: Briar
