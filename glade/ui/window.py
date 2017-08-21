from PySide.QtCore import *
from PySide.QtGui import *

from .search import PluginSearch
from .refresh import PluginRefresh
from .view.list import PluginList
from .view.item import PluginItem
from .view.item import PluginWidget

class PluginManagerWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PluginManagerWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.search = PluginSearch()
        self.refresh = PluginRefresh()
        self.list = PluginList()

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search)
        search_layout.addWidget(self.refresh)

        layout.addLayout(search_layout)
        layout.addWidget(self.list)

        self._add()

    def _add(self):

        for index in range(5):

            widget = PluginWidget("Item: %s" % index)
            item = PluginItem()
            item.setSizeHint(widget.sizeHint())

            self.list.addItem(item)
            self.list.setItemWidget(item, widget)



