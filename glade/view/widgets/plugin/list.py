from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade.view import utils
from glade.view.widgets.plugin.section import PluginSectionWidget

class PluginList(QFrame):

    def __init__(self, parent=None):
        super(PluginList, self).__init__(parent=parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)

        self.sections = {}

        self.setObjectName("pluginList")

    def filter(self, terms):
        """"""
        for directory, section in self.sections.iteritems():
            section.filter(terms)

    def __add_section(self, directory):
        """"""
        section = self.sections.get(directory, None)
        if section is None:
            section = PluginSectionWidget(directory, parent=self)
            self.layout().addWidget(section)
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