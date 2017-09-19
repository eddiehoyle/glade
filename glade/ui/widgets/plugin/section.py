from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

from .item import PluginItemWidget
from . import AbstractPluginHeaderWidget
from . import AbstractPluginBodyWidget
from ... import style


class PluginSectionHeaderWidget(AbstractPluginHeaderWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionHeaderWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QHBoxLayout()
        self.setLayout(layout)

        folder_pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/folder.png")
        folder_label = QLabel()
        folder_label.setPixmap(folder_pix.scaled(16, 16, Qt.KeepAspectRatio))

        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/arrow_left.png")
        self.arrow_label = QLabel()
        self.arrow_label.setPixmap(pix.scaled(16, 16, Qt.KeepAspectRatio))

        self.label = QLabel(directory)
        self.label.setText(directory)
        self.label.setObjectName("sectionPluginDirectory")
        layout.addWidget(folder_label)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.arrow_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setObjectName("sectionHeader")


        self.setMouseTracking(True)
        self.expand.connect(self.__update_icon)

    def __update_icon(self):
        if self.is_expanded:
            path = "/Users/eddiehoyle/Code/python/glade/icons/arrow_down.png"
        else:
            path = "/Users/eddiehoyle/Code/python/glade/icons/arrow_left.png"

        pix = QPixmap(path)
        self.arrow_label.setPixmap(pix.scaled(16, 16, Qt.KeepAspectRatio))

    def highlight(self, chars):

        new_string = ""

        # Currently applies colors per-character, instead of substring
        for index, char in enumerate(self.directory):
            if char in chars:
                char = "<font color='red'>%s</font>" % char
            new_string += char

        self.label.setText(new_string)

    def mouseMoveEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginSectionHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)

class PluginSectionBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.setObjectName("sectionBody")


class PluginSectionWidget(QWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.header_widget = PluginSectionHeaderWidget(directory)
        self.header_widget.expand.connect(self.expand)

        self.body_widget = PluginSectionBodyWidget(directory)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        self.plugins = []

        self.header_widget.set_expanded(False)

    @Slot(bool)
    def expand(self, state):
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginItemWidget(plugin)
        self.plugins.append(widget)
        self.body_widget.layout().addWidget(widget)

    def filter(self, terms):
        self.header_widget.filter(terms)
        self.body_widget.filter(terms)