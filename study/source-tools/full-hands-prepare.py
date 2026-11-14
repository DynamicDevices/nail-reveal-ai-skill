"""Prepare fresh, finite full-hand attempts without changing original evidence."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from study_driver import checked_id, compile_steps

identity = checked_id(sys.argv[1])
stages = json.loads(sys.argv[2])
for label, steps in stages.items():
    checked_id(label)
    compile_steps(steps)
folder = ROOT / 'attempts' / identity
folder.mkdir(exist_ok=False)
(folder / 'stages.json').write_text(json.dumps(stages, indent=2) + '\n')
print(identity)
