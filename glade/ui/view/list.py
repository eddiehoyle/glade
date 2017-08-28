from PySide.QtCore import *
from PySide.QtGui import *
from collections import defaultdict
import os
from . import item
from glade.ui import utils

class PluginList(QWidget):

    def __init__(self, parent=None):
        super(PluginList, self).__init__(parent=parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        # utils.randombg(self)

        self.sections = {}

    def add_plugin(self, plugin):


        directory = os.path.dirname(plugin.path)
        section = self.sections.get(directory, None)
        if section is None:
            section = item.PluginSectionWidget(directory)
            self.layout.addWidget(section)
            self.sections[directory] = section

        section.add_plugin(plugin)

        # widget = item.PluginWidget(plugin)
        # section = self.sections[directory]
        # section.addWidget(widget)
        # self.layout.addWidget(widget)

    def clear(self):
        pass