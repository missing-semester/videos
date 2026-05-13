import argparse
import importlib.util
import os
import runpy


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Missing Semester lecture video")
    parser.add_argument("year", type=int, help="Lecture year (e.g. 2020, 2026)")
    parser.add_argument("number", type=int, help="Lecture number")
    parser.add_argument("directory", help="Directory containing the source video files")
    args = parser.parse_args()

    module = f"msv.lectures.iap{args.year}.lec{args.number}"
    try:
        found = importlib.util.find_spec(module) is not None
    except ModuleNotFoundError:
        found = False
    if not found:
        parser.error(f"no such lecture: iap{args.year} lec{args.number}")

    try:
        os.chdir(args.directory)
    except OSError as e:
        parser.error(f"cannot access directory {args.directory!r}: {e.strerror}")
    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    main()
