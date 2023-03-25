class KeywordChooser:
    @staticmethod
    def get_keywords(script_type):
        if script_type == 'Swift':
            return ['break', 'case', 'continue', 'default', 'do', 'else',
                    'fallthrough', 'if', 'return', 'switch']
        elif script_type == 'Kotlin':
            return ['as', 'break', 'class', 'continue',
                    'do', 'else', 'for', 'fun', 'if', 'in']
        else:
            return []
