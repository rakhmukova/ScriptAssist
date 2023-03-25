from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPlainTextEdit

from src.models.keywords_chooser import KeywordChooser
from src.ui.widgets.keyword_highlighter import KeywordsHighlighter


class EditorPane(QPlainTextEdit):
    def __init__(self, start_config, parent=None):
        super().__init__(parent)
        self.current_config = None
        self.highlighter = None
        self.keyword_color = QColor(0, 0, 255)  # blue color
        self.setObjectName('editorPane')

        self.set_script_config(start_config)

    def set_script_config(self, script_config):
        self.current_config = script_config
        self.upload_from_config()
        keywords = KeywordChooser.get_keywords(self.current_config.script_type)
        self.highlighter = KeywordsHighlighter(keywords, self.keyword_color, self.document())

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
