"""Offline content checks. Run: python -B tests/validate_content.py"""

import csv
import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "nail-reveal" / "SKILL.md"


class ContentTests(unittest.TestCase):
    def test_media_manifest(self):
        manifest = json.loads((ROOT / "media" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["videos"]), 9)
        for item in manifest["videos"]:
            path = ROOT / item["path"]
            digest = hashlib.sha256()
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            self.assertEqual(digest.hexdigest(), item["sha256"], path)
            self.assertEqual(path.stat().st_size, item["bytes"], path)
            self.assertEqual(len(item["streams"]), 1)
            self.assertEqual(item["streams"][0]["codec_type"], "video")
            self.assertEqual(item["streams"][0]["width"], 400)
            self.assertEqual(item["streams"][0]["height"], 850)

    def test_skill_entrypoint(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: nail-reveal$")
        self.assertRegex(frontmatter, r"(?m)^description: .+")
        self.assertIn("license: MIT", frontmatter)
        self.assertIn("fallback", text.lower())

    def test_relative_markdown_targets(self):
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            text = document.read_text(encoding="utf-8")
            for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                relative = target.split("#", 1)[0]
                resolved = (document.parent / relative).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (document, target))
                self.assertTrue(resolved.exists(), (document, target))

    def test_contact_data(self):
        with (ROOT / "tests" / "contact-results.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 15)
        cases = {row["case"]: row for row in rows}
        self.assertEqual(cases["stationary_short"]["blue_pixels"], "0")
        self.assertEqual(cases["brush_cleanup_after"]["blue_pixels"], "14576")
        for row in rows:
            self.assertNotIn(None, row)
            self.assertGreaterEqual(int(row["blue_pixels"]), 0)

    def test_media_headers_and_host_limit(self):
        videos = list((ROOT / "media" / "videos").glob("*.mp4"))
        self.assertEqual(len(videos), 9)
        for path in videos:
            with path.open("rb") as handle:
                header = handle.read(12)
            self.assertEqual(header[4:8], b"ftyp", path)
            self.assertLess(path.stat().st_size, 100 * 1024 * 1024, path)
        images = list((ROOT / "media" / "images").rglob("*.png"))
        self.assertTrue(images)
        for path in images:
            with path.open("rb") as handle:
                self.assertEqual(handle.read(8), b"\x89PNG\r\n\x1a\n", path)

    def test_rights_and_limitations(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("MIT", text)
        self.assertIn("remain the property", text)
        self.assertIn("Windows setup is documented but has not been tested live", text)
        self.assertIn("Assisted-by: Briar", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
