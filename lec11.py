from lib import *

audio = Audio('MIT-Missing-Semester-lec-mit-0000-2020jan30-1405-Adhoc Section_1.mp4', delay=5/30)
screen = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan30-1405-Adhoc Section_2.mp4', delay=5/30)
wide = Fullscreen('MIT-Missing-Semester-lec-mit-0000-2020jan30-1405-Adhoc Section_4.mp4')
main = Overlay(wide, screen, crop_x=0, crop_y=78, crop_width=1920, crop_height=234, width=1920, margin=0, opacity=1, location=Location.TOP_CENTER)

Multitrack([
  Clip(main, start='1:50', end='55:39'),
], audio).render('lec11.mp4')
