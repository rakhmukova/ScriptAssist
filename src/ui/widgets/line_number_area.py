from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPlainTextEdit


class LineNumberArea(QPlainTextEdit):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.setReadOnly(True)
        self.update_line_numbers(self.text_edit.blockCount())

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def update_line_numbers(self, number):
        line_numbers = ''
        digits = len(str(number))
        for i in range(1, number + 1):
            line_numbers += str(i).rjust(digits) + '\n'

        self.setPlainText(line_numbers)

    def update_scrollbar(self, dy):
        self.verticalScrollBar().setValue(dy)
