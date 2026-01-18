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
        Clip(wide, start="05:34"),
        Clip(screen_lectern, start="06:20"),
        Clip(wide, start="07:16"),
        Clip(screen_lectern, start="08:21"),
        Clip(wide, start="08:30"),
        Clip(screen_lectern, start="12:16"),
        Clip(wide, start="13:30"),
        Clip(left_chalkboard, start="13:57"),
        Clip(wide, start="15:47"),
        Clip(screen_lectern, start="16:05"),
        Clip(wide, start="19:02"),
        Clip(left_chalkboard, start="19:33"),
        Clip(wide, start="20:12"),
        Clip(screen_lectern, start="20:40"),
        Clip(tracking, start="27:00"),  # camera is still this whole time
        Clip(screen_lectern, start="29:48"),
        Clip(wide, start="34:15"),
        Clip(left_chalkboard, start="35:22"),
        Clip(wide, start="35:52"),
        Clip(screen_lectern, start="36:30"),
        Clip(wide, start="39:25"),
        Clip(screen_lectern, start="41:20"),
        Clip(wide, start="51:05", end="59:22"),
    ],
    audio,
).render("lec3.mp4", title="Missing Semester IAP 2026: Lecture 3")

"""
Title: Lecture 3: Development Environment and Tools

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/development-environment/

0:00 - Introduction
3:51 - Text editing and Vim
8:05 - Modal editing
12:42 - Basics: inserting text
13:28 - Vim's interface is a programming language
24:13 - Putting it all together
28:56 - Code intelligence and language servers
33:54 - AI-powered development
35:25 - Autocomplete
42:25 - Inline chat
45:32 - Student questions
"""
