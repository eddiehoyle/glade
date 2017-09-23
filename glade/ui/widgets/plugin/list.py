from PySide.QtCore import *
from PySide.QtGui import *
import os
from glade.ui import utils
from .section import PluginSectionWidget

class PluginList(QFrame):

    def __init__(self, parent=None):
        super(PluginList, self).__init__(parent=parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.sections = {}

    def filter(self, terms):
        """"""
        for directory, section in self.sections.iteritems():
            section.filter(terms)

    def __add_section(self, directory):
        """"""

        section = self.sections.get(directory, None)
        if section is None:
            index = len(self.sections)
            section = PluginSectionWidget(index, directory)
            self.layout.addWidget(section)
            self.sections[directory] = section
        return section

    def add_plugin(self, plugin):
        """"""
        directory = os.path.dirname(plugin.path)
        section = self.__add_section(directory)
        return section.add_plugin(plugin)

    def clear(self):
        """"""
        for directory, section in self.sections.iteritems():
            section.deleteLater()
        self.sections = {}