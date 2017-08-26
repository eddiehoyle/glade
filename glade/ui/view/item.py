from PySide.QtCore import *
from PySide.QtGui import *


def colorbg(cls, color):
    pal = QPalette()
    pal.setColor(QPalette.Background, color);
    cls.setAutoFillBackground(True);
    cls.setPalette(pal);

class PluginSectionWidget(QListWidgetItem):

    expand = Signal(bool)
    
    def __init__(self, directory, parent=None):
        super(PluginSectionWidget, self).__init__(parent=parent)

        self.directory = directory

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.is_expanded = False

        icon = QIcon()
        label = QLabel(directory)

        layout.addWidget(icon)
        layout.addWidget(label)
        layout.addStretch()

    def mouseMoveEvent(self, event):
        super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginHeaderWidget, self).mousePressEvent(event)
        self.expand.emit(not self.is_expanded)
        self.is_expanded = not self.is_expanded
        print "mousePressEvent()"

class PluginBodyWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginBodyWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QFormLayout()
        self.setLayout(layout)

        self.initialise()

    def initialise(self):

        for key, value in self.plugin.data().iteritems():
            edit = QLineEdit()
            edit.setText(value)
            self.layout().addRow(key, edit)

class PluginHeaderWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, plugin, parent=None):
        super(PluginHeaderWidget, self).__init__(parent=parent)

        self.plugin = plugin

        # Header
        self.name_label = QLabel(plugin.name)
        self.load_label = QLabel("Load")
        self.load_checkbox = QCheckBox()
        self.autoload_label = QLabel("Autoload")
        self.autoload_checkbox = QCheckBox()

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.name_label)
        header_layout.addStretch()
        header_layout.addWidget(self.load_label)
        header_layout.addWidget(self.load_checkbox)
        header_layout.addWidget(self.autoload_label)
        header_layout.addWidget(self.autoload_checkbox)
        self.setLayout(header_layout)

        self.is_expanded = False
        self.setMouseTracking(True)

        self.initialise()

        self.setFixedHeight(self.sizeHint().height())

        colorbg(self,  "#123512")

    def initialise(self):

        self.name_label.setText(self.plugin.name)
        self.load_checkbox.setChecked(self.plugin.is_loaded)
        self.autoload_checkbox.setChecked(self.plugin.is_autoload)

    def mouseMoveEvent(self, event):
        super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginHeaderWidget, self).mousePressEvent(event)
        self.expand.emit(not self.is_expanded)
        self.is_expanded = not self.is_expanded
        print "mousePressEvent()"


class PluginWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginWidget, self).__init__(parent=parent)


        self.plugin = plugin

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.header_widget = PluginHeaderWidget(plugin)
        self.body_widget = PluginBodyWidget(plugin)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        colorbg(self,  "#747321")
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedHeight(self.sizeHint().height())


    @Slot(bool)
    def expand(self, state):
        print "Expanding: %s" % state