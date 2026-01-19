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
        Clip(screen_lectern, start="13:37"),
        Clip(wide, start="1:20:30", end="1:21:06"),
    ],
    audio,
).render("lec1.mp4", title="Missing Semester IAP 2026: Lecture 1")

"""
Title: Lecture 1: Course Overview + Introduction to the Shell

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/course-shell/

0:00:00 - Introduction
0:01:20 - Motivation
0:03:50 - Class structure and logistics
0:07:06 - What is the shell?
0:11:59 - Why should you care about it?
0:14:04 - Navigating in the shell
0:28:02 - What is available in the shell?
0:58:50 - The shell language (bash)
1:14:05 - Conclusion
"""
