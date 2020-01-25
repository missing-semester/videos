from lib import *
from typing import Dict, Any

audio = 'MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_1.mp4'
tracking = 'MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_1.mp4'
screen = 'MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_2.mp4'
chalkboard = 'MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_3.mp4'
wide = 'MIT-Missing-Semester-lec-mit-0000-2020jan14-1400-Adhoc Section_4.mp4'

audio_volume = 10.0
audio_offset = -0.06
overlay_params: Dict[str, Any] = {'crop_x': 1466, 'crop_y': 458, 'crop_width': 454, 'opacity': 0.85}

Multitrack([
  Clip(Fullscreen(wide), start='04:40', end='05:40'),
  Clip(Overlay(screen, wide, **overlay_params), end='51:55'),
  Clip(Fullscreen(wide), end='53:35')
], audio, audio_volume, audio_offset).render('lec2.mp4')

