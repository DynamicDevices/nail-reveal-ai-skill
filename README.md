# nail-reveal-ai-skill
Portable Agent Skills guide for playing Nail Reveal over Android ADB: Linux and Windows setup, safe dialog handling, recording and flag exercises.

## Pull-request review integration

The `.github/preloop` helpers and three workflows start from the reviewed
gameplay bootstrap at `182e90548bfaa39df400d59954bcd94513583fcf`, with the same
status read-back and completed-lease lifecycle corrections proposed in gameplay
PR #4. Those corrections still need final exact-candidate review before merge.
Offline contract tests run without service credentials:

```sh
python3 -B -m unittest discover -s .github/preloop -p 'test_*.py'
```

Live reviews require this repository's own exact-source, hardware-signed
publication policy and existing repository-scoped credentials. The gameplay
repository's policy and credentials must not be reused here. Installation is
not activation or evidence of a successful live review. Keep the review
workflows disabled until the final policy and service bindings are validated.

Disabling either review workflow suspends publication. Cancel affected runs
before re-enabling; reconcile writes already in flight. The live pilot must
verify the actual review, check and status on the exact PR revision.

Running startup requires an unrevoked read lease (`lease_revoked: null`).
Completed publication requires confirmed cleanup (`lease_revoked: true`) plus
the controller's exact-commit checkout, setup and agent-start proof. Missing or
failed cleanup does not pass. Status publication independently checks both the
exact commit and GitHub's list-statuses actor record.

(Briar helped draft this)
