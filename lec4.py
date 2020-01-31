from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_1.mp4', delay=4/30)
tracking = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_1.mp4', delay=-1/30)
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_2.mp4', delay=5/30)
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan16-1359-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1176, crop_y=367, crop_width=744, opacity=0.85)

Multitrack([
  Clip(tracking, start='6:27', end='7:48'),
  Clip(screen, end='55:40'),
  Clip(tracking, end='56:30'),
], audio).render('lec4.mp4')
