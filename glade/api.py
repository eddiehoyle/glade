
import os
from maya import cmds
from glade.model.plugin import Plugin

def get_plugin_directories():
    """
    """

    return os.getenv("MAYA_PLUG_IN_PATH", "").split(":")

def get_plugin_files(directory):
    """
    """

    if not os.path.exists(directory) or not os.path.isdir(directory):
        return []

    plugin_extensions = [".bundle", ".py", ".so"]
    
    files = []
    for filename in os.listdir(directory):

        # Skip '__' named  files
        if filename.startswith("__"):
            continue

        # Check legal extensions
        extension = os.path.splitext(filename)[-1]
        if extension in plugin_extensions:
            files.append(filename)

    return files

def get_plugins(directory):
    """
    """

    plugins = []
    files = get_plugin_files(directory)
    for filename in files:
        try:
            plugin = Plugin(filename, directory)
            plugins.append(plugin)
        except NameError as exc:
            pass
    return plugins

def get_all_plugins():
    """
    """

    plugins = []
    directories = get_plugin_directories()
    for directory in directories:
        plugins.extend(get_plugins(directory))
    return plugins