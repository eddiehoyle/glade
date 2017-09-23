import os
from PySide.QtCore import QDir
QDir.setSearchPaths(
    "stylesheets",
    [os.path.join(os.getenv("GLADE_ROOT", ""), "resources/stylesheets")]
)