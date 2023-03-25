from PyQt6.QtWidgets import QPlainTextEdit


class EditorPane(QPlainTextEdit):
    def __init__(self, start_config, parent=None):
        super().__init__(parent)
        self.current_config = None
        self.setObjectName('editorPane')

        self.set_script_config(start_config)

    def set_script_config(self, script_config):
        self.current_config = script_config
        self.upload_from_config()

    def upload_from_config(self):
        self.clear()
        file_path = self.current_config.path
        with open(file_path, 'r') as f:
            script_content = f.read()

        self.appendPlainText(script_content)

    def save_script(self):
        file_path = self.current_config.path
        script_content = self.toPlainText()
        with open(file_path, 'w') as f:
            f.write(script_content)
