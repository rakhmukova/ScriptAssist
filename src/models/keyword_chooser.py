from models.script_type import ScriptType


class KeywordChooser:
    """
    A class that provides a list of commonly used keywords for a given script type.
    """
    __KEYWORDS = {
        ScriptType.SWIFT: [
            'let', 'var', 'if', 'in', 'else', 'switch', 'case', 'default',
            'for', 'while', 'continue', 'break', 'return', 'func',
            'class', 'struct', 'enum', 'extension', 'protocol', 'init', 'deinit'
        ],
        ScriptType.KOTLIN: [
            'package', 'import', 'class', 'interface', 'fun', 'val',
            'var', 'if', 'else', 'when', 'is', 'in', 'for', 'while',
            'do', 'return', 'break', 'continue', 'throw', 'try', 'catch', 'finally'
        ],
    }

    @staticmethod
    def get_keywords(script_type: ScriptType) -> list[str]:
        """
        Get a list of commonly used keywords for the given script type.

        :param script_type: A ScriptType representing the script type.
        :return: A list of commonly used keywords for the given script type.
        """
        return KeywordChooser.__KEYWORDS.get(script_type, [])
