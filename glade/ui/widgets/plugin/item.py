from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

from . import AbstractPluginWidget
from . import AbstractPluginBodyWidget
from . import AbstractPluginHeaderWidget
from ... import style
from .load import LabelledChecboxWidget

class PluginItemWidget(AbstractPluginWidget):

    def __init__(self, plugin, parent=None):
        super(PluginItemWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.header_widget = PluginHeaderWidget(plugin)
        self.header_widget.expand.connect(self.expand)

        self.body_widget = PluginBodyWidget(plugin)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)
        layout.addStretch()

        self.header_widget.set_expanded(False)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

        self.setObjectName("item")
        self.header_widget.setObjectName("itemHeader")
        self.body_widget.setObjectName("itemBody")

    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)


class PluginHeaderWidget(AbstractPluginHeaderWidget):

    def __init__(self, plugin, parent=None):
        super(PluginHeaderWidget, self).__init__(parent=parent)

        self.plugin = plugin

        self.name_label = QLabel(plugin.name)
        self.name_label.setObjectName("itemPluginName")

        self.load_widget = LabelledChecboxWidget("Load")
        self.autoload_widget = LabelledChecboxWidget("Autoload")
        
        # self.load_label = QLabel("Load")
        # self.load_label.setObjectName("loadLabel")
        # self.autoload_label = QLabel("Autoload")
        # self.autoload_label.setObjectName("autoloadLabel")

        # self.load_checkbox = QCheckBox()
        # self.autoload_checkbox = QCheckBox()

        # load_pix = QPixmap("resources:icons/load.png")
        # load_icon = QIcon()
        # load_icon.addPixmap(load_pix)
        # self.load_button = QPushButton("Load")
        # self.load_button.setObjectName("loadIcon")
        # self.load_button.setIcon(load_icon)
        # self.load_button.setCheckable(True)


        # autoload_pix = QPixmap("resources:icons/autoload.png")
        # autoload_icon = QIcon()
        # autoload_icon.addPixmap(autoload_pix)
        # self.autoload_button = QPushButton("Autoload")
        # self.autoload_button.setObjectName("autoloadIcon")
        # self.autoload_button.setIcon(autoload_icon)
        # self.autoload_button.setCheckable(True)

        # spacer = QSpacerItem(2, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        layout.addWidget(self.name_label)
        layout.addStretch()
        # layout.addItem(spacer)
        # layout.addWidget(self.load_button)
        # layout.addWidget(self.load_label)
        # layout.addWidget(self.load_checkbox)
        # layout.addWidget(self.autoload_checkbox)
        # layout.addWidget(self.autoload_button)
        # layout.addWidget(self.autoload_label)
        layout.addWidget(self.load_widget)
        layout.addWidget(self.autoload_widget)

        self.is_expanded = True
        self.setMouseTracking(True)

        self.initialise()

    def set_expanded(self, state):
        super(PluginHeaderWidget, self).set_expanded(state)

    def highlight(self, chars):
        pass

    def initialise(self):
        self.name_label.setText(self.plugin.name)
        # self.load_button.setChecked(self.plugin.is_loaded)
        # self.autoload_button.setChecked(self.plugin.is_autoload)

    def mouseMoveEvent(self, event):
        print self.load_widget.rect().contains(event.pos())
        if not self.load_widget.rect().contains(self.load_widget.mapFromGlobal(event.pos())):
            super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if not self.load_widget.rect().contains(self.load_widget.mapFromGlobal(event.pos())):
            super(PluginHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if not self.load_widget.rect().contains(self.load_widget.mapFromGlobal(event.pos())):
            super(PluginHeaderWidget, self).mouseReleaseEvent(event)


class PluginBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, plugin, parent=None):
        super(PluginBodyWidget, self).__init__(parent=parent)

        # Unset base class layout
        QWidget().setLayout(self.layout())

        self.plugin = plugin

        layout = QFormLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)

        self.initialise()

    def add_data(self, label, widget):
        label.setObjectName("itemDataKey")
        widget.setObjectName("itemDataValue")
        self.layout().addRow(label, widget)

    def initialise(self):
        for key, value in self.plugin.data().iteritems():
            label = QLabel(key)
            widget = QLineEdit()
            widget.setText(value)
            self.add_data(label, widget)

