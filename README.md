# glade
Learning QThreads by writing a custom Maya plugin manager.

temp usage:

```python
import sys
path = "/Users/eddiehoyle/Code/python/glade"
if path not in sys.path:
    sys.path.insert(0, path)

import glade;reload(glade)
from glade.ui import resources;reload(resources)
from glade.ui.widgets import plugin;reload(plugin)
from glade.ui.widgets.plugin import item;reload(item)
from glade.ui.widgets.plugin import section;reload(section)
from glade.ui.widgets.plugin import list;reload(list)
from glade.ui import window;reload(window)

win = window.PluginManagerWindow()
win.show()
#win.move(650, -700)
win.move(160, 200)
#win.styleSheet()

#from PySide.QtCore import *
```
