from PySide.QtCore import *
from PySide.QtGui import *

from glade.ui import utils


class HighlightableLabel(QLabel):

    def __init__(self, parent=None):
        super(HighlightableLabel, self).__init__(parent=parent)
