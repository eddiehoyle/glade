
class Worker(QObject):

    start = Signal()
    done = Signal()
    result = Signal(bool)

    def __init__(self, path, parent=None):
        super(Worker, self).__init__(parent=parent)
        self.path = path
        self.start.connect(self.process)
        self.is_quitting = False

    @Slot()
    def process(self):
        sprint("Worker.process() : path=%s" % (self.path))
        while not self.is_quitting:
            time.sleep(2)
            if not self.is_quitting:
                self.result.emit(os.path.exists(self.path))
                self.quit()
        self.done.emit()

    @Slot()
    def quit(self):
        self.is_quitting = True


class WorkerThread(QThread):

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent=parent)

    def __del__(self):
        self.wait()


# class WorkerController(QObject):

#     result = Signal(bool)

#     def __init__(self, parent=None):
#         super(WorkerController, self).__init__(parent=parent)

#         self.thread = WorkerThread()
#         self.worker = None

#     def is_available(self):
#         return not self.thread.isRunning()

#     def start(self, path):
#         sprint("WorkerController.start() : path=%s" % path)
#         if self.thread.isRunning():
#             return

#         self.worker = Worker(path)
#         self.thread.started.connect(self.worker.start)
#         self.worker.result.connect(self.result)
#         self.worker.done.connect(self.stop)
#         self.worker.moveToThread(self.thread)
#         self.thread.start()

#     @Slot()
#     def stop(self):
#         sprint("WorkerController.stop()")
#         self.worker.quit()
#         self.thread.quit()
#         self.thread.wait()

#     def poll(self):
#         sprint("WorkerController.poll()")


class WorkerThread2(QThread):

    result = Signal(list)

    def __init__(self, directory, parent=None):
        super(WorkerThread2, self).__init__(parent=parent)

        self.directory = directory

    def __del__(self):
        self.wait()

    def run(self):
        sprint("WorkerThread2.run()")
        plugins = api.get_plugins(self.directory)
        time.sleep(random.random())
        self.result.emit(plugins)


class WorkerController2(QObject):

    result = Signal(list)

    def __init__(self, directory, parent=None):
        super(WorkerController2, self).__init__(parent=parent)

        self.thread = WorkerThread2(directory)
        self.thread.result.connect(self.result)

    def is_available(self):
        return not self.thread.isRunning()

    def start(self):
        sprint("WorkerController2.start()")
        self.thread.start()

    @Slot()
    def stop(self):
        sprint("WorkerController2.stop()")
        self.thread.quit()


class Dispatcher(QObject):

    result = Signal(list)

    def __init__(self, parent=None):
        super(Dispatcher, self).__init__(parent=parent)

        cpus = 8
        self.controllers = {}

    def start(self):

        self.directories = api.get_plugin_directories()

        if not self.directories:
            return

        count = 0
        while self.directories:
            directory = self.directories.pop()
            self.controllers[count] = WorkerController2(directory)
            self.controllers[count].result.connect(self.result)
            self.controllers[count].start()
            count += 1
