"""Focused non-device checks for local study export helpers."""
import tempfile
import unittest
from pathlib import Path
from package_study import ROOT, WORKSPACE, build, sanitise, sha


class PackageTests(unittest.TestCase):
    def test_absolute_source_paths_and_image_names_are_mapped(self):
        source = str(ROOT / 'attempts/d20-c04-a01/hand-full.png')
        self.assertEqual(sanitise(source), 'attempts/d20-c04-a01/hand-gameplay.png')
        self.assertEqual(sanitise(str(WORKSPACE / 'outputs/test.png')), 'outputs/test.png')

    def test_unrelated_text_is_not_rewritten(self):
        self.assertEqual(sanitise('Full-hand set: not completed.'), 'Full-hand set: not completed.')

    def test_never_overwrites_an_existing_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileExistsError):
                build(Path(directory))

    def test_hash_reads_file_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample'
            path.write_bytes(b'abc')
            self.assertEqual(sha(path), 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')


if __name__ == '__main__':
    unittest.main()
