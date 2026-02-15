import os
import sys

from lib import Audio, Clip, Framerate, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# noise reduction using Audacity,
# noise source is lecture 6, approx 8:03.70 -- 8:04.85; this only has background static
# noise reduction applied with settings: reduction 30 dB, sensitivity 6.00, frequency smoothing 2 bands
audio = Audio("denoised.wav", delay=0.12)
tracking = Framerate(Fullscreen("Missing-Semester-of-your-CS-Education-on-1_20_2026-(Tue)-Tracking-2026jan20.mp4"), 30)
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_20_2026-(Tue)-PC2-2026jan20.mp4", delay=-3 / 60)

screen_lectern = Overlay(screen_only, tracking, crop_x=680, crop_y=260, crop_width=600, crop_height=440, opacity=0.85)

Multitrack(
    [
        Clip(tracking, start="8:06"),
        Clip(screen_lectern, start="10:07", end="1:11:40"),
    ],
    audio,
).render("lec6.mp4", title="Missing Semester IAP 2026: Lecture 6")

"""
Title: Lecture 6: Packaging and Shipping Code

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/shipping-code/

0:00:00 - Introduction
0:02:00 - Dependencies & Environments
0:12:55 - Artifacts & Packaging
0:21:27 - Releases & Versioning
0:25:10 - Reproducibility
0:30:53 - VMs & Containers
0:45:37 - Services & Orchestration
0:54:38 - Publishing
1:00:20 - Conclusion
"""
