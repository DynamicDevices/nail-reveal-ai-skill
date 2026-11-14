"""Glazed Hand contact sheet,retaining exact source/crop mappings."""
import json,textwrap
from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;out=R.parent.parent/'outputs'
study=json.loads((R/'study.json').read_text());ideas=study['ideas']
assert len(ideas)==20 and all(i.get('glaze') for i in ideas)
sheet=Image.new('RGB',(1400,1480),'white');mapping=[]
for k,i in enumerate(ideas):
    src=out/f"study-{i['id']}-glazed-hand.png"
    with Image.open(src) as full:
        assert full.size==(1080,2400),(i['id'],full.size)
        tile=Image.new('RGB',(280,370),'white')
        tile.paste(full.crop((310,1000,450,1160)).resize((280,320)),(0,0))
    draw=ImageDraw.Draw(tile)
    for n,t in enumerate(textwrap.wrap(i['id'].upper()+' - '+i['concept'],width=40)[:3]):
        draw.text((5,325+13*n),t,fill='black')
    x=(k%5)*280;y=(k//5)*370;sheet.paste(tile,(x,y))
    mapping.append(dict(idea=i['id'],source=str(src),source_size=[1080,2400],crop_origin=[310,1000],crop_size=[140,160],display_size=[280,320],scale=2,tile_origin=[x,y]))
sheet.save(out/'study-twenty-glazed-designs.png')
(out/'study-twenty-glazed-designs-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(str(out/'study-twenty-glazed-designs.png'))
selected=['d03','d05','d06','d08','d20']
detail=Image.new('RGB',(2000,880),'white');detailmap=[]
for k,idea in enumerate(selected):
    entry=next(i for i in ideas if i['id']==idea)
    src=R/entry['glaze']['closeup']/'final-full.png'
    with Image.open(src) as full:
        assert full.size==(1080,2400),(idea,full.size)
        detail.paste(full.crop((140,400,940,2100)).resize((400,850)),(k*400,30))
    ImageDraw.Draw(detail).text((k*400+8,8),idea.upper()+' - SHORTLIST REVIEW',fill='black')
    detailmap.append(dict(idea=idea,source=str(src),crop_origin=[140,400],crop_size=[800,1700],display_size=[400,850],scale=.5,tile_origin=[k*400,30]))
detail.save(out/'study-shortlist-closeups.png')
(out/'study-shortlist-closeups-mapping.json').write_text(json.dumps(detailmap,indent=2)+'\n')
print(str(out/'study-shortlist-closeups.png'))
