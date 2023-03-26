from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPlainTextEdit


class LineNumberArea(QPlainTextEdit):
    def __init__(self, text_edit: QPlainTextEdit):
        """
        A custom widget that displays line numbers for a QPlainTextEdit widget.

        :param text_edit: The QPlainTextEdit widget for which to display line numbers.
        """
        super().__init__()
        self.__text_edit = text_edit
        self.setReadOnly(True)
        self.setObjectName('lineNumberArea')
        self.update_line_numbers(self.__text_edit.blockCount())

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def update_line_numbers(self, number: int):
        """
        Update the line numbers displayed in the LineNumberArea widget.

        :param number: The number of lines in the QPlainTextEdit widget.
        """
        line_numbers = ''
        digits = len(str(number))
        for i in range(1, number + 1):
            line_numbers += str(i).rjust(digits) + '\n'

        self.setPlainText(line_numbers)

    def update_scrollbar(self, dy: int):
        """
        Update the vertical scrollbar of the LineNumberArea widget.

        :param dy: The change in the vertical scrollbar value.
        """
        self.verticalScrollBar().setValue(dy)
