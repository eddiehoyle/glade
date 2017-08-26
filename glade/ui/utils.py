from PySide.QtCore import *
from PySide.QtGui import *

def colorbg(cls, color):
    pal = QPalette()
    pal.setColor(QPalette.Background, color);
    cls.setAutoFillBackground(True);
    cls.setPalette(pal);

def randombg(cls):
    import random
    gen = lambda: random.randint(0,255)
    hexcode = "#%02X%02X%02X" % (gen(),gen(),gen())
    pal = QPalette()
    pal.setColor(QPalette.Background, hexcode);
    cls.setAutoFillBackground(True);
    cls.setPalette(pal);