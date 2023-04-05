from PyQt6.QtGui import QColor, QTextCursor
from PyQt6.QtWidgets import QPlainTextEdit, QWidget

from models.error_location import ErrorLocation
from models.file_util import FileUtil
from models.keyword_chooser import KeywordChooser
from models.script_config import ScriptConfig
from ui.widgets.keyword_highlighter import KeywordHighlighter


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

    def on_config_changed(self, script_config: ScriptConfig):
        """
        Sets the current script configuration and updates the editor content.

        :param script_config: The script configuration object.
        """
        self.__current_config = script_config
        keywords = KeywordChooser.get_keywords(self.__current_config.script_type)
        if self.__highlighter is None:
            self.__highlighter = KeywordHighlighter(keywords, self.__keyword_color, self.document())
        else:
            self.__highlighter.keywords = keywords
        self.__upload_from_config()

    def __upload_from_config(self):
        self.clear()
        file_path = self.__current_config.path
        script_content = FileUtil.upload_file(file_path)
        if script_content:
            self.appendPlainText(script_content)

    def move_cursor_to_error_location(self, error_location: ErrorLocation):
        """
        Moves the text cursor to the specified line and column in the text edit widget.
        """
        block = self.document().findBlockByLineNumber(error_location.line_number - 1)
        if not block.isValid():
            return

        cursor = QTextCursor(block)
        cursor.setPosition(block.position() + error_location.column_number - 1)
        self.setTextCursor(cursor)
        self.ensureCursorVisible()
        self.setFocus()
