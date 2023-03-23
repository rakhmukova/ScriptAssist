from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPlainTextEdit

from src.ui.widgets.editor_pane import EditorPane
from src.ui.widgets.output_pane import OutputPane


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ScriptAssist')
        self.setGeometry(200, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.editor_pane = EditorPane()
        self.output_pane = OutputPane()

        layout.addWidget(self.editor_pane, stretch=2)
        layout.addWidget(self.output_pane, stretch=1)
