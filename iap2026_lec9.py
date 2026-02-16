import os
import sys

from lib import Audio, Clip, Crop, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# TODO replace with better audio
audio = Audio(
    "Missing-Semester-of-your-CS-Education-on-1_23_2026-(Fri)-Tracking-2026jan23.mp4", delay=0.09, loudnorm=False
)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_23_2026-(Fri)-Wideshot-2026jan23.mp4", delay=-7 / 30)
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_23_2026-(Fri)-PC2-2026jan23.mp4", delay=-5 / 30)

screen_lectern = Overlay(screen_only, wide, crop_x=1150, crop_y=425, crop_width=450, opacity=0.85)
wide_crop = Crop(wide, x=1920 - 736, y=400, width=736)

Multitrack(
    [
        Clip(screen_lectern, start="06:18"),
        Clip(wide_crop, start="1:12:30", end="1:21:33"),
    ],
    audio,
).render("lec9.mp4", title="Missing Semester IAP 2026: Lecture 9")
