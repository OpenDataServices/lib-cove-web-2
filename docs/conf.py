import os
import pathlib
import sys

import django

import libcoveweb2.settings

project = "LibCoveWeb2"

master_doc = "index"

html_theme = "odsc_default_sphinx_theme"

extensions = [
    "sphinx.ext.autodoc",
]

###### Make Sphinx able to document our python code

# We need to be able to see our code, so add this directory to path
sys.path.insert(0, str(pathlib.Path("..").resolve()))

# We need to set up Django enough that it won't complain
libcoveweb2.settings.INSTALLED_APPS += ("libcoveweb2",)
os.environ["DJANGO_SETTINGS_MODULE"] = "libcoveweb2.settings"
django.setup()
