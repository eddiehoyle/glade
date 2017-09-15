from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils

from . import AbstractPluginHeaderWidget
from . import AbstractPluginBodyWidget
from ... import style

class PluginHeaderWidget(AbstractPluginHeaderWidget):

    def __init__(self, plugin, parent=None):
        super(PluginHeaderWidget, self).__init__(parent=parent)

        self.plugin = plugin

        self.name_label = QLabel(plugin.name)
        # self.load_label = QLabel("Load")
        # self.load_checkbox = QCheckBox()
        # self.autoload_label = QLabel("Autoload")
        # self.autoload_checkbox = QCheckBox()

        pix_load = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/disk.png")
        icon_load = QIcon()
        icon_load.addPixmap(pix_load.scaled(10, 10, Qt.KeepAspectRatio))
        self.load_button = QPushButton("Load")
        self.load_button.setIcon(icon_load)
        self.load_button.setStyleSheet("QPushButton { padding:0; }")
        self.load_button.setCheckable(True)

        pix_autoload = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/disk2.png")
        icon_autoload = QIcon()
        icon_autoload.addPixmap(pix_autoload.scaled(10, 10, Qt.KeepAspectRatio))
        self.autoload_button = QPushButton("Autoload")
        self.autoload_button.setIcon(icon_autoload)
        self.autoload_button.setStyleSheet("QPushButton { padding:0; }")
        self.autoload_button.setCheckable(True)

        spacer = QSpacerItem(2, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QHBoxLayout()
        layout.setContentsMargins(
            style.PluginItemStyle.HEADER_MARGIN,
            style.PluginItemStyle.HEADER_MARGIN,
            style.PluginItemStyle.HEADER_MARGIN,
            style.PluginItemStyle.HEADER_MARGIN,
        )
        layout.setSpacing(style.PluginItemStyle.HEADER_SPACING)
        self.setLayout(layout)

        layout.addWidget(self.name_label)
        layout.addStretch()
        # layout.addWidget(self.load_label)
        # layout.addWidget(self.load_checkbox)
        # layout.addWidget(self.autoload_label)
        # layout.addWidget(self.autoload_checkbox)
        layout.addWidget(self.load_button)
        layout.addItem(spacer)
        layout.addWidget(self.autoload_button)

        self.is_expanded = True
        self.setMouseTracking(True)

        self.initialise()

        utils.colorbg(self,  "#123512")

    def set_expanded(self, state):
        super(PluginHeaderWidget, self).set_expanded(state)

    def highlight(self, chars):
        pass

    def initialise(self):
        self.name_label.setText(self.plugin.name)
        self.load_button.setChecked(self.plugin.is_loaded)
        self.autoload_button.setChecked(self.plugin.is_autoload)

    def mouseMoveEvent(self, event):
        super(PluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(PluginHeaderWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(PluginHeaderWidget, self).mouseReleaseEvent(event)


class PluginBodyWidget(AbstractPluginBodyWidget):

    def __init__(self, plugin, parent=None):
        super(PluginBodyWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QFormLayout()
        layout.setContentsMargins(
            style.PluginItemStyle.BODY_MARGIN,
            style.PluginItemStyle.BODY_MARGIN,
            style.PluginItemStyle.BODY_MARGIN,
            style.PluginItemStyle.BODY_MARGIN,
        )
        layout.setSpacing(style.PluginItemStyle.BODY_SPACING)
        self.setLayout(layout)

        self.initialise()

    def initialise(self):

        for key, value in self.plugin.data().iteritems():
            edit = QLineEdit()
            edit.setText(value)
            utils.colorbg(edit, "#222222")
            edit.setStyleSheet(
"""QLineEdit {
    border: none;
    padding: 2;
    background: rgb(32, 32, 32);
}
""")
            self.layout().addRow(key, edit)


class PluginItemWidget(QWidget):

    def __init__(self, plugin, parent=None):
        super(PluginItemWidget, self).__init__(parent=parent)

        self.plugin = plugin

        layout = QVBoxLayout()
        layout.setContentsMargins(
            style.PluginItemStyle.MARGIN,
            style.PluginItemStyle.MARGIN,
            style.PluginItemStyle.MARGIN,
            style.PluginItemStyle.MARGIN,
        )
        layout.setSpacing(style.PluginItemStyle.SPACING)
        self.setLayout(layout)

        self.header_widget = PluginHeaderWidget(plugin)
        self.header_widget.expand.connect(self.expand)
        self.body_widget = PluginBodyWidget(plugin)

        layout.addWidget(self.header_widget)
        layout.addWidget(self.body_widget)
        layout.addStretch()

        self.header_widget.set_expanded(False)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)

