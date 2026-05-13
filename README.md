# Missing Semester: Lecture Videos [![Build Status](https://github.com/missing-semester/videos/actions/workflows/ci.yml/badge.svg)](https://github.com/missing-semester/videos/actions/workflows/ci.yml)

This repository contains the `msv` package: a small DSL over [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) for producing lecture videos for [Missing Semester](https://missing.csail.mit.edu), along with the per-lecture rendering scripts.

## Installation

The package uses [uv](https://docs.astral.sh/uv/).

For local development, `uv sync` in a clone of this repo will set up the environment.

If you want to use the DSL from outside the package, you can install it directly from GitHub (this package is not published to PyPI):

```bash
uv add git+https://github.com/missing-semester/videos
```

## Library

The DSL lives in `msv.lib`. A minimal example:

```python
from msv.lib import Audio, Clip, Fullscreen, Multitrack

video = Fullscreen("raw.mp4")
audio = Audio("raw.mp4")
Multitrack([Clip(video, start="00:30", end="01:00")], audio).render("out.mp4")
```

See `src/msv/lectures/` for many more examples.

## Console scripts

Installing the package provides the following commands:

- `msv-sync-audio`: Useful for syncing an audio and a video track.
- `msv-sync-video`:  2x2 tile of synced video streams. Useful for finding audio/video offsets across multi-camera recordings.
- `msv-normalize-sbv`: split long lines in `.sbv` caption files to YouTube-ish widths.
- `msv-render-lecture [year] [number] [directory]`: render a specific Missing Semester lecture, e.g. `msv-render-lecture 2026 1 /path/to/raw/footage`.

You can also run these without installing the package with `uv run [command name]`.

## Development

```bash
uv run mypy .          # type-check
uv run ruff check      # lint
uv run ruff format     # format
```

## License

Copyright (c) Anish Athalye, Jose Javier, and Jon Gjengset. Released under the MIT License. See [LICENSE.md](LICENSE.md) for details.
