from lib import *
from typing import Dict, Any

audio = 'MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_1.mp4'
tracking_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_1.mp4'
screen_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_2.mp4'
chalkboard_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_3.mp4'
wide_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_4.mp4'

overlay_params: Dict[str, Any] = {'crop_x': 1300, 'crop_y': 384, 'crop_width': 545, 'opacity': 0.85}

wide = Fullscreen(wide_f)
tracking = Fullscreen(tracking_f)
chalkboard = Fullscreen(chalkboard_f)
screen = Overlay(screen_f, wide_f, **overlay_params)

audio_volume = 10.0
audio_offset = -0.06

Multitrack([
  Clip(tracking, start='1:47', end='5:37'),
  Clip(screen, end='14:09'),
  Clip(tracking, end='18:12'),
  Clip(chalkboard, end='18:46'),
  Clip(tracking, end='21:54'),
  Clip(chalkboard, end='22:56'),
  Clip(wide, end='25:07'),
  Clip(tracking, end='33:40'),
  Clip(screen, end='34:28'),
  Clip(tracking, end='35:29'),
  Clip(screen, end='36:09'),
  Clip(tracking, end='46:24'),
  Clip(screen, end='46:34'),
  Clip(tracking, end='47:10'),
  Clip(screen, end='47:18'),
  Clip(tracking, end='47:55'),
  Clip(screen, end='48:03'),
  Clip(tracking, end='48:49'),
  Clip(wide, end='48:53'),
  Clip(chalkboard, end='51:13'),
  Clip(wide, end='51:39'),
], audio, audio_volume, audio_offset).render('lec8.mp4')

