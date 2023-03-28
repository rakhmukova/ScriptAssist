from models.script_type import ScriptType


class KeywordChooser:
    """
    A class that provides a list of commonly used keywords for a given script type.
    """
    @staticmethod
    def get_keywords(script_type: ScriptType) -> list:
        """
        Get a list of commonly used keywords for the given script type.

        :param script_type: A string representing the script type (either 'Swift' or 'Kotlin').
        :return: A list of commonly used keywords for the given script type.
        """
        if script_type == ScriptType.SWIFT:
            return ['let', 'var', 'if', 'in', 'else', 'switch', 'case', 'default',
                    'for', 'while', 'continue', 'break', 'return', 'func', 
                    'class', 'struct', 'enum', 'extension', 'protocol', 'init', 'deinit']
        elif script_type == ScriptType.UNDEFINED:
            return ['package', 'import', 'class', 'interface', 'fun', 'val',
                    'var', 'if', 'else', 'when', 'is', 'in', 'for', 'while',
                    'do', 'return', 'break', 'continue', 'throw', 'try', 'catch', 'finally']
        else:
            return []
