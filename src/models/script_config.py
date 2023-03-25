import os

from PyQt6.QtCore import QObject, pyqtSignal


class ScriptConfig(QObject):
    EXTENSION_TO_SCRIPT_TYPE = {
        '': '',
        '.kts': 'Kotlin',
        '.swift': 'Swift',
    }

    path_changed = pyqtSignal(str)
    script_type_changed = pyqtSignal(str)
    parameters_changed = pyqtSignal(object)

    def __init__(self, path=None, parameters=None):
        super().__init__()
        if path is None:
            path = ''
        if parameters is None:
            parameters = []
        self._path = path
        self._script_type = self.define_script_type(path)
        self._parameters = parameters

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path
        self._script_type = self.define_script_type(new_path)
        self.path_changed.emit(new_path)
        self.script_type_changed.emit(self._script_type)

    @property
    def script_type(self):
        return self._script_type

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, new_parameters):
        self._parameters = new_parameters
        self.parameters_changed.emit(new_parameters)

    def define_script_type(self, path):
        _, ext = os.path.splitext(path)
        return self.EXTENSION_TO_SCRIPT_TYPE[ext]
