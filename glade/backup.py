from PySide.QtCore import *
# from PySide.QtGui import *
# import os
# import time

# class WorkerSignals(QObject):

#     def __init__(self):
#         super(WorkerSignals, self).__init__()

#     result = Signal(bool)

# class Worker(QThread):
#     def __init__(self, path):
#         super(Worker, self).__init__()
#         print "Worker.__init__()"
#         self.path = path
#         self.signals = WorkerSignals()

#     def run(self):
#         print "Worker.run()"
#         time.sleep(1)
#         result = os.path.exists(self.path)
#         self.signals.result.emit(True)

# class Dispatcher(QObject):

#     def __init__(self, parent=None):
#         super(Dispatcher, self).__init__(parent=parent)
        
#         self.pool = QThreadPool.globalInstance()
#         self.pool.setMaxThreadCount(4)

#     @Slot(bool)
#     def process(self, result):
#         print "Dispatcher.process(): ", result

#     def start(self):
        
#         print "Dispatcher.start()"
#         plugin_paths = filter(None, os.getenv("MAYA_PLUG_IN_PATH").split(":"))
#         while(plugin_paths):
#             worker = Worker(plugin_paths.pop())
#             worker.signals.result.connect(self.process)
#             # self.pool.start(worker)
#             worker.start()

#         self.pool.waitForDone()

# class PluginManagerWindow(QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(PluginManagerWindow, self).__init__(*args, **kwargs)

#         layout = QVBoxLayout()
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#         button = QPushButton("Dispatch")
#         button.clicked.connect(self.dispatch)
#         layout.addWidget(button)

#         self.manager = None

#     @Slot()
#     def dispatch(self):
#         print "dispatch()"
#         dispatcher = Dispatcher()
#         dispatcher.start()

