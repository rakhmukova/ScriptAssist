from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPlainTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ScriptAssist')
        self.setGeometry(200, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.setLayout(layout)

        self.editor_pane = QPlainTextEdit()
        self.output_pane = QTextEdit()

        layout.addWidget(self.editor_pane, stretch=2)
        layout.addWidget(self.output_pane, stretch=1)
