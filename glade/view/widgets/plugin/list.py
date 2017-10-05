from PySide.QtCore import *
from PySide.QtGui import *

import os

from glade.view import utils
from glade.view.widgets.plugin.section import PluginSectionWidget

class PluginList(QFrame):

    # plugin_loaded = Signal(str, str)
    # plugin_unloaded = Signal(str, str)

    def __init__(self, parent=None):
        super(PluginList, self).__init__(parent=parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)
        layout.addStretch()

        self.sections = {}

        self.setObjectName("pluginList")

    def plugin_loaded(self, directory, name):
        """"""
        section = self.sections.get(directory)
        # print "PluginList.plugin_loaded() :", directory, name
        if section is not None:
            section.plugin_loaded(name)

    def plugin_unloaded(self, directory, name):
        """"""
        section = self.sections.get(directory)
        # print "PluginList.plugin_unloaded() :", directory, name
        if section is not None:
            section.plugin_unloaded(name)

    def filter(self, terms):
        """"""
        for directory, section in self.sections.iteritems():
            section.filter(terms)

    def __add_section(self, directory):
        """"""
        section = self.sections.get(directory, None)
        if section is None:
            section = PluginSectionWidget(directory, parent=self)
            self.layout().insertWidget(self.layout().count() - 1, section)
            self.sections[directory] = section
        return section

    def add_plugin(self, directory, plugin):
        """"""
        section = self.__add_section(directory)
        return section.add_plugin(plugin)

    def clear(self):
        """"""
        for directory, section in self.sections.iteritems():
            section.deleteLater()
        self.sections = {}