from lib import *
from typing import Dict, Any

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_1.mp4', delay=6/30)
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_2.mp4', delay=6/30)
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1466, crop_y=458, crop_width=454, opacity=0.85)

Multitrack([
  Clip(wide, start='04:40', end='05:40'),
  Clip(screen, end='51:55'),
  Clip(wide, end='53:35')
], audio).render('lec2.mp4')

