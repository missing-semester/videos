from lib import *
from typing import Dict, Any

audio = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_1.mp4'
tracking_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_1.mp4'
screen_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_2.mp4'
chalkboard_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_3.mp4'
wide_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_4.mp4'

overlay_params: Dict[str, Any] = {'crop_x': 1182, 'crop_y': 394, 'crop_width': 545, 'opacity': 0.85}

wide = Fullscreen(wide_f)
tracking = Fullscreen(tracking_f)
chalkboard = Fullscreen(chalkboard_f)
screen = Overlay(screen_f, wide_f, **overlay_params)

audio_volume = 10.0
audio_offset = -0.06

Playlist([
  Clip(wide, start='2:42', end='5:05'),
  Clip(screen, end='13:52'),
  Clip(wide, end='15:00'),
  Clip(screen, end='42:36'),
  Clip(wide, end='43:30'),
  Clip(screen, end='53:40'),
  Clip(wide, end='56:55'),
], audio, audio_volume, audio_offset).render('lec7.mp4')
