#!/usr/bin/env python3
"""news-image-20261118 entry: write the 18 Nov 2026 world-news summary
image to /output/entry.png.

Deterministic, stdlib only, no network: copies the bundled entry.png.
Running it twice writes the same bytes both times.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
