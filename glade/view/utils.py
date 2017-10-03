from PySide.QtCore import *
from PySide.QtGui import *
import gc
import sys

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

    document = ""
    stylesheet_file = QFile(path)
    if stylesheet_file.open(QIODevice.ReadOnly | QFile.Text):
        stream = QTextStream(stylesheet_file)
        while not stream.atEnd():
            document += stream.readLine()
    stylesheet_file.close()
    return document

def flush(name):
    '''
    flushes all loaded modules from sys.modules which causes them to be reloaded
    when next imported...  super useful for developing crap within a persistent
    python environment
    '''

    flush_keys = []
    for mod_name, mod_obj in sys.modules.items():

        try:
            mod_obj.__file__
        except AttributeError:
            continue

        if name in mod_name:
            flush_keys.append(mod_name)

    count = 0
    for key in flush_keys:
        count += 1
        del( sys.modules[key] )

    print "Flushed %s module(s)" % count

    gc.collect()  #force a garbage collection