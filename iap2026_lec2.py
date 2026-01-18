import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

audio = Audio("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-Tracking-2026jan13.mp4", delay=0.08)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-Tracking-2026jan13.mp4")
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-PC2-2026jan13.mp4", delay=5 / 60)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-Wideshot-2026jan13.mp4", delay=-17 / 60)
right_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-RightChalk-2026jan13.mp4", delay=-41 / 60
)
screen_tracking = Overlay(screen_only, tracking, crop_y=200, crop_x=(1920 - 1000) // 2, crop_width=1000, opacity=0.85)

Multitrack(
    [
        Clip(tracking, start="06:17"),
        Clip(screen_tracking, start="07:33"),
        Clip(tracking, start="1:12:17", end="1:12:36"),
    ],
    audio,
).render("lec2.mp4", title="Missing Semester IAP 2026: Lecture 2")

"""
Title: Lecture 2: Command-line Environment

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/command-line-environment/

0:00 - Introduction
1:17 - The Command Line Interface
2:37 - Arguments
10:26 - Streams
16:19 - Environment variables
21:08 - Return codes
26:04 - Signals
31:59 - Remote Machines
37:30 - Terminal Multiplexers
41:24 - Customizing the Shell
1:00:28 - AI in the Shell
1:04:56 - Terminal Emulators
"""
