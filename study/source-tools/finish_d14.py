"""Package inspected D14 evidence; does not publish or certify beauty."""
from prepare_d14 import *
import shutil,subprocess
out=R.parent.parent/'outputs'
s=json.loads((R/'study.json').read_text());i=s['ideas'][-1];assert i['id']=='d14' and len(i['accepted_cycles'])==5
i['concept']='Gold umbrella with scarlet canopy inset on black'
i['pending']=None;i['status']='five-improvements-and-glaze-captured'
i['glaze']=dict(transition='attempts/d14-glaze',closeup='attempts/d14-glazed-closeup',saved_gallery_persistence_tested=False)
(R/'study.json').write_text(json.dumps(s,indent=2)+'\n')
for a,label in [('d14-glazed-closeup','closeup'),('d14-glaze','hand')]:
    shutil.copyfile(R/'attempts'/a/'final-full.png',out/f'study-d14-glazed-{label}.png')
subprocess.run(['magick',str(R/'attempts/d14-glaze/final-full.png'),'-crop','140x160+310+1000','+repage','-resize','560x640',str(R/'attempts/d14-glaze/hand-detail.png')],check=True)
imgs=[str(R/'attempts'/a/'final-nail.png') for a in ['d14-baseline','d14-c01-a01','d14-c02-a01','d14-c03-a01','d14-c04-a01','d14-c05-a03']]
subprocess.run(['magick','montage',*imgs,'-tile','3x2','-geometry','400x850+8+8',str(out/'study-d14-progression.png')],check=True)
