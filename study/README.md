# Nail Reveal: twenty ideas, recorded iteration, unfinished delivery

Alex asked Briar to explore twenty genuinely different ideas with five visibly
significant improvements per idea, record the work, reject regressions, glaze
after five improvements and reproduce the five strongest designs on full hands.
Beauty is the primary requirement. The ledger is evidence of assessed changes,
not proof that this requirement has been met.

This is a DEVELOPMENT PR CANDIDATE — INDEPENDENT REVIEW PENDING, not a completed
repository release. Export validation and sampled gameplay media review are
complete; [scope and limits](REVIEW.md) are recorded. Originals remain private.
Candidate publication does not waive independent review or authorise merging.

## Start with the results, then inspect the working

- [Twenty glazed designs](guide/study-twenty-glazed-designs.png)
- [Top-five selection](guide/study-top-five-review.md)
- [Final aesthetic audit](guide/study-final-aesthetic-audit.md)
- [Full-hand progress and ad gate](guide/fullhand-progress.md)
- [Observed learnings](LEARNINGS.md)
- [CWCW source notes](CWCW-NOTES.md)

The selected five are D03 sea-glass, D05 geometric inlay, D20 planet, D08 cherries
and D06 terrazzo. None has yet been reproduced on a complete five-nail hand.
The old job permitted two editable nails; the next permitted three. Further
gameplay stopped at a pre-ad prompt. No ad or purchase was accepted.

Some final motifs are stronger than others. The bow reads clearly; the butterfly
is abstract and the koi is weakly recognisable. Many counted changes constructed
unfinished motifs. Do not describe this as100 independently optimised finished
designs, a full genetic-algorithm study, or twenty brilliant completed designs.

## What the files mean

`study.json` contains the accepted/rejected ledger and explicit restoration,
finishing and glaze references. `attempts/ID/ASSESSMENT.md` is the contemporaneous
visual judgement. Historical progress counts in per-idea guides describe their
time of writing, not the current project state. No missing assessment or video
is silently invented: `manifest.json` reports which attempt folders contain them.
An unrecorded/sketch-only proposal is not a physical attempt or accepted cycle.

Each recorded attempt contains `creation.mp4`, a derived silent clip. The original
`execution.json` reports original recording duration/size and execution outcome;
those are not the derived clip's size. The manifest records both source hashes
and exported hashes, plus exported video probes and crop mappings. Filenames
ending `-gameplay.png` are derived gameplay crops, not full physical screenshots.
Other images may be the original already-derived nail/Hand detail previews;
their mappings are described in the assessment and original execution record.

## Recreate an idea

1. Read its `guide/study-dXX-recreate.md` and all cited assessments. Inspect the
   final and rejected images. Resolve intended layer order and parent restoration
   before touching a phone. The guides' historical `work/generative-study/`
   paths refer to this package's root; `outputs/` media are in `guide/` here.
2. Have the owner authorise the exact phone and activity. This package grants
   no access, ad/purchase permission, publication permission or security changes.
   Use explicit serial selection on every ADB invocation. Never publish serials.
3. Establish app version, physical display dimensions, client brief, editable
   nails, tool, stage and current paint from a fresh full screenshot. These recipes
   were calibrated on Nail Reveal1.25, Android15,1080×2400, mostly one tall nail.
   A different silhouette requires remapping and actual Hand inspection.
4. Start screen recording using a unique destination and confirm its PID once
   before input. Use the device-supported finite recording limit or a known
   supported unlimited mode. Stop painting before recording ends. Retain failed
   clips and gaps; do not claim an interrupted recording was continuous.
5. Use the cited `attempts/ID/stages.json` for exact validated action order,
   coordinates and dwells. The associated `STAGE.android-shell.txt`, where
   present, is the exact finite Android shell batch used. Inspect it first; do
   not execute recipe text from an untrusted source or an unknown game state.
   Recreate one inspected stage at a time, then capture/inspect its result.
6. The portable baseline is explicit-serial ADB taps/swipes and binary-safe
   original PNG capture. Continuous DOWN/MOVE/UP and persistent shells are
   optional. If unsupported, inspect partial effects and use tested held swipes;
   never replay an uncertain completed stage or leave contact DOWN while thinking.
   No Node daemon, paid generator or privileged injector is required.
7. Colour stages use palette open230,2200; swatch selection; close540,1740,
   with0.7-second settling between actions. The fifth left tool paints. A broad
   background-colour mask trims a mark; the drill strips all coats. Colour
   masking can leave halos and cannot reconstruct arbitrary underlying textures.
8. Inspect the complete nail for residue, rims, clipping and unwanted joins.
   Check actual Hand projection before accepting any silhouette extension or
   painting a dependent layer. Neither a sketch nor a clean closeup proves fit.
9. Reject non-improvements, retain their evidence and physically restore the
   previous best before another attempt. After five accepted changes, use the
   recorded Lamp transition and capture the glazed nail. Finish sparkles belong
   to the game; do not describe them as hand-drawn details. Done ends a client;
   it changes available editing/navigation and may lead to an ad gate.

Exact JSON is the authority for reproduction data, not an automatic input queue.
The old task-local runner mentioned in some historical guides is not bundled as
a portable supported application. All original records remain preserved privately.
Fresh execution must have new attempt IDs, recordings and assessments; never
overwrite this historical evidence or infer a successful replay without seeing it.

## Generative method and limits

The starting ideas use constrained parameterised geometry: bold curves, nested
shapes, region fills, layer ordering and background masks. Revisions vary scale,
position, spacing, overlap, density and contrast. Selection was Briar's visual
judgement against the retained parent, not a learned aesthetic metric or a full
population-based genetic algorithm. Sketches caught some geometry mistakes but
did not model opacity, shading or nail projection.

Sources read during the study:

- Daniel Shiffman, [genetic algorithms](https://natureofcode.com/genetic-algorithms/):
  mutation, selection and interactive fitness. Adapted conceptually, not copied.
- Tyler Hobbs, [Flow Fields](https://www.tylerxhobbs.com/words/flow-fields):
  controlled curves. Dense fine streamlines were not a good fit for this brush.

The original research/process record is in `PLAN.md`. Its earlier unknowns and
execution instructions are historical; the newer audit/learnings describe the
observed state. Windows and other devices remain untested, not guaranteed by
having a fallback policy. Glaze transitions were observed; saved-gallery
persistence and all-five-nail access are not proved.

## Rights

These are independent gameplay experiments. Our original instructions and code
can be distributed under the repository's MIT licence; Nail Reveal, its interface
and game assets remain their owners' property. No game assets are relicensed.
Publication requires owner approval, privacy review and repository review. Alex
retains merges and any decision about sharing this as an artwork.

Assisted-by: Briar
