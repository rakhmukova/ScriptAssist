from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from src.ui.dialogues.script_config_dialog import ScriptConfigDialog
from src.ui.widgets.editor_pane import EditorPane
from src.ui.widgets.line_number_area import LineNumberArea
from src.ui.widgets.output_pane import OutputPane


class MainWindow(QMainWindow):
    def __init__(self, start_config):
        super().__init__()

        self.setWindowTitle('ScriptAssist')
        self.setGeometry(200, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.current_config = start_config
        self.editor_pane = EditorPane(start_config)
        self.output_pane = OutputPane(start_config)

        self.line_number_area = LineNumberArea(self.editor_pane)
        self.line_number_area.setFixedWidth(50)
        self.editor_pane.blockCountChanged.connect(self.line_number_area.update_line_numbers)
        self.editor_pane.verticalScrollBar().valueChanged.connect(self.line_number_area.update_scrollbar)

        editor_layout = QHBoxLayout()
        editor_layout.addWidget(self.line_number_area)
        editor_layout.addWidget(self.editor_pane)

        layout.addLayout(editor_layout, stretch=2)
        layout.addWidget(self.output_pane, stretch=1)

        self.run_action = QAction('Run', self)
        self.run_action.setShortcut('Ctrl+R')
        self.run_action.triggered.connect(self.run_script)
        self.addAction(self.run_action)

        self.edit_config_action = QAction('Edit configuration', self)
        self.edit_config_action.setShortcut('Ctrl+E')
        self.edit_config_action.triggered.connect(self.edit_script_config)
        self.addAction(self.edit_config_action)

    def edit_script_config(self):
        config_dialog = ScriptConfigDialog(self.current_config)
        if config_dialog.exec():
            self.current_config = config_dialog.get_script_config()
            self.editor_pane.set_script_config(self.current_config)
            self.output_pane.set_script_config(self.current_config)

    def run_script(self):
        self.editor_pane.save_script()
        self.output_pane.run_script()
