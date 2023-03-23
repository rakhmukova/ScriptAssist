from PyQt6.QtWidgets import QTextEdit


class OutputPane(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('outputPane')
