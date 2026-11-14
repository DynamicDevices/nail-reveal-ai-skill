#!/usr/bin/env python3
"""Check a completed local export's integrity, not privacy or aesthetic quality."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def validate(root):
    root = root.resolve()
    manifest = json.loads((root / 'manifest.json').read_text())
    assert manifest['schema'] == 'nail-study-local-review-package/v1'
    assert manifest['status'] in {
        'LOCAL REVIEW CANDIDATE — NOT PRIVACY/REVIEW APPROVED FOR PUBLICATION',
        'DEVELOPMENT PR CANDIDATE — INDEPENDENT REVIEW PENDING',
    }
    paths, videos = set(), 0
    for record in manifest['files']:
        name = record['path']
        target = (root / name).resolve()
        assert target.is_relative_to(root), f'Escaping path: {name}'
        assert name not in paths, f'Duplicate export: {name}'
        paths.add(name)
        assert target.is_file(), f'Missing export: {name}'
        assert target.stat().st_size == record['bytes'], f'Wrong size: {name}'
        assert digest(target) == record['sha256'], f'Hash mismatch: {name}'
        if target.suffix == '.mp4':
            probe = json.loads(subprocess.check_output([
                'ffprobe', '-v', 'error', '-show_entries',
                'format=duration:stream=codec_type,width,height', '-of', 'json', str(target)], text=True))
            assert len(probe['streams']) == 1
            stream = probe['streams'][0]
            assert stream == dict(codec_type='video', width=482, height=994)
            assert float(probe['format']['duration']) > 0
            assert record['transform']['audio'] is False
            videos += 1
        elif target.suffix in {'.md', '.json', '.jsonl', '.txt'}:
            text = target.read_text()
            assert '/home/' not in text, f'Private absolute path: {name}'
            assert '/data_drive/' not in text, f'Private absolute path: {name}'
    study = json.loads((root / 'study.json').read_text())
    accepted, rejected = set(), set()
    for idea in study['ideas']:
        assert len(idea['accepted_cycles']) == 5
        for key in ['baseline', 'initial_baseline', 'best', 'clean_base']:
            if idea.get(key):
                assert (root / idea[key]).is_dir(), f'Missing {key}: {idea["id"]}'
        for ref in idea['accepted_cycles']:
            assert ref not in accepted
            accepted.add(ref)
            folder = root / ref
            assert (folder / 'stages.json').is_file()
            assert (folder / 'creation.mp4').is_file()
            assessment = (folder / 'ASSESSMENT.md').read_text().splitlines()[0]
            assert 'accepted' in assessment.lower()
        for ref in idea.get('rejected_attempts', []):
            rejected.add(ref)
            folder = root / ref
            assert (folder / 'creation.mp4').is_file()
            assert 'rejected' in (folder / 'ASSESSMENT.md').read_text().splitlines()[0].lower()
        for ref in idea.get('restorations', []) + idea.get('finishing_attempts', []):
            assert (root / ref / 'creation.mp4').is_file()
        for ref in idea['glaze'].values():
            if isinstance(ref, str) and ref.startswith('attempts/'):
                assert (root / ref / 'creation.mp4').is_file()
        for ref in idea.get('effective_final_images', {}).values():
            assert (root / ref).is_file()
    assert len(study['ideas']) == 20 and len(accepted) == 100
    assert not accepted.intersection(rejected)
    assert videos == sum(a['recorded'] for a in manifest['attempts'])
    print(json.dumps(dict(result='PASS', exported_files=len(paths), videos=videos,
                          accepted_records=len(accepted), rejected_records=len(rejected),
                          limitation='Integrity only: not privacy, beauty, full-hand completion or publication approval')))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('package', type=Path)
    validate(parser.parse_args().package)
