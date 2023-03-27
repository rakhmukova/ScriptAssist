from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from src.ui.dialogues.script_config_dialog import ScriptConfigDialog
from src.ui.widgets.editor_pane import EditorPane
from src.ui.widgets.line_number_area import LineNumberArea
from src.ui.widgets.output_pane import OutputPane
from src.ui.widgets.top_panel import TopPanel


class MainWindow(QMainWindow):
    def __init__(self, start_config):
        super().__init__()

        self.current_config = None

        self.setWindowTitle('ScriptAssist')
        self.setGeometry(200, 100, 800, 600)

        central_widget = QWidget()
        central_widget.setObjectName('centralWidget')
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.top_panel = TopPanel()
        self.top_panel.run_button.clicked.connect(self.run_script)
        self.top_panel.stop_button.clicked.connect(self.stop_script)
        self.top_panel.edit_config_button.clicked.connect(self.edit_script_config)

        self.editor_pane = EditorPane()

        self.line_number_area = LineNumberArea(self.editor_pane)
        self.line_number_area.setFixedWidth(50)
        self.editor_pane.blockCountChanged.connect(self.line_number_area.update_line_numbers)
        self.editor_pane.verticalScrollBar().valueChanged.connect(self.line_number_area.update_scrollbar)

        self.run_indication_label = QLabel()
        self.run_indication_label.setObjectName('runIndicationLabel')
        self.run_indication_label.setFixedHeight(25)

        self.output_pane = OutputPane()
        self.output_pane.script_finished.connect(self.show_finish_result)

        self.create_layout(layout)

        self.run_action = None
        self.stop_action = None
        self.edit_config_action = None
        self.create_actions()

        self.set_script_config(start_config)

    def create_layout(self, layout):
        editor_layout = QHBoxLayout()
        editor_layout.setSpacing(0)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.addWidget(self.line_number_area)
        editor_layout.addWidget(self.editor_pane)

        layout.addWidget(self.top_panel)
        layout.addLayout(editor_layout, stretch=2)
        layout.addWidget(self.run_indication_label)
        layout.addWidget(self.output_pane, stretch=1)

    def create_actions(self):
        self.run_action = QAction('Run', self)
        self.run_action.setShortcut('Ctrl+R')
        self.run_action.triggered.connect(self.run_script)
        self.addAction(self.run_action)

        self.stop_action = QAction('Stop', self)
        self.stop_action.setShortcut('Ctrl+T')
        self.stop_action.triggered.connect(self.stop_script)
        self.addAction(self.stop_action)

        self.edit_config_action = QAction('Edit configuration', self)
        self.edit_config_action.setShortcut('Ctrl+E')
        self.edit_config_action.triggered.connect(self.edit_script_config)
        self.addAction(self.edit_config_action)

    def set_script_config(self, config):
        self.current_config = config
        self.editor_pane.set_script_config(config)
        self.output_pane.set_script_config(config)

        file_name = config.path.split('/')[-1]
        self.top_panel.script_name_label.setText(file_name)

        self.run_indication_label.setText('Ready')
        self.run_indication_label.setStyleSheet('color: black')

    def edit_script_config(self):
        config_dialog = ScriptConfigDialog(self.current_config)
        if config_dialog.exec():
            config = config_dialog.get_script_config()
            self.set_script_config(config)

    def run_script(self):
        self.editor_pane.save_script()
        self.output_pane.run_script()
        self.run_indication_label.setText('Running...')
        self.run_indication_label.setStyleSheet('color: black')

    def stop_script(self):
        self.output_pane.stop_script()

    def show_finish_result(self, exit_code):
        if exit_code != 0:
            self.run_indication_label.setStyleSheet('color: darkred')

        self.run_indication_label.setText(f'Finished with exit code {exit_code}')
