from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui.widgets.plugin import AbstractPluginWidget
from glade.ui.widgets.plugin import AbstractPluginHeaderWidget
from glade.ui.widgets.plugin import AbstractPluginBodyWidget
from glade.ui.widgets.plugin.item import PluginItemWidget


class PluginSectionWidget(AbstractPluginWidget):

    plugin_added = Signal(int)

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

        self.plugin_added.connect(self.header_widget.count_updated)

        self.header_widget.set_expanded(False)

        self.setObjectName("section")
        self.body_widget.setObjectName("sectionBody")
        self.header_widget.setObjectName("sectionHeader")

    @Slot(bool)
    def expand(self, state):
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginItemWidget(plugin, parent=self)
        self.body_widget.addWidget(widget)
        self.plugin_added.emit(self.body_widget.layout().count())

    def filter(self, terms):
        self.header_widget.filter(terms)
        self.body_widget.filter(terms)


class PluginSectionHeaderWidget(AbstractPluginHeaderWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionHeaderWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QHBoxLayout()
        self.setLayout(layout)

        folder_pix = QPixmap("resources:icons/directory.png")
        folder_label = QLabel()
        folder_label.setPixmap(folder_pix)

        self.directory_label = QLabel(directory)
        self.directory_label.setText(directory)
        self.directory_label.setObjectName("sectionHeaderLabel")

        self.count_label = QLabel("0")
        self.count_label.setObjectName("sectionHeaderCount")

        # pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/arrow_left.png")
        # self.arrow_label = QLabel()
        # self.arrow_label.setPixmap(pix.scaled(16, 16, Qt.KeepAspectRatio))

        layout.addWidget(folder_label)
        layout.addWidget(self.directory_label)
        layout.addStretch()
        layout.addWidget(self.count_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setMouseTracking(True)

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

        self.directory_label.setText(new_string)

    def mouseMoveEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginSectionHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)

class PluginSectionBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)
