from PySide.QtCore import *
from PySide.QtGui import *

from difflib import SequenceMatcher as SM

class SearchLineEdit(QLineEdit):

    def __init__(self, icon, parent=None):
        super(SearchLineEdit, self).__init__(parent=parent)
        self.icon = icon
        self.setTextMargins(0, 0, 0, 0)
        self.setObjectName("searchField")
        self.setFrame(False)

    def paintEvent(self, event):
        super(SearchLineEdit, self).paintEvent(event)

        painter = QPainter(self)
        pix = self.icon.pixmap(30, 30)
        pix_x = (self.height()/2)-(pix.height()/2)
        pix_y = pix_x
        painter.drawPixmap(pix_x, pix_y, pix)
