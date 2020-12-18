# Missing Semester: Lecture Videos [![Build Status](https://github.com/missing-semester/videos/workflows/CI/badge.svg)](https://github.com/missing-semester/videos/actions?query=workflow%3ACI)

This repository contains scripts for producing lecture videos for [Missing
Semester](https://missing.csail.mit.edu).

## Dependencies

```bash
pip install ffmpeg-python
```

## Usage

Run `python lec{n}.py` to produce a lecture video. The DSL defined in `lib.py`
is pretty simple; look at any of the processing scripts for any lecture video,
and it should be clear how to make new ones.

To type-check the code, run:

```bash
mypy .
```

## License

Copyright (c) 2020 Anish Athalye, Jose Javier, and Jon Gjengset. Released under
the MIT License. See [LICENSE.md](LICENSE.md) for details.
