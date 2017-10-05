import os

from PySide.QtCore import *
from PySide.QtGui import *

from glade import api
from glade.controller.plugin import PluginController
from glade.controller.callbacks import CallbackController
from glade.view.widgets.search import SearchLineEdit
from glade.view.widgets.plugin.list import PluginList
from glade.view import utils


class GladeWindow(QMainWindow):
    """"""

    def __init__(self, *args, **kwargs):
        super(GladeWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        search_pixmap = QPixmap("resources:icons/search.png")
        search_icon = QIcon()
        search_icon.addPixmap(search_pixmap)

        search_field = SearchLineEdit(search_icon)
        search_field.textChanged.connect(self.search)
        search_field.setFocus()
        search_field.setTextMargins(20, 1, 1, 1)

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_field)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(0)
        search_widget = QWidget()
        search_widget.setLayout(search_layout)

        self.list = PluginList()
        search_field.textChanged.connect(self.list.filter)

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidget(self.list)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame);

        body_layout = QHBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(8)
        body_layout.addWidget(scroll)
        body_widget = QWidget()
        body_widget.setLayout(body_layout)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.reload_stylesheet)

        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(0, 0, 0, 0)
        footer_layout.addWidget(close_button)
        footer_layout.addWidget(refresh_button)
        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)

        layout.addWidget(search_widget)
        layout.addWidget(body_widget)
        layout.addWidget(footer_widget)

        self.setMinimumWidth(self.sizeHint().width())

        self.plugin_control = PluginController()
        self.plugin_control.plugin_found.connect(self.list.add_plugin)
        self.callback_control = CallbackController()
        self.callback_control.plugin_loaded.connect(self.list.plugin_loaded)
        self.callback_control.plugin_unloaded.connect(self.list.plugin_unloaded)

        # Temp
        self.refresh()
        self.reload_stylesheet()

        # Resize
        size = self.sizeHint()
        size.setHeight(400)
        size.setWidth(400)
        self.resize(size)

    @Slot()
    def show(self):
        super(GladeWindow, self).show()
        self.plugin_control.start()
        self.callback_control.register()

    def closeEvent(self, event):
        self.plugin_control.stop()
        self.callback_control.unregister()

    @Slot(str)
    def search(self, text):
        """"""
        

    @Slot()
    def reload_stylesheet(self):
        """Temp"""
        stylesheet = utils.read_stylesheet("resources:stylesheets/style.qss")
        self.setStyleSheet(stylesheet)

    def refresh(self):
        """"""
        directories = api.get_plugin_directories()
        for directory in directories:
            self.plugin_control.add_directory(directory)

        # filenames = api.get_all_plugins()
        # for filename in filenames:
        #     self.list.add_plugin(os.path.split())
