import os
import sys

from lib import Audio, Clip, Crop, Fullscreen, Multitrack, Overlay

os.chdir(sys.argv[1])

# TODO replace with better audio
audio = Audio(
    "Missing-Semester-of-your-CS-Education-on-1_21_2026-(Wed)-Tracking-2026jan21.mp4", delay=0.09, loudnorm=False
)
wide = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_21_2026-(Wed)-Wideshot-2026jan21.mp4", delay=-16 / 30)
screen_only = Fullscreen("Missing-Semester-of-your-CS-Education-on-1_21_2026-(Wed)-PC2-2026jan21.mp4", delay=0)
left_chalkboard = Fullscreen(
    "Missing-Semester-of-your-CS-Education-on-1_21_2026-(Wed)-LeftChalk-2026jan21.mp4", delay=-18 / 30
)

screen_lectern = Overlay(screen_only, wide, crop_x=1200, crop_y=450, crop_width=450, opacity=0.85)
wide_crop = Crop(wide, x=200, y=50, width=1400)

Multitrack(
    [
        Clip(wide_crop, start="07:21"),  # intro
        Clip(screen_lectern, start="08:23"),  # using computer
        Clip(wide_crop, start="17:28"),  # questions
        Clip(left_chalkboard, start="19:50"),  # using chalkboard
        Clip(wide_crop, start="28:32"),  # questions
        Clip(screen_lectern, start="31:17"),  # using computer
        Clip(wide_crop, start="47:33"),  # questions, walking over to chalkboard
        Clip(left_chalkboard, start="49:40"),  # using chalkboard
        Clip(wide_crop, start="50:50"),  # walking back to computer
        Clip(screen_lectern, start="51:26"),  # using computer
        Clip(wide_crop, start="52:40"),  # walking over to chalkboard
        Clip(left_chalkboard, start="52:45"),  # using chalkboard
        Clip(wide_crop, start="56:15"),  # walking back to computer
        Clip(screen_lectern, start="56:21"),  # using computer
        Clip(wide_crop, start="57:11"),  # walking over to chalkboard, briefly using chalkboard
        Clip(screen_lectern, start="58:10"),  # using computer
        Clip(wide_crop, start="59:56"),  # walking over to chalkboard, briefly using chalkboard
        Clip(screen_lectern, start="1:00:30"),  # using computer
        Clip(wide_crop, start="1:00:40"),  # walking over to chalkboard, briefly using chalkboard
        Clip(screen_lectern, start="1:03:30"),  # using computer
        Clip(wide_crop, start="1:04:15", end="1:07:55"),  # talking, questions
    ],
    audio,
).render("lec7.mp4", title="Missing Semester IAP 2026: Lecture 7")
