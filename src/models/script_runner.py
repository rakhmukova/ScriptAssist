from PyQt6.QtCore import QObject, pyqtSignal, QProcess

from models.interpreter_config import InterpreterConfig
from models.script_config import ScriptConfig


class ScriptRunner(QObject):
    """
    Runs scripts using an interpreter specified by the user.
    """
    stdout_received = pyqtSignal(str)
    stderr_received = pyqtSignal(str)
    finished = pyqtSignal(int)

    def __init__(self, interpreter_config: InterpreterConfig, script_config: ScriptConfig):
        """
        Creates a new ScriptRunner instance.
        :param interpreter_config: The interpreter configuration.
        :param script_config: The script configuration.
        """
        super().__init__()

        self.__interpreter_config = interpreter_config
        self.__script_config = script_config

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.__handle_stdout)
        self.process.readyReadStandardError.connect(self.__handle_stderr)
        self.process.finished.connect(self.__process_finished)

    def run(self):
        """
        Starts running the script.
        """
        program = self.__interpreter_config.path
        args = self.__interpreter_config.options + [self.__script_config.path] + self.__script_config.parameters
        self.process.start(program, args)

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
