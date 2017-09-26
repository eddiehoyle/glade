import os
from PySide.QtCore import QDir
QDir.setSearchPaths(
    "resources",
    [os.path.join(os.getenv("GLADE_ROOT", ""), "resources")]
)