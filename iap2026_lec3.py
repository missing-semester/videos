import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# denoised in the same way as lecture 2
audio = Audio("denoised.wav", delay=0.10)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_14_2026-(Wed)-Tracking-2026jan14.mp4")
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_14_2026-(Wed)-PC2-2026jan14.mp4", delay=62 / 60)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_14_2026-(Wed)-Wideshot-2026jan14.mp4", delay=46 / 60)
left_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_14_2026-(Wed)-LeftChalk-2026jan14.mp4", delay=28 / 60
)

screen_lectern = Overlay(screen_only, wide, crop_x=1192, crop_y=459, crop_width=473, opacity=0.85)

Multitrack(
    [
        Clip(tracking, start="05:34"),
        Clip(screen_lectern, start="06:20"),
        Clip(tracking, start="07:16"),
        Clip(screen_lectern, start="08:21"),
        Clip(tracking, start="08:30"),
        Clip(screen_lectern, start="12:16"),
        Clip(wide, start="13:30"),
        Clip(left_chalkboard, start="13:57"),
        Clip(wide, start="15:47"),
        Clip(screen_lectern, start="16:05"),
        Clip(wide, start="19:02"),
        Clip(left_chalkboard, start="19:33"),
        Clip(wide, start="20:12"),
        Clip(screen_lectern, start="20:40"),
        Clip(tracking, start="27:00"),
        Clip(screen_lectern, start="29:48"),
        Clip(tracking, start="34:15"),
        Clip(screen_lectern, start="36:30"),
        Clip(tracking, start="39:25"),
        Clip(screen_lectern, start="41:20"),
        Clip(wide, start="51:05"),
        Clip(tracking, start="51:30", end="59:22"),
    ],
    audio,
).render("lec3.mp4", title="Missing Semester IAP 2026: Lecture 3")
