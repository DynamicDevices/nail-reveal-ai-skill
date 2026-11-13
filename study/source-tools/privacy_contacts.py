"""Sample every exported clip for a local visual privacy review; no publication."""
import io
import json
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw

root = Path(sys.argv[1]).resolve()
destination = Path(sys.argv[2]).resolve()
destination.mkdir(exist_ok=False)
manifest = json.loads((root / 'manifest.json').read_text())
videos = [f for f in manifest['files'] if f['path'].endswith('.mp4')]
pages = []
sheet = None
for index, record in enumerate(videos):
    position = index % 12
    if position == 0:
        sheet = Image.new('RGB', (1260, 1240), 'white')
        draw = ImageDraw.Draw(sheet)
    duration = float(record['transform']['exported_probe']['format']['duration'])
    x, y = (position % 3) * 420, (position // 3) * 310
    label = Path(record['path']).parent.name
    draw.text((x+3, y+3), label, fill='black')
    for sample, instant in enumerate([0, duration/2, max(0, duration-.3)]):
        pixels = subprocess.check_output([
            'ffmpeg', '-nostdin', '-v', 'error', '-ss', str(instant),
            '-i', str(root / record['path']), '-frames:v', '1',
            '-vf', 'scale=140:288', '-f', 'image2pipe', '-vcodec', 'png', '-threads', '1', '-'])
        with Image.open(io.BytesIO(pixels)) as picture:
            sheet.paste(picture, (x+sample*140, y+19))
    if position == 11 or index == len(videos)-1:
        path = destination / f'clips-{len(pages)+1:02d}.jpg'
        sheet.save(path, quality=90)
        pages.append(dict(path=path.name, first_index=index-position,
                          last_index=index, clips=[v['path'] for v in videos[index-position:index+1]]))
        if len(pages) == 1:
            print(json.dumps(dict(first_contact_sheet=str(path))), flush=True)
(destination / 'index.json').write_text(json.dumps(dict(
    method='Every clip sampled at start, midpoint and near end; not a frame-by-frame review.',
    videos=len(videos), pages=pages), indent=2)+'\n')
print(json.dumps(dict(videos=len(videos), pages=len(pages), index=str(destination/'index.json'))))
