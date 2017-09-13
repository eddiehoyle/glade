from PySide.QtCore import *
from PySide.QtGui import *

class AbstractPluginStyle(object):

    HEADER_MARGIN = 5
    HEADER_SPACING = 0

    BODY_MARGIN = 5
    BODY_SPACING = 0

class PluginItemStyle(AbstractPluginStyle):

    MARGIN = 0
    SPACING = 0

    BODY_SPACING = 5

class PluginSectionStyle(AbstractPluginStyle):

    MARGIN = 0
    SPACING = 0

    BODY_MARGIN = 0
    HEADER_MARGIN = 8
