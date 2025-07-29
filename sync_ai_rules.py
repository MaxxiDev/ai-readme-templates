#!/usr/bin/env python3
"""
sync_ai_rules.py
-----------------

This script walks through a directory tree (by default, ``/Users/maxxi/Documents/www``)
and applies a set of Cursor AI rules to every Laravel project it finds.

A Laravel project is detected by the presence of an ``artisan`` file in its
project root. For each such project, the script ensures that a ``.cursor``
directory exists and copies a unified rules template (``laravel_rule.md``)
into ``<project>/.cursor/rules``.  The template is expected to live in
``/Users/maxxi/Documents/AI_README_FOLDER/laravel_rule.md`` by default.

The script prints a success message for each project it updates.

Usage:
    python sync_ai_rules.py [www_root [template_file]]

Positional arguments:
    www_root:       Root directory containing your projects. Defaults to
                    ``/Users/maxxi/Documents/www``.
    template_file:  Path to the unified Laravel rules template. Defaults to
                    ``/Users/maxxi/Documents/AI_README_FOLDER/laravel_rule.md``.

Example:
    python sync_ai_rules.py

"""
import os
import shutil
import sys
from pathlib import Path


def apply_rules_to_projects(project_paths: list[Path], template_file: Path) -> None:
    """Apply the unified rules template to each project in ``project_paths``.

    For each project path provided, ensure a ``.cursor`` directory exists and
    copy ``template_file`` into ``.cursor/rules``. If the project path does
    not exist or the copy fails, an exception is raised.

    Parameters
    ----------
    project_paths : list[Path]
        A list of project root directories (already identified as Laravel projects).
    template_file : Path
        The file containing the unified Laravel rules to be copied.
    """
    if not template_file.is_file():
        raise FileNotFoundError(f"Template file not found: {template_file}")

    for project_path in project_paths:
        cursor_dir = project_path / '.cursor'
        cursor_dir.mkdir(exist_ok=True)
        dest_rules_file = cursor_dir / 'rules'
        shutil.copyfile(template_file, dest_rules_file)
        print(f"✅ Laravel rules applied to: {project_path}")


def detect_laravel_projects(www_root: Path) -> list[Path]:
    """Traverse ``www_root`` and return a list of Laravel project paths.

    A Laravel project is detected by the presence of an ``artisan`` file. Only
    top-level project directories are returned; subdirectories beneath a
    detected project are not scanned further.

    Parameters
    ----------
    www_root : Path
        The directory containing multiple projects. Each subdirectory
        is considered a potential project root.

    Returns
    -------
    list[Path]
        A list of paths to detected Laravel projects.
    """
    projects: list[Path] = []
    for root, dirs, files in os.walk(www_root):
        root_path = Path(root)
        if 'artisan' in files:
            projects.append(root_path)
            # Skip walking into subdirectories of this project
            dirs.clear()
    return projects


def main() -> None:
    """Entry point for running the script from the command line.

    Usage::

        python sync_ai_rules.py [www_root] [template_file] [project_list_json]

    The first argument, if provided, is interpreted as the root directory to scan
    for Laravel projects.  The second argument, if provided, is the path to the
    unified rules template file.  The third optional argument is a JSON file
    containing a list of project paths; if provided, scanning is skipped and
    projects are loaded from this file instead.
    """
    default_www_root = Path('/Users/maxxi/Documents/www')
    default_template_file = Path('/Users/maxxi/Documents/AI_README_FOLDER/laravel_rule.md')

    # Parse command-line arguments
    args = sys.argv[1:]
    www_root = Path(args[0]) if len(args) > 0 else default_www_root
    template_file = Path(args[1]) if len(args) > 1 else default_template_file
    project_list_json = Path(args[2]) if len(args) > 2 else None

    # Determine list of projects
    if project_list_json:
        # Load project paths from JSON
        import json
        with project_list_json.open('r', encoding='utf-8') as f:
            raw_list = json.load(f)
        project_paths = [Path(p) for p in raw_list]
    else:
        # Detect projects by scanning
        project_paths = detect_laravel_projects(www_root)

    apply_rules_to_projects(project_paths, template_file)


if __name__ == '__main__':
    main()