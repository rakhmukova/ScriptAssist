from PyQt6.QtWidgets import QDialog, QHBoxLayout, QPushButton

from src.ui.dialogues.script_config_dialog import ScriptConfigDialog


class StartDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ScriptAssist')
        self.setFixedSize(300, 200)

        new_button = QPushButton('Create Script')
        open_button = QPushButton('Open')

        new_button.clicked.connect(self.on_new_clicked)
        open_button.clicked.connect(self.on_open_clicked)

        layout = QHBoxLayout()
        layout.addWidget(new_button)
        layout.addWidget(open_button)

        self.setLayout(layout)

        self.start_config = None

    def on_open_clicked(self):
        self.handle_choice(True)

    def on_new_clicked(self):
        self.handle_choice(False)

    def handle_choice(self, to_open):
        config_dialog = ScriptConfigDialog(to_open=to_open)
        if config_dialog.exec():
            self.accept()
            self.start_config = config_dialog.get_script_config()

    def get_script_config(self):
        return self.start_config
