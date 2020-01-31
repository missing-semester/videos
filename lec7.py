from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_1.mp4', delay=7/30)
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_2.mp4', delay=5/30)
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan23-1402-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1182, crop_y=394, crop_width=545, opacity=0.85)

Multitrack([
  Clip(wide, start='2:42', end='5:05'),
  Clip(screen, end='13:52'),
  Clip(wide, end='15:00'),
  Clip(screen, end='42:36'),
  Clip(wide, end='43:30'),
  Clip(screen, end='53:40'),
  Clip(wide, end='56:55'),
], audio).render('lec7.mp4')
