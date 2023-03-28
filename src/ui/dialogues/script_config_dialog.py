from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QComboBox, QDialogButtonBox

from models.file_util import FileUtil
from models.script_config import ScriptConfig


class ScriptConfigDialog(QDialog):
    def __init__(self, script_config=None, parent=None, to_open=True):
        super().__init__(parent)

        self.to_open = to_open

        self.setWindowTitle('Script Configuration')
        self.setFixedSize(600, 250)

        self.script_type_label = QLabel('Script type:')
        self.script_type_label.setObjectName('scriptTypeLabel')
        self.script_type_combobox = QComboBox()
        self.script_type_combobox.addItems(['Swift', 'Kotlin'])
        self.script_type_combobox.currentIndexChanged.connect(self.script_type_changed)

        self.path_label = QLabel('Script path:')
        self.path_edit = QLineEdit()
        self.path_button = QPushButton('Browse')

        self.args_label = QLabel('Parameters:')
        self.args_edit = QLineEdit()

        self.path_button.clicked.connect(self.browse_path)

        layout = QVBoxLayout()

        script_type_layout = QHBoxLayout()
        script_type_layout.addWidget(self.script_type_label)
        script_type_layout.addWidget(self.script_type_combobox)
        script_type_layout.addStretch()
        layout.addLayout(script_type_layout)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(self.path_button)
        layout.addLayout(path_layout)

        args_layout = QHBoxLayout()
        args_layout.addWidget(self.args_label)
        args_layout.addWidget(self.args_edit)
        layout.addLayout(args_layout)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

        self.enable_accept_button(False)

        if script_config is not None:
            self.set_initial_values(script_config)

    def set_initial_values(self, current_config):
        self.path_edit.setText(current_config.path)
        parameters = ' '.join([str(param) for param in current_config.parameters])
        self.args_edit.setText(parameters)
        script_type = current_config.script_type
        index = self.script_type_combobox.findText(script_type)
        if index >= 0:
            self.script_type_combobox.setCurrentIndex(index)

        self.enable_accept_button(True)

    def browse_path(self):
        script_type = self.script_type_combobox.currentText()
        extension_option = 'Kotlin Files (*.kts)' if script_type == 'Kotlin' else 'Swift Files (*.swift)'
        if self.to_open:
            file_name = FileUtil.browse_file(self, extension_option)
        else:
            file_name = FileUtil.save_file(self, extension_option)

        if file_name:
            self.path_edit.setText(file_name)
            self.enable_accept_button(True)

    def script_type_changed(self):
        self.path_edit.clear()
        self.enable_accept_button(False)

    def get_script_config(self):
        path = self.path_edit.text()
        args = self.args_edit.text().split()
        return ScriptConfig(
            path,
            args
        )

    def enable_accept_button(self, to_enable):
        self.button_box.button(QDialogButtonBox.StandardButton.Ok).setEnabled(to_enable)
