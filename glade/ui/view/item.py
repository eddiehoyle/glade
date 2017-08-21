from PySide.QtCore import *
from PySide.QtGui import *

class PluginItem(QListWidgetItem):
    
    def __init__(self, parent=None):
        super(PluginItem, self).__init__(parent=parent)

class PluginWidget(QWidget):

    def __init__(self, label, parent=None):
        super(PluginWidget, self).__init__(parent=parent)

        self.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton(label)
        layout.addWidget(button)


