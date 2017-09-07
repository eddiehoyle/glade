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

        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/plus.png")
        pix.rect()
        pix_label = QLabel()
        pix_label.setPixmap(pix.scaled(10, 10, Qt.KeepAspectRatio))

        self.label = QLabel(directory)
        self.label.setText(directory)
        layout.addWidget(pix_label)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.setContentsMargins(
            style.PluginSectionStyle.HEADER_MARGIN,
            style.PluginSectionStyle.HEADER_MARGIN,
            style.PluginSectionStyle.HEADER_MARGIN,
            style.PluginSectionStyle.HEADER_MARGIN,
        )
        layout.setSpacing(style.PluginSectionStyle.HEADER_SPACING)

        self.setMouseTracking(True)

        utils.colorbg(self, "#444444")

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
        # utils.colorbg(self, "#222222")

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)
        # utils.colorbg(self, "#444444")

class PluginSectionBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(
            style.PluginSectionStyle.BODY_MARGIN,
            style.PluginSectionStyle.BODY_MARGIN,
            style.PluginSectionStyle.BODY_MARGIN,
            style.PluginSectionStyle.BODY_MARGIN,
        )
        layout.setSpacing(style.PluginSectionStyle.BODY_SPACING)
        self.setLayout(layout)


class PluginSectionWidget(QWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QVBoxLayout()
        layout.setContentsMargins(
            style.PluginSectionStyle.MARGIN,
            style.PluginSectionStyle.MARGIN,
            style.PluginSectionStyle.MARGIN,
            style.PluginSectionStyle.MARGIN,
        )
        layout.setSpacing(style.PluginSectionStyle.SPACING)
        self.setLayout(layout)

        self.header_widget = PluginSectionHeaderWidget(directory)
        self.header_widget.expand.connect(self.expand)

        self.body_widget = PluginSectionBodyWidget(directory)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        self.plugins = []

        self.header_widget.setExpanded(False)

    @Slot(bool)
    def expand(self, state):
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginItemWidget(plugin)
        self.plugins.append(widget)
        self.body_widget.layout().addWidget(widget)

        # TODO: Improve this
        if len(self.plugins) % 2 == 0:
            utils.colorbg(widget.header_widget, "#111111")
        else:
            utils.colorbg(widget.header_widget, "#222222")

    def filter(self, terms):
        self.header_widget.filter(terms)
        self.body_widget.filter(terms)
