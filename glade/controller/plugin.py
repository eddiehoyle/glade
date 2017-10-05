import os
import time
import datetime
from Queue import Queue

from PySide.QtCore import *
from PySide.QtGui import *

from glade import api
from glade.plugin import Plugin


def sprint(content):
    print("{0} ~ {1}".format(str(datetime.datetime.now()), content))  


class Worker(QThread):

    plugin_found = Signal(str, str)

    def __init__(self, directories, index, parent=None):
        super(Worker, self).__init__(parent=parent)

        self.index = index
        self.queue = directories

        self.__is_running = False

    def __str__(self):
        return "<class Worker(id={0}, running={1})>".format(
            self.index, self.__is_running
        )

    def start(self):
        super(Worker, self).start()
        self.__is_running = True
        sprint("start() : id=%s" % self.index)

    def quit(self):
        self.__is_running = False
        super(Worker, self).quit()
        sprint("quit() : id=%s" % self.index)

    def run(self):
        # sprint("Worker.run() : (%s)" % self.index)

        while self.__is_running:

            if self.queue.empty():
                # sprint("Worker.run() : (%s) sleeping..." % (self.index))
                time.sleep(0.1)
                continue

            directory = self.queue.get()
            # sprint("Worker.run() : (%s) scanning: %s" % (self.index, directory))
            plugins = api.get_plugins(directory)
            for plugin in plugins:
                # sprint("Worker.run() : (%s) found: %s" % (self.index, plugin))
                self.plugin_found.emit(directory, plugin)

        # sprint("Worker.run() : (%s) Done!" % (self.index))


class PluginController(QObject):

    plugin_found = Signal(str, str)

    def __init__(self):
        super(PluginController, self).__init__()

        self.queue = Queue()

        thread_count = max(1, QThread.idealThreadCount() - 1)

        self.threads = []
        for index in range(thread_count):
            thread = Worker(self.queue, index)
            thread.plugin_found.connect(self.plugin_found)
            self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            thread.start()

    def stop(self):
        for thread in self.threads:
            thread.quit()

        # for thread in self.threads:
        #     thread.wait()

    def terminate(self):
        for thread in self.threads:
            thread.terminate()

    def add_directories(self, directories):
        for directory in directories:
            self.add_directory(directory)

    def add_directory(self, directory):
        self.queue.put(directory)

