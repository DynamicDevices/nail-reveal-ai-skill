# Export review — 13 November 2026

Briar prepared this development candidate for Alex's review. This record is
self-review, not independent repository approval or a beauty certification.

## Gameplay media and privacy

The export includes 319 attempt/proposal folders and 304 silent clips. Video
frames were physically cropped to the gameplay area, resized to 482×994 at
12 fps, and stripped of audio and source metadata. Full-screen stills were
converted to gameplay crops; existing smaller nail/Hand previews were retained.
Original media remain private. Known private absolute workspace paths were
removed from exported text. Approval records and control logs were excluded.

Briar visually inspected all 26 contact sheets covering every clip at the
start, midpoint and near end: 912 sampled frames. These showed Nail Reveal
gameplay, palettes, synthetic clients, salon/stylebook and finishing screens,
including the known pre-ad offer. No unrelated apps, photographs, notifications
or account identifiers were observed in those samples. Final screenshots had
also been inspected during the study; that unchanged evidence was reused.

This was sampled review, not frame-by-frame inspection. Cropping and silence
reduce exposure but do not prove every frame contains no private information.
The source/export hashes and transformations are retained in `manifest.json`.

## Validation and static finding

Package validation checked all 3,888 manifest-indexed files for hashes and sizes,
304 single-video-stream clips, references, 100 accepted records and 29 indexed
rejections, and absence of private absolute paths in indexed text. Additional
delivery documents and archival helpers are outside that source-export index.
The repository content tests and focused exporter unit tests are separate checks.

The candidate skill's SkillSpector scan reported score 7/LOW with one raw MEDIUM
EA2 finding on “Do not replay a partially completed batch without checking the
screen.” This is a prohibition against unsafe replay, not permission to act
autonomously; triaged as a false positive. The finding is disclosed, not hidden
or represented as independent approval.

## What remains unproved

Independent exact-candidate repository review and applicable checks are still
required. The ledger counts do not establish that each accepted change was a
significant aesthetic improvement. Outcomes are uneven; the five full-hand sets
are unstarted. Windows portability, saved-gallery persistence and access to all
five editable nails are not proved. No ad or purchase was accepted. Historical
helper scripts are evidence, not a tested portable application or an input queue.

Assisted-by: Briar
