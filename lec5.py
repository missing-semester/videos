from lib import *
from typing import Dict, Any

audio = 'MIT-Missing-Semeste-lec-mit-0000-2020jan21-1400-Adhoc Section_1.mp4'
tracking_f = 'MIT-Missing-Semeste-lec-mit-0000-2020jan21-1400-Adhoc Section_1.mp4'
screen_f = 'MIT-Missing-Semeste-lec-mit-0000-2020jan21-1400-Adhoc Section_2.mp4'
chalkboard_f = 'MIT-Missing-Semeste-lec-mit-0000-2020jan21-1400-Adhoc Section_3.mp4'
wide_f = 'MIT-Missing-Semeste-lec-mit-0000-2020jan21-1400-Adhoc Section_4.mp4'

overlay_params: Dict[str, Any] = {'crop_x': 1182, 'crop_y': 394, 'crop_width': 545, 'opacity': 0.85}

wide = Fullscreen(wide_f)
tracking = Fullscreen(tracking_f)
chalkboard = Fullscreen(chalkboard_f)
screen = Overlay(screen_f, wide_f, **overlay_params)

audio_volume = 10.0
audio_offset = -0.06

Multitrack([
  Clip(wide, start='4:42', end='6:16'),
  Clip(chalkboard, end='6:53'),
  Clip(tracking, end='7:25'),
  Clip(screen, end='18:00'),
  Clip(wide, end='20:17'),
  Clip(chalkboard, end='20:35'),
  Clip(wide, end='20:47'),
  Clip(screen, end='28:45'),
  Clip(wide, end='30:30'),
  Clip(screen, end='42:47'),
  Clip(chalkboard, end='44:24'),
  Clip(wide, end='48:00'),
  Clip(screen, end='58:00'),
  Clip(wide, end='58:56'),
  Clip(screen, end='59:50'),
  Clip(wide, end='1:00:48'),
], audio, audio_volume, audio_offset).render('lec5.mp4')

