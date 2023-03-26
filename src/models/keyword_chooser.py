class KeywordChooser:
    @staticmethod
    def get_keywords(script_type):
        if script_type == 'Swift':
            return ['let', 'var', 'if', 'in', 'else', 'switch', 'case', 'default',
                    'for', 'while', 'continue', 'break', 'return', 'func', 
                    'class', 'struct', 'enum', 'extension', 'protocol', 'init', 'deinit']
        elif script_type == 'Kotlin':
            return ['package', 'import', 'class', 'interface', 'fun', 'val',
                    'var', 'if', 'else', 'when', 'is', 'in', 'for', 'while',
                    'do', 'return', 'break', 'continue', 'throw', 'try', 'catch', 'finally']
        else:
            return []
