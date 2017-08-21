from itertools import cycle
from PySide.QtCore import *
from PySide.QtGui import *

import api

import os
import sys
import time
import random
import datetime
import threading
from Queue import Queue

DEBUG = True

def sprint(content):
    if DEBUG:
        print("{0} ~ {1}\n".format(str(datetime.datetime.now()), content))  
    # sys.stdout.write("{0} ~ {1}\n".format(str(datetime.datetime.now()), content))
    # sys.stdout.flush()


class Worker(QThread):

    result = Signal(list)
    done = Signal()

    def __init__(self, directories, parent=None):
        super(Worker, self).__init__(parent=parent)
        self.queue = directories
        self.finished.connect(self.done)

    def run(self):
        sprint("Worker.run()")
        while not self.queue.empty():
            plugins = api.get_plugins(self.queue.get())
            time.sleep(random.random())
            self.result.emit(plugins)
        self.finished.emit()

    def done(self):
        sprint("Worker.done() : isRunning=%s" % self.isRunning())

    @Slot()
    def terminate(self):
        super(Worker, self).terminate()
        sprint("Worker.terminate()")


class Dispatcher(QObject):

    result = Signal(list)

    def __init__(self, parent=None):
        super(Dispatcher, self).__init__(parent=parent)

        self.queue = Queue()

        self.threads = []
        for index in range(QThread.idealThreadCount()):
            worker = Worker(self.queue)
            worker.result.connect(self.result)
            self.threads.append(worker)

    def start(self):
        sprint("Dispatcher.start()")

        directories = api.get_plugin_directories()
        while directories:
            self.queue.put(directories.pop())

        for thread in self.threads:
            thread.start()

    def stop(self):
        for thread in self.threads:
            thread.terminate()


class PluginManagerWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PluginManagerWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start)
        layout.addWidget(start_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        layout.addWidget(clear_button)

        poll_button = QPushButton("Poll")
        poll_button.clicked.connect(self.poll)
        layout.addWidget(poll_button)

        self.tree = QTreeWidget()
        layout.addWidget(self.tree)

        self.dispatcher = Dispatcher()
        self.dispatcher.result.connect(self.add_result)

    @Slot()
    def add_result(self, result):
        if not result:
            return
        for res in result:
            sprint("Dispatcher.add_result()")
            widget = QTreeWidgetItem()
            text = "%s\n%s\n%s" % (res.vendor, res.name, res.path)
            widget.setText(0, text)
            self.tree.insertTopLevelItem(0, widget)

    @Slot()
    def start(self):
        self.dispatcher.start()

    @Slot()
    def clear(self):
        self.dispatcher.stop()
        self.tree.clear()
        # self.tree = QTreeView()
        # self.model = QStandardItemModel()
        # self.tree.setModel(self.model)
        # self.dispatcher.stop()

    @Slot()
    def poll(self):
        self.dispatcher.poll()


