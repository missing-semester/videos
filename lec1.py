from lib import *

audio = Audio('MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_1.mp4', delay=6/30)
tracking = Fullscreen('MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_1.mp4')
screen_only = Fullscreen('MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_2.mp4', delay=6/30)
wide = Fullscreen('MIT-Adhoc Course-lec-mit-0000-2020jan13-1343-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1298, crop_y=356, crop_width=545, opacity=0.85)

Multitrack([
  Clip(wide, start='22:22', end='26:29'),
  Clip(tracking, end='28:20'),
  Clip(screen, end='1:08:10'),
  Clip(tracking, end='1:10:38'),
], audio).render('lec1.mp4')
