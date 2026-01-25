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

"""
Title: Lecture 4: Debugging and Profiling

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/debugging-profiling/

0:00:00 - Introduction
0:00:11 - Debugging
0:11:25 - Record-Replay Debugging
0:24:36 - System Call Tracing
0:35:15 - bpftrace and eBPF
0:43:45 - Network Debugging
0:46:49 - Sanitizers
0:50:56 - Valgrind: When You Can't Recompile
0:52:35 - AI for Debugging
0:54:42 - Profiling
0:55:05 - Timing
0:58:33 - Resource Monitoring
1:01:24 - Visualizing Performance Data
1:12:40 - Conclusion
"""
