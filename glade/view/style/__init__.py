from PySide.QtCore import *
from PySide.QtGui import *

class AbstractPluginStyle(object):

    HEADER_MARGIN = 0
    HEADER_SPACING = 0

    BODY_MARGIN = 0
    BODY_SPACING = 0

    MARGIN = 0
    SPACING = 0

class PluginItemStyle(AbstractPluginStyle):
    pass

class PluginSectionStyle(AbstractPluginStyle):
    pass

def compile():
    data = []
    # QFile file(":/qss/style.qss");
    # if(file.open(QFile::ReadOnly)) {
    #    QString StyleSheet = QLatin1String(file.readAll());
    #    qApp->setStyleSheet(StyleSheet);
    # }
    qss_file = QFile(":/qss/section.qss")
    with open("section.qss", "r") as f:
        data = f.readlines()
    return "".join()

SECTION_STYLESHEET = """
QFrame#sectionHeader {
    background-color: rgb(120, 120, 120);
    margin: 0px;
    padding: 5px;
}
QFrame#sectionBody {
    background-color: rgb(80, 80, 80);
    margin: 0px;
    padding: 5px;
}
"""