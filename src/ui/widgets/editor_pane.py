from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPlainTextEdit, QWidget

from src.models.file_util import FileUtil
from src.models.keyword_chooser import KeywordChooser
from src.models.script_config import ScriptConfig
from src.ui.widgets.keyword_highlighter import KeywordHighlighter


class EditorPane(QPlainTextEdit):
    """
    A custom QPlainTextEdit widget for editing scripts.
    """
    def __init__(self, parent: QWidget = None):
        """
        Initializes an instance of the EditorPane.

        :param parent: Parent widget, defaults to None.
        """
        super().__init__(parent)
        self.__current_config = None
        self.__highlighter = None
        self.__keyword_color = QColor(0, 0, 255)  # blue color
        self.setObjectName('editorPane')

    def set_script_config(self, script_config: ScriptConfig):
        """
        Sets the current script configuration and updates the editor content.

        :param script_config: The script configuration object.
        """
        self.__current_config = script_config
        self.__upload_from_config()
        keywords = KeywordChooser.get_keywords(self.__current_config.script_type)
        self.__highlighter = KeywordHighlighter(keywords, self.__keyword_color, self.document())

    def __upload_from_config(self):
        self.clear()
        file_path = self.__current_config.path
        script_content = FileUtil.upload_file(file_path)
        if script_content:
            self.appendPlainText(script_content)

    def save_script(self):
        """
        Saves the editor content to the current script file.
        """
        file_path = self.__current_config.path
        script_content = self.toPlainText()
        FileUtil.save_to_file(file_path, script_content)
