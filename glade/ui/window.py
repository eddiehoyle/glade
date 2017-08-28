from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade import api

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

        self.search_field = PluginSearch()
        self.refresh_button = PluginRefresh()
        self.refresh_button.clicked.connect(self.refresh)

        self.list = PluginList()

        scroll = QScrollArea()
        scroll.setWidget(self.list)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                 border: none;
            }"""
        )

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(self.refresh_button)

        layout.addLayout(search_layout)
        layout.addWidget(scroll)

        self.refresh()

        self.setMinimumWidth(self.sizeHint().width())

    @Slot()
    def refresh(self):

        plugins = api.get_all_plugins()

        directories = {os.path.dirname(p.path) for p in plugins}
        for plugin in plugins:
            self.list.add_plugin(plugin)
        self.list.layout.addStretch()




