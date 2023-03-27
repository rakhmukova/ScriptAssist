from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from src.models.script_config import ScriptConfig
from src.ui.dialogues.script_config_dialog import ScriptConfigDialog
from src.ui.widgets.editor_pane import EditorPane
from src.ui.widgets.line_number_area import LineNumberArea
from src.ui.widgets.output_pane import OutputPane
from src.ui.widgets.script_status_label import ScriptStatusLabel
from src.ui.widgets.top_panel import TopPanel


class MainWindow(QMainWindow):
    config_changed = pyqtSignal(object)

    def __init__(self, start_config: ScriptConfig):
        """
        Constructor for the main window of the ScriptAssist application.

        Args:
            start_config: The configuration of the script to be loaded on startup.
        """
        super().__init__()

        self.__script_config = None

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

        self.script_status_label = ScriptStatusLabel()
        self.script_status_label.setObjectName('scriptStatusLabel')
        self.script_status_label.setFixedHeight(25)

        self.output_pane = OutputPane()
        self.output_pane.script_finished.connect(self.script_status_label.show_finish_status)

        self.create_layout(layout)

        self.run_action = None
        self.stop_action = None
        self.edit_config_action = None
        self.create_actions()

        self.subscribe_to_config_change()
        self.script_config = start_config

    def create_layout(self, layout: QVBoxLayout):
        editor_layout = QHBoxLayout()
        editor_layout.setSpacing(0)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.addWidget(self.line_number_area)
        editor_layout.addWidget(self.editor_pane)

        layout.addWidget(self.top_panel)
        layout.addLayout(editor_layout, stretch=2)
        layout.addWidget(self.script_status_label)
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

    def subscribe_to_config_change(self):
        signaled = self.config_changed
        signaled.connect(self.editor_pane.on_config_changed)
        signaled.connect(self.output_pane.on_config_changed)
        signaled.connect(self.top_panel.on_config_changed)
        signaled.connect(self.script_status_label.show_ready_status)

    @property
    def script_config(self):
        return self.__script_config

    @script_config.setter
    def script_config(self, config):
        self.__script_config = config
        self.config_changed.emit(config)

    def edit_script_config(self):
        config_dialog = ScriptConfigDialog(self.__script_config)
        if config_dialog.exec():
            config = config_dialog.get_script_config()
            self.script_config = config

    def run_script(self):
        self.editor_pane.save_script()
        self.output_pane.run_script()
        self.script_status_label.show_run_status()

    def stop_script(self):
        self.output_pane.stop_script()
