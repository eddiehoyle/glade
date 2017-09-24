from PySide.QtCore import *
from PySide.QtGui import *

class AbstractPluginHeaderWidget(QFrame):

    MARGIN = 0
    SPACING = 0

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractPluginHeaderWidget, self).__init__(parent=parent)

        self.is_expanded = False

    def set_expanded(self, state):
        self.expand.emit(state)
        self.is_expanded = state

    def mouseMoveEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mousePressEvent(event)
        self.set_expanded(not self.is_expanded)

    def mouseReleaseEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mouseReleaseEvent(event)

    def enterEvent(self, event):
        super(AbstractPluginHeaderWidget, self).enterEvent(event)
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        super(AbstractPluginHeaderWidget, self).leaveEvent(event)
        self.unsetCursor()


class AbstractPluginBodyWidget(QFrame):

    def __init__(self, parent=None):
        super(AbstractPluginBodyWidget, self).__init__(parent=parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

    def addWidget(self, widget):
        """Override"""

        self.layout().addWidget(widget)

    def setVisible(self, state):
        """Override"""

        updates_enabled = self.updatesEnabled()
        self.setUpdatesEnabled(False)
        super(AbstractPluginBodyWidget, self).setVisible(state)
        self.setUpdatesEnabled(updates_enabled)


class AbstractPluginWidget(QFrame):

    def __init__(self, parent=None):
        super(AbstractPluginWidget, self).__init__(parent=parent)
