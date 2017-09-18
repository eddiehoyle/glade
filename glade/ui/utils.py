from PySide.QtCore import *
from PySide.QtGui import *

def colorbg(cls, color):
    pass
    # pal = QPalette()
    # pal.setColor(QPalette.Background, color);
    # cls.setAutoFillBackground(True);
    # cls.setPalette(pal);

def randombg(cls):
    pass
    # import random
    # gen = lambda: random.randint(0,255)
    # hexcode = "#%02X%02X%02X" % (gen(),gen(),gen())
    # pal = QPalette()
    # pal.setColor(QPalette.Background, hexcode);
    # cls.setAutoFillBackground(True);
    # cls.setPalette(pal);

def read_stylesheet(path):
    """"""

    stylesheet_file = QFile(path)
    if stylesheet_file.open(QIODevice.ReadOnly | QFile.Text):
        stream = QTextStream(stylesheet_file)
        document = ""
        while not stream.atEnd():
            document += stream.readLine()
    stylesheet_file.close()
    return document