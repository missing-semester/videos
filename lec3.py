from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_1.mp4', delay=6/30)
tracking = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_1.mp4', delay=-1/30)
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_2.mp4', delay=5/30)
chalkboard = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_3.mp4')
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan15-1406-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1458, crop_y=394, crop_width=462, opacity=0.85)

Multitrack([
  Clip(wide, start='0:38', end='5:25'), # tracking cam isn't locked in at start
  Clip(chalkboard, end='8:55'),
  Clip(wide, end='10:10'), # tracking cam is a bit jumpy here
  Clip(screen, end='20:08'),
  Clip(tracking, end='21:00'),
  Clip(screen, end='48:00'),
  Clip(wide, end='49:04'),
], audio).render('lec3.mp4')
