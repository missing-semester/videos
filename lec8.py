from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_1.mp4', delay=5/30)
tracking = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_1.mp4')
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_2.mp4', delay=5/30)
chalkboard = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_3.mp4', delay=-1/30)
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan27-1403-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1300, crop_y=384, crop_width=545, opacity=0.85)

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
], audio).render('lec8.mp4')
