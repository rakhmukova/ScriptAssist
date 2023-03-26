from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTextEdit

from src.models.runner_factory import RunnerFactory


class OutputPane(QTextEdit):
    script_finished = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.script_runner = None
        self.current_config = None
        self.setObjectName('outputPane')

        self.output_cursor = self.textCursor()
        self.setReadOnly(True)

    def set_script_config(self, script_config):
        self.current_config = script_config
        self.clear()

    def run_script(self):
        if self.script_runner is None:
            self.clear()
            self.script_runner = RunnerFactory.get_runner(self.current_config)
            self.script_runner.new_error.connect(self.handle_error)
            self.script_runner.new_output.connect(self.handle_output)
            self.script_runner.finished.connect(self.handle_finish)
            self.script_runner.run()

    def stop_script(self):
        if self.script_runner is not None:
            self.script_runner.cancel()
            self.script_runner = None

    def rerun_script(self):
        self.stop_script()
        self.run_script()

    def handle_error(self, error):
        self.append(error)

    def handle_output(self, output):
        self.append(output)

    def handle_finish(self, exit_code):
        self.script_runner = None
        self.script_finished.emit(exit_code)
