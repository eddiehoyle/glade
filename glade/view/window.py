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

        self.plugin_controller = PluginController()
        self.callback_controller = CallbackController()

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

        # Temp
        self.refresh()
        self.reload_stylesheet()

        self.setMinimumWidth(self.sizeHint().width())

        # Resize
        size = self.sizeHint()
        size.setHeight(min(size.height() * 2, 350))
        size.setWidth(size.width() + 30)
        self.resize(size)

    @Slot()
    def show(self):
        super(GladeWindow, self).show()
        self.plugin_controller.start()
        self.callback_controller.register()

    def closeEvent(self, event):
        self.plugin_controller.stop()
        self.callback_controller.unregister()

    @Slot()
    def reload_stylesheet(self):
        """Temp"""
        stylesheet = utils.read_stylesheet("resources:stylesheets/style.qss")
        self.setStyleSheet(stylesheet)

    def refresh(self):
        """"""

        self.list.layout().addStretch()

        directories = api.get_plugin_directories()
        self.plugin_controller.add_directories(directories)
        self.plugin_controller.plugin_found.connect(self.list.add_plugin)

        # plugins = api.get_all_plugins()
        # for plugin in plugins:
        #     self.list.add_plugin(plugin)
        

    @Slot(str)
    def search(self, text):
        """"""

        print "Searching:", text