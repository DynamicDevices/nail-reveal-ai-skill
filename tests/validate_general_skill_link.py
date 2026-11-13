"""Offline checks for the general-skill companion; no device/network access."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REVISION = "93905be40c2611d903c508cdfd266bd091f1418f"


class GeneralSkillLinkTests(unittest.TestCase):
    def test_general_dependency_is_pinned_and_honest(self):
        text = (ROOT / "skills/nail-reveal/references/general-playtesting.md").read_text(encoding="utf-8")
        self.assertIn("game-playtesting-skill/tree/" + REVISION, text)
        self.assertIn("not a claim that its PR is merged", text)
        self.assertIn("has not yet been tested live in Claude", text)

    def test_standalone_safety_and_game_findings_remain(self):
        text = (ROOT / "skills/nail-reveal/SKILL.md").read_text(encoding="utf-8")
        for phrase in ["explicit", "fallback", "pointer UP", "purchases", "Cone Bit",
                       "both polish and base coat", "full-hand", "general-playtesting.md", "partially completed"]:
            self.assertTrue(phrase in text, "Missing preserved finding/boundary: " + phrase)
        for name in ["recipes.md", "uk-flag.md", "japan-brazil.md", "design-lab.md",
                     "paint-and-tools.md", "generative-study.md", "optimisation.md", "setup.md"]:
            self.assertTrue((ROOT / "skills/nail-reveal/references" / name).is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
