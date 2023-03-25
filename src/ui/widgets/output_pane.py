from PyQt6.QtCore import pyqtSlot, pyqtSignal, QThreadPool
from PyQt6.QtWidgets import QTextEdit

from src.models.runner_factory import RunnerFactory
from src.models.script_runnable import ScriptRunnable


class OutputPane(QTextEdit):
    new_user_input = pyqtSignal(str)

    def __init__(self, start_config, parent=None):
        super().__init__(parent)
        self.current_config = None
        self.setObjectName('outputPane')

        self.set_script_config(start_config)
        self.output_cursor = self.textCursor()
        self.setReadOnly(True)

    def set_script_config(self, script_config):
        self.current_config = script_config
        self.clear()

    def run_script(self):
        self.clear()

        script_runner = RunnerFactory.get_runner(self.current_config)
        script_runner.new_output.connect(self.display_stdout)
        script_runner.new_error.connect(self.display_stderr)

        script_runnable = ScriptRunnable(script_runner)
        pool = QThreadPool.globalInstance()
        pool.start(script_runnable)

    @pyqtSlot(str)
    def display_stdout(self, output):
        self.append(output)

    @pyqtSlot(str)
    def display_stderr(self, error):
        self.append(error)

    def handle_finish(self):
        pass
