"""Package already inspected five-cycle/glaze evidence; no publication."""
import json,shutil,subprocess,sys
from pathlib import Path
from study_driver import checked_id
R=Path(__file__).resolve().parent;idea=checked_id(sys.argv[1]);out=R.parent.parent/'outputs'
p=R/'study.json';s=json.loads(p.read_text());i=next(i for i in s['ideas'] if i['id']==idea)
assert len(i['accepted_cycles'])==5
glaze=R/'attempts'/(idea+'-glaze');close=R/'attempts'/(idea+'-glazed-closeup')
for f in (glaze,close):
    assert json.loads((f/'execution.json').read_text())['failure'] is None
    assert (f/'creation.mp4').stat().st_size>0
shutil.copyfile(glaze/'final-full.png',out/f'study-{idea}-glazed-hand.png')
shutil.copyfile(close/'final-full.png',out/f'study-{idea}-glazed-closeup.png')
subprocess.run(['magick',str(glaze/'final-full.png'),'-crop','140x160+310+1000','+repage','-resize','560x640',str(glaze/'hand-detail.png')],check=True)
(glaze/'hand-detail-mapping.json').write_text(json.dumps(dict(source='final-full.png',crop_origin=[310,1000],crop_size=[140,160],display_size=[560,640],scale=4),indent=2)+'\n')
shutil.copyfile(glaze/'hand-detail.png',out/f'study-{idea}-glazed-detail.png')
imgs=[]
for ref in [i['baseline']]+i['accepted_cycles']:
    imgs.append(str(R/i.get('effective_final_images',{}).get(ref,ref+'/final-nail.png')))
subprocess.run(['magick','montage',*imgs,'-tile','3x2','-geometry','400x850+8+8',str(out/f'study-{idea}-progression.png')],check=True)
i['pending']=None;i['status']='five-improvements-and-glaze-captured';i['glaze']=dict(transition='attempts/'+idea+'-glaze',closeup='attempts/'+idea+'-glazed-closeup',saved_gallery_persistence_tested=False)
p.write_text(json.dumps(s,indent=2)+'\n')
