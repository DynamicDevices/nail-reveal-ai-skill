# Rejected preparation — visible old dark streaks

Alex explicitly pointed out insufficient cleaning and leftovers in this image.
The white base visibly retains dark streaks near the upper tip and lower region.
Do not paint the floral motif over this, accept this preparation, or count it as
an improvement cycle. Preserve the original failed base image and video.

The compiled serpentine has a confirmed path defect: after reaching y=2170 at
one column it jumps diagonally to y=1500 on the next (and similarly shortcuts
the top). It does not traverse to the new column at the same endpoint before
reversing. This omits direct full-height passes in alternating columns. Whether
that completely explains the visible streaks must be tested on the actual nail;
gloss/reflection or another cause must not be ruled out by assertion.

A new versioned coat-v2 primitive corrects those endpoint traversals; original
coat semantics and executed command files are retained for historical replay.
Inspect whole-nail opacity/edge coverage before any motif. Remaining unintended
marks mean preparation failed, regardless of successful ADB execution.

Assisted-by: Briar
