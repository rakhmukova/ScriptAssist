from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPlainTextEdit

from src.ui.dialogues.script_config_dialog import ScriptConfigDialog
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

        self.run_action = QAction('Run', self)
        self.run_action.setShortcut('Ctrl+R')
        self.run_action.triggered.connect(self.output_pane.run_script)
        self.addAction(self.run_action)

        self.edit_config_action = QAction('Edit configuration', self)
        self.edit_config_action.setShortcut('Ctrl+E')
        self.edit_config_action.triggered.connect(self.edit_script_config)
        self.addAction(self.edit_config_action)

        self.current_config = None

    def edit_script_config(self):
        config_dialog = ScriptConfigDialog()
        config_dialog.exec()
        self.current_config = config_dialog.get_script_config()
