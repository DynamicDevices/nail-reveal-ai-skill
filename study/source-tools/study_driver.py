#!/usr/bin/env python3
"""Interactive, finite study batches; one retained ADB control shell, no daemon.

JSON commands: begin(id, recipe), run(steps, label), capture(label), finish, quit.
Steps: colour(x,y), tool(x,y), path(points, initial=.25, final=.3), hold(x,y,t), coat.
All source media remains private. Outputs are not automatically published.
"""
import json
import os
from pathlib import Path
import re
import select
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def checked_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,70}', value):
        raise ValueError('Unsafe artifact identifier')
    return value


def point(x, y):
    if type(x) is not int or type(y) is not int or not 0 <= x < 1080 or not 0 <= y < 2400:
        raise ValueError('Point outside calibrated display')
    return f'{x} {y}'


def dwell(value):
    if type(value) not in (int, float) or not 0 <= value <= 2:
        raise ValueError('Invalid contact dwell')
    return str(value)


def compile_steps(steps):
    result = []
    for step in steps:
        kind = step['type']
        if kind == 'colour':
            result += ['input tap 230 2200', 'sleep 0.7',
                       'input tap ' + point(step['x'], step['y']), 'sleep 0.7',
                       'input tap 540 1740', 'sleep 0.7']
        elif kind == 'tool':
            result += ['input tap ' + point(step['x'], step['y']), 'sleep 0.3']
        elif kind == 'native-swipe':
            # Optional straight-line primitive. Do not automatically replay on
            # failure: inspect partial effects and resume with the dense path.
            start, end = step['start'], step['end']
            start_text, end_text = point(*start), point(*end)
            if 430 <= start[0] <= 810 and 1870 <= start[1] <= 1990:
                raise ValueError('Swipe DOWN targets the known Choose colour button')
            duration = step['duration_ms']
            if type(duration) is not int or duration <= 0:
                raise ValueError('Swipe duration must be a positive integer in milliseconds')
            result.append(f'input swipe {start_text} {end_text} {duration}')
        elif kind == 'wait':
            duration = step['seconds']
            if type(duration) not in (int, float) or not 0 <= duration <= 15:
                raise ValueError('Transition wait must be finite and at most 15 seconds')
            result.append('sleep ' + str(duration))
        elif kind in ('path', 'hold', 'coat', 'coat-v2'):
            if kind in ('coat', 'coat-v2'):
                points = [[230,850],[200,480]]
                for i, x in enumerate([200,300,400,500,600,700,800,900,850,750,650,550,450,350,250]):
                    if kind == 'coat-v2':
                        # Traverse at the endpoint before reversing, rather
                        # than shortcut diagonally toward the next mid-height.
                        points.append([x, 480 if i % 2 == 0 else 2170])
                    points += [[x,y] for y in ([1000,1500,2170] if i % 2 == 0 else [1500,1000,480])]
            elif kind == 'hold':
                points = [[step['x'],step['y']]]
            else:
                points = step['points']
            if not points:
                raise ValueError('Empty path')
            # Tested painting-layout button: do not mistake the upward visual
            # brush offset for permission to start a contact on this control.
            start_x, start_y = points[0]
            if 430 <= start_x <= 810 and 1870 <= start_y <= 1990:
                raise ValueError('Paint DOWN targets the known Choose colour button; redesign the contact')
            result += ['input motionevent DOWN ' + point(*points[0]),
                       'sleep ' + dwell(step.get('initial', .25))]
            for x,y in points[1:]:
                result.append('input motionevent MOVE ' + point(x,y))
                if kind in ('coat', 'coat-v2') and y in (480,2170):
                    result.append('sleep 0.2')
            result += ['sleep ' + dwell(step.get('t', step.get('final', .3))),
                       'input motionevent UP ' + point(*points[-1])]
        else:
            raise ValueError('Unknown primitive')
    return result


class Study:
    def __init__(self):
        rows = subprocess.check_output(['adb','devices'], text=True).splitlines()[1:]
        devices = [r.split()[0] for r in rows if len(r.split()) >= 2 and r.split()[1] == 'device']
        if len(devices) != 1:
            raise RuntimeError('Expected exactly the previously selected authorised phone')
        self.adb = ['adb','-s',devices[0]]
        model = subprocess.check_output(self.adb + ['shell','getprop','ro.product.model'], text=True).strip()
        if model != 'A063':
            raise RuntimeError('Selected device model changed')
        self.shell = subprocess.Popen(self.adb + ['shell'], stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
        self.buffer = b''
        self.sequence = 0
        self.recording = None
        self.folder = None

    def batch(self, commands):
        self.sequence += 1
        marker = f'NAIL_STUDY_{self.sequence}_DONE:'
        # Every primitive is validated/generated locally, not taken from game text.
        script = '( ' + ' && '.join(commands) + ' ); nail_rc=$?; '
        script += "input motionevent UP 540 1300 >/dev/null 2>&1; printf '\\n" + marker + "%s\\n' \"$nail_rc\"\n"
        self.shell.stdin.write(script.encode()); self.shell.stdin.flush()
        deadline = time.monotonic() + 120
        while time.monotonic() < deadline:
            ready, _, _ = select.select([self.shell.stdout], [], [], min(1, max(0, deadline-time.monotonic())))
            if ready:
                block = os.read(self.shell.stdout.fileno(), 65536)
                if not block:
                    raise RuntimeError('Control shell disconnected; reconcile state before replay')
                self.buffer += block
                match = re.search(re.escape(marker.encode()) + rb'(\d+)\r?\n', self.buffer)
                if match:
                    transcript = self.buffer[:match.end()]
                    self.buffer = self.buffer[match.end():]
                    if self.folder:
                        with (self.folder / 'control.log').open('ab') as log:
                            log.write(script.encode() + transcript)
                    if match[1] != b'0':
                        raise RuntimeError('Batch failed; inspect current canvas before retry')
                    return
        raise RuntimeError('Finite batch deadline exceeded; no automatic replay')

    def capture(self, label, commands=None):
        label = checked_id(label)
        remote = '/sdcard/nail-study-capture.png'
        self.batch((commands or []) + ['screencap -p ' + remote])
        full = self.folder / (label + '-full.png')
        subprocess.run(self.adb + ['pull',remote,str(full)], check=True, capture_output=True)
        preview = self.folder / (label + '-nail.png')
        subprocess.run(['magick',str(full),'-crop','800x1700+140+400','+repage','-resize','400x850',str(preview)], check=True)
        return {'full':str(full),'preview':str(preview),'mapping':{'origin':[140,400],'scale':.5}}

    def command(self, command):
        operation = command['op']
        if operation == 'begin':
            if self.recording:
                raise RuntimeError('Finish current recording first')
            identity = checked_id(command['id'])
            self.folder = ROOT / 'attempts' / identity
            self.folder.mkdir(parents=True, exist_ok=False)
            focus = subprocess.check_output(self.adb + ['shell','dumpsys','window'], text=True)
            if not any('com.onteca.nailreveal' in line for line in focus.splitlines() if 'mCurrentFocus' in line):
                raise RuntimeError('Game focus changed')
            if subprocess.run(self.adb + ['shell','pidof','screenrecord'], capture_output=True).stdout.strip():
                raise RuntimeError('An existing recorder needs reconciliation')
            self.remote_video = '/sdcard/Download/nail-study-' + identity + '.mp4'
            (self.folder / 'recipe.json').write_text(json.dumps(command['recipe'],indent=2)+'\n')
            self.video_log = (self.folder / 'recorder.log').open('wb')
            self.recording = subprocess.Popen(self.adb + ['shell','screenrecord','--bit-rate','4000000','--time-limit','0',self.remote_video],stdout=self.video_log,stderr=subprocess.STDOUT)
            time.sleep(.5)
            pid = subprocess.check_output(self.adb + ['shell','pidof','screenrecord'],text=True).strip()
            if self.recording.poll() is not None or not re.fullmatch(r'\d+',pid):
                raise RuntimeError('Recording startup failed; do not paint')
            self.pid = pid
            return {'recording':'confirmed','attempt':identity}
        if operation == 'finish':
            if not self.recording:
                raise RuntimeError('No active recording')
            subprocess.run(self.adb + ['shell','kill','-2',self.pid],check=True,capture_output=True)
            self.recording.wait(timeout=20); self.video_log.close()
            video = self.folder / 'creation.mp4'
            subprocess.run(self.adb + ['pull',self.remote_video,str(video)],check=True,capture_output=True)
            probe = subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','json',str(video)],text=True)
            self.recording = None
            return {'video':str(video),'probe':json.loads(probe)}
        if not self.folder or not self.recording or self.recording.poll() is not None:
            raise RuntimeError('No confirmed live recording; do not paint')
        if operation in ('capture','run'):
            started = time.monotonic()
            result = self.capture(command['label'],compile_steps(command.get('steps',[])))
            result['batch_capture_seconds'] = round(time.monotonic()-started,3)
            with (self.folder / 'batches.jsonl').open('a') as file:
                file.write(json.dumps({'command':command,'result':result})+'\n')
            return result
        raise ValueError('Unknown operation')


if __name__ == '__main__':
    study = Study()
    print(json.dumps({'ready':True,'control':'one persistent ADB shell','model':'A063'}),flush=True)
    for line in sys.stdin:
        try:
            request = json.loads(line)
            if request.get('op') == 'quit':
                if study.recording:
                    raise RuntimeError('Finish recording before quitting')
                study.shell.stdin.write(b'exit\n');study.shell.stdin.flush()
                break
            print(json.dumps(study.command(request)),flush=True)
        except Exception as error:
            print(json.dumps({'error':str(error),'automatic_retry':False}),flush=True)
