"""Offline checks for the general-skill companion; no device/network access."""

from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = json.loads((ROOT / "skills/nail-reveal/dependencies.json").read_text())["dependencies"][0]
REVISION = DEPENDENCY["revision"]


class GeneralSkillLinkTests(unittest.TestCase):
    def test_general_dependency_is_pinned_and_honest(self):
        text = (ROOT / "skills/nail-reveal/references/general-playtesting.md").read_text(encoding="utf-8")
        self.assertIn("game-playtesting-skill/tree/" + REVISION, text)
        self.assertIn("not a claim that its PR is merged", text)
        self.assertIn("has not yet been tested live in Claude", text)

    def test_required_dependency_and_game_findings_remain(self):
        text = (ROOT / "skills/nail-reveal/SKILL.md").read_text(encoding="utf-8")
        for phrase in ["explicit", "fallback", "purchases", "Cone Bit", "If it is missing, stop",
                       "both polish and base coat", "full-hand", "general-playtesting.md", "dependencies.json"]:
            self.assertTrue(phrase in text, "Missing preserved finding/boundary: " + phrase)
        for name in ["recipes.md", "uk-flag.md", "japan-brazil.md", "design-lab.md",
                     "paint-and-tools.md", "generative-study.md", "optimisation.md", "setup.md"]:
            self.assertTrue((ROOT / "skills/nail-reveal/references" / name).is_file())

    def test_dependency_manifest_is_required_and_all_links_match(self):
        self.assertEqual(DEPENDENCY["name"], "app-playtesting")
        self.assertIs(DEPENDENCY["required"], True)
        self.assertEqual(DEPENDENCY["path"], "skills/app-playtesting")
        self.assertRegex(REVISION, r"^[0-9a-f]{40}$")
        for path in [ROOT / "README.md", *(ROOT / "skills/nail-reveal/references").glob("*.md")]:
            for revision in re.findall(r"game-playtesting-skill/(?:blob|tree)/([0-9a-f]{40})", path.read_text()):
                self.assertEqual(revision, REVISION, str(path))

    def test_generic_procedures_are_not_copied_into_nail_references(self):
        for name in ["setup.md", "optimisation.md"]:
            text = (ROOT / "skills/nail-reveal/references" / name).read_text()
            self.assertIn("game-playtesting-skill/blob/" + REVISION, text)
            self.assertNotIn("adb devices -l", text)
            self.assertNotIn("NAIL_BATCH_001_DONE", text)
            self.assertNotIn("| Optional speedup |", text)
            self.assertNotIn("x=x0+u*w/W", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
