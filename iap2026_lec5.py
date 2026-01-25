import os
import sys

from lib import Audio, Clip, Crop, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

audio = Audio("Missing-Semester-of-your-CS-Education-on-1_16_2026-(Fri)-Tracking-2026jan16.mp4", delay=0.09)
tracking = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_16_2026-(Fri)-Tracking-2026jan16.mp4")
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_16_2026-(Fri)-Wideshot-2026jan16.mp4", delay=4 / 60)
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_16_2026-(Fri)-PC2-2026jan16.mp4", delay=-2 / 60)
left_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_16_2026-(Fri)-LeftChalk-2026jan16.mp4", delay=-36 / 60
)

screen_lectern = Overlay(screen_only, wide, crop_x=1200, crop_y=480, crop_width=450, opacity=0.85)
wide_crop = Crop(wide, x=200, y=50, width=1400)
screen_wide_crop = Overlay(screen_only, wide, crop_x=200, crop_y=50, crop_width=1400, opacity=0.85)

Multitrack(
    [
        Clip(wide_crop, start="5:40"),  # intro
        Clip(screen_wide_crop, start="09:09"),  # xkcd comic
        Clip(wide_crop, start="09:44"),  # back to wide
        Clip(left_chalkboard, start="11:26"),  # Git internals, on chalkboard
        Clip(wide_crop, start="32:10"),  # questions, staging area
        Clip(screen_lectern, start="43:30"),  # start of demos
        Clip(screen_wide_crop, start="49:55"),  # pointing to chalkboard (twice)
        Clip(wide_crop, start="51:56"),  # questions, using chalkboard
        Clip(screen_lectern, start="54:04"),  # back to demos
        Clip(wide_crop, start="58:30"),  # questions, using chalkboard
        Clip(screen_lectern, start="59:14"),  # back to demos
        Clip(wide_crop, start="1:00:01"),  # questions, using chalkboard
        Clip(screen_lectern, start="1:01:38"),  # back to demos
        Clip(screen_wide_crop, start="1:04:47"),  # pointing to chalkboard
        Clip(screen_lectern, start="1:04:58"),  # back to lectern
        Clip(wide_crop, start="1:11:43"),  # questions, using chalkboard
        Clip(screen_lectern, start="1:12:57", end="1:15:12"),  # back to demos
    ],
    audio,
).render("lec5.mp4", title="Missing Semester IAP 2026: Lecture 5")

"""
Title: Lecture 5: Version Control and Git

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/version-control/

0:00:00 - Introduction
0:05:45 - Git's data model
0:06:16 - Snapshots
0:07:54 - Modeling history: relating snapshots
0:12:00 - Data model, as pseudocode
0:15:31 - Objects and content-addressing
0:20:55 - References
0:32:07 - Repositories
0:34:45 - Staging area
0:37:50 - Git command-line interface
0:38:37 - Basics
0:48:24 - Branching and merging
1:00:23 - Remotes
1:06:34 - Conclusion
"""
