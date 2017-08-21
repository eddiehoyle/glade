from PySide.QtCore import *
from PySide.QtGui import *

class PluginRefresh(QPushButton):
    
    def __init__(self, parent=None):
        super(PluginRefresh, self).__init__(parent=parent)

        self.setText("Refresh")