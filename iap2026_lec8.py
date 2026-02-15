import os
import sys

from lib import Audio, Clip, Crop, Fullscreen, Multitrack

os.chdir(sys.argv[1])

# noise reduction using Audacity,
# noise source is lecture 8, approx 24:46.75 -- 24:48.00; works better than using lecture 3's noise sample
# noise reduction applied with settings: reduction 30 dB, sensitivity 6.00, frequency smoothing 2 bands
audio = Audio("denoised.wav", delay=0.14)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_22_2026-(Thu)-Wideshot-2026jan22.mp4", delay=30 / 60)

wide_crop = Crop(wide, x=840, y=350, width=800)

Multitrack(
    [
        Clip(wide_crop, start="4:21", end="1:09:58"),
    ],
    audio,
).render("lec8.mp4", title="Missing Semester IAP 2026: Lecture 8")

"""
Title: Lecture 8: Beyond the Code

Description:

You can find the lecture notes and exercises for this lecture at https://missing.csail.mit.edu/2026/beyond-code/

0:00:00 - Introduction
0:01:53 - One-way communication
0:20:49 - Collaboration
0:54:08 - Education
0:58:41 - AI etiquette
1:04:16 - Conclusion
"""
