from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade import api
from glade.ui import resources
from glade.ui import utils
from glade.ui.widgets.search import IconLineEdit
from glade.ui.widgets.plugin.list import PluginList
from glade.ui import style


class PluginManagerWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PluginManagerWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        pix_load = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/search.png")
        icon_load = QIcon()
        icon_load.addPixmap(pix_load.scaled(10, 10, Qt.KeepAspectRatio))

        search_edit = IconLineEdit(icon_load)
        search_edit.textChanged.connect(self.search)
        search_edit.setFocus()
        search_edit.setTextMargins(20, 1, 1, 1)

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_edit)
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

        body_layout = QHBoxLayout()
        body_widget = QWidget()
        body_widget.setLayout(body_layout)
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

        stylesheet = utils.read_stylesheet("stylesheets:style.qss")
        self.setStyleSheet(stylesheet)

    @Slot()
    def refresh(self):

        plugins = api.get_all_plugins()
        for plugin in plugins:
            self.list.add_plugin(plugin)
        self.list.layout.addStretch()


    @Slot(str)
    def search(self, text):
        """"""
        pass
        # terms = text.split()
        # self.list.filter(terms)

    def filter(self, terms):
        """"""

        sections = self.list.get_sections()
