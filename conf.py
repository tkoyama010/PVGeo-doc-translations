# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized PVGeo document.
For example::
    sphinx-build -D language=ja -b html . _build/html
This conf.py do:
- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'PVGeo/docs/source`.
"""
import os
import shutil
import sys

import mock
from sphinx.util.pycompat import execfile_

sys.path.append(os.path.join(os.path.dirname(__file__), "./PVGeo/docs/source"))

os.environ["PYVISTA_VIRTUAL_DISPLAY"] = "True"
os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["PYVISTA_USE_PANEL"] = "true"
os.environ["PYVISTA_PLOT_THEME"] = "document"
os.environ["PYVISTA_AUTO_CLOSE"] = "false"

shutil.rmtree("PVGeo/docs/examples", ignore_errors=True)
shutil.rmtree("PVGeo/docs/source/index.rst", ignore_errors=True)
shutil.copytree("locale/examples", "PVGeo/docs/examples")
shutil.copyfile("locale/index.rst", "PVGeo/docs/source/index.rst")

absdir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.join(absdir, "PVGeo/docs/source")
execfile_(os.path.join(basedir, "conf.py"), globals())

locale_dirs = [os.path.join(basedir, "../../../locale/")]

# Mock the paraview module to build pvmacros docs
MOCK_MODULES = ["paraview", "paraview.simple", "discretize", "pyproj"]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()
autodoc_mock_imports = ["paraview", "vtk"]

sphinx_gallery_conf = {
    "plot_gallery": "False",
    "gallery_dirs": "examples",
}

html_static_path = [os.path.join(basedir, "_static")]


def setup(app):
    from sphinx.ext.autodoc import cut_lines

    app.srcdir = basedir
    app.confdir = app.srcdir
    app.connect("autodoc-process-docstring", cut_lines(4, what=["module"]))
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )

    # workaround for RTD
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    app.info = lambda *args, **kwargs: logger.info(*args, **kwargs)
    app.warn = lambda *args, **kwargs: logger.warning(*args, **kwargs)
    app.debug = lambda *args, **kwargs: logger.debug(*args, **kwargs)
