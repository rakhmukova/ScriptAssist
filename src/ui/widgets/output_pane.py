from PyQt6.QtCore import pyqtSlot, pyqtSignal, QThreadPool
from PyQt6.QtWidgets import QTextEdit

from src.models.runner_factory import RunnerFactory
from src.models.script_runnable import ScriptRunnable


class OutputPane(QTextEdit):
    new_user_input = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('outputPane')

        self.output_cursor = self.textCursor()
        self.setReadOnly(True)

    def run_script(self, config):
        self.clear()

        script_runner = RunnerFactory.get_runner(config)
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
