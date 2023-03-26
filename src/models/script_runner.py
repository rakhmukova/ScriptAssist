from PyQt6.QtCore import QObject, pyqtSignal, QProcess


class ScriptRunner(QObject):
    """
    Runs scripts using an interpreter specified by the user.
    """
    stdout_received = pyqtSignal(str)
    stderr_received = pyqtSignal(str)
    finished = pyqtSignal(int)

    def __init__(self, interpreter_path: str, interpreter_options: list, script_path: str,
                 parameters: list = None):
        """
        Creates a new ScriptRunner instance.

        :param interpreter_path: The path to the interpreter that should be used to run the script.
        :param interpreter_options: The options to pass to the interpreter when running the script.
        :param script_path: The path to the script file.
        :param parameters: Any additional parameters to pass to the script.
        """
        super().__init__()
        if parameters is None:
            parameters = []

        self.program = interpreter_path
        self.args = interpreter_options + [script_path] + [str(param) for param in parameters]

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.__handle_stdout)
        self.process.readyReadStandardError.connect(self.__handle_stderr)
        self.process.finished.connect(self.__process_finished)

    def run(self):
        """
        Starts running the script.
        """
        self.process.start(self.program, self.args)

    def cancel(self):
        """
        Cancels the currently running script.
        """
        self.process.terminate()
        self.process.waitForFinished()

    def __handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode()
        self.stderr_received.emit(stderr)

    def __handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode()
        self.stdout_received.emit(stdout)

    def __process_finished(self, exit_code: int):
        self.finished.emit(exit_code)
        self.process.deleteLater()
        self.process = None
