
from PySide.QtCore import *
from PySide.QtGui import *

from functools import partial

from glade import api

from maya.OpenMaya import MSceneMessage

from Queue import Queue
import datetime

DEBUG = True

def sprint(content):
    if DEBUG:
        print("{0} ~ {1}\n".format(str(datetime.datetime.now()), content))  
    # sys.stdout.write("{0} ~ {1}\n".format(str(datetime.datetime.now()), content))
    # sys.stdout.flush()


class Worker(QThread):

    finished = Signal()
    plugin_added = Signal(str, str)

    def __init__(self, directories, parent=None):
        super(Worker, self).__init__(parent=parent)

        self.directories = directories
        self.is_working = False

    def start(self):
        super(Worker, self).start()
        self.is_working = True

    def run(self):
        while self.is_working:
            directory = self.directories.get()
            plugins = api.get_plugins(directory)
            for plugin in plugins:
                self.plugin_added.emit(plugin.name, directory)
        self.finished.emit()

    @Slot()
    def terminate(self):
        self.is_working = False
        super(Worker, self).terminate()
        sprint("Worker.terminate()")


class Dispatcher(QObject):

    plugin_added = Signal(str, str)

    def __init__(self, parent=None):
        super(Dispatcher, self).__init__(parent=parent)

        self.queue = Queue()

        NUM_THREADS = 4

        self.threads = []
        for index in range(NUM_THREADS):
            worker = Worker(self.queue)
            worker.plugin_added.connect(self.plugin_added)
            self.threads.append(worker)

    # def plugin_added(self, plugin, directory):
    #     print plugin, directory

    def put_directory(self, directory):
        self.queue.put(directory)

    def start(self):
        sprint("Dispatcher.start()")

        for thread in self.threads:
            thread.start()

    def stop(self):
        for thread in self.threads:
            thread.terminate()



class PluginController(QObject):

    directory_added = Signal(str)

    plugin_added = Signal(str, str)
    plugin_loaded = Signal(str, str)
    plugin_unloaded = Signal(str, str)

    def __init__(self):
        super(PluginController, self).__init__()

        self.dispatcher = Dispatcher()
        self.dispatcher.plugin_added.connect(self.plugin_added)
        self.directory_added.connect(self.dispatcher.put_directory)

        self.plugin_added.connect(self.debug)

        self.callback_ids = []

    def debug(self, *args):
        print "debug:", args
        # sprint(args)

    def initialise(self):
        # self.callback_ids.append(
        #     MSceneMessage.addStringArrayCallback(
        #         MSceneMessage.kAfterPluginLoad,
        #         self.__plugin_loaded,
        #     )
        # )
        # self.callback_ids.append(
        #     MSceneMessage.addStringArrayCallback(
        #         MSceneMessage.kAfterPluginUnload,
        #         self.__plugin_unloaded,
        #     )
        # )

        self.dispatcher.start()

        directories = api.get_plugin_directories()
        while directories:
            self.directory_added.emit(directories.pop())

        print "initialise() : Added callbacks:", len(self.callback_ids)

    def teardown(self):
        print "teardown() : Removing callbacks", len(self.callback_ids)
        while  self.callback_ids:
            callback_id = self.callback_ids.pop()
            MSceneMessage.removeCallback(callback_id)

        self.dispatcher.stop.emit()

    def __plugin_loaded(self, array, data):
        print "__plugin_loaded", array, data
        plugin_name, plugin_directory = array
        self.plugin_loaded.emit(plugin_name, plugin_directory)
        # __plugin_loaded ([u'/Applications/Autodesk/maya2016/Maya.app/Contents/MacOS/plug-ins/AutodeskPacketFile.bundle', u'AutodeskPacketFile'], None) {}


    def __plugin_unloaded(self, array, data):
        print "__plugin_unloaded", array, data
        plugin_name, plugin_directory = array
        self.plugin_unloaded.emit(plugin_name, plugin_directory)
        # __plugin_unloaded ([u'AutodeskPacketFile.bundle', u'/Applications/Autodesk/maya2016/Maya.app/Contents/MacOS/plug-ins/AutodeskPacketFile.bundle'], None) {}

