import select
from subprocess import Popen, PIPE

from PyQt6.QtCore import QObject, pyqtSignal


class ScriptRunner(QObject):
    new_output = pyqtSignal(str)
    new_error = pyqtSignal(str)
    process_finished = pyqtSignal(int)

    def __init__(self, interpreter_path, interpreter_options, script_path, parameters=None):
        super().__init__()
        self.interpreter_path = interpreter_path
        self.interpreter_options = interpreter_options
        self.script_path = script_path
        if parameters is None:
            parameters = []
        self.parameters = list(map(str, parameters))
        self.process = None

    def start_process(self):
        self.process = Popen([self.interpreter_path] + self.interpreter_options + [self.script_path] + self.parameters,
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)

    def handle_stdout_and_stderr(self):
        stdout = self.process.stdout
        stderr = self.process.stderr

        to_break = False
        while not to_break:
            ready, _, _ = select.select([stdout, stderr], [], [], 0.1)
            if ready:
                for stream in ready:
                    if stream == stdout:
                        output = stdout.readline()
                        if output.decode() == '':
                            to_break = True
                        self.new_output.emit(output.strip().decode())
                    elif stream == stderr:
                        error = stderr.readline()
                        self.new_error.emit(error.strip().decode())

        stdout.close()
        stderr.close()
        exit_code = self.process.wait()
        self.process_finished.emit(exit_code)

    def run(self):
        self.start_process()
        self.handle_stdout_and_stderr()
