from maya import cmds
from functools import partial

class Plugin(object):

    def __init__(self, name):
        super(Plugin, self).__init__()

        if not cmds.pluginInfo(name, query=True, registered=True):
            raise NameError("Plugin not registered: %s" % name)

        self.name = name
        self.path = cmds.pluginInfo(self.name, query=True, path=True)
        self.vendor = cmds.pluginInfo(self.name, query=True, vendor=True)
        self.version = cmds.pluginInfo(self.name, query=True, version=True)
        self.for_api_version = cmds.pluginInfo(self.name, query=True, apiVersion=True)
        self.is_autoload = cmds.pluginInfo(self.name, query=True, autoload=True)
        self.is_loaded = cmds.pluginInfo(self.name, query=True, loaded=True)
        self.commands = cmds.pluginInfo(self.name, query=True, command=True) or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def data(self):
        return {
            # "name": str(self.name),
            # "path": str(self.path),
            "vendor": str(self.vendor),
            "version": str(self.version),
            "for_api_version": str(self.for_api_version),
            # "is_autoload": str(self.is_autoload),
            # "is_loaded": str(self.is_loaded),
            "commands": ", ".join(self.commands),
        }