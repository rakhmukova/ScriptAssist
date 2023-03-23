from PyQt6.QtWidgets import QDialog, QHBoxLayout, QPushButton


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

    def on_open_clicked(self):
        self.accept()

    def on_new_clicked(self):
        self.accept()
