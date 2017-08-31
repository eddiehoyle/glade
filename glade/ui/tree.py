from PySide.QtCore import *
from PySide.QtGui import *
from collections import defaultdict
import os
from glade.ui import utils
from glade import api
# from .view.item import PluginWidget


class PluginTreeModel(QStandardItemModel):

    def __init__(self, parent=None):
        super(PluginTreeModel, self).__init__(parent=parent)


class PluginTreeItem(QStandardItem):

    def __init__(self, parent=None):
        super(PluginTreeItem, self).__init__(parent=parent)

class PluginTreeItemWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginTreeItemWidget, self).__init__(parent=parent)

        self.plugin = plugin

        self.name_label = QLabel(plugin.name)
        self.load_label = QLabel("Load")
        self.load_checkbox = QCheckBox()
        self.autoload_label = QLabel("Autoload")
        self.autoload_checkbox = QCheckBox()

        layout = QHBoxLayout()
        layout.addWidget(self.name_label)
        layout.addStretch()
        layout.addWidget(self.load_label)
        layout.addWidget(self.load_checkbox)
        layout.addWidget(self.autoload_label)
        layout.addWidget(self.autoload_checkbox)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

class PluginTree(QTreeView):

    def __init__(self, parent=None):
        super(PluginTree, self).__init__(parent=parent)

        self.setModel(PluginTreeModel())

        item = PluginTreeItem()
        self.model().setItem(0, 0, item)
        index = self.model().index(0, 0, QModelIndex())
        button = QPushButton()

        plugin = api.get_all_plugins()[0]

        w = PluginTreeItemWidget(plugin)
        self.setIndexWidget(index, w)
        # self.model().appendRow([item])

    def add_section(self, directory):
        """"""
        pass

    def add_plugin(self, plugin):
        """"""
        pass

    def clear(self):
        """"""
        pass
