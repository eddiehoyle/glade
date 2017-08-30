from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

class AbstractHeaderWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractHeaderWidget, self).__init__(parent=parent)

        self.is_expanded = True

    def setExpanded(self, state):
        """"""
        self.expand.emit(state)
        self.is_expanded = state

    def mouseMoveEvent(self, event):
        super(AbstractHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(AbstractHeaderWidget, self).mousePressEvent(event)
        self.setExpanded(not self.is_expanded)

    def mouseReleaseEvent(self, event):
        super(AbstractHeaderWidget, self).mouseReleaseEvent(event)


class AbstractBodyWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractBodyWidget, self).__init__(parent=parent)

class PluginSectionBodyWidget(AbstractBodyWidget):

    expand = Signal(bool)
    
    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)


class PluginSectionHeaderWidget(AbstractHeaderWidget):

    expand = Signal(bool)
    
    def __init__(self, directory, parent=None):
        super(PluginSectionHeaderWidget, self).__init__(parent=parent)

        layout = QHBoxLayout()
        self.setLayout(layout)

        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/plus.png")
        pix.rect()
        pix_label = QLabel()
        pix_label.setPixmap(pix.scaled(10, 10, Qt.KeepAspectRatio))

        label = QLabel(directory)
        label.setText(directory)
        layout.addWidget(pix_label)
        layout.addWidget(label)
        layout.addStretch()
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(0)

        self.setMouseTracking(True)


    def mouseMoveEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseMoveEvent(event)
        utils.colorbg(self, "#444444")

    def mousePressEvent(self, event):
        super(PluginSectionHeaderWidget, self).mousePressEvent(event)
        utils.colorbg(self, "#222222")

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)
        utils.colorbg(self, "#444444")


class PluginSectionBodyWidget(QWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionBodyWidget, self).__init__(parent=parent)

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        utils.colorbg(self, "#222222")

class PluginSectionWidget(QWidget):

    def __init__(self, directory, parent=None):
        super(PluginSectionWidget, self).__init__(parent=parent)

        self.directory = directory

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.header_widget = PluginSectionHeaderWidget(directory)
        self.header_widget.expand.connect(self.expand)
        self.body_widget = PluginSectionBodyWidget(directory)

        self.layout.addWidget(self.header_widget)
        self.layout.addWidget(self.body_widget)

        self.plugins = []

        self.header_widget.setExpanded(False)

    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginWidget(plugin)
        self.plugins.append(widget)
        self.body_widget.layout().addWidget(widget)

    def mouseMoveEvent(self, event):
        super(PluginSectionWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginSectionWidget, self).mousePressEvent(event)
        

# ----------------------------------------------------------------------------

class PluginHeaderWidget(AbstractHeaderWidget):

    def __init__(self, plugin, parent=None):
        super(PluginHeaderWidget, self).__init__(parent=parent)

        self.plugin = plugin

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
        header_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(header_layout)

        self.is_expanded = True
        self.setMouseTracking(True)

        self.initialise()

        utils.colorbg(self,  "#123512")

    def initialise(self):
        self.name_label.setText(self.plugin.name)
        self.load_checkbox.setChecked(self.plugin.is_loaded)
        self.autoload_checkbox.setChecked(self.plugin.is_autoload)

    def mouseMoveEvent(self, event):
        super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(PluginHeaderWidget, self).mouseReleaseEvent(event)

class PluginBodyWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginBodyWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QFormLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        self.setLayout(layout)

        self.initialise()

    def initialise(self):

        for key, value in self.plugin.data().iteritems():
            edit = QLineEdit()
            edit.setText(value)
            self.layout().addRow(key, edit)



class PluginWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.header_widget = PluginHeaderWidget(plugin)
        self.body_widget = PluginBodyWidget(plugin)
        self.header_widget.expand.connect(self.expand)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)

        utils.colorbg(self,  "#747321")
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.header_widget.setExpanded(False)
        
    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)