from lib import *

audio = 'MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_1.mp4'
tracking_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_1.mp4'
screen_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_2.mp4'
wide_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_4.mp4'

wide = Fullscreen(wide_f)
tracking = Fullscreen(tracking_f)
screen = Overlay(screen_f, wide_f, crop_x=1176, crop_y=367, crop_width=744, opacity=0.85)

audio_volume = 10.0
audio_offset = -0.06

Playlist([
  Clip(tracking, start='6:27', end='7:48'),
  Clip(screen, end='55:40'),
  Clip(tracking, end='56:30'),
], audio, audio_volume, audio_offset).render('lec4.mp4')
