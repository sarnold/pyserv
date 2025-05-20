#!/usr/bin/env python

"""
Get the path to markdown files and process image URLs based on files in
args. One or more (SVG or PNG) files are required.
"""
import os
import sys
from pathlib import Path
from string import Template
from typing import List, Tuple

DEBUG = int(os.getenv('DEBUG', default='0'))
EXTENSIONS = ['.svg', '.png']

FIG_TPL = """```{figure} ${figure_path}
:width: 90 %
:align: center
:alt: ${caption_lc}

${caption_title} (captured from mermaid to SVG or PNG).
```
"""

CTX = {
    'caption_lc': '',
    'caption_title': '',
    'figure_path': '',
}


def render_caption(caption: str, path: str):
    """
    Render a string template.
    """
    CTX.update(
        {
            'caption_lc': caption.lower(),
            'caption_title': caption.title(),
            'figure_path': path,
        }
    )
    return Template(FIG_TPL).substitute(CTX)


def find_mdfiles(
    start: str = '.', fglob: str = '*.md', excludes: Tuple = ('.github', '.tox', '.venv')
) -> List:
    """
    Find markdown files subject to specified exclude paths.

    :param start: directory to start file search
    :param fglob: file extension glob
    :param excludes: tuple of excludes
    """
    target_files: List = []
    files = Path(start).rglob(fglob)
    for file in list(files):
        if str(file).startswith(excludes):
            continue
        target_files.append(file)
    if DEBUG:
        print(f'Found file list: {target_files}')
    return target_files


def process_files(new_files: List, target_files: List):
    """
    process files if we found enough of each.
    """
    for img_file in new_files:
        for md_file in target_files:
            doc_str = Path(md_file).read_text(encoding='utf-8')
            if Path(img_file).name not in doc_str:
                continue
            with Path(md_file).open(encoding='utf-8') as file:
                lines = file.readlines()
            with Path(md_file).open(mode='w', encoding='utf-8') as file:
                for line in lines:
                    if line.startswith(('![', '[')) and Path(img_file).name in line:
                        if DEBUG:
                            print(line)
                        cap_str = line.split('[', 1)[1].split(']')[0]
                        path_str = line.split('(', 1)[1].split(')')[0]
                        text = render_caption(cap_str, path_str)
                        file.write(text + '\n')
                    else:
                        file.write(line)


def main(argv: list[str] | None = None) -> None:
    """
    Runs the program.

    Args:
        argv: A list of arguments, not including the prog name.
    """
    if not argv:
        if DEBUG:
            print("No image files, nothing to do ...")
        sys.exit(0)

    if DEBUG:
        print(argv)
    new_files = [f for f in argv if Path(f).suffix in EXTENSIONS and Path(f).exists()]
    if len(new_files) < 1:
        if DEBUG:
            print(f"No valid input files (only {EXTENSIONS} are allowed)")
        sys.exit(1)
    if DEBUG:
        print(new_files)

    target_files = find_mdfiles()
    if not target_files:
        if DEBUG:
            print("No markdown files, nothing to do ...")
        sys.exit(0)

    if DEBUG:
        print(target_files)

    process_files(new_files, target_files)


# print(','.join(target_files))

if __name__ == "__main__":
    main(sys.argv[1:])
