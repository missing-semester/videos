from lib import *
from typing import Dict, Any

audio = 'MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_1.mp4'
tracking = 'MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_1.mp4'
screen = 'MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_2.mp4'
chalkboard = 'MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_3.mp4'
wide = 'MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_4.mp4'

audio_volume = 10.0
audio_offset = -0.06
overlay_params: Dict[str, Any] = {'crop_x': 1298, 'crop_y': 356, 'crop_width': 545, 'opacity': 0.85}

Multitrack([
  Clip(Fullscreen(wide), start='22:22', end='26:29'),
  Clip(Fullscreen(tracking), end='28:20'),
  Clip(Overlay(screen, wide, **overlay_params), end='1:08:10'),
  Clip(Fullscreen(tracking), end='1:10:38'),
], audio, audio_volume, audio_offset).render('lec1.mp4')
