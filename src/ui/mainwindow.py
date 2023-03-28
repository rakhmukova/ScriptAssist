from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from models.script_config import ScriptConfig
from ui.dialogues.script_config_dialog import ScriptConfigDialog
from ui.widgets.editor_pane import EditorPane
from ui.widgets.line_number_area import LineNumberArea
from ui.widgets.output_pane import OutputPane
from ui.widgets.script_status_label import ScriptStatusLabel
from ui.widgets.top_panel import TopPanel


class MainWindow(QMainWindow):
    config_changed = pyqtSignal(object)

    def __init__(self, start_config: ScriptConfig):
        """
        Constructor for the main window of the ScriptAssist application.

        :param start_config: The configuration of the script to be loaded on startup.
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

        self.__top_panel = TopPanel()
        self.__top_panel.run_button.clicked.connect(self.__run_script)
        self.__top_panel.stop_button.clicked.connect(self.__stop_script)
        self.__top_panel.edit_config_button.clicked.connect(self.__edit_script_config)

        self.__editor_pane = EditorPane()

        self.__line_number_area = LineNumberArea(self.__editor_pane)
        self.__line_number_area.setFixedWidth(50)
        self.__editor_pane.blockCountChanged.connect(self.__line_number_area.update_line_numbers)
        self.__editor_pane.verticalScrollBar().valueChanged.connect(self.__line_number_area.update_scrollbar)

        self.__script_status_label = ScriptStatusLabel()
        self.__script_status_label.setObjectName('scriptStatusLabel')
        self.__script_status_label.setFixedHeight(25)

        self.__output_pane = OutputPane()
        self.__output_pane.script_finished.connect(self.__script_status_label.show_finish_status)

        self.__create_layout(layout)

        self.__run_action = None
        self.__stop_action = None
        self.__edit_config_action = None
        self.__create_actions()

        self.__subscribe_to_config_change()
        self.script_config = start_config

    def __create_layout(self, layout: QVBoxLayout):
        editor_layout = QHBoxLayout()
        editor_layout.setSpacing(0)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.addWidget(self.__line_number_area)
        editor_layout.addWidget(self.__editor_pane)

        layout.addWidget(self.__top_panel)
        layout.addLayout(editor_layout, stretch=2)
        layout.addWidget(self.__script_status_label)
        layout.addWidget(self.__output_pane, stretch=1)

    def __create_actions(self):
        self.__run_action = QAction('Run', self)
        self.__run_action.setShortcut('Ctrl+R')
        self.__run_action.triggered.connect(self.__run_script)
        self.addAction(self.__run_action)

        self.__stop_action = QAction('Stop', self)
        self.__stop_action.setShortcut('Ctrl+T')
        self.__stop_action.triggered.connect(self.__stop_script)
        self.addAction(self.__stop_action)

        self.__edit_config_action = QAction('Edit configuration', self)
        self.__edit_config_action.setShortcut('Ctrl+E')
        self.__edit_config_action.triggered.connect(self.__edit_script_config)
        self.addAction(self.__edit_config_action)

    def __subscribe_to_config_change(self):
        signaled = self.config_changed
        signaled.connect(self.__editor_pane.on_config_changed)
        signaled.connect(self.__output_pane.on_config_changed)
        signaled.connect(self.__top_panel.on_config_changed)
        signaled.connect(self.__script_status_label.show_ready_status)

    @property
    def script_config(self):
        return self.__script_config

    @script_config.setter
    def script_config(self, config):
        self.__script_config = config
        self.config_changed.emit(config)

    def __edit_script_config(self):
        config_dialog = ScriptConfigDialog(self.script_config)
        if config_dialog.exec():
            config = config_dialog.get_script_config()
            self.script_config = config

    def __run_script(self):
        self.__editor_pane.save_script()
        self.__output_pane.run_script()
        self.__script_status_label.show_run_status()

    def __stop_script(self):
        self.__output_pane.stop_script()
