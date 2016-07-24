# -*- coding: utf-8 -*-
project = u'pyscaffolding'
copyright = u'2016, Bob Baxley'
author = u'Bob Baxley'

version = u'0.1'
release = u'0.1'

from recommonmark.parser import CommonMarkParser

extensions = [
    'sphinx.ext.autodoc',
    'nbsphinx',
    'sphinx.ext.mathjax'
]
nbsphinx_allow_errors = True
templates_path = ['_templates']
source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
master_doc = 'index'
language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints']

pygments_style = 'sphinx'

html_theme = "sphinx_rtd_theme"
html_logo = 'scaff.png'

html_favicon = 'favicon.ico'

html_static_path = ['_static']

