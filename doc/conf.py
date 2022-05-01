""" Document configuration. """
# -*- coding: utf-8 -*-
#
# PyModbus documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 20 12:31:10 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from recommonmark.transform import AutoStructify
from pymodbus import __version__
parent_dir = os.path.abspath(os.pardir)
# examples = os.path.join(parent_dir, "examples")
example_contrib = os.path.join(parent_dir, "examples/contrib")
example_common = os.path.join(parent_dir, "examples/common")
example_gui = os.path.join(parent_dir, "examples/gui")

sys.path.insert(0, os.path.abspath(os.pardir))
sys.path.append(example_common)
sys.path.append(example_contrib)
sys.path.append(example_gui)
# sys.path.extend([examples, example_common, example_contrib, example_gui])
# sys.path.insert(0, os.path.abspath('../'))

github_doc_root = 'https://github.com/riptideio/pymodbus/tree/master/doc/' # pylint: disable=invalid-name
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

#extensions = ['sphinx.ext.autodoc', 'm2r', 'recommonmark']
extensions = ['sphinx.ext.autodoc', 'm2r2']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
#source_parsers = {
#    '.md': CommonMarkParser,
#}

source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index' # pylint: disable=invalid-name

# General information about the project.
project = 'PyModbus' # pylint: disable=invalid-name
copyright = '2017, Sanjay' # pylint: disable=redefined-builtin,invalid-name
author = 'Sanjay' # pylint: disable=invalid-name

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None # pylint: disable=invalid-name

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx' # pylint: disable=invalid-name

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False # pylint: disable=invalid-name


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # pylint: disable=invalid-name

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyModbusdoc' # pylint: disable=invalid-name


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
latex_documents = [ #NOSONAR
    (master_doc, 'PyModbus.tex', 'PyModbus Documentation', #NOSONAR
     'Sanjay', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pymodbus', 'PyModbus Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PyModbus', 'PyModbus Documentation',
     author, 'PyModbus', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    """ Setup. """
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
