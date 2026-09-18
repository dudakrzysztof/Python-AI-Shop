#!/usr/bin/env python3
"""Run the root Django management entrypoint from any working directory."""

from __future__ import annotations

import os
from pathlib import Path
import runpy
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """Execute ``manage.py`` with the repository root as the working directory."""
    os.chdir(PROJECT_ROOT)
    manage_file = PROJECT_ROOT / "manage.py"
    sys.argv = [str(manage_file), *sys.argv[1:]]
    runpy.run_path(str(manage_file), run_name="__main__")


if __name__ == "__main__":
    main()
