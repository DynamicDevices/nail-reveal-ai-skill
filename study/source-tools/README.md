# Historical study tools

These are the Python source files used to prepare, record, assess, compare and
package the study. They are preserved for inspection and reproducibility, not
installed or automatically executed. Some scripts assume the original private
working layout and the calibrated A063 phone. Preparation scripts may rewrite
proposal files: do not run them over historical evidence.

The portable skill remains ordinary explicit-serial ADB plus screenshot
inspection and recording. Read ../README.md and the per-idea recreation guide;
use each attempt's stages.json and recorded Android shell batch for exact input
data. Check authority, state, dimensions, geometry, recording and partial effects
before replay. Replays need fresh attempt IDs and a separate scratch directory.

The task-local runner is not a multi-device portable application. Its unique
phone/model checks are historical laboratory assumptions, not permission to
operate whichever device happens to be connected. Do not use it without first
selecting and verifying the owner's exact intended device; adapt explicit serial
handling before using it on a multi-device host.

package_study.py and privacy_contacts.py generate local review artifacts using
existing Pillow/ffmpeg. They do not publish or supply privacy approval. The
manifest's exported hashes identify the media in this repository; source hashes
identify private originals, not an invitation to publish them.

Safe offline checks for this package:

```sh
python3 -B -m unittest discover -s study/source-tools -p test_package_study.py
python3 -B study/source-tools/validate_package.py study
python3 -B tests/validate_content.py
```

Do not run an unrestricted test discovery across the historical source files:
some files named test_*.py are physical experiments, not isolated unit tests.

Assisted-by: Briar
