from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

class AbstractHeaderWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractHeaderWidget, self).__init__(parent=parent)

        self.is_expanded = True

    def mouseMoveEvent(self, event):
        super(AbstractHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(AbstractHeaderWidget, self).mousePressEvent(event)
        state = not self.is_expanded
        self.expand.emit(state)
        self.is_expanded = state

    def mouseReleaseEvent(self, event):
        super(AbstractHeaderWidget, self).mouseReleaseEvent(event)

class PluginSectionHeaderWidget(AbstractHeaderWidget):

    expand = Signal(bool)
    
    def __init__(self, directory, parent=None):
        super(PluginSectionHeaderWidget, self).__init__(parent=parent)

        layout = QHBoxLayout()
        self.setLayout(layout)

        # p.scaled(w,h,Qt::KeepAspectRatio));
        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/plus.png")
        pix_label = QLabel()
        pix_label.setPixmap(pix.scaled(14, 14, Qt.KeepAspectRatio))

        label = QLabel(directory)
        label.setText(directory)
        layout.addWidget(pix_label)
        layout.addWidget(label)
        layout.addStretch()

        self.setMouseTracking(True)

        self.is_expanded = True

    def mouseMoveEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginSectionHeaderWidget, self).mousePressEvent(event)
        utils.colorbg(self, "#444444")

    def mouseReleaseEvent(self, event):
        super(PluginSectionHeaderWidget, self).mouseReleaseEvent(event)
        utils.colorbg(self, "#333333")


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

        self.body_layout = QVBoxLayout()
        self.body_layout.setSpacing(0)
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_widget = QWidget()
        self.body_widget.setLayout(self.body_layout)

        self.layout.addWidget(self.header_widget)
        self.layout.addWidget(self.body_widget)

        self.is_expanded = True
        colorbg(self, "#333333")

        self.plugins = []


    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)

    def add_plugin(self, plugin):
        widget = PluginWidget(plugin)
        self.plugins.append(widget)
        self.body_layout.addWidget(widget)

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
        self.setLayout(header_layout)

        self.is_expanded = True
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

    def mouseReleaseEvent(self, event):
        super(PluginHeaderWidget, self).mouseReleaseEvent(event)

class PluginBodyWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginBodyWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QFormLayout()
        layout.setContentsMargins(0, 0, 0, 0)
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

        colorbg(self,  "#747321")
        layout.setContentsMargins(0, 0, 0, 0)
        
    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)