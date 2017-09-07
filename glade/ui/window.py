from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade import api

from .widgets.plugin.list import PluginList
from . import utils


class PluginManagerWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PluginManagerWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        search_label = QLabel("Filter")
        search_field = QLineEdit()
        search_field.textChanged.connect(self.search)
        search_field.setFocus()

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(search_field)

        self.list = PluginList()

        scroll = QScrollArea()
        scroll.setWidget(self.list)
        scroll.setWidgetResizable(True)
        scroll.setObjectName("pluginScroll")

        footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.refresh)
        footer_layout.addWidget(close_button)
        footer_layout.addWidget(refresh_button)
        footer_layout.setContentsMargins(0, 0, 0, 0)

        layout.addLayout(search_layout)
        layout.addWidget(scroll)
        layout.addWidget(footer_widget)

        self.refresh()

        self.setMinimumWidth(self.sizeHint().width())
        size = self.sizeHint()
        size.setHeight(min(size.height() * 2, 350))
        size.setWidth(size.width() + 30)
        self.resize(size)

        utils.colorbg(self.list, "#333333")



    @Slot()
    def refresh(self):

        plugins = api.get_all_plugins()

        directories = {os.path.dirname(p.path) for p in plugins}
        for plugin in plugins:
            self.list.add_plugin(plugin)
        self.list.layout.addStretch()


    @Slot(str)
    def search(self, text):
        """"""
        # terms = text.split()
        # self.list.filter(terms)

    def filter(self, terms):
        """"""

        sections = self.list.get_sections()
