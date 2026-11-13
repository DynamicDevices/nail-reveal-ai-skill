# General method, specific game

The reusable method now lives in
[DynamicDevices/game-playtesting-skill](https://github.com/DynamicDevices/game-playtesting-skill/tree/866fa0fa1e334ca82dfd4f867934704bbd62b3c2).
This immutable revision is the integration dependency for this companion update;
it is a development candidate, not a claim that its PR is merged. No remote code
needs to execute merely to read or use these game-specific instructions.

This is a required dependency, not an optional companion. `../dependencies.json`
is the authoritative repository/revision/path record. The manifest is this
repository's explicit convention, not a claim that Agent Skills or Claude
automatically resolves or installs dependencies. Use the full pinned folder.
Install its complete `skills/app-playtesting` folder using its
[Claude guide](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/docs/claude.md),
and keep the complete `skills/nail-reveal` folder alongside it for this game.
Verify the selected revision and the agent's actual input/image capabilities;
installing instructions does not grant device access. If the dependency is
unavailable, stop before input and explain the missing installation. Old local
setup/execution files are historical evidence, not an alternate current procedure.

## What belongs where

- General skill: controlled exploration, conditional state-based actions,
  expected/actual evidence, restoration, adapter fallbacks and developer reports.
- Nail Reveal companion: actual stage/tool effects, calibration, palette
  positions, drawing recipes and the recorded study. Setup/execution references
  here are compatibility pointers plus app-specific observations, not copies.
- App developer: optional debug hooks, code changes and separately authorised
  real-player research. Neither skill implements those changes or proves engagement.

For a tool experiment, use the general method and record the current Nail Reveal
stage, client, tool, build, screen and baseline. Consult
[tool observations](paint-and-tools.md), not assumptions about icon appearance.
For art, use [recipes](recipes.md) and the [design lab](design-lab.md); for study
limits, use [the generative-study reference](generative-study.md).

For Jon's developer feedback, use the general package's
[report template](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/assets/developer-report.md)
and [experiment guide](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/experiments.md).
Keep bugs, usability observations, possible disengagement and creative features
separate. Do not infer player boredom or retention from an agent's playthrough,
or turn app scores/100 recorded changes into proof of beauty or improvement.

The general package has offline tests but has not yet been tested live in Claude,
a second game or a conventional app. This refactor preserves the historical
recipes and media; it does not establish a successful replay or new device support.

Assisted-by: Briar
