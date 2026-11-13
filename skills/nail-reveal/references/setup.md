# Nail Reveal setup — game-specific companion

This skill requires the pinned `app-playtesting` dependency listed in
`../dependencies.json`. Read [dependency installation](general-playtesting.md)
first. If it is missing, stop before input; this file is not a standalone copy
of the general procedure.

For Android authorisation, Platform Tools, Linux/Windows setup, device selection
and binary-safe screenshots, follow the general skill's
[canonical Android setup](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/android-setup.md)
and [execution/capture](https://github.com/DynamicDevices/game-playtesting-skill/blob/866fa0fa1e334ca82dfd4f867934704bbd62b3c2/skills/app-playtesting/references/android-execution.md).
Do not maintain a second ADB setup/fallback procedure here.

## Nail Reveal configuration

- Install/open the owner-authorised official Nail Reveal app. Its Android
  package is `com.onteca.nailreveal`.
- Recorded evidence used app 1.25, Android 15, a 1080×2400 phone and Linux.
  Windows and other-device replay remain untested.
- Establish the current client, editable nail, tool and preparation/painting
  stage. Transport/installation success does not establish those states.
- Use [controls](controls.md), [tool/contact results](paint-and-tools.md) and
  [calibration](optimisation.md) before choosing a recipe. Contact footprint and
  upward tool offset can damage an existing design.
- Experiments were recorded silently. No ad, purchase or unexpected account/
  consent choice is authorised by the recipes.

Historical detailed setup remains in Git history; it is not the live canonical
procedure. Assisted-by: Briar.
