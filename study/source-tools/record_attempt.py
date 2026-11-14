#!/usr/bin/env python3
"""Record one prewritten finite candidate, preserve its images/video, then stop."""
import json
from pathlib import Path
import re
import subprocess
import sys
import time
from study_driver import ROOT, checked_id, compile_steps

attempt = checked_id(sys.argv[1])
folder = ROOT / 'attempts' / attempt
stages = json.loads((folder/'stages.json').read_text())
for label, steps in stages.items():
    checked_id(label)
    compile_steps(steps)
rows = subprocess.check_output(['adb','devices'],text=True).splitlines()[1:]
serials = [r.split()[0] for r in rows if len(r.split()) >= 2 and r.split()[1] == 'device']
if len(serials) != 1:
    raise RuntimeError('Device selection needs reconciliation')
adb = ['adb','-s',serials[0]]
if subprocess.check_output(adb+['shell','getprop','ro.product.model'],text=True).strip() != 'A063':
    raise RuntimeError('Selected phone model changed')
focus = subprocess.check_output(adb+['shell','dumpsys','window'],text=True)
if not any('com.onteca.nailreveal' in l for l in focus.splitlines() if 'mCurrentFocus' in l):
    raise RuntimeError('Game no longer focused')
if subprocess.run(adb+['shell','pidof','screenrecord'],capture_output=True).stdout.strip():
    raise RuntimeError('Reconcile existing recorder before starting another')
video = folder/'creation.mp4'
if video.exists():
    raise RuntimeError('Never overwrite attempt evidence')
remote = '/sdcard/Download/nail-study-'+attempt+'.mp4'
log = (folder/'recorder.log').open('wb')
recorder = subprocess.Popen(adb+['shell','screenrecord','--bit-rate','4000000','--time-limit','0',remote],stdout=log,stderr=subprocess.STDOUT)
pid = None
failure = None
started = time.monotonic()
try:
    time.sleep(.5)
    pid = subprocess.check_output(adb+['shell','pidof','screenrecord'],text=True).strip()
    if recorder.poll() is not None or not re.fullmatch(r'\d+',pid):
        raise RuntimeError('Recorder startup not confirmed; do not paint')
    print(json.dumps({'recording_confirmed':True,'attempt':attempt}),flush=True)
    for label in stages:
        if recorder.poll() is not None:
            raise RuntimeError('Recording stopped; no further painting')
        subprocess.run([sys.executable,'-B',str(ROOT/'render_batch.py'),attempt,label],check=True,timeout=110)
except BaseException as error:
    failure = type(error).__name__+': '+str(error)
finally:
    if pid and re.fullmatch(r'\d+',pid):
        subprocess.run(adb+['shell','kill','-2',pid],capture_output=True,timeout=10)
    try:
        recorder.wait(timeout=20)
    except subprocess.TimeoutExpired:
        failure = (failure or '')+' Recorder did not finalise; reconcile before restart.'
    log.close()
    subprocess.run(adb+['pull',remote,str(video)],capture_output=True,timeout=30,check=True)
    probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','json',str(video)],text=True))
    result = {'attempt':attempt,'recording_start_confirmed':pid is not None,'video':str(video),'video_probe':probe,'elapsed_seconds':round(time.monotonic()-started,3),'stages':list(stages),'failure':failure,'accepted':None}
    (folder/'execution.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
if failure:
    raise SystemExit(1)
