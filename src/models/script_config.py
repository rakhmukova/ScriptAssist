from PyQt6.QtCore import QObject


class ScriptConfig(QObject):
    def __init__(self, path, script_type, parameters=None):
        super().__init__()
        self.path = path
        self.script_type = script_type
        self.parameters = parameters
