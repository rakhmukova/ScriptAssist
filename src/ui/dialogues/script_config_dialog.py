from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QComboBox, QDialogButtonBox

from models.script_type import ScriptType
from src.models.file_util import FileUtil
from src.models.script_config import ScriptConfig


class ScriptConfigDialog(QDialog):
    _SCRIPT_TYPE_TO_EXTENSION_OPTION = {
        ScriptType.KOTLIN.value: 'Kotlin Files (*.kts)',
        ScriptType.SWIFT.value: 'Swift Files (*.swift)'
    }

    """
    A dialog window for configuring a script.
    """

    def __init__(self, script_config: ScriptConfig = None, parent: QDialog = None, to_open: bool = True):
        """
        Initialize the ScriptConfigDialog.

        :param script_config: (optional) a ScriptConfig object to use as the initial configuration.
        :param parent: (optional) the parent widget.
        :param to_open: (optional) a boolean indicating whether the dialog should allow
        the user to open a file or save a file.
        """

        super().__init__(parent)

        self.to_open = to_open

        self.__script_type_label = None
        self.__script_type_combobox = None

        self.__path_label = None
        self.__path_edit = None
        self.__path_button = None

        self.__args_label = None
        self.__args_edit = None

        self.__button_box = None

        self.setWindowTitle('Script Configuration')
        self.setFixedSize(600, 250)

        self.__create_widgets()
        self.__create_layout()
        self.__create_connections()

        self.__enable_accept_button(False)

        if script_config is not None:
            self.__set_initial_values(script_config)

    def get_script_config(self) -> ScriptConfig:
        """
        Get the ScriptConfig object representing the current configuration.

        :return: a ScriptConfig object.
        """

        path = self.__path_edit.text()
        args = self.__args_edit.text().split()
        return ScriptConfig(path, args)

    def __create_widgets(self):
        self.__script_type_label = QLabel('Script type:')
        self.__script_type_label.setObjectName('scriptTypeLabel')
        self.__script_type_combobox = QComboBox()
        script_types = [script_type.value for script_type in ScriptType
                        if script_type is not ScriptType.UNDEFINED]
        self.__script_type_combobox.addItems(script_types)

        self.__path_label = QLabel('Script path:')
        self.__path_edit = QLineEdit()
        self.__path_button = QPushButton('Browse')

        self.__args_label = QLabel('Parameters:')
        self.__args_edit = QLineEdit()

        self.__button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                                             | QDialogButtonBox.StandardButton.Cancel)

    def __create_layout(self):
        script_type_layout = QHBoxLayout()
        script_type_layout.addWidget(self.__script_type_label)
        script_type_layout.addWidget(self.__script_type_combobox)
        script_type_layout.addStretch()

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.__path_label)
        path_layout.addWidget(self.__path_edit)
        path_layout.addWidget(self.__path_button)

        args_layout = QHBoxLayout()
        args_layout.addWidget(self.__args_label)
        args_layout.addWidget(self.__args_edit)

        layout = QVBoxLayout()
        layout.addLayout(script_type_layout)
        layout.addLayout(path_layout)
        layout.addLayout(args_layout)
        layout.addWidget(self.__button_box)
        self.setLayout(layout)

    def __create_connections(self):
        self.__path_button.clicked.connect(self.__browse_path)
        self.__button_box.accepted.connect(self.accept)
        self.__button_box.rejected.connect(self.reject)
        self.__script_type_combobox.currentIndexChanged.connect(self.__script_type_changed)

    def __set_initial_values(self, current_config: ScriptConfig):
        self.__path_edit.setText(current_config.path)
        parameters = ' '.join(map(str, current_config.parameters))
        self.__args_edit.setText(parameters)
        index = self.__script_type_combobox.findText(current_config.script_type.value)
        if index >= 0:
            self.__script_type_combobox.setCurrentIndex(index)
        self.__enable_accept_button(True)

    def __browse_path(self):
        script_type = self.__script_type_combobox.currentText()
        extension_option = self._SCRIPT_TYPE_TO_EXTENSION_OPTION[script_type]
        if self.to_open:
            file_name = FileUtil.browse_file(self, extension_option)
        else:
            file_name = FileUtil.save_file(self, extension_option)
        if file_name:
            self.__path_edit.setText(file_name)
            self.__enable_accept_button(True)

    def __script_type_changed(self):
        self.__path_edit.clear()
        self.__enable_accept_button(False)

    def __enable_accept_button(self, to_enable: bool):
        self.__button_box.button(QDialogButtonBox.StandardButton.Ok).setEnabled(to_enable)
