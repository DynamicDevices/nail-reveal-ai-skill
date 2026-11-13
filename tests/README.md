# Recorded tests

Tests progressed from single colour and stripes to tool/contact experiments and
three non-flag designs. The images show actual gameplay, not ideal SVG references.
The [media index](../media/README.md) links recordings and intermediate captures.

| Test | Observed result | Recreate / limitations |
| --- | --- | --- |
| Single coat | Recognisable colour; game completion preceded full edge coverage | [Original recipe](../skills/nail-reveal/references/recipes.md); inspect the lower rim |
| French tricolour | Blue/white/red bands | Same recipe; soft boundaries, incomplete lower rim |
| Faster blue base | Continuous contact covered more of the prior design | [Optimisation](../skills/nail-reveal/references/optimisation.md); different workloads, no total speedup ratio |
| UK flag | Recognisable red/white/blue design | [Recipe](../skills/nail-reveal/references/uk-flag.md); symmetric diagonals, not exact flag proportions |
| Japan | White recoat and red disc | [Recipe](../skills/nail-reveal/references/japan-brazil.md); the first white coat left ghosts |
| Brazil | Muted green, yellow diamond, blue centre/white band | Same recipe; pastel palette, rounded corners, no stars/lettering |
| Contact timing | Held contact painted without motion; short requested holds left no dot | [Tool tests](../skills/nail-reveal/references/paint-and-tools.md) and [measurements](contact-results.csv); actual contact time includes command overhead |
| File and buffer | No change to the matched fresh-polish dot | Tool tests; not evidence they do nothing in preparation stages |
| Drill | Removed polish and base coat, exposing pink nail | Tool tests; not a selective colour eraser |
| Cone Bit | Locked until Salon Level 2 | Function untested; no ad accepted |
| Brush cleanup | Background-white overpainting trimmed a blue mark | Tool tests; cannot restore an unknown texture or hidden layer |
| Crescent | Stripped round window, offset black repaint, white dots | [Design lab](../skills/nail-reveal/references/design-lab.md) |
| Flower | Held-contact petals/centre and continuous stem/leaves | Design lab; bold rounded shapes, not fine linework |
| Sunset | Stripped window/yellow infill and dark peaks | Design lab; soft halo and rounded silhouette |

## Failures retained

- Fast long swipes and sparse coats left gaps or ghosts; longer overlap/dwell
  and a dense recoat improved coverage.
- An early point-measurement crop included neighbouring marks. The published
  measurements use isolated crops; a cleanup crop also excluded an existing
  drill hole and idle tool graphic before counting pink pixels.
- Tools did not provide five verified brush widths. Their actual effects
  needed isolated tests; a visible tool overlap was captured for no-effect cases.
- The persistent shell/recorder was lost across an interruption. We checked the
  phone and missing completion artifact before retrying through fresh ADB calls.
- One earlier session missed four cleanup strokes between recordings. The two
  recordings are not one uninterrupted capture; the gap remains disclosed.
- An animated-scene accessibility dump could fail and leave stale XML. Fresh
  screenshots were the fallback.

Most designs were sequential experiments on one nail, not saved manicures.
No curing/top-coat/finished-game persistence acceptance was performed for these
later designs. Linux was tested; Windows and other-device compatibility remain
untested. No independent integration review is claimed by this test record.

Assisted-by: Briar.
# General-skill companion checks

Run `python3 -B tests/validate_general_skill_link.py` alongside the existing
content tests. It checks the pinned general-skill dependency, honest live-test
limits and retention of the local safety/tool findings. It does not drive a phone
or prove cross-app/Claude compatibility. The study, media and recreation recipes
are unchanged by this companion refactor.

The changed Nail Reveal skill passed static scanning (score 7/LOW, one finding).
The unchanged prohibition “Do not replay a partially completed batch without
checking the screen” was already triaged in the study review as a false-positive
autonomy finding. This scan is not independent repository approval. The new
general skill's scan had score 0/no findings; its offline checks live in its own
repository. Neither result certifies app behaviour or player engagement.

