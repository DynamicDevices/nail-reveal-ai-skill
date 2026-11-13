#!/usr/bin/env python3
"""Check study counts and evidence continuity, not aesthetic quality."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
study = json.loads((ROOT/'study.json').read_text())
accepted = []

def execution(folder):
    data = json.loads((folder/'execution.json').read_text())
    assert data['failure'] is None, f'Failed execution: {folder.name}'
    video = folder/'creation.mp4'
    assert video.is_file() and video.stat().st_size > 0, f'Missing video: {folder.name}'
    assert float(data['video_probe']['format']['duration']) > 0
    final = folder/(data['stages'][-1]+'-full.png')
    with final.open('rb') as image:
        assert image.read(8) == b'\x89PNG\r\n\x1a\n', f'Invalid final PNG: {folder.name}'
    assert (folder/(data['stages'][-1]+'-nail.png')).is_file()
    assert (folder/'recipe.json').is_file() and (folder/'stages.json').is_file()

for idea in study['ideas']:
    cycles = idea['accepted_cycles']
    assert len(cycles) <= study['target_accepted_cycles_per_idea']
    assert not set(cycles).intersection(idea.get('rejected_attempts',[]))
    for relative in cycles:
        folder = ROOT/relative
        execution(folder)
        assessment = (folder/'ASSESSMENT.md').read_text()
        assert 'accepted' in assessment.splitlines()[0].lower()
        accepted.append(relative)
    for relative in idea.get('rejected_attempts',[]):
        folder = ROOT/relative
        assert 'rejected' in (folder/'ASSESSMENT.md').read_text().splitlines()[0].lower()
        execution(folder)
    for relative in idea.get('finishing_attempts',[]):
        execution(ROOT/relative)
    for relative in idea.get('restorations',[]):
        execution(ROOT/relative)
        assert (ROOT/relative/'ASSESSMENT.md').is_file(), f'Missing restoration assessment: {relative}'
    for relative, image in idea.get('effective_final_images',{}).items():
        assert relative in cycles and (ROOT/image).is_file()
    if idea['status'] == 'five-improvements-and-glaze-captured':
        assert len(cycles) == 5
        for key in ('transition','closeup'):
            execution(ROOT/idea['glaze'][key])
assert len(accepted) == len(set(accepted)) == study['accepted_cycles_total']
assert study['target_distinct_ideas'] * study['target_accepted_cycles_per_idea'] == study['target_accepted_cycles_total'] == 100
print(f'PASS: {len(accepted)}/100 accepted-cycle evidence chains; rejection separation and completed-idea glaze artifacts. This does not certify beauty, full study completion, publication or persistence.')
