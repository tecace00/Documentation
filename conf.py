# -*- coding: utf-8 -*-
#
# SmartThings Documentation documentation build configuration file, created by
# sphinx-quickstart on Mon May 19 14:16:05 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, tostring
import xmltodict
import collections

# Convert a passed in capability name to the preference reference name.
def getReferenceName(name):
    result=""
    for index, value in enumerate(name.split()):
        if index == 0:
            result+=value.lower()
        else:
            result+=value
    return result

# Read in capability XML files
root = Element('capabilities')
properties = {}
elements = {}

# Read in the capability XML and properties files.
path = '_static/capabilities'
for dirpath, dirs, files in os.walk(path):
    for filename in sorted(files):
        if filename.endswith('.xml'):
            # If we have a XML file, read and parse it into and element tree
            # structure. Then use xmltodict to convert the XML structure into a
            # dictionary.
            fname = os.path.join(dirpath, filename)
            tree = ET.parse(fname)
            refName = getReferenceName(tree.getroot().get('name'))
            prefRef = Element('reference', {'name': refName})
            tree.getroot().append(prefRef)
            elements.update({refName: tree})
        elif filename.endswith('.properties'):
            # If we have a properties file, create a dictionary of its values
            # and stuff it into the properties dictionary
            key = filename.split(".", 1)[0]
            fname = os.path.join(dirpath, filename)
            with open(fname, 'r') as f:
                tempdict = {}
                for line in f:
                    line = line.rstrip()
                    if "=" not in line: continue
                    if line.startswith("#"): continue
                    k, v = line.split("=", 1)
                    tempdict[k] = v
            properties[key] = tempdict
        else:
            continue
# Sort the element tree by capability reference name
sortedElements = collections.OrderedDict(sorted(elements.items()))

for key, value in sortedElements.items():
    root.append(value.getroot())

capabilitiesDict = xmltodict.parse(tostring(root))

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SmartThings Developer Documentation'
copyright = u'2017, SmartThings'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'latest'
# The full version, including alpha/beta/rc tags.
release = 'latest'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'
#html_style = '/default.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'sticky_navigation': True
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'SmartThings Developer Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add øany paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'SmartThingsDocumentationdoc'

# Add the capabilities and properties dictionaries to the html_context so they
# are available to our Jinja templates.
html_context = {
    'capabilities': capabilitiesDict.get('capabilities').get('capability'),
    'properties': properties
}


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
# Set TOC depth to 5 for a nice, deep TOC.
'preamble': '\setcounter{tocdepth}{5}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'SmartThingsDocumentation.tex', u'SmartThings Developer Documentation',
   u'SmartThings', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'smartthingsdocumentation', u'SmartThings Documentation Documentation',
     [u'SmartThings'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'SmartThingsDocumentation', u'SmartThings Documentation Documentation',
   u'SmartThings', 'SmartThingsDocumentation', 'One line description of project.',
   'Miscellaneous'),
]

def setup(app):
  app.add_stylesheet("css/custom.css")
  app.add_javascript("javascript/clipboard.min.js")
  app.add_javascript("javascript/copycode.js")
  app.connect("source-read", rstjinja) # Add Jinja template processing to HTML build.
  app.connect("builder-inited", add_jinja_tests) # Add custom Jinja tests.

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Run rst files through the Jinja templating system. Currently only supports
# HTML output formats.
def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html' or app.builder.templates is None:
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
#    Uncomment this code if you want to see the generated RST file, output.txt
#    if 'test' in docname:
#        f = open('output.txt', 'w')
#        f.write(rendered.encode('utf8'))
#        f.close()
    source[0] = rendered

# Add custom tests to Jinja
def add_jinja_tests(app):
    if app.builder.format != 'html' or app.builder.templates is None:
        return
    app.builder.templates.environment.tests.update({
        'a_list': a_list # Test if the given argument is a list.
    })

# Test for Jinja that will return true if the given value argument is a list.
def a_list(value):
    return isinstance(value, list)
