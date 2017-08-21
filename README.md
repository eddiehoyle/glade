# glade
Learning QThreads by writing a custom Maya plugin manager.

temp usage:

```python
import sys
path = "/Users/eddiehoyle/Code/python/glade"
if path not in sys.path:
    sys.path.insert(0, path)
    
import glade;reload(glade)
from glade.ui import refresh;reload(refresh)
from glade.ui.view import list;reload(list)
from glade.ui.view import item;reload(item)
from glade.ui import window;reload(window)

win = window.PluginManagerWindow()
win.show()
```
