from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade import api

from .search import PluginSearch
from .refresh import PluginRefresh
from .view.list import PluginList
from .view.item import PluginWidget
from .tree import PluginTree


class PluginManagerWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PluginManagerWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        search_label = QLabel("Search")
        self.search_field = PluginSearch()
        self.refresh_button = PluginRefresh()
        self.refresh_button.clicked.connect(self.refresh)

        # self.list = PluginList()
        self.tree = PluginTree()

        # scroll = QScrollArea()
        # scroll.setWidget(self.list)
        # scroll.setWidgetResizable(True)
        # scroll.setObjectName("pluginScroll")

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(self.refresh_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        layout.addLayout(search_layout)
        layout.addWidget(self.tree)
        layout.addWidget(self.close_button)

        self.refresh()

        self.setMinimumWidth(self.sizeHint().width())
        size = self.sizeHint()
        size.setHeight(size.height() * 2)
        self.resize(size)

        self.setStyleSheet("""QScrollArea { background-color: #333333; }""")

    @Slot()
    def refresh(self):

        plugins = api.get_all_plugins()

        directories = {os.path.dirname(p.path) for p in plugins}

        # for plugin in plugins:
        #     self.list.add_section(os.path.dirname(plugin.path))
        # for plugin in plugins:
        #     self.list.add_plugin(plugin)
        # self.list.layout.addStretch()


