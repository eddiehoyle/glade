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
        self.is_autoload = cmds.pluginInfo(self.name, query=True, autoload=True)
        self.is_loaded = cmds.pluginInfo(self.name, query=True, loaded=True)
        self.commands = cmds.pluginInfo(self.name, query=True, command=True) or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def set_loaded(self, state):
        if state:
            cmds.loadPlugin(self.name)
        else:
            cmds.unloadPlugin(self.name)

    def set_autoload(self, state):
        cmds.pluginInfo(self.name, autoload=state, edit=True)

    def data(self):
        return {
            "Vendor": str(self.vendor),
            "Version": str(self.version),
            "Commands": ", ".join(self.commands),
        }