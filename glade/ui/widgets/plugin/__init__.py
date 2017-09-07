from PySide.QtCore import *
from PySide.QtGui import *

class AbstractPluginHeaderWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractPluginHeaderWidget, self).__init__(parent=parent)

        self.is_expanded = True

    def setExpanded(self, state):
        self.expand.emit(state)
        self.is_expanded = state

    def mouseMoveEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mousePressEvent(event)
        self.setExpanded(not self.is_expanded)

    def mouseReleaseEvent(self, event):
        super(AbstractPluginHeaderWidget, self).mouseReleaseEvent(event)


class AbstractPluginBodyWidget(QWidget):

    expand = Signal(bool)

    def __init__(self, parent=None):
        super(AbstractPluginBodyWidget, self).__init__(parent=parent)