# General method, specific game

The reusable method now lives in
[DynamicDevices/game-playtesting-skill](https://github.com/DynamicDevices/game-playtesting-skill/tree/93905be40c2611d903c508cdfd266bd091f1418f).
This immutable revision is the integration dependency for this companion update;
it is a development candidate, not a claim that its PR is merged. No remote code
needs to execute merely to read or use these game-specific instructions.

Install its complete `skills/app-playtesting` folder using its
[Claude guide](https://github.com/DynamicDevices/game-playtesting-skill/blob/93905be40c2611d903c508cdfd266bd091f1418f/docs/claude.md),
and keep the complete `skills/nail-reveal` folder alongside it for this game.
Verify the agent's actual input/image capabilities; installing instructions does
not grant device access. If the generic skill is unavailable, this skill's local
setup, controls, fallback and recipes remain usable. Do not infer new permissions.

## What belongs where

- General skill: controlled exploration, conditional state-based actions,
  expected/actual evidence, restoration, adapter fallbacks and developer reports.
- Nail Reveal companion: actual stage/tool effects, calibration, tested ADB
  details, palette positions, drawing recipes and the recorded study.
- App developer: optional debug hooks, code changes and separately authorised
  real-player research. Neither skill implements those changes or proves engagement.

For a tool experiment, use the general method and record the current Nail Reveal
stage, client, tool, build, screen and baseline. Consult
[tool observations](paint-and-tools.md), not assumptions about icon appearance.
For art, use [recipes](recipes.md) and the [design lab](design-lab.md); for study
limits, use [the generative-study reference](generative-study.md).

For Jon's developer feedback, use the general package's
[report template](https://github.com/DynamicDevices/game-playtesting-skill/blob/93905be40c2611d903c508cdfd266bd091f1418f/skills/app-playtesting/assets/developer-report.md)
and [experiment guide](https://github.com/DynamicDevices/game-playtesting-skill/blob/93905be40c2611d903c508cdfd266bd091f1418f/skills/app-playtesting/references/experiments.md).
Keep bugs, usability observations, possible disengagement and creative features
separate. Do not infer player boredom or retention from an agent's playthrough,
or turn app scores/100 recorded changes into proof of beauty or improvement.

The general package has offline tests but has not yet been tested live in Claude,
a second game or a conventional app. This refactor preserves the historical
recipes and media; it does not establish a successful replay or new device support.

Assisted-by: Briar
