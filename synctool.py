from lib import *
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--start', type=str, required=True)
  parser.add_argument('--end', type=str, required=True)
  parser.add_argument('--video-1', type=str, required=True)
  parser.add_argument('--delay-1', type=float, default=0)
  parser.add_argument('--video-2', type=str, required=True)
  parser.add_argument('--delay-2', type=float, default=0)
  parser.add_argument('--video-3', type=str, required=True)
  parser.add_argument('--delay-3', type=float, default=0)
  parser.add_argument('--video-4', type=str, required=True)
  parser.add_argument('--delay-4', type=float, default=0)
  parser.add_argument('--audio', type=str)
  parser.add_argument('--delay-audio', type=float, default=0)
  parser.add_argument('--volume', type=float, default=1)
  parser.add_argument('--out', type=str, required=True)
  args = parser.parse_args()
  if args.audio is None:
    args.audio = args.video_1

  video_1 = Fullscreen(args.video_1, delay=args.delay_1)
  video_2 = Fullscreen(args.video_2, delay=args.delay_2)
  video_3 = Fullscreen(args.video_3, delay=args.delay_3)
  video_4 = Fullscreen(args.video_4, delay=args.delay_4)
  audio = Audio(args.audio, volume=args.volume, delay=args.delay_audio)
  Multitrack([Clip(Tile(video_1, video_2, video_3, video_4), start=args.start, end=args.end)], audio).render(args.out)

if __name__ == '__main__':
  main()
