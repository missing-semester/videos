import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# denoised in the same way as lecture 2
audio = Audio("denoised.wav", delay=0.10)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_15_2026-(Thu)-Tracking-2026jan15.mp4")
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_15_2026-(Thu)-Wideshot-2026jan15.mp4", delay=-9 / 60)
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_15_2026-(Thu)-PC2-2026jan15.mp4", delay=4 / 60)

screen_lectern = Overlay(screen_only, wide, crop_x=1100, crop_y=460, crop_width=450, opacity=0.85)

Multitrack(
    [
        Clip(wide, start="2:43"),
        Clip(screen_lectern, start="14:10"),
        Clip(wide, start="22:35"),
        Clip(screen_lectern, start="23:05"),
        Clip(wide, start="1:09:04", end="1:15:52"),
    ],
    audio,
).render("lec4.mp4", title="Missing Semester IAP 2026: Lecture 4")
