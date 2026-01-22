# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Deep Learning Course'
copyright = '2023, Eugenio Culurciello'
author = 'Eugenio Culurciello'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_show_sphinx = False
# html_show_copyright = False
# html_last_updated_fmt = ''
# html_theme = 'alabaster'
# html_theme = 'piccolo_theme'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# def setup(app):
#     app.add_css_file('custom.css')


# html_theme_options = {
# #    'analytics_id': 'UA-65442910-1',  #  Provided by Google in your dashboard
#     'display_version': False,
#     'logo_only': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'style_nav_header_background': '#F0F0F0',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
# }