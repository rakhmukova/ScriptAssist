from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, \
    QComboBox, QDialogButtonBox

from src.models.script_config import ScriptConfig


class ScriptConfigDialog(QDialog):
    def __init__(self, parent=None, to_open=True):
        super().__init__(parent)

        self.to_open = to_open

        self.setWindowTitle('Script Configuration')
        self.setFixedSize(600, 250)

        self.path_label = QLabel('Script path:')
        self.path_edit = QLineEdit()
        self.path_button = QPushButton('Browse')

        self.args_label = QLabel('Parameters:')
        self.args_edit = QLineEdit()

        self.script_type_label = QLabel('Script type:')
        self.script_type_combobox = QComboBox()
        self.script_type_combobox.addItems(['Swift', 'Kotlin'])

        self.path_button.clicked.connect(self.browse_path)

        layout = QVBoxLayout()

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(self.path_button)
        layout.addLayout(path_layout)

        args_layout = QHBoxLayout()
        args_layout.addWidget(self.args_label)
        args_layout.addWidget(self.args_edit)
        layout.addLayout(args_layout)

        script_type_layout = QHBoxLayout()
        script_type_layout.addWidget(self.script_type_label)
        script_type_layout.addWidget(self.script_type_combobox)
        layout.addLayout(script_type_layout)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def browse_path(self):
        script_type = self.script_type_combobox.currentText()
        extension_option = 'Kotlin Files (*.kts)' if script_type == 'Kotlin' else 'Swift Files (*.swift)'
        all_files_option = 'All Files (*)'
        if self.to_open:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Select File',
                                                       filter=f'{extension_option};;{all_files_option}')
        else:
            file_name, _ = QFileDialog.getSaveFileName(self, 'Select Path')

        if file_name:
            self.path_edit.setText(file_name)

    def get_script_config(self):
        return ScriptConfig(
            self.path_edit.text(),
            self.script_type_combobox.currentText(),
            self.args_edit.text() if self.args_edit.text() else None
        )
