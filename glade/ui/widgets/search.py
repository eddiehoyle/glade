from PySide.QtCore import *
from PySide.QtGui import *


class IconLineEdit(QLineEdit):

    def __init__(self, icon, parent=None):
        super(IconLineEdit, self).__init__(parent=parent)
        self.icon = icon
        self.setTextMargins(36, 1, 1, 1)
        self.setFixedHeight(36)
        # print 'sdf'
        self.setStyleSheet("""
QLineEdit {
    padding: 2 2 2 18;
    border: None;
    background-color: #333333;
    border-radius: 3px;
}""")

    def paintEvent(self, event):
        super(IconLineEdit, self).paintEvent(event)

        painter = QPainter(self)
        pix = self.icon.pixmap(30, 30)
        pix_x = (self.height()/2)-(pix.height()/2)
        pix_y = pix_x
        painter.drawPixmap(pix_x, pix_y, pix)
        # painter.setPen(QColor("#444444"));
        # painter.drawLine(
        #     self.height()-8,
        #     8,
        #     self.height()-9,
        #     self.height()-8);