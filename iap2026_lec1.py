import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

audio = Audio("Missing-Semester-of-your-CS-Education-on-1_12_2026-(Mon)-Tracking-2026jan12.mp4", delay=0.10)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_12_2026-(Mon)-Tracking-2026jan12.mp4")
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_12_2026-(Mon)-PC2-2026jan12.mp4", delay=13 / 60)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_12_2026-(Mon)-Wideshot-2026jan12.mp4", delay=-36 / 60)
right_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_12_2026-(Mon)-RightChalk-2026jan12.mp4", delay=27 / 60
)

# screen_tracking = Overlay(screen_only, tracking, crop_x=470, crop_y=250, crop_width=950, opacity=0.85)
screen_lectern = Overlay(screen_only, wide, crop_x=1192, crop_y=459, crop_width=473, opacity=0.85)
screen_wide = Overlay(screen_only, wide, crop_x=0, crop_y=0, crop_width=1920, opacity=0.85)

Multitrack(
    [
        Clip(wide, start="06:23"),
        Clip(screen_wide, start="06:30"),
        Clip(wide, start="06:43"),
        Clip(tracking, start="12:32"),
        Clip(screen_lectern, start="20:28"),
        Clip(wide, start="1:20:30", end="1:21:06"),
    ],
    audio,
).render("lec1.mp4", title="Missing Semester IAP 2026: Lecture 1")
