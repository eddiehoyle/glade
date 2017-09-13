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
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(0)
        search_widget = QWidget()
        search_widget.setLayout(search_layout)

        self.list = PluginList()

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidget(self.list)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame);
        scroll.setObjectName("pluginScroll")

        column_layout = QVBoxLayout()
        column_layout.setContentsMargins(0, 0, 0, 0)
        column_layout.setSpacing(0)
        column_widget = QWidget()
        column_widget.setLayout(column_layout)

        utils.colorbg(column_widget, "#123123")

        expand_button = QPushButton("+")
        expand_button.setFixedSize(23, 23)
        collapse_button = QPushButton("-")
        collapse_button.setFixedSize(23, 23)

        column_layout.addWidget(expand_button)
        column_layout.addWidget(collapse_button)
        column_layout.addStretch()

        body_layout = QHBoxLayout()
        body_widget = QWidget()
        body_widget.setLayout(body_layout)
        body_layout.addWidget(column_widget)
        body_layout.addWidget(scroll)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(8)

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

        layout.addWidget(search_widget)
        layout.addWidget(body_widget)
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
        for i, plugin in enumerate(plugins):
            self.list.add_plugin(plugin)
            break;
        self.list.layout.addStretch()


    @Slot(str)
    def search(self, text):
        """"""
        # terms = text.split()
        # self.list.filter(terms)

    def filter(self, terms):
        """"""

        sections = self.list.get_sections()
