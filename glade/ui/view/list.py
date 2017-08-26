from PySide.QtCore import *
from PySide.QtGui import *
from collections import defaultdict
from . import item
from glade.ui import utils

class PluginList(QWidget):

    def __init__(self, parent=None):
        super(PluginList, self).__init__(parent=parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        utils.randombg(self)

        self.sections = {}

    def add_section(self, directory):
        section = PluginSectionWidget(directory)
        self.sections[directory] = []

    def add_plugin(self, directory, plugin):
        self.sections[section].append(plugin)
        widget = item.PluginWidget(plugin)
        self.layout.addWidget(widget)

    def clear(self):
        pass