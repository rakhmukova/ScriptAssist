from PyQt6.QtWidgets import QDialog, QHBoxLayout, QPushButton

from models.script_config import ScriptConfig
from ui.dialogues.script_config_dialog import ScriptConfigDialog


class StartDialog(QDialog):
    """
    A dialog window to choose between creating a new script or opening an existing one.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ScriptAssist')
        self.setFixedSize(300, 200)

        self.__new_button = QPushButton('Create Script')
        self.__open_button = QPushButton('Open')

        self.__new_button.clicked.connect(self.__on_new_clicked)
        self.__open_button.clicked.connect(self.__on_open_clicked)

        layout = QHBoxLayout()
        layout.addWidget(self.__new_button)
        layout.addWidget(self.__open_button)

        self.setLayout(layout)

        self.__script_config = None

    def __on_open_clicked(self):
        self.__handle_choice(True)

    def __on_new_clicked(self):
        self.__handle_choice(False)

    def __handle_choice(self, to_open: bool):
        """
        Show the script configuration dialog for opening an existing script or creating a new one.

        :param to_open: a boolean indicating whether the user wants to open an existing script or create a new one.
        """

        config_dialog = ScriptConfigDialog(script_config=self.__script_config, to_open=to_open)
        config_dialog.script_config_changed.connect(self.__on_config_changed)
        if config_dialog.exec() == QDialog.DialogCode.Accepted:
            self.accept()

    def __on_config_changed(self, script_config: ScriptConfig):
        self.__script_config = script_config

    @property
    def script_config(self):
        """
        Get the script configuration object.

        :return: a ScriptConfig object representing the script configuration.
        """

        return self.__script_config
