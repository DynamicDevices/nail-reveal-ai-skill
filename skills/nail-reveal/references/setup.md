# Linux and Windows: first connection

The human must own the phone or have permission to control it. ADB provides
powerful device access: approve only a trusted computer, and revoke its USB
debugging authorisation afterwards if the connection is temporary.
The AI needs a shell/process tool and image inspection. If either is missing,
ask the human to run the commands or inspect the screenshots; do not pretend
to have direct access. No agent-specific SDK is required.

## Install ADB

Use Google's [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools)
or a trusted distribution package. Do not download random ADB bundles.

### Linux

Have the human install the `adb` package with their normal package manager
(on Debian/Ubuntu, the package is named `adb`), or unpack Google's Linux
Platform Tools and use the absolute path to `platform-tools/adb`.
Keep any administrator password in the human's trusted terminal, not the chat.
Run `adb version` to confirm the executable works.

If the device reports “no permissions”, use the distribution's Android/udev
setup instructions. Do not run ADB as root or broadly loosen USB permissions.
Disconnect/reconnect only when needed after an authorised setup change.

### Windows

Download and extract Google's Windows Platform Tools ZIP. In PowerShell, point
to the extracted executable; this avoids needing a permanent PATH change:

```powershell
$NailAdb = 'C:\Tools\platform-tools\adb.exe'
& $NailAdb version
& $NailAdb devices -l
```

Replace the path with the actual extraction directory. If Windows needs a USB
driver, use the phone manufacturer's official driver guidance; do not install
an unknown driver or disable signature/security protections. The live tests
for this repository were on Linux; Windows instructions remain unverified.

## Enable phone access: the human's steps

1. Install Nail Reveal from the official Play Store listing if it is not already
   installed. The package is `com.onteca.nailreveal`.
2. In Android Settings, find Build number under About phone and tap it seven
   times to enable Developer options. Locations vary by manufacturer.
3. Enable USB debugging in Developer options. Connect an unlocked phone with
   a data-capable USB cable. Charge-only cables will not work; try File transfer
   mode if the manufacturer requires it.
4. Check the debugging authorisation prompt on the phone. Approve only the
   expected trusted computer/fingerprint. Do not ask an AI to bypass this prompt.
5. Run `adb devices -l`. Select the intended phone explicitly. If several are
   present, have the human identify the correct one; never silently pick one.

`unauthorized` means the human has not approved the host. `offline` is a
transport problem. An empty list can mean cable, port, driver or permission
trouble. Resolve the observed cause; do not repeatedly click or restart blindly.
No Wi-Fi pairing, root, data clearing, app reinstall or security change is
required by these painting recipes.

## Confirm the selected device

Replace `SERIAL` with the selected private identifier. Do not commit that value.

```sh
adb -s SERIAL get-state
adb -s SERIAL shell getprop ro.product.model
adb -s SERIAL shell wm size
adb -s SERIAL shell pm path com.onteca.nailreveal
```

In PowerShell use `& $NailAdb` in place of `adb`. Have the human open the game,
then inspect the current screenshot. Installation and transport success do not
prove that the game is ready or on the expected nail/stage.

## Binary-safe capture on either platform

Use a unique filename each time. The device-file/pull route works without host
binary redirection or an image package:

```sh
adb -s SERIAL shell screencap -p /sdcard/Download/nail-capture-001.png
adb -s SERIAL pull /sdcard/Download/nail-capture-001.png nail-capture-001.png
```

On Linux a separate binary-safe `adb -s SERIAL exec-out screencap -p > capture.png`
is faster when supported. Do not assume older PowerShell redirection preserves
PNG bytes. Crop/resize only as an optional preview; keep the original dimensions
and the crop offset/scale when mapping touch coordinates.

## First actions and recording

Confirm the tool and stage before input. These baseline Android commands need
no daemon:

```sh
adb -s SERIAL shell input tap X Y
adb -s SERIAL shell input swipe X1 Y1 X2 Y2 DURATION_MS
```

Read [controls](controls.md) and [contact tests](paint-and-tools.md) before using
held DOWN/MOVE/UP sequences. Their footprint, upward offset and delayed paint
response can otherwise damage a design.

Before experiments, check the device's `screenrecord --help`. Use a supported
finite time limit and unique output path; zero/unlimited is device-specific.
Start recording as a managed process, confirm it once before touches, and stop
with SIGINT to its identified recorder before pulling the MP4. Check the final
video actually opens. Restart recording before touching after an interruption;
disclose gaps. Recording is silent here; never promise microphone capture.

No converter installed? Inspect the original PNG. No persistent shell support?
Use individual/finitely batched ADB calls. See the [fallback ladder](optimisation.md#fallback-ladder).
