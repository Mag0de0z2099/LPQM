# docs/conf.py
import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, PROJECT_ROOT)  # por si luego importas tu paquete

# -- Project information -----------------------------------------------------
project = "LPQM"
author = "Mag0de0z2099"
year = datetime.now().year
copyright = f"{year}, {author}"
version = ""
release = version

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
templates_path = ["_templates"]

# 👇 MUY IMPORTANTE: solo el nombre lógico, sin .rst y sin rutas
root_doc = "index"          # (en Sphinx < 8 sería master_doc = "index")

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Si usas MyST o Markdown más adelante, podrás añadir:
# extensions += ["myst_parser"]

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"    # puedes cambiarlo luego si quieres
html_static_path = ["_static"]
