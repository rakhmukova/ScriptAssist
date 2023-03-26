from PyQt6.QtCore import QObject, pyqtSignal, QProcess


class ScriptRunner(QObject):
    new_output = pyqtSignal(str)
    new_error = pyqtSignal(str)
    finished = pyqtSignal(int)

    def __init__(self, interpreter_path, interpreter_options, script_path, parameters=None):
        super().__init__()
        self.interpreter_path = interpreter_path
        self.interpreter_options = interpreter_options
        self.script_path = script_path
        if parameters is None:
            parameters = []
        self.parameters = list(map(str, parameters))

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

    def run(self):
        self.process.start(self.interpreter_path,
                           self.interpreter_options + [self.script_path] + self.parameters)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode()
        self.new_error.emit(stderr)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode()
        self.new_output.emit(stdout)

    def process_finished(self, exit_code):
        self.finished.emit(exit_code)
