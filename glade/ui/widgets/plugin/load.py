from PySide.QtCore import *
from PySide.QtGui import *



class LabelledCheckboxWidget2(QFrame):
    """Not in use"""

    def __init__(self, label, parent=None):
        super(LabelledCheckboxWidget2, self).__init__(parent=parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.checkbox = QCheckBox(label)

        self.setObjectName("loadWidget")
        self.checkbox.setObjectName("loadCheckbox")

        layout.addWidget(self.checkbox)

        self.setMouseTracking(True)

    def check(self, state):
        self.checkbox.setChecked(state)

    def mouseMoveEvent(self, event):
        super(LabelledCheckboxWidget2, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(LabelledCheckboxWidget2, self).mousePressEvent(event)
        self.checkbox.setChecked(not self.checkbox.isChecked())

    def mouseReleaseEvent(self, event):
        super(LabelledCheckboxWidget2, self).mouseReleaseEvent(event)

    def enterEvent(self, event):
        super(LabelledCheckboxWidget2, self).enterEvent(event)
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        super(LabelledCheckboxWidget2, self).leaveEvent(event)
        self.unsetCursor()

