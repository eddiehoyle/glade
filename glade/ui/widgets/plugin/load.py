from PySide.QtCore import *
from PySide.QtGui import *


class LabelledChecboxWidget(QFrame):

    def __init__(self, label, parent=None):
        super(LabelledChecboxWidget, self).__init__(parent=parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.checkbox = QCheckBox()
        self.label = QLabel(label)

        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)

        self.setMouseTracking(True)

        self.setObjectName("loadCheckbox")

    def mouseMoveEvent(self, event):
        super(LabelledChecboxWidget, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(LabelledChecboxWidget, self).mousePressEvent(event)
        self.checkbox.setChecked(not self.checkbox.isChecked())

    def mouseReleaseEvent(self, event):
        super(LabelledChecboxWidget, self).mouseReleaseEvent(event)

    def enterEvent(self, event):
        super(LabelledChecboxWidget, self).enterEvent(event)
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        super(LabelledChecboxWidget, self).leaveEvent(event)
        self.unsetCursor()

