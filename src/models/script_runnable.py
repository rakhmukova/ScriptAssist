from PyQt6.QtCore import QRunnable


class ScriptRunnable(QRunnable):
    def __init__(self, script_runner):
        super().__init__()
        self.script_runner = script_runner

    def run(self):
        self.script_runner.run()
