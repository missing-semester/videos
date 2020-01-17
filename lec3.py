from lib import *

audio = 'MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_1.mp4'
tracking_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_1.mp4'
screen_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_2.mp4'
chalkboard_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_3.mp4'
wide_f = 'MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_4.mp4'

wide = Fullscreen(wide_f)
tracking = Fullscreen(tracking_f)
chalkboard = Fullscreen(chalkboard_f)
screen = Overlay(screen_f, wide_f, crop_x=1458, crop_y=394, crop_width=462)

audio_volume = 10.0
audio_offset = -0.06

Playlist([
  Clip(wide, start='0:38', end='1:30'),
  Clip(tracking, end='5:25'),
  Clip(chalkboard, end='8:55'),
  Clip(tracking, end='10:10'),
  Clip(screen, end='20:08'),
  Clip(tracking, end='21:00'),
  Clip(screen, end='48:00'),
  Clip(wide, end='49:04'),
], audio, audio_volume, audio_offset).render('lec3.mp4')
