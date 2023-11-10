# -- Project information -----------------------------------------------------

project = 'Site Title'
copyright = '2023, Your name'
author = 'Your Name'



# ----------------------------------------------------------------------------
#            Below here does not need to be edited for the lab
# ----------------------------------------------------------------------------

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
    'sphinx.ext.intersphinx',
    "sphinx_design",
    "sphinxext.opengraph",
]

# "sphinxext.rediraffe",

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*",
        "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md",
        '_data','_pages','_people','_projects']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

import yaml
with open ('info.yml','r') as f:
    html_context = yaml.safe_load(f)


html_theme_options = {
  "github_url": "https://github.com/username/",
  "twitter_url": "https://twitter.com/username",
  "search_bar_text": "Search this site...",
#   "navbar_end": ["search-field.html"],
}

# html_favicon = "_static/favicon.ico"
#  change this to change the site title
html_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_js_files = [
#     'slides.js',
# ]
# html_extra_path = ["feed.xml"]
# map pages to which sidebar they should have 
#  "page_file_name": ["list.html", "of.html", "sidebar.html", "files.html"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "resume": ["hello.html"],
    "news": ["hello.html", 'ablog/archives.html'],
    "news/**": ['ablog/postcard.html', 'ablog/recentposts.html', 'ablog/archives.html'],
    "blog": ['tagcloud.html', 'archives.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "pechakucha":[]
}


blog_title = "Blog "
blog_path = "news"
blog_feed_length = 5
fontawesome_included = True
blog_post_pattern = "news/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    # "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "attrs_block",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    # "tasklist",
]

def setup(app):
    app.add_css_file("custom.css")
    # app.add_js_file("custom.js")
