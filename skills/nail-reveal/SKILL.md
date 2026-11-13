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

This is the game-specific companion to the [general playtesting skill](references/general-playtesting.md).
Use that skill for controlled exploration, developer reports, disengagement
hypotheses, creative proposals and experiment planning. Keep Nail Reveal controls,
calibration and reproduction evidence here. Do not load the full study for a
simple test: choose the relevant reference below.

## Start here

1. Have the owner connect and authorise their intended phone. Select an explicit
   serial from `adb devices -l`; never use an implicit default or publish serials.
2. Inspect the current game and physical screenshot dimensions. Read the client
   brief, selected tool and stage card; do not infer state from a rotating hint.
3. Start a private screen recording before experiments and confirm it is running
   once. Preserve failures and disclose gaps. Sharing is a separate decision.
4. Read [tested controls](references/controls.md) for the current stage and
   [efficient execution](references/optimisation.md) before painting.
5. Apply the general observe/test/verify method, with [this game's ADB implementation](references/optimisation.md):
   finite batches in one control shell, separate binary-safe capture, relevant
   crops with original/mapping retained, and full-view checks for transitions or
   uncertainty. Optional speedups must have a working fallback. Stop dependent
   input on failed prerequisites; inspect partial effects before any replay.

The local setup and fallback references remain usable without installing the
general skill. They preserve the tested device procedure, not a claim that
generic coordinates or timing transfer to another game.

## Important findings

- The left icons change tools, not demonstrated brush sizes. On the tested
  five-icon layout: drill, nail file, Cone Bit offer, pink buffer, polish brush.
  First/second findings come from the earlier test; fourth/fifth were confirmed
  in the optimisation session. The Cone Bit later unlocked through normal
  Level2 progression and completed a preparation-stage tidy-base task; its
  effect on painted polish remains unknown. Decline understood offers; do not watch ads.
- Read [paint/contact and tool tests](references/paint-and-tools.md) before
  cleanup. The drill removed both polish and base coat, exposing pink nail;
  the file and buffer left the tested polish dots unchanged. The Cone Bit was
  locked until Salon Level 2 during the polish-removal test. Its later
  preparation-stage success is not a polish-erasing test. Do not call these five
  interchangeable erasers.
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

## Choose a Nail Reveal task

| Task | Read |
| --- | --- |
| First connection / portable fallback | [Linux/Windows setup](references/setup.md) and [ADB execution](references/optimisation.md) |
| Identify stage/tool effects | [Controls](references/controls.md) and [contact/cleanup experiments](references/paint-and-tools.md) |
| Single coat, bands, French tricolour | [Starter recipes](references/recipes.md) |
| UK, Japan or Brazil flags | [UK](references/uk-flag.md) or [Japan/Brazil](references/japan-brazil.md) |
| Crescent, flower or sunset | [Coat/cut/repaint design lab](references/design-lab.md) |
| Iterative art and quality assessment | [Generative study](references/generative-study.md) |

Read each recipe's limits: earlier flag/design-lab tests were not cured; UK
proportions and Brazil's colours/details are approximate. Later study glaze
captures do not retroactively cure those tests. The study's20 ideas and100
accepted-change records do not certify beauty; outcomes are uneven and the five
full-hand sets remain unfinished. A sketch or partial manicure is not execution
or a full hand. Windows/device-specific replay remains untested; no daemon is
required. Keep exact recipes and historical evidence in their linked references.

Keep original photos, recordings, device/account identifiers and authorisation
material private. MIT covers our original instructions/code, not the game/assets.

For feedback to the developer, distinguish these observed game results from
usability interpretations, disengagement hypotheses and untested feature ideas.
Use the general report/experiment templates; no player study or app code change
is authorised by a playtest request alone.

Assisted-by: Briar
