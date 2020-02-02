from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan29-1401-Adhoc Section_1.mp4', delay=5/30)
tracking = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan29-1401-Adhoc Section_1.mp4', delay=-1/30)
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan29-1401-Adhoc Section_2.mp4', delay=5/30)
chalkboard = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan29-1401-Adhoc Section_3.mp4')
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan29-1401-Adhoc Section_4.mp4')
screen_wide = Overlay(screen_only, wide, crop_x=0, crop_y=0, crop_width=1920, opacity=0.85) # can't do better because speaker moves around
screen_lectern = Overlay(screen_only, wide, crop_x=1192, crop_y=459, crop_width=473, opacity=0.85)

Multitrack([
  Clip(wide, start='3:46'),
  Clip(screen_wide, start='12:30'),
  Clip(wide, start='14:38'),
  Clip(chalkboard, start='16:19'),
  Clip(wide, start='19:21'),
  Clip(chalkboard, start='34:03'),
  Clip(wide, start='35:50'),
  Clip(chalkboard, start='43:35'),
  Clip(wide, start='44:50'),
  Clip(screen_lectern, start='46:26'),
  Clip(wide, start='49:30'),
  Clip(screen_lectern, start='52:00'),
  Clip(wide, start='53:30'),
  Clip(screen_lectern, start='56:05'),
  Clip(wide, start='56:55'),
  Clip(screen_lectern, start='57:20'),
  Clip(wide, start='57:30'),
  Clip(screen_lectern, start='58:47'),
  Clip(wide, start='1:00:15', end='1:01:40'),
], audio).render('lec10.mp4')
