from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTextEdit, QWidget

from models.interpreter_factory import InterpreterFactory
from models.script_config import ScriptConfig
from models.script_runner import ScriptRunner


class OutputPane(QTextEdit):
    """
    A QTextEdit widget that displays output from running a script.
    """
    script_finished = pyqtSignal(int)

    def __init__(self, parent: QWidget = None):
        """
        Creates a new OutputPane instance.

        :param parent: The parent widget of the OutputPane.
        """
        super().__init__(parent)
        self.__script_runner = None
        self.__current_config = None
        self.setObjectName('outputPane')
        self.setReadOnly(True)

    def on_config_changed(self, script_config: ScriptConfig):
        """
        Sets the configuration for the script to be run.

        :param script_config: The script configuration to set.
        """
        self.__current_config = script_config
        self.clear()

    def run_script(self):
        """
        Runs the script using the configuration set by set_script_config().
        """
        if self.__script_runner is None:
            self.clear()
            try:
                script_config = self.__current_config
                interpreter_config = InterpreterFactory.get_interpreter_config(script_config)
                self.__script_runner = ScriptRunner(interpreter_config, script_config)
                self.__script_runner.stderr_received.connect(self.__handle_run_error)
                self.__script_runner.stdout_received.connect(self.__handle_output)
                self.__script_runner.finished.connect(self.__handle_finish)
                self.__script_runner.run()
            except ValueError as e:
                self.__handle_start_error(e)

    def stop_script(self):
        """
        Stops the currently running script.
        """
        if self.__script_runner is not None:
            self.__script_runner.cancel()
            self.__script_runner = None

    def rerun_script(self):
        """
        Stops the currently running script and then runs it again.
        """
        self.stop_script()
        self.run_script()

    def __handle_run_error(self, error: str):
        self.append(error)

    def __handle_output(self, output: str):
        self.append(output)

    def __handle_finish(self, exit_code: int):
        self.__script_runner = None
        self.script_finished.emit(exit_code)

    def __handle_start_error(self, error: ValueError):
        self.script_finished.emit(1)
        self.append(str(error))
