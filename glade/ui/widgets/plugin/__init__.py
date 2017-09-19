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

class AbstractPluginBodyWidget(QFrame):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractPluginBodyWidget, self).__init__(parent=parent)