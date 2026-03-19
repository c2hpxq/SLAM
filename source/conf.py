# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SLAM-Notes'
copyright = '2026, c2hpxq'
author = 'c2hpxq'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh'

# Allow MathJax to render formulas written as $...$ and $$...$$ in rst text.
mathjax3_config = {
    'tex': {
        'inlineMath': [['\\(', '\\)'], ['$', '$']],
        'displayMath': [['\\[', '\\]'], ['$$', '$$']],
    }
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Always load MathJax on HTML pages so formulas written as $...$/$$...$$
# inside rst plain text can still be rendered by the browser.
html_js_files = [
    'mathjax-config.js',
    'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
]
