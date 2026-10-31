import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

project = "Student Tools"
author = "Марущак Сергей"
release = "1.0"
language = "ru"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_ivar = True

html_theme = "furo"
html_title = "Student Tools"
html_static_path = ["_static"]
exclude_patterns = []
