#!/usr/bin/env python3
"""Known-working finite ADB fallback, with replayable stage inputs and captures."""
import json
from pathlib import Path
import subprocess
import sys
import time
from study_driver import ROOT, checked_id, compile_steps

attempt, stage = map(checked_id, sys.argv[1:])
folder = ROOT / 'attempts' / attempt
steps = json.loads((folder / 'stages.json').read_text())[stage]
commands = compile_steps(steps)
rows = subprocess.check_output(['adb','devices'],text=True).splitlines()[1:]
serials = [r.split()[0] for r in rows if len(r.split()) >= 2 and r.split()[1] == 'device']
if len(serials) != 1:
    raise RuntimeError('Selected device needs reconciliation')
adb = ['adb','-s',serials[0]]
if subprocess.check_output(adb+['shell','getprop','ro.product.model'],text=True).strip() != 'A063':
    raise RuntimeError('Device model changed')
pid = subprocess.run(adb+['shell','pidof','screenrecord'],capture_output=True,text=True)
if not pid.stdout.strip():
    raise RuntimeError('Recorder absent; do not paint')
remote = '/sdcard/nail-study-stage.png'
script = ' && '.join(commands + ['input motionevent UP 1040 2100','sleep 0.15','screencap -p '+remote])
script_file = folder / (stage + '.android-shell.txt')
script_file.write_text(script+'\n')
started = time.monotonic()
try:
    subprocess.run(adb+['shell',script],check=True,timeout=90)
except BaseException:
    subprocess.run(adb+['shell','input','motionevent','UP','540','1300'],timeout=10,capture_output=True)
    raise
full = folder / (stage+'-full.png')
subprocess.run(adb+['pull',remote,str(full)],check=True,capture_output=True)
preview = folder / (stage+'-nail.png')
subprocess.run(['magick',str(full),'-crop','800x1700+140+400','+repage','-resize','400x850',str(preview)],check=True)
result = {'stage':stage,'seconds':round(time.monotonic()-started,3),'full':str(full),'preview':str(preview),'crop_origin':[140,400],'scale':.5,'steps':steps}
with (folder/'finite-batches.jsonl').open('a') as log:
    log.write(json.dumps(result)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'steps'}))
