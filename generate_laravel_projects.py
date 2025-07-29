#!/usr/bin/env python3
"""
generate_laravel_projects.py
---------------------------

This script scans a directory tree and writes out a JSON file listing all
detected Laravel project paths.  A Laravel project is identified by the
presence of an ``artisan`` file in the project root.

Usage:
    python generate_laravel_projects.py [www_root] [output_json]

Positional arguments:
    www_root:      Root directory containing your projects. Defaults to
                   ``/Users/maxxi/Documents/www``.
    output_json:   Path to write the JSON file. Defaults to
                   ``laravel_projects.json`` in the current working directory.

The resulting JSON file will contain a simple array of absolute path strings.

Example::

    python generate_laravel_projects.py
    # outputs `laravel_projects.json` in the current directory

    python generate_laravel_projects.py /path/to/www /tmp/my_projects.json

To use this list with ``sync_ai_rules.py``, run::

    python sync_ai_rules.py /Users/maxxi/Documents/www /path/to/laravel_rule.md /path/to/laravel_projects.json

"""
import os
import json
import sys
from pathlib import Path


def detect_laravel_projects(www_root: Path) -> list[str]:
    """Return a list of Laravel project paths under ``www_root``.

    Parameters
    ----------
    www_root : Path
        The directory containing multiple project folders.

    Returns
    -------
    list[str]
        A list of string paths (absolute) pointing to directories that
        contain an ``artisan`` file in their root.
    """
    projects: list[str] = []
    for root, dirs, files in os.walk(www_root):
        if 'artisan' in files:
            projects.append(str(Path(root).resolve()))
            dirs.clear()  # Prevent descending into this project's subdirectories
    return projects


def main() -> None:
    default_www_root = Path('/Users/maxxi/Documents/www')
    default_output = Path('laravel_projects.json')

    args = sys.argv[1:]
    www_root = Path(args[0]) if len(args) > 0 else default_www_root
    output_json = Path(args[1]) if len(args) > 1 else default_output

    projects = detect_laravel_projects(www_root)
    with output_json.open('w', encoding='utf-8') as f:
        json.dump(projects, f, indent=2)
    print(f"Detected {len(projects)} Laravel projects and saved to {output_json}")


if __name__ == '__main__':
    main()