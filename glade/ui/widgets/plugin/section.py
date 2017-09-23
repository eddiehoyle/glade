from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

from .item import PluginItemWidget
from . import AbstractPluginHeaderWidget
from . import AbstractPluginBodyWidget
from . import AbstractIndexedPluginWidget
from ... import style


class PluginSectionWidget(AbstractIndexedPluginWidget):

    plugin_added = Signal(int)

    def __init__(self, index, directory, parent=None):
        super(PluginSectionWidget, self).__init__(index, parent=parent)

        self.directory = directory

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.header_widget = PluginSectionHeaderWidget(directory)
        self.header_widget.expand.connect(self.expand)
        self.plugin_added.connect(self.header_widget.count_updated)

        self.body_widget = PluginSectionBodyWidget(directory)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        self.plugins = []

        self.header_widget.set_expanded(False)

        self.initialise()

    def initialise(self):
        suffix = "A" if self.index() % 2 == 0 else "B"
        self.setObjectName("section{0}".format(suffix))
        self.body_widget.setObjectName("sectionBody{0}".format(suffix))
        self.header_widget.setObjectName("sectionHeader{0}".format(suffix))

    @Slot(bool)
    def expand(self, state):
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        index = len(self.plugins)
        widget = PluginItemWidget(index, plugin)
        self.plugins.append(widget)
        self.body_widget.addWidget(widget)
        self.plugin_added.emit(index + 1)

    def filter(self, terms):
        self.header_widget.filter(terms)
        self.body_widget.filter(terms)


class PluginSectionHeaderWidget(AbstractPluginHeaderWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionHeaderWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QHBoxLayout()
        self.setLayout(layout)

        folder_pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/folder.png")
        folder_label = QLabel()
        folder_label.setPixmap(folder_pix.scaled(16, 16, Qt.KeepAspectRatio))

        self.label = QLabel(directory)
        self.label.setText(directory)
        self.label.setObjectName("sectionPluginDirectory")

        self.count_label = QLabel("0")

        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/arrow_left.png")
        self.arrow_label = QLabel()
        self.arrow_label.setPixmap(pix.scaled(16, 16, Qt.KeepAspectRatio))


        layout.addWidget(folder_label)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.count_label)
        layout.addWidget(self.arrow_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setMouseTracking(True)
        self.expand.connect(self.__update_icon)

    def __update_icon(self):
        if self.is_expanded:
            path = "/Users/eddiehoyle/Code/python/glade/icons/arrow_down.png"
        else:
            path = "/Users/eddiehoyle/Code/python/glade/icons/arrow_left.png"

        pix = QPixmap(path)
        self.arrow_label.setPixmap(pix.scaled(16, 16, Qt.KeepAspectRatio))

    Slot(int)
    def count_updated(self, number):
        self.count_label.setText(str(number))

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
