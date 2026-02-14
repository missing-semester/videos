import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

audio = Audio("Missing-Semester-of-your-CS-Education-on-1_20_2026-(Tue)-Tracking-2026jan20.mp4", delay=0.12)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_20_2026-(Tue)-Tracking-2026jan20.mp4")
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_20_2026-(Tue)-PC2-2026jan20.mp4", delay=-3 / 60)

screen_lectern = Overlay(screen_only, tracking, crop_x=680, crop_y=260, crop_width=600, crop_height=440, opacity=0.85)

Multitrack(
    [
        Clip(tracking, start="8:06"),
        Clip(screen_lectern, start="10:07", end="1:11:40"),
    ],
    audio,
).render("lec6.mp4", title="Missing Semester IAP 2026: Lecture 6")
