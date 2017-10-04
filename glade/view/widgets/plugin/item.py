from PySide.QtCore import *
from PySide.QtGui import *


from glade.view.widgets.plugin import AbstractPluginWidget
from glade.view.widgets.plugin import AbstractPluginBodyWidget
from glade.view.widgets.plugin import AbstractPluginHeaderWidget


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

    def plugin_loaded(self):
        # print "PluginItemWidget.plugin_loaded() : %s" % self.plugin.name
        self.header_widget.load_checkbox.setChecked(True)

    def plugin_unloaded(self):
        # print "PluginItemWidget.plugin_unloaded() : %s" % self.plugin.name
        self.header_widget.load_checkbox.setChecked(False)

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

        self.load_checkbox = QCheckBox("Load")
        self.autoload_checkbox = QCheckBox("Autoload")

        self.load_checkbox.toggled.connect(self.plugin.set_loaded)
        self.autoload_checkbox.toggled.connect(self.plugin.set_autoload)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        layout.addWidget(self.name_label)
        layout.addStretch()
        layout.addWidget(self.load_checkbox)
        layout.addWidget(self.autoload_checkbox)

        self.is_expanded = True
        self.setMouseTracking(True)

        self.initialise()

    def set_expanded(self, state):
        super(PluginHeaderWidget, self).set_expanded(state)

    def highlight(self, chars):
        pass

    def initialise(self):
        self.load_checkbox.blockSignals(True)
        self.autoload_checkbox.blockSignals(True)

        self.name_label.setText(self.plugin.name)
        self.load_checkbox.setChecked(self.plugin.is_loaded)
        self.autoload_checkbox.setChecked(self.plugin.is_autoload)
        
        self.load_checkbox.blockSignals(False)
        self.autoload_checkbox.blockSignals(False)

    def mouseMoveEvent(self, event):
        under_load = self.load_checkbox.underMouse()
        under_autoload = self.autoload_checkbox.underMouse()
        if not under_load and not under_autoload:
            super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        under_load = self.load_checkbox.underMouse()
        under_autoload = self.autoload_checkbox.underMouse()
        if not under_load and not under_autoload:
            super(PluginHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        under_load = self.load_checkbox.underMouse()
        under_autoload = self.autoload_checkbox.underMouse()
        if not under_load and not under_autoload:
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

