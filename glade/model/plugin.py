from maya import cmds
from functools import partial

class Plugin(object):

    def __init__(self, filename, directory=None):
        super(Plugin, self).__init__()

        if not cmds.pluginInfo(filename, query=True, registered=True):
            raise NameError("Plugin not registered: %s" % filename)

        self.filename = filename
        self.directory = directory
        self.is_autoload = cmds.pluginInfo(self.filename, query=True, autoload=True)
        self.is_loaded = cmds.pluginInfo(self.filename, query=True, loaded=True)

        self.name = None
        self.path = None
        self.vendor = None
        self.version = None
        self.commands = None

        if self.is_loaded:
            self.name = cmds.pluginInfo(self.filename, query=True, name=True)
            self.path = cmds.pluginInfo(self.filename, query=True, path=True)
            self.vendor = cmds.pluginInfo(self.filename, query=True, vendor=True)
            self.version = cmds.pluginInfo(self.filename, query=True, version=True)
            self.commands = cmds.pluginInfo(self.filename, query=True, command=True) or []

    def __str__(self):
        return "<class Plugin(name='{0}')>".format(self.name)

    def set_loaded(self, state):
        if state:
            cmds.loadPlugin(self.filename)
        else:
            cmds.unloadPlugin(self.filename)

    def set_autoload(self, state):
        cmds.pluginInfo(self.name, autoload=state, edit=True)

    def data(self):
        return {
            "Vendor": str(self.vendor),
            "Version": str(self.version),
            "Commands": ", ".join(self.commands),
        }