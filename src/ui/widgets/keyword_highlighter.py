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
        self.__keywords = keywords
        self.__highlighting_rules = []

        # Set up highlighting rules for the keywords
        for keyword in self.__keywords:
            pattern = QRegularExpression("\\b" + keyword + "\\b")
            rule = (pattern, color)
            self.__highlighting_rules.append(rule)

    def highlightBlock(self, text: str):
        """
        Highlights the specified text block using the configured keywords and color.

        :param text: The text block to highlight.
        """

        # Apply the highlighting rules to the text block
        for rule, keyword_format in self.__highlighting_rules:
            match_iterator = rule.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                start_index = match.capturedStart()
                match_length = match.capturedLength()
                self.setFormat(start_index, match_length, keyword_format)
