from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan28-1405-Adhoc Section_1.mp4', delay=5/30)
tracking = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan28-1405-Adhoc Section_1.mp4')
screen_only = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan28-1405-Adhoc Section_2.mp4', delay=5/30)
chalkboard = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan28-1405-Adhoc Section_3.mp4')
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan28-1405-Adhoc Section_4.mp4')
screen = Overlay(screen_only, wide, crop_x=1245, crop_y=447, crop_width=456, opacity=0.85)

Multitrack([
  Clip(tracking, start='0:23'),
  Clip(screen, start='2:16'),
  Clip(wide, start='3:13'),
  Clip(chalkboard, start='3:20'),
  Clip(wide, start='7:17'),
  Clip(chalkboard, start='8:20'),
  Clip(wide, start='9:10'),
  Clip(screen, start='9:20'),
  Clip(wide, start='10:20'),
  Clip(chalkboard, start='10:30'),
  Clip(wide, start='11:25'),
  Clip(screen, start='12:08'),
  Clip(wide, start='12:20'),
  Clip(screen, start='14:53'),
  Clip(wide, start='15:20'),
  Clip(screen, start='20:33'),
  Clip(wide, start='21:20'),
  Clip(chalkboard, start='21:50'),
  Clip(wide, start='23:00'),
  Clip(chalkboard, start='24:25'),
  Clip(wide, start='27:00'),
  Clip(chalkboard, start='30:30'),
  Clip(wide, start='31:05'),
  Clip(screen, start='31:58'),
  Clip(wide, start='33:35'),
  Clip(chalkboard, start='36:50'),
  Clip(wide, start='38:00'),
  Clip(chalkboard, start='38:50'),
  Clip(wide, start='41:00'),
  Clip(chalkboard, start='44:16'),
  Clip(wide, start='46:05'),
  Clip(screen, start='48:30'),
  Clip(wide, start='49:40'),
  Clip(chalkboard, start='56:20'),
  Clip(wide, start='59:55', end='1:01:22')
], audio).render('lec9.mp4')
