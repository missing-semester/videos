from lib import *
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--start', type=str, required=True)
  parser.add_argument('--end', type=str, required=True)
  parser.add_argument('--video', type=str, required=True)
  parser.add_argument('--delay-video', type=float, default=0)
  parser.add_argument('--audio', type=str)
  parser.add_argument('--delay-audio', type=float, default=0)
  parser.add_argument('--out', type=str, required=True)
  args = parser.parse_args()
  if args.audio is None:
    args.audio = args.video_1

  video = Fullscreen(args.video, delay=args.delay_video)
  audio = Audio(args.audio, delay=args.delay_audio)
  Multitrack([Clip(video, start=args.start, end=args.end)], audio).render(args.out)

if __name__ == '__main__':
  main()
