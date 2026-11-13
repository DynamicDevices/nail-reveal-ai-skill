#!/usr/bin/env python3
"""Build a local review package; does not publish or authorise publication.

Retain original evidence privately. Export only named study records and derived,
silent gameplay media. Source hashes bind every exported file to its original.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[1]
GAMEPLAY = (56, 340, 964, 1990)
VIDEO_SIZE = (482, 994)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def sanitise(value):
    """Remove known private source roots, not arbitrary substrings/secrets."""
    value = value.replace(str(ROOT) + '/', '')
    value = value.replace(str(WORKSPACE) + '/', '')
    return re.sub(r'([a-z0-9-]+)-full\.png', r'\1-gameplay.png', value)


def build(destination, resume=False):
    from PIL import Image
    if destination.exists() and not resume:
        raise FileExistsError('Choose a fresh package path; never overwrite evidence')
    destination.mkdir(parents=True, exist_ok=resume)
    records, attempts = [], []
    started = time.monotonic()

    def record(source, target, transform=None):
        records.append(dict(
            source=str(source.relative_to(WORKSPACE)),
            source_sha256=sha(source), source_bytes=source.stat().st_size,
            path=str(target.relative_to(destination)),
            sha256=sha(target), bytes=target.stat().st_size,
            transform=transform))

    def text_copy(source, target):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(sanitise(source.read_text()))
        record(source, target, 'known source-root removal and full→gameplay reference mapping')

    # Explicit allowlist: no approval records, control logs, credentials, unrelated
    # photos, general workspace inventories or private runtime configuration.
    for name in ['study.json', 'LEARNINGS.md', 'PLAN.md']:
        text_copy(ROOT / name, destination / name)
    for source in sorted((WORKSPACE / 'outputs').glob('study-*.md')):
        text_copy(source, destination / 'guide' / source.name)
    for name in ['fullhand-progress.md']:
        text_copy(WORKSPACE / 'outputs' / name, destination / 'guide' / name)
    text_copy(WORKSPACE / 'work/cwcw/INSIGHT-NOTES.md', destination / 'CWCW-NOTES.md')

    # Guide image links remain valid. These are copies of already derived local
    # images, except full phone images, which get the same gameplay crop below.
    guide = destination / 'guide'
    for source in sorted((WORKSPACE / 'outputs').glob('study-*.png')):
        target = guide / source.name
        with Image.open(source) as picture:
            if picture.size == (1080, 2400):
                x, y, width, height = GAMEPLAY
                picture.crop((x, y, x+width, y+height)).resize((482, 995)).save(target)
                transform = dict(crop=list(GAMEPLAY), output_size=[482, 995])
            else:
                shutil.copyfile(source, target)
                transform = 'existing derived image, unchanged'
        record(source, target, transform)
    source = WORKSPACE / 'outputs/fullhand-ad-gate.png'
    target = guide / source.name
    with Image.open(source) as picture:
        x, y, width, height = GAMEPLAY
        picture.crop((x, y, x+width, y+height)).resize((482, 995)).save(target)
    record(source, target, dict(crop=list(GAMEPLAY), output_size=[482, 995]))

    for folder in sorted((ROOT / 'attempts').iterdir()):
        if not folder.is_dir():
            continue
        target_folder = destination / 'attempts' / folder.name
        target_folder.mkdir(parents=True, exist_ok=resume)
        execution = folder / 'execution.json'
        attempts.append(dict(id=folder.name, recorded=(folder/'creation.mp4').is_file(),
                             execution_record_present=execution.is_file(),
                             assessment_present=(folder/'ASSESSMENT.md').is_file(),
                             stages_present=(folder/'stages.json').is_file()))
        for source in sorted(folder.iterdir()):
            if not source.is_file():
                continue
            if source.name in {'recipe.json', 'stages.json', 'ASSESSMENT.md',
                               'execution.json', 'finite-batches.jsonl', 'batches.jsonl'} or source.name.endswith('.android-shell.txt'):
                text_copy(source, target_folder / source.name)
            elif source.suffix.lower() == '.png':
                target = target_folder / source.name.replace('-full.png', '-gameplay.png')
                with Image.open(source) as picture:
                    if picture.size == (1080, 2400):
                        x, y, width, height = GAMEPLAY
                        picture.crop((x, y, x+width, y+height)).resize((482, 995)).save(target)
                        transform = dict(crop=list(GAMEPLAY), output_size=[482, 995])
                    else:
                        shutil.copyfile(source, target)
                        transform = 'existing derived image, unchanged'
                record(source, target, transform)
            elif source.name == 'creation.mp4':
                target = target_folder / 'creation.mp4'
                temporary = target_folder / 'creation.partial.mp4'
                if temporary.exists():
                    raise RuntimeError(f'Reconcile interrupted partial file before resuming: {temporary}')
                x, y, width, height = GAMEPLAY
                command = ['ffmpeg', '-nostdin', '-v', 'error', '-i', str(source),
                           '-map', '0:v:0', '-an', '-sn', '-dn', '-map_metadata', '-1',
                           '-vf', f'crop={width}:{height}:{x}:{y},scale=482:994,fps=12',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27',
                           '-pix_fmt', 'yuv420p', '-threads', '2', '-movflags', '+faststart',
                           '-n', str(temporary)]
                if not (resume and target.is_file()):
                    process = subprocess.Popen(command, stdout=subprocess.DEVNULL,
                                               stderr=subprocess.PIPE)
                    print(json.dumps(dict(encoding_started=folder.name, pid=process.pid)), flush=True)
                    _, errors = process.communicate()
                    if process.returncode:
                        raise RuntimeError(f'Encoding failed for {folder.name}: {errors.decode()[:700]}')
                    temporary.rename(target)
                probe = json.loads(subprocess.check_output([
                    'ffprobe', '-v', 'error', '-show_entries',
                    'format=duration:stream=codec_type,width,height', '-of', 'json', str(target)], text=True))
                if len(probe['streams']) != 1 or probe['streams'][0]['codec_type'] != 'video':
                    raise RuntimeError('Expected exactly one silent video stream')
                stream = probe['streams'][0]
                if (stream['width'], stream['height']) != VIDEO_SIZE:
                    raise RuntimeError('Wrong exported video dimensions')
                original_duration = float(subprocess.check_output([
                    'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                    '-of', 'default=noprint_wrappers=1:nokey=1', str(source)], text=True))
                if abs(float(probe['format']['duration']) - original_duration) > .2:
                    raise RuntimeError(f'Incomplete or mismatched exported clip: {folder.name}')
                record(source, target, dict(crop=list(GAMEPLAY), output_size=list(VIDEO_SIZE),
                                           fps=12, audio=False, source_metadata_removed=True,
                                           exported_probe=probe))
        if len(attempts) % 50 == 0:
            print(json.dumps(dict(attempt_folders_exported=len(attempts))), flush=True)

    index = dict(schema='nail-study-local-review-package/v1',
                 status='LOCAL REVIEW CANDIDATE — NOT PRIVACY/REVIEW APPROVED FOR PUBLICATION',
                 original_media='retained privately; package media are derivatives',
                 beauty='100 accepted-change records do not certify beauty P0',
                 full_hands='none completed; ad gate awaiting Alex',
                 attempts=attempts, files=records)
    (destination / 'manifest.json').write_text(json.dumps(index, indent=2) + '\n')
    print(json.dumps(dict(package=str(destination), attempt_folders=len(attempts),
                          videos=sum(a['recorded'] for a in attempts), files=len(records),
                          elapsed_seconds=round(time.monotonic()-started, 2))), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--resume', action='store_true', help='Reuse named completed exports; validate streams/duration and rebuild the manifest')
    arguments = parser.parse_args()
    build(arguments.destination.resolve(), resume=arguments.resume)
