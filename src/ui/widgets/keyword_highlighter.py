from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat


class KeywordHighlighter(QSyntaxHighlighter):
    def __init__(self, keywords, color, parent=None):
        super().__init__(parent)
        self.keywords = keywords
        self.highlighting_rules = []
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(color)

        self.highlighting_rules = [(QRegularExpression('\\b' + keyword + '\\b'), keyword_format)
                                   for keyword in keywords]

    def highlightBlock(self, text):
        if not text:
            return
        for rule, keyword_format in self.highlighting_rules:
            pattern = QRegularExpression(rule.pattern())
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                start_index = match.capturedStart()
                match_length = match.capturedLength()
                self.setFormat(start_index, match_length, keyword_format)
