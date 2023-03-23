from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import QTextEdit


class OutputPane(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('outputPane')

        self.output_cursor = self.textCursor()

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.display_stdout)
        self.process.readyReadStandardError.connect(self.display_stderr)
        self.process.finished.connect(self.handle_finish)

        self.setReadOnly(True)

        self.previous_text_length = 0

    def run_script(self):
        self.clear()
        self.setReadOnly(False)
        self.textChanged.connect(self.input_stdin)

        scripts_path = '../example_scripts/swift/'
        script_file = 'hello_world'
        self.process.start('/usr/bin/env', ['swift', scripts_path + script_file + '.swift'])

    def display_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.append(output)
        self.previous_text_length += len(output)

    def display_stderr(self):
        error = self.process.readAllStandardError().data().decode()
        self.append(error)
        self.previous_text_length += len(error)

    def input_stdin(self):
        current_text = self.toPlainText()
        current_text_length = len(current_text)

        new_text = current_text[self.previous_text_length:]
        if new_text:
            self.process.write(new_text.encode())

        self.previous_text_length = current_text_length

    def handle_finish(self):
        self.textChanged.disconnect(self.input_stdin)
        self.setReadOnly(True)
