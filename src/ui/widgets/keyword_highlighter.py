from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QColor


class KeywordHighlighter(QSyntaxHighlighter):
    """
    A syntax highlighter for highlighting language keywords in a text block.
    """

    def __init__(self, keywords: list, color: QColor, parent=None):
        """
        Initializes the keyword highlighter with the specified keywords and text color.

        :param keywords: A list of keywords to highlight.
        :param color: The text color for highlighting the keywords.
        :param parent: The parent object of the highlighter.
        """
        super().__init__(parent)
        self.__color = color
        self.keywords = keywords

    @property
    def keywords(self) -> list[str]:
        """
        Returns the list of keywords used for highlighting in the syntax highlighter.

        :return: A list of strings representing the keywords.
        """
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: list[str]):
        """
        Sets the list of keywords used for highlighting in the syntax highlighter.

        :param keywords: A list of strings representing the keywords.
        """
        self.__keywords = keywords
        self.__highlighting_rules = []
        self.__setup_highlighting_rules()

    def __setup_highlighting_rules(self):
        for keyword in self.__keywords:
            pattern = QRegularExpression("\\b" + keyword + "\\b")
            rule = (pattern, self.__color)
            self.__highlighting_rules.append(rule)

    def highlightBlock(self, text: str):
        """
        Highlights the specified text block using the configured keywords and color.

        :param text: The text block to highlight.
        """
        for rule, keyword_format in self.__highlighting_rules:
            match_iterator = rule.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                start_index = match.capturedStart()
                match_length = match.capturedLength()
                self.setFormat(start_index, match_length, keyword_format)
