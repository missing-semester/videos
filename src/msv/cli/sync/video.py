import argparse

from msv.lib import Audio, Clip, Framerate, Fullscreen, Multitrack, Stream, Tile


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=str, required=True)
    parser.add_argument("--end", type=str, required=True)
    parser.add_argument("--video-1", type=str, required=True)
    parser.add_argument("--delay-1", type=float, default=0)
    parser.add_argument("--fps-1", type=float, default=None)
    parser.add_argument("--video-2", type=str, required=True)
    parser.add_argument("--delay-2", type=float, default=0)
    parser.add_argument("--fps-2", type=float, default=None)
    parser.add_argument("--video-3", type=str, required=True)
    parser.add_argument("--delay-3", type=float, default=0)
    parser.add_argument("--fps-3", type=float, default=None)
    parser.add_argument("--video-4", type=str, required=True)
    parser.add_argument("--delay-4", type=float, default=0)
    parser.add_argument("--fps-4", type=float, default=None)
    parser.add_argument("--audio", type=str)
    parser.add_argument("--delay-audio", type=float, default=0)
    parser.add_argument("--out", type=str, required=True)
    args = parser.parse_args()
    if args.audio is None:
        args.audio = args.video_1

    video_1: Stream = Fullscreen(args.video_1, delay=args.delay_1)
    if args.fps_1 is not None:
        video_1 = Framerate(video_1, args.fps_1)

    video_2: Stream = Fullscreen(args.video_2, delay=args.delay_2)
    if args.fps_2 is not None:
        video_2 = Framerate(video_2, args.fps_2)

    video_3: Stream = Fullscreen(args.video_3, delay=args.delay_3)
    if args.fps_3 is not None:
        video_3 = Framerate(video_3, args.fps_3)

    video_4: Stream = Fullscreen(args.video_4, delay=args.delay_4)
    if args.fps_4 is not None:
        video_4 = Framerate(video_4, args.fps_4)

    audio = Audio(args.audio, delay=args.delay_audio)
    Multitrack([Clip(Tile(video_1, video_2, video_3, video_4), start=args.start, end=args.end)], audio).render(args.out)


if __name__ == "__main__":
    main()
