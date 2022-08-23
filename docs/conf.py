# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

import ckb_commander

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

project = "ckb_commander"
copyright = "2022, Josef Friedrich"
author = "Josef Friedrich"

version = ckb_commander.__version__
release = ckb_commander.__version__
language = "en"

exclude_patterns = ["_build"]

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": True,
    # "private-members": True,
    # "special-members": True,
    "inherited-members": True,
    "show-inheritance": True,
    "ignore-module-all": True,
    # "imported-members": False,
    "exclude-members": True,
    "class-doc-from": True,
    "no-value": True,
}
