import os
import sys

from lib import Audio, Clip, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# noise reduction using Audacity,
# noise source is lecture 3 (cleanest sample), approx 51:57.25--51:59.75
# noise reduction applied with settings: reduction 30 dB, sensitivity 6.00, frequency smoothing 2 bands
audio = Audio("denoised.wav", delay=0.08)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-Tracking-2026jan13.mp4")
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-PC2-2026jan13.mp4", delay=5 / 60)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-Wideshot-2026jan13.mp4", delay=-17 / 60)
right_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_13_2026-(Tue)-RightChalk-2026jan13.mp4", delay=-41 / 60
)

screen_lectern = Overlay(screen_only, wide, crop_x=1192, crop_y=459, crop_width=473, opacity=0.85)

Multitrack(
    [
        Clip(wide, start="06:17"),
        Clip(screen_lectern, start="07:33"),
        Clip(tracking, start="1:12:17", end="1:12:36"),
    ],
    audio,
).render("lec2.mp4", title="Missing Semester IAP 2026: Lecture 2")

"""
Title: Lecture 2: Command-line Environment

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/command-line-environment/

0:00:00 - Introduction
0:01:17 - The Command Line Interface
0:02:37 - Arguments
0:10:26 - Streams
0:16:19 - Environment variables
0:21:08 - Return codes
0:26:04 - Signals
0:31:59 - Remote Machines
0:37:30 - Terminal Multiplexers
0:41:24 - Customizing the Shell
1:00:28 - AI in the Shell
1:04:56 - Terminal Emulators
"""
