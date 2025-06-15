# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

from datetime import datetime

from semaver import Version
import sphinx_nefertiti

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


# -- Project information -----------------------------------------------------

project = 'pyserv'
author = 'Stephen Arnold'
copyright = '2022 - ' + str(datetime.now().year) + f' {author}'

# -- General configuration ------------------------------------------------

_ver_list = version('pyserv').split(".")

# The X.Y number.
version = ".".join(_ver_list[:2])
# The X.Y.Z number.
release = ".".join(_ver_list[:3])

_ver_last = Version(release) - Version('0.0.1')

# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_git',
    'sphinxcontrib.apidoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_nefertiti',
    'sphinxcontrib.mermaid',
]

myst_enable_extensions = [
    'amsmath',
    'attrs_block',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'tasklist',
    'substitution',
]

myst_suppress_warnings = ["myst.header"]
myst_fence_as_directive = ["mermaid"]

# sphinxcontrib.apidoc
apidoc_module_dir = f'../../src/{project}'
apidoc_output_dir = 'api'
apidoc_excluded_paths = ['scripts', 'tests']
apidoc_include_private = True
apidoc_separate_modules = True

autodoc_typehints = 'description'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# Brief project description
#
description = 'A collection of simple servers for HTTP, WSGI, and TFTP'

# test nefertiti settings
language = "en"
today_fmt = '%A %d. %B %Y, %H:%M'

html_theme = "sphinx_nefertiti"

html_theme_options = {
    "monospace_font_size": ".90rem",

    "style": "blue",
    "style_header_neutral": True,
    "pygments_light_style": "pastie",
    "pygments_dark_style": "dracula",

    "repository_url": f"https://github.com/sarnold/{project}",
    "repository_name": f"{project}",

    "current_version": "latest",
    "versions": [
        (f"v{release}", f"https://sarnold.github.io/{project}/"),
        (f"v{_ver_last}", f"https://sarnold.github.io/{project}/"),
    ],

    "show_colorset_choices": True,
    # Return user's to 'blue' after a day since color was picked.
    "reset_colorset_choice_after_ms": 1000 * 60 * 60 * 24,
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = f'{project}doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     [author], 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, f'{project}', f'{project} Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, f'{project}', f'{project} Documentation',
     [author], f'{project}', description,
     'Miscellaneous'),
]

