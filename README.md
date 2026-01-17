# Missing Semester: Lecture Videos [![Build Status](https://github.com/missing-semester/videos/actions/workflows/ci.yml/badge.svg)](https://github.com/missing-semester/videos/actions/workflows/ci.yml)

This repository contains scripts for producing lecture videos for [Missing
Semester](https://missing.csail.mit.edu).

## Dependencies

These scripts rely on [uv](https://docs.astral.sh/uv/).

## Usage

Run `uv run python {term}_lec{n}.py` to produce a lecture video. The DSL
defined in `lib.py` is pretty simple; look at any of the processing scripts for
any lecture video, and it should be clear how to make new ones.

## Development

To type-check the code, run:

```bash
uv run mypy .
```

To run the linter, run:

```bash
uv run ruff check --fix
```

To run the formatter, run:

```bash
uv run ruff format
```

## License

Copyright (c) Anish Athalye, Jose Javier, and Jon Gjengset. Released under the
MIT License. See [LICENSE.md](LICENSE.md) for details.
