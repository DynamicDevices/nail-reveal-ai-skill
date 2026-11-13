---
name: nail-reveal
description: Play Nail Reveal on an authorised Android phone using ADB, with efficient recorded batches and screenshot-grounded nail art.
license: MIT
compatibility: Requires a shell, Android Platform Tools (adb), an authorised Android phone with Nail Reveal, and screenshot inspection.
metadata:
  status: development-draft
  tested-game-version: "1.25"
---

# Nail Reveal

Use when the human asks you to play or make nail art in Nail Reveal.
This skill does not grant phone access, purchases, account changes or publication.
If you cannot run ADB or inspect screenshots, explain that limitation to the human.

## Start here

1. Have the owner connect and authorise their intended phone. Select an explicit
   serial from `adb devices -l`; never use an implicit default or publish serials.
2. Inspect the current game and physical screenshot dimensions. Read the client
   brief, selected tool and stage card; do not infer state from a rotating hint.
3. Start a private screen recording before experiments and confirm it is running
   once. Preserve failures and disclose gaps. Sharing is a separate decision.
4. Read [tested controls](references/controls.md) for the current stage and
   [efficient execution](references/optimisation.md) before painting.
5. Keep one ADB control shell open across finite batches. Capture screenshots on
   a separate binary-safe connection. Inspect after stage/modal/tool transitions,
   not after every known stroke. Stop dependent actions if a prerequisite fails.
6. Treat speedups as optional. Follow the [fallback ladder](references/optimisation.md#fallback-ladder)
   when a platform or device cannot support them. Reconcile partial effects first;
   never replay a whole batch merely because its completion marker was lost.
7. After known actions, inspect only the relevant image region: nail silhouette
   for painting, palette for colour, or dialog for its choices. Retain the full
   capture and crop/scale mapping. Use full-frame inspection for initial state,
   unfamiliar transitions, suspected dialogs or uncertainty. See
   [focused image inspection](references/optimisation.md#focused-image-inspection).

## Important findings

- The left icons change tools, not demonstrated brush sizes. On the tested
  five-icon layout: drill, nail file, Cone Bit offer, pink buffer, polish brush.
  First/second findings come from the earlier test; fourth/fifth were confirmed
  in the optimisation session. Decline understood offers; do not watch ads.
- Read [paint/contact and tool tests](references/paint-and-tools.md) before
  cleanup. The drill removed both polish and base coat, exposing pink nail;
  the file and buffer left the tested polish dots unchanged. The Cone Bit was
  locked until Salon Level 2. Do not call these five interchangeable erasers.
- Use the fifth brush for polish on this layout. Icon positions can change.
- An uninterrupted DOWN/MOVE/UP path produced near-complete blue coverage much
  faster than the older independent long-pass approach, on the tested nail.
  Do not generalise that result to preparation tools or another device.
- Shorter swipes alone left endpoint gaps. Keep contact through turns and allow
  short endpoint dwell; inspect the actual painted silhouette, not game score.
- Held contact can paint without movement. Requested 0.25-second and 1-second
  holds produced dots; 0.05-second holds did not in this test. Longer holds
  increased density more than size. These are observations, not a minimum-time
  guarantee; avoid leaving DOWN active while thinking or running other tools.
- Use explicit pointer UP even after a failed continuous-contact experiment.
  Do not replay a partially completed batch without checking the screen.
- The portable baseline is explicit-serial ADB taps and individual held swipes,
  original PNG screenshots, and human inspection when agent image access fails.
  Persistent shells, continuous paths and image resizing are optional speedups.
- Informational, purchase, ad, consent and account dialogs are different states.
  Read before dismissing; stop for human help if the choice is unclear.
- Multi-touch rotation and brush-width adjustment remain unverified. Parallel
  ADB swipes are not a verified two-finger gesture.

## Exercises and remaining work

Start with a single coat, then bands, then the [tested French tricolour recipe](references/recipes.md).
The [first recorded UK-flag recipe](references/uk-flag.md) produced a recognisable,
stylised Union Jack. Exact proportions, offset diagonals and curing remain unverified.
The [Japan and Brazil attempts](references/japan-brazil.md) added round marks,
overlapping recoats, diamond fills and outline smoothing. Brazil uses approximate
colours and has no stars or lettering. These designs were not cured.
For non-flag art, use the [recorded coat/cut/repaint designs](references/design-lab.md):
a negative-space crescent, a five-petal flower, and a sunset inlay with mountains.
Keep painting-stage results separate from unverified gel/cure/top-coat behaviour.
Read [Linux/Windows setup](references/setup.md) before first use. This experimental
skill uses ordinary ADB; no packaged agent-specific helper or daemon is required.
Windows/device-specific behaviour still needs live validation.

Keep original photos, recordings, device/account identifiers and authorisation
material private. MIT covers our original instructions/code, not the game/assets.

Assisted-by: Briar
