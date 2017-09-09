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
        self.load_label = QLabel("Load")
        self.load_checkbox = QCheckBox()
        self.autoload_label = QLabel("Autoload")
        self.autoload_checkbox = QCheckBox()

        pix = QPixmap("/Users/eddiehoyle/Code/python/glade/icons/plus.png")
        icon = QIcon()
        icon.addPixmap(pix.scaled(10, 10, Qt.KeepAspectRatio))
        self.load_button = QPushButton(icon, "L")
        self.load_button.setStyleSheet("QPushButton { padding:0; }")
        self.autoload_button = QPushButton(icon, "A")
        self.autoload_button.setStyleSheet("QPushButton { padding:0; }")

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
        layout.addWidget(self.autoload_button)

        self.is_expanded = True
        self.setMouseTracking(True)

        self.initialise()

        utils.colorbg(self,  "#123512")

    def highlight(self, chars):
        pass

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
            # utils.colorbg(edit, "#234512")
            # edit.setFixedHeight(80)
            edit.setStyleSheet(
"""QLineEdit {
    border: none;
    padding: 2;
}
""")
            # edit.setAlignment(Qt.AlignCenter)
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

        self.header_widget.setExpanded(False)

    def filter(self, terms):
        """"""
        self.header_widget.filter(terms)
        self.body_widget.filter(terms)

    @Slot(bool)
    def expand(self, state):
        """"""
        self.body_widget.setVisible(state)