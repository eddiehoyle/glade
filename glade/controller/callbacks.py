import os
from PySide.QtCore import *
from PySide.QtGui import *
from maya.OpenMaya import MSceneMessage

class CallbackController(QObject):

    plugin_loaded = Signal(str, str)
    plugin_unloaded = Signal(str, str)

    def __init__(self):
        super(CallbackController, self).__init__()

        self.callback_ids = []

    def register(self):
        self.callback_ids.append(
            MSceneMessage.addStringArrayCallback(
                MSceneMessage.kAfterPluginLoad,
                self.__plugin_loaded,
            )
        )
        self.callback_ids.append(
            MSceneMessage.addStringArrayCallback(
                MSceneMessage.kAfterPluginUnload,
                self.__plugin_unloaded,
            )
        )

    def unregister(self):
        while self.callback_ids:
            callback_id = self.callback_ids.pop()
            MSceneMessage.removeCallback(callback_id)

    def __plugin_loaded(self, string_array, client_data=None):
        plugin_path, plugin_name = string_array
        plugin_directory = os.path.dirname(plugin_path)
        self.plugin_loaded.emit(plugin_directory, plugin_name)
        # print "plugin_loaded() :", plugin_directory, plugin_name
        # __plugin_loaded ([u'/Applications/Autodesk/maya2016/Maya.app/Contents/MacOS/plug-ins/AutodeskPacketFile.bundle', u'AutodeskPacketFile'], None) {}

    def __plugin_unloaded(self, string_array, client_data=None):
        plugin_name, plugin_path = string_array
        plugin_directory = os.path.dirname(plugin_path)
        self.plugin_unloaded.emit(plugin_directory, plugin_name)
        # print "plugin_unloaded() :", plugin_directory, plugin_name
        # __plugin_unloaded ([u'AutodeskPacketFile.bundle', u'/Applications/Autodesk/maya2016/Maya.app/Contents/MacOS/plug-ins/AutodeskPacketFile.bundle'], None) {}

