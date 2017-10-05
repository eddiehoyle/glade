from PySide.QtCore import *
from PySide.QtGui import *

from glade.view.widgets.plugin import AbstractPluginWidget
from glade.view.widgets.plugin import AbstractPluginHeaderWidget
from glade.view.widgets.plugin import AbstractPluginBodyWidget
from glade.view.widgets.plugin.item import PluginItemWidget


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

        self.plugin_added.connect(self.header_widget.count_updated)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        self.header_widget.set_expanded(False)

        self.setObjectName("section")
        self.body_widget.setObjectName("sectionBody")
        self.header_widget.setObjectName("sectionHeader")

        self.plugins = {}

    def plugin_loaded(self, name):
        """Emit load signals to widget
        """
        # print "PluginSectionWidget.plugin_loaded() :", name, self.plugins.keys()
        widget = self.plugins.get(name)
        if widget is not None:
            widget.plugin_loaded()

    def plugin_unloaded(self, name):
        """"""
        # print "PluginSectionWidget.plugin_unloaded() :", name
        widget = self.plugins.get(name)
        if widget is not None:
            widget.plugin_unloaded()

    @Slot(bool)
    def expand(self, state):
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginItemWidget(plugin, parent=self)
        self.body_widget.addWidget(widget)
        self.plugin_added.emit(self.body_widget.layout().count())

        self.plugins[plugin] = widget

    def filter(self, terms):
        self.header_widget.filter(terms)




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

    def filter(self, terms):
        pass

    def mouseMoveEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginSectionHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)

class PluginSectionBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)

        self.layout().setSpacing(1)
