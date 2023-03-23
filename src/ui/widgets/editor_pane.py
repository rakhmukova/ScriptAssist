from PyQt6.QtWidgets import QPlainTextEdit


class EditorPane(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('editorPane')
