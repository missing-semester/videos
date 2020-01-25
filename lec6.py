from lib import *

part_1 = 'MIT-Missing-Semester-lec-mit-0000-2020jan22-1406-Adhoc Section_{}.mp4'
audio_1 = part_1.format(1)
screen_1_f = part_1.format(2)
chalkboard_1_f = part_1.format(3)
wide_1_f = part_1.format(4)

part_2 = 'MIT-Missing-Semester-lec-mit-0000-2020jan23-1313-Adhoc Section_{}.mp4'
audio_2 = part_2.format(1)
screen_2_f = part_2.format(2)
wide_2_f = part_2.format(4)

wide_1 = Fullscreen(wide_1_f)
chalkboard_1 = Fullscreen(chalkboard_1_f)
screen_1 = Overlay(screen_1_f, wide_1_f, crop_x=1243, crop_y=424, crop_width=470, opacity=0.85)

wide_2 = Fullscreen(wide_2_f)
screen_2 = Overlay(screen_2_f, wide_2_f, crop_x=1256, crop_y=443, crop_width=431, opacity=0.85)

audio_volume = 10.0
audio_offset = -0.06

Sequence([
  Playlist([
    Clip(wide_1, start='0:38', end='5:25'),
    Clip(screen_1, end='05:50'),
    Clip(wide_1, end='08:55'),
    Clip(chalkboard_1, end='25:40'),
    Clip(wide_1, end='27:05'),
    Clip(screen_1, end='28:30'),
    Clip(wide_1, end='28:55'),
    Clip(screen_1, end='31:05'),
    Clip(wide_1, end='31:38'),
    Clip(screen_1, end='33:30'),
    Clip(wide_1, end='35:30'),
    Clip(screen_1, end='37:00'),
    Clip(wide_1, end='37:12'),
    Clip(screen_1, end='45:10'),
    Clip(wide_1, end='46:39'),
    Clip(screen_1, end='47:05'),
    Clip(wide_1, end='47:44'),
  ], audio_1, audio_volume, audio_offset),
  Playlist([
    Clip(screen_2, start='0:27', end='38:20')
  ], audio_2, audio_volume, audio_offset),
]).render('lec6.mp4')
