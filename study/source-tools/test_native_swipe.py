"""Focused local safety/compilation checks, not a live quality benchmark."""
import unittest
from study_driver import compile_steps
class NativeSwipe(unittest.TestCase):
    def test_command(self):
        self.assertEqual(compile_steps([dict(type='native-swipe',start=[240,1130],end=[840,1130],duration_ms=1200)]),['input swipe 240 1130 840 1130 1200'])
    def test_invalid(self):
        for change in [dict(start=[540,1920]),dict(end=[1080,1200]),dict(duration_ms=0),dict(duration_ms=-1),dict(duration_ms=True)]:
            step=dict(type='native-swipe',start=[240,1130],end=[840,1130],duration_ms=1200);step.update(change)
            with self.assertRaises(ValueError):compile_steps([step])
    def test_dense_unchanged(self):
        self.assertEqual(compile_steps([dict(type='path',points=[[240,1130],[250,1130]])]),['input motionevent DOWN 240 1130','sleep 0.25','input motionevent MOVE 250 1130','sleep 0.3','input motionevent UP 250 1130'])
if __name__=='__main__':unittest.main()
